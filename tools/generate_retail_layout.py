#!/usr/bin/env python3
"""Generate the stable retail function-address manifest used by layout tools."""

import argparse
import csv
import sys
from pathlib import Path

import match_progress


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("progress_csv")
    parser.add_argument("output_csv")
    parser.add_argument("--version", default="us")
    parser.add_argument("--symbol-addrs", default=None)
    args = parser.parse_args()

    progress_path = Path(args.progress_csv)
    with progress_path.open(newline="") as stream:
        rows = [
            row for row in csv.DictReader(stream)
            if row.get("version") == args.version
        ]

    segments = match_progress.load_segments(
        args.version, str(progress_path), str(progress_path.parent)
    )
    symbol_path = args.symbol_addrs or match_progress.default_symbol_addrs_path(
        args.version, str(progress_path), None, None
    )
    symbol_addrs = match_progress.load_symbol_addrs(symbol_path)
    match_progress.add_retail_lengths(rows, args.version, segments, symbol_addrs)

    output_rows = []
    for row in rows:
        address = match_progress.function_vram(row, symbol_addrs)
        output_rows.append({
            "section": row["section"],
            "filename": row["filename"],
            "function": row["function"],
            "address": f"0x{address:08X}",
            "end": f"0x{address + row['_retail_nwords'] * 4:08X}",
        })
    output_rows.sort(key=lambda row: int(row["address"], 16))

    with Path(args.output_csv).open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=("section", "filename", "function", "address", "end")
        )
        writer.writeheader()
        writer.writerows(output_rows)


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main()
