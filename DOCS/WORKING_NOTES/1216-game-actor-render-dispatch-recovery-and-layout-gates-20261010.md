# Actor Render-Dispatch Recovery And Layout Gates - 2026-10-10

## Scope And Baseline

Resume [Note 1215](1215-game-actor-distance-tier-updater-byte-match-20261010.md).
Target complete func_1502C974: VA 0x1502C974..0x1502CC34,
ROM 0x59E24..0x5A0E4, 176 words / 704 bytes, frame 0x58.
The Gfx-pointer zero-return placeholder remains in
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
This checkpoint recovers and qualifies the full semantic candidate but does
not install it or credit a byte match. Keep the same full caller as the next
target; do not substitute an easier helper.

Consumer baseline d7a15f4199bcdd782704c14ed5b54121a7b2e2cf; mounted tools
6c5b8a48f5d4aed18c7b92bf2ba385e2731e6927, both initially clean.
Single Codex writer, zero Claude calls. No host/OGL, Release, saves, editor,
push or unrelated changes. Ignored conker/build/game-actor-render-dispatch-test
preserves source/ELF/guards/conversion/rodata baselines before qualification.

Baseline source SHA-256
65bd86e98d3df8536c883351dc4bd9ef98c1ed26372f17fccfc3c80fcce23b70;
ELF d5b9745d2361d77d2a5fb1a7a4a5d974bcf7f2b1104b003b1c02432cd2662e4a;
guards 865adc57371ae97c008f5b7fc394da116684e88272b76eba70052cc5174ea332;
conversion 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24;
rodata 11473e0e167c2b30fc6f458dbd3f717e6e02b3f28afa6cce2d7ba4fd5c82b1d6.
All five remain byte-unchanged in the final qualification.

## Complete Retail Contract

Five incoming arguments are cursor, s32 slot, s32 view, s32 mode and s32 extra.
Retain the original cursor privately for overflow rollback. The original
0x58 frame saves RA at +0x24 and homes the first four arguments at
+0x58/+0x5C/+0x60/+0x64; the fifth remains at +0x68.

D_800C3638 nonzero with D_800C3656 zero calls func_150229E4 on the actor;
zero result returns the incoming cursor. Recompute actor after that callback.
Actor addressing uses the unsigned low-word slot*0x32C product.
Actor byte +0x74 masks view with the MIPS variable-shift low five bits;
an exact bit match skips rendering. Keep the explicit C shift mask rather
than introducing undefined shifts for negative or wide views.

First func_1506196C(actor, view) result zero skips. Negative results do not.
Read the fresh matrix pointer actor +0x1D4 only after this query; NULL skips.
Modes other than 3, 4 and 5 call the banked func_1502C6E8 with signed low
halfword view and unchanged mode as its unused third argument, then capture
actor +0x1C8. Modes 3/4/5 instead call func_150849CC(actor, &tier).
The retail private tier output is +0x54, even though this caller does not
subsequently read that word. Do not discard it during physical qualification.

func_1502D54C(slot, parameters) initializes RGB. The private parameter base is
+0x40; alpha is +0x4C. Read fresh D_800B0DF0 and its signed halfword +0x3E.
Nonzero calls func_1502D630(actor, parameters, view); zero stores alpha 255.
Do not cache the global pointer across the RGB callback.

Query func_1506196C a second time. This query is not interchangeable with the
first. For signed alpha below 255, read actor +0x318; if non-NULL, read owner
word +0x2C. Type 0x100 with full incoming view unequal to actor byte +0x127
forces 255. Other owner types, NULL, equal view, or alpha >=255 do not.

Mode 4 reads fresh unsigned D_800DF7C4 and pointer D_800DF7C0. Multiply alpha
as low-word unsigned bits, reinterpret the product as signed, then arithmetic
shift eight. Signed division would round negative products differently.
Other modes reload actor +0x1D4 after all intervening callbacks.

Call func_1502CCFC(cursor, slot, view, matrix, alpha, parameters, mode, extra).
The retail actor home is +0x2C, retained original cursor +0x34, selected matrix
+0x38. Outgoing stack words +0x10/+0x14/+0x18/+0x1C hold alpha, parameter
pointer, mode and extra.

After render returns, read fresh byte D_800BE9C0, pointer table D_800BE9C8
at that index, and signed D_800BEBA4. Subtract returned cursor minus base as
a wrapping low word, reinterpret signed and arithmetic-shift three.
Strict limit < count rolls back to the retained original cursor; equality
keeps the returned cursor. This does not undo callback writes to commands.
The extra word at VA 0x1502CC20 is unreachable in ordinary control flow.

## Compiler Measurements

[Candidate driver](../../tools/experiments/game_actor_render_dispatch_candidates.py)
measures 38 complete/profile forms, without production changes.
The initial complete semantic O2/g3 body has 162 words / 0x60 frame /
174 isolated-link differences, with saved s0 holding actor.
O2 has 160 / 0x60 / 171; O1/g3 has 183 / 0x50 / 173;
O1 has 183 / 0x50 / 176. All compile without diagnostics or new pools.

