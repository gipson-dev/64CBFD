#!/usr/bin/env python3
"""Convert packed 16-byte N64 Vtx records to C initializers.

This handles the standard SDK Vtx layout. It does not decode Conker's
six-byte position-only model records documented in DOCS/ASSET_FORMATS.md.
"""

import argparse
import re
import sys
from pathlib import Path


VERTEX_HEX_LENGTH = 32


def signed16(value):
    return value - 0x10000 if value & 0x8000 else value


def normalize_hex(text):
    lines = [
        line for line in text.splitlines()
        if not line.lstrip().startswith("dlabel")
    ]
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"0[xX]", "", cleaned)
    cleaned = re.sub(r"[\s,_]", "", cleaned)
    if not cleaned:
        return ""
    if not re.fullmatch(r"[0-9A-Fa-f]+", cleaned):
        raise ValueError("input contains characters outside hexadecimal separators")
    if len(cleaned) % VERTEX_HEX_LENGTH:
        raise ValueError(
            "input length must be a multiple of 32 hexadecimal digits "
            "(16 bytes per Vtx)"
        )
    return cleaned


def format_vertex(vertex_hex):
    values = bytes.fromhex(vertex_hex)
    x = signed16(int.from_bytes(values[0:2], "big"))
    y = signed16(int.from_bytes(values[2:4], "big"))
    z = signed16(int.from_bytes(values[4:6], "big"))
    flag = int.from_bytes(values[6:8], "big")
    texture_x = signed16(int.from_bytes(values[8:10], "big"))
    texture_y = signed16(int.from_bytes(values[10:12], "big"))
    red, green, blue, alpha = values[12:16]
    return (
        "{{{ "
        f"{x}, {y}, {z}"
        f" }}, 0x{flag:04X}, {{ {texture_x}, {texture_y} }}, "
        "{ "
        f"0x{red:02X}, 0x{green:02X}, 0x{blue:02X}, 0x{alpha:02X}"
        " }}},"
    )


def convert(text):
    cleaned = normalize_hex(text)
    return [
        format_vertex(cleaned[offset:offset + VERTEX_HEX_LENGTH])
        for offset in range(0, len(cleaned), VERTEX_HEX_LENGTH)
    ]


def parse_args():
    parser = argparse.ArgumentParser(
        description="convert packed standard N64 Vtx records to C initializers"
    )
    parser.add_argument(
        "hex",
        nargs="*",
        help="hexadecimal Vtx data; whitespace, commas, underscores, and 0x are allowed",
    )
    parser.add_argument(
        "-f",
        "--file",
        action="append",
        default=[],
        type=Path,
        help="read hexadecimal Vtx data from a file (repeatable; use - for stdin)",
    )
    parser.add_argument(
        "-n",
        "--array-name",
        help="wrap the output in a Vtx array declaration",
    )
    return parser, parser.parse_args()


def main():
    parser, args = parse_args()
    if args.array_name and not re.fullmatch(
        r"[A-Za-z_][A-Za-z0-9_]*", args.array_name
    ):
        parser.error("--array-name must be a valid C identifier")
    inputs = list(args.hex)
    for path in args.file:
        if str(path) == "-":
            inputs.append(sys.stdin.read())
        else:
            try:
                inputs.append(path.read_text())
            except OSError as error:
                parser.error(str(error))
    if not inputs:
        inputs.append(sys.stdin.read())

    output = []
    try:
        for value in inputs:
            output.extend(convert(value))
    except ValueError as error:
        parser.error(str(error))

    if not output:
        parser.error("no vertex data was provided")

    if args.array_name:
        print(f"Vtx {args.array_name}[] = {{")
        for line in output:
            print(f"    {line}")
        print("};")
    else:
        print("\n".join(output))


if __name__ == "__main__":
    main()
