# Game Owner Point Arc Workspace And Frame Audit

Date: 2026-10-09

## Target And Checkpoint

Continue func_151B3CF0 after consumer ac15f190 and mounted tools
1f5723501b05767c15efc7dbb29654d7d83ae50c. Both active checkouts started clean.
Keep the complete recovery and actual linked-helper audit in
[Note 1189](1189-game-owner-point-arc-recovery-and-helper-audit-20261009.md).

Retail: VA 0x151B3CF0..0x151B3F28, ROM 0x1E11A0..0x1E13D8,
142 words / 568 bytes, frame 0x88. The production zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) is unchanged.
No installation, guard/profile changes, conversion credit or matching credit.

Single Codex writer, zero Claude calls. Reuse the existing IDO compiler,
binary parser, bounded guest/native32 fixtures and scoped graph query. Do not
modify OGL, Release, saves or editor. Keep commits in tools-first order.

## Private Frame And Register Audit

Read the complete original assembly and actual compiler output, not a guessed
frame diagram. Original private homes and saved-register stores are:

| Value | Original SP Offset |
| --- | --- |
| Saved F20/F21 through F30/F31 pairs | 0x10, 0x18, 0x20, 0x28, 0x30, 0x38 |
| Saved S0, S1, S2, S3, RA | 0x44, 0x48, 0x4C, 0x50, 0x54 |
| Last endpoint offset XYZ | 0x58, 0x5C, 0x60 |
| First endpoint offset XYZ | 0x64, 0x68, 0x6C |
| Midpoint XYZ | 0x70, 0x74, 0x78 |
| Vertical endpoint delta | 0x80 |

Endpoint F26/F28/F30 lifetimes end after the offset-vector stores. Retail
reuses F26/F28 for normalized Z/X, F24 for vertical difference and F30 for
projection across the angle-helper call. F20 becomes angle, F22 radius,
F30 the retained step and F24 the sine result. The loop distinguishes current
record S0 from next cursor S2, byte offset S1 and bound S3. Midpoint fields
are reloaded from private memory; the branch delay advances the angle.

The midpoint-pointer diagnostic retains first.x in F30 and spills projection
at SP+0x58 across the angle call. It saves three rather than four S registers,
starts FP saves at SP+0x18 and places midpoint at SP+0x8C/0x90/0x94. Its
cursor/update schedule also differs. These are measured discrepancies, not
permission to patch stack words or guess a register remap.

## Complete Source Fitting

[Fitting driver](../../tools/experiments/game_owner_points_arc_fitting.py):
39 complete source forms, including actual vector workspaces, midpoint pointer,
endpoint snapshots, current/next cursor variants, local scopes, grouped vectors,
declaration order and real radius/sine lifetime reuse. Volatile workspaces are
diagnostic controls, not recovered original qualifiers. No dummy padding locals,
ROM-derived output words or reduced-function substitutes.

| Complete Form / Profile | Words | Frame Bytes | Word Differences |
| --- | ---: | ---: | ---: |
| Retained compact / O2 g3 | 141 | 208 | 118 |
| First/last explicit workspace / O2 g3 | 141 | 160 | 127 |
| Midpoint pointer / O2 g3 | 147 | 152 | 147 |
| Snapshot + reused radius/sine / O1 g3 | 178 | 136 | 175 |
| Grouped compact workspace / O1 g3 | 194 | 120 | 193 |

The new midpoint-pointer frame is 56 bytes smaller than the retained compact
recovery, but it overflows the retail slot by five words. It does not supersede
the 141-word/118-difference compact baseline. The 136-byte O1 frame coincidence
does not preserve retail's saved-register layout or 142-word body. Reject it.
Smaller-than-retail frames also provide no installation acceptance.

The authoritative test sweep measures all 39 forms at O2 g3 and three selected
forms at all four existing profiles, yielding 48 form/profile combinations.
Each runs eight complete guest fixtures: 384 cases / 768 executions. Every
measured combination has zero compiler diagnostics and zero constant-pool bytes.
None is byte-exact. Separate CLI snapshot/grouped profile screens are exploratory;
do not imply every form passed all four profiles or all special-value fixtures.
Filtered CLI measurements have separate filenames so one screen cannot overwrite
another screen's receipt.