Twenty-four declaration orders leave 162 / 0x60, at best 173 differences.
A volatile local actor pointer recovers the exact 0x58 frame and RA home,
but emits 167 words / 144 differences. It uses actor home +0x50,
parameter base +0x3C, tier +0x38 and original cursor +0x54, not retail homes.
This complete form also passes public guest/connected/fault tests, but is not
private-alias or private-fault equivalent. Other isolated type/return/shift
forms do not close the extent. No shared profile or helper changes.

## Fresh Qualification

[Focused recovery suite](../../tools/tests/test_game_actor_render_dispatch_recovery.py):
10 tests pass in 20.258s. Earlier fixture/setup failures are not acceptance.

- 2,160 guest cases compare an independent full semantic reference with retail
  and both complete C forms. Cover endpoint slots, negative/wide views, modes,
  signed alpha boundaries, owner types, all early gates and both stack phases.
  Public memory, callback arguments, parameter values and ordered public
  accesses agree. Private callback pointers are normalized by their semantic
  role, not presented as exact physical addresses.
- 2,228 factor/cursor cases include all 256 factor bytes across eight signed
  alpha boundaries, plus signed pointer-wrap, negative count, equality and
  strict-overflow boundaries. Rollback preserves callback side effects.
- 64 mutation cases distinguish the two alpha queries and fresh matrix, owner,
  configuration pointer, factor, alternate matrix, table index/base and limit.
- 60 connected cases run the complete 176-word original caller against both
  complete C forms. Actual banked alternate selector (19 words), distance
  updater (163 words) and identity leaf (11 words) are verified ELF == ROM and
  executed as real instructions. Other callbacks, including the renderer,
  visibility/alpha/RGB/shading and final update callback, are bounded opaque.
  This is full caller execution with bounded callees, not whole renderer or
  hardware acceptance.
- 1,491,048 native32 cases execute the initial complete C with 26 bounded slots,
  four views, seven modes, eight signed alpha values and all factor bytes,
  plus fresh matrix/post-render rollback mutations. Host callbacks are models,
  not native execution of banked MIPS code.
- Seven fresh effective compiled negatives distinguish public results or
  traces: inverted mask/alpha gates, missing second query, unsigned alpha,
  signed division instead of arithmetic shift, inclusive limit and no rollback.
- 63 verified public fault prefixes / 189 original/two-C executions confirm
  each public gate fired. Private fault order is explicitly not qualified.
  These are emitted guest-order claims, not portable C fault guarantees.
- 64 rebase cases use two additional compiled links with changed global/callee
  symbols and signed-LO16 carries. These qualify semantics, not a byte match.
- All 37 copied-owner neighbor bodies, relative relocations and decoded pools
  are exact. Copied-owner target raw bytes equal the isolated candidate.
  Retain adjacent placeholder bodies and their existing O32 v0 contract in
  the diagnostic copy, using an explicit pointer-result cast at the render
  call. Do not add typed dummy formals that generate new neighboring spills.
- Public cases reach 175/176 retail words, excluding the unreachable move at
  index 171. Saved registers and RA/SP are checked by the reused oracle.

Production source/ELF/guards/conversion/rodata remain unchanged.
Protected .game_data is 189,088 bytes / 720 owners, zero byte/owner differences,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Fresh tools-check passes. Matching totals stay Game 2,757/4,816 (57.25%),
total 3,430/5,489 (62.49%), zero drift / 2,059 different.
Root README aggregate rows therefore require no change.

## Bank And Resume

Bank mounted tools 3dba67b5b35e711b30c2a7badea205a836e9068c first, then
consumer documentation and tools pin, without push. Mirror only two absent
new authored files to the independently dirty older checkout.
Preserve its HEAD ddbdd16 and tracked-dirty fingerprints. Dirty entries rise
from 191 to 193 solely for these mirrors; no reset, older commit or overwrite.

Scoped validator passes: 38 documents / 4,203 relative links, zero broken
links and 65 exact authored-tool mirrors, both copies parsed, with older
HEAD/tracked-dirty fingerprints preserved.
Manual graphify update exits 1, refusing a 39,362 to 17,581-node shrink;
retention keeps 19,398 nodes from 2,972 excluded-but-existing files.
Existing skill/package and zero-node devcontainer warnings remain.
No force, purge, installation or policy change. Verify the new consumer's
detached hook using fresh process/log evidence, not prior hook receipts.

1. Keep full func_1502C974 as the next matching target.
2. Resolve the emitted actor lifetime and private homes: original 0x58 frame,
   actor +0x2C, original cursor +0x34, matrix +0x38, RGB/alpha +0x40/+0x4C,
   tier output +0x54, RA +0x24 and original inbound/outgoing argument homes.
3. Recover the complete 176-word extent and closed instruction/relocation
   schedule. The two currently qualified forms remain 162 and 167 words.
   Do not install by copying unexplained retail words or pad a missing body.
4. Add full private alias/fault-prefix and stale-dependency qualification,
   copied-owner padding, complete connected-call checks and linked-only audit
   before installation or a new matching credit.

Preserve the separate uninstalled curve rejection in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game goal and full hardware/live acceptance remain open.
