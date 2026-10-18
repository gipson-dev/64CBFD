# Route Record Setup Installed Byte Match

Date: 2026-10-18. **Installed, normalized byte-exact C recovery; +1 match.**

## Result And Baseline

Replace the zero-return placeholder for `func_150870D0` with complete typed
`void func_150870D0(s32 key, s32 playerCount, s32 extraCount)` in
`conker/src/game/generated_B3020.c`. VA `150870D0..15087350`, ROM
`B4580..B4800`, **160 words / 640 bytes / frame 0x60**. The linked function
matches all 160 retail words at its original address.

Consumer predecessor **345ed002**, tools predecessor **b12e663**. Tools
**38eefad** is committed first. Continue the recovery and initial-capture
evidence from [1566](1566-route-record-setup-semantic-recovery-and-private-order-boundary-20261018.md)
and [1567](1567-route-record-setup-initial-s7-capture-and-delayed-stores-20261018.md).

Fresh installed matching counts:

| Section | Exact / C functions | Percent | Different | Drift |
| --- | ---: | ---: | ---: | ---: |
| Game | 2,991 / 4,828 | 61.95% | 1,837 | 0 |
| Total | 3,664 / 5,501 | 66.61% | 1,837 | 0 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The rebuilt conversion CSV independently confirms unchanged totals:
5,501/6,044 C functions (91.02%), 1,941,784/2,256,728 converted bytes (86.04%);
Game 4,828/5,323 (90.70%), 1,770,348/2,072,880 bytes (85.41%). This installation
restores a preexisting C stub, not a new language-conversion row. Root README
receives only the two changed aggregate matching rows, not a function narrative.

## Semantic Source And Compiler Evidence

The complete source preserves the full-width key/count interface, low-byte
seed indices, signed mode and count globals, five-neighbor last-tie selection,
both initial selector calls, closed-route walk, modular allocation size,
fresh per-record table/count/human reads and original field-store ordering.
The six observed scratch byte homes remain inside their recovered workspace;
the reserved struct view is not a claim about the original C type.

Seven focused source screens preserve all 72 primary-owner neighbors and pools.
Moving the next-index byte assignment into the final validity gate reduces
raw differences **39 to 37**, retaining 160 words/frame0x60 and the literal
nine-word initial S7 capture/delayed-store block. Shorter direct-field controls
(152/154/156 words) and 159-word nested/late-load controls are not installed.
Raw target SHA-256:
`bdfe29694f9756fa66c4a4be439376e2b1a81129d69ed74954f8cfbef31b5442`.

One **newly owned, normal-profile compiler capture** observes the isolated
body, independently checked identical to the full-owner target. Existing
fingerprint-locked frontend/UGEN helpers capture CFE and UOPT wire streams
without compiler-decision patches. All four prepared cc/cfe/uopt/ugen hashes,
fired probes, producer/consumer association, complete object text/functions/
bindings/pools, all four child exits and driver exit0, probe removal and final
null inferior are required. No debugger is attached to an existing application.

In procedure 768 the optimized wire loads seed M-23 before M-24. It copies the
after value through GPR2 to GPR30/FP, and loads the before value into GPR23/S7.
The final instructions instead read SP+0x48 before SP+0x49. Thus the read-order
reversal is **after the optimized wire**; this does not isolate UGEN versus
the assembler or observe the original retail compiler's choices. Frontend
indirect-field evaluation order and original source types are not inferred.
Completed captures are audited/reused by tests, not rerun on every suite call.

## Explicit Normalization

This is **not a direct C match or a pure instruction permutation**. The
file-free recipe rejects any unknown 640-byte input or any of its 26 bindings.
It uses closed GP lifetime changes, commutative operands, independent cursor/
argument setup and post-allocation scheduling, plus two explicit control cases:

1. Rejoin the selected-FF edge at the relocated read/gate block. This restores
   retail's otherwise-unused private-byte read on that path, closing the old
   36-versus-37 access count. It is not a portable indeterminate-byte C claim.
2. Coalesce the redundant after-value copy in source slot 74. Its two endpoints
   now denote S7. Derive the taken-return RA restore from the existing compiled
   C epilogue instruction in slot 148, use a likely branch, and rejoin at slot
   149. The ordinary epilogue restore remains for the other return paths.

All 160 **source slots** are accounted for, with no inserted/omitted slots.
One original copy operation is eliminated and an epilogue restore is duplicated
statically onto its return path; **not all original operations are retained**.
No routine-sized instruction blob is substituted. The normalized text and all
bindings independently equal the separately GNU-assembled original function.
Unrelocated normalized SHA-256:
`b98cd565a4ce4933e954e47e5d308624944833b82f0d81ed2772e12c412a274b`.

The 160 relocation-aware guards append after the exact **2,486,705-byte**
original manifest prefix. No Makefile change or flag override is added.
The original four GLOBAL_ASM routines and normal-profile projection override
remain preserved in the mixed owner.

## Fresh Qualification

**All 17 installed tests pass in 107.128 seconds, no skips.** The complete
pre-install run passes in 94.261 seconds. A final caller-receipt label-only
clarification is followed by a focused normalized-state/caller test pass in
46.709 seconds; it changes no C, guards or linked bytes.

- 1,259 paired raw-C guest cases: 530 route/count/provider cases and 729
  five-slot/class cases. Compare complete ordinary RAM, public access/call order
  and saved ABI, including both stack phases and guest-only aliases.
- The real 19/88/33-word lookup/selector/constructor helpers execute, freshly
  verified against retail; only allocation is opaque and caller-clobbering.
