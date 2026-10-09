# Game Wrapped Record Step Match

Date: 2026-10-09

## Result And Baseline

Continue [Note 1154](1154-game-payload-callback-update-match-20261009.md)
under the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and
zero Claude calls. Convert complete GLOBAL_ASM **func_15148AF4** in
[generated_175250.c](../../conker/src/game/generated_175250.c):
VA **0x15148AF4..0x15148BA4**, ROM **0x175FA4..0x176054**,
**44 words / 176 bytes**, frameless. Raw semantic C emits all 44 words,
**43 unchanged and one commutative pointer-add difference**. One expected-
word guard normalizes that difference. This is guard-assisted matching,
not a direct compiler match; no filler, truncated body or profile override.

Start from clean parent **9330e866** and mounted tools **a2e5ea7**. The
assembly routine already matched retail; this checkpoint moves it to C.
Saved baseline ELF SHA-256:
`9882610856cfd36a0022c543d536b8b6817c335a3b74a95ce1c24abaea0e143e`.
The baseline contains **6,058 linked function slots** and **11,506 guards**.
Original assembly, four remaining GLOBAL_ASM bodies, other source/profile/
layout/header/build files and shared tool implementations stay unchanged.

Normal manifest-triggered rebuild succeeds in **268.698s**, with **489 cfe
warnings** across rebuilt owners. The existing duplicate generated_12D630
recipe warning remains. No warning-free full build is claimed. Strict linked
audit verifies **every ELF byte is identical**, including all **6,058 slots**,
code/data, sizes, headers, symbols and metadata. There is no audit exception.

Preserve **all 11,506 old guard rows and their exact CSV bytes**; append only
the one target row, total **11,507**. Exactly one progress row changes
**asm -> c**, credit **one function / 176 bytes**. Fresh totals: **5,486 /
6,042 converted (90.80%, 85.92% bytes)** and **3,403 / 5,486 exact
(62.03%)**; Game **4,813 / 5,321 converted (90.45%, 85.27% bytes)** and
**2,730 / 4,813 exact (56.72%)**. Init 492 / 492 and Debugger 181 / 181
stay exact. Zero drift and **2,083 still different**. Conversion measurements
filter the real US rows, excluding concatenated repeated CSV headers.

## Complete Recovered Contract

Inspect the entire [retail routine](../../conker/asm/175250.s) and its
complete banked payload and timer dispatchers, not just the isolated leaf.

- Capture records at actor **+0x94** and payload at **+0x98 once**.
- Load the signed starting byte at actor **+0x2E**. Decrement before each
  iteration. If negative, load live **unsigned actor+0x25**, subtract one
  and use that index. The count is lazy: do not read it without wrapping.
- Select a **20-byte record**. Update vertical velocity at **+0x0C** by
  subtracting payload gravity **+0x10** times **D_800BE9A4**.
- Update record X at **+0**, using payload X velocity **+0x04** and a fresh
  global time load. Update Y at **+0x04**, using the just-updated vertical
  velocity and another fresh time load. Update Z at **+0x08**, using payload
  Z velocity **+0x0C** and the fourth fresh time load.
- Preserve ordered single-precision multiply/add/subtract operations. The
  fifth record word is not consumed or changed by this routine.
- Read live signed endpoint actor **+0x2D after all four stores**. Continue
  with decrement in the taken branch delay until the current index equals
  that endpoint; return full-word **1**.

Do not add an empty-count exit, range clamp or production iteration bound.
Count zero can update record **-1** and return for endpoint **-1**, or cycle
for an unreachable endpoint. Other invalid endpoints can also cycle. Tests
bound observations of those emitted loops, not the production implementation.
Captured pointers do not imply cached public fields or a cached time value.
In the alias witness, the first velocity store changes the global time and
the remaining updates use its new value.

Actual protected **D_8008A3E0[2] at 0x8008A3E8** points to this leaf.
The complete **97-word func_15147EB8** invokes it and publishes position;
that updater is reached from complete **100-word func_15147740** through
actual **D_8008A200[1] at 0x8008A204**. Do not infer safe table bounds from
neighboring labels. Hardware/gameplay and complete upstream routing remain
separate from these emitted-function tests.

## Source Fitting And Guard Proof

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_wrapped_record_step_candidates.py)
and [qualification suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_wrapped_record_step_match.py)
reuse existing complete-owner IDO/GNU parsing, assembly processing/padding,
instruction oracle, native32 and linked audit helpers. Retain O2g3.

Moving the decrement to the top of the do loop resolves the complete loop
shape directly: bottom-postdecrement emits **45 words / 17 differences**;
selected top-decrement emits **44 / 1**, both frameless. Four profiles:
O2g3 **44 / frame0 / 1**, O2 **43 / frame0 / 3**, O1g3 and O1 each
**59 / frame0x10 / 58**. These are measured complete bodies, not prefixes.

Guard word **16**, function offset **0x40**, VA **0x15148B34**:
**0x01C23021 -> 0x004E3021**, ADDU **A2,T6,V0 -> A2,V0,T6**.
Both operands, destination and result remain unchanged; no frame/register
mapping, branch, access-order, floating operation or relocation is changed.
Both original HI16/LO16 relocations for D_800BE9A4 remain symbolic at
offsets **0x00 / 0x10**. Reject a stale expected word and prove an
unaffected-word control is not repaired by normalization.

