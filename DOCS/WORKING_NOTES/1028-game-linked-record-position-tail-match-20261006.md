# Game Linked Record Position Tail Match

Date: 2026-10-06. Starting checkpoint: `9db7974c`.

Handoff correction: [Note 1029](1029-game-float-reference-packet-wrapper-direct-match-20261006.md)
verifies that `func_15134908` already has semantic C and matches all 50 retail
words. The original placeholder classification near the end of this note was
incorrect; no callee conversion is needed. The wrapper is now matched there.

**Game func_150E6FAC is now linked byte-exact across all 72 words / 288 bytes.**
Slot: 0x150E6FAC..0x150E70CC, ROM 0x11445C..0x11457C, frame 0x38.
The semantic C body in
[generated_113D60.c](../../conker/src/game/generated_113D60.c) is unchanged.
It still emits 71 words with 15 aligned differences before normalization.
This is a **guarded control-layout match**, not a direct raw-C match.

## Closed Tail Proof

[Note 920](920-game-linked-record-position-stack-and-float-shape-20261004.md)
already recovered all calculation, call, register and private-home words.
It correctly rejected a blind replacement of the 15 differing positions.
This pass instead proves a two-instruction permutation plus one inserted
saved-RA load, using the existing fail-closed padding tool.

Three rows in
[retail_word_patches.us.csv](../../conker/retail_word_patches.us.csv) bind the
original compact offsets and explicitly empty relocations:

| Compact Offset | Expected | Replacement | Insert After |
| --- | --- | --- | --- |
| +0x28 | 0x50400032 | 0x50400033 | None |
| +0xE8 | 0x10000007 | 0xE6320008 | None |
| +0xEC | 0xE6320008 | 0x10000008 | 0x8FBF001C |

- Move the final coordinate store out of the success branch's delay slot.
- Emit the retail success branch to the shared S0 restore, with the duplicated
  load of saved RA from SP+0x1C in its delay slot.
- The fallback retains its original saved-RA load. All compact words from
  index 60 onward are unchanged and shift by exactly one output word.
- Adjust the opening branch-likely displacement by one so it still targets
  the fallback store, with the original actor-X load in its delay slot.

No arithmetic, helper-call target, argument, constant, register assignment,
private home, frame or external store is replaced. The 71-word compact body
plus the single inserted word fills the original 72-word slot exactly.
No omission, overflow, profile change, assembly restoration or source padding.

The proof binds words 0..9 and 11..57 directly to retail, the complete
unchanged suffix to retail words 61..71, and the three-word expanded success
tail to its original store and existing saved-RA load. It does not treat
the aligned 15-word difference as 15 independent scheduling instructions.

## Source And Backend Controls

[Tail driver](../../tools/experiments/game_linked_record_tail_candidates.py)
freezes the prior source. Four source forms (control and final-store volatile
casts on either/both paths) run under four profiles: standard, `-Wc,-notailopt`,
`-Wb,-nopeep`, and both options. **Sixteen controls**, empty diagnostics.

All standard/no-tail forms emit the unchanged 71-word / 15-difference body.
No-peep forms emit 74 words / 52 differences and are oversized, uninstalled.
Neither volatile stores nor these backend flags explains a direct retail
tail. Earlier explicit-return/goto and O1/O2 controls remain rejected in
the [original exit driver](../../tools/experiments/compile_game_linked_record_exits.py).
Receipts: ignored `conker/build/game-linked-record-tail/measurements.json`.

## Qualification

[Tail tests](../../tools/tests/test_game_linked_record_tail_match.py) compare
retail, raw C and normalized instructions with an independent float32
reference across **3360 guest cases**, both stack phases. Cases cover failed
and positive/negative successful lookup results, seven RNG words, five finite
fractions, callback mutations at each of the five call boundaries, and four
output placements including actor, record and node overlap. They compare
all non-stack bytes, ordered external reads/output writes and call arguments;
the guest runner checks saved GPR/FPR/SP/RA state at return.

