#!/usr/bin/env python3
"""Re-space functions in a C object toward their retail addresses.

IDO emits one contiguous .text section per source file.  A non-matching
function that is shorter than retail therefore moves every later function in
the object, even when those later functions compile byte-for-byte.  This tool
keeps every compiled instruction and relocation intact while inserting zero
filled gaps before functions at their retail-relative addresses. Oversized
non-matching functions keep their full compiled bodies in section-local
overflow regions and use short in-slot jump trampolines, preventing them from
displacing later functions.
"""

import argparse
import csv
import re
from pathlib import Path

from pad_generated_object import parse_object


def load_layout(path, filename):
    rows = []
    with Path(path).open(newline="") as stream:
        for row in csv.DictReader(stream):
            if row["filename"] != filename:
                continue
            rows.append({
                "name": row["function"],
                "address": int(row["address"], 16),
                "end": int(row["end"], 16),
                "section": row["section"],
            })
    if not rows:
        raise ValueError(f"no retail layout rows for {filename}")
    if len({row["section"] for row in rows}) != 1:
        raise ValueError(f"{filename} spans multiple retail sections")
    return sorted(rows, key=lambda row: row["address"])


def emit_padded_assembly(object_path, layout_path, filename):
    text, compiled, relocations = parse_object(object_path)
    retail = load_layout(layout_path, filename)
    retail_names = {row["name"] for row in retail}
    section = retail[0]["section"]
    for name in sorted(set(compiled) - retail_names):
        match = re.fullmatch(r"func_([0-9A-Fa-f]{8})", name)
        if not match:
            continue
        address = int(match.group(1), 16)
        retail.append({
            "name": name,
            "address": address,
            "end": address + compiled[name]["size"],
            "section": section,
        })
    retail.sort(key=lambda row: row["address"])
    for row, next_row in zip(retail, retail[1:]):
        row["end"] = min(row["end"], next_row["address"])
    retail_names = {row["name"] for row in retail}
    compiled_names = set(compiled)
    if retail_names != compiled_names:
        raise ValueError(
            f"function mismatch for {filename}: "
            f"missing={sorted(retail_names - compiled_names)}, "
            f"extra={sorted(compiled_names - retail_names)}"
        )

    base = retail[0]["address"]
    retail_end = max(row["end"] for row in retail) - base
    output = [
        '.section .text, "ax"',
        ".set noat",
        ".set noreorder",
        ".set gp=64",
        "",
        f"/* C-compiled functions re-spaced using {Path(layout_path).name}. */",
        "",
    ]
    current = 0
    overflow = []

    for row in retail:
        symbol = compiled[row["name"]]
        desired = row["address"] - base
        target = max(current, desired)
        if target > current:
            output.append(f".space 0x{target - current:X}, 0")

        name = row["name"]
        output.extend((f".globl {name}", f".type {name}, @function", f"{name}:"))
        start = symbol["value"]
        retail_size = row["end"] - row["address"]
        if symbol["size"] > retail_size:
            if retail_size < 8:
                raise ValueError(
                    f"{name} has only {retail_size} retail bytes for a trampoline"
                )
            overflow_name = f"__retail_overflow_{name}"
            output.extend((f"j {overflow_name}", "nop"))
            if retail_size > 8:
                output.append(f".space 0x{retail_size - 8:X}, 0")
            overflow.append((overflow_name, symbol))
            emitted_size = retail_size
        else:
            for relative in range(0, symbol["size"], 4):
                compact_offset = start + relative
                for relocation_name, relocation_symbol in relocations.get(
                    compact_offset, []
                ):
                    output.append(
                        f".reloc ., {relocation_name}, {relocation_symbol}"
                    )
                word = int.from_bytes(
                    text[compact_offset:compact_offset + 4], "big"
                )
                output.append(f".word 0x{word:08X}")
            emitted_size = symbol["size"]
        output.extend((f".size {name}, . - {name}", ""))
        current = target + emitted_size

    if retail_end > current:
        output.append(f".space 0x{retail_end - current:X}, 0")
    if overflow:
        output.extend(("", f'.section .{section}_overflow, "ax"', ""))
        for overflow_name, symbol in overflow:
            output.extend((f".type {overflow_name}, @function", f"{overflow_name}:"))
            start = symbol["value"]
            for relative in range(0, symbol["size"], 4):
                compact_offset = start + relative
                for relocation_name, relocation_symbol in relocations.get(
                    compact_offset, []
                ):
                    output.append(
                        f".reloc ., {relocation_name}, {relocation_symbol}"
                    )
                word = int.from_bytes(
                    text[compact_offset:compact_offset + 4], "big"
                )
                output.append(f".word 0x{word:08X}")
            output.extend((f".size {overflow_name}, . - {overflow_name}", ""))
    output.append("")
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("object", help="compact C-compiled relocatable object")
    parser.add_argument("layout", help="retail function layout CSV")
    parser.add_argument("filename", help="progress filename key")
    parser.add_argument("output", help="padded assembly output")
    args = parser.parse_args()
    Path(args.output).write_text(
        emit_padded_assembly(args.object, args.layout, args.filename),
        newline="\n",
    )


if __name__ == "__main__":
    main()
