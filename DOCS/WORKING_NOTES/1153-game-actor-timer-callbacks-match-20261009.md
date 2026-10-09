# Game Actor Timer Callbacks Match

Date: 2026-10-09

## Result

Continue [Note 1152](1152-game-actor-graphics-dispatch-match-20261009.md)
under the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and
zero Claude calls. Restore false-zero `func_15147740` in
[generated_174BF0.c](../../conker/src/game/generated_174BF0.c):
VA **0x15147740..0x151478D0**, ROM **0x174BF0..0x174D80**,
**100 words / 400 bytes / frame0x20**, complete semantic C and linked
byte-exact with **six expected-word private spill-slot guards**. This is
guard-assisted matching, not a direct compiler match. The complete raw body
already matches 94 words; only six SB/LB accesses differ.

Start from clean parent **470d7d94** and mounted tools **7b88702**. Baseline
ELF SHA-256 is the exact Note 1152 artifact:
`7eb984ef2d80b7ffce34bc2eb3d93bddd5357e4fb14c55f732405803931afbf2`.
New ELF SHA-256:
`9882610856cfd36a0022c543d536b8b6817c335a3b74a95ce1c24abaea0e143e`.
All **6,058** function addresses/extents and every other function's bytes
remain unchanged. The complete protected Game-data image and conversion CSV
bytes are unchanged. Preserve all **11,475 old guard rows/bytes**; append
exactly six target rows, for **11,481 total**. Original assembly, layout,
Makefile/profile, headers and shared tools are unchanged.

The broad rebuild also exchanges two absolute-symbol ordering slots. The
byte-level audit accounts for that precise six-byte non-allocated metadata
permutation, not arbitrary symbol-table differences; details below. All
logical symbol records remain unchanged except target size **12 -> 400**.

The placeholder already counted as C, so no converted-function/byte credit.
Fresh totals advance one: **5,484 converted / 3,401 exact (62.02%)**;
Game **4,811 / 2,728 (56.70%)**, Init 492 / 492 and Debugger 181 / 181
exact. Zero address drift and **2,083 different**. The trail constructor
remains **144 words / 61 differences**. Root README aggregate rows only;
the wider Game goal stays open.

## Recovered Contract

Recover the one-argument **void** actor updater. V0 residue depends on helper
calls/last loads; do not invent a public status return. Inspect the complete
[retail routine](../../conker/asm/174BF0.s), not a prefix or only its last call.

- If actor flags u16+0x1E contain bit **1**, subtract the full live
  **D_800BE9E4** word from the signed-halfword timer at +0x1C. Use unsigned
  low-word subtraction, store the low halfword and reload it as signed.
  A negative stored result sets the failure flag. When the bit is clear,
  neither the timer nor the global needs reading.
- Read unsigned selector **+0x2F**. At **15..255**, clean up immediately
  through `func_1516972C`. Otherwise invoke **D_8008A200[selector]** only
  for nonzero selector and no failure. A full-word zero callback result
  sets failure; any nonzero word, including high-bit values, succeeds.
- Reload unsigned selector **+0x30 after the callback**. At **18..255**,
  clean up immediately. Otherwise invoke **D_8008A23C[selector]** only
  for nonzero selector and no failure; zero return sets failure.
- Reload flags +0x1E. Only when bit **0x10** is now set, read signed byte
  **+0x24**. Values below **-1** or at least **8** clean up immediately;
  **-1** is the disabled sentinel. For **0..7**, invoke
  **D_8008A284[selector]** only without failure, and set failure on zero.
- Finally clean up if failure remains. Callback failure/timer expiration
  suppresses later callbacks, **not later selector validation**. There is
  no invented null callback check, selector clamp or early failure return.

Actor, flags, later selectors and callback tables remain live across calls.
The protected tables have **15 / 18 / 8 entries**, **39 nonnull targets**;
only the first two tables' zero entries are disabled. Target incoming data
pointer witnesses are **0x8008BB90 / 0x8008C44C**; no direct J26 caller was
found in the inspected retail assembly. Actual upstream dispatch/callback
bodies are separate acceptance gates.

