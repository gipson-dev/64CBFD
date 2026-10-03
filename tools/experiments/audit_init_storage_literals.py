"""Find adjacent and optional block-local literals, not complete memory ownership."""

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


def block_local_literals(payload, base, low=LOW, high=HIGH):
    """Lexical basic-block candidates; no path merging or loaded-pointer inference."""
    if len(payload) % 4 or base & 3 or not 0 <= low < high <= 0x100000000:
        raise ValueError("expected aligned words and a nonempty address interval")
    words = [word for (word,) in struct.iter_unpack(">I", payload)]
    targets = set()
    for index, word in enumerate(words):
        pc, op = base + index * 4, word >> 26
        immediate = word & 0xFFFF
        signed = immediate if immediate < 0x8000 else immediate - 0x10000
        if op in (1, 4, 5, 6, 7, 20, 21, 22, 23):
            targets.add((pc + 4 + signed * 4) & 0xFFFFFFFF)
        elif op in (2, 3):
            targets.add(((pc + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2))
    values, rows, clear_at = {0: (0, ())}, [], None
    for index, word in enumerate(words):
        pc, op = base + index * 4, word >> 26
        if pc in targets or pc == clear_at:
            values = {0: (0, ())}
        rs, rt, rd = word >> 21 & 31, word >> 16 & 31, word >> 11 & 31
        immediate, fn = word & 0xFFFF, word & 63
        signed = immediate if immediate < 0x8000 else immediate - 0x10000
        left, right = values.get(rs), values.get(rt)
        destination, result = None, None
        if op == 15 and rs == 0:
            destination, result = rt, (immediate << 16, (pc,))
        elif op in (8, 9, 12, 13, 14):
            destination = rt
            if left is not None:
                operations = {8: lambda: left[0] + signed, 9: lambda: left[0] + signed,
                              12: lambda: left[0] & immediate, 13: lambda: left[0] | immediate,
                              14: lambda: left[0] ^ immediate}
                result = operations[op]() & 0xFFFFFFFF, left[1] + (pc,)
                if op == 8:
                    value = left[0] if left[0] < 0x80000000 else left[0] - 0x100000000
                    if not -0x80000000 <= value + signed <= 0x7FFFFFFF:
                        result = None
        elif op in MEMORY:
            kind, size = MEMORY[op]
            if left is not None and left[1]:
                address = (left[0] + signed) & 0xFFFFFFFF
                if low <= address < high or address < low < address + size:
                    rows.append({"use_pc": pc, "address": address, "kind": kind,
                                 "bytes": size, "definition_pcs": list(left[1]), "word": word})
            if kind == "load" and op not in (49, 53):
                destination = rt
        elif op == 0 and fn in (0, 2, 3, 33, 35, 36, 37, 38, 39):
            destination = rd
            if fn in (0, 2, 3) and right is not None:
                shift = word >> 6 & 31
                value = right[0] if right[0] < 0x80000000 else right[0] - 0x100000000
                result = ({0: right[0] << shift, 2: right[0] >> shift,
                           3: value >> shift}[fn] & 0xFFFFFFFF, right[1] + (pc,))
            elif left is not None and right is not None:
                operations = {33: lambda: left[0] + right[0], 35: lambda: left[0] - right[0],
                              36: lambda: left[0] & right[0], 37: lambda: left[0] | right[0],
                              38: lambda: left[0] ^ right[0], 39: lambda: ~(left[0] | right[0])}
                result = operations[fn]() & 0xFFFFFFFF, tuple(sorted(set(left[1] + right[1] + (pc,))))
        elif op in (1, 2, 3, 4, 5, 6, 7, 20, 21, 22, 23) or op == 0 and fn in (8, 9):
            clear_at = pc + 8
            if op == 3 or op == 0 and fn == 9:
                values.pop(31 if op == 3 else rd, None)
        else:
            values = {0: (0, ())}
        if destination:
            values.pop(destination, None)
            if result is not None:
                values[destination] = result
                if result[1] and low <= result[0] < high:
                    rows.append({"use_pc": pc, "address": result[0], "kind": "address",
                                 "bytes": 0, "definition_pcs": list(result[1]), "word": word})
        values[0] = 0, ()
    return rows


def audit(rom, block_local=False):
    if hashlib.sha1(rom).hexdigest() != ROM_SHA1:
        raise ValueError("expected original US retail ROM")
    game = b"".join(page[4] for page in retail_pages(rom))
    sections = (("Init", rom[0x1000:0x290D0], 0x10001000),
                ("Game", game, 0x15000000),
                ("Debugger", rom[0x19EA88:0x1A2178], 0x16000000))
    result, tracked = [], []
    for name, payload, base in sections:
        result.extend({"section": name, **row} for row in literal_pairs(payload, base))
        if block_local:
            tracked.extend({"section": name, **row} for row in block_local_literals(payload, base))
    report = {"scope": "literal candidates only; absence is not ownership proof",
              "interval": [LOW, HIGH], "references": result}
    if block_local:
        report["block_local_references"] = tracked
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rom", type=Path, default=ROOT / "baserom.us.z64")
    parser.add_argument("--block-local", action="store_true")
    args = parser.parse_args()
    print(json.dumps(audit(args.rom.read_bytes(), block_local=args.block_local), indent=2))


if __name__ == "__main__":
    main()
