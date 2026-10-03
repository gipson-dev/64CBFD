"""Find adjacent MIPS literal address pairs, not complete memory ownership."""

import argparse
import hashlib
import json
import struct
from pathlib import Path

from tools.tests.test_init_decompressor_retail_pages import ROM_SHA1, retail_pages


ROOT = Path(__file__).resolve().parents[2]
LOW, HIGH = 0x80031AE0, 0x80035504
MEMORY = {32: ("load", 1), 33: ("load", 2),
          35: ("load", 4), 36: ("load", 1), 37: ("load", 2),
          39: ("load", 4), 40: ("store", 1),
          41: ("store", 2), 43: ("store", 4),
          49: ("load", 4), 53: ("load", 8),
          55: ("load", 8), 57: ("store", 4), 61: ("store", 8),
          63: ("store", 8)}


def literal_pairs(payload, base, low=LOW, high=HIGH):
    if len(payload) % 4 or base & 3 or not 0 <= low < high <= 0x100000000:
        raise ValueError("expected aligned words and a nonempty address interval")
    words = [word for (word,) in struct.iter_unpack(">I", payload)]
    rows = []
    for index, (first, second) in enumerate(zip(words, words[1:])):
        register = first >> 16 & 31
        if first >> 26 != 15 or first >> 21 & 31 or not register:
            continue
        op, rs, immediate = second >> 26, second >> 21 & 31, second & 0xFFFF
        if rs != register:
            continue
        if op in (8, 9, 13) and not second >> 16 & 31:
            continue
        upper = (first & 0xFFFF) << 16
        signed = immediate if immediate < 0x8000 else immediate - 0x10000
        if op in (8, 9):
            address, kind, size = (upper + signed) & 0xFFFFFFFF, "address", 0
        elif op == 13:
            address, kind, size = upper | immediate, "address", 0
        elif op in MEMORY:
            address = (upper + signed) & 0xFFFFFFFF
            kind, size = MEMORY[op]
        else:
            continue
        if low <= address < high or size and address < low < address + size:
            rows.append({"pc": base + index * 4, "use_pc": base + (index + 1) * 4,
                         "address": address, "kind": kind, "bytes": size,
                         "words": [first, second]})
    return rows


def audit(rom):
    if hashlib.sha1(rom).hexdigest() != ROM_SHA1:
        raise ValueError("expected original US retail ROM")
    game = b"".join(page[4] for page in retail_pages(rom))
    sections = (("Init", rom[0x1000:0x290D0], 0x10001000),
                ("Game", game, 0x15000000),
                ("Debugger", rom[0x19EA88:0x1A2178], 0x16000000))
    result = []
    for name, payload, base in sections:
        result.extend({"section": name, **row} for row in literal_pairs(payload, base))
    return {"scope": "adjacent literal pairs only; absence is not ownership proof",
            "interval": [LOW, HIGH], "references": result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rom", type=Path, default=ROOT / "baserom.us.z64")
    args = parser.parse_args()
    print(json.dumps(audit(args.rom.read_bytes()), indent=2))


if __name__ == "__main__":
    main()
