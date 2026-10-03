import struct

from tools.tests.test_init_decompressor_tables import BuilderFixture


class GuestImage:
    def __init__(self, data):
        if len(data) < 52 or data[:6] != b"\x7fELF\x01\x02":
            raise ValueError("expected a big-endian ELF32 executable")
        header = struct.unpack_from(">16sHHIIIIIHHHHHH", data)
        if header[1:3] != (2, 8) or header[11] != 40:
            raise ValueError("expected a linked ELF32 MIPS executable")

        def chunk(offset, size):
            if offset < 0 or size < 0 or offset + size > len(data):
                raise ValueError("ELF range exceeds file")
            return data[offset:offset + size]

        raw_sections = chunk(header[6], header[12] * 40)
        sections = list(struct.iter_unpack(">10I", raw_sections))
        self.memory, self.code, self.symbols, self.readonly = {}, {}, {}, []
        for section in sections:
            _, kind, flags, address, offset, size, link, _, _, stride = section
            if flags & 2:
                payload = bytes(size) if kind == 8 else chunk(offset, size)
                if any(address + index in self.memory for index in range(size)):
                    raise ValueError("overlapping allocated ELF sections")
                self.memory.update((address + index, value) for index, value in enumerate(payload))
                if not flags & 1:
                    self.readonly.append((address, address + size))
                if flags & 4:
                    if address & 3 or size & 3:
                        raise ValueError("executable section is not word aligned")
                    self.code.update((address + index * 4, word[0]) for index, word in
                                     enumerate(struct.iter_unpack(">I", payload)))
            if kind == 2:
                if stride != 16 or size % 16 or link >= len(sections):
                    raise ValueError("invalid ELF symbol table")
                strings = chunk(sections[link][4], sections[link][5])
                for symbol in struct.iter_unpack(">IIIBBH", chunk(offset, size)):
                    first, value, _, _, _, owner = symbol
                    if first >= len(strings):
                        raise ValueError("invalid ELF symbol name")
                    end = strings.find(b"\0", first)
                    if end < 0:
                        raise ValueError("unterminated ELF symbol name")
                    if owner:
                        self.symbols[strings[first:end].decode("ascii")] = value
            if kind in (4, 9) and size:
                raise ValueError("linked guest image retains relocations")
        self.entry = self.symbols.get("init_decode_build")
        if self.entry != header[4] or self.entry not in self.code:
            raise ValueError("builder entry differs from linked executable entry")


