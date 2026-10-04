#!/usr/bin/env python3

import csv
import re
import struct
import sys
from collections import Counter
from pathlib import Path

import yaml


def generated_slice_replacement(name):
    return f"build/src/game/generated_{name}.c.o(.text);"


def anchor_init_math_rodata(text):
    # Earlier recovered audio objects omit rodata; keep SDK math constants
    # at their retail addresses rather than relying on absolute symbol aliases.
    marker = "        build/asm/data/2C850.rodata.s.o(.rodata);"
    anchor = "        . = ABSOLUTE(0x8002C850);\n"
    return text.replace(marker, anchor + marker)


def restore_init_audio_data_order(text):
    start_marker = "        init_data_DATA_START = .;"
    end_marker = "        init_data_RODATA_END = .;"
    if start_marker not in text:
        return text
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    block = text[start:end]

    def move_before(owners, target, anchor=None):
        nonlocal block
        lines = [f"        build/{owner};\n" for owner in owners]
        target_line = f"        build/{target};\n"
        for line in lines + [target_line]:
            if block.count(line) != 1:
                raise ValueError(f"expected one Init data owner: {line.strip()}")
        for line in lines:
            block = block.replace(line, "")
        replacement = "".join(lines)
        if anchor is not None:
            replacement += f"        . = ABSOLUTE(0x{anchor:08X});\n"
        block = block.replace(target_line, replacement + target_line)

    # Splat groups input sections by ELF type, but the retail Init audio
    # data/rodata owners alternate. Keep jump tables at their physical addresses.
    move_before(
        [f"asm/data/{address}.rodata.s.o(.rodata)"
         for address in ("2C0C0", "2C120", "2C1B0", "2C200", "2C240")],
        "assets/2C250.bin.o(.data)",
    )
    move_before(
        ["src/libultra/audio/init_128D0.c.o(.rodata)"],
        "assets/2C460.bin.o(.data)", 0x8002C460,
    )
    move_before(
        ["asm/data/2C750.rodata.s.o(.rodata)",
         "src/libultra/audio/cents2ratio.c.o(.rodata)",
         "asm/data/2C770.rodata.s.o(.rodata)",
         "src/libultra/audio/init_1D900.c.o(.rodata)"],
        "assets/2C7A0.bin.o(.data)", 0x8002C7A0,
    )
    marker = "        build/asm/data/2C770.rodata.s.o(.rodata);"
    block = block.replace(marker, "        . = ABSOLUTE(0x8002C770);\n" + marker)
    return text[:start] + block + text[end:]


def load_game_data_layout(project_dir):
    config = yaml.safe_load((project_dir / "conker.us.yaml").read_text())
    if not isinstance(config, dict) or not isinstance(config.get("segments"), list):
        raise ValueError("Game data YAML needs a segment list")
    segments = config["segments"]
    matches = [i for i, segment in enumerate(segments)
               if isinstance(segment, dict) and segment.get("name") == "game_data"]
    if len(matches) != 1:
        raise ValueError("expected one Game data YAML segment")
    index = matches[0]
    if index + 1 >= len(segments):
        raise ValueError("Game data YAML segment needs an end boundary")
    segment = segments[index]
    following = segments[index + 1]
    if not isinstance(following, dict) and not (isinstance(following, list) and following):
        raise ValueError("invalid Game data end segment")
    end = following.get("start") if isinstance(following, dict) else following[0]
    start, vram = segment.get("start"), segment.get("vram")
    entries = segment.get("subsegments")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Game data YAML needs nonempty owner entries")
    for entry in entries:
        if not isinstance(entry, list) or len(entry) not in (2, 3):
            raise ValueError(f"malformed Game data owner: {entry}")
        if type(entry[0]) is not int or entry[0] < 0 or entry[0] & 3:
            raise ValueError(f"unaligned or invalid Game data owner: {entry}")
        if len(entry) == 3 and (not isinstance(entry[2], str) or
                               not re.fullmatch(r"[A-Za-z0-9_/-]+", entry[2]) or
                               any(part in ("", ".", "..") for part in entry[2].split("/"))):
            raise ValueError(f"invalid Game data owner name: {entry}")
    if any(type(value) is not int or not 0 <= value <= 0xFFFFFFFF
           for value in (start, vram, end)) or vram & 3 or vram + end - start > 0xFFFFFFFF:
        raise ValueError("invalid Game data segment boundaries")
    offsets = [entry[0] for entry in entries] + [end]
    if not offsets or offsets[0] != start or any(a >= b for a, b in zip(offsets, offsets[1:])):
        raise ValueError("Game data YAML spans must be contiguous and increasing")
    owners = []
    for entry, next_offset in zip(entries, offsets[1:]):
        offset, kind = entry[:2]
        name = entry[2] if len(entry) == 3 else f"{offset:X}"
        if kind in ("data", "rodata"):
            path, section = f"asm/data/{name}.{kind}.s.o", f".{kind}"
        elif kind == "bin":
            path, section = f"assets/{name}.bin.o", ".data"
        elif kind == ".rodata" and len(entry) == 3:
            path, section = f"src/{name}.c.o", ".rodata"
        else:
            raise ValueError(f"unsupported Game data owner: {entry}")
        owners.append({"rom": offset, "address": vram + offset - start,
                       "end": vram + next_offset - start, "section": section,
                       "input": f"build/{path}({section})"})
    if len({owner["input"] for owner in owners}) != len(owners):
        raise ValueError("duplicate Game data YAML owner")
    return start, vram, end, owners