## Complete Source And Spill Proof

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_actor_timer_callbacks_candidates.py)
screens **44 complete ordinary forms**: selector widths/lifetimes, range
capture order, 24 declaration orders, initialization, timer/flags/result
locals and subtraction shape. Baseline emits **100/0x20/25 differences**;
unsigned selectors plus signed third action reach 19. Separate **u8 first,
u8 second, s8 action** resolve the register cycle and reach six. None of
the remaining ordinary forms resolves those six directly. No phony local,
expanded layout, truncated body, fake filler or profile change is installed.

The only remaining raw differences are word indices **32 / 37 / 55 / 60 /
85 / 90**, offsets **0x80 / 0x94 / 0xDC / 0xF0 / 0x154 / 0x168**.
They save/reload failure as A1 at **SP+0x1F**, versus retail **SP+0x1B**.
Three SB and their three LB reads move as one closed private byte lifetime.
Each expected/replacement word differs only by immediate bit 2. Raw stack
memory accesses use only **+0x14 (RA), +0x20 (actor home), +0x1F (flag)**;
normalized accesses use +0x1B for that flag. There is no conflicting owned
frame access. Frame, branches, registers, calls, relocations and all other
94 words remain untouched. Each stale expected word is rejected.

Profiles: O2g3 **100/6**, O2 **100/6**, O1g3 **115/106**, O1 **115/107**,
all frame0x20. No isolated diagnostics/pools. Four cleanup J26 calls and
four HI/LO pairs (tick plus three tables) retain their symbolic relocations.
Keep the existing O2g3 owner profile.

## Qualification

The [eight-test suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_timer_callbacks_match.py)
reuses the existing signed-byte-capable instruction oracle, native32 harness,
owner compiler, ELF/object/pool parsers and actual generated-slice padder.
Independent three-stage behavior, full call arguments and public memory
supplement raw/normalized/retail stream comparison.

- **9,600 cases / 28,800 executions** cover every byte in all three
  selectors, signed timer boundaries/wrap, full-word ticks/results, pass/fail
  masks, live selector/flag/table mutations and four outgoing homes clobbered.
  All **99 reachable words** execute. Word **76**, a duplicated -1 constant,
  is structurally unreachable; it still emits naturally from complete C and
  matches retail. Raw and normalized public states agree; normalized/retail
  complete register/FP/event/memory states agree at SP phases 0/8.
- **524 missing-public-byte triples** qualify lazy tick/timer/third-selector/
  table access and exact emitted fault prefixes. Private-frame actor aliases,
  portable C fault behavior and hardware traps are not claimed.
- **50 complete compiled forms / eight samples each** include six effective
  negatives: wrong tick operation, first/second bound, third signedness,
  ignored first failure and stale second selector. Every form first completes;
  all 44 ordinary forms satisfy the independent behavior check and all six
  negatives fail it. The initial overlapping fixture tables were corrected
  to their real bounds; that was a fixture issue, not a production repair.
- Preserve **10 copied-owner neighbors**, their bytes, relative relocations,
  pools and the same **seven diagnostics**. Actual padder emits all **400
  bytes** without `.space`; precisely six target guards. **Four independent
  GNU links / 512 cases** exercise moved tick/table addresses, HI/LO carry
  and different J26 regions.
- **721,664 actual native32 C cases** cover all 65,536 timer patterns,
  all 65,536 flag patterns, all three selector bytes, full-word ticks and
  callback results, live mutations and **256-byte actor/canary comparisons**.
  Callback/cleanup implementations remain bounded fixtures, not gameplay.
- **656 cases / 1,968 executions** use all protected retail table identities
  and verify all 39 nonnull targets resolve to linked functions. These execute
  the complete updater with bounded hooks, **not actual callback bodies**
  or upstream dispatch. Both incoming pointer witnesses remain exact.

