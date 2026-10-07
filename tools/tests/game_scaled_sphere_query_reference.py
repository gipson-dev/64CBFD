"""Independent scaled-caller arithmetic and evolving memory for bounded probes.

Private helper prologues/return-address stores are not an acceptance surface of
this reference. Call-boundary snapshots cover initialized caller locals and
incoming homes, not a complete private frame or instruction-read schedule.
"""

import math

from tools.tests import game_sphere_frame_reference as sphere
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_projection_lifetime_recovery import put, peek
from tools.tests.test_game_table_range_loader import STACK

DIMENSION, NORMALIZE, WRAPPER, CALLEE, DOT = 0x1515C1A0, 0x15145128, 0x151451F0, 0x151452C4, 0x15144A74


def private(address):
    return STACK - 0x600 <= address < STACK + 0x100


def external(memory):
    return {a: b for a, b in memory.items() if not private(a)}


def snapshot(memory, target, frame):
    offsets = range(0x38, 0x88, 4)
    return target, tuple(peek(memory, frame + offset) for offset in offsets), tuple(
        peek(memory, frame + 0x88 + i * 4) for i in range(8))


def reference(memory, args, phase=0, snapshots=None, caller_saves=None):
    memory, writes, calls = memory.copy(), [], []
    entry, frame = STACK + phase, STACK + phase - 0x88
    origin, direction, actor, point0, point1, radius, height, center = args
    if caller_saves is not None:
        put(memory, frame + 0x34, caller_saves[1])
        put(memory, frame + 0x30, caller_saves[0])
    for i, word in enumerate(args):
        put(memory, entry + i * 4, word)

    def word(address):
        return peek(memory, address)

    def read(address):
        return floating(word(address))

    def rnd(value):
        return floating(bits(value))

    def multiply(a, b):
        return rnd(a * b)

    def add(a, b):
        return rnd(a + b)

    def store_word(address, value):
        put(memory, address, value)
        if not private(address):
            writes.append(('W', address, 4, value))

    def store(address, value):
        store_word(address, bits(value))

    def half(offset):
        value = peek(memory, actor + offset, 2)
        return value if value < 0x8000 else value - 0x10000

    radius = frame + 0x78 if radius else 0
    height = frame + 0x74 if height else 0
    center = frame + 0x7C if center else 0
    put(memory, entry + 0x14, radius)
    put(memory, entry + 0x18, height)
    calls.append((DIMENSION, actor, center, radius, height))
    special = memory[actor + 4] < 0xBB
    store(radius, float(half(0xD2)) if special else 1.0)
    store(height, float(half(0xD4)) if special else 1.0)
    store_word(center, word(actor + 0x14))
    if special:
        store(center + 4, add(read(actor + 0x18), float(half(0xD6))))
    else:
        store_word(center + 4, word(actor + 0x18))
    store_word(center + 8, word(actor + 0x1C))
    if read(height) == 0.0 or read(radius) == 0.0:
        return memory, writes, 0, calls

    inverse, scale = read(actor + 0xE0), read(actor + 0xDC)
    store(frame + 0x3C, inverse)
    for source, target in ((origin, frame + 0x68), (direction, frame + 0x5C)):
        store_word(target, word(source))
        store(target + 4, multiply(read(source + 4), scale))
        store_word(target + 8, word(source + 8))
    store(frame + 0x40, scale)
    local_direction = frame + 0x5C
    calls.append((NORMALIZE, local_direction, local_direction, frame + 0x4C, frame + 0x38))
    if snapshots is not None:
        snapshots.append(snapshot(memory, NORMALIZE, frame))
    squares = [multiply(read(local_direction + i * 4), read(local_direction + i * 4)) for i in range(3)]
    length_squared = add(add(squares[0], squares[1]), squares[2])
    if length_squared == 0.0:
        return memory, writes, 0, calls
    store(frame + 0x4C, rnd(math.sqrt(length_squared)))
    store(frame + 0x38, rnd(1.0 / read(frame + 0x4C)))
    for i in range(3):
        store(local_direction + i * 4, multiply(read(frame + 0x38), read(local_direction + i * 4)))
    scale = read(frame + 0x40)
    store_word(frame + 0x50, word(center))
    store(frame + 0x54, multiply(read(center + 4), scale))
    store_word(frame + 0x58, word(center + 8))
    wrapper_args = (frame + 0x68, local_direction, frame + 0x50, word(radius), word(frame + 0x4C),
                    word(entry + 0xC), word(entry + 0x10), frame + 0x48, frame + 0x44)
    calls.append((WRAPPER, *wrapper_args))
    for i, value in enumerate(wrapper_args[4:]):
        put(memory, frame + 0x10 + i * 4, value)
    if snapshots is not None:
        snapshots.append(snapshot(memory, WRAPPER, frame))
    helper_args = (*wrapper_args[:4], *wrapper_args[5:])
    calls.append((CALLEE, *helper_args))
    memory, helper_writes, status, dot = sphere.reference(memory, helper_args, phase - 0x88 - 0x28)
    writes.extend(e for e in helper_writes if not private(e[1]))
    if dot is not None:
        calls.append((DOT, *dot))
    if not status:
        return memory, writes, 0, calls
    first, second = read(frame + 0x48), read(frame + 0x44)
    if first < 0.0 and second < 0.0:
        return memory, writes, 0, calls
    if not (first >= 0.0 and second < 0.0) and not first < read(frame + 0x10):
        return memory, writes, 0, calls
    point1, point0 = word(entry + 0x10), word(entry + 0xC)
    inverse = read(frame + 0x3C)
    store(point0 + 4, multiply(read(point0 + 4), inverse))
    store(point1 + 4, multiply(read(point1 + 4), inverse))
    return memory, writes, 1, calls
