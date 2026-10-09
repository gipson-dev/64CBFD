# Game Record Phase Shaping Match

Date: 2026-10-09

## Result And Baseline

Continue [Note 1155](1155-game-wrapped-record-step-match-20261009.md)
under the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and
zero Claude calls. Convert complete GLOBAL_ASM **func_15148DE0** in
[generated_175250.c](../../conker/src/game/generated_175250.c):
VA **0x15148DE0..0x15148EF8**, ROM **0x176290..0x1763A8**,
**70 words / 280 bytes**, frameless. All **70 words emit directly from C**
with the existing O2g3 profile. No guards, artificial filler, shortened body,
inline assembly or compiler-profile override.

Start from clean parent **3e2f3e6d** and mounted tools **919a0c1**.
The original assembly was already retail-exact; this checkpoint credits its
conversion to semantic C without changing executable behavior. The saved
and rebuilt complete ELF share SHA-256
`9882610856cfd36a0022c543d536b8b6817c335a3b74a95ce1c24abaea0e143e`.
Every ELF byte, all **6,058 function slots**, code/data, sizes, addresses,
headers, symbols and metadata remain identical. No audit exception or mask.
Original assembly, three remaining GLOBAL_ASM bodies, profiles, Makefile,
layouts, headers and shared tool implementations remain unchanged.

All **11,507 guard rows and exact manifest bytes remain unchanged**.
Only the target conversion CSV row changes **asm -> c**, credit **one
function / 280 bytes**. Fresh totals: **5,487 / 6,042 converted (90.81%,
85.93% bytes)** and **3,404 / 5,487 exact (62.04%)**; Game **4,814 /
5,321 converted (90.47%, 85.28% bytes)** and **2,731 / 4,814 exact
(56.73%)**. Init 492 / 492 and Debugger 181 / 181 stay exact. Zero drift
and **2,083 still different**. Measure only US CSV rows, excluding repeated
concatenated headers. Root README receives aggregate rows only.

## Complete Recovered Contract

Inspect the entire [retail routine](../../conker/asm/175250.s), not a prefix.

- Read signed active byte actor **+0x2C**. Below **3**, return full-word
  **0** without accessing payload, records, cursor, head or count.
- Otherwise decrement that stored byte and reload it signed. Its divisor
  is now **2..126**. Capture payload **+0x98** and records **+0x94 once**.
- Capture signed start cursor actor **+0x2D**. Compute unsigned-halfword
  step **4096 / reloaded active byte**. Initial phase is **4096** when
  payload **+0x18 bit0x20** is set, otherwise **0**.
- Decrement the stored signed head at actor **+0x2E**, then reload the
  narrowed byte. Only if that reload is negative, load **unsigned actor
  +0x25**, store count minus one back to head, and reload it signed again.
  In particular an original head **0x80** becomes **0x7F**; a count of
  **255** stores **0xFE**, then reloads as **-2**, not 254.
- Walk forward from the captured signed start while it differs from live
  signed head. Each **20-byte record** receives only a **u16 at +0x10**;
  all other record bytes stay untouched.
- After each store, reread live payload flags. Bit0x20 selects subtraction
  of step; otherwise add step. Narrow the phase after each update to **16
  bits**, preserving wrap rather than clamping it.
- Load live unsigned count, increment the full-width index and reset it
  to zero only on equality with that count. Reload live signed head after
  the possible wrap; do not replace either field with a cached value.
- Return full-word **1**, including a successful empty window.

No invented null/range check, empty-count return or production loop bound.
Stable count5/stored-head127 and count255/stored-head-2 fixtures produce
genuine small-table wrap cycles. Count-zero fixtures qualify only their first **12
iterations**, not an infinite-loop claim: their full-width forward index
has different eventual behavior. Wider invalid-address and interrupt
behavior is unqualified. Stored signed-byte narrowing is measured for IDO
and native32, not claimed as universal portable-C implementation behavior.

Actual protected **D_8008A3E0[4] at 0x8008A3F0** points to this leaf.
The complete **97-word func_15147EB8** calls it and publishes position;
that updater is invoked by complete **100-word func_15147740** through
actual **D_8008A200[1] at 0x8008A204**. Neighboring table labels do not
authorize invented selector bounds. Connected fixtures qualify successful
dispatch, not all other callbacks, cleanup, upstream routing or gameplay.

## Source Fitting

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_phase_shaping_candidates.py)
and [qualification suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_phase_shaping_match.py)
reuse established full-owner IDO/GNU parsers, assembly processor/padder,
signed-byte/division-capable instruction oracle, native32 and linked audit.
No shared helper is changed. The local oracle validates stores before
logging completed accesses, matching its independent reference's fault
prefix convention rather than logging a failed store as a completed write.

Early-return source emits **70 words / 54 differences**. Keeping the
positive gate around the body gives **70 / 31**. Ordinary setup ordering
then resolves the entire routine: records capture, payload capture,
signed cursor load, division, initial phase. Retain natural stored-byte
decrements/reloads and u16 phase/step lifetimes. Twelve representative
declaration orders and all 24 setup orders remain reproducible in the
driver; the initial 120 declaration permutations alone did not improve
the 31-difference positive-gate body. No speculative broad batch is installed.

O2g3 and O2 each emit **70 words / frame0 / zero differences**. O1g3 and
O1 each emit **88 / frame0x10 / 85 differences**. Preserve the existing
owner O2g3 profile. The leaf has **no relocations or data/rodata pool**;
independent entry links test relative branches, not nonexistent HI/LO pairs.

## Qualification Receipts

