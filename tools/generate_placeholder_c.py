#!/usr/bin/env python3
"""Generate non-matching C placeholders for a text-only assembly slice."""

import argparse
import re
from pathlib import Path


def function_layout(path):
    label = re.compile(r"^glabel\s+(\S+)")
    instruction = re.compile(
        r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+[0-9A-Fa-f]{8}\s*\*/"
    )
    pending = None
    functions = []
    last_address = None
    for line in Path(path).read_text().splitlines():
        match = label.match(line)
        if match:
            pending = match.group(1)
            continue
        match = instruction.search(line)
        if not match:
            continue
        address = int(match.group(1), 16)
        last_address = address
        if pending is not None:
            functions.append((pending, address))
            pending = None

    if not functions or last_address is None:
        raise ValueError(f"no glabel functions found in {path}")
    names = [name for name, _address in functions]
    invalid = [name for name in names if not re.fullmatch(r"[A-Za-z_]\w*", name)]
    if invalid:
        raise ValueError(f"invalid C identifiers in {path}: {invalid}")
    if len(names) != len(set(names)):
        raise ValueError(f"duplicate function labels in {path}")
    end = last_address + 4
    return [
        (name, (functions[index + 1][1] if index + 1 < len(functions) else end) - address)
        for index, (name, address) in enumerate(functions)
    ]


def generate(source):
    source = Path(source)
    lines = [
        "#include <ultra64.h>",
        "",
        f"/* Non-matching placeholders for the text-only asm slice asm/{source.name}. */",
        "",
    ]
    for name, size in function_layout(source):
        if size < 12:
            lines.extend((f"void {name}() {{", "}", ""))
        else:
            lines.extend((f"s32 {name}() {{", "    return 0;", "}", ""))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="text-only assembly slice")
    parser.add_argument("output", help="generated C output")
    args = parser.parse_args()
    Path(args.output).write_text(generate(args.source), newline="\n")


if __name__ == "__main__":
    main()
