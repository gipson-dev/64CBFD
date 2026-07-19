#!/usr/bin/env python3
"""Walk and dump Conker asset archives directly from a ROM.

The asset sections are offset-table containers (see DOCS/ASSET_FORMATS.md).
Each entry is `(u32 data_offset, u32 packed)`. In `packed`, bit 31 marks the
final entry, bits 30-28 select the payload type (1 = rzip-compressed), and bits
27-0 contain the payload length. An rzip payload is a four-byte big-endian
uncompressed size followed by raw DEFLATE.

Usage:
    python tools/asset_dump.py list                       # list master sections
    python tools/asset_dump.py dump assets13 out/         # dump every file
    python tools/asset_dump.py dump assets13 out/ --idx 0 # dump one file

ROM path defaults to ./baserom.us.z64 (override with --rom). US section
boundaries are read directly from the master table at ROM 0xAB1950.
"""
import argparse
import os
import struct
import sys
import zlib

MASTER_TABLE_BASE = 0x00AB1950
ASSET_SECTION_COUNT = 0x1D  # assets00 through assets1C

SECTION_NOTES = {
    "assets06": "scripted entity / cutscene / dialogue data",
    "assets08": "chapter / menu metadata",
    "assets13": "animated s16 XYZ position arrays",
    "assets16": "streamed MPEG-2 Layer III dialogue",
    "assets17": "audio banks, samples, sequences, and support tables",
    "assets1A": "language-related structured records",
    "assets1C": "credits/text layout and strings",
}


def read_table(data):
    """Parse a container header -> (offset, type, final, length) rows."""
    table_size = struct.unpack(">I", data[:4])[0]
    if table_size == 0 or table_size % 8 != 0 or table_size > len(data):
        raise ValueError(f"invalid table size 0x{table_size:X}")
    rows = []
    for i in range(table_size // 8):
        off, packed = struct.unpack(">II", data[i * 8:i * 8 + 8])
        rows.append((
            off,
            (packed >> 28) & 0x7,
            bool(packed & 0x80000000),
            packed & 0x0FFFFFFF,
        ))
    return rows


def get_us_sections(rom):
    """Read assets00-assets1C boundaries from the retail-US master table."""
    table_size = struct.unpack(">I", rom[MASTER_TABLE_BASE:MASTER_TABLE_BASE + 4])[0]
    table = rom[MASTER_TABLE_BASE:MASTER_TABLE_BASE + table_size]
    rows = read_table(table)
    if len(rows) < ASSET_SECTION_COUNT:
        raise ValueError(
            f"master table has {len(rows)} rows; expected at least "
            f"{ASSET_SECTION_COUNT}"
        )

    sections = {}
    for index, (off, payload_type, _is_final, length) in enumerate(
            rows[:ASSET_SECTION_COUNT]):
        if payload_type != 0:
            raise ValueError(
                f"master entry {index} has unexpected type {payload_type}"
            )
        name = f"assets{index:02X}"
        start = MASTER_TABLE_BASE + off
        sections[name] = (start, start + length)
    return sections, rows[ASSET_SECTION_COUNT:]


def unrzip(block):
    """Decode an rzip block: 4-byte BE uncompressed size + raw DEFLATE."""
    usize = struct.unpack(">I", block[:4])[0]
    out = zlib.decompress(block[4:], -15)
    if len(out) != usize:
        raise ValueError(f"rzip size mismatch: got {len(out)}, expected {usize}")
    return out


def walk_archive(rom, base, end):
    """Yield (start, payload_type, final, length) for a section's files."""
    files = []
    i = 0
    prev = -1
    while True:
        rec = rom[base + i * 8: base + i * 8 + 8]
        if len(rec) < 8:
            break
        off, packed = struct.unpack(">II", rec)
        i += 1
        start = base + off
        payload_type = (packed >> 28) & 0x7
        is_final = bool(packed & 0x80000000)
        length = packed & 0x0FFFFFFF
        if off == 0 and packed == 0:
            break
        if start >= end:
            break
        if length == 0:
            continue
        if start < prev:
            break
        prev = start
        files.append((start, payload_type, is_final, length))
        if is_final:
            break
    return files


def get_file(rom, sections, section, idx):
    base, end = sections[section]
    start, payload_type, _is_final, length = walk_archive(rom, base, end)[idx]
    raw = rom[start:start + length]
    return unrzip(raw) if payload_type == 1 else raw


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["list", "dump"])
    ap.add_argument("section", nargs="?")
    ap.add_argument("outdir", nargs="?")
    ap.add_argument("--rom", default="baserom.us.z64")
    ap.add_argument("--idx", type=int, default=None)
    args = ap.parse_args()

    rom = open(args.rom, "rb").read()
    sections, trailing_entries = get_us_sections(rom)

    if args.cmd == "list":
        for name, (s, e) in sections.items():
            note = SECTION_NOTES.get(name, "unclassified")
            print(f"{name}: 0x{s:08X}-0x{e:08X} ({e - s:>9} bytes)  {note}")
        for index, (off, payload_type, is_final, length) in enumerate(
                trailing_entries, start=ASSET_SECTION_COUNT):
            start = MASTER_TABLE_BASE + off
            print(
                f"master[{index:02d}]: 0x{start:08X}-0x{start + length:08X} "
                f"({length:>9} bytes)  type={payload_type} final={is_final}"
            )
        return

    if not args.section or not args.outdir:
        ap.error("dump requires SECTION and OUTDIR")
    if args.section not in sections:
        ap.error(
            f"unknown section {args.section!r}; expected assets00-assets1C"
        )
    base, end = sections[args.section]
    files = walk_archive(rom, base, end)
    os.makedirs(args.outdir, exist_ok=True)
    indices = [args.idx] if args.idx is not None else range(len(files))
    for i in indices:
        data = get_file(rom, sections, args.section, i)
        path = os.path.join(args.outdir, f"{args.section}_{i:04d}.bin")
        open(path, "wb").write(data)
        print(f"wrote {path} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