- 1,286 native32 cases per positive O0/O2 profile, both with UBSan, all three
  actual C helpers, complete output banks/globals/calls and all mode/player/
  human bytes. Five semantic negatives exit ordinary wrong-result 23.
- 472 real call-lifetime observations preserve initial S7 and unwritten seeds.
  The freshly recompiled older 43-difference recovery remains an effective
  negative. Its earlier source/input pins are not overwritten.
- 530 paired **normalized** ordinary cases and **466 fired normalized prefixes**
  agree with retail in complete RAM, all modeled GPR/FPR values, access/call
  order, PC and branch-delay identity. Both previously rejected boundaries
  close. The four-node constructor witness now has S7=after2 / FP=before3.
- Effective return/join controls require ordinary observed wrong state, not a
  crash: omitting the scheduled restore leaves RA `150871E0` instead of the
  outer `DEAD0000` at the fired return checkpoint; bypassing the restored join
  read produces 36 instead of 37 accesses on the selected-FF path.
- 41 raw and 41 normalized retail-only caller windows execute all three real
  argument loads, including A2 in the delay slot, and the caller's zero-result
  branch. Whole-Game scanning still finds the sole direct site in func_1509DFC4
  at `1509E1B8`. Full dispatcher/unknown indirect interfaces are not claimed.
- 186 raw-word/binding controls, 34 layout-recipe controls, 46 live/snapshot
  corruptions, three mixed-stage rejections and wrong-image/span controls fail
  closed. Compiler evidence adds 11 semantic, five lifecycle and five payload/
  fingerprint controls, with no new debugger capture for those negative tests.
- Ten independent GNU links cover three code placements and two additional
  global placements crossing HI16/LO16 carries. Ninety-six paired code-rebased
  guest cases agree. Changed-global guest execution is not claimed.
- Actual private mixed-profile padding preserves 72 neighbors in both profiles,
  all other padded bytes/addresses/extents and pools. All seven expanded Make
  commands reproduce qualification: primary has one no-unroll flag, override
  none; all 73 primary functions and all four retained assembly bodies agree.

Raw C still has 37 differences, the old private-order rejection and swapped
later saved roles; those diagnostics are retained explicitly. Matching credit
comes from the **installed normalized code and linked audit**, not raw output
agreement. Synthetic access cuts, finite native cases and opaque providers do
not prove physical traps, all portable-C domains, full callers or gameplay.
Native incompatible aliases, positive null allocations and malformed/nonclosing
routes retain their documented qualification exclusions.

## Actual Link And Audit

The first actual shadow link matches an independently constructed predecessor
image with only target instructions and the target symbol size 12-to-640
changed. **484 changed ELF bytes, zero metadata-order groups/exemptions.**
The production N64 build reproduces that immutable first prediction exactly.

All **6,057 function addresses** and **6,056 other bodies** stay fixed.
All **189,088 protected Game-data bytes / 720 owners** remain exact, zero
different bytes/owners, digest
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The other 20 frozen inputs keep their predecessor hashes; all 23 original
snapshots and the three successor snapshots remain guarded and immutable.

| Successor | SHA-256 |
| --- | --- |
| Whole ELF | `3c8fd0411cd80d7a66440b81db22eef663fc8d557d365cdbbf5b3ce43dd5591a` |
| B3020 source | `fb512dd6fda54a37ab8adb84fa5efc50527941de4c622d66e12c6c3481c8ddbd` |
| Guard manifest | `cc92cdc4549964c1e9ebca306ee85ff5b7e57392a657bd9b15386384a8ab49d4` |

The manifest dependency causes broad N64 recompilation. The build exits0;
existing warnings in untouched code and the duplicate generated_12D630 Make
recipe warnings remain. No warning-free build is claimed. Target/private
compiles and actual shadow commands add no new diagnostics. Preserve the
existing manifest line-ending policy/prefix rather than unrelated normalization.

## Bank And Resume

Tools **38eefad** first. Both tools copies pass three repository-setup tests
and smoke checks; consumer `make tools-check` passes. Only five absent task
files are added to the independently dirty standalone mirror. Preserve all
**1,274 old hashes**, its older ddbdd16 HEAD and now **1,279 dirty leaf paths**,
without reset or mirror commit. Five task pairs are ASCII/AST-valid and identical.
No push, Claude call, emulator/live gameplay, host-port edit or frozen Release
build/launch/modification. One owned compiler-debugger capture only.

The new integration suite uses the guarded historical 23-input view for its
raw diagnostics and actual Make reproduction after installation. Use it rather
than running predecessor-only fixture entrypoints directly against the new ELF:

```sh
python3 -m unittest tools.tests.test_game_route_record_integration -v
python3 -m tools.experiments.game_route_record_integration --audit
make -C conker match-progress NON_MATCHING=1
```

Ignored `conker/build/game-route-record-reload/` keeps the compiler capture,
wire facts and source screens; `game-route-record-integration/` keeps immutable
prediction/successors, private Make plans, guest/native/rebase/corruption
receipts, production-build log and installed audit. Unchanged broad neighbor
suites are not called fresh tests.

Next inspect **func_15087350**, the adjacent **604-word** route caller:
VA `15087350..15087CC0`, ROM `B4800..B5170`, retail frame **0x1C8**. Its
production source is still a three-word stub, not retained assembly. Prior
vector tests cover only four bounded retail windows, not its complete logic.
Derive its full arguments, route/helper/provider contract and complete body
before qualification. Keep this installed baseline fixed. Wider Game work
remains active, with 1,837 C functions still different.
