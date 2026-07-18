#!/usr/bin/env python3
"""Generate typed non-matching C placeholders for a standalone asm slice."""

import argparse
from pathlib import Path

from generate_placeholder_c import function_layout, placeholder_definition
from replace_global_asm_with_placeholders import declared_signature, load_headers


def generate(project_dir, source):
    project_dir = Path(project_dir)
    source = Path(source)
    headers = load_headers(project_dir)
    headers.append((project_dir / "src/libultra/io/controller.h").read_text())
    layout = function_layout(source)
    lines = [
        "#include <ultra64.h>",
        '#include "controller.h"',
        "",
    ]
    for name, _size in layout:
        lines.extend((f"#ifdef {name}", f"#undef {name}", "#endif"))
    lines.extend([
        "",
        f"/* Non-matching C placeholders for {source.as_posix()}. */",
        "",
    ])
    for name, size in layout:
        signature = declared_signature(name, headers)
        if signature is None:
            return_type = "void" if size < 12 else "s32"
            parameters = ""
        else:
            return_type, parameters = signature
        lines.extend(placeholder_definition(name, size, return_type, parameters))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", help="project root containing include/")
    parser.add_argument("source", help="text-only assembly slice")
    parser.add_argument("output", help="generated C output")
    args = parser.parse_args()
    Path(args.output).write_text(
        generate(args.project_dir, args.source), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
