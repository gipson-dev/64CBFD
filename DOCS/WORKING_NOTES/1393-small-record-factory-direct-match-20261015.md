# Small Record Factory Direct Match

Verified 2026-10-15. The previous goal turn recovered the larger factory;
this checkpoint recovers its neighboring small factory from the additional
source lead. The whole additional-C / Game goal remains active.

## Target And Source

| Item | Value |
| --- | --- |
| Function / owner | func_1516D4E8 / generated_19A8B0 |
| VA / ROM | 0x1516D4E8 / 0x19A998 |
| Complete slot / frame | 100 words, 400 bytes / 0x38 bytes |
| Existing allocator / secondary | func_15167A68 / func_150448D0 |
| Consumer / tools predecessor | d805b028 / 49b76f0 |
| Profile | Existing O2/g3, unchanged |

The archive `game/game_19A8B0.c` supplies the allocation and optional-call
shape, but again substitutes overlapping 32-bit writes for packed retail
fields. Recover all 31 argument widths from the full original routine, six
signed halfword fields, byte fields, full-word kind/selector/context inputs,
null paths and stored secondary pointer. Use meaningful `record` and `kind`
locals and a purpose comment without inventing names for unproven fields.

Add a private forward declaration for the actual tagged
`struct PositionScaleRecord71820` and its nine-argument creator. Its position
and scale arguments are s16 pointers into the primary record; the returned
pointer is stored with that real type, not an integer-return placeholder.
Do not alter either helper's definition or shared headers.

Fresh corrected full-owner screen: 100 words / five differences, no diagnostics.
Moving the zero-byte clear after the neighboring halfword assignment recovers
the retail three-word schedule, leaving only two saved-pointer stack offsets.
Ordering the existing `record` local before `kind` recovers the original
`sp+0x34` store/reload instead of `sp+0x30`: **all 100 raw words match**.
No fake/unused locals, volatile, new guards or profile changes are installed.
The proper typed pointer remains live across the optional call.

Bounded rejected forms include all-word parameters (100 / 32), saved-record
copy and named-binding forms (100 / 5), and narrower kind locals (101 / 86).
Register annotation and unsigned kind leave the two stack differences. These
are bounded observations, not a claim that every alternative C form is ruled
out. The older isolated archive screen's 120 / 106 result is historical lead
evidence, not the accepted body.

## Fresh Qualification

All **14 focused checks pass in 47.525 seconds** across
`test_game_small_record_factory`, `_candidates` and `_installed`.

- All 100 raw and actual production-padded words equal retail, including the
  complete frame, both call delay slots, the sp+0x34 pointer lifetime and the
  final secondary-pointer store. No extra/omitted alignment words.
- 3,072 guest cases cover every input/field, both stack phases, primary and
  secondary nulls, high bits/sign boundaries, live post-provider homes, and
  the early optional-selector read before later field stores. Included are
  1,536 backed stack-alias cases. An independent semantic memory/call reference
  agrees, including provider clobbers and destination mutations.
- 630 paired, fired guest access-fault prefixes preserve complete retail order.
  This is emitted guest-order qualification, not portable C fault semantics or
  full N64 hardware/runtime acceptance.
- Actual selected C passes 4,096 native32 cases at each O2/O0 profile, with
  canaries, typed field values, all nine optional-call arguments, provider
  effects and stored null/non-null pointers. Six compiled semantic negatives
  fail in both guest and native fixtures: wrong kind, allocation size,
  halfword source, position/scale pointer, optional gate and zero clear.
  Native fixtures do not claim guest stack-alias behavior.
- Independently assemble the full original routine for three text/two-call
  target rebase pairs. All 100 words and rebased call packets agree.
- 128 cases connect the real recovered factory and unchanged installed
  **28-word allocator / 37-word position-scale creator**. Check the actual
  five-word heap call, registration, eight-word record-builder call, optional
  allocation failure and returned secondary fields/pointers. Only the lower
  heap, registration and record-builder providers remain opaque. No full
  gameplay or host-transfer acceptance follows from these bounded models.
