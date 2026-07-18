#!/usr/bin/env python3

import csv
import re
import struct
import sys
from pathlib import Path


SLICE_SIZES = {
    "49D30": 0x6FF0,
    "58F80": 0x4340,
    "5D2C0": 0x41D0,
    "71820": 0x3890,
    "AEB40": 0x3670,
    "B3020": 0x9410,
    "11C2B0": 0x34D0,
    "133190": 0x2300,
    "13D350": 0x5210,
    "142560": 0xA8D0,
    "176A00": 0x3530,
    "179F30": 0x2BC0,
    "17CAF0": 0x6140,
    "185560": 0x2EE0,
    "18A8F0": 0x2960,
    "1B1600": 0x3D70,
    "1BA1D0": 0x4EC0,
    "1C2C60": 0x77C0,
    "1CC440": 0x4400,
    "1D6E80": 0x2470,
    "1D92F0": 0x3780,
    "1E73B0": 0x5D40,
    "1F4650": 0x6120,
    "1FA770": 0x5400,
    "20AE20": 0xAB40,
}


def generated_slice_replacement(name, _size):
    return f"build/src/game/generated_{name}.c.o(.text);"


REPLACEMENTS = {
    f"build/asm/{name}.s.o(.text);": generated_slice_replacement(name, size)
    for name, size in SLICE_SIZES.items()
}

OVERFLOW_SECTIONS = """
    /* Oversized non-matching C functions execute out-of-line so they cannot
       displace later byte-exact functions from their retail addresses. */
    init_overflow_ROM_START = __romPos;
    .init_overflow 0x10F00000 : AT(init_overflow_ROM_START)
    {
        *(.init_overflow);
    }
    __romPos += SIZEOF(.init_overflow);
    __romPos = ALIGN(__romPos, 16);

    game_overflow_ROM_START = __romPos;
    .game_overflow 0x15F00000 : AT(game_overflow_ROM_START)
    {
        *(.game_overflow);
    }
    __romPos += SIZEOF(.game_overflow);
    __romPos = ALIGN(__romPos, 16);

    debugger_overflow_ROM_START = __romPos;
    .debugger_overflow 0x16F00000 : AT(debugger_overflow_ROM_START)
    {
        *(.debugger_overflow);
    }
    __romPos += SIZEOF(.debugger_overflow);
    __romPos = ALIGN(__romPos, 16);

"""

def load_object_layout(path):
    grouped = {}
    with path.open(newline="") as stream:
        for row in csv.DictReader(stream):
            key = (row["section"], row["filename"])
            grouped.setdefault(key, []).append(
                (row["function"], int(row["address"], 16))
            )
    return grouped


def read_c_string(data, offset):
    end = data.find(b"\0", offset)
    if end < 0:
        raise ValueError("unterminated ELF string")
    return data[offset:end].decode("ascii")


def elf_text_info(path):
    data = path.read_bytes()
    header = struct.unpack_from(">16sHHIIIIIHHHHHH", data)
    section_offset = header[6]
    section_entry_size = header[11]
    section_count = header[12]
    section_names_index = header[13]
    section_format = struct.Struct(">IIIIIIIIII")
    sections = [
        section_format.unpack_from(data, section_offset + i * section_entry_size)
        for i in range(section_count)
    ]
    names_header = sections[section_names_index]
    names = data[names_header[4]:names_header[4] + names_header[5]]
    names_by_index = []
    text = None
    symtab = None
    for section in sections:
        end = names.find(b"\0", section[0])
        name = names[section[0]:end].decode("ascii")
        names_by_index.append(name)
        if name == ".text":
            text = section
        elif name == ".symtab":
            symtab = section
    if text is None or symtab is None:
        raise ValueError(f"no .text/.symtab section in {path}")

    strings = sections[symtab[6]]
    string_data = data[strings[4]:strings[4] + strings[5]]
    symbols = {}
    symbol_format = struct.Struct(">IIIBBH")
    entry_size = symtab[9] or symbol_format.size
    for offset in range(symtab[4], symtab[4] + symtab[5], entry_size):
        name_offset, value, _size, _info, _other, section = symbol_format.unpack_from(
            data, offset
        )
        if section != names_by_index.index(".text") or not name_offset:
            continue
        symbols[read_c_string(string_data, name_offset)] = value
    return text[5], symbols


def anchor_objects(text, object_layout, project_dir):
    section_start = re.compile(
        r"^\s*\.(init|game|debugger)(?:\s+(0x[0-9A-Fa-f]+))?\s*:"
    )
    object_line = re.compile(
        r"^(?P<indent>\s*)build/(?P<path>[^;]+\.[cs]\.o)\(\.text\);$"
    )
    default_starts = {"game": 0x15000000, "debugger": 0x16000000}
    output = []
    current_section = None
    current = None

    for line in text.splitlines():
        match = section_start.match(line)
        if match:
            current_section = match.group(1)
            current = (
                int(match.group(2), 16)
                if match.group(2)
                else default_starts.get(current_section)
            )

        if current_section and re.search(
            rf"{current_section}_TEXT_END\s*=\s*\.", line
        ):
            output.append(line)
            current_section = None
            current = None
            continue
        if current is None:
            output.append(line)
            continue

        match = object_line.match(line)
        if not match:
            output.append(line)
            continue
        object_path = project_dir / "build" / match.group("path")
        current = (current + 15) & ~15
        filename = Path(match.group("path")).name
        for suffix in (".c.o", ".s.o"):
            if filename.endswith(suffix):
                filename = filename.removesuffix(suffix)
                break
        text_size, symbols = elf_text_info(object_path)
        layout = object_layout.get((current_section, filename), [])
        anchors = [
            (address, address - symbols[name])
            for name, address in layout
            if name in symbols
        ]
        retail_start = min(anchors)[1] if anchors else None
        if retail_start is not None and current <= retail_start:
            output.append(
                f"{match.group('indent')}. = ABSOLUTE(0x{retail_start:08X});"
            )
            current = retail_start
        output.append(line)
        current += text_size
    return "\n".join(output) + "\n"


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print(f"usage: {sys.argv[0]} <linker-script> [version]", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    version = sys.argv[2] if len(sys.argv) == 3 else "us"
    text = path.read_text()
    if version != "us":
        path.write_text(text)
        return 0
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    text = text.replace("    /DISCARD/ :", OVERFLOW_SECTIONS + "    /DISCARD/ :")
    layout_path = path.parent.parent / "retail_layout.us.txt"
    text = anchor_objects(
        text, load_object_layout(layout_path), path.parent.parent
    )
    path.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
