"""Bounded bitmap store/return-lifetime trials, separate from production."""

import argparse
import json
import struct
import subprocess
from pathlib import Path


PROFILES = (("o2g3", ["-O2", "-g3"]),
            ("o2g3-no-unroll", ["-O2", "-g3", "-Wo,-loopunroll,0"]),
            ("o1", ["-O1"]))


def compile_shapes(shapes):
    root = Path(__file__).resolve().parents[2]
    cwd = root / "conker"
    output = cwd / "build/init-bitmap-ordered"
    output.mkdir(parents=True, exist_ok=True)
    source = "../tools/experiments/init_bitmap_ordered.c"
    retail = (cwd / "conker.us.bin").read_bytes()[0x5BE0:0x5C2C]
    report = []
    for shape in shapes:
        if shape not in range(1, 14):
            raise ValueError("unknown bitmap shape: %s" % shape)
        prefix = "build/init-bitmap-ordered/shape%d" % shape
        host = prefix + "-host"
        subprocess.run(["cc", "-O2", "-std=c99", "-Wall", "-Wextra",
                        "-Werror", "-DHOST_TEST",
                        "-DSHAPE=%d" % shape, source, "-o", host], cwd=cwd, check=True)
        subprocess.run(["./" + host], cwd=cwd, check=True)
        for profile, flags in PROFILES:
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
            frames = [0x10000 - (word & 0xFFFF) for word, in
                      struct.iter_unpack(">I", body)
                      if word >> 16 == 0x27BD and word & 0x8000]
            if len(frames) > 1:
                raise ValueError("bitmap trial requires control-flow stack analysis")
            differences = sum(body[i:i + 4] != retail[i:i + 4]
                              for i in range(0, max(len(body), len(retail)), 4))
            disassembly = subprocess.check_output(
                ["mips-linux-gnu-objdump", "-d", "-z", elf], cwd=cwd, text=True)
            (cwd / (obj + ".asm.txt")).write_text(disassembly)
            report.append({"shape": shape, "profile": profile,
                           "body_words": end, "different_positions": differences,
                           "exact": body == retail, "host_cases": 79,
                           "frame_bytes": sum(frames),
                           "host_return_checked": shape in (4, 5)})
    (output / "measurements.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shapes", type=int, nargs="+", choices=range(1, 14),
                        default=list(range(1, 12)),
                        help="select isolated shapes; 12/13 use unsigned address induction")
    report = compile_shapes(parser.parse_args().shapes)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
