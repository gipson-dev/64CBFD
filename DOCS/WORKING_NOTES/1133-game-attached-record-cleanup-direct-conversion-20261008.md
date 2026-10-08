# Game Attached-Record Cleanup Direct Conversion

Date: 2026-10-08

## Result

Continue [Note 1132](1132-game-record-velocity-integrator-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
`func_151D77C8` in [generated_204660.c](../../conker/src/game/generated_204660.c)
to complete semantic C. All **26 words / 104 bytes**, **frame 0**, emit
directly byte-exact under the existing IDO5.3 O2/g3 profile. **No guards**,
filler, pools, new globals, data, compiler-profile or Makefile changes.
VA 0x151D77C8..0x151D7830, ROM 0x204C78..0x204CE0.

Replace only the retained directive and local untyped integer declaration
with the complete body and `void func_151D77C8(u8 *owner);`. Preserve
[204660.s](../../conker/asm/204660.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_204660/func_151D77C8.s).
All other owner routines and linked instructions remain unchanged.

## Recovered Contract

- Read the attachment pointer at owner+0x28. If null, do not access attachment,
  flags, timer, nested storage or the stack.
- Reload the attachment and capture its nested pointer at attachment+0x98.
  This captured nested destination is not recomputed from later attachments.
- Clear attachment[0x30], then reload the owner pointer for each of three
  unsigned-16 flag updates at attachment+0x1E: clear bit 1, set bit 3, set bit 0.
- Reload the owner pointer again and store the 16-bit value 20 at +0x1C.
- Clear the captured nested word, then clear the owner's attachment slot last.

The initial gate plus subsequent operations perform six owner-slot reads.
The common non-aliased final flags are `(oldFlags & 0xFFFD) | 9`, but combining
the stores or caching the record loses retail access order and alias behavior.
Character writes can change the owner's pointer representation; flag writes
can redirect subsequent loads in mapped guest cases. Preserve the natural
source's reloads. Adding volatile is unnecessary and adds an instruction.

All four observed direct calls are in the same original owner: three cleanup
branches in func_151D7264 and the func_151D7404 wrapper. None consumes a return
value. The exact void body leaves owner+0x28 in V0 incidentally; that is checked
as emitted register state, **not exposed as a new return API**. A pointer-return
probe emits an extra word. Assembly does not alone prove the historical unused
return type; the typed void interface recovers the observed used contract.

A fault on the very first slot load occurs before V0 initialization. The
fixture therefore asserts the surviving slot address only after successful
completion, while comparing full retail/compiled partial state at faults.
No invalid-return or zero-return scaffold is used to force a match.

## Fitting

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_attached_record_cleanup_candidates.py)
retains 17 measured source forms: eight ordinary semantic forms, eight
effective behavior/order negatives and one unused-return probe.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 26 | 0 | 0 |
| O2 | 26 | 0 | 0 |
| O1/g3 | 36 | 8 | 36 |
| O1 | 36 | 8 | 36 |

Unsigned nested type, register slot, block-local nested pointer, null spelling
and old-style pointer parameters are also directly exact. Signed flags retain
26 words but differ in three signed loads. Volatile slot emits 27 words / 23
differences; pointer-return probe 27 / 4; cached record 20 / 21; combined flags
19 / 16. Preserve the shortest natural complete body and existing profile.
Isolated compilation has zero diagnostics, pools and relocations.

## Qualification

[Eight focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_attached_record_cleanup_match.py)
reuse TriangleOracle, ProgressReference, native32, owner/parser, guard-history
and actual padder helpers. Only target-local reference and aligned-access
checks are added; shared domain engines and historical guard checks are unchanged.

- **66,304 guest cases** cover all 65,536 unsigned flag patterns and old-timer
  patterns, all 256 clear-byte patterns, eight alias layouts, null/non-null
  attachments and two SP phases. The exhaustive flag sweep alternates SP
  phase; it is not claimed as the full flag-by-phase Cartesian product.
  All 26 words are reached. Complete GP/FP/memory/trace matches retail and
  independent reference load/store flow. Sixteen deliberately misaligned
  guest alias cases preserve matching partial fault state.
- **93 required fault-prefix cases** remove bytes from each required public
  access under the alias layouts, or supply a null nested pointer. Two lazy
  null cases map only the owner slot and prove no other access. Alignment and
  mapping checks qualify emitted instructions, not portable C fault behavior
  or N64 CP0 exception metadata.
- **786,432 actual native32 C executions** sweep all flag/timer patterns,
  six layouts and null/non-null attachments through a volatile typed function
  pointer. A separately indexed numeric-pointer reference computes all expected
  writes; every byte in the 512-byte backing arena is compared, including
  untouched canaries. Uses the prepared aligned, no-strict-aliasing native32
  toolchain and its pointer representation, not universal ISO C alias promises.
  Host little-endian byte-pointer mutation is checked on its own valid arena;
  high guest addresses and misaligned guest aliases are not presented as native
  or cross-platform pointer-representation equivalence.
- **17 compiled forms / 1,024 ordinary executions / eight effective negatives**
  expose cached records, combined flag stores, wrong mask/active bit/timer,
  late nested capture, owner-first unlink and omitted nested clear. Negatives
  discriminate final state, partial fault state or observable access order.
  The pointer-return experiment is measured only, not a different installed API.
- Copied complete owners preserve **22 neighbors**, all relative relocations
  and normalized data/rodata pools. Typed prototype preserves the wrapper's
  entire body and all other neighbors. Four existing pointer/integer warnings
  at func_151D7404/func_151D8764 call sites remain identical; none added or hidden.
