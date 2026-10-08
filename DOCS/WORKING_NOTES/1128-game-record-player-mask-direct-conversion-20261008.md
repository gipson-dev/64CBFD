# Game Record Player-Mask Direct Conversion

Date: 2026-10-08

## Result

Continue [Note 1127](1127-game-record-distance-level-direct-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
func_151D8B24 to complete C in
[generated_205C90.c](../../conker/src/game/generated_205C90.c).
All **25 words /100 bytes**, frame **0x20**, emit directly under existing
IDO 5.3 O2/g3. No guards, filler, new data, profiles, headers or Makefile changes.
Reference [205C90.s](../../conker/asm/205C90.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_205C90/func_151D8B24.s)
remain untouched. VA0x151D8B24..0x151D8B88, ROM0x205FD4..0x206038.

This converts already exact assembly to semantic C. Every linked instruction
remains unchanged; only this 100-byte conversion row changes.

## Recovered Contract

void func_151D8B24(u8 *owner) iterates four unsigned byte player indices.
Read owner+0x13 on every iteration and call func_1501C17C(player) when that
player's bit is set. Capture owner across callbacks, but reload the mask
after each callback. Keep saved S0/S1/RA lifetimes, byte counter narrowing,
branch-likely increment and R_MIPS_26 call at +0x34.
The retail V0 finishes at4; void C does not promise a return value.

The actual [generated_48FD0.c](../../conker/src/game/generated_48FD0.c)
callee uses unsigned D_80084060[player] mapping. It clears D_800BE93C[index]
only when index<4; invalid mappings skip the write. All thirteen linked
callee words match the retail reference, and the tests execute those actual
instructions. Owner/mapped-state aliases demonstrate that the clear can
change future mask bits, so caching the mask is not equivalent.

Both actual direct callers, func_151D8B88 and func_151D8BB4, are complete
eleven-word routines. They pass the owner, call this dispatcher, reload their
incoming owner home and call func_15169804 or func_15169824. They do not
consume the dispatcher's residual V0. Only the second helpers remain
controlled interfaces in these tests; no full-gameplay acceptance is claimed.

Add a local void/u8 callback prototype. Two existing integer-parameter
callers now explicitly cast arg0 to u8* before calling the typed dispatcher.
Keep their existing parameter/return declarations; no wider ABI cleanup.
Both callers and every other owner body remain byte-identical.

## Source Fit And Qualification

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_player_mask_candidates.py)
retains thirteen complete source forms. Ordinary byte loop and explicit
nonzero test emit directly. Signed/unsigned int counters still emit25 words
but frame0x28 and23 differences; explicit byte increment leaves9 differences,
volatile owner15. Cached-mask control emits24 words/22 differences.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 25 | 0x20 | 0 |
| O2 | 25 | 0x20 | 3 |
| O1/g3 | 24 | 0x20 | 24 |
| O1 | 24 | 0x20 | 24 |

[Eight focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_player_mask_match.py)
reuse existing Triangle/ProgressReference, native32, owner, relocation and
padder helpers; no shared oracle change:

- **197,120 guest cases**: every initial/first-callback byte-mask pair in two
  SP phases, all65,536 per-player post-callback nibble schedules with alternating
  SP phases, and512 static masks. All25 words reached. Independent ordered
  public reference plus complete selected/retail GP/FP/trace/memory equality.
- **Twelve required fault prefixes**: mask reads, saved S0/S1/RA stores,
  next mask read after callback and saved-RA reload after callbacks, in two
  SP phases. These establish bounded emitted-instruction order, not portable
  C faults or arbitrary saved-register aliases.
- **1,114,368 complete native32 C executions** through a volatile function
  pointer:256 static masks,65,536 byte mutation pairs, and16 initial low
  nibbles times65,536 per-player update schedules. Assert four-byte pointer/
  int, ordered callback arguments/count and all64 canary bytes. Valid array
  pointers only.
- Sixteen source/profile forms and72 ordinary executions; seven effective
  compiled negatives: cached mask, wrong offset, reversed bits, three players,
  inverted gate, first-hit-only break and shifted argument. No unsupported
  instruction or assertion exception is used as a passing negative.
- Copied owner has zero diagnostics and **ten unchanged neighbors**, identical
  pools/relative relocations. Actual padder emits exactly100 bytes, no filler/
  data. Five independent entry/callback links execute20 fixtures.
- **25,600 actual thirteen-word clearer connections** cover all256 masks,
  ten mapping patterns, ordinary owner plus four mapped-state aliases and
  two SP phases. **3,072 complete direct-caller executions** cover both
  eleven-word callers, all256 masks, three mappings and two SP phases.
  Two additional instruction cases prove dispatcher captures owner while its
  caller reloads a changed home. Actual linked callee/callers equal retail;
  later helper semantics remain controlled.

