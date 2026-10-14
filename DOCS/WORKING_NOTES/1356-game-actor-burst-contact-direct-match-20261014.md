# Game Actor Burst Contact Direct Match

Verified locally: 2026-10-14. Continue the Game matching goal from
[Note 1355](1355-game-actor-burst-consumer-guarded-match-20261014.md).
This is a retail guest-code match, not complete host gameplay or hardware
floating-point acceptance. Preserve unrelated work and frozen host Release.

## Target And Banked Inputs

- `func_151A743C`, owner `conker/src/game/generated_1D43B0.c`.
- VA `0x151A743C..0x151A7610`, ROM `0x1D48EC..0x1D4AC0`.
- Complete 117-word / 468-byte slot, frame `0x48`, existing O2/g3/MIPS2 profile.
- Starting consumer `7d636c72`, tools `eb93e2e`; active trees initially clean
  except the resumed, untracked contact experiment.
- Tools `bb793d8a452b512c84a09fded97767dd64acdcda` committed first.
- Before ELF `b2c092d4e31f04377ebc5c05314803c8aed6e75233b93b58e30447187139c499`.
- Installed ELF `205c023e2ffa29a90d7204bb8eb260989590a4ea30f268e916cd252f88d21708`.
- Installed owner `32c9ac5a400ecb34d0dbd63de6809ca57dfc4dfa29d2ba971c6b156b5994bf8a`.

Before snapshots and generated receipts live in
`conker/build/game-actor-burst-contact-match-test/`. Reuse the existing
`BurstExtra1D43B0` payload and RNG declaration. Add only the typed release and
12-argument effect declarations and replace this function's zero-return body.
No assembly, layout, Makefile, shared header or guard edits are needed.

## Recovered Behavior

Update field `3C` from field `10` plus the incoming fifth float. If the animation
pointer at `174` is nonzero, reread it for release and clear the original payload
pointer after the callback. Compare payload threshold `170` with field `48`.

On the ordered-less path, keep four distinct flag clears at `60`, zero fields
`44/48/4C`, and clamp the signed duration at `64` only when greater than 32.
Payload byte `178` gates the optional effect. Snapshot byte `179` as boolean
before RNG; use unsigned remainder to choose count 2..4. Read field `18` and
both signed payload shorts after RNG, retaining callback feedback.

The effect receives two floats in F12/F14, context in A2, `35 * field18` bits
in A3, and eight stack arguments: count, field18, its half, field18, its half,
two sign-extended shorts, and the snapshotted boolean. The false/unordered path
damps six fields by `14`, with NEG.S preceding multiplication for field `48`.
Every path returns one. Avoid speculative names for fields `10/14/18`.

The unused third argument's source type is not observable beyond its saved raw
word. The real table dispatcher also supplies an unused sixth pointer; the
five-formal callback does not access it. No assertion of its original C type
or of a reconstructed complete effect helper is made.

## Source Matching

Initial semantic C emits 114 words/frame `58` with 77 differences. Recovering
the explicit byte-flag branch yields 117 words/frame `50`, 18 differences.
Removing the unnecessary named velocity/value temporaries restores frame `48`
and leaves one multiply operand-order difference at compact offset `18C`.
Writing the damping expression as factor times negated field value makes all
117 words exact directly from C. No word guards, padding insertions, profile
change, invented volatile access, inline assembly or broad normalizer is used.

The one-word uncommuted source remains an effective compiler shape control.
Both actual padders preserve exact extent and all three external JAL
relocations. Independently assembled original code and both padded objects
agree at the retail address and three rebased entries.

## Verified Gates

Pre-install qualification passes **9 checks in 20.255s**. The installed contact,
consumer match/recovery, producer and complete protected-text suites pass
**67 checks in 234.138s**. Both project-tool smoke copies and Windows
byte-compilation of the five affected tool modules also pass.

- **7,680 guest domains** cover threshold relations, quiet-NaN threshold
  comparison, signed duration boundaries, animation/effect gates, boolean
  variants, high-bit RNG words, callback mutations and two SP phases.
- Independent external-memory/callback reference and complete modeled
  memory/GPR/FPR/HI/LO states agree. Saved F20..F31 and return/SP survive calls.
  All 116 reachable words execute; the unreachable duplicate load at
  `151A75B0` is retained as the 117th exact word, not called covered.
