import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.test_game_oriented_record_overlap import START, TYPES


class InitBitmapAllocatorContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.compiler = shutil.which("cc")
        if cls.compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.flags = ["-m32", "-O2", "-std=c99", "-ffreestanding", "-nostdlib",
                     "-static", "-fno-pie", "-no-pie", "-fno-stack-protector",
                     "-fno-strict-aliasing", "-fwrapv"]
        probe = cls.path / "probe.c"
        probe.write_text("int run(void) { return 0; }\n" + START)
        result = subprocess.run([cls.compiler, *cls.flags, str(probe), "-o",
                                 str(cls.path / "probe")], capture_output=True, text=True)
        if result.returncode:
            raise unittest.SkipTest("freestanding 32-bit compiler support is unavailable")
        try:
            result = subprocess.run([str(cls.path / "probe")], timeout=5)
        except OSError as error:
            raise unittest.SkipTest("32-bit host execution is unavailable") from error
        if result.returncode:
            raise unittest.SkipTest("32-bit host execution probe failed")
        cls.project = Path(__file__).resolve().parents[2] / "conker"

        def function(filename, name):
            source = (cls.project / "src" / filename).read_text()
            match = re.search(r"(?:void|s32) " + name + r"\([^;{]*\{\n.*?\n\}",
                              source, re.S)
            if match is None:
                raise AssertionError("production function not found: " + name)
            return match.group(0)

        structures = (cls.project / "include/structs.h").read_text()
        layout = re.search(r"struct struct54 \{\n.*?\n\};", structures, re.S)
        if layout is None:
            raise AssertionError("production allocator layout was not found")
        data = (cls.project / "asm/data/290D0.data.s").read_text()

        def table(name):
            body = data.split("dlabel " + name + "\n", 1)[1].split(
                "enddlabel " + name, 1)[0]
            words = re.findall(r"\.word 0x([0-9A-Fa-f]+)", body)
            raw = b"".join(struct.pack(">I", int(word, 16)) for word in words)
            return ",".join(str(value) for value in struct.unpack(">5h", raw[:10]))

        cls.source = TYPES + r'''
typedef signed char s8;
typedef u32 OSIntMask;
#define NULL 0
typedef struct struct54 struct54;
''' + layout.group(0) + r'''
typedef struct { s16 values[5]; } MemoryAlignmentTable;
static u8 heap[0x200000] __attribute__((section(".test_heap"), aligned(16)));
#define D_800E9D10 heap[0]
u32 D_80038098, D_80038080, D_80038090, D_80038094, D_8003809C;
struct54 *D_800380B0, *D_800380B4, *D_800380B8;
s32 *D_800380BC;
s32 D_8002AC30, D_800380C0, D_800380C4, D_800380C8, D_800380CC;
s32 D_800380D0, D_8003C8E0;
static u32 interruptMask = 0x1234;
static s32 errors;
OSIntMask osSetIntMask(OSIntMask mask) {
    OSIntMask old = interruptMask;
    interruptMask = mask;
    return old;
}
void func_150AD770(void) { errors++; }
void func_1000440C(void);
s32 func_10003C6C(s32, s32, s32, s32, s32);
''' + "MemoryAlignmentTable D_8002AC34 = {{" + table("D_8002AC34") + "}};\n" + \
            "MemoryAlignmentTable D_8002AC40 = {{" + table("D_8002AC40") + "}};\n" + \
            "\n".join((function("init_3930.c", "func_10003930"),
                        function("init_3BD0.c", "func_10003BD0"),
                        function("init_3C40.c", "allocate_memory"),
                        function("init_3C40.c", "func_10003C6C"),
                        function("init_3C40.c", "func_1000440C"))) + r'''
static void initialize(void) {
    s32 i;
    for (i = 0; i < sizeof(heap); i++) heap[i] = 0xA5;
    D_80038098 = (u32)heap + sizeof(heap);
    D_8002AC30 = 0x10000000;
    errors = 0;
    interruptMask = 0x1234;
    func_10003BD0();
}
static s32 in_heap(u32 address, u32 size) {
    return address >= (u32)heap && address <= D_80038098 &&
           size <= D_80038098 - address && address > 0x8003BE7F;
}
static s32 valid_lists(void) {
    struct54 *block, *previous = NULL;
    s32 steps = 0;
    for (block = D_800380B4; block; block = block->unk0) {
        if (++steps > 2048 || !in_heap((u32)block, 0x14)) return 0;
        if (block->unk4 != previous) return 0;
        if (!in_heap((u32)block + 0xC, block->unk8 & 0xFFFFFF)) return 0;
        if (block->unk0 && (u32)block->unk0 <= (u32)block) return 0;
        previous = block;
    }
    previous = NULL; steps = 0;
    for (block = D_800380B8; block; block = (struct54 *)block->unkC) {
        if (++steps > 2048 || !in_heap((u32)block, 0x14)) return 0;
        if (block->unk8 >> 24 || block->unk10 != (s32)previous) return 0;
        if (previous && (u32)previous >= (u32)block) return 0;
        previous = block;
    }
    return (s32 *)previous == D_800380BC && interruptMask == 0x1234;
}
'''

    def run_case(self, body):
        fixture = self.path / "allocator.c"
        binary = self.path / "allocator"
        fixture.write_text(self.source + "\nint run(void) {\n" + body + "\n}\n" + START)
        result = subprocess.run([self.compiler, *self.flags,
                                 "-Wl,--section-start=.test_heap=0x800E9D10",
                                 str(fixture), "-o", str(binary)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([str(binary)], capture_output=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_production_ram_limits_and_initial_heap_ownership(self):
        self.run_case(r'''
    s32 expansion;
    if (sizeof(void *) != 4 || (u32)heap != 0x800E9D10) return 1;
    for (expansion = 0; expansion < 2; expansion++) {
        D_80038080 = expansion;
        func_10003930();
        if (D_80038098 != (expansion ? 0x807F5000 : 0x803F5000)) return 2;
        func_10003BD0();
        if ((u32)D_800380B4 != 0x800E9D10 || D_800380B8 != D_800380B4 ||
            D_800380B0 != D_800380B4 || (void *)D_800380BC != D_800380B4) return 3;
        if (D_800380B4->unk0 || D_800380B4->unk4 || D_800380B4->unkC ||
            D_800380B4->unk10 || D_800380B4->unk8 != D_80038098 - 0x800E9D10 - 0x14)
            return 4;
    }
    return 0;
''')

    def test_all_direct_counts_page_allocation_then_bitmap(self):
        self.run_case(r'''
    s32 count, pages, bitmap, size, rounded;
    for (count = 107; count <= 362; count++) {
        initialize();
        pages = func_10003C6C(count << 12, 0xFF, 4, 1, 2);
        if (!pages || !in_heap((u32)pages, count << 12)) return 1;
        if ((u32)pages & 0x1FFF) return 2;
        size = (count + 7) >> 3;
        bitmap = allocate_memory(size, 0xFF, 0, 0);
        rounded = (size + 3) & ~3;
        if (!bitmap || !in_heap((u32)bitmap, rounded)) return 3;
        if ((u32)bitmap + rounded > (u32)pages) return 4;
        if ((((struct54 *)((u32)bitmap - 0xC))->unk8 & 0xFFFFFF) != rounded) return 5;
        if (!valid_lists() || errors) return 6;
    }
    return 0;
''')

    def test_small_bitmap_request_rounding(self):
        self.run_case(r'''
    s32 count, size, bitmap, rounded;
    for (count = 1; count <= 64; count++) {
        initialize();
        size = (count + 7) >> 3;
        rounded = ((size < 8 ? 8 : size) + 3) & ~3;
        bitmap = allocate_memory(size, 0xFF, 0, 0);
        if ((u32)bitmap != (u32)heap + 0xC || !in_heap((u32)bitmap, rounded)) return 1;
        if ((((struct54 *)((u32)bitmap - 0xC))->unk8 & 0xFFFFFF) != rounded) return 2;
        if (!valid_lists() || errors) return 3;
    }
    return 0;
''')

    def test_repeated_mixed_direction_allocations_preserve_heap_bounds(self):
        self.run_case(r'''
    s32 i, direction, allocation, size;
    u32 low = (u32)heap, high = (u32)heap + sizeof(heap);
    initialize();
    for (i = 0; i < 128; i++) {
        direction = i & 1;
        size = ((107 + (i * 17) % 256 + 7) >> 3);
        size = (size + 3) & ~3;
        allocation = func_10003C6C(size, 0xFF, 0, direction, 0);
        if (!allocation || !in_heap((u32)allocation, size)) return 1;
        if ((u32)allocation < low || (u32)allocation + size > high) return 2;
        if (direction) high = (u32)allocation - 0xC;
        else low = (u32)allocation + size;
        if (!valid_lists() || errors) return 3;
    }
    return 0;
''')

    def test_exhaustion_is_not_implicit_allocation_success(self):
        self.run_case(r'''
    s32 result;
    initialize();
    result = allocate_memory(sizeof(heap) + 4, 0xFF, 0, 0);
    if (result || errors != 1 || D_8003C8E0 != 0x0C000042) return 1;
    if (!valid_lists()) return 2;
    result = func_10003C6C(sizeof(heap) + 4, 0xFF, 4, 1, 2);
    if (result || errors != 1 || !valid_lists()) return 3;
    return 0;
''')

    def test_all_alignment_classes_in_both_directions(self):
        self.run_case(r'''
    s32 alignment, direction, index, request, rounded, allocation;
    s32 sizes[] = {0, 1, 4, 8, 17, 64, 4096, 438272};
    struct54 *header;
    for (alignment = 0; alignment < 5; alignment++) {
        for (direction = 0; direction < 2; direction++) {
            for (index = 0; index < 8; index++) {
                initialize();
                request = sizes[index];
                rounded = alignment == 2 ? (request + 15) & ~15 : request;
                rounded = ((rounded < 8 ? 8 : rounded) + 3) & ~3;
                allocation = func_10003C6C(request, 0xFF, alignment, direction, 0);
                if (!allocation || !in_heap((u32)allocation, rounded)) return 1;
                if ((u32)allocation & ~(s32)D_8002AC40.values[alignment]) return 2;
                header = (struct54 *)((u32)allocation - 0xC);
                if ((header->unk8 >> 24) != 0xFF ||
                    (header->unk8 & 0xFFFFFF) < rounded) return 3;
                if (!valid_lists() || errors) return 4;
            }
        }
    }
    return 0;
''')


if __name__ == "__main__":
    unittest.main()
