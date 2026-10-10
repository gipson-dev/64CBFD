# Game Owner Point Arc Recovery And Helper Audit

Date: 2026-10-09

## Target And Baseline

Continue the Game matching goal after consumer 4bdbae69 and mounted tools
94a6a0bf42bf3388ce2cb6c0233c657140c25b0c. Previous turn banked the complete
point initializer; this turn recovers its adjacent arc-preparation callback.

func_151B3CF0: VA 0x151B3CF0..0x151B3F28, ROM 0x1E11A0..0x1E13D8,
142 words / 568 bytes, frame 0x88. Production remains the zero-return placeholder
in [generated_1E0560.c](../../conker/src/game/generated_1E0560.c).
Do not install the candidate or award matching/conversion credit.

Fresh scoped checkout state was clean except this turn's two new tools files.
Use the existing single-writer workflow, compiler/parser/native32/guest helpers;
zero Claude calls. Query Graphify for the target and angle helper before the
complete assembly/source/caller audit. Do not change OGL, Release, saves or editor.

## Complete Recovered Contract

COMPACT in tools/experiments/game_owner_points_arc_candidates.py is the full
semantic body, not a reduced renderer or a retail word lookup.

- Snapshot endpoint coordinates at actor+0x14 and actor+0x20; compute ordered
  binary32 differences.
- Return 1 without helpers or output writes unless X or Z separation exceeds
  D_800AA3A0 after absolute value. Preserve unordered comparison behavior.
- Compute midpoint, both endpoint offsets and reciprocal horizontal magnitude.
  Preserve ordered products/additions in the projected endpoint difference.
- Call func_150484A0(vertical difference, projected difference), using F12/F14
  in that order. The helper is not blindly replaced with host atan2.
- Radius is half the binary32 magnitude of projected/vertical differences.
  Load angle bias D_800AA3A4 and angle step D_800AA3A8 after the angle helper.
- Invoke sinf then cosf for each of ten records; advance angle even after the
  last position store. Retain the step through subsequent callbacks.
- Write only each position vector at actor+0x48 + index*24; leave second vectors,
  flags, headers and canaries unchanged unless an explicit test callback mutates them.
- Preserve one-argument callback ABI, success return and saved GPR/FP state.

Measured retail global bits: threshold 0x38D1B717, bias 0x40490FDB,
step 0x3EB2B8C3. Keep the exact values, independent global reads and expression
order; do not substitute a decimal approximation or interpolate final endpoints.

## Source Fitting Evidence

Thirteen complete source forms and four compact compiler-profile controls are
qualified; the source-form ordinary gate has eight fixtures per form.
No compiler diagnostics or constant-pool bytes in the measured forms.

| Complete Form | Words | Frame Bytes | Word Differences |
| --- | ---: | ---: | ---: |
| Compact selected recovery | 141 | 208 | 118 |
| Initial indexed recovery | 145 | 232 | 143 |
| Initial pointer walk | 142 | 232 | 130 |
| Compact early horizontal normalization | 138 | 152 | 137 |
| Typed owner | 141 | 208 | 118 |
| Typed reused normal | 141 | 200 | 125 |
| Typed interleaved endpoint offsets | 140 | 208 | 133 |

The early-normalization variant changes the arithmetic schedule; it is a
discriminator, not proof of FCSR/exception-order equivalence.
A word-count fit alone is not installation acceptance. Selected C has frame
0xD0 rather than retail 0x88, and 118 word differences remain. Actual owner
padder fits the 568-byte slot with a 564-byte candidate symbol plus four zero
padding bytes. Reject installation for the frame/private-home/full-word mismatch.
No guards, frame patches, unused padding locals or broad conversion batch.

## Fresh Qualification

Command: python3 -m unittest tools.tests.test_game_owner_points_arc_recovery -v.
Final fresh run: all ten tests pass in 26.746s, zero skips.

- Guest: 2,048 cases / 4,096 executions, all 256 flag bytes, both stack phases,
  complete 142 original / 141 candidate words reached; saved GPR/FP restored.
- Boundary/callback mutations: 48 cases / 96 executions, threshold equality/
  just-above, signed zero, tiny values, NaN/infinity and large finite inputs.
- Seven effective compiled negatives: return, count, angle increment, stale
  step reload, angle arguments, threshold comparison and coordinate normal.
- Native32 actual compact C: 512 finite cases against complete original guest
  results; helper argument bits/order, complete actor and canary bytes.
