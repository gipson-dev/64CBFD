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
        self.readonly = image.readonly
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
        return super().run(budget=budget, entry=self.image.entry if entry is None else entry,
                           stop_pc=stop_pc)