- **680 fired root-access pairs** preserve complete prefixes, instruction PC
  and modeled branch-delay state. **64 fired alias prefixes** include three
  private actor aliases. Callback observations are excluded from root cuts.
- **1,920 native32 cases per O2/O0 profile** check initialized actor fields and
  every callback argument bit. A signed-remainder source control fails the
  trace check with high-bit RNG input, proving the unsigned gate is effective.
- Six freshly compiled semantic controls fail; merged flag stores fail the
  intermediate write-trace comparison. Whole-image target/neighbor/table/
  symbol/source/raw-guard corruption controls remain effective.
- Both complete owner padders preserve six neighbors, their relative
  relocations, pools and warning statements, including the 315-word consumer
  and its ten existing scheduling guards.
- Eight real `func_15132DDC` continuation-window cases use table
  `D_80089934[4]` at VA `80089944` / ROM `22E404`. Execute original instructions
  `15132FE0..15133010`, the actual callback, then stop at the fired continuation
  gate at `15133014`. The fifth float and unused sixth pointer match the ABI.
  Earlier dispatcher speed computation is outside this bounded window.

RNG/release/effect systems remain bounded hooks. Quiet NaNs are qualified only
as comparison thresholds, not arithmetic payloads. Native private-home aliases,
hardware FCSR/rounding, hardware EPC/BD and complete gameplay are not claimed.

## Closed Linked Image

The entire 3,261,160-byte ELF differs in exactly **358 bytes**: **356 instruction
bytes** and **two function-size bytes**, from 12 to 468. There are no symbol
record/string permutations or metadata exclusions. Every undeclared byte stays
fixed. The first audit was started while linkage was still running and failed;
after awaiting build completion, the independent expected image equals the
completed ELF with zero undeclared bytes. Only completed-build receipts count.

Protected data remains exact: 189,088 bytes / 720 owners, zero differing bytes
or owners. Guard SHA-256 stays
`8d23395466ed5dcdb44292506471c06d9af3c7459820d75a6090be4f7ab3c8b9`;
conversion CSV stays
`14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b`.
The producer/consumer and protected-text audits retain their original pinned
snapshots and apply only this asserted slot/size transform. No baseline reset
or disabled corruption check is used.

## Banking And Next Work

Fresh Game **2,834/4,823 (58.76%)**, total **3,507/5,496 (63.81%)**,
still different **1,989**, drift **0**. Init 492/492 and Debugger 181/181 remain
exact. Converted totals do not change. Root README changes only aggregate rows.

The older mirror stays at `ddbdd16`. Verify all 462 starting fingerprints;
copy only the five owned tool modules. Three prior modules change and two are
added, leaving all 459 unrelated fingerprints fixed and 464 dirty paths.
Preserve its independent history. No push, dependency installation, REA
configuration change or host Release build/launch occurs.

Next recover `func_151A7610` in the same owner: VA `151A7610..151A77C0`,
ROM `1D4AC0..1D4C70`, 108 words/frame `98`. It remains a zero-return placeholder.
Keep the completed consumer and contact callback exact while investigating its
randomized effect packet. The wider Game matching goal remains active.

```sh
python3 -m unittest tools.tests.test_game_actor_burst_contact_match -v
python3 -m unittest tools.tests.test_game_actor_burst_consumer_match -v
python3 -m unittest tools.tests.test_game_actor_burst_packet_match -v
```

## Post-Bank And Cross-Project Verification

Consumer `a39ab592` banks the installation and tools pin. Seven fresh post-bank
checks pass **10.729s**: both actual padders/rebased links, contact image and
corruptions, consumer image/serialization, producer image and protected-text
corruptions. The active consumer and tools trees are clean after that commit.

The full graph update refuses an 18,903-node replacement of the 40,670-node
corpus; do not force it. The incremental commit hook finishes **40,680 nodes /
81,158 edges**, preserving 19,398 nodes from 2,972 excluded but present files.
No graph worker remains. Tools are a submodule and this root graph does not
establish coverage of the new tools modules; their direct tests are the proof.

Read-only sibling audit: `64CBFDOGL/recomp_out/.c:1240341` still defines
`func_151A743C` as a zero-return placeholder. Its CMakeLists selects that
generated translation unit. Both files are independently dirty; leave them
unchanged. Transfer/regenerate the callback only in a separate PC-port task
after reviewing that local work, then qualify applicable host behavior. No
automatic cross-project synchronization or PC gameplay repair is claimed here.
