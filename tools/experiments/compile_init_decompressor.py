"""Compile two isolated guest profiles; never touch the production owner/link."""

import argparse
import json
import os
import struct
import subprocess
from pathlib import Path


def analyze_guest_calls(text, named_entries, targets):
    """Conservative direct-JAL frame sum, including unnamed IDO helper entries."""
    if len(text) & 3:
        raise ValueError("text length is not word aligned")
    starts = sorted({0, *named_entries, *targets.values()})
    if any(start < 0 or start >= len(text) or start & 3 for start in starts):
        raise ValueError("call target is not a text instruction")
    units = {}
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(text)
        words = struct.unpack_from(">%dI" % ((end - start) // 4), text, start)
        frames = [0x10000 - (word & 0xFFFF) for word in words
                  if word >> 16 == 0x27BD and word & 0x8000]
        if len(frames) > 1:
            raise ValueError("multiple stack allocations need control-flow analysis")
        calls = set()
        for offset, word in enumerate(words):
            if word >> 26 == 2:
                raise ValueError("absolute jump needs separate tail-transfer qualification")
            if word >> 26 == 3:
                pc = start + offset * 4
                if pc not in targets:
                    raise ValueError("direct JAL lacks a resolved relocation")
                calls.add(targets[pc])
            if word >> 26 == 0 and word & 63 == 9:
                raise ValueError("indirect JALR needs separate call-graph qualification")
        units[start] = {"entry": start, "name": named_entries.get(start, "local_%04x" % start),
                        "frame_bytes": max(frames, default=0), "calls": sorted(calls),
                        "word_store_forms": {name: sum(word >> 26 == opcode for word in words)
                                             for name, opcode in (("sw", 43), ("swl", 42), ("swr", 46))}}

    def bound(start, active=()):
        if start in active:
            raise ValueError("recursive call graph has no finite static frame sum")
        unit = units[start]
        return unit["frame_bytes"] + max((bound(target, (*active, start))
                                         for target in unit["calls"]), default=0)

    for start, unit in units.items():
        unit["direct_call_frame_bound"] = bound(start)
    return list(units.values())


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
    entry_layout_symbol = None
    symbol_records = []
    for offset in range(symbols[4], symbols[4] + symbols[5], symbols[9]):
        symbol = struct.unpack_from(">IIIBBH", data, offset)
        symbol_records.append(symbol)
        label = name(symbol_strings, symbol[0])
        if symbol[3] & 15 == 2 and symbol[5] == text_index:
            functions.append((symbol[1], label))
        if label == "init_decode_guest_sizes":
            size_symbol = symbol
        if label == "init_decode_guest_frame_layout":
            frame_symbol = symbol
        if label == "init_decode_entry_layout":
            entry_layout_symbol = symbol
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
    if entry_layout_symbol is None:
        raise ValueError("entry layout receipt missing")
    section = sections[entry_layout_symbol[5]]
    entry_layout = struct.unpack_from(">5I", data, section[4] + entry_layout_symbol[1])
    if entry_layout[0] != 4 or entry_layout[1] not in (2, 4) or entry_layout[2:] != (0, 1, 2):
        raise ValueError("entry byte layout differs from retail")
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
    relocations = sections[indices[".rel.text"]]
    targets = {}
    for offset in range(relocations[4], relocations[4] + relocations[5], relocations[9]):
        pc, info = struct.unpack_from(">2I", data, offset)
        if info & 255 != 4:
            continue
        word = struct.unpack_from(">I", data, text[4] + pc)[0]
        if word >> 26 != 3:
            raise ValueError("non-JAL R_MIPS_26 transfer needs separate qualification")
        symbol = symbol_records[info >> 8]
        if symbol[5] != text_index:
            raise ValueError("external call has no local frame measurement")
        targets[pc] = symbol[1] + ((word & 0x03FFFFFF) << 2)
    call_graph = analyze_guest_calls(data[text[4]:text[4] + text[5]],
                                    {start: label for start, label in functions}, targets)
    return {"text_bytes": text[5], "entry_bytes": entry_size,
            "entry_layout": entry_layout,
            "state_bytes": state_size, "frame_layout": frame_layout,
            "functions": measurements, "call_graph": call_graph}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--frame-backed", action="store_true",
                        help="compile the isolated physical-frame scratch variant")
    parser.add_argument("--flat-bits", action="store_true",
                        help="flatten take_bits without changing state-access order")
    parser.add_argument("--aligned-entry", action="store_true",
                        help="give the four-byte entry its retail word alignment")
    parser.add_argument("--packed-entry", action="store_true",
                        help="construct a packed leaf word; implies --aligned-entry")
    parser.add_argument("--bounded-builder-shifts", action="store_true",
                        help="use the builder's clamped tree-width shift bounds")
    parser.add_argument("--cache-workspace", action="store_true",
                        help="capture the builder's stable workspace pointer")
    parser.add_argument("--byte-parent", action="store_true",
                        help="use byte-offset parent lookup; requires --frame-backed")
    parser.add_argument("--no-unroll", action="store_true",
                        help="disable IDO loop unrolling for both guest profiles")
    parser.add_argument("--local-allocated", action="store_true",
                        help="hold builder allocation cursor locally; commit every allocation")
    parser.add_argument("--cache-dynamic-lengths", action="store_true",
                        help="capture the dynamic decoder's stable length-buffer base")
    parser.add_argument("--dynamic-cursor", action="store_true",
                        help="write decoded lengths through a bounded pointer cursor")
    parser.add_argument("--cache-dynamic-code", nargs="?", const="all",
                        choices=("all", "mask", "inline"),
                        help="select captured lookup state, mask-only capture or inline mask")
    parser.add_argument("--cache-builder", nargs="?", const="all",
                        choices=("all", "counts-offsets"),
                        help="capture the builder's scratch array bases")
    args = parser.parse_args()
    if args.byte_parent and not args.frame_backed:
        parser.error("--byte-parent requires --frame-backed")
    if args.packed_entry:
        args.aligned_entry = True
    root = Path(__file__).resolve().parents[2]
    suffix = "-frame" if args.frame_backed else ""
    if args.flat_bits:
        suffix += "-flat-bits"
    if args.aligned_entry:
        suffix += "-aligned-entry"
    if args.packed_entry:
        suffix += "-packed"
    if args.bounded_builder_shifts:
        suffix += "-bounded-shifts"
    if args.cache_workspace:
        suffix += "-cached-workspace"
    if args.byte_parent:
        suffix += "-byte-parent"
    if args.no_unroll:
        suffix += "-no-unroll"
    if args.local_allocated:
        suffix += "-local-allocated"
    if args.cache_dynamic_lengths:
        suffix += "-cached-dynamic-lengths"
    if args.dynamic_cursor:
        suffix += "-dynamic-cursor"
    if args.cache_dynamic_code:
        suffix += "-cached-dynamic-code"
        if args.cache_dynamic_code != "all":
            suffix += "-" + args.cache_dynamic_code
    if args.cache_builder:
        suffix += "-cached-builder"
        if args.cache_builder != "all":
            suffix += "-" + args.cache_builder
    output = (args.output or root / ("conker/build/init-decompressor-semantic" + suffix)).resolve()
    output.mkdir(parents=True, exist_ok=True)
    cwd = root / "conker"
    compiler = "../ido/ido5.3_recomp/cc"
    source = Path(__file__).with_name("init_decompressor_semantic.c")
    common = [str(compiler), "-c", "-32", "-G", "0", "-Xfullwarn", "-Xcpluscomm",
              "-signed", "-nostdinc", "-non_shared", "-Wab,-r4300_mul",
              "-mips2", "-o32", "-DINIT_DECODE_GUEST"]
    if args.frame_backed:
        common.append("-DINIT_DECODE_FRAME_BACKED")
    if args.flat_bits:
        common.append("-DINIT_DECODE_FLAT_BITS")
    if args.aligned_entry:
        common.append("-DINIT_DECODE_ALIGNED_ENTRY")
    if args.packed_entry:
        common.append("-DINIT_DECODE_PACKED_ENTRY")
    if args.bounded_builder_shifts:
        common.append("-DINIT_DECODE_BOUNDED_BUILDER_SHIFTS")
    if args.cache_workspace:
        common.append("-DINIT_DECODE_CACHE_WORKSPACE")
    if args.byte_parent:
        common.append("-DINIT_DECODE_BYTE_PARENT")
    if args.no_unroll:
        common.append("-Wo,-loopunroll,0")
    if args.local_allocated:
        common.append("-DINIT_DECODE_LOCAL_ALLOCATED")
    if args.cache_dynamic_lengths:
        common.append("-DINIT_DECODE_CACHE_DYNAMIC_LENGTHS")
    if args.dynamic_cursor:
        common.append("-DINIT_DECODE_DYNAMIC_CURSOR")
    if args.cache_dynamic_code:
        common.append("-DINIT_DECODE_CACHE_DYNAMIC_CODE=" +
                      str({"all": 1, "mask": 2, "inline": 3}[args.cache_dynamic_code]))
    if args.cache_builder:
        common.append("-DINIT_DECODE_CACHE_BUILDER=" +
                      ("1" if args.cache_builder == "all" else "2"))
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
        if report[label]["entry_layout"][1] != (4 if args.aligned_entry else 2):
            raise ValueError("entry alignment does not match the selected representation")
    (output / "measurements.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