def restore_game_data_order(text, project_dir):
    if "game_data_DATA_START" not in text:
        return text
    start_marker = "        game_data_DATA_START = .;"
    end_marker = "        game_data_RODATA_END = .;"
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise ValueError("expected one Game data linker owner block")
    start, end = text.index(start_marker), text.index(end_marker)
    block = text[start:end]
    rom_start, vram, rom_end, owners = load_game_data_layout(project_dir)
    expected = [owner["input"] for owner in owners]
    # Existing ignored splat scripts can still select these now-empty C pools.
    # The updated YAML regenerates assembly owners; accept either input spelling
    # on first repair, but retain the same strict duplicate/missing-owner gate.
    for source, address in (("libultra/gu/guPerspectiveF", "23D870"),
                            ("libultra/gu/guRotateF", "23D880"),
                            ("game/done/game_75810", "23D890"),
                            ("game/done/game_75950", "23D8A0")):
        restored = f"build/asm/data/{address}.rodata.s.o(.rodata)"
        if restored in expected:
            block = block.replace(f"build/src/{source}.c.o(.rodata);", restored + ";")
    selector = r"\s*(build/[^;\s]+\.o\([^;\n]+\));\s*"
    for line in block.splitlines():
        if line.strip().startswith("ASSERT("):
            continue
        if (".o(" in line and not re.fullmatch(selector, line)) or "*(" in line:
            raise ValueError("Game data owners differ from YAML: unrecognized input " + line.strip())
    inputs = re.findall("^" + selector + "$", block, re.M)
    if Counter(inputs) != Counter(expected):
        missing = list((Counter(expected) - Counter(inputs)).elements())
        extra = list((Counter(inputs) - Counter(expected)).elements())
        raise ValueError(f"Game data owners differ from YAML: missing={missing}, extra={extra}")

    # Splat's type grouping loses retail's interleaving. Each YAML owner has a
    # fixed physical span; the linker must reject overflow rather than shift it.
    lines = [start_marker]
    readonly_started = False
    for owner in owners:
        lines.append(f"        . = ABSOLUTE(0x{owner['address']:08X});")
        if not readonly_started and owner["section"] == ".rodata":
            lines.extend(("        game_data_DATA_END = .;",
                          "        game_data_DATA_SIZE = ABSOLUTE(game_data_DATA_END - game_data_DATA_START);",
                          "        game_data_RODATA_START = .;"))
            readonly_started = True
        lines.append(f"        {owner['input']};")
        lines.append(f"        ASSERT(. <= ABSOLUTE(0x{owner['end']:08X}), "
                     f'"Game data owner exceeds retail span: {owner["input"]}");')
    if not readonly_started:
        raise ValueError("Game data YAML has no rodata owner")
    lines.append(f"        . = ABSOLUTE(0x{vram + rom_end - rom_start:08X});")
    result = text[:start] + "\n".join(lines) + "\n" + text[end:]
    header = re.compile(r"(^\s*\.game_data\s+0x([0-9A-Fa-f]+)\s*:\s*"
                        r"AT\(game_data_ROM_START\)\s+SUBALIGN\()\d+(\))", re.M)
    matches = list(header.finditer(result))
    if len(matches) != 1 or int(matches[0].group(2), 16) != vram:
        raise ValueError("Game data linker base does not match YAML")
    # Explicit anchors own alignment, including the retail eight-byte boundary
    # at 0x236578; SUBALIGN(16) would advance past that owner's address.
    return header.sub(lambda match: match.group(1) + "4" + match.group(3), result)


def replace_generated_slices(text, project_dir):
    asm_by_name = {}
    for path in (project_dir / "asm").rglob("*.s"):
        if "nonmatchings" not in path.parts:
            asm_by_name.setdefault(path.stem, []).append(path)
    for source in (project_dir / "src" / "game").glob("generated_*.c"):
        name = source.stem.removeprefix("generated_")
        candidates = asm_by_name.get(name, [])
        if len(candidates) != 1:
            raise ValueError(
                f"expected one standalone asm slice for {name}, found {candidates}"
            )
        asm_path = candidates[0].relative_to(project_dir).as_posix()
        text = text.replace(
            f"build/{asm_path}.o(.text);",
            generated_slice_replacement(name),
        )
    return text

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
    project_dir = path.parent.parent
    text = replace_generated_slices(text, project_dir)
    text = text.replace("    /DISCARD/ :", OVERFLOW_SECTIONS + "    /DISCARD/ :")
    layout_path = project_dir / "retail_layout.us.txt"
    text = anchor_objects(
        text, load_object_layout(layout_path), project_dir
    )
    text = restore_init_audio_data_order(text)
    text = anchor_init_math_rodata(text)
    text = restore_game_data_order(text, project_dir)
    path.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
