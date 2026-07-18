#!/usr/bin/env python3
"""Generate non-matching C placeholders for a text-only assembly slice."""

import argparse
import re
from pathlib import Path


def function_layout(path):
    # Handwritten and spimdisasm-generated slices sometimes indent secondary
    # global entry points even though they are independently tracked symbols.
    label = re.compile(r"^\s*glabel\s+(\S+)")
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


def placeholder_definition(name, size, return_type=None, parameters=""):
    if return_type is None:
        return_type = "void" if size < 12 else "s32"
    value_type = return_type.removeprefix("static ").strip()
    if value_type == "void":
        return [f"{return_type} {name}({parameters}) {{", "}", ""]
    value = "0.0f" if value_type == "f32" else "0.0" if value_type == "f64" else "0"
    return [f"{return_type} {name}({parameters}) {{", f"    return {value};", "}", ""]


def placeholder_lines(source, return_types=None):
    source = Path(source)
    lines = []
    for name, size in function_layout(source):
        if size < 8:
            raise ValueError(
                f"{source}: {name} has a {size}-byte retail span; "
                "the smallest C stub is 8 bytes"
            )
        return_type = return_types.get(name) if return_types else None
        lines.extend(placeholder_definition(name, size, return_type))
    return lines


def generate(source):
    source = Path(source)
    lines = [
        "#include <ultra64.h>",
        "",
        f"/* Non-matching placeholders for the text-only asm slice asm/{source.name}. */",
        "",
    ]
    lines.extend(placeholder_lines(source))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="text-only assembly slice")
    parser.add_argument("output", help="generated C output")
    args = parser.parse_args()
    Path(args.output).write_text(generate(args.source), newline="\n")


if __name__ == "__main__":
    main()
