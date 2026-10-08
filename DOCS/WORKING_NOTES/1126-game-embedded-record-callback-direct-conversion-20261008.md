# Game Embedded Record Callback Direct Conversion

Date: 2026-10-08

## Result

Continue [Note 1125](1125-game-node-group-swap-direct-conversion-20261008.md)
using the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
`func_151D8BE0` to complete C in
[generated_205C90.c](../../conker/src/game/generated_205C90.c).
All **8 words /32 bytes**, **frame 0x18**, emit directly under existing
IDO 5.3 O2/g3. No guards, filler, new data, profile, header or Makefile changes.
Reference [205C90.s](../../conker/asm/205C90.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_205C90/func_151D8BE0.s)
stay untouched. VA `0x151D8BE0..0x151D8C00`, ROM `0x206090..0x2060B0`.

This is an asm-to-C conversion of already exact assembly. Every linked
function body remains unchanged; only the 32-byte conversion row changes.

## Calling Contract

`void func_151D8BE0(u8 *record)` calls func_151D8C00 once with original
record and embedded record+0x18, computing A1 in the JAL delay slot.
Preserve the 0x18 frame, saved RA lifetime and symbolic R_MIPS_26 call at+8.
There is no wrapper dereference, null gate, extra call or explicit result.
The helper's V0 survives the emitted wrapper, but void C promises no result.

The actual caller is indirect: table D_8008FCC0 in
[234780.rodata.s](../../conker/asm/data/234780.rodata.s) contains
`[func_151D8BE0, 0, 0, 0]`. Dispatcher
[func_151D8A24.s](../../conker/asm/nonmatchings/generated_205C90/func_151D8A24.s)
reads signed selector +0x14. Zero selects this callback; -1 skips table/call.
Its JALR passes the record and continuation does not consume callback V0.
Do not invent callbacks for the three null table entries.

## Source Fit And Qualification

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_embedded_callback_candidates.py):
plain call, explicit discarded result, indexed embedded address and an
integer-return forwarding control all emit the same 8 words. The selected
source remains void because the caller ignores result; identical compiler
output does not establish the original source return type.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 8 | 0x18 | 0 |
| O2 | 8 | 0x18 | 0 |
| O1/g3 | 11 | 0x18 | 8 |
| O1 | 11 | 0x18 | 9 |

[Eight tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_embedded_callback_match.py)
reuse complete-body MIPS/native32, signed-byte, owner and padding helpers:

- **131,248 guest cases**: all 65,536 low16 patterns, alternating four upper
  patterns and eight helper results, two SP phases, plus 176 explicit null,
  unaligned, sign/wrap-boundary cases. All8 words reached. Complete selected/
  retail GP/FP, ordered trace and memory agree; saved ABI is checked. Raw
  invalid-pointer transport is emitted-instruction evidence, not a portable
  C promise about null/out-of-object pointer arithmetic.
- **96 callback mutation/alias cases**, including incoming-home storage,
  preserve captured arguments. Ten required-stack fault prefixes check
  failure before helper and saved-RA read after helper. Arbitrary private
  saved-RA aliases and hardware behavior remain unqualified.
- **1,048,576 actual native32 complete-C executions** through a volatile
  function pointer:65,536 valid private-array offsets, eight result patterns,
  two mutation modes. Assert four-byte pointers/ints; verify call count,
  both arguments and all 96 canary-window bytes.
- Fourteen source/profile forms,28 ordinary executions and seven effective
  compiled negatives: wrong/scaled offset, swapped arguments, shifted base,
  added null gate, double call and forced zero. The forced-zero control
  distinguishes emitted V0, not a promised void-C return value.
- Copied owner retains **10 unchanged neighbors**, normalized pools and
  relative relocations, zero diagnostics. Real padder emits exactly 32 bytes,
  no filler/data. Six independent entry/helper links and 18 executions retain
  symbolic call relocation across shifted and edge bindings.
- **96 actual dispatch-prefix/wrapper executions**: ten retail caller words,
  four retail table words, signed zero/-1 selector, JALR, complete wrapper,
  helper clobbers/mutations and two SP phases. A synthetic exit follows the
  prefix. Helper is a controlled interface; full helper/caller gameplay is
  not qualified by these wrapper tests.

Initial eight-test run: six pass, two fixture failures in 30.984s. O1/control
bodies extend into the retail helper address, so execute controls with a real
symbolic re-link to non-overlapping0x151E8C00; keep original-profile raw
measurements. The existing Triangle oracle lacks signed LB needed by the
real caller; delegate only that instruction to existing CopyOracle handler.
No shared engine or production-body change; selected full-state/order checks
stay strict. Corrected **eight pre-install tests pass in 29.054s**;
**eight post-install tests pass in 33.021s**, zero skips/errors/failures.
Ten shared padder checks pass in 0.043s. Both tools project checks, syntax,
both drivers/profiles/CLI help pass.

The first adapted audit accidentally points at its own not-yet-created
after.json. Correct its baseline path before installation. Corrected audits
pass against `game-node-group-swap-test/after.json`; no baseline/body/data
assertion is weakened.

## Linked Audit And Progress

