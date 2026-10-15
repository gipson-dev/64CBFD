# Table Fade Callback Frame Restoration And Guarded Match

Date: 2026-10-15. Finish the matching boundary from
[Note 1403](1403-table-fade-callback-recovery-and-frame-gap-20261015.md)
without narrowing the full additional-source / Game objective.

## Result

Replace `func_1516F024`'s zero-return stub in
`conker/src/game/generated_19A8B0.c` with its complete semantic C callback.
**All 103 linked words / 412 bytes are byte-exact**, VA `0x1516F024`, ROM
`0x19C4D4`, original frame **0x68**. Raw C has **103 words / 15 positional
differences**; this is a **guarded match, not a direct raw C match**.

Preserve the four 11-byte table snapshots, packed record widths, full-word
clamps/completion, live post-helper step/extent and actual helper interfaces
recovered in Note 1403. Keep the address-based name and concise measured
comment. Add only private owner declarations; no shared header, caller,
compiler profile or original assembly is changed. No frame or FP guards.

## Measured Frame Provenance

The existing hash-gated observer follows only a newly owned compiler driver
and children. Capture the actual CFE/UOPT consumer inputs, decode descriptor-
defined records, require fired frame watches and successful producer/consumer/
driver exits, and compare all emitted text, function definitions, relocations
and pools against a normal compile. The isolated target must also equal its
complete owner. No compiler modification, simulated-memory writes or installs.

The old form reserves 64 CFE bytes, grows to 68 in UOPT, and rounds to 72
local bytes in UGEN. The accepted form introduces genuine live post-helper
`step` and `coefficient` locals before the existing scalar/table declarations.
They are assigned after the movement helper and both used in the extent
calculation, not dummy padding or physical-register bindings.

| Measurement | Previous Recovery | Accepted C |
| --- | ---: | ---: |
| CFE M definition | 64 | 72 |
| UOPT M definition | 68 | 76 |
| UGEN local reservation | 72 | 80 |
| Saved-register reservation | 8 | 8 |
| Outgoing reservation | 16 | 16 |
| Observed temporary increment | 0 | 0 |
| Final frame | 96 | 104 |
| Raw differences | 19 | 15 |

Frame writes are `0 -> 8 -> 24 -> 96` versus `0 -> 8 -> 24 -> 104`.
The accepted table offsets are M-32/-44/-56/-68, yielding the original
`SP+0x48/+0x3C/+0x30/+0x24`; the index home moves M-12 -> M-20 and stays
at original `SP+0x54`. Saved RA and incoming record homes are also original.
All four compiler hashes remain those documented in Note 1322/1403.

Thirteen maintained source forms are screened. Naming operands throughout
the earlier fade path also recovers the frame but causes 59 differences;
keep the live declarations restricted to their actual tail work. Other tail
expression forms retain 15, 17, 19, 25 or 26 differences. Do not import them
as extra matches or add unused locals to force a frame.

The diagnostic object files are **not literally byte-identical**: `.mdebug`
contains run timestamps and normal/traced output-command names. The receipt
records that difference explicitly. Text, functions, relocations and pools
are identical; this is not a whole-object metadata-equality claim. The
production linked-ELF gate below compares every byte without such exclusions.

## Bounded Normalization

Raw target SHA-256:
`a4e70e3d7f6665707a623eeb4bd88762f9c11f4951cba7a63290fc90ec6113a4`.
Reject any unknown complete raw body or any of its 16 relocation bindings.

Append **27 expected-word guards**: **15 numeric replacements** and
**12 identity relocation-binding checks**. Preserve every old CSV byte,
including its mixed line endings. No insertion, omission or branch patch.

- Five words at +232..248 reorder independent fade address/load work with
  the closed T7 -> T8 -> T9 -> T7 cycle and commutative multiply order.
  Move step HI16 from +236 to +232 and LO16 from +240 to +244, preserving
  their actual symbol bindings and signed-low carries.
