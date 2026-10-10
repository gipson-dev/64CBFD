# Game Actor Render-Dispatch Lifetime And Private Counterexamples

Date: 2026-10-10. Continue the same complete func_1502C974, not a smaller
helper. This is a banked layout investigation, not an installed byte match.
Codex is the single writer; zero Claude calls. No push, host build, Release,
runtime save, editor or older-tools commit/reset.

## Target And Baseline

Retail VA 0x1502C974..0x1502CC34, ROM 0x59E24..0x5A0E4:
176 words / 704 bytes, original 0x58 frame and RA +0x24.
Production [owner](../../conker/src/game/generated_58F80.c) remains the
zero-return placeholder. The complete semantic recovery and bounded callback
contracts are retained in [Note 1216](1216-game-actor-render-dispatch-recovery-and-layout-gates-20261010.md).

Original private homes: actor +0x2C, original cursor +0x34, matrix +0x38,
RGB/alpha parameter base +0x40 / alpha +0x4C, tier output +0x54.
Incoming arguments start +0x58; outgoing arguments occupy +0x10..+0x1C.
The retail word at VA 0x1502CC20 remains unreachable in ordinary control flow.

## New Measurements

[Layout/lifetime driver](../../tools/experiments/game_actor_render_dispatch_layout.py)
and [focused suite](../../tools/tests/test_game_actor_render_dispatch_layout.py)
compile 31 complete source forms under O2/g3 and O1/g3: 62 emitted bodies.
All retain explicit view masking, five incoming/eight renderer arguments,
two alpha queries, full callback order and strict signed cursor rollback.
No shared compiler profile changes, copied retail-word recipe or new pools.

| O2/g3 form | Words | Frame | Isolated-link word differences |
| --- | ---: | ---: | ---: |
| Initial complete C | 162 | 0x60 | 174 |
| Explicit overflow flag | 175 | 0x60 | 154 |
| Ternary overflow flag | 177 | 0x60 | 154 |
| Scoped overflow flag | 176 | 0x60 | 151 |
| Nested render / volatile actor | 166 | 0x58 | 142 |
| Retail | 176 | 0x58 | 0 |

An explicit overflow flag recovers actor in a3, with a3 spilled across calls,
without making the actor local volatile. It retains RA +0x24 but uses actor
+0x30, original cursor +0x5C, matrix +0x54, parameters +0x44, alpha +0x50,
tier +0x40 and incoming arguments +0x60. These are not retail private homes.
The ternary form recovers the explicit zero/one result construction;
the scoped form reaches 176 words but keeps the wrong frame and homes.
Declaration order and variable renaming do not repair these gates.

The redundant emitted view AND and ensuing register/schedule differences
remain open. Do not remove the portable C mask simply to gain a word.
Inspection of the retained shading callback confirms its parameter alpha
write at +0xC; there is no evidence here for inventing a fifth parameter or
dummy stack padding as a matching fix.

## Fresh Qualification

- New suite: four tests pass in 77.533s. Earlier fault-probe setup failures
  and partial runs are not acceptance. The probe uses a distinct method name
  to preserve the inherited oracle's own gate.
- 312 reference/retail cases and 19,344 compiled candidate executions.
  All 31 O2/g3 bodies agree on public memory, return value, callback values
  and ordered public accesses. Cover endpoint slots, negative/wide views,
  modes, signed alpha boundaries, owner override, early gates and two stack
  phases. Callback parameter/tier pointer addresses are normalized by role.
- All 31 O1/g3 bodies have 20 public trace mismatches each: in the observed
  wide-view path, the narrow helper argument is passed as full 0x12340002
  rather than retail's sign-extended halfword 2. Record these emitted ABI
  differences; do not normalize them away or promote these candidates.
  This does not claim a connected callee necessarily returns a wrong value.
- Three complete closer forms (explicit, ternary, scoped flag) each pass
  1,491,048 actual native32 cases: 4,473,144 executions in total. The reused
  fixture exercises all 256 factors, signed alpha boundaries, callback
  mutation and rollback. Native callbacks remain bounded models.
- Four closer forms expose actual callback pointer homes different from
  retail. Eight private-access fault ordinals per form execute both original
  and candidate: 64 verified fault executions, every requested gate fired.
  Their blocked-address sequences differ. This is an explicit counterexample
  to exact private fault/address parity, not full private-alias qualification.
- Original recovery suite rerun: ten tests pass in 21.697s. Its original
  baseline/volatile candidates retain full public gates, effective negatives,
  rebases and real banked selector/distance/identity connections. All 37
  copied-owner neighbors, relocations and pools still agree. These owner and
  connected receipts do not newly qualify every layout candidate.
- Production source, ELF, guard CSV, conversion CSV and retained rodata
  fingerprints remain unchanged. Protected .game_data stays exact:
  189,088 bytes / 720 owners, SHA-256
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
  No production build or installation was needed for this candidate checkpoint.
- Fresh tools-check passes. Matching stays Game 2,757/4,816 (57.25%),
  total 3,430/5,489 (62.49%), zero drift / 2,059 different.
  Root README aggregate rows therefore remain unchanged.

## Bank And Resume

Bank tools 2b91082 first, then consumer documentation and tools pin, no push.
Only two absent authored files are mirrored to the separate older tools
checkout. Preserve HEAD ddbdd16 and both tracked-dirty fingerprints; its
dirty entries rise from 193 to 195 solely for these absent-only mirrors.
Historical candidate/baseline receipts stay separate from the new
ignored conker/build/game-actor-render-dispatch-layout-test outputs.

Native graphify update exits 1, refusing a 39,371 to 17,590-node shrink.
Retention preserves 19,398 nodes from 2,972 excluded-but-existing files.
Existing version and zero-node devcontainer warnings remain; no force,
purge, installation or policy change. Verify the fresh consumer hook's
workers and log tail after commit; prior hook receipts are not fresh evidence.

Scoped validator passes: 39 documents / 4,213 relative links, zero broken
links, 67 exact authored-tool mirrors parsed in both copies, and preserved
older HEAD/tracked-dirty fingerprints. Fresh match-progress confirms the
unchanged counts above; the known duplicate generated_12D630 recipe warning
remains. This is not a warning-free full-build claim.

1. Continue full func_1502C974 using the nonvolatile overflow-flag lifetime
   evidence. The closest length is now 176, but the private homes remain wrong.
2. Recover original 0x58 frame, all private/incoming/outgoing homes, masked
   shift handling and final result/rollback branches as one complete body.
3. Qualify closed instruction/relocation guards, stale-dependency rejection,
   full private aliases/fault prefixes, copied-owner padding and complete
   connections before installing or awarding a match.
4. Perform the whole linked-only target-slot/data/progress audit after any
   eventual installation. Preserve the separate curve rejection gates in
   [Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).

The wider Game goal and hardware/live acceptance remain open.
