"""Measure SDK guest layout and retail core use, without changing any owner."""

import argparse
import json
import os
import struct
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_retail_pages as pages
from tools.tests.test_init_decompressor_streams import StreamFixture


def read_layout(path):
    data = path.read_bytes()
    header = struct.unpack_from(">16sHHIIIIIHHHHHH", data)
    if data[:6] != b"\x7fELF\x01\x02" or header[2] != 8:
        raise ValueError("Expected big-endian ELF32 MIPS")
    sections = [struct.unpack_from(">IIIIIIIIII", data, header[6] + i * header[11])
                for i in range(header[12])]
    symbols = next(section for section in sections if section[1] == 2)
    strings = sections[symbols[6]]
    strings = data[strings[4]:strings[4] + strings[5]]
    for offset in range(symbols[4], symbols[4] + symbols[5], symbols[9]):
        symbol = struct.unpack_from(">IIIBBH", data, offset)
        name = strings[symbol[0]:].split(b"\0", 1)[0]
        if name == b"init_thread_storage_layout":
            section = sections[symbol[5]]
            if symbol[2] != 16:
                raise ValueError("Unexpected layout receipt size")
            values = struct.unpack_from(">4I", data, section[4] + symbol[1])
            return dict(zip(("thread_bytes", "context_offset", "fp0_offset",
                             "fp30_offset"), values))
    raise ValueError("Layout symbol missing")


def compile_layout(directory):
    obj = directory / "thread-layout.o"
    command = ["../ido/ido5.3_recomp/cc", "-c", "-32", "-O2", "-g3", "-D_LANGUAGE_C",
               "-Xcpluscomm", "-nostdinc", "-non_shared",
               "-mips2", "-o32", "-I", "include/2.0L", "-I", "include/2.0L/PR",
               "-I", "include/libc", "-o", os.path.relpath(obj, ROOT / "conker"),
               "../tools/experiments/init_thread_storage_layout.c"]
    obj.unlink(missing_ok=True)
    result = subprocess.run(command, cwd=ROOT / "conker", env={**os.environ, "LC_ALL": "C"},
                            text=True, capture_output=True)
    (directory / "compile.log").write_text(result.stdout + result.stderr)
    result.check_returncode()
    if result.stdout or result.stderr:
        raise ValueError("Guest layout compile was not warning-clean")
    return read_layout(obj)


def validate_observed_writes(writes, output, output_bytes):
    low = pages.CALLER_SP - 0xA88
    regions = ((low, pages.CALLER_SP), (pages.WORKSPACE, 0x800354F8),
               (output, output + output_bytes))
    for address, size in writes:
        if size <= 0 or not any(start <= address and address + size <= end
                                for start, end in regions):
            raise ValueError("Write outside observed call regions")


def survey_pages(rom):
    contract.InitDecompressorContractTests.setUpClass.__func__(
        contract.InitDecompressorContractTests)
    image = (ROOT / "conker/conker.us.bin").read_bytes()
    results = []
    for index, start, end, chunk, expected in pages.retail_pages(rom):
        image_start = 0x2D4B0 + index * 0x1000
        if expected != image[image_start:image_start + len(expected)]:
            raise ValueError("Pristine page mismatch")
        fixture = StreamFixture(chunk)
        fixture.INPUT, fixture.OUTPUT = pages.INPUT, 0x80050000
        fixture.WORKSPACE = pages.WORKSPACE
        fixture.registers[29] = pages.CALLER_SP
        low = pages.CALLER_SP - 0xA88
        fixture.memory.update({address: 0xA5 for address in range(low, pages.CALLER_SP)})
        dma = (end - start + 15) & ~15
        fixture.memory.update({pages.INPUT + i: byte for i, byte in
                               enumerate(rom[start:start + dma])})
        fixture.reads, fixture.writes = [], []
        returned = fixture.core(False)
        if returned != len(expected) or fixture.output() != expected:
            raise ValueError("Retained core mismatch on page %d" % index)
        if fixture.registers[29] != pages.CALLER_SP:
            raise ValueError("Core SP changed")
        scratch = [(a, n) for a, n in fixture.writes
                   if pages.WORKSPACE <= a < fixture.OUTPUT]
        span = max((a + n - pages.WORKSPACE for a, n in scratch), default=0)
        validate_observed_writes(fixture.writes, fixture.OUTPUT, len(expected))
        results.append({"page": index, "dma_bytes": dma, "output_bytes": len(expected),
                        "workspace_write_span": span})
        if index % 100 == 0:
            print("qualified retail page %d" % index, flush=True)
    return {"pages": len(results), "maximum_dma": max(results, key=lambda row: row["dma_bytes"]),
            "maximum_workspace": max(results, key=lambda row: row["workspace_write_span"]),
            "rows": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all-pages", action="store_true")
    args = parser.parse_args()
    directory = ROOT / "conker/build/init-exception-storage"
    directory.mkdir(parents=True, exist_ok=True)
    report = {"sdk_guest_layout": compile_layout(directory)}
    if args.all_pages:
        report["retail_core_survey"] = survey_pages((ROOT / "baserom.us.z64").read_bytes())
    (directory / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    summary = {key: ({k: v for k, v in value.items() if k != "rows"}
                     if isinstance(value, dict) else value) for key, value in report.items()}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
