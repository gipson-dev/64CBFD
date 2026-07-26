#!/usr/bin/env python3
"""Smoke-test the project-native raw-object and minimal-ELF wrappers."""

import struct
import subprocess
import sys
import tempfile
from pathlib import Path


ELF_HEADER = struct.Struct(">16sHHIIIIIHHHHHH")
SECTION_HEADER = struct.Struct(">IIIIIIIIII")


def read_c_string(data, offset):
    end = data.find(b"\0", offset)
    if end < 0:
        raise ValueError("unterminated ELF string")
    return data[offset:end].decode("ascii")


def read_elf(path):
    data = path.read_bytes()
    header = ELF_HEADER.unpack_from(data)
    ident = header[0]
    if ident[:4] != b"\x7fELF" or ident[4] != 1 or ident[5] != 2:
        raise ValueError(f"{path} is not a 32-bit big-endian ELF")
    if header[2] != 8:
        raise ValueError(f"{path} is not a MIPS ELF")

    section_offset = header[6]
    section_size = header[11]
    section_count = header[12]
    names_index = header[13]
    if section_size != SECTION_HEADER.size:
        raise ValueError(f"{path} has an unsupported section header size")

    sections = [
        SECTION_HEADER.unpack_from(data, section_offset + index * section_size)
        for index in range(section_count)
    ]
    names_header = sections[names_index]
    names = data[names_header[4]:names_header[4] + names_header[5]]
    by_name = {}
    for section in sections:
        by_name[read_c_string(names, section[0])] = {
            "address": section[3],
            "offset": section[4],
            "size": section[5],
            "alignment": section[8],
        }
    return header, data, by_name


def check_data_section(path, payload, address):
    _header, data, sections = read_elf(path)
    section = sections[".data"]
    contents = data[section["offset"]:section["offset"] + section["size"]]
    if section["address"] != address:
        raise ValueError(
            f"{path} .data address is 0x{section['address']:X}, expected 0x{address:X}"
        )
    if section["alignment"] != 0x10:
        raise ValueError(f"{path} .data alignment is not 0x10")
    if section["size"] != 0x10:
        raise ValueError(f"{path} .data size is not the expected padded 0x10")
    if contents != payload + bytes(0x10 - len(payload)):
        raise ValueError(f"{path} .data contents do not match the fixture")


def check_vertex_converter(tools_dir, temp_dir):
    packed = "ffff000280001234fff0002011223344"
    expected = (
        "{{{ -1, 2, -32768 }, 0x1234, { -16, 32 }, "
        "{ 0x11, 0x22, 0x33, 0x44 }}},"
    )
    direct = subprocess.run(
        [sys.executable, str(tools_dir / "vertconvert.py"), packed],
        check=True,
        capture_output=True,
        text=True,
    )
    if direct.stdout.strip() != expected:
        raise ValueError("vertconvert.py produced an unexpected initializer")

    source = temp_dir / "vertex input.txt"
    source.write_text(
        "dlabel ignored_label\n"
        "0xFFFF, 0x0002, 0x8000, 0x1234,\n"
        "0xFFF0, 0x0020, 0x11223344\n"
    )
    wrapped = subprocess.run(
        [
            sys.executable,
            str(tools_dir / "vertconvert.py"),
            "--file",
            str(source),
            "--array-name",
            "test_vertices",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    if wrapped.stdout != f"Vtx test_vertices[] = {{\n    {expected}\n}};\n":
        raise ValueError("vertconvert.py array output is malformed")

    invalid = subprocess.run(
        [sys.executable, str(tools_dir / "vertconvert.py"), "00"],
        capture_output=True,
        text=True,
    )
    if invalid.returncode == 0 or "multiple of 32" not in invalid.stderr:
        raise ValueError("vertconvert.py accepted a partial vertex")

    invalid_name = subprocess.run(
        [
            sys.executable,
            str(tools_dir / "vertconvert.py"),
            packed,
            "--array-name",
            "not-an-identifier",
        ],
        capture_output=True,
        text=True,
    )
    if (
        invalid_name.returncode == 0
        or "valid C identifier" not in invalid_name.stderr
    ):
        raise ValueError("vertconvert.py accepted an invalid C array name")


def main():
    tools_dir = Path(__file__).resolve().parent
    payload = bytes.fromhex("00112233445566")

    with tempfile.TemporaryDirectory(prefix="cbfd-tools-") as temp_name:
        temp_dir = Path(temp_name)
        raw = temp_dir / "fixture input.bin"
        obj = temp_dir / "fixture raw.o"
        elf = temp_dir / "fixture simple.elf"
        raw.write_bytes(payload)

        subprocess.run(
            [str(tools_dir / "mkrawobject"), str(raw), str(obj), "0x10"],
            check=True,
        )
        check_data_section(obj, payload, 0)

        subprocess.run(
            [
                str(tools_dir / "mksimpleelf"),
                str(obj),
                str(elf),
                "0x80000000",
            ],
            check=True,
        )
        header, _data, _sections = read_elf(elf)
        if header[1] != 2:
            raise ValueError(f"{elf} is not an executable ELF")
        check_data_section(elf, payload, 0x80000000)
        check_vertex_converter(tools_dir, temp_dir)

    print("project tool checks passed")


if __name__ == "__main__":
    main()