- All 29 copied-owner neighbors retain raw bytes, extents, relative relocation
  ownership and normalized pools. The larger factory and earlier wrapper are
  unchanged. Reuse older unchanged broad-suite receipts explicitly, not as
  fresh test runs.

## Complete Image And Progress

The normal ELF/progress build succeeds. Build the entire expected ELF
independently from the pinned predecessor, 400 retail bytes and only symbol
extent `12 -> 400`. The installed image equals it: **299 changed bytes**,
target slot/extent only, no metadata allowances. Every other ELF byte and all
**189,088 protected bytes / 720 owners** stay fixed. Known duplicate
generated_12D630 recipe warnings remain; do not claim a warning-free project.

| Input | SHA-256 |
| --- | --- |
| ELF | 1975c17c531328dc05d7462d93e3362308edf353cca4c99cc0815f1531333327 |
| Owner | 1d96ec240e7ef4685e0dfe144cab10ee7c85adbbe5f38e23251c0e01f40db117 |
| Unchanged guards | 5d5daf3748fdb04f64d3bc337f875552b6f6e6a3dd870b74095f01d0d232eb73 |
| Unchanged progress CSV | 595443d0129e7d6ccd1f824b050854d5759c0f45c1af5b0818ef7cde682528ee |

Pin all **45 inputs**: two changes, 43 unchanged. Effective controls alter
every current input, source text, six physical ELF/symbol/helper/data sites
and every before/after capture. The exact-input inverse rejects unknown or
corrupt artifacts; current image and connected-chain acceptance use no
inverse. All **801 original archive fingerprints** are freshly checked and
unchanged. Generated progress CSV remains ignored, not force-added.

Fresh matcher: Game **2,892/4,828 (59.90%)**, total **3,565/5,501 (64.81%)**,
different **1,936**, zero drift. Init stays 492/492 and Debugger 181/181 exact.
Conversions stay total **5,501/6,044 (91.02%), bytes 86.04%**, Game
**4,828/5,323 (90.70%), bytes 85.41%**. The stub was already counted C, so this
adds one exact body without increasing converted counts. Root README changes
only two aggregate rows; recovery details remain here.

## Banking And Next Work

Bank tools **b545f58** before the consumer pin/source/docs. Shared tools checks,
standalone five-file syntax and all three ROM-free tests pass. Preserve the
independent older-mirror ddbdd16 HEAD and all **628 initial dirty fingerprints**;
copy only five absent owned files and verify all **633 final fingerprints**.
No mirror commit/reset, push, host source/build/launch, real save/configuration
or frozen Release action. Claude calls: zero. Ignored receipts live under
`conker/build/game-small-record-factory/`.

Seven documents / 4,948 relative Markdown links validate with zero broken.
The full Graphify update refuses 19,317 nodes against 41,096 curated nodes,
retaining 19,398 nodes from 2,972 excluded-but-present files. Preserve that
fail-closed result and await the incremental commit worker; do not force it.

Next recover **func_1516D678**, the still-stubbed **48-word record updater** in
this owner. Its old isolated archive screen emits 50 words / 38 real
differences. Re-establish the complete live field/argument/callee contract and
active compiler shape before adoption; that old result is only a lead. Keep
the full additional-source/binding queue, handwritten Init hardware routines
and func_1510BF60 open. No automatic host transfer or completion claim.

## Post-Bank Verification

Consumer **f3a2ee59** banks the source, tools b545f58 pin, aggregate README
rows and working documentation. All **14 post-bank checks pass in 47.216
seconds**, including the independent complete current image, all 45 input
states and fresh hashes for all 801 archive files. The normal ELF/progress
build is up to date. This function remains a direct 100-word C match with no
new guards; the existing larger-factory guards remain unchanged.

Both active checkouts are clean before this receipt. All 633 final older-mirror
fingerprints, including the 628 initial fingerprints and independent ddbdd16
HEAD, remain fixed. The source commit's incremental graph worker completes at
**41,104 nodes / 81,201 edges / 3,844 communities**, without forcing the refused
smaller full scan. No push, host/Release action or full-game completion claim.
Continue the whole additional-C / Game goal at func_1516D678.