- Ten words in +320..380 rename the post-helper step, growth, old extent,
  product and constant temporary lifetimes. Preserve final V0. In particular,
  +356 starts A1's separate scale-table-address lifetime and must not join
  the earlier coefficient rename. The first isolated normalization caught
  this boundary as one remaining word; it was corrected before installation.
- The 12 identity rows check the remaining table, step and helper bindings.
  All table data and both actual helper interfaces remain semantic C.

Normalization is mechanically derived from compiled instructions, register
lifetimes and relocations, not a copied retail instruction body in C. Raw
instruction-fault scheduling remains different; only guarded emitted code
passes literal private/fault qualification.

## Fresh Qualification

**All 16 installed checks pass in 72.903 seconds**, no skips:

- **8,352 paired guest cases** now match complete private RAM/registers,
  memory/call events, LO, FP condition/values, writes and visited instructions,
  as well as the independent public reference. Cover mode 0..10, intensity/
  clamp boundaries, eight steps, three flags, four providers and both stack
  phases. Visit 102 words; retain the unreachable home store at +304.
- **232 paired fired guest-memory faults** match literal partial state.
  The raw schedule fails 48 of these comparisons. Every injection fires;
  no affine stack comparison, portable C fault or hardware claim.
- **270,336 native32 cases per O2/O0** execute the same complete C and
  preserve full record/table/provider observations. All **eight compiled
  guest/native negative controls** fail semantically and are rejected by
  normalization. The original 1,024-case merge-model receipt is unchanged
  historical evidence, not claimed as a new standalone sweep here.
- **264 actual helper-chain pairs** match full private states using the
  current 34/14/12/12-word movement, scale and nested helpers, all freshly
  compared with ROM and connected. Of **28 synthetic stack aliases**, 26
  complete and two reproduce identical unmapped-read prefixes after their
  saved index is overwritten. Do not count those two as completed runs or
  claim portable C aliasing, actual game-index validity or full gameplay.
- Three independent original/normalized links match all 103 words with
  seven independently rebased symbols across signed-low carry boundaries.
- Reject all **103 raw-word flips**, **48 relocation mutations**, **27 stale
  physical guard words** and **16 stale physical bindings**. Preserve all
  29 owner neighbors' bytes, sizes, relative relocations and pools.
- Reject all **52 live-input flips**, source-text changes, **27 appended
  guard-row mutations**, six physical code/helper/binding/data changes,
  eight exact-serialization changes, all **52 immutable-before flips** and
  all three exact successor inputs/captures. Freshly verify all **801 original
  archive fingerprints** and missing/corrupted compiler-capture controls.

The earlier pre-install run passes 11 checks in 31.782s. The corrected trace
check separately passes in 17.139s during the shared rebuild. Initial fixture
failures were a native control-patching recursion and an under-backed stack
alias; retain their diagnoses above, not as production defects. Zero Claude
calls. Reuse the prior additional-source audit without calling it a fresh
1,717-object rescreen; the whole source-review objective remains open.

## Complete Linked Image

Compare the entire **3,257,636-byte ELF** against the frozen predecessor with
only the target's original 412-byte slot, extent `12 -> 412`, and four exact
symbol/name serializations applied. All **413 changed bytes** are closed:
**307 target slot/extent bytes** and **106 metadata bytes**. Every other byte
is fixed; no symbol or metadata section/range is ignored.

The four adjacent symbol/name swaps are:

- `D_800D2E45` / `D_80089C28`
- `D_8008CBE8` / `func_15007A70`
- `D_800E0D9E` / `D_80089C70`
- `func_15070830` / `D_80089BC0`

Require their exact predecessor positions, name lengths, values, sizes,
bindings and section indices. Adjust each st_name offset for unequal name
lengths and require canonical named-definition equality except target size.
The initial target-only prediction rejected these 106 bytes; the new exact
permutation model and corruption controls close them without widening the
allowed image. Of 52 inputs, only ELF, owner and guards change; all **49
others**, including progress rows, shared headers, original assembly and
profiles, stay fixed. All **189,088 protected bytes / 720 owners** remain exact.

