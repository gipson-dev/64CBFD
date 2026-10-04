#!/usr/bin/env python3
"""Compare the complete physical Game-data image against checksum-verified retail."""

import argparse
import hashlib
import json
import sys
from pathlib import Path

if not __package__:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER, read_c_string
from tools.patch_generated_slice_ld import load_game_data_layout


def load_section(path, name):
    data = Path(path).read_bytes()

    def chunk(offset, size):
        if offset < 0 or size < 0 or offset + size > len(data):
            raise ValueError("ELF range exceeds file")
        return data[offset:offset + size]

    header = ELF_HEADER.unpack(chunk(0, ELF_HEADER.size))
    if header[0][:7] != b"\x7fELF\x01\x02\x01" or header[1:3] != (2, 8):
        raise ValueError("expected a linked ELF32 big-endian MIPS executable")
    if header[11] != SECTION_HEADER.size or not 0 < header[13] < header[12]:
        raise ValueError("unsupported ELF section table")
    sections = list(SECTION_HEADER.iter_unpack(chunk(header[6], header[12] * header[11])))
    names = sections[header[13]]
    if names[1] != 3:
        raise ValueError("ELF section names are not a string table")
    strings = chunk(names[4], names[5])
    found = []
    for section in sections:
        if section[0] >= len(strings):
            raise ValueError("ELF section name exceeds string table")
        if read_c_string(strings, section[0]) == name:
            found.append(section)
    if len(found) != 1:
        raise ValueError("expected one ELF section: " + name)
    section, = found
    if section[1] != 1 or not section[2] & 2 or section[2] & 4:
        raise ValueError("expected allocated, non-executable initialized data")
    return section[3], chunk(section[4], section[5])


def compare_layout(address, data, reference, layout):
    rom_start, vram, rom_end, owners = layout
    expected = reference[rom_start:rom_end]
    if len(expected) != rom_end - rom_start:
        raise ValueError("reference ROM does not cover Game-data span")

    def differences(actual, wanted):
        return sum(a != b for a, b in zip(actual, wanted)) + abs(len(actual) - len(wanted))

    different_owners = []
    for owner in owners:
        first = owner["address"] - address
        size = owner["end"] - owner["address"]
        actual = data[max(first, 0):max(first + size, 0)]
        wanted = reference[owner["rom"]:owner["rom"] + size]
        count = differences(actual, wanted)
        if count:
            different_owners.append({"rom": owner["rom"], "address": owner["address"],
                                     "input": owner["input"], "different_bytes": count})
    count = differences(data, expected)
    return {"exact": address == vram and len(data) == len(expected) and count == 0,
            "address": address, "expected_address": vram,
            "bytes": len(data), "expected_bytes": len(expected),
            "different_bytes": count, "owner_count": len(owners),
            "different_owner_count": len(different_owners),
            "different_owners": different_owners,
            "sha256": hashlib.sha256(data).hexdigest()}


def audit_layout(elf, project_dir):
    project_dir = Path(project_dir)
    reference = (project_dir / "conker.us.bin").read_bytes()
    config = yaml.safe_load((project_dir / "conker.us.yaml").read_text())
    if hashlib.sha1(reference).hexdigest() != config.get("sha1"):
        raise ValueError("reference ROM checksum differs from YAML")
    address, data = load_section(elf, ".game_data")
    return compare_layout(address, data, reference, load_game_data_layout(project_dir))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("elf", type=Path)
    parser.add_argument("--project-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "conker")
    parser.add_argument("--limit", type=int, default=10,
                        help="maximum differing owners to print; comparison always covers all bytes")
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit must be nonnegative")
    report = audit_layout(args.elf, args.project_dir)
    report["different_owners"] = report["different_owners"][:args.limit]
    print(json.dumps(report, indent=2))
    return 0 if report["exact"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
