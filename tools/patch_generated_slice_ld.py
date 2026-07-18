#!/usr/bin/env python3

import sys
from pathlib import Path


REPLACEMENTS = {
    "build/asm/B3020.s.o(.text);": (
        "build/src/game/generated_B3020.c.o(.text);\n"
        "        build/src/game/generated_jlabels.s.o(.text);"
    ),
    "build/asm/142560.s.o(.text);": "build/src/game/generated_142560.c.o(.text);",
    "build/asm/179F30.s.o(.text);": "build/src/game/generated_179F30.c.o(.text);",
    "build/asm/1C2C60.s.o(.text);": "build/src/game/generated_1C2C60.c.o(.text);",
    "build/asm/1BA1D0.s.o(.text);": "build/src/game/generated_1BA1D0.c.o(.text);",
    "build/asm/20AE20.s.o(.text);": "build/src/game/generated_20AE20.c.o(.text);",
    "build/asm/1E73B0.s.o(.text);": "build/src/game/generated_1E73B0.c.o(.text);",
    "build/asm/49D30.s.o(.text);": "build/src/game/generated_49D30.c.o(.text);",
    "build/asm/1FA770.s.o(.text);": "build/src/game/generated_1FA770.c.o(.text);",
}


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <linker-script>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    text = path.read_text()
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    path.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
