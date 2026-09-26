#!/usr/bin/env python3
"""Re-space functions in a C object toward their retail addresses.

IDO emits one contiguous .text section per source file. A non-matching
function that is shorter than retail therefore moves every later function in
the object, even when those later functions compile byte-for-byte.  This tool
keeps every compiled instruction and relocation intact while inserting zero
filled gaps before functions at their retail-relative addresses. Oversized
non-matching functions keep their full compiled bodies in section-local
overflow regions and use short in-slot jump trampolines, preventing them from
displacing later functions. An optional guarded table can replace known
compiler-scheduling words or insert a non-relocated scheduling word after
verifying the compiled input value. Patches may also move relocations when
both the expected and replacement lists are declared explicitly.
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


def load_word_patches(path, filename):
    if path is None:
        return {}

    patches = {}
    with Path(path).open(newline="") as stream:
        for row in csv.DictReader(stream):
            if row["filename"] != filename:
                continue
            key = (row["function"], int(row["offset"], 0))
            if key in patches:
                raise ValueError(
                    f"duplicate word patch for {key[0]} at 0x{key[1]:X}"
                )
            patches[key] = {
                "expected": int(row["expected"], 0),
                "replacement": int(row["replacement"], 0),
                "expected_relocations": parse_relocation_spec(
                    row.get("expected_relocations")
                ),
                "replacement_relocations": parse_relocation_spec(
                    row.get("replacement_relocations")
                ),
                "insert_after": parse_optional_word(row.get("insert_after")),
                "note": row.get("note", ""),
            }
            if ((patches[key]["expected_relocations"] is None) !=
                    (patches[key]["replacement_relocations"] is None)):
                raise ValueError(
                    f"word patch for {key[0]} at 0x{key[1]:X} must declare "
                    "both relocation fields"
                )
    return patches


def parse_optional_word(value):
    if value is None or not value.strip():
        return None
    return int(value, 0)


def parse_relocation_spec(value):
    if value is None or not value.strip():
        return None
    if value.strip() == "-":
        return []

    relocations = []
    for item in value.split(";"):
        relocation_type, separator, symbol = item.strip().partition(":")
        if not separator or not relocation_type or not symbol:
            raise ValueError(f"invalid relocation specification: {value}")
        relocations.append((relocation_type, symbol))
    return relocations


def emit_padded_assembly(
    object_path, layout_path, filename, rodata_symbol=None, word_patches_path=None
):
    text, compiled, relocations = parse_object(object_path)
    retail = load_layout(layout_path, filename)
    word_patches = load_word_patches(word_patches_path, filename)
    applied_patches = set()
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
            for relative in range(0, retail_size, 4):
                word = 0x08000000 if relative == 0 else 0
                word_relocations = (
                    [("R_MIPS_26", overflow_name)] if relative == 0 else []
                )
                patch_key = (name, relative)
                patch = word_patches.get(patch_key)
                if patch is not None:
                    if patch["insert_after"] is not None:
                        raise ValueError(
                            f"overflow trampoline patch for {name}+0x{relative:X} "
                            "cannot insert a word"
                        )
                    if word != patch["expected"]:
                        raise ValueError(
                            f"stale overflow word patch for {name}+0x{relative:X}: "
                            f"expected 0x{patch['expected']:08X}, "
                            f"generated 0x{word:08X}"
                        )
                    expected_relocations = patch["expected_relocations"]
                    if (expected_relocations is not None and
                            word_relocations != expected_relocations):
                        raise ValueError(
                            f"stale overflow relocations for {name}+0x{relative:X}: "
                            f"expected {expected_relocations}, "
                            f"generated {word_relocations}"
                        )
                    if expected_relocations is not None:
                        word_relocations = patch["replacement_relocations"]
                    word = patch["replacement"]
                    applied_patches.add(patch_key)
                for relocation_name, relocation_symbol in word_relocations:
                    output.append(
                        f".reloc ., {relocation_name}, {relocation_symbol}"
                    )
                output.append(f".word 0x{word:08X}")
            overflow.append((overflow_name, symbol))
            emitted_size = retail_size
        else:
            inserted_size = sum(
                4
                for (patch_name, _), patch in word_patches.items()
                if patch_name == name and patch["insert_after"] is not None
            )
            if symbol["size"] + inserted_size > retail_size:
                raise ValueError(
                    f"patched {name} is 0x{symbol['size'] + inserted_size:X} "
                    f"bytes but its retail slot is 0x{retail_size:X}"
                )
            for relative in range(0, symbol["size"], 4):
                compact_offset = start + relative
                word_relocations = list(relocations.get(compact_offset, []))
                word = int.from_bytes(
                    text[compact_offset:compact_offset + 4], "big"
                )
                patch_key = (name, relative)
                patch = word_patches.get(patch_key)
                if patch is not None:
                    if word != patch["expected"]:
                        raise ValueError(
                            f"stale word patch for {name}+0x{relative:X}: "
                            f"expected 0x{patch['expected']:08X}, "
                            f"compiled 0x{word:08X}"
                        )
                    expected_relocations = patch["expected_relocations"]
                    if (expected_relocations is not None and
                            word_relocations != expected_relocations):
                        raise ValueError(
                            f"stale relocations for {name}+0x{relative:X}: "
                            f"expected {expected_relocations}, "
                            f"compiled {word_relocations}"
                        )
                    if expected_relocations is not None:
                        word_relocations = patch["replacement_relocations"]
                    word = patch["replacement"]
                    applied_patches.add(patch_key)
                for relocation_name, relocation_symbol in word_relocations:
                    if (
                        rodata_symbol is not None
                        and relocation_symbol == ".rodata"
                    ):
                        relocation_symbol = rodata_symbol
                    output.append(
                        f".reloc ., {relocation_name}, {relocation_symbol}"
                    )
                output.append(f".word 0x{word:08X}")
                if patch is not None and patch["insert_after"] is not None:
                    output.append(f".word 0x{patch['insert_after']:08X}")
            emitted_size = symbol["size"] + inserted_size
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
                    if (
                        rodata_symbol is not None
                        and relocation_symbol == ".rodata"
                    ):
                        relocation_symbol = rodata_symbol
                    output.append(
                        f".reloc ., {relocation_name}, {relocation_symbol}"
                    )
                word = int.from_bytes(
                    text[compact_offset:compact_offset + 4], "big"
                )
                output.append(f".word 0x{word:08X}")
            output.extend((f".size {overflow_name}, . - {overflow_name}", ""))
    unapplied_patches = set(word_patches) - applied_patches
    if unapplied_patches:
        formatted = ", ".join(
            f"{name}+0x{offset:X}" for name, offset in sorted(unapplied_patches)
        )
        raise ValueError(f"word patches were not applied: {formatted}")
    output.append("")
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("object", help="compact C-compiled relocatable object")
    parser.add_argument("layout", help="retail function layout CSV")
    parser.add_argument("filename", help="progress filename key")
    parser.add_argument("output", help="padded assembly output")
    parser.add_argument(
        "--rodata-symbol",
        help="retail symbol corresponding to offset zero of compact .rodata",
    )
    parser.add_argument(
        "--word-patches",
        help="CSV of guarded compiled-word replacements",
    )
    args = parser.parse_args()
    Path(args.output).write_text(
        emit_padded_assembly(
            args.object,
            args.layout,
            args.filename,
            rodata_symbol=args.rodata_symbol,
            word_patches_path=args.word_patches,
        ),
        newline="\n",
    )


if __name__ == "__main__":
    main()