| Installed Input | SHA-256 |
| --- | --- |
| ELF | 43f01cd6db9d414aa372134ab47ee0d464ea53cc79200be7922dd96cf3644b09 |
| Owner | 89f090fd6271117e29c2faa1ca5a6609ca846618931fb76e23d4b71d98cb96d9 |
| Guards | 29d703d96e0013c3b74e85e4afc6923b810f3e7e2096c0b6bfe8d044ec72fdaa |

The shared guard dependency rebuilds many existing owners with their known
SDK/type/profile warnings, including the duplicate generated_12D630 recipe.
The build succeeds; isolated target compilation has zero diagnostics. Do not
repair unrelated warnings or claim a warning-free complete build.

Fresh official matcher: **Game 2,899/4,828 (60.05%)**, **total 3,572/5,501
(64.93%)**, **1,929 different**, zero drift. Init 492/492 and Debugger 181/181
remain exact. This was already a C-classified stub, so converted counts/bytes
remain fixed. Root README changes only its two matching aggregate rows.

## Banking And Next Work

Bank tools **908f406** first, then consumer source/guards/docs/pin. Shared
tools checks and both Windows syntax/standalone checks pass. Preserve older
mirror HEAD **ddbdd16** and all **671 initial dirty fingerprints**; copy only
five absent owned paths for **676 final paths**, all equal active tools.
No mirror reset/history copying/commit, push, host source/build/launch,
account change, install or frozen Release action.

The explicit full graph refresh refuses **19,429 nodes against 41,208**,
retaining 19,398 nodes from 2,972 excluded-but-present files. Preserve the
fail-closed result; await actual incremental commit workers separately.

Prepared WSL consumer-root reproduction:

```sh
python3 -m tools.experiments.game_table_fade_frame --screen
python3 -m tools.experiments.game_table_fade_frame --name tail-live-operands
python3 -m tools.experiments.game_table_fade_match
python3 -m unittest tools.tests.test_game_table_fade_match tools.tests.test_game_table_fade_match_installed -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

Completed subsequently in [Note 1405](1405-dual-factory-preset-direct-match-20261015.md):
all 148 words match directly from C. Its three narrowing casts are now measured
as native-only negatives because this IDO context optimizes them away; the
actual remaining source/home mismatch is resolved. Preserve the handoff below
as historical context.

Next recover **func_1516F2F8**, **148 words / 592 bytes**, ROM `0x19C7A8`,
frame `0xD8`. The adjacent `func_1516F1C0` preset is already semantic/exact;
do not redo it. The next routine has six inputs and two complete 49-word
factory packets. Preserve arg0's low byte across the first call; the original
arg1/arg2/arg3/arg5 word forwards must not inherit the archive's premature
u16/u8 casts. Inspect actual callers and both real factory boundaries before
choosing its interface or importing the draft. No next-function edit here.

Retain the inherited-stack renderer deferral and complete
[failed-comment/binding/unanchored queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md).
The full additional-source / Game goal remains active and incomplete.

## Post-Bank Verification

Consumer **f01675b3** banks source, guards, aggregate-only README changes,
working docs and the tools **908f406** pin. All **16 post-bank checks pass
in 121.611 seconds**, exit 0, including the entire independent image,
canonical bindings, all 52 input states, 801 archive hashes, guard-row and
capture corruption controls, literal private/fault behavior and real helpers.
The normal ELF/progress build is up to date; no production artifact changes
during the rerun. Raw C remains 103/15; only the documented guarded output
is exact across all 103 words.

Both active checkouts are clean before this receipt edit. Recheck independent
mirror ddbdd16: all **676 final fingerprints** remain fixed, all **671 initial
dirty files** are preserved and all five owned copies equal active tools.
Eight documents resolve **5,024 relative links with zero broken**. The source
commit's actual incremental graph workers finish at **41,218 nodes / 81,320
edges / 3,948 communities**, without forcing the refused smaller full scan.
Continue func_1516F2F8 and the complete additional-source / Game queues.
