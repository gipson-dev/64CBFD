# Game Record Distance-Level Direct Conversion

Date: 2026-10-08

## Result

Continue [Note 1126](1126-game-embedded-record-callback-direct-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
func_151D8C00 to complete C in
[generated_205C90.c](../../conker/src/game/generated_205C90.c).
All **87 words /348 bytes**, frame **0x38**, emit directly under existing
IDO 5.3 O2/g3. No new guards, filler, generated data, profiles, headers or
Makefile changes. Reference [205C90.s](../../conker/asm/205C90.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_205C90/func_151D8C00.s)
remain untouched. VA 0x151D8C00..0x151D8D5C, ROM 0x2060B0..0x20620C.

This converts already exact assembly to semantic C; it does not change
any linked instructions. The only progress-row change is this 348-byte slot.

## Recovered Contract

Owner-local RecordDistanceLevel layout: x/y/z at +0/+4/+8, inner radius +0xC,
width +0x10, inverse width +0x14, unsigned player byte +0x18; size28.
The native32 fixture asserts size, player offset and four-byte float/pointers.

Call func_15144B34 with unsigned player, subtract returned origin coordinates
from parameter coordinates, then call func_15143E64 on the private three-float
delta. Verified [game_16EE20.c](../../conker/src/game_16EE20.c) definitions
return the indexed player position and sqrtf of the squared vector magnitude.
Their complete actual implementations are not executed by these new tests;
lookup and magnitude are controlled interfaces.

Choose level1 below inner radius, level0 above inner+width, otherwise
1-(distance-inner)*inverseWidth. Write low byte of (u32)(level*8) at owner+0x12.
Retain R_MIPS_26 calls at +0x10 and +0x4C. Complete retail unsigned conversion
saves FCSR, requests truncation, handles the signed/unsigned fallback and
restores original FCSR. Return is void; no C promise about residual V0.

The initial owner-local non-prototype void declaration is tightened to
void(u8 *, RecordDistanceLevel *). The wrapper explicitly casts record+0x18
to the typed parameter pointer. This avoids leaving a call through an
untyped declaration with unlike pointer arguments. Wrapper remains all8
words directly exact; every other owner body stays unchanged. No shared ABI
header change.

## Focused Qualification

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_distance_level_candidates.py)
retains ten complete source forms. Typed selected, unsigned-long and named
scaled value emit directly; raw-byte and delta-first variants leave four
differences. Byte-cast identical code is a control, not a portable-C substitute
for u32 conversion. Existing profiles:

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 87 | 0x38 | 0 |
| O2 | 88 | 0x38 | 5 |
| O1/g3 | 109 | 0x30 | 102 |
| O1 | 108 | 0x30 | 103 |

[Eight helper tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_distance_level_match.py)
reuse the existing AreaOracle conversion handler, native32 harness, owner,
relocation and padder helpers without changing a shared engine:

- **49,152 guest cases**: all256 player bytes,32 boundary/exceptional
  configurations, two SP phases and three initial FCSR patterns. Compare
  complete selected/retail GP/FP state, memory and ordered trace plus an
  independent public semantic reference. Inner/outer equality and adjacent
  f32 values, non-normalized widths, signed zero, unsigned thresholds,
  negative results, NaN and infinities are covered.
- **84 reachable words /87 complete matching words**. The three unreachable
  compiler duplicates are +0x80, +0xA4 and +0x138. Do not claim they are
  dynamically reached; their equality is established by the complete slot.
- **72 mutation/alias/reload cases**, including embedded parameters, origin
  aliases and controlled incoming-owner/parameter home updates. Ten required
  access-fault prefixes and two skipped-field gates preserve read/write
  order and conditional access. Private-home mutations qualify emitted guest
  instructions, not portable C parameter mutation.
- **6,144 complete native32 C executions** through a volatile function
  pointer:256 players,12 distance/conversion configurations and two callback
  mutation modes. Include finite casts below, at and above 2^31 and below
  2^32; check owner/parameter bytes and origin values. Only defined finite
  nonnegative u32 casts are asserted on the host.
- Four profiles/40 ordinary control executions and six effective compiled
  negatives: signed player, wrong output byte, wrong scale, wrong inner/outer
  comparisons and signed result cast. Negative signed loads delegate to the
  existing CopyOracle handler locally; signed trunc.w.s handling is local
  and used only by a compiled control.
- Copied-owner compilation has zero diagnostics, **ten unchanged neighbors**,
  identical pools/relative relocations. Actual padder emits exactly348 bytes,
  no filler or data. Five independent entry/lookup/magnitude links execute
  fifteen fixtures, preserving both symbolic calls.
- **48 complete retail-wrapper/helper connections** execute actual8-word
  wrapper and complete87-word helper with embedded parameters, unsigned
  byte players, two SP phases, threshold cases and callback mutations.

Initial run: seven pass, one negative-control fixture failure,58.971s.
The unsupported signed LB occurs only in the deliberately wrong signed-player
control. Reuse the existing handler rather than treating it as a production
failure. Corrected **eight pre-install tests pass in65.555s**.