Build succeeds with existing duplicate generated_12D630 recipe warnings;
actual owner compilation has no diagnostics. All **6,058 bodies/addresses/
extents**,6,042 retail slots/16 overflow symbols, protected sections and
**11,146 guards** remain unchanged. The audit also checks the actual linked
callback table and dispatch prefix directly against retail, not only fixtures.
All720 Game-data owners /189,088 bytes retain SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Exactly one conversion-row change: `func_151D8BE0: asm -> c`,32 bytes.

| Section | Converted | Converted Bytes | Byte-Exact | Different /Drift |
| --- | --- | --- | --- | --- |
| Total | 5,470/6,042 (90.53%) | 1,932,380/2,256,728 (85.63%) | 3,381/5,470 (61.81%) | 2,089 /0 |
| Game | 4,797/5,321 (90.15%) | 1,760,944/2,072,880 (84.95%) | 2,708/4,797 (56.45%) | 2,089 /0 |

Init 492/492 and Debugger 181/181 stay exact. New ignored baseline:
`conker/build/game-record-embedded-callback-test/after.json`.
Root README changes aggregate rows only.

## Repository And Workflow Record

At turn start, source HEAD b794defb and mounted tools 35dd106 retain the
Note1125 dirty state. Source-before SHA256:
`87406d90e09068a94844a27c06ce5cdc0d760bd8939bf16c98733088bb45bdf7`;
reference 205C90.s SHA256:
`1486d7fdf9a87e5aff20f0dfc427862fd4a55a322990f7e95e082a9666994ff2`.
Private ROM, guard and profile fingerprints were also read before edits.
Ignored `owner-before.c` and before-progress.json retain scoped comparison.

External Git commits during the turn advance source to
`c73a85af2f704caf3a8cc5e291879737441e109d` and parent/mounted tools pin to
`8d84f4b9cc890ae6138af77db5c25a9dde9e08e5`. Preserve them; the wrapper driver
is committed there. Wrapper source edit, its test and the distance-helper
experiment remain local at this checkpoint. Standalone tools HEAD stays
ddbdd16 with mirrored files; do not reset or overwrite that dirty checkout.
No Git commit/push by Codex; remote publication is not verified this turn.

Claude budget0 /attempted0 /completed0. Exact source/assembly/compiler and
focused tests settle this wrapper without a second opinion. Reuse prior
Note1125 broader receipts explicitly, not as freshly rerun tests: shared
helpers/profiles and every linked body/data/guard are unchanged. New native,
guest, indirect-caller, copied-owner and full linked gates are fresh.

Required Graphify update attempted after source changes; it refuses to
replace 38,459 nodes with 16,671 after the existing ignore changes reduced its
corpus. Preserve the old graph, no force-overwrite. Refresh remains incomplete.
No frozen OGL Release, saves/configuration or live-runtime operation.

Documentation validation: **112 documents /3,910 relative links /zero broken**.
Fourteen relevant tools policy/fixture files are byte-identical between
mounted and standalone copies. All three checkouts pass whitespace checks.

## Next Helper: Measured Direct Candidate

`func_151D8C00` remains retained assembly: **87 words /348 bytes**, frame 0x38,
VA 0x151D8C00..0x151D8D5C, ROM 0x2060B0..0x20620C. Its complete semantic
[distance-level driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_distance_level_candidates.py)
already emits **87 words/frame 0x38/zero differences**, no pools/diagnostics.
Symbolic calls are at+0x10 to func_15144B34 and+0x4C to func_15143E64.

Verified callees in [game_16EE20.c](../../conker/src/game_16EE20.c): the first
returns the player's position; the second returns the three-coordinate
magnitude. Parameters hold position+0/+4/+8, inner radius+0xC, width+0x10,
inverse width+0x14 and unsigned player+0x18. Compute distance; choose1 inside,
0 outside inner+width, otherwise1-(distance-inner)*inverseWidth; write low
byte of `(u32)(level*8)` to owner+0x12. Preserve full unsigned conversion,
including emitted FCSR save/truncate/fallback/restore sequence.

Ten source forms: typed initial, unsigned-long cast, byte-cast control and
named-scaled value are direct; raw byte parameters and delta-first layout
each leave four differences. Volatile parameter/owner forms disturb layout
or lifetime. Existing O2 without g3 emits88 words/five differences; O1/g3
109 words/102 differences, O1 108 words/103 differences. The byte-cast form's
identical guest words do not prove portable C behavior outside u8 range.

**Not installed or behavior-qualified.** Continue from saved complete body:

1. Use existing AreaOracle conversion/FCSR handling; explicitly retain its
   bounded-model limits, not a claim of complete hardware FP status/traps.
2. Qualify inner/outer boundaries, all byte players, unsigned-conversion
   branches, lookup/magnitude mutations, incoming-home reloads, aliases,
   fault prefixes and valid native32 ranges. Check actual wrapper/helper
   connection; distinguish guest exceptional values from defined host casts.
3. Build copied owner with a consistent owner-local declaration: existing
   `s32 func_151D8C00()` must become void when installing a void definition.
   Add only the necessary parameter layout, preserve wrapper's8 words and
   all neighbors/pools/call relocations. No shared-header/profile rewrite.
4. Install only after focused gates; rebuild/audit from this new wrapper
   baseline and measure the sole 348-byte asm-to-C row change.

Wider Game matching/resolver/full caller/hardware/gameplay/PC-port work
remains open; this checkpoint does not complete the goal.
