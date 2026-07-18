#!/usr/bin/env python3
"""Re-space generated C functions at their retail text addresses.

The generated game slices intentionally contain small, non-matching C
placeholders. Compiling them normally packs every function together and
changes the addresses of every later symbol. This tool reads the compiler's
relocatable ELF object, keeps each function's compiled instruction bytes and
relocations, and emits assembly that places those bytes at the function's
original offset from the preserved raw-assembly slice. The gaps are zero-filled
MIPS nops. Exported jump-table labels are restored at their retail offsets too.

The result is still C-derived code: only inter-function layout is changed.
"""

import argparse
import re
import struct
from collections import defaultdict
from pathlib import Path


ELF_HEADER = struct.Struct(">16sHHIIIIIHHHHHH")
SECTION_HEADER = struct.Struct(">IIIIIIIIII")
SYMBOL = struct.Struct(">IIIBBH")
RELOCATION = struct.Struct(">II")

SHT_REL = 9
STT_FUNC = 2

RELOCATION_NAMES = {
    2: "R_MIPS_32",
    4: "R_MIPS_26",
    5: "R_MIPS_HI16",
    6: "R_MIPS_LO16",
}


def read_c_string(data, offset):
    end = data.find(b"\0", offset)
    if end < 0:
        raise ValueError("unterminated ELF string")
    return data[offset:end].decode("ascii")


def parse_object(path):
    data = Path(path).read_bytes()
    header = ELF_HEADER.unpack_from(data)
    ident = header[0]
    if ident[:4] != b"\x7fELF" or ident[4] != 1 or ident[5] != 2:
        raise ValueError(f"{path} is not a 32-bit big-endian ELF object")

    section_offset = header[6]
    section_entry_size = header[11]
    section_count = header[12]
    section_names_index = header[13]
    if section_entry_size != SECTION_HEADER.size:
        raise ValueError(f"unsupported section header size {section_entry_size}")

    sections = []
    for index in range(section_count):
        values = SECTION_HEADER.unpack_from(
            data, section_offset + index * section_entry_size
        )
        sections.append({
            "index": index,
            "name_offset": values[0],
            "type": values[1],
            "offset": values[4],
            "size": values[5],
            "link": values[6],
            "info": values[7],
            "entry_size": values[9],
        })

    section_names = sections[section_names_index]
    section_name_data = data[
        section_names["offset"]:section_names["offset"] + section_names["size"]
    ]
    for section in sections:
        section["name"] = read_c_string(section_name_data, section["name_offset"])

    by_name = {section["name"]: section for section in sections}
    text = by_name[".text"]
    symtab = by_name[".symtab"]
    strtab = sections[symtab["link"]]
    string_data = data[strtab["offset"]:strtab["offset"] + strtab["size"]]

    symbols = []
    entry_size = symtab["entry_size"] or SYMBOL.size
    for offset in range(symtab["offset"], symtab["offset"] + symtab["size"], entry_size):
        values = SYMBOL.unpack_from(data, offset)
        symbols.append({
            "name": read_c_string(string_data, values[0]),
            "value": values[1],
            "size": values[2],
            "type": values[3] & 0xF,
            "section": values[5],
        })

    relocations = defaultdict(list)
    for section in sections:
        if section["type"] != SHT_REL or section["info"] != text["index"]:
            continue
        entry_size = section["entry_size"] or RELOCATION.size
        for offset in range(
            section["offset"], section["offset"] + section["size"], entry_size
        ):
            relocation_offset, info = RELOCATION.unpack_from(data, offset)
            symbol_index = info >> 8
            relocation_type = info & 0xFF
            if relocation_type not in RELOCATION_NAMES:
                raise ValueError(
                    f"unsupported relocation type {relocation_type} at "
                    f"0x{relocation_offset:X}"
                )
            relocations[relocation_offset].append(
                (RELOCATION_NAMES[relocation_type], symbols[symbol_index]["name"])
            )

    functions = {
        symbol["name"]: symbol
        for symbol in symbols
        if symbol["type"] == STT_FUNC
        and symbol["section"] == text["index"]
        and symbol["size"]
    }
    text_data = data[text["offset"]:text["offset"] + text["size"]]
    return text_data, functions, relocations


