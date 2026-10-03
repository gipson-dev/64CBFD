# Init Exception Storage Boundaries and All Retail Core Page Survey

Date: 2026-10-03. Baseline: `ffdc54d`.

## Result

All 507 original retail Game pages pass through the retained core model at the
exception input/workspace/SP addresses. Every modeled write fits the observed
core frame, workspace comparison window, or actual output length. This extends
Note 804's three-page core sample to the entire retail page table.

The linked map and symbol declarations do not establish separately owned
exception arrays. Keep production assembly unchanged: neither observed use
nor an adjacent symbol establishes an allocation capacity for a C adapter.
Init remains 492/539 C functions, with 47 retained assembly routines.

## Thread Context Boundary

The isolated IDO guest probe `tools/experiments/init_thread_storage_layout.c`
includes the current `PR/os_thread.h` directly and exports sizeof/offsetof
values. The driver parses its ELF32 big-endian MIPS symbol and data section;
no host pointer-size assumptions enter the result.

| Current SDK field | Guest value |
| --- | ---: |
| `sizeof(OSThread)` | `0x1B0` (432 bytes) |
| `context` offset | `0x20` |
| `context.fp0` offset | `0x130` |
| `context.fp30` offset | `0x1A8` |

The retail context save in `func_100071D0` and restore in `func_10007A38` use
32 full-width FPR slots: offset `0x130 + 8 * register`, ending exclusively at
`0x230`. The SDK type describes sixteen paired slots instead. Its size cannot
be used as the retail context storage boundary. This is a measured layout
discrepancy, not a claim that current thread creation corrupts memory.

`0x800318B0 + 0x230 == 0x80031AE0`, consistent with the two startup thread
addresses. The second known context footprint ends at `0x80031D10`.
The retained decoder's lowest modeled SP is `0x80031F88`, a 632-byte numerical
gap. Four stored/dynamic wrapper runs covering both CU1 states preserve
canaries throughout the known second context footprint and this gap.
This does not prove the gap is free storage or authorize an extra C frame.

The current linked map ends `.init_data` at `0x8002D4B0`. The later BSS names
are absolute assignments, not sized arrays. Startup clears through
`0x80043B40`, and YAML records BSS size `0x16690`, but neither yields individual
stack/workspace ownership. No broad SDK header or linker rewrite is made.

## Page Table and Input Boundary

For the actual 507-page startup count, the rounded DMA of `(count + 2) * 4`
bytes is `0x800`. Beginning at `0x80032B30`, it ends exactly at input
`0x80033330`. The 508 decoded endpoint words end at `0x80033320`, leaving
sixteen bytes of transferred padding before input. Tests pin the original
startup instructions implementing the arithmetic, not just the formula.

The maximum input DMA is still 3,072 bytes on page 169, leaving 440 bytes
before workspace at `0x800340E8`. The full retained-core survey finds the
maximum workspace write span on page 50:

| Measurement | Result |
| --- | ---: |
| Pages executed and compared | 507 / 507 |
| Page 50 rounded input DMA | 2,096 bytes |
| Page 50 output | 4,096 bytes |
| Maximum workspace write span | 3,564 bytes |
| Exclusive final workspace write | `0x80034ED4` |
| Distance to comparison symbol `D_800354F8` | 1,572 bytes |

The survey independently compares each output with both zlib decoding and the
corresponding pristine Game bytes, verifies returned lengths and restored SP,
and rejects writes crossing the observed regions. A nonpositive write size,
input write, or one-byte boundary crossing also has explicit rejection tests.
The comparison window up to `D_800354F8` is not declared allocation capacity.
The survey covers retail successful pages, not arbitrary malformed streams or
the separate startup data-decompression allocation.

## Reproduction

Run from the repository root in WSL:

```sh
python3 tools/experiments/qualify_init_exception_storage.py --all-pages
python3 -m unittest tools.tests.test_init_exception_storage -v
```

The driver verifies original US ROM identity before parsing pages. Generated
object, compile log and per-page JSON remain under ignored
`conker/build/init-exception-storage`. The guest layout test recompiles the
current header into a private temporary directory instead of trusting a stale
ignored object. No ROM payload is added to the repository.

An initial broad `ultra64.h` probe hit the old compiler's comment parsing;
the final probe includes only the needed thread header and uses the project's
comment mode. Absolute output paths containing spaces also produced no object;
the final command uses relative paths, removes stale output first, and checks
the compiler log. The final guest compile is warning-clean.

## Verification

- Both complete 507-page retained-core surveys pass; the final run uses the
  finalized write-check helper and reproduces the same peak on page 50.
- All six new storage tests pass (0.457 seconds), including a fresh guest
  SDK layout compile into private temporary storage.
- All 587 project tool tests pass (98.136 seconds); the Init subset is 112 tests.
- Root `make tools-check` and `git diff --check` pass.
- Existing linked ELF `.init` (164,048 bytes) and `.init_data` (17,376 bytes)
  independently compare byte-for-byte with the pristine decompressed image.
  Their SHA-256 values remain
  `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`
  and `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.
  No production source rebuild or gameplay/hardware qualification is claimed.

## Next

These boundaries narrow the connected adapter investigation without settling
ownership. Preserve the actual 32-FPR context extent in future storage models.
The frame-backed C still needs fitting text and a proven stack/adapter contract.
Do not add nested C frames based only on the 632-byte numerical gap, or report
the current SDK type as the full retail thread context.
