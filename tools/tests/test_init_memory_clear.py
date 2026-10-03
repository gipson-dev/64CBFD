import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class InitMemoryClearTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("cc")
        if compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/init_1420.c").read_text()
        match = re.search(r"void func_10001420\(void\) \{\n.*?\n\}", source, re.S)
        if match is None:
            raise AssertionError("Init memory-clear definition was not found")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        directory = Path(cls.directory.name)
        fixture = directory / "clear.c"
        fixture.write_text(
            "#include <stdint.h>\n#include <stdlib.h>\n#include <string.h>\n"
            "typedef uint32_t u32;\n"
            "static struct { u32 before[4], payload[0x3F8], after[4]; } storage;\n"
            "#define D_80043B40 storage.payload\n" + match.group(0) + r"""
int main(int argc, char **argv) {
    unsigned char *bytes = (unsigned char *)&storage;
    unsigned char pattern = (unsigned char)strtoul(argv[1], 0, 0);
    size_t i;
    if (sizeof(u32) != 4 || (uintptr_t)&storage > UINT32_MAX - sizeof(storage))
        return 77;
    memset(&storage, pattern, sizeof(storage));
    func_10001420();
    func_10001420();
    for (i = 0; i < sizeof(storage); i++) {
        unsigned char expected = i >= sizeof(storage.before) &&
            i < sizeof(storage.before) + sizeof(storage.payload) ? 0 : pattern;
        if (bytes[i] != expected)
            return 1;
    }
    return 0;
}
"""
        )
        cls.binary = directory / "clear"
        # A non-PIE executable supplies real low addresses for the guest u32 casts.
        subprocess.run(
            [compiler, "-O2", "-std=c99", "-fno-pie", "-no-pie",
             str(fixture), "-o", str(cls.binary)],
            check=True, capture_output=True, text=True,
        )

    def checkPattern(self, pattern):
        result = subprocess.run([str(self.binary), str(pattern)], check=False)
        if result.returncode == 77:
            self.skipTest("host fixture cannot represent its address in guest u32")
        self.assertEqual(result.returncode, 0)

    def test_clear_exact_range_and_preserve_sentinels(self):
        self.checkPattern(0xA5)

    def test_clear_all_bits_and_repeat(self):
        self.checkPattern(0xFF)

    def test_already_zero_range(self):
        self.checkPattern(0)


if __name__ == "__main__":
    unittest.main()