def parse_retail_slice(path):
    instruction = re.compile(
        r"/\*\s*([0-9A-Fa-f]+)\s+([0-9A-Fa-f]{8})\s+"
        r"[0-9A-Fa-f]{8}\s*\*/"
    )
    label = re.compile(r"^\s*(glabel|jlabel)\s+(\S+)")
    pending = []
    functions = {}
    jump_labels = defaultdict(list)
    addresses = []

    for line in Path(path).read_text().splitlines():
        match = label.match(line)
        if match:
            pending.append((match.group(1), match.group(2)))
            continue
        match = instruction.search(line)
        if not match:
            continue
        address = int(match.group(2), 16)
        addresses.append(address)
        for kind, name in pending:
            if kind == "glabel":
                functions[name] = address
            else:
                jump_labels[address].append(name)
        pending.clear()

    if pending:
        raise ValueError(f"labels without instructions in {path}: {pending}")
    if not addresses or not functions:
        raise ValueError(f"no text functions found in {path}")
    return min(addresses), max(addresses) + 4, functions, jump_labels


def emit_padded_assembly(object_path, retail_path):
    text, compiled, relocations = parse_object(object_path)
    retail_start, retail_end, retail, jump_labels = parse_retail_slice(retail_path)

    missing = sorted(set(retail) - set(compiled))
    extra = sorted(set(compiled) - set(retail))
    if missing or extra:
        raise ValueError(
            f"function mismatch for {retail_path}: missing={missing}, extra={extra}"
        )

    functions = sorted(
        ((address - retail_start, name, compiled[name]) for name, address in retail.items())
    )
    label_offsets = {
        address - retail_start: names for address, names in jump_labels.items()
    }
    slice_size = retail_end - retail_start
    output = [
        '.section .text, "ax"',
        ".set noat",
        ".set noreorder",
        ".set gp=64",
        "",
        f"/* C-compiled functions padded to retail layout from {Path(retail_path).name}. */",
        "",
    ]
    current = 0
    emitted_labels = set()

    def emit_labels(offset):
        for name in label_offsets.get(offset, []):
            if name in emitted_labels:
                continue
            output.append(f".globl {name}")
            output.append(f"{name}:")
            emitted_labels.add(name)

    def pad_to(target):
        nonlocal current
        for offset in sorted(
            value for value in label_offsets if current <= value < target
        ):
            if offset > current:
                output.append(f".space 0x{offset - current:X}, 0")
                current = offset
            emit_labels(offset)
        if target > current:
            output.append(f".space 0x{target - current:X}, 0")
            current = target

    for index, (target, name, symbol) in enumerate(functions):
        pad_to(target)
        emit_labels(target)
        next_target = functions[index + 1][0] if index + 1 < len(functions) else slice_size
        if symbol["size"] > next_target - target:
            raise ValueError(
                f"compiled {name} is 0x{symbol['size']:X} bytes but its retail "
                f"span is only 0x{next_target - target:X}"
            )

        output.extend((f".globl {name}", f".type {name}, @function", f"{name}:"))
        start = symbol["value"]
        for relative in range(0, symbol["size"], 4):
            emit_labels(target + relative)
            compact_offset = start + relative
            for relocation_name, relocation_symbol in relocations.get(compact_offset, []):
                output.append(
                    f".reloc ., {relocation_name}, {relocation_symbol}"
                )
            word = int.from_bytes(text[compact_offset:compact_offset + 4], "big")
            output.append(f".word 0x{word:08X}")
        output.append(f".size {name}, . - {name}")
        output.append("")
        current = target + symbol["size"]

    pad_to(slice_size)
    emit_labels(slice_size)
    expected_labels = {name for names in jump_labels.values() for name in names}
    if emitted_labels != expected_labels:
        missing_labels = sorted(expected_labels - emitted_labels)
        raise ValueError(f"failed to emit jump labels: {missing_labels}")
    output.append("")
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("object", help="compact C-compiled relocatable object")
    parser.add_argument("retail_asm", help="preserved raw assembly slice")
    parser.add_argument("output", help="padded assembly output")
    args = parser.parse_args()
    Path(args.output).write_text(
        emit_padded_assembly(args.object, args.retail_asm), newline="\n"
    )


if __name__ == "__main__":
    main()