Pre-install eight tests pass in **49.897s**. The manifest-triggered normal
rebuild succeeds in **257.163s**, with **489 cfe warnings** across rebuilt
owners and the existing duplicate generated_12D630 recipe warning; no claim
that the broad build is warning-free or has a fresh prior warning-count
baseline. Focused owner diagnostics stay at seven. Final post-install
**eight tests pass in 64.224s**, no skips. Fresh **25 shared tooling tests
pass in 0.359s**, and both local tools checks pass. Historical baseline-
sensitive suites are retained, not falsely reported as fresh reruns.

Documentation validation passes across **139 documents / 4,201 relative
links / zero broken**. All **25 mounted/mirrored tooling files** parse and
have identical bytes; this check does not reset the older standalone tree.

## Exact Linked Metadata Audit

Preserve the original before.elf. After accounting for target instructions
and size 12 -> 400, the initial strict byte audit finds **six additional
bytes**, solely in non-allocated **.symtab / .strtab**. D_8008A200 and
D_80089800 exchange adjacent symbol entries and equal-length string slots.
Their names, absolute values, sizes, binding/type, visibility and section
identity are unchanged logically. This is a physical order permutation.

Verify **every logical ELF symbol record** as a multiset after the target
size update. Separately derive the exact two-entry/two-string permutation
from the captured baseline, with expected values, zero sizes, ABS sections,
16-byte entry spacing and 11-byte name-slot spacing checked. Then compare
**every ELF byte** against that precise expected result. No broad metadata
mask or new baseline. All code/data/header/other metadata bytes remain
unchanged outside the target and this explicitly verified permutation.
The old guard CSV bytes are an exact prefix of the six-row append; conversion
CSV bytes and the checksum-verified complete Game-data image are identical.

## Receipts And Banking

Ignored `conker/build/game-actor-timer-callbacks-test/` receipts include
baseline.json, before.elf, before guards/progress, slot.json, guest.json,
faults.json, forms.json, owner.json, native.json, tables.json, linked.json,
after.json, build.log/build.json and unexpected-elf.json. Keep before.elf;
the initial audit-failure receipt documents the six bookkeeping bytes.
Separate candidate screens live in game-actor-timer-callbacks/.

Per "Keep commited", mounted tools
**b3086e20a451aa298c0df9ba6b7af8ccaedaa45e** is committed first; parent
source/guards/docs/gitlink pins that exact revision. Mirror only the two
absent new files with parse/exact-byte checks. Preserve older standalone
HEAD ddbdd16, independent owner-pool/effect-test fingerprints, pre-existing
untracked paths and history. No push, pause, reset or duplicate mirror commit.
Commit no ROMs, ELF/native binaries, generated probes, progress CSV or saves.

Manual Graphify refresh refuses **16,961 nodes** over retained **38,749**,
preserving **19,398 nodes from 2,972 excluded files still on disk**. No force,
dependency/account change or graph-corpus completion claim; the parent hook
is checked separately. No OGL/Release, runtime/save/editor or bridge work.
Zero Claude calls suffice because complete assembly, fitting and independent
tests settle the current source/ABI/private-slot questions.

## Next Work

Follow-up [Note 1154](1154-game-payload-callback-update-match-20261009.md)
converts the complete 97-word `func_15147EB8` from GLOBAL_ASM to C, linked
exact with 25 closed frame/return guards, and connects it to the banked timer
updater. Correct the old description below: this callback was GLOBAL_ASM,
not false-zero. The full linked ELF remains byte-identical. Next recover
44-word first-stage callback `func_15148AF4`; original handoff is historical.

Recover false-zero **func_15147EB8**, the actual first-table slot-1 callback,
in [generated_175250.c](../../conker/src/game/generated_175250.c):
VA **0x15147EB8..0x1514803C**, ROM **0x175368..0x1754EC**,
**97 words / 388 bytes / frame0x30**. It captures the payload pointer,
invokes live payload-selected callbacks, updates the bounded fade byte,
conditionally invokes a failure callback, publishes/zeros three position
words and returns signed-byte success. Qualify the complete routine and
connect it back to this banked timer updater. Alternatively continue the
trail constructor's **61 actual differences**. Already exact 13-word
func_151478F4/func_15147928 are not fresh matching targets. Keep wider
callback/cleanup/upstream/hardware/gameplay and graph corpus gates open.
