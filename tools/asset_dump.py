#!/usr/bin/env python3
"""Walk and dump Conker asset archives directly from a ROM.

The asset sections are offset-table containers (see DOCS/ASSET_FORMATS.md).
Each entry is (u32 data_offset, u8 flags, u24 length); flag bit 0x10 marks the
payload as rzip-compressed (4-byte big-endian uncompressed size + raw DEFLATE).

Usage:
    python tools/asset_dump.py list                       # list known sections
    python tools/asset_dump.py dump assets13 out/         # dump every file
    python tools/asset_dump.py dump assets13 out/ --idx 0 # dump one file

ROM path defaults to ./baserom.us.z64 (override with --rom).
Section offsets below are the US ROM values from conker.us.yaml.
"""
import argparse
import os
import struct
import sys
import zlib

# name: (start, end) in the US ROM
US_SECTIONS = {
    "assets00": (0x00AB1A40, 0x00AF4918),
    "assets01": (0x00AF4918, 0x00BB1BA0),
    "assets06": (0x0117FE50, 0x012043B0),  # scripted cutscene / dialogue data
    "assets08": (0x01204400, 0x01204780),  # chapter / menu metadata
    "assets13": (0x01300188, 0x01304F00),  # 3D model data (textures + geometry)
    "assets16": (0x01330478, 0x029AE9E8),  # streamed MP3 audio
    "assets17": (0x029AE9E8, 0x03F82170),  # audio subsystem (banks + samples)
    "assets1C": (0x03F8AB18, 0x03F8B770),  # text / credits
}


def read_table(data):
    """Parse an offset-table container header -> [(offset, flags, length)]."""
    table_size = struct.unpack(">I", data[:4])[0]
    rows = []
    for i in range(table_size // 8):
        off, packed = struct.unpack(">II", data[i * 8:i * 8 + 8])
        rows.append((off, packed >> 24, packed & 0x0FFFFFFF))
    return rows


def unrzip(block):
    """Decode an rzip block: 4-byte BE uncompressed size + raw DEFLATE."""
    usize = struct.unpack(">I", block[:4])[0]
    out = zlib.decompress(block[4:], -15)
    if len(out) != usize:
        raise ValueError(f"rzip size mismatch: got {len(out)}, expected {usize}")
    return out


def walk_archive(rom, base, end):
    """Yield (start, flags, length) for each file in a container section."""
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
        flags = packed >> 24
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
        files.append((start, flags, length))
    return files


def get_file(rom, section, idx):
    base, end = US_SECTIONS[section]
    start, flags, length = walk_archive(rom, base, end)[idx]
    raw = rom[start:start + length]
    return unrzip(raw) if (flags & 0x10) else raw


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["list", "dump"])
    ap.add_argument("section", nargs="?")
    ap.add_argument("outdir", nargs="?")
    ap.add_argument("--rom", default="baserom.us.z64")
    ap.add_argument("--idx", type=int, default=None)
    args = ap.parse_args()

    if args.cmd == "list":
        for name, (s, e) in US_SECTIONS.items():
            print(f"{name}: 0x{s:X}-0x{e:X}")
        return

    if not args.section or not args.outdir:
        ap.error("dump requires SECTION and OUTDIR")
    rom = open(args.rom, "rb").read()
    base, end = US_SECTIONS[args.section]
    files = walk_archive(rom, base, end)
    os.makedirs(args.outdir, exist_ok=True)
    indices = [args.idx] if args.idx is not None else range(len(files))
    for i in indices:
        data = get_file(rom, args.section, i)
        path = os.path.join(args.outdir, f"{args.section}_{i:04d}.bin")
        open(path, "wb").write(data)
        print(f"wrote {path} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