- Real padder emits exactly 104 bytes, with no filler, target relocations or
  guards. **Six independent links / 768 executions** preserve all retail
  instructions across low/high/carry-boundary entry addresses and alias cases.
- **224 complete actual eight-word func_151D7404 wrapper connections** execute
  the full helper and real caller epilogue with nulls/aliases/two SP phases.
  Check the actual argument, public event order, full raw state agreement,
  preserved stack and incidental V0 value. The larger floating gate caller,
  allocator, hardware and gameplay remain separately unqualified.

Initial fixture corrections were confined to a premature V0 assertion on a
first-load fault and an ignored audit script's copied baseline path/labels.
After corrections, all eight pre-install tests pass in **37.342s**, no skips.
Fresh installed target plus neighboring integrator owner/padder and complete
ring-caller regression: **10 tests pass in 47.235s**, no skips. Ten shared
word-patch/PC16 tests pass in 0.043s. Both tools project checks, CLI help and
syntax checks pass. Previous full suites remain historical receipts, not fresh
claims; unchanged shared-engine checks do not justify broader gameplay claims.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` exits 0. Only this owner
recompiles, then the project relinks and regenerates progress. Report the four
existing owner warnings and duplicate generated_12D630 recipes; this is not a
warning-free build. `match-progress NON_MATCHING=1` also exits 0.

Fresh audit compares `game-record-velocity-test/after.json`:

- All **6,058 function bodies, addresses and extents** unchanged: 6,042 retail
  rows plus 16 overflow symbols. Init/init-data/debugger/game-data unchanged.
- All **720 game-data owners / 189,088 bytes** remain exact. The complete
  cleanup and wrapper slots match retail, not only model outputs.
- All **11,155 guard rows** unchanged, including raw CSV hash; zero new guards.
- Exactly one progress row changes: func_151D77C8, 104 bytes, asm -> c.
- Total converted **5,477 / 6,042 (90.65%)**, bytes 1,933,844 / 2,256,728 (85.69%).
  Game **4,804 / 5,321 (90.28%)**, bytes 1,762,408 / 2,072,880 (85.02%).
- Byte-exact **3,388 / 5,477 (61.86%)** overall and **2,715 / 4,804 (56.52%)**
  Game; 2,089 still different, zero address drift. Init 492/492 and debugger
  181/181 remain exact.

Ignored receipts live in `conker/build/game-attached-record-cleanup-test/`:
slot, guest, faults, native, controls, owner-padder, connected, installed,
audit-baseline, audit-installed, before-progress and new `after.json` baseline.
Root README changes aggregate rows only. Detailed evidence lives here;
current status, update log, working index and roadmap point to this checkpoint.

## Workflow And Next

Baseline source `8ed6e3153504fc2900620a9963446a7a7f977912`, mounted tools
`f36e9aff91515dd4398196b265cc6e84db4cc27c`; both clean on entry. Pre-edit SHA-256:

```text
source: 84d545fec365e9af58daf851e1563ed0c298b5072864267bbbbb34920cdf54c9
reference ASM: 14c690097e848287eb8f9e5f3f1031cfa7c3fd65ebdb31075cdafc30a732fa48
Makefile: d5e4c8459b9bf1ac7485b913f559fe9e0242ec284d76cddf0650c210e2a73466
progress: 8ba5afb628ebe7b844181965b286f51ecd1799a87f7584acb9d16a3505f90500
guard CSV: d20b5a5057b8d3f58d2813799bb5e4be83e3b59772342a7d36a514ca93ded518
prior linked snapshot: aaa09b24d117261653b6028be9a644c52645446bffc703f8ed3de513aad9febb
```

Zero Claude calls; routine matching, used ABI and lifetime settled locally.
No host/runtime/save/editor/bridge/account changes; OGL Release remains frozen.
Authorized banking and final documentation checks are recorded below. Preserve the
older independently dirty standalone tools checkout without reset or duplicate
divergent commits; task fixtures are mirrored byte-identically.

Graph query exits 0 without a node. Refresh exits 1: 16,753 new nodes versus
38,541 existing; it refuses overwrite, preserving 19,398 nodes from 2,972
excluded-but-existing files. No forced overwrite or ignore edits. The commit
hook's background refresh is not evidence of a completed full graph scan.

Next retained target **func_151D7830**, **63 words / 252 bytes**, frame **0x88**:
VA 0x151D7830..0x151D792C, ROM 0x204CE0..0x204DDC. Recover the two position-based
stack packets, eleven supplied func_15147A80 call arguments, allocation-failure gate,
28-byte nested memcpy, captured allocated-record lifetime and owner+0x28
attachment store. A candidate is not yet fitted or behavior-qualified. Keep
the wider Game goal active and full gate-caller/hardware/gameplay work open.

## Banking

Documentation verification: **119 documents / 4,000 relative links / zero
broken links**. All **27 relevant tools files** are byte-identical between
the mounted and older standalone checkouts. Both scoped diff checks pass.

Per "Keep commited", tools **6f18cf1f100b0c5fd2a05f18a007e831ca4085c5** banks
the candidate and eight-test fixture first. The parent source/docs checkpoint
records that exact tools pin. No push, reset, stash, unrelated staging or
duplicate divergent tools commit. The older standalone mirror retains its
independent dirty work. Graph completion and broader Game work remain open.