class GuestBuilderFixture(BuilderFixture):
    STATE = 0x40000
    FRAME = 0x50000

    def __init__(self, image, lengths, bits=7, simple=None, allocated=0,
                 bases=(), extras=()):
        self.readonly, self.allowed_writes = [], None
        super().__init__(lengths, bits=bits, simple=simple, allocated=allocated,
                         bases=bases, extras=extras)
        self.image = image
        self.code = image.code
        self.memory.update(image.memory)
        for first, last in ((self.STACK - 4096, self.STACK + 64),
                            (self.FRAME - 16, self.FRAME + 0xA88 + 16),
                            (self.WORKSPACE, self.WORKSPACE + 0x10000)):
            self.memory.update((address, 0xA5) for address in range(first, last))
        state = (0, 0, self.WORKSPACE, 0, 0, 0, 0, allocated,
                 self.FRAME, self.WORKSPACE)
        for index, value in enumerate(state):
            self.put(self.STATE + index * 4, value, 4)
        for offset, value in ((16, self.BASES), (20, self.EXTRAS),
                              (24, self.ROOT), (28, self.BITS)):
            self.put(self.STACK + offset, value, 4)
        self.registers[4:8] = [self.STATE, self.LENGTHS, len(lengths),
                               len(lengths) if simple is None else simple]
        self.before = self.registers[:]
        self.min_sp = self.STACK
        self.readonly = list(image.readonly)
        self.allowed_writes = [(self.STACK - 4096, self.STACK + 64),
                               (self.STATE, self.STATE + 40),
                               (self.FRAME, self.FRAME + 0xA88),
                               (self.WORKSPACE, self.WORKSPACE + 0x10000),
                               (self.ROOT, self.ROOT + 2), (self.BITS, self.BITS + 4)]
        self.writes.clear()

    def put(self, address, value, size):
        if any(address < last and address + size > first for first, last in self.readonly):
            raise AssertionError("guest write overlaps read-only image")
        if self.allowed_writes is not None and not any(
                first <= address and address + size <= last for first, last in self.allowed_writes):
            raise AssertionError("guest write exceeds caller-owned buffers")
        super().put(address, value, size)

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        rd, fn, immediate = word >> 11 & 31, word & 63, word & 0xFFFF
        signed = immediate if immediate < 0x8000 else immediate - 0x10000
        if op == 11:
            self.registers[rt] = int(self.registers[rs] < (signed & 0xFFFFFFFF))
        elif op == 14:
            self.registers[rt] = self.registers[rs] ^ immediate
        elif op == 0 and fn == 43:
            self.registers[rd] = int(self.registers[rs] < self.registers[rt])
        elif op == 0 and fn == 3:
            self.registers[rd] = (self.signed(self.registers[rt]) >> (word >> 6 & 31)) & 0xFFFFFFFF
        elif op in (42, 46):
            address = (self.registers[rs] + signed) & 0xFFFFFFFF
            offset = address & 3
            if op == 42:
                size = 4 - offset
                self.put(address, self.registers[rt] >> (offset * 8), size)
            else:
                size = offset + 1
                address &= ~3
                self.put(address, self.registers[rt], size)
            self.writes.append((address, size))
        else:
            super().execute(word)
        self.registers[0] = 0
        self.min_sp = min(self.min_sp, self.registers[29])

    def run(self, budget=200000, entry=None, stop_pc=None):
        pc = self.image.entry if entry is None else entry
        for _ in range(budget):
            if pc == stop_pc:
                return self.registers[2]
            if pc in self.capture:
                self.snapshots[pc] = (self.registers[:], self.fprs[:])
            self.visits[pc] = self.visits.get(pc, 0) + 1
            word = self.code[pc]
            op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
            if op in (1, 4, 5, 6, 7, 20, 21, 22, 23):
                if op == 1:
                    if rt not in (0, 1, 2, 3):
                        raise AssertionError("unsupported guest REGIMM branch")
                    negative = self.signed(self.registers[rs]) < 0
                    taken = negative if rt in (0, 2) else not negative
                    likely = rt in (2, 3)
                elif op in (4, 5, 20, 21):
                    taken = self.registers[rs] == self.registers[rt]
                    if op in (5, 21):
                        taken = not taken
                    likely = op in (20, 21)
                else:
                    value = self.signed(self.registers[rs])
                    taken = value <= 0 if op in (6, 22) else value > 0
                    likely = op in (22, 23)
                immediate = word & 0xFFFF
                offset = immediate if immediate < 0x8000 else immediate - 0x10000
                if taken or not likely:
                    self.execute(self.code[pc + 4])
                pc = pc + 4 + offset * 4 if taken else pc + 8
            elif op in (2, 3):
                if op == 3:
                    self.registers[31] = pc + 8
                self.execute(self.code[pc + 4])
                pc = ((pc + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2)
            elif word == 0x03E00008:
                target = self.registers[31]
                self.execute(self.code[pc + 4])
                if target == 0xDEAD0000:
                    return self.registers[2]
                pc = target
            else:
                self.execute(word)
                pc += 4
        raise AssertionError("compiled guest instruction budget exhausted")


class GuestStreamFixture(GuestBuilderFixture):
    STATE = 0x60000
    FRAME = 0x70000
    INPUT = 0x50000
    OUTPUT = 0x40000
    FIXED_BASE = 0x8003BE90

    def __init__(self, image, raw, limit=0x70000000):
        super().__init__(image, [])
        self.memory.update((address, 0xA5) for address in
                           range(self.OUTPUT - 16, self.INPUT))
        self.memory.update((self.INPUT + index, value) for index, value in
                           enumerate(raw + b"\0" * 16))
        self.memory.update((self.FIXED_BASE + index, 0xA5) for index in range(0x10000))
        fixed_range = (self.FIXED_BASE, self.FIXED_BASE + 0x10000)
        self.allowed_writes.extend((fixed_range, (self.OUTPUT, self.INPUT)))
        self.put(self.STATE + 8, self.FIXED_BASE, 4)
        self.put(self.STATE + 36, self.FIXED_BASE, 4)
        self.registers[4] = self.STATE
        initializer_registers = self.registers[:]
        self.run(entry=image.symbols["init_decode_fixed_tables"], budget=2000000)
        if self.get(self.STATE + 28, 4) != 658:
            raise AssertionError("compiled fixed-table allocation differs from retail")
        if [self.get(self.FRAME + offset, size) for offset, size in
                ((0x9C8, 2), (0x9CC, 4), (0x9D0, 2), (0x9D4, 4))] != [1, 7, 626, 5]:
            raise AssertionError("compiled fixed roots/widths differ from retail")
        for register in (*range(16, 24), 28, 29, 30, 31):
            if self.registers[register] != initializer_registers[register]:
                raise AssertionError("compiled initializer changed a saved O32 register")
        if bytes(self.memory[self.FRAME + offset] for offset in range(0xA44, 0xA88 + 16)) != b"\xa5" * 84:
            raise AssertionError("compiled initializer overwrote reserved frame cells")
        self.fixed_table = bytes(self.memory[self.FIXED_BASE + index] for index in range(658 * 4))
        self.allowed_writes.remove(fixed_range)
        self.readonly.append(fixed_range)
        # Initializer and stream have independent caller scratch lifetimes.
        self.memory.update((self.FRAME + index, 0xA5) for index in range(0xA88))
        for index, value in enumerate((self.INPUT, self.OUTPUT, self.WORKSPACE, 0,
                                       0, 0, limit, 0, self.FRAME, self.WORKSPACE)):
            self.put(self.STATE + index * 4, value, 4)
        self.registers[4:8] = [self.STATE, self.FIXED_BASE, 0, 0]
        self.before = self.registers[:]
        self.min_sp = self.STACK
        self.reads, self.writes, self.visits = [], [], {}

    def stream(self):
        return self.run(entry=self.image.symbols["init_decode_stream"], budget=2000000)

    def core(self, alignment=0, workspace=None):
        workspace = self.WORKSPACE if workspace is None else workspace
        self.put(self.STATE, self.INPUT + alignment, 4)
        self.put(self.STATE + 8, workspace, 4)
        self.registers[4:8] = [self.STATE, self.FIXED_BASE, self.INPUT + alignment, self.OUTPUT]
        self.put(self.STACK + 16, workspace, 4)
        return self.run(entry=self.image.symbols["init_decode_core"], budget=2000000)
