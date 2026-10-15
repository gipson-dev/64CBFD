# Counter Preset Recovery And Private Schedule Gap

Date: 2026-10-15. Continue the complete additional-source / Game objective
from [Note 1400](1400-actor-type-preset-direct-match-20261015.md).

## Result And Boundary

Recover **func_1516EED4**, VA `0x1516EED4`, ROM `0x19C384`, **84 retail
words / 336 bytes**, frame `0xD0`, in `generated_19A8B0.c`. The maintained
semantic candidate emits **85 words / 76 positional differences**, with no
compiler diagnostics. It is **not installed or counted as byte-exact**.
The direct-match and strict production-padding gates reject it. No production
C, header, compiler profile, guard CSV, ELF or progress row is changed.

The source and tests are in tools `experiments/game_counter_preset.py` and
`tests/test_game_counter_preset.py`. Keep the address-based function name,
four signed-word inputs and void result. The archived caller in
`conker/src/game_981E0.c` forwards four arguments and ignores the result;
this is source-interface evidence, not whole-caller binary qualification.

## Recovered Semantics

- Test **signed slot < 4**, with no added lower-bound check. Do not replace
  this with an unsigned 0..3 test. No counter byte is read when slot >= 4.
- Load `D_800DD2A0[slot]` as an **unsigned byte** and compare it with the full
  **signed-word threshold**. Negative thresholds accept every byte value.
  The scalar declaration agrees with the existing `variables.h` declaration;
  use `(&D_800DD2A0)[arg0]` without changing the shared header.
- On acceptance, clear the counter **before** the factory call, including
  null allocation. A provider's subsequent counter write must survive return.
- Preserve the complete **49-argument func_1516D99C packet**: fixed extents
  `0x200`, slot31 = 30, full incoming slot word at34, unsigned low arg2 byte
  at47 and full arg3 word at48. The actual factory consumes some fields
  narrowly; its storage contract is distinct from the physical caller packet.

The original archive's cached pointer form compiles to **85/78**. Retail
captures outgoing input homes before clearing the counter, whereas this
cached-pointer form clears earlier. Inline repeated subscripts recover that
clear/capture ordering and the ascending zero-store schedule, giving **85/76**.
Explicit input locals, pointer assignment/index/cast variations and register
hints do not fix the original opening reload.

Fresh screen: **27 maintained recipes**, all warning-free. Twenty emit 85/78,
four inline/assigned-gate forms emit 85/76, two pointer-difference gates 86/84,
and the conditional-expression gate 90/83. No profile is adopted or changed.

## Remaining Closed Delta

Retail's opening `arg0` load into T6 feeds both `slti` and the pointer add in
the first branch delay slot. Raw C instead reloads arg0 into T7 at **+0x28**,
then adds the pointer after the branch. That also leaves the rejected path's
private V0 different. Later temporary allocation rotates through ten registers.

`diagnostic_fit` describes the complete difference without copying retail
instruction words: remove the redundant +0x28 load, shorten the opening
branch displacement by one, and apply the closed register cycle
`8 -> 25 -> 24 -> 15 -> 14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8`.
Preserve the opening T6 index lifetime before joining the later cycle.
This produces **84 described words / zero differences**. All 85 independent
input-word flips and a wrong-length input are rejected by its SHA-256 gate.

| Diagnostic Input | SHA-256 |
| --- | --- |
| Linked 85-word candidate | 368f27dd4d9fa72f9effe32c97fad90f86ff257964b5e7ef7a58cbb221092952 |
| Raw object target | 898c7e35028b16b935e6af23ea92bebb10b329ea42d5ebcac359af50c57f00a0 |

Raw relocations are +0x18 HI16 / +0x1C LO16 for `D_800DD2A0`, and +0x13C
R_MIPS_26 for `func_1516D99C`. The diagnostic is **not** a padder, guard
manifest, rebased normalization, full private/fault match, or installed image.
Normal tool output remains `installable=false`; `--qualify` still rejects 85/76.
Do not give this descriptive transform matching credit or bypass those gates.

## Fresh Qualification

**All 11 focused checks pass in 142.171 seconds**:

- **3,240 paired guest cases**, 1,386 accepted / 1,854 rejected, cover signed
  slot/threshold boundaries, byte values, two stack phases and three provider
  clobber modes. Public packets and external memory agree; all 84 retail
  instructions are visited. **All 3,240 full private states still differ**.
- **40,960 native32 cases per O2/O0 profile** cover all 256 counter bytes,
  ten signed thresholds and eight backed indices from -64 through 11. The
  macro-backed array keeps native pointer arithmetic within its real fixture.
  It does not establish arbitrary pointer or actual game-slot validity.
- **Ten effective compiled guest/native negatives** detect unsigned slot or
  threshold, signed-byte reads, strict comparison, wrong/misordered clear,
  wide flags and wrong actor, final word or preset. A target-local LB oracle
  extension supports the signed-byte negative; no shared helper is changed.
