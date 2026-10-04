"""Bounded bitmap store/return-lifetime trials, separate from production."""

import json
import subprocess
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[2]
    cwd = root / "conker"
    output = cwd / "build/init-bitmap-ordered"
    output.mkdir(parents=True, exist_ok=True)
    source = "../tools/experiments/init_bitmap_ordered.c"
    retail = (cwd / "conker.us.bin").read_bytes()[0x5BE0:0x5C2C]
    report = []
    for shape in (1, 2, 3, 4, 5):
        prefix = "build/init-bitmap-ordered/shape%d" % shape
        host = prefix + "-host"
        subprocess.run(["cc", "-O2", "-std=c99", "-Wall", "-Wextra",
                        "-Werror", "-DHOST_TEST",
                        "-DSHAPE=%d" % shape, source, "-o", host], cwd=cwd, check=True)
        subprocess.run(["./" + host], cwd=cwd, check=True)
        for profile, flags in (("o2g3", ["-O2", "-g3"]), ("o1", ["-O1"])):
            obj = prefix + "-" + profile + ".o"
            (cwd / obj).unlink(missing_ok=True)
            result = subprocess.run([
                "../ido/ido5.3_recomp/cc", "-c", "-32", "-G", "0", "-Xfullwarn",
                "-Xcpluscomm", "-signed", "-nostdinc", "-non_shared",
                "-Wab,-r4300_mul", "-mips2", "-o32", "-DSHAPE=%d" % shape,
                *flags, "-o", obj, source], cwd=cwd, capture_output=True, text=True)
            (cwd / (obj + ".log")).write_text(result.stdout + result.stderr)
            if result.returncode or not (cwd / obj).is_file():
                raise RuntimeError("guest compile failed: " + obj + "\n" + result.stderr)
            elf, binary = obj + ".elf", obj + ".bin"
            subprocess.run(["mips-linux-gnu-ld", "-m", "elf32btsmip",
                "-Ttext=0x10005BE0", "-e", "func_10005BE0",
                "--defsym=D_8003BE70=0x8003BE70", "--defsym=D_8003BE7C=0x8003BE7C",
                "--defsym=D_8003BE78=0x8003BE78", "-o", elf, obj], cwd=cwd, check=True)
            subprocess.run(["mips-linux-gnu-objcopy", "-O", "binary",
                            "--only-section=.text", elf, binary], cwd=cwd, check=True)
            data = (cwd / binary).read_bytes()
            words = [data[i:i + 4] for i in range(0, len(data), 4)]
            end = max(i for i, word in enumerate(words) if word == b"\x03\xe0\x00\x08") + 2
            body = data[:end * 4]
            differences = sum(body[i:i + 4] != retail[i:i + 4]
                              for i in range(0, max(len(body), len(retail)), 4))
            disassembly = subprocess.check_output(
                ["mips-linux-gnu-objdump", "-d", "-z", elf], cwd=cwd, text=True)
            (cwd / (obj + ".asm.txt")).write_text(disassembly)
            report.append({"shape": shape, "profile": profile,
                           "body_words": end, "different_positions": differences,
                           "exact": body == retail, "host_cases": 79,
                           "host_return_checked": shape in (4, 5)})
    (output / "measurements.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
