"""Bounded low-word retail instruction oracle, not a MIPS/FCSR emulator."""

import math
import re
import struct
from pathlib import Path


def bits(value):
    try:
        return struct.unpack(">I", struct.pack(">f", value))[0]
    except OverflowError:
        return bits(math.copysign(math.inf, value))


def floating(word):
    return struct.unpack(">f", struct.pack(">I", word))[0]


def signed(word):
    return word if word < 0x80000000 else word - 0x100000000


class TimelineOracle:
    STATE = 0x20000
    STACK = 0x40000
    ACTORS = 0x800CC2D0
    ACTOR = ACTORS + 2 * 0x32C
    CALLBACK = 0x151FFFF0
    HELPER = 0x1506AD30
    TIME = 0x800BE9A4
    TICKS = 0x800BE9E4
    FREEZE = 0x800BEA0C
    MODES = 0x800C35EA
    ENABLE = 0x800C365E
    SLOT = 0x800C3E78
    CURRENT = 0x800D154C

    def __init__(self, case):
        source = (Path(__file__).resolve().parents[2] / "conker/asm/A9260.s").read_text()
        source = source.split("glabel func_1507BDB0\n", 1)[1].split("endlabel func_1507BDB0", 1)[0]
        self.code = {int(address, 16): int(word, 16) for address, word in re.findall(
            r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+([0-9A-Fa-f]{8})\s*\*/", source)}
        self.case = case
        self.memory = {self.STATE + i: 0xA5 for i in range(0x40)}
        self.memory.update({self.ACTOR + i: 0xA5 for i in range(0x32C)})
        self.memory.update({self.STACK - 0x40 + i: 0xA5 for i in range(0x80)})
        self.r = [0x5A000000 + i for i in range(32)]
        self.r[0] = 0
        self.r[4:8] = [self.STATE, bits(case.get("step", 1.0)),
                       self.ACTOR if case.get("actor", True) else 0, case.get("mode", 0)]
        self.r[29], self.r[31] = self.STACK, 0xDEAD0000
        self.before = self.r[:]
        self.f = [0] * 32
        self.condition = False
        self.lo = 0
        self.events = []
        self.writes = []
        self.visits = set()
        self.put(self.STATE, self.CALLBACK if case.get("callback", False) else 0, 4)
        self.put(self.STATE + 4, case.get("flags", 0), 2)
        for offset, name, default in ((8, "frame", 2.0), (0x10, "rate", 1.0),
                                      (0x18, "end", 10.0), (0x20, "start", 1.0)):
            self.put(self.STATE + offset, bits(case.get(name, default)), 4)
        self.put(self.STATE + 0x28, case.get("sequence", 1), 4)
        self.put(self.STATE + 0x3A, case.get("decrement", 1), 2)
        self.put(self.STATE + 0x3C, case.get("timer", 0), 2)
        self.put(self.ACTOR + 0xF4, case.get("actor_flags", 0), 4)
        self.put(self.ACTOR + 0x1FC, case.get("actor_bits", 0xA5), 1)
        self.put(self.ACTOR + 0x1FD, case.get("turn", 0), 1)
        self.put(self.ACTOR + 0x76, case.get("angle", 0xFF80), 2)
        self.put(self.TIME, bits(case.get("time", 1.0)), 4)
        self.put(self.TICKS, case.get("ticks", 1), 4)
        self.put(self.FREEZE, case.get("freeze", 0), 1)
        for i in range(4):
            self.put(self.MODES + i, case.get("modes", [0] * 4)[i], 1)
            self.put(self.ENABLE + i, case.get("enable", [0] * 4)[i], 1)
        self.put(self.SLOT, 0xAA, 1)
        self.put(self.CURRENT, self.ACTORS, 4)

    def put(self, address, value, size):
        data = (value & ((1 << (size * 8)) - 1)).to_bytes(size, "big")
        self.memory.update({address + i: byte for i, byte in enumerate(data)})

    def get(self, address, size):
        return int.from_bytes(bytes(self.memory[address + i] for i in range(size)), "big")

    def mutate(self, callback):
        mutation = self.case.get("mutation", 0)
        if callback and mutation == 1:
            self.put(self.STATE + 0x28, 2, 4)
            self.put(self.STATE + 8, bits(4.5), 4)
            self.put(self.STATE + 0x18, bits(20.0), 4)
        if callback and mutation == 2:
            self.put(self.STATE + 0x18, bits(5.0), 4)
            self.put(self.STATE + 4, 0, 2)
            self.put(self.ACTOR + 0xF4, 0, 4)
        if not callback and mutation == 3:
            self.put(self.STATE + 0x10, bits(-1.0), 4)
            self.put(self.STATE + 0x18, bits(20.0), 4)
        if not callback and mutation == 4 and sum(e[0] == 0 for e in self.events) == 2:
            self.put(self.STATE + 8, bits(6.25), 4)
        if callback and mutation == 5:
            self.put(self.CURRENT, self.ACTORS + 0x32C, 4)
        if callback and mutation == 6:
            self.put(self.STATE + 0x28, 0, 4)
            self.put(self.STATE + 8, bits(4.5), 4)

    def hook(self, target):
        callback = target == self.CALLBACK
        if target not in (self.CALLBACK, self.HELPER):
            raise AssertionError("Unknown external call %08X" % target)
        if callback:
            self.events.append((1, 0, 0, 0))
            result = 0
        else:
            index = sum(e[0] == 0 for e in self.events)
            self.events.append((0, self.r[4], self.r[5], self.r[6]))
            result = bits(self.case.get("results", [0.0, 0.0])[index])
        self.mutate(callback)
        for i in (2, 3, *range(4, 16), 24, 25):
            self.r[i] = 0xA5000000 + i
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.f[0] = result

    def execute(self, word):
        op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
        rd, shift, fn = (word >> 11) & 31, (word >> 6) & 31, word & 63
        imm = word & 0xFFFF
        simm = imm if imm < 0x8000 else imm - 0x10000
        address = (self.r[rs] + simm) & 0xFFFFFFFF
        if word == 0:
            pass
        elif op == 15:
            self.r[rt] = imm << 16
        elif op in (9, 12, 13):
            self.r[rt] = {9: lambda: self.r[rs] + simm,
                          12: lambda: self.r[rs] & imm,
                          13: lambda: self.r[rs] | imm}[op]()
        elif op in (33, 35, 36, 37, 49):
            size = {33: 2, 35: 4, 36: 1, 37: 2, 49: 4}[op]
            value = self.get(address, size)
            if op == 33 and value & 0x8000:
                value -= 0x10000
            if op == 49:
                self.f[rt] = value
            else:
                self.r[rt] = value
        elif op in (40, 41, 43, 57):
            size = {40: 1, 41: 2, 43: 4, 57: 4}[op]
            self.put(address, self.f[rt] if op == 57 else self.r[rt], size)
            self.writes.append((address, size))
        elif op == 0 and fn in (0, 18, 25, 26, 33, 35, 37):
            if fn == 0:
                self.r[rd] = self.r[rt] << shift
            elif fn == 18:
                self.r[rd] = self.lo
            elif fn == 25:
                self.lo = (self.r[rs] * self.r[rt]) & 0xFFFFFFFF
            elif fn == 26:
                left, right = signed(self.r[rs]), signed(self.r[rt])
                self.lo = ((abs(left) // abs(right)) * (-1 if (left < 0) != (right < 0) else 1)) & 0xFFFFFFFF
            else:
                self.r[rd] = {33: lambda: self.r[rs] + self.r[rt],
                              35: lambda: self.r[rs] - self.r[rt],
                              37: lambda: self.r[rs] | self.r[rt]}[fn]()
        elif op == 17 and rs in (0, 4, 16):
            if rs == 0:
                self.r[rt] = self.f[rd]
            elif rs == 4:
                self.f[rd] = self.r[rt]
            else:
                left, right = floating(self.f[rd]), floating(self.f[rt])
                if fn in (50, 60, 62):
                    self.condition = {50: lambda: left == right, 60: lambda: left < right,
                                      62: lambda: left <= right}[fn]()
                elif fn in (0, 1, 2, 6):
                    self.f[shift] = self.f[rd] if fn == 6 else bits(
                        {0: lambda: left + right, 1: lambda: left - right,
                         2: lambda: left * right}[fn]())
                else:
                    raise AssertionError("Unsupported FPU function %d" % fn)
        else:
            raise AssertionError("Unsupported word %08X" % word)
        self.r[:] = [value & 0xFFFFFFFF for value in self.r]
        self.r[0] = 0

    def run(self):
        pc = 0x1507BDB0
        for _ in range(1000):
            self.visits.add(pc)
            word = self.code[pc]
            op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
            imm = word & 0xFFFF
            offset = imm if imm < 0x8000 else imm - 0x10000
            if op in (4, 5, 6, 20, 21) or (op == 17 and rs == 8):
                if op == 17:
                    take, likely = self.condition == bool(rt & 1), bool(rt & 2)
                else:
                    take = signed(self.r[rs]) <= 0 if op == 6 else self.r[rs] == self.r[rt]
                    if op in (5, 21): take = not take
                    likely = op in (20, 21)
                if take or not likely: self.execute(self.code[pc + 4])
                pc = pc + 4 + offset * 4 if take else pc + 8
            elif op == 3 or (op == 0 and word & 63 in (8, 9)):
                target = (((pc + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2)
                          if op == 3 else self.r[rs])
                call = op == 3 or word & 63 == 9
                if call: self.r[31] = pc + 8
                self.execute(self.code[pc + 4])
                if target == 0xDEAD0000:
                    for i in (*range(16, 24), 28, 29, 30, 31):
                        assert self.r[i] == self.before[i], (i, self.r[i], self.before[i])
                    return self
                if call:
                    self.hook(target)
                    pc += 8
                else:
                    pc = target
            else:
                self.execute(word)
                pc += 4
        raise AssertionError("Timeline instruction budget exhausted")