- Three independent original/selected text, table and call rebases cross
  signed-low carry boundaries. **Twelve backed, synthetic rebased home aliases**
  now preserve the original full packet when the clear touches an input home.
  These qualify the repaired ordering, not all rebased words or native C aliases.
- **138 paired fired guest-memory faults** give 30 exact / 108 different private
  prefixes. Every injection fires; private fault order remains unqualified.
- **128 real wrapper/factory/allocator-chain pairs** include 85 rejections,
  ten null allocations and 33 registered records. Execute the actual 125-word
  factory and 28-word allocator wrapper; verify the complete initialized record
  and that null allocation does not undo the pre-call clear. Only lower heap
  and registration providers are modeled. No hardware/gameplay/host claim.
- All 29 owner neighbors retain raw sizes/bytes, pools and relative relocations.
  All **52 production inputs** are byte-identical, including the entire ELF,
  guards, shared headers and progress rows. Reject all 52 immutable-capture
  corruptions and all 52 live-input corruptions. The protected **189,088 bytes /
  720 owners** remain exact. Freshly verify all **801 archive fingerprints**.

The first negative-control run exposed unsupported LB in the target oracle;
the local signed-load implementation fixes the fixture, not the production
routine. Later full runs pass; do not reinterpret the failed fixture as a
retail/C defect. Prior unchanged suites are historical receipts, not fresh tests.

## Bounded Review

One attempted/completed tool-free Claude analysis, using the existing
claude.ai / firstParty Pro route without provider/account overrides. Fresh
CLI 2.1.218 help/auth checks precede the call; init reports tools=[] and
mcp_servers=[], zero tool-use events, exit0. No second writer or second call.
Stdin packet SHA-256:
`ef5aefe67b18fe9e87bf363219c7572834bd3686ee5496bca8c34012476f89ff`.
The response/usage receipt is ignored in `claude-analysis.jsonl` below; a CLI
cost estimate is not an observed subscription charge.

Independently test the inline-subscript suggestion: accept its observed
clear/capture improvement, **not** the claim that it removes the opening
reload. Reject the suggested source-after-call clear: provider-entry and
provider-write controls prove that ordering wrong. The original source shape
and cause of the compiler's extra load are still not uniquely established.

## Banking And Next Work

Bank tools **f14494c** before consumer documentation/pin changes. Shared tool
checks and native Windows syntax pass. Preserve mirror ddbdd16 and all
**663 initial dirty fingerprints**; copy only two absent owned files for
**665 final paths**. Its standalone ROM-free recipe/gate check passes.

Normal ELF/progress build is up to date. Fresh official matcher remains
**Game 2,897/4,828 (60.00%)**, **total 3,570/5,501 (64.90%)**, different 1,931,
zero drift; converted counts/bytes stay fixed. Root README needs no change.
The separate full Graphify update refuses 19,397 nodes against 41,176 and retains
19,398 nodes from 2,972 excluded-but-present files. Do not force the smaller
scan; await the incremental commit worker. No push or host/Release operation.

Ignored evidence: `conker/build/game-counter-preset/`. Reproduce:

```sh
python3 -m tools.experiments.game_counter_preset
python3 -m tools.experiments.game_counter_preset --screen
python3 -m unittest tools.tests.test_game_counter_preset -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

Next finish this same function: inspect the original index/home lifetime
before the first branch, then seek direct C scheduling or separately qualify
the described closed transform. Any guarded route must gate the actual raw
words and all three relocations, preserve branch-delay and saved-RA lifetime,
pass literal private/fault and independent rebase tests, reject corrupted
guards, and close the **entire** installed ELF before source adoption.
No guard normalization has been implemented or qualified by a passing
diagnostic alone. After this function, continue func_1516F024 and the full
[additional-source repair queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md).
Keep the inherited-stack deferral and wider Game objective open. The earlier
1,717-object audit is not rerun or reclassified as fresh evidence here.

## Post-Bank Verification

Consumer **9f5b8cf7** banks the recovery handoff and tools f14494c pin.
All **11 post-bank checks pass in 59.781 seconds**, including all 52 unchanged
production inputs, all 801 original archive hashes, the effective negative
controls and the diagnostic's 85 independent input-word corruption controls.
The production stub is still untouched; raw 85/76 remains non-installable.

Both active checkouts are clean before this receipt edit. Recheck mirror
ddbdd16: all **665 final fingerprints** stay fixed, including every one of
the **663 initial dirty files**; the two owned copies equal the active tools.
Seven documents resolve **5,003 relative links with zero broken**. The consumer
commit's incremental graph workers finish at **41,186 nodes / 81,281 edges /
3,813 communities**, without forcing the refused smaller full scan. No live
test or graph handle from that checkpoint remains. Keep the wider goal open.
