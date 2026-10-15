# Table Fade Callback Recovery And Frame Gap

Date: 2026-10-15. Continue the full additional-source / Game objective after
[Note 1402](1402-counter-preset-guarded-match-20261015.md).

## Result And Installation Boundary

Recover `func_1516F024`, VA `0x1516F024`, ROM `0x19C4D4`, in
`conker/src/game/generated_19A8B0.c`: **103 words / 412 bytes**. The selected
complete semantic candidate and its production-padded object both have
**103 words / 19 positional differences**, with zero isolated IDO diagnostics.
Its frame is **0x60**, not retail **0x68**. This is **semantic recovery only,
not a byte match or an installed C conversion**. Production retains the stub.

Bank the experiment and focused tests in tools **e086765**. The tool reports
`installable=false`; its direct-match qualifier rejects this candidate. No
new guards, profile changes, frame patches, invented padding locals, volatile
declarations or affine private-stack acceptance are used. Root README and
all production source, ELF, guards and progress rows remain unchanged.

## Recovered Behavior

- Copy four actual **11-byte** tables before record reads or helper calls:
  scales `D_8008CBC4`, growth `D_8008CBD0`, limits `D_8008CBDC`, and fades
  `D_8008CBE8`. Preserve four partial-word tails and their untouched padding
  bytes; these are typed struct snapshots, not uninitialized `void *` locals.
- Snapshot unsigned mode byte `record+0x2C` and intensity byte `+0x1F`.
  The active byte is `+0x24`. Active intensity rises by wrapping word
  `step << 4` and clamps using a signed word comparison to its table limit;
  inactive nonzero intensity falls by `step * fades[index]` and clamps at zero.
- Keep the **full word** through clamping and completion, storing only the
  low byte. Re-read active for the return test. In particular, mode 6,
  intensity 1, inactive, step -1 yields word 256 / stored byte 0, and must still
  continue rather than return 1. The archive's byte accumulator is incorrect.
- Call actual `func_1516F864(record)` with its one consumed argument. After
  it returns, re-read the live step and signed extent halfword `+0x14`, but
  retain the snapshotted mode and local growth/scale tables. Add the wrapping
  growth product, store halfwords `+0x16` and `+0x14`, and set `+0x18` to 100
  for mode 3. Call `func_1516F94C(record, scale)` with two consumed arguments;
  return 0. Early inactive full-word zero returns 1 without either call.

The original callback-table entry at `D_8008CBA0` index 2 points to this
routine. The 48-byte table source at ROM `0x231684` matches the frozen linked
ELF exactly. Its original owner, `conker/asm/data/231660.rodata.s`, is already
protected as the existing `callback_original` input; do not duplicate that
path under another manifest key. The malformed archived locals, uninitialized
`sp`, word-wide field accesses and premature byte truncation are not adopted.
Keep the address-based function name and measured semantic comment.

## Emission Evidence

Screen **ten maintained source forms and twelve declaration layouts**, all
with the existing owner profile. All 22 retain 103 words and frame 0x60; none
matches. Moving the genuine scalar declarations `(value, extent, index)`
ahead of table declarations yields the selected **19-difference** result,
improving the initial 26. `(extent, value, index)` ties it. Halfword-extent
variants retain 21 differences. Literal local arrays create a separate pool
and 34 differences; do not invent a pool mapping. An additional scoped
old-style helper-declaration probe is unchanged at 103/19; retain typed helpers.

The selected index spill is `SP+0x54`; four table bases are `+0x48`, `+0x3C`,
`+0x30`, `+0x24`, matching retail's relative layout. Absolute private addresses
still differ by eight because the frame differs. Saved RA remains `SP+0x14`.

| Remaining Group | Byte Offsets From Entry | Words |
| --- | --- | ---: |
| Frame and incoming record home | 0, 284, 292, 304, 336, 400 | 6 |
| Fade address/load/register schedule | 232, 236, 240, 244, 248 | 5 |
| Extent step/table/register/operand order | 320, 324, 328, 332, 348, 352, 364, 380 | 8 |

The object contains 16 target relocations: four table HI16/LO16 pairs, three
step HI16/LO16 pairs and two helper JAL bindings. Raw binding offsets remain
in the ignored candidate objects/receipts. No normalization is implemented
for this target, and equal lengths do not close these instruction differences.

## Fresh Qualification

**All ten checks pass in 37.649 seconds**:

