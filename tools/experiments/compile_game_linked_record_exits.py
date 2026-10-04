"""Isolated source exit-layout trials; never alters production ownership."""

import json
import re
import struct
import subprocess
import unittest
from pathlib import Path

from tools.tests.test_game_linked_record_position import GameLinkedRecordPositionTests


def shapes(body):
    marker = "    if (func_1514ECE0(*(void **)(actor + 0x2F4), 0x16, &node)) {\n"
    declarations, paths = body.split(marker)
    success, fallback = paths.split("    } else {\n")
    fallback = fallback.removesuffix("    }\n}")
    call = "func_1514ECE0(*(void **)(actor + 0x2F4), 0x16, &node)"
    return {
        "control": body,
        "success-return": declarations + marker + success + "        return;\n    } else {\n" + fallback + "    }\n}",
        "success-goto": declarations + marker + success + "        goto done;\n    } else {\n" + fallback + "    }\ndone:\n    return;\n}",
        "failure-return": declarations + "    if (!" + call + ") {\n" + fallback + "        return;\n    }\n" + success + "}",
        "failure-goto": declarations + "    if (!" + call + ") goto fallback;\n" + success + "    return;\nfallback:\n" + fallback + "}",
    }


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / "conker/build/game-linked-record-exits"
    output.mkdir(parents=True, exist_ok=True)
    source = (root / "conker/src/game/generated_113D60.c").read_text()
    body = re.search(r"void func_150E6FAC\(f32 \*output, u8 \*actor\) \{\n.*?\n\}", source, re.S).group(0)
    retail = (root / "conker/conker.us.bin").read_bytes()[0x11445C:0x11457C]
    types = "typedef unsigned char u8; typedef short s16; typedef int s32; typedef float f32;\n"
    declarations = ("s32 func_150ADA20(void); f32 func_150ADA68(void);\n"
                    "f32 func_151423D8(u8); s32 func_1514ECE0(void *,s16,void **);\n")
    methods = [name for name in unittest.defaultTestLoader.getTestCaseNames(GameLinkedRecordPositionTests)
               if name != "test_independent_ido_body_fits_retail_slot"]
    GameLinkedRecordPositionTests.setUpClass()
    report = []
    try:
        for shape, candidate in shapes(body).items():
            suite = unittest.TestSuite()
            for name in methods:
                test = GameLinkedRecordPositionTests(name)
                test.fixture = test.fixture.replace(test.body, candidate)
                suite.addTest(test)
            result = unittest.TestResult()
            suite.run(result)
            if not result.wasSuccessful() or result.skipped:
                raise AssertionError((shape, result.errors, result.failures, result.skipped))
            trial = output / (shape + ".c")
            trial.write_text(types + declarations + candidate + "\n")
            for profile, flags in (("o2g3", ["-O2", "-g3"]), ("o2", ["-O2"]),
                                   ("o1g3", ["-O1", "-g3"]), ("o1", ["-O1"])):
                prefix = output / (shape + "-" + profile)
                obj, elf, binary = (Path(str(prefix)+suffix) for suffix in (".o", ".elf", ".bin"))
                command = [str(root / "ido/ido5.3_recomp/cc"), "-c", "-32", "-G", "0",
                    "-Xfullwarn", "-Xcpluscomm", "-signed", "-nostdinc", "-non_shared",
                    "-Wab,-r4300_mul", "-mips2", "-o32", *flags, "-o",
                    str(obj.relative_to(root)), str(trial.relative_to(root))]
                compiled = subprocess.run(command, cwd=root, capture_output=True, text=True)
                Path(str(prefix)+".log").write_text(compiled.stdout + compiled.stderr)
                if compiled.returncode or compiled.stdout or compiled.stderr or not obj.is_file():
                    raise RuntimeError(compiled.stdout + compiled.stderr)
                script = output / "position.ld"
                script.write_text("SECTIONS { .text 0x150E6FAC : SUBALIGN(4) { *(.text) } }\n")
                subprocess.run(["mips-linux-gnu-ld", "-m", "elf32btsmip", "-T", str(script),
                    "-e", "func_150E6FAC", "--defsym=func_150ADA20=0x150ADA20",
                    "--defsym=func_150ADA68=0x150ADA68", "--defsym=func_151423D8=0x151423D8",
                    "--defsym=func_1514ECE0=0x1514ECE0", "-o", str(elf), str(obj)],
                    check=True, capture_output=True, text=True)
                subprocess.run(["mips-linux-gnu-objcopy", "-O", "binary", "-j", ".text",
                    str(elf), str(binary)], check=True, capture_output=True, text=True)
                data = binary.read_bytes()
                words = struct.unpack(">" + "I"*(len(data)//4), data)
                end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
                emitted = data[:end*4]
                disassembly = subprocess.check_output(["mips-linux-gnu-objdump", "-d", "-z", str(elf)], text=True)
                Path(str(prefix)+".asm.txt").write_text(disassembly)
                differences = sum(emitted[i:i+4] != retail[i:i+4]
                                  for i in range(0, max(len(emitted), len(retail)), 4))
                report.append({"shape": shape, "profile": profile, "body_words": end,
                    "different_positions": differences, "exact": emitted == retail,
                    "host_tests_passed": len(methods)})
    finally:
        GameLinkedRecordPositionTests.doClassCleanups()
    (output / "measurements.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
