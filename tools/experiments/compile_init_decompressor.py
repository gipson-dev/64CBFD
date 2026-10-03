"""Compile two isolated guest profiles; never touch the production owner/link."""

import argparse
import json
import os
import struct
import subprocess
from pathlib import Path


def inspect_object(path):
    data = path.read_bytes()
    header = struct.unpack_from(">16sHHIIIIIHHHHHH", data)
    if data[:6] != b"\x7fELF\x01\x02" or header[2] != 8:
        raise ValueError("expected a big-endian ELF32 MIPS object")
    sections = [struct.unpack_from(">IIIIIIIIII", data, header[6] + i * header[11])
                for i in range(header[12])]
    names = sections[header[13]]
    strings = data[names[4]:names[4] + names[5]]

    def name(table, offset):
        return table[offset:].split(b"\0", 1)[0].decode()

    indices = {name(strings, section[0]): i for i, section in enumerate(sections)}
    text_index = indices[".text"]
    text = sections[text_index]
    symbols = sections[indices[".symtab"]]
    symbol_strings = sections[symbols[6]]
    symbol_strings = data[symbol_strings[4]:symbol_strings[4] + symbol_strings[5]]
    functions = []
    size_symbol = None
    frame_symbol = None
    for offset in range(symbols[4], symbols[4] + symbols[5], symbols[9]):
        symbol = struct.unpack_from(">IIIBBH", data, offset)
        label = name(symbol_strings, symbol[0])
        if symbol[3] & 15 == 2 and symbol[5] == text_index:
            functions.append((symbol[1], label))
        if label == "init_decode_guest_sizes":
            size_symbol = symbol
        if label == "init_decode_guest_frame_layout":
            frame_symbol = symbol
    functions.sort()
    measurements = []
    for i, (start, label) in enumerate(functions):
        end = functions[i + 1][0] if i + 1 < len(functions) else text[5]
        words = struct.unpack_from(">%dI" % ((end - start) // 4), data, text[4] + start)
        returns = [index for index, word in enumerate(words) if word == 0x03E00008]
        body_words = max(returns) + 2 if returns else len(words)
        frames = [0x10000 - (word & 0xFFFF) for word in words[:12]
                  if word >> 16 == 0x27BD and word & 0x8000]
        measurements.append({"function": label, "slot_words": len(words),
                             "body_words": body_words, "frame_bytes": max(frames, default=0)})
    if size_symbol is None:
        raise ValueError("guest layout size symbol missing")
    section = sections[size_symbol[5]]
    entry_size, state_size = struct.unpack_from(">2I", data, section[4] + size_symbol[1])
    if frame_symbol is None:
        raise ValueError("guest frame layout symbol missing")
    section = sections[frame_symbol[5]]
    frame_layout = struct.unpack_from(">24I", data, section[4] + frame_symbol[1])
    expected_layout = (0xA88, 0, 0x44, 0x84, 0x504, 0x548, 0x9C8, 0x9CC,
                       0x9D0, 0x9D4, 0xA38, 0xA3A, 0xA3C, 0xA40, 0xA44,
                       0xA48, 0xA68, 0xA6C, 0xA70, 0xA74, 0xA78, 0xA7C,
                       0xA80, 0xA84)
    if frame_layout != expected_layout:
        raise ValueError("guest frame differs from recovered retail offsets")
    return {"text_bytes": text[5], "entry_bytes": entry_size,
            "state_bytes": state_size, "frame_layout": frame_layout,
            "functions": measurements}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = (args.output or root / "conker/build/init-decompressor-semantic").resolve()
    output.mkdir(parents=True, exist_ok=True)
    cwd = root / "conker"
    compiler = "../ido/ido5.3_recomp/cc"
    source = Path(__file__).with_name("init_decompressor_semantic.c")
    common = [str(compiler), "-c", "-32", "-G", "0", "-Xfullwarn", "-Xcpluscomm",
              "-signed", "-nostdinc", "-non_shared", "-Wab,-r4300_mul",
              "-mips2", "-o32", "-DINIT_DECODE_GUEST"]
    report = {}
    for label, profile in (("o2g3", ["-O2", "-g3"]), ("o1", ["-O1"])):
        obj = output / (label + ".o")
        obj.unlink(missing_ok=True)
        result = subprocess.run(
            [*common, *profile, "-o", os.path.relpath(obj, cwd),
             os.path.relpath(source, cwd)], cwd=cwd, capture_output=True, text=True)
        (output / (label + ".log")).write_text(result.stdout + result.stderr)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        if not obj.is_file():
            raise RuntimeError("compiler returned success without producing " + str(obj))
        disassembly = subprocess.check_output(
            ["mips-linux-gnu-objdump", "-dr", "-z", str(obj)], text=True)
        (output / (label + ".asm.txt")).write_text(disassembly)
        report[label] = inspect_object(obj)
    (output / "measurements.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
