"""Independent rounded-float memory model for bounded eight-argument probes."""

import math
from dataclasses import dataclass

from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_projection_lifetime_recovery import put, peek
from tools.tests.test_game_table_range_loader import STACK


@dataclass(frozen=True)
class Layout:
    direction: int
    origin: int
    relative: int


RETAIL = Layout(0x58, 0x4C, 0x28)
TRIAL = Layout(0x64, 0x58, 0x4C)


def reference(memory, args, phase=0, layout=RETAIL):
    memory = memory.copy()
    origin, direction, center, radius, point0, point1, distance0, distance1 = args
    entry, frame = STACK + phase, STACK + phase - 0x70
    for i, value in enumerate(args[4:]):
        put(memory, entry + 0x10 + i * 4, value)
    writes = []

    def store_word(address, value):
        put(memory, address, value)
        writes.append(('W', address, 4, value))

    def read(address):
        return floating(peek(memory, address))

    def rounded(value):
        return floating(bits(value))

    def multiply(a, b):
        return rounded(a * b)

    def add(a, b):
        return rounded(a + b)

    def store(address, value):
        store_word(address, bits(value))

    store_word(entry + 0xC, radius)
    store_word(frame + 0x14, 0xDEAD0000)
    store_word(entry, origin)
    delta = [rounded(read(center + i * 4) - read(origin + i * 4)) for i in range(3)]
    for source, target in ((direction, frame + layout.direction), (origin, frame + layout.origin)):
        for i in range(3):
            store_word(target + i * 4, peek(memory, source + i * 4))
    products = [multiply(delta[i], read(frame + layout.direction + i * 4)) for i in range(3)]
    projection = add(add(products[0], products[1]), products[2])
    radius_squared = multiply(read(entry + 0xC), read(entry + 0xC))
    squares = [multiply(value, value) for value in delta]
    perpendicular = rounded(add(add(squares[0], squares[1]), squares[2]) - multiply(projection, projection))
    store(frame + 0x1C, perpendicular)
    if radius_squared < read(frame + 0x1C):
        return memory, writes, 0, None
    root = rounded(math.sqrt(rounded(radius_squared - read(frame + 0x1C))))
    if projection < root:
        root = -root
    first, second = rounded(projection - root), add(projection, root)
    # Both point pointers precede output writes; scalar pointers are late reloads.
    point0, point1 = peek(memory, entry + 0x10), peek(memory, entry + 0x14)
    for point, scalar, home in ((point0, first, 0x18), (point1, second, 0x1C)):
        for i in range(3):
            value = add(multiply(scalar, read(frame + layout.direction + i * 4)),
                        read(frame + layout.origin + i * 4))
            store(point + i * 4, value)
        store(peek(memory, entry + home), scalar)
    for i in range(3):
        store(frame + layout.relative + i * 4, rounded(read(point0 + i * 4) - read(origin + i * 4)))
    products = [multiply(read(frame + layout.relative + i * 4), read(direction + i * 4)) for i in range(3)]
    status = int(not add(add(products[0], products[1]), products[2]) < 0.0)
    return memory, writes, status, (frame + layout.relative, direction)