- **8,352 paired guest cases** match the full record, external memory, result
  and actual consumed call arguments on the bounded mode domain 0..10. Cover
  intensity/clamp boundaries, eight word steps, three active values and four
  provider mutation/clobber modes. All **8,352 retain private differences**;
  this is not whole-machine equality. Visit 102 of 103 retail words; retain the
  unreachable duplicate incoming-home store at `+0x130`, rather than omit it.
- **270,336 native32 cases per O2/O0** cover all 256 intensity bytes, 11 modes,
  eight steps, three flags and four provider modes. Check the full 80-byte record,
  table snapshots, live step, call order/arguments and 11-byte struct size.
  This is native byte/halfword ABI evidence, not big-endian guest memory,
  arbitrary index validity or portable alias qualification.
- **Eight effective compiled guest and native negatives** reject wrong
  active width, rise factor, early truncation, fade/growth table, special
  mode and live growth/scale reads. Only expected-negative native variants
  suppress unused-variable warnings when a mutation intentionally removes a
  local use; positive O2/O0 and IDO diagnostic gates remain unchanged.
- **264 real helper-chain pairs** execute the current linked 34-word movement,
  14-word scale and both 12-word nested helpers. Freshly compare all four with
  ROM and connect every nested call; these helpers are not opaque hooks in
  this test. This does not qualify the complete caller, gameplay or hardware.
- **1,024 partial-word merge cases** cover all four lanes. Also verify the
  four three-byte tails and untouched slot padding for candidate and retail.
  Cross-check the low-word big-endian LWR/SWR masks and shifts against
  [Project64's interpreter](https://github.com/project64/project64/blob/develop/Source/Project64-core/N64System/Interpreter/InterpreterOps.cpp).
  The target-local oracle models aligned LWR reads and selected SWR bytes;
  it does not claim complete CPU, bus, TLB or exception behavior.
- **116 paired fired guest-memory faults all retain literal private failures**.
  Frame/SP and the first RA store diverge. Every injection fires; do not
  relabel this rejection evidence as matching fault-prefix qualification.
- Preserve all 29 owner neighbors' raw bytes, sizes and relative relocations,
  and all pools. The actual production padder retains 103/19; it adds no match.
- Freshly verify all **52 unique production inputs**, all 52 immutable-capture
  and 52 live-input flip controls, all **801 original archive fingerprints**,
  and **189,088 protected data bytes / 720 owners**, zero differences.

Reuse established compiler/padder/oracle/native32 helpers; no shared helper
changes. The initial unqualified `game-table-fade-callback` capture included
a duplicate path key and was rejected. Preserve that diagnostic directory;
the corrected 52-input immutable captures use the separate owned
`conker/build/game-table-fade-recovery/` directory. Neither fixture repair
is evidence of a production defect. Zero Claude calls, installs, account
changes, host source/build/launch or frozen Release operations.

## Progress And Banking

Normal ELF/progress build is up to date. Fresh official matcher remains
**Game 2,898/4,828 (60.02%)**, **total 3,571/5,501 (64.92%)**, **1,930 different**,
zero drift. Init 492/492 and Debugger 181/181 remain exact. Converted counts and
bytes remain fixed. This recovery earns no new match/conversion credit.

Shared tools checks and Windows syntax pass. Preserve independent mirror
HEAD **ddbdd16** and all **669 initial dirty fingerprints**; copy only the
two absent owned files, giving **671 final paths**. Both hashes match active
tools, and its standalone ROM-free strict-gate check passes. Do not commit,
reset or copy history into that older mirror. No push is performed.

The explicit full Graphify refresh refuses **19,418 nodes against 41,197**,
retaining 19,398 nodes from 2,972 excluded-but-present paths. Preserve the
fail-closed graph; do not force a smaller replacement or install an update.
Await actual incremental commit workers separately.

Prepared WSL consumer-root reproduction:

```sh
python3 -m tools.experiments.game_table_fade_callback
python3 -m tools.experiments.game_table_fade_callback --screen
python3 -m tools.experiments.game_table_fade_callback --layouts
python3 -m unittest tools.tests.test_game_table_fade_callback -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

## Next Work

Stay on **func_1516F024**. Inspect the exact CFE/UOPT local-reservation and
frame formation with the existing hash-gated compiler tools, then resolve
the six frame/home words and the two remaining scheduling/register groups.
Do not manufacture unused locals, frame patches or affine private acceptance.
Require literal private/fault agreement, independent rebases, owner/padder
checks and a complete linked-image audit before replacing the production stub.

Retain the inherited-stack renderer deferral and full
[failed-comment/binding/unanchored queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md).
The earlier 1,717-object audit is historical, not freshly rerun here. The full
additional-source / Game objective remains open.