Screen **42 complete compiled forms / five samples each**: **33 positive
forms** and **nine effective negatives**. Negatives are unsigned start,
signed count, unsigned endpoint, cached time, Y update before gravity,
invented empty exit, and s8/u8/u32 loop indices. Negative buffers are mapped
far enough to observe actual changed memory/termination rather than a crash.
Alternative positive forms can reorder independent reads; record that trace
difference separately from semantic memory/return agreement. Only the
selected raw/normalized/retail streams claim the complete retail access trace.

An exploratory baseline emits XOR, absent from the reused oracle's existing
coverage. Add its local register-XOR execution without modifying shared
oracle code. This was a test coverage limitation, not a production fix.

## Qualification Receipts

- **1,896 cases / 5,688 raw, normalized and retail executions** cover every
  byte pattern in start, endpoint and unsigned count, SP phases 0 / 8,
  finite time/record samples and signed zero. **504 cases** are bounded
  loop observations. All **44 words** execute. Complete public memory,
  access order, iteration count and outcome agree with the independent
  ordered reference; all three emitted streams have identical full state.
- **223 missing-public-byte triples**, four explicit cyclic fixtures and
  lazy count access checks preserve emitted fault prefixes. Zero-count
  record -1 behavior is retained. These are emitted-order facts, not
  portable C fault behavior, hardware traps or arbitrary private aliases.
- Preserve all **10 copied-owner neighbors**, relative relocations, pools
  and **zero diagnostics** before/after. Actually post-process the remaining
  assembly routines. Actual guarded padder emits **176 bytes without
  .space**. **Four independent GNU links / 80 cases** qualify moved entries,
  moved global time and HI/LO carry boundaries.
- **66,176 actual native32 C cases**: all **65,536 head/count byte pairs**
  with reachable endpoints, plus 128 signed reachable endpoints over five
  time samples. Compare all **11,200 record-canary bytes**, including the
  unchanged fifth words, against independent ordered float32 products.
  Cyclic inputs are emitted-prefix tests, never unbounded native calls.
- **40 connected cases / 120 executions** run the full **100 + 97 + 44
  word** timer/payload/leaf chain through both protected table identities.
  No callback or cleanup hook is needed in these fixtures. Record updates,
  position publication and full emitted states agree. This does not claim
  all upstream, other callback, cleanup or gameplay paths are qualified.

All **eight pre-install tests pass in 141.714s**, no skips. Fresh **35
shared tests pass in 5.747s**; both project-tools checks pass. Historical
baseline-sensitive target suites are retained, not reported as fresh reruns.
FCSR exceptions, NaN payloads, FTZ, interrupts and real hardware/gameplay
behavior remain unqualified.

Final post-install **eight tests pass in 135.871s**, no skips, including
the actual installed C/guard/progress and whole-ELF audit. The fresh matcher
confirms the aggregate counts above against the rebuilt ELF.
Post-install **35 shared tests pass again in 18.738s**; both tools checks
also pass again. Documentation validation checks **141 documents / 4,221
relative links / zero broken**. All **29 mounted/mirrored tooling files**
parse and have identical bytes. All **62 pre-existing standalone status
lines**, both independent dirty-file hashes and its HEAD are preserved.

## Banking And Open Boundaries

Ignored `conker/build/game-wrapped-record-step-test/` holds original baseline,
before ELF/guards/progress, complete candidate/native probes and slot/guest/
faults/forms/owner/linked/native/connected/after/build receipts. Preserve
the original before.elf; do not recapture it to hide an audit failure.
Commit no retail ROM, native/ELF binary, probe, progress CSV or save.

Per "Keep commited", tools checkpoint
**919a0c1c075131e1a877ddc12acda28e11d8d63b** is committed first; parent
source/guard/docs/gitlink pins that exact revision second. Mirror only the
two absent new tool files. Older standalone HEAD **ddbdd16**, both existing
dirty-file hashes and all other pre-existing status remain unchanged; do
not reset it or create a duplicate standalone commit. No push, pause,
dependency/account change or OGL/Release/runtime/editor work. Root README
receives aggregate rows only. Wider Game completion is not claimed.

Local Graphify query found no target node. Manual refresh refuses **16,984
nodes** over retained **38,771**, preserving **19,398 nodes from 2,972
excluded files still on disk**. Existing version/zero-node warnings remain.
No force or reinstall; reduced-corpus repair remains open. Check the parent
post-commit hook separately before the final clean-state report.

## Next Work

Completed in [Note 1156](1156-game-record-phase-shaping-match-20261009.md):
the 70-word callback now emits directly from semantic C without guards;
its complete successful timer/payload/leaf connection is qualified and the
whole ELF remains byte-identical. The original next-target description
below records this note's historical handoff, not an outstanding conversion.

Recover full first-stage callback **func_15148DE0**,
**D_8008A3E0[4]**, still GLOBAL_ASM in this owner: VA
**0x15148DE0..0x15148EF8**, ROM **0x176290..0x1763A8**,
**70 words / 280 bytes**, frameless. Complete assembly has a signed active-
count gate/decrement, signed division, halfword phase shaping, stored/reloaded
signed head wrap, and a forward 20-byte record loop with live payload flags,
count and endpoint. Preserve narrowing and actual termination; qualify it
through the same complete dispatcher rather than assume similarity to this
leaf. Slot-1 func_151488C4 and trail constructor func_151DA6F8's 61
differences remain open.