Coverage is **71/72 retail words**. Word 61 (0x150E70A0, actor-X load) is
structurally unreachable: the taken opening likely branch loads X in its
delay slot and targets word 62; the success branch targets word 68. This is
an explained unreachable instruction, not an untested reachable branch.

Stale words and unexpected relocations at each anchor fail in the actual
padding tool. The emitted assembly is assembled and linked independently,
then compared with all 72 retail words. Every incomplete transformation has
a control-flow/output or ordered-read counterexample; missing the +0x28
adjustment adds an extra actor-X read even where output values stay equal.
Production tests bind all three CSV rows and the complete linked slot.

Five pre-install checks pass in **5.904 seconds**, no skips, before touching
the production CSV. The thirteen original linked-record/random-range/sound
tests also pass. All **84 combined post-link tests pass in 267.948 seconds**,
no skips: six tail tests, thirteen linked-record/random-range/sound tests,
three scope tests and the preceding 62 edge/root/parent/visitor regressions.
No shared oracle change. Full gameplay, connected lookup/RNG/trig behavior,
FCSR/exception modes and exceptional floating-point payload acceptance are
not newly qualified by the bounded callback models.

## Linked Audit

The before receipt equals the preceding **6059-slot** checkpoint. After the
shared-CSV rebuild, all names, addresses and lengths survive. **Only
func_150E6FAC changes**; all other 6058 slots, including the 102-difference
edge helper and exact root lookup, are byte-for-byte unchanged.

Target SHA-256:
`f287e0a23ba9d4eb9d687aecb11609a28ae18b59f19cddea18b5f0e8f09540ce`.
Ignored before/after/audit and behavioral receipts live under
`conker/build/game-linked-record-tail-test/`.

Init 164048 bytes, Init data 17376 bytes, Debugger 19800 bytes and Game data
189088 bytes remain unchanged. Fresh Game-data audit checks all **720 owners**:
zero differing bytes/owners, retail-exact. All **10643** old guard rows remain
identical and ordered; only the three new rows are added, for **10646** total.
Build/progress/match-progress pass; the existing duplicate generated_12D630
recipe warning remains. No sibling source/build/save/frozen Release change.

Project tool and whitespace checks pass. **3067 relative links across eleven
documents** pass, zero broken links. No generated build/screen output is
committed.

Fresh counts: total **3310/5462 exact (60.60%)**, Game **2637/4789 (55.06%)**,
Init **492/492**, Debugger **181/181**, zero drift, **2152** different Game C.
Converted function/byte totals do not change. README receives aggregate rows
only; detailed updates stay in documentation.

## Reproduction And Next

```sh
python3 -m tools.experiments.game_linked_record_tail_candidates
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_linked_record_tail_match tools.tests.test_game_linked_record_position tools.tests.test_game_random_range_position tools.tests.test_game_object_position_sound_adapter -v -f
make tools-check
git diff --check
```

Wait for relinking before linked-image tests. Next ordinary Game candidate:
**func_150C2804**, 37 retail words, currently a zero-return placeholder with
36 differences in [game_EF410.c](../../conker/src/game_EF410.c). Its retail
body constructs a stack packet and dispatches it to `func_15134908`; recover
the six-argument ABI, packet field widths and two float data anchors before
matching or claiming its meaning. No conversion installed in this pass.

The callee's [retail assembly](../../conker/asm/nonmatchings/game_161520/func_15134908.s)
confirms a pointer/null return, ORs bit 1 into input packet byte +0x16 and
copies all 28 packet bytes. On success its first three copied words are used
as pointers to floats. The later live source/ELF audit in Note 1029 confirms
that its C body already implements this behavior and is exact across all 50
words. Qualify the wrapper's opaque-callback contract and bounded connected
effect separately from full allocator/gameplay acceptance.
Use `func_15136A50`'s existing packet shape as a local layout reference, not
as proof of correct field names or argument types.

Keep handwritten `func_150A76F0` in its separate register-contract/assembly
lane. The edge helper's 102-difference frame/lifetime boundary remains open
in [Note 1027](1027-game-graph-edge-crossing-scope-audit-20261006.md).
The full Game matching goal remains active. No push.