- **3,136 cases / 6,272 raw-C and retail executions** cover every byte
  pattern in active count, start, head, unsigned wrap count and flags,
  SP phases 0 / 8, narrowing boundaries and ascending/descending u16 wrap.
  **1,174 cases** are bounded loop observations, not proof that every one
  is non-returning. Public memory, completed access order, iteration count
  and return/outcome match the independent reference. Raw and retail full
  modeled register/FP/LO/event/memory states agree.
- All **65 reachable words** execute. Word indices **17 / 21 / 22 / 23**
  are unreachable division-check paths because the gated divisor is 2..126
  and numerator is 4096. Word **54** is the original unreachable duplicate
  phase add bypassed by branch-likely scheduling. All five emit naturally
  and match; do not delete them or invent filler to replace them.
- **69 missing-public-byte pairs**, inactive fixtures containing only the
  active byte, lazy empty record/count checks, and four bounded-loop prefix
  fixtures retain the completed-access/fault conventions. These are emitted
  order facts, not portable C faults or real hardware trap acceptance.
- **26 public-alias cases / 52 executions** qualify captured records and
  payload while halfword writes overlap actor count/head/pointer fields and
  payload flags. Public fields remain live, captured pointers do not reload.
  Do not claim portable partially aliased structs or arbitrary private frames.
- **53 complete compiled forms / eight samples each**, **46 positive
  forms** and **seven effective negatives**: unsigned active/start/head,
  signed count, cached flags, wrong phase direction and wrong divisor.
  Independent read scheduling in alternative forms is reported separately
  from public memory/return agreement. The signed-count witness must actually
  reach count128's wrap from start126; narrowed fallback stores alone are
  identical for signed and unsigned counts. Every negative changes behavior
  without an unmapped-storage fault being used as evidence.
- Preserve all **10 copied-owner neighbors**, bytes, sizes, relative
  relocations, pools and **zero diagnostics** before/after, including actual
  post-processing of the remaining assembly bodies. The actual padder emits
  **280 bytes without .space or guards**. **Four independent GNU links /
  128 cases** retain all 70 words, moved entries and two SP phases.
- **66,560 actual native32 C cases** cover all **65,536 head/count pairs**,
  all active-byte patterns, reachable signed endpoints and both phase
  directions. Compare complete **256-byte actor / 128-byte payload /
  11,600-byte record** canaries against the independent model. Choose
  terminating native fixtures; invalid long-running cases stay emitted-prefix
  observations, never unbounded native invocations.
- **24 connected cases / 48 executions** run the complete **100 + 97 + 70
  word** timer/payload/leaf chain through both protected table identities.
  Record phase changes, position publication and modeled states agree.
  No external callback or cleanup hook is used in these successful fixtures.
  Failure-to-cleanup and broader upstream/hardware/gameplay remain separate.

All **nine pre-install tests pass in 100.973s**, no skips. Normal incremental
rebuild succeeds in **22.747s**, zero cfe warnings; the existing duplicate
generated_12D630 recipe warning remains. Final post-install **nine tests
pass in 90.033s**, no skips, including the installed C/progress and strict
whole-ELF audit. Fresh **35 shared tests pass in 4.561s** and both tools
checks pass. Retain historical baseline-sensitive target-suite receipts;
do not describe them as fresh reruns.

Documentation validation checks **142 documents / 4,231 relative links /
zero broken**. All **31 mounted/mirrored tool files** parse and have
identical bytes. All **64 pre-existing standalone status lines**, both
independent dirty-file hashes and its HEAD remain preserved.

## Banking And Open Boundaries

Ignored `conker/build/game-record-phase-shaping-test/` holds original baseline,
before ELF/guards/progress, full candidate/native probes, slot/guest/faults/
aliases/forms/owner/linked/native/connected/after/build/final-tests/progress
receipts. Preserve the original before.elf. Candidate-only exploratory
screens live in game-record-phase-shaping/. Commit no ROM, ELF/native
binary, generated probe, progress CSV or save.

Per "Keep commited", tools checkpoint
**741b4055bf8dd9394c3ea64c107d0bf82b7b7787** is committed first; parent
source/docs/gitlink pins that exact revision second. Mirror only the two
absent new tool files. Preserve older standalone HEAD **ddbdd16**, both
independent dirty-file hashes and all **64 pre-existing status lines**;
do not reset it or duplicate its history. No push, pause, dependency/account
change or OGL/Release/runtime/editor work. Root README gets aggregate rows
only. Wider Game completion is not claimed. Zero Claude calls suffice for
this complete directly matching source/ABI case.

Local Graphify query finds no target node. Manual refresh refuses **16,995
nodes** over retained **38,782**, preserving **19,398 nodes from 2,972
excluded files still on disk**. Existing version/zero-node warnings remain.
No force or reinstall; reduced-corpus repair stays open. Check the parent
post-commit hook separately before the final clean-state report.

## Next Work

Recover complete first-stage **func_151488C4**, **D_8008A3E0[1]**, still
GLOBAL_ASM in this owner: VA **0x151488C4..0x15148AF4**, ROM
**0x175D74..0x175FA4**, **140 words / 560 bytes / frame0x10**. Full body
integrates a forward record window with live time/gravity/XYZ loads, appends
actor position and initial vertical velocity, narrows/wraps the stored head,
shapes record halfwords, or changes the live first-stage selector to 2/3.
Preserve captured pointers, live flags/count/cursors and sequential copies.
Analyze the conditional **u16 step at SP+0**: the zero-active path skips
initializing it. Do not invent a default or claim portable behavior from
an uninitialized stack read. Connect the whole callback to the banked
dispatcher. Slot-3 func_15148BA4 and trail constructor func_151DA6F8's
61 differences remain open.