## Fresh Qualification

Command: python3 -m unittest tools.tests.test_game_owner_points_arc_recovery
tools.tests.test_game_owner_points_arc_fitting -v.
Final fresh combined run: all 14 tests pass in 71.805s, zero skips.

Four new tests in
[fitting qualification](../../tools/tests/test_game_owner_points_arc_fitting.py):

- Full source/profile sweep and explicit saved-register signature rejection of
  the 136-byte frame coincidence.
- Midpoint-pointer guest: 2,048 cases / 4,096 executions, all 256 flag bytes,
  both stack phases and every word in the 142-word original/147-word candidate.
  Saved GPR/FP state, actor bytes, canaries and helper argument bits are retained.
- Boundary/callback mutations: 48 cases / 96 executions, including threshold
  equality, tiny values, signed zero, NaN/infinity and retained step mutations.
  Seven compiled negative mutations are effective, not merely compiled.
- Actual midpoint-pointer native32 C: 512 finite cases against full original
  guest results, exact helper order/argument bits and all actor/canary bytes.
- Source/ELF/guards/progress fingerprints remain equal to Note 1189's baseline;
  frame, saved homes, slot overflow and complete-word mismatch reject installation.

The ten prior recovery tests also rerun freshly, including actual registered
81-word update, independent rebases, copied owner/padder, fault prefixes,
protected data and actual linked-helper audit. Those owner/padder and independent
rebase receipts remain for the retained compact candidate, not the overflowing
midpoint-pointer diagnostic. Do not extend their acceptance to the new form.

Helpers remain bounded caller-clobbering contracts; native32 finite checks are
actual compiled C, not original sine/cosine math. No FCSR, hardware exception,
portable C fault, complete public-read-order or live rendering proof is claimed.
Actual linked sinf/cosf remain zero-return placeholders; the angle helper's
entire original 80-word slot remains exact.

## Banked State And Next Step

Fresh make tools-check passes. Fresh matcher: total 3,417/5,489 (62.25%),
Game 2,744/4,816 (56.98%), Init 492/492 and Debugger 181/181 exact;
zero address drift / 2,072 different. Root README aggregates stay unchanged.
No production rebuild is needed for unchanged source/profile/data/guards;
retain Note 1188's build receipt explicitly, without claiming a fresh rebuild.

Tools 7a130987be36abd9c24036f12fa419c328104f00 commits the two new authored
fitting files before consumer documentation/pin. Mirror only those two absent
files to the older standalone checkout. Its HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and 133 pre-existing dirty entries
remain untouched; the two additions yield 135 entries. Preserve both dirty
tracked-file hashes, do not overwrite conflicts, reset, duplicate commits or push.

Fresh scoped documentation audit: 12 documents / 3,941 relative links, zero
broken links. Seven initializer/arc tooling files parse in both checkouts and
match their exact older mirrors; two are this turn's newly authored files.

Fresh graphify update . exits 1, refusing a 39,111-to-17,330 node shrink.
Keep the existing graph and 19,398 nodes from 2,972 out-of-corpus files. Retain
version/zero-node warnings; no force, purge or install.
Ignored receipts: conker/build/game-owner-points-arc-fitting/ and
conker/build/game-owner-points-arc-fitting-test/.

- [x] Audit original private homes, saved-FP lifetimes and current/next cursor.
- [x] Qualify complete fitting forms and explicit frame-coincidence rejection.
- [x] Rerun the retained full recovery suite; preserve production and metrics.
- [x] Commit tools first and bank consumer documentation/pin.
- [ ] Recover original 0x88 frame AND private vector/saved-register homes from
  real C locals. Eliminate projection spill and release first.x's F30 lifetime.
- [ ] Recover current/next cursor and branch-delay angle advance directly;
  fit the complete 142-word body before any allocation/scheduling guards.
- [ ] Install only after full linked owner/ELF/data/guard-history and independent
  relocation proof; recover sine/cosine separately before real rendering acceptance.

The wider Game matching goal remains active.