- Registered D_8008FAF8[1] at 0x8008FAFC: original pointer and complete 81-word
  update; 18 cases / 36 executions preserve actual one-argument success ABI.
- Four independent symbol sets / eight links: 32 cases / 64 executions,
  original relocation-use multiset preserved; semantic, not byte-exact.
- Actual copied owner: 16 neighbors/pools/relative relocations unchanged,
  zero diagnostics; actual padder preserves every byte outside the target slot.
- Six missing-byte faults / 12 executions preserve public write/call prefixes;
  two missing unused bytes / four executions still return normally.
- Production source/ELF/guards/progress fingerprints unchanged and all 189,088
  protected data bytes / 720 owners remain exact.

Fix fixture issues rather than weaken gates: preserve NaN propagation in the
local sqrt model; compare unchanged early-exit native bytes without interpreting
them in the opposite byte order; compare unlinked owner against unlinked isolated
object; distinguish candidate symbol size from the padded retail slot.
Do not assume symbol size proves linked slot matching.

The guest helper responses are explicit bounded contracts with caller-saved
register/FP clobbers and callback mutations, not original math bodies.
Native helper fixtures use the same response contract but actual compiled C.
No FCSR, portable C fault, complete public-read-order, real trigonometric or live
rendering acceptance is claimed.

## Actual Linked Helper Boundary

| Helper | Symbol Bytes | Retail Slot Words | Linked Word Differences |
| --- | ---: | ---: | ---: |
| cosf | 20 | 88 | 77 |
| sinf | 20 | 104 | 93 |
| func_150484A0 | 316 | 80 | 0 |

The actual linked sinf/cosf first five words are store-argument, MTC1 zero to
F0, NOP, JR RA, NOP. Eight complete executions include finite/NaN arguments
and return zero. Their C sources are also zero-return placeholders.
The angle helper's entire 80-word slot is exact despite its shorter symbol size.
This is measured current ELF evidence, not an inference from source labels.
No helper source is changed this turn; real sine/cosine recovery remains open.

## Checkpoint And Next Boundary

Production fingerprint baseline:
source d3b46d32585f6b4a643388dbb7d6ff4d92a3b8c56d7c5c05a48c1b02dd489fe6,
ELF a3619d2acd1642392048d0b7b6a79dabc8b4c6ade388ea8ca116841272b5a479,
guards 6fb0dc9d296edc12a78000c2cd96734f4df724ffd4836d41e244ef9b231a124b,
progress 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.

Fresh make tools-check passes. No production rebuild is needed for unchanged
source/profile/data/guards; Note 1188's full build receipt is reused explicitly.
Fresh matcher: total 3,417/5,489 (62.25%), Game 2,744/4,816 (56.98%),
Init 492/492 and Debugger 181/181 exact, zero drift / 2,072 different.
Root README aggregates stay unchanged; do not add a recovery narrative there.

Tools 1f5723501b05767c15efc7dbb29654d7d83ae50c commits the two authored files
before consumer documentation/pin. Older standalone HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a, all 131 pre-existing dirty entries
and both tracked dirty-file hashes remain unchanged. Mirror only two absent
authored files, yielding 133 entries; no older commit/reset/push. No push requested.

Fresh scoped documentation check: eleven documents / 3,932 relative links,
zero broken links. Five initializer/arc tooling files parse in both checkouts
and match their exact mounted/older mirrors; the two new arc files are this
turn's authored tooling changes, not a broad unchanged-suite claim.

Final explicit graphify update . exits 1, refusing 39,101-to-17,320 node shrink.
Preserve 19,398 nodes from 2,972 existing out-of-corpus files and existing graph;
retain version/zero-node warnings, no force/purge/install.
Ignored receipts: conker/build/game-owner-points-arc/ and
conker/build/game-owner-points-arc-test/.

- [x] Recover complete threshold/midpoint/normalization/angle/ten-point contract.
- [x] Qualify complete bodies, actual dispatch, native32, mutation/fault controls,
  independent links, owner/padder and unchanged production.
- [x] Measure actual helper gap and bank tools before consumer docs/pin.
- [ ] Fit func_151B3CF0's original 0x88 frame, private vector homes, saved-FP
  reuse and complete 142-word schedule directly from real fields/live locals.
  Preserve the selected complete diagnostic and its full qualification.
- [ ] Install only after every linked word plus owner/ELF/data/guard-history audit.
- [ ] Recover original sine/cosine math separately before real arc-rendering
  acceptance; keep FCSR/hardware/gameplay outside bounded matching evidence.

The full Game matching goal remains active.
