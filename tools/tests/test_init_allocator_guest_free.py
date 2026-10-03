import re
import shutil
import subprocess
import unittest

from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture, GuestImage
from tools.tests import test_init_bitmap_allocator_contract as allocator
from tools.tests import test_init_decompressor_retail_pages as retail


class AllocatorGuestFixture(GuestBuilderFixture):
    HEAP = 0x800E9D10
    LIMIT = HEAP + 0x200000

    def __init__(self, image):
        self.image, self.code = image, image.code
        self.memory = dict(image.memory)
        self.memory.update((address, 0xA5) for address in range(self.STACK - 4096,
                                                             self.STACK + 64))
        self.readonly = image.readonly
        # ELF writes must stay in mapped writable bytes; heap and stack are private.
        self.allowed_writes = [(self.HEAP, self.LIMIT),
                               (self.STACK - 4096, self.STACK + 64)]
        self.registers = [0x5A000000 + i for i in range(32)]
        self.registers[0] = 0
        self.registers[29] = self.min_sp = self.STACK
        self.registers[31] = 0xDEAD0000
        self.before = self.registers[:]
        self.fprs = [0] * 32
        self.reads, self.writes, self.visits = [], [], {}
        self.capture, self.snapshots = set(), {}

    def put(self, address, value, size):
        if all(address + i in self.image.memory for i in range(size)):
            allowed = self.allowed_writes
            self.allowed_writes = None
            try:
                return super().put(address, value, size)
            finally:
                self.allowed_writes = allowed
        return super().put(address, value, size)

    def get(self, address, size):
        # Lazily materialize only reads inside the private, poisoned heap.
        for i in range(size):
            if self.HEAP <= address + i < self.LIMIT:
                self.memory.setdefault(address + i, 0xA5)
        return super().get(address, size)

    def execute(self, word):
        op = word >> 26
        if op in (53, 57, 61):
            rs, rt, immediate = word >> 21 & 31, word >> 16 & 31, word & 0xFFFF
            offset = immediate if immediate < 0x8000 else immediate - 0x10000
            address = (self.registers[rs] + offset) & 0xFFFFFFFF
            size = 4 if op == 57 else 8
            if op == 53:
                value = self.get(address, size)
                self.fprs[rt], self.fprs[rt + 1] = value >> 32, value & 0xFFFFFFFF
                self.reads.append((address, size))
            else:
                value = self.fprs[rt] if size == 4 else (self.fprs[rt] << 32) | self.fprs[rt + 1]
                self.put(address, value, size)
                self.writes.append((address, size))
        elif op == 33:  # Signed LH used by the production alignment tables.
            rs, rt, immediate = word >> 21 & 31, word >> 16 & 31, word & 0xFFFF
            offset = immediate if immediate < 0x8000 else immediate - 0x10000
            address = (self.registers[rs] + offset) & 0xFFFFFFFF
            value = self.get(address, 2)
            self.registers[rt] = (value if value < 0x8000 else value - 0x10000) & 0xFFFFFFFF
            self.registers[0] = 0
            self.reads.append((address, 2))
        else:
            super().execute(word)


class InitAllocatorGuestFreeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        allocator.InitBitmapAllocatorContractTests.setUpClass.__func__(cls)
        cls.root = cls.project.parent
        cls.ido = cls.root / "ido/ido5.3_recomp/cc"
        cls.linker = shutil.which("mips-linux-gnu-ld")
        if not cls.ido.is_file() or not cls.linker:
            raise unittest.SkipTest("IDO/MIPS linker is unavailable")
        cls.source = cls.source.replace(
            'static u8 heap[0x200000] __attribute__((section(".test_heap"), aligned(16)));',
            'extern u8 heap[0x200000];').replace(
                'for (i = 0; i < sizeof(heap); i++) heap[i] = 0xA5;', '')
        production = (cls.project / "src/init_3C40.c").read_text()
        sweeps = ['static s32 cleanupCalls, cleanupMask;\n'
                  'void func_15042D50(void) { cleanupCalls++; cleanupMask = interruptMask; }\n']
        for name in ("func_10004250", "func_10004308", "func_100043B4"):
            match = re.search(r"void " + name + r"\([^;{]*\{\n.*?\n\}", production, re.S)
            if match is None:
                raise AssertionError("production function not found: " + name)
            sweeps.append(match.group(0))
        cls.source += "\n" + "\n".join(sweeps)

    def run_guest(self, body, retail_cleanup=False):
        for profile in (("-O2", "-g3"), ("-O1",)):
            with self.subTest(profile=profile):
                source, obj, elf = (self.path / name for name in ("guest.c", "guest.o", "guest.elf"))
                source.write_text(self.source + '\ns32 init_decode_build(void) {\n' + body + '\n}\n')
                command = [str(self.ido), "-c", "-32", "-G", "0", "-Xfullwarn",
                           "-Xcpluscomm", "-signed", "-nostdinc", "-non_shared",
                           "-Wab,-r4300_mul", "-mips2", "-o32", *profile,
                           str(source), "-o", str(obj)]
                result = subprocess.run(command, capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                result = subprocess.run([self.linker, "-Ttext", "0x10400000", "-Tdata",
                                         "0x10500000", "-e", "init_decode_build", "--defsym",
                                         "heap=0x800E9D10", str(obj), "-o", str(elf)],
                                        capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                fixture = AllocatorGuestFixture(GuestImage(elf.read_bytes()))
                if retail_cleanup:
                    image = (self.project / "conker.us.bin").read_bytes()
                    pages = retail.retail_pages((self.root / "baserom.us.z64").read_bytes())
                    raw = b"".join(page[4] for page in pages)
                    first, last = 0x42D50, 0x43A00
                    payload = raw[first:last]
                    self.assertEqual(payload, image[0x2D4B0 + first:0x2D4B0 + last])
                    self.assertEqual(payload[:40].hex(),
                                     "27bdffe8afbf00143c01800dac20bd640d410ce100002025"
                                     "8fbf001427bd001803e0000800000000")
                    assembly = (self.project / "asm/nonmatchings/game_70200/func_15043384.s").read_text()
                    words = re.findall(r"/\* [0-9A-F]+ ([0-9A-F]+) ([0-9A-F]{8}) \*/", assembly)
                    self.assertEqual(len(words), (0x15043A00 - 0x15043384) // 4)
                    for pc, word in words:
                        offset = int(pc, 16) - 0x15000000
                        self.assertEqual(raw[offset:offset + 4].hex(), word.lower())
                    fixture.code = dict(fixture.code)
                    fixture.code.update((0x15000000 + first + i,
                                         int.from_bytes(payload[i:i + 4], "big"))
                                        for i in range(0, len(payload), 4))
                    thunk = fixture.image.symbols["func_15042D50"]
                    fixture.code[thunk] = (2 << 26) | ((0x15042D50 >> 2) & 0x3FFFFFF)
                    fixture.code[thunk + 4] = 0
                    fixture.allowed_writes.extend(((0x800CBD60, 0x800CBD84),
                                                   (0x80085CD0, 0x80085CD4)))
                    fixture.put(0x800CBD64, 0x800E9D1C, 4)
                    fixture.put(0x80085CD0, 41, 4)
                    fixture.fprs[20:22] = [0x11223344, 0x55667788]
                self.assertEqual(fixture.run(budget=3000000), 0)
                for register in (*range(16, 24), 28, 29, 30):
                    self.assertEqual(fixture.registers[register], fixture.before[register])
                self.assertIn(fixture.image.symbols["func_10004074"], fixture.visits)
                if retail_cleanup:
                    self.assertIn(0x150433D0, fixture.visits)
                    self.assertIn(0x1504393C, fixture.visits)
                    self.assertNotIn(0x150433D8, fixture.visits)
                    self.assertNotIn(0x15043918, fixture.visits)
                    self.assertEqual(fixture.get(0x80085CD0, 4), 42)
                    self.assertEqual(fixture.get(0x800CBD64, 4), 0)
                    self.assertEqual(fixture.get(0x800CBD60, 4), 0xFFFFFFFF)
                    self.assertEqual(fixture.get(0x800CBD6C, 4), 0x80)
                    self.assertEqual(fixture.get(0x800CBD70, 4), 0x000A000A)
                    self.assertEqual(fixture.get(0x800CBD80, 4), 0x3F800000)
                    self.assertEqual(fixture.fprs[20:22], [0x11223344, 0x55667788])

    def test_resize_cycles_free_pool_before_bitmap_and_reclaim_heap(self):
        self.run_guest(r'''
    s32 count, pool, bitmap;
    initialize();
    for (count = 107; count <= 362; count++) {
        pool = func_10003C6C(count << 12, 0xFF, 4, 1, 2);
        bitmap = allocate_memory((count + 7) >> 3, 0xFF, 0, 0);
        if (!pool || !bitmap || !valid_lists()) return 1;
        func_10004074((void *)pool);
        if (!valid_lists()) return 2;
        func_10004074((void *)bitmap);
        if (!valid_lists() || errors) return 3;
        if (D_800380B4 != (struct54 *)heap || D_800380B4->unk0 ||
            D_800380B4->unk8 != sizeof(heap) - 0x14 ||
            D_800380B8 != D_800380B4 || (void *)D_800380BC != D_800380B4) return 4;
    }
    return 0;
''')

    def test_middle_reinsertion_then_two_sided_coalescing(self):
        self.run_guest(r'''
    s32 a, b, c;
    initialize();
    a = allocate_memory(32, 0xFE, 0, 0);
    b = allocate_memory(64, 0xFD, 0, 0);
    c = allocate_memory(128, 0xFC, 0, 0);
    func_10004074((void *)b);
    if (!valid_lists() || ((struct54 *)(b - 0xC))->unk8 != 64) return 1;
    func_10004074((void *)a);
    if (!valid_lists()) return 2;
    func_10004074((void *)c);
    func_10004074(NULL);
    if (!valid_lists() || errors || D_800380B4->unk0 ||
        D_800380B4->unk8 != sizeof(heap) - 0x14) return 3;
    return 0;
''')

    def test_free_preserves_adjacent_live_payload_and_tag(self):
        self.run_guest(r'''
    s32 a, b, c, i;
    initialize();
    a = allocate_memory(32, 0xFE, 0, 0);
    b = allocate_memory(64, 0xFD, 0, 0);
    c = allocate_memory(128, 0xFC, 0, 0);
    for (i = 0; i < 32; i++) ((u8 *)a)[i] = i;
    for (i = 0; i < 128; i++) ((u8 *)c)[i] = i ^ 0x5A;
    func_10004074((void *)b);
    if (!valid_lists() || ((struct54 *)(a - 0xC))->unk8 != 0xFE000020 ||
        ((struct54 *)(c - 0xC))->unk8 != 0xFC000080) return 1;
    for (i = 0; i < 32; i++) if (((u8 *)a)[i] != i) return 2;
    for (i = 0; i < 128; i++) if (((u8 *)c)[i] != (i ^ 0x5A)) return 3;
    return 0;
''')

    def test_aging_sweep_frees_tag_two_and_ages_three_four(self):
        self.run_guest(r'''
    s32 a, b, c, d, persistent;
    initialize();
    a = allocate_memory(32, 1, 0, 0);
    b = allocate_memory(64, 2, 0, 0);
    c = allocate_memory(96, 3, 0, 0);
    d = allocate_memory(128, 4, 0, 0);
    persistent = allocate_memory(160, 0xFF, 0, 0);
    func_10004250();
    if (!valid_lists() || ((struct54 *)(a - 12))->unk8 != 0x01000020 ||
        ((struct54 *)(b - 12))->unk8 != 64 ||
        ((struct54 *)(c - 12))->unk8 != 0x02000060 ||
        ((struct54 *)(d - 12))->unk8 != 0x03000080 ||
        ((struct54 *)(persistent - 12))->unk8 != 0xFF0000A0) return 1;
    func_10004250();
    if (!valid_lists() || ((struct54 *)(d - 12))->unk8 != 0x02000080) return 2;
    func_10004250();
    if (!valid_lists() || errors || ((struct54 *)(a - 12))->unk8 != 0x01000020 ||
        ((struct54 *)(persistent - 12))->unk8 != 0xFF0000A0 || cleanupCalls) return 3;
    func_10004074((void *)a);
    func_10004074((void *)persistent);
    if (!valid_lists() || D_800380B4->unk0 ||
        D_800380B4->unk8 != sizeof(heap) - 0x14) return 4;
    return 0;
''')

    def test_full_sweep_crosses_adjacent_frees_and_preserves_other_tags(self):
        self.run_guest(r'''
    s32 allocations[8], tags[8] = {1, 2, 3, 4, 0xFF, 1, 5, 2};
    s32 i;
    initialize();
    for (i = 0; i < 8; i++) {
        allocations[i] = allocate_memory(32, tags[i], 0, 0);
        ((u8 *)allocations[i])[0] = 0x80 + i;
    }
    func_10004074((void *)allocations[1]);
    func_10004308();
    if (!valid_lists() || errors || cleanupCalls != 1 || cleanupMask != 1) return 1;
    for (i = 0; i < 8; i++) {
        if (tags[i] == 5 || tags[i] == 0xFF) {
            if (((struct54 *)(allocations[i] - 12))->unk8 != ((tags[i] << 24) | 32) ||
                ((u8 *)allocations[i])[0] != 0x80 + i) return 2;
        }
    }
    func_10004074((void *)allocations[4]);
    func_10004074((void *)allocations[6]);
    if (!valid_lists() || D_800380B4->unk0 ||
        D_800380B4->unk8 != sizeof(heap) - 0x14) return 3;
    return 0;
''')

    def test_retag_preserves_size_and_changes_sweep_lifetime(self):
        self.run_guest(r'''
    s32 allocation;
    initialize();
    allocation = allocate_memory(64, 0xFF, 0, 0);
    func_100043B4((s32 *)allocation, 4);
    if (!valid_lists() || ((struct54 *)(allocation - 12))->unk8 != 0x04000040) return 1;
    func_10004250();
    if (!valid_lists() || ((struct54 *)(allocation - 12))->unk8 != 0x03000040) return 2;
    func_10004250();
    if (!valid_lists() || ((struct54 *)(allocation - 12))->unk8 != 0x02000040) return 3;
    func_10004250();
    if (!valid_lists() || errors || D_800380B4->unk0 ||
        D_800380B4->unk8 != sizeof(heap) - 0x14) return 4;
    return 0;
''')

    def test_full_sweep_with_actual_retail_cleanup_null_list_path(self):
        if not (self.project / "conker.us.bin").is_file() or not (self.root / "baserom.us.z64").is_file():
            self.skipTest("local retail ROM and decompressed image required")
        self.run_guest(r'''
    s32 selected, persistent;
    initialize();
    selected = allocate_memory(64, 2, 0, 0);
    persistent = allocate_memory(128, 0xFF, 0, 0);
    ((u8 *)persistent)[0] = 0x5A;
    func_10004308();
    if (!valid_lists() || errors || ((struct54 *)(selected - 12))->unk8 != 64 ||
        ((struct54 *)(persistent - 12))->unk8 != 0xFF000080 ||
        ((u8 *)persistent)[0] != 0x5A) return 1;
    func_10004074((void *)persistent);
    if (!valid_lists() || D_800380B4->unk0 ||
        D_800380B4->unk8 != sizeof(heap) - 0x14) return 2;
    return 0;
''', retail_cleanup=True)

    def test_fatal_callback_is_retail_syscall_slot_not_returning_c_stub(self):
        path = self.root / "baserom.us.z64"
        if not path.is_file():
            self.skipTest("local retail ROM required")
        raw = b"".join(page[4] for page in retail.retail_pages(path.read_bytes()))
        self.assertEqual(raw[0xAD770:0xAD780], bytes.fromhex(
            "0000000C 00000000 00000000 00000000"))


class AllocatorGuestInstructionTests(unittest.TestCase):
    def test_fpr_pair_save_restore_and_word_store_are_big_endian(self):
        fixture = AllocatorGuestFixture.__new__(AllocatorGuestFixture)
        fixture.memory, fixture.reads, fixture.writes = {}, [], []
        fixture.registers, fixture.fprs = [0] * 32, [0] * 32
        fixture.readonly, fixture.allowed_writes = [], [(0x1000, 0x1010)]
        fixture.image = type("Image", (), {"memory": {}})()
        fixture.registers[1] = 0x1000
        fixture.fprs[20:22] = [0x11223344, 0x55667788]
        fixture.execute((61 << 26) | (1 << 21) | (20 << 16))
        self.assertEqual(fixture.get(0x1000, 8), 0x1122334455667788)
        fixture.fprs[20:22] = [0, 0]
        fixture.execute((53 << 26) | (1 << 21) | (20 << 16))
        self.assertEqual(fixture.fprs[20:22], [0x11223344, 0x55667788])
        fixture.execute((57 << 26) | (1 << 21) | (21 << 16) | 8)
        self.assertEqual(fixture.get(0x1008, 4), 0x55667788)

    def test_signed_halfword_reads_big_endian_and_sign_extends(self):
        fixture = AllocatorGuestFixture.__new__(AllocatorGuestFixture)
        fixture.memory = {0x1000: 0xFF, 0x1001: 0xFC, 0x1002: 0, 0x1003: 7}
        fixture.registers, fixture.reads = [0] * 32, []
        fixture.registers[1] = 0x1002
        fixture.execute((33 << 26) | (1 << 21) | (2 << 16) | 0xFFFE)
        self.assertEqual(fixture.registers[2], 0xFFFFFFFC)
        fixture.execute((33 << 26) | (1 << 21) | (2 << 16))
        self.assertEqual(fixture.registers[2], 7)
        self.assertEqual(fixture.reads, [(0x1000, 2), (0x1002, 2)])


if __name__ == "__main__":
    unittest.main()
