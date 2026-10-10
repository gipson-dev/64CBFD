# Game Owner Point Arc Saved And Vector Home Recovery

Date: 2026-10-09

## Baseline And Target

Continue after consumer 82bb9b97 and tools 7a130987be36abd9c24036f12fa419c328104f00.
Both active checkouts started clean. The preceding goal turn made progress by
banking the full workspace/profile audit in
[Note 1190](1190-game-owner-point-arc-workspace-and-frame-audit-20261009.md).

func_151B3CF0: VA 0x151B3CF0..0x151B3F28, ROM 0x1E11A0..0x1E13D8,
142 words / 568 bytes, frame 0x88. The production zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) remains unchanged.
No production installation, guard/profile changes, conversion or matching credit.

Single Codex writer, zero Claude calls. Inspect complete assembly, actual IDO
output and current scoped checkout state; reuse the existing parsers, compiler,
guest/native32 helpers and scoped graph query. Do not touch OGL, Release, saves
or editor. Root README gets aggregate rows only; these are unchanged.

## Recovered Layout

[Lifetime fitting](../../tools/experiments/game_owner_points_arc_lifetimes.py),
SELECTED_NAME = direct-delta-vector, preserves the full semantic recovery.

- Reuse the actor parameter as the current point, keeping a separate advancing
  cursor. This recovers all four saved GPRs instead of the compact body's three.
- Reuse the projection temporary as the later angle-step local, after radius
  consumes the projection. This eliminates the angle-call projection spill.
- Use an actual delta vector before the midpoint workspace, not dummy padding.
  Its X/Z values stay in registers. Remove the separate current-point local.
- Explicit first/last workspaces constrain their real offset-vector storage.
  Their volatile qualifier remains a diagnostic control, not recovered original
  source evidence or a reason by itself to install the function.

| Home | Original And New Diagnostic SP Offsets |
| --- | --- |
| Saved F20/F21 through F30/F31 pairs | 0x10, 0x18, 0x20, 0x28, 0x30, 0x38 |
| Saved S0, S1, S2, S3, RA | 0x44, 0x48, 0x4C, 0x50, 0x54 |
| Last endpoint offset XYZ | 0x58, 0x5C, 0x60 |
| First endpoint offset XYZ | 0x64, 0x68, 0x6C |
| Midpoint XYZ | 0x70, 0x74, 0x78 |

The frame is now 136 bytes, exactly retail 0x88. The complete final memory
image matches retail everywhere outside SP+0x80..0x83 in qualified cases,
including early exits. Original always spills delta Y there; the candidate
keeps it in a register and does not write that home. All nine vector values
and their private-write multisets agree; private-write ordering is not claimed.
This is stronger than a frame-size coincidence, but not full private-frame match.

Measured body: 143 words, 140 raw word differences, zero compiler diagnostics
and zero pool bytes. The actual padder rejects the one-word overflow. Do not
replace the retained 141-word/frame208/118-difference compact diagnostic or
pretend the new raw difference count is lower. The new form closes layout
boundaries; it has not closed scheduling, instruction count or every word.

Fresh bounded read trace: active retail reads each endpoint word once (six
reads); the candidate reads actor+0x14 once and +0x18/0x1C/0x20/0x24/0x28
twice (eleven reads). Five redundant reloads remain. Both early-exit traces
have six reads. Equal final state does not establish public-read-order parity.

## Source Discriminators

114 complete forms pass eight ordinary guest fixtures each: 912 cases / 1,824
executions. Four existing profiles qualify the selected source's public contract;
the original-home claim applies to the selected O2/g3 form, not every profile.

The sweep covers scalar/array/record representations, register-local hints,
current/next cursor lifetime, subset/stage reuse, actual delta workspaces,
endpoint-vector snapshots and statement order. Register hints exclude arrays,
which require addressable C storage. No ROM-derived output or reduced routine.

Useful measured controls:

| Complete Form | Words | Frame Bytes | Word Differences |
| --- | ---: | ---: | ---: |
| Retained compact | 141 | 208 | 118 |
| Reused first/last workspace | 142 | 136 | 133 |
| Stage projection-step + separate cursor | 143 | 128 | 141 |
| Selected actual delta vector | 143 | 136 | 140 |
| Endpoint vectors | 142 | 192 | 117 |

The 142/frame136 first/last form has wrong saved/vector homes and is rejected.
Endpoint vectors slightly reduce raw differences but lose the original frame.
Six counter-first, for-increment and do-condition forms still emit 143/frame136;
they do not recover the retail branch-delay angle advance. Keep them as measured
discriminators, not a source-order promise. Filtered CLI receipts do not overwrite
other families' measurement files.

## Fresh Qualification