First eight-test run: six pass, two fixture failures,139.408s. The saved-RA
fault hook initially deletes the same byte on every callback; restrict that
deletion to its first callback, so the intended final RA load causes the fault.
Native GCC correctly rejects misleading same-line if/increment formatting;
put the increments on separate lines without relaxing -Werror. The corrected
two checks pass in1.617s. Reuse the unchanged six prequalification receipts
explicitly rather than rerunning the exhaustive cases before installation.

Fresh installed **all eight tests pass in145.264s**, zero skips/errors/failures.
Ten shared padder checks pass in0.073s. Both tools project checks, source/
profile driver, CLI help and syntax checks pass. No shared helpers/profiles
change, so broader unchanged Note1127/1126 suites are prior receipts, not
claimed as freshly rerun. New focused qualification and all-body audit are fresh.

## Linked Audit And Progress

Build succeeds with the existing duplicate generated_12D630 recipe warnings;
the actual owner compile has no diagnostics. Audit from
game-record-distance-level-test/after.json preserves all **6,058
bodies/addresses/extents**,6,042 retail slots/16 overflow symbols,
protected sections and **11,146 guards**. Actual linked callback table/
dispatch prefix also remain retail-exact. All720 Game-data owners /189,088
bytes retain SHA256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Exactly one conversion-row change: func_151D8B24, asm -> c,100 bytes.

| Section | Converted | Converted Bytes | Byte-Exact | Different /Drift |
| --- | --- | --- | --- | --- |
| Total | 5,472/6,042 (90.57%) | 1,932,828/2,256,728 (85.65%) | 3,383/5,472 (61.82%) | 2,089 /0 |
| Game | 4,799/5,321 (90.19%) | 1,761,392/2,072,880 (84.97%) | 2,710/4,799 (56.47%) | 2,089 /0 |

Init492/492 and Debugger181/181 converted routines remain exact.
New ignored baseline: conker/build/game-record-player-mask-test/after.json.
Root README changes aggregates only. Detailed updates remain in this note
and concise current indexes.

## Repository And Workflow Record

Source HEAD c73a85af, parent/mounted tools pin8d84f4b and standalone tools
HEAD ddbdd16 are preserved along with unrelated dirty work. No Codex
commit/push/stash/reset/branch/pin change; remote publication not verified.
Both target tools files are mirrored between mounted and standalone copies.
Source-before SHA256:
7df51c55ee691ce1ea56c346c6cd1971361de56a53b73d73f7125831fe03064d.
Original owner and before-progress rows are retained beside ignored receipts.
Guard CSV SHA256:
5f029ab9d10ca4a13d8ad7b3b045c8fcf5f73592a67c10471d7ef738b2ed0d78.
Reference205C90.s SHA256:
1486d7fdf9a87e5aff20f0dfc427862fd4a55a322990f7e95e082a9666994ff2.
Every installed audit compares the prior distance baseline, not its own after.

Claude budget0 /attempted0 /completed0. Follow focused gates plus whole-linked
audit and explicitly reused unchanged receipts. No OGL Release, real saves/
configuration or live-runtime operation.

Graphify refresh is attempted after code edits. It refuses to replace38,459
nodes with16,694 after the existing ignore changes reduced its corpus.
Preserve old graph and user ignore changes; no forced overwrite.
Graph refresh remains incomplete and is not a matching gate failure.

Documentation validation:114 documents /3,937 relative links /zero broken.
Seventeen relevant tools policy/fixture files are byte-identical between
mounted and standalone copies. All three checkouts pass whitespace checks.
Final source SHA256:
1b88c25b732795af584427280cae903f5c8ca3d3248230444d5a6b96a023c90b.
Final progress SHA256:
0cff94677de94b8e11fd9e35c4a86ab84b835e24b12026b6f5eaeb898f323f89.

## Next Function: Complete Direct Candidate

[func_151D87E0.s](../../conker/asm/nonmatchings/generated_205C90/func_151D87E0.s)
is retained: **34 words /136 bytes**, frame0, VA0x151D87E0..0x151D8868,
ROM0x205C90..0x205D18. Fresh complete candidate already emits34 words/zero
differences, no pools/diagnostics, under O2/g3. Prototype and old-style byte
argument forms both match, as does an int mapped-index local. An int player
counter emits67 words/63 differences. Ignored next-predicate.py,
next-predicate-screen.json and next-predicate-prototype.c retain the evidence.

It accepts a byte player mask and scans selected players in order. A selected
mapping>=4 returns0 immediately; a valid selected D_800BE944[index] nonzero
returns1 immediately. Otherwise continue and return0. Do not replace it with
a simple any-state OR that ignores the invalid-first early return.

Actual retained func_151D8868 calls it with owner+5 in the JAL delay slot
and branches on V0. Next gates: all byte masks/mappings/state flags, selected
read laziness and early-return order, argument home/width, native32, copied
owner, rebased globals and bounded actual caller-prefix connection. Candidate
is uninstalled and not behavior-qualified.

Wider Game matching/full callers/hardware/gameplay/PC-port work remains open.