Initial installed helper/wrapper run:16 tests pass in104.021s. After typed
declaration/cast cleanup,16 tests pass in101.245s; the updated eight-wrapper
suite separately passes in34.865s. Its actual cast native fixture now checks
**262,144 cases /16,384 aligned offsets**, eight result patterns and two
mutation modes, all96 canary-window bytes. Alignment4 is required by the
typed parameter cast; historical Note1126's million arbitrary byte offsets
qualified the former byte-pointer source, not this typed cast. Raw unaligned
transport remains instruction-only guest evidence. Refresh that native
receipt separately: one test passes in4.454s.

The bounded FP oracle does not emulate all hardware rounding, exception
flags, traps, denormals or NaN payload propagation. Model agreement plus
complete instruction equality is not hardware/gameplay acceptance. Full
actual callees, full dispatcher/caller and PC-port behavior remain open.

## Linked Audit And Progress

Build succeeds with existing duplicate generated_12D630 recipe warnings;
actual owner compilation emits no diagnostics. Audit from
game-record-embedded-callback-test/after.json preserves all **6,058
bodies/addresses/extents**,6,042 retail slots/16 overflow symbols,
protected sections and **11,146 guards**. The linked callback table and
dispatch prefix remain retail-exact. All720 Game-data owners /189,088 bytes
retain SHA256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Exactly one conversion change: func_151D8C00, asm -> c,348 bytes.

| Section | Converted | Converted Bytes | Byte-Exact | Different /Drift |
| --- | --- | --- | --- | --- |
| Total | 5,471/6,042 (90.55%) | 1,932,728/2,256,728 (85.64%) | 3,382/5,471 (61.82%) | 2,089 /0 |
| Game | 4,798/5,321 (90.17%) | 1,761,292/2,072,880 (84.97%) | 2,709/4,798 (56.46%) | 2,089 /0 |

Init492/492 and Debugger181/181 converted routines stay exact. New ignored
baseline: conker/build/game-record-distance-level-test/after.json.
Fresh shared padder checks: ten pass in0.045s. Both tools project checks,
driver/forms/profiles/CLI help and syntax gates pass. Root README aggregate
rows only; detailed updates stay here and in the concise indexes.

## Repository And Workflow Boundary

Source HEAD c73a85af, parent/mounted tools pin8d84f4b and standalone tools
HEAD ddbdd16 are preserved. Existing wrapper/source/docs and tools dirty work
remain intact. No Codex commit, push, stash, reset, pin or branch change.
Driver and both target tests are mirrored between mounted/standalone tools.
Remote publication is not verified.

Source-before SHA256:
77b9bef2388ea241605efd47ab5d70023d544b608e84544d2f4481f55f861ce3.
Guard CSV:
5f029ab9d10ca4a13d8ad7b3b045c8fcf5f73592a67c10471d7ef738b2ed0d78.
Private ROM:
f2ce85ad021adccf773bc62f847b4818bca5227bfdd5d14433231f8c663fd382.
Source-before copy and before-progress rows are retained beside ignored
audit/qualification receipts. Every post-install audit uses the prior
wrapper baseline, not a self-generated after baseline.

Claude budget0 /attempted0 /completed0. Fresh focused target/neighbor gates,
all-linked-body audit and unchanged shared tool checks support this conversion.
Reuse broader Note1125/1126 receipts explicitly, not as freshly rerun suites.
No frozen OGL Release, real saves/configuration or live-runtime operations.

Graphify refresh is attempted after code changes. Existing ignore changes
reduce the scan corpus; the refresh refuses to replace38,459 nodes with
16,683-node extraction. Preserve the old graph and user ignore changes;
do not force an overwrite. Refresh remains incomplete.

Documentation validation:113 documents /3,924 relative links /zero broken.
Fifteen relevant tools policy/fixture files are byte-identical between mounted
and standalone copies. An initial mirror check finds two extra trailing blank
lines in the new standalone test; remove only those lines and rerun successfully.

## Next Function

Resume adjacent retained
[func_151D8B24.s](../../conker/asm/nonmatchings/generated_205C90/func_151D8B24.s):
**25 words /100 bytes**, frame0x20, VA0x151D8B24..0x151D8B88,
ROM0x205FD4..0x206038. Two installed sibling callers invoke it before their
second helper. It iterates four byte player indices, re-reads owner+0x13
each iteration and calls func_1501C17C for each set bit. Callback mutations
of future mask bits are important; do not cache the mask or treat this as
only a count. Keep actual return/caller contract, native byte behavior,
access order, mutations and copied-owner preservation as the next gates.

Fresh complete C screening is saved in ignored
conker/build/game-record-distance-level-test/next-player-mask.py and
next-mask-screen.json. The ordinary byte-index for loop emits25 words/frame0x20/
zero differences under O2/g3, no pools/diagnostics; O2 has three differences,
O1/g3 and O1 each emit24 words/24 differences. Callee func_1501C17C in
[generated_48FD0.c](../../conker/src/game/generated_48FD0.c) uses the player's
mapping byte and clears a mapped entry only below4. Candidate remains
uninstalled and behavior-unqualified; start next turn from this measured body.

Wider Game matching remains active; this is a completed target, not completion
of the overall decomp or PC port.