Command: python3 -m unittest tools.tests.test_game_owner_points_arc_recovery
tools.tests.test_game_owner_points_arc_fitting tools.tests.test_game_owner_points_arc_lifetimes -v.
Final fresh run: all 25 tests pass in 174.430s, zero skips.

Eleven selected-lifetime tests in
[qualification](../../tools/tests/test_game_owner_points_arc_lifetimes.py):

- Guest: 2,048 cases / 4,096 executions, all 256 flag bytes, both stack phases;
  every 142 original / 143 candidate word reached; saved GPR/FP and actor/canaries.
  Complete final memory agrees except the documented delta-Y home, with equal
  vector homes and private-write multisets.
- Boundary/callback mutations: 48 cases / 96 executions, including signed zero,
  threshold equality/just-above, tiny values, NaN/infinity and retained-step
  mutations. Seven compiled semantic negatives are effective.
- Actual native32 selected C: 512 finite cases against complete original guest
  results, including helper argument bits/order and every actor/canary byte.
- Actual registered callback at 0x8008FAFC: complete original 81-word update,
  18 cases / 36 executions, one argument and success-return ABI.
- Four independently rebased symbol sets / eight links: 32 cases / 64 executions,
  all nine original relocation uses and the selected saved/vector homes retained.
- Actual copied owner: 16 neighbors/pools/relative relocations unchanged,
  isolated and owner target bytes equal, zero diagnostics. Actual padder rejects
  the 143-word target; no accepted padded owner or installed ELF is claimed.
- Six missing-byte faults / 12 executions retain public write/call prefixes;
  two unused-byte cases still succeed. No complete public-read-order claim.
- Two additional compiled layout controls retain the public contract: swapping
  delta/midpoint declaration order retains frame/saved homes but fails private
  homes; the 142/frame136 coincidence fails saved homes. Both gates are effective.
- Source/ELF/guards/progress fingerprints and all 189,088 protected bytes / 720
  owners remain unchanged. Actual trig placeholders/helper audit rerun freshly.

The ten retained recovery and four previous fitting tests also rerun freshly.
The first lifetime run exposed a fixture coupling: patching COMPACT for the
selected native test also changed the sweep seed. Capture RECOVERY_COMPACT
before patching and keep target receipts in their own directory; do not skip
forms or suppress compiler diagnostics to make the sweep pass.

Helper responses are bounded caller-clobbering contracts, not original sine/
cosine implementations. No hardware/FCSR, portable C fault, general stack/input
aliasing, complete read/write order or live rendering acceptance is claimed.

## Banked State And Resume

Fresh make tools-check passes. Fresh matcher: total 3,417/5,489 (62.25%),
Game 2,744/4,816 (56.98%), Init 492/492 and Debugger 181/181 exact;
zero drift / 2,072 different. Production and README aggregates stay unchanged.
No production rebuild is needed for unchanged source/profile/data/guards;
Note 1188's build receipt is explicitly reused, not reported as a fresh build.

Tools b9f09b3fe890afc40d89724dd4b09e97ec3a3286 commits the two authored files
before consumer docs/pin. Mirror only those absent files to the older standalone
checkout. Its HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a, all 135 prior
dirty entries and both tracked dirty-file hashes remain unchanged; two additions
yield 137 entries. No reset, conflicting overwrite, older commit or push.

Fresh scoped documentation audit: 13 documents / 3,950 relative links, zero
broken links. Nine affected initializer/arc tooling files parse in both
checkouts and have exact older mirrors; two are this turn's authored files.

Fresh graphify update . exits 1, refusing 39,120-to-17,339 node shrink. Preserve
the existing graph and 19,398 nodes from 2,972 out-of-corpus files; keep version/
zero-node warnings. No force/purge/install.
Ignored receipts: conker/build/game-owner-points-arc-lifetimes/ and
conker/build/game-owner-points-arc-lifetimes-test/.

- [x] Recover original frame, all saved-register homes and all nine vector homes.
- [x] Eliminate projection spill using real nonoverlapping stage lifetimes.
- [x] Qualify complete bodies, private-memory boundary, actual dispatch/native32/
  rebases/owner/fault controls and effective layout negatives; bank tools first.
- [ ] Emit original SP+0x80 delta-Y store/load from the real delta workspace.
- [ ] Remove the five redundant endpoint reloads without growing the frame or
  abandoning the original saved/vector homes; do not infer fault equivalence.
- [ ] Fit all 142 words, FP allocation and counter/cursor/branch-delay scheduling.
- [ ] Install only after full linked owner/ELF/data/guard-history qualification;
  recover real sine/cosine separately before rendering acceptance.

The wider Game matching goal remains active.
