# Game Owner Threshold Curve Frame And Delta-Y Fitting

Date: 2026-10-10

## Baseline And Scope

Continue after consumer c1a483f1b8eab31cc6926e47f8f88895527745af and mounted
tools0329f7097d84c79cd3769a31087da1158490c609, both verified clean.
The full semantic recovery and original workspace are in
[Note 1197](1197-game-owner-threshold-curve-recovery-20261010.md).

Target func_151B3FDC remains VA0x151B3FDC..0x151B42A4,
ROM0x1E148C..0x1E1754,178 words/712 bytes, original frame0x118.
This turn improves a complete diagnostic's real frame and delta-Y home,
not the production placeholder. Single Codex writer, zero Claude calls;
no OGL, Release, editor, saves, profile changes or production guards.

## Complete Source Fitting

[Workspace driver](../../tools/experiments/game_owner_points_threshold_curve_workspace.py)
reuses the existing compiler, typed volatile-Y delta, scalar lifetime transformer
and complete threshold-curve body. It measures76 complete forms at O2/g3:
48 vector/scalar/reuse/cursor forms,16 compact endpoint forms and12 delta-first
declaration forms. No unused frame padding, invented private arrays or wholesale
word replacement. All three public paths and the literal subtraction in both
curve coordinates remain intact.

The driver retains an immutable original seed. The first test run passed in
68.153s, but review found that the inherited test's selected-body patch also
changed the driver's generated seed. Fix that fixture, add a source/measurement
discriminator, and rerun all76 actual forms. Only the corrected final result is
the qualification receipt; do not count the first run as76 independent forms.

| Complete Source Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Ordinary snapshot, register scalars | 180 | 0x108 | 171 |
| Relative vectors, private threshold/quarter | 178 | 0x108 | 153 |
| Relative vectors, endpoint reuse, private threshold/quarter/radii | 178 | 0xD8 | 159 |
| Delta-first ordinary, private radii (selected) | 188 | 0x118 | 187 |
| Delta-first ordinary, private threshold/quarter/radii | 185 | 0x118 | 181 |
| Delta-first relative, private threshold/quarter | 178 | 0x108 | 153 |

Raw differences are a complete aligned word comparison including overflow;
they are not a count of independent guard edits. Several forms coincide with
retail length or frame but none matches the complete body. The selected form
isolates frame/delta-Y recovery with only private radius declarations; the
185-word alternative is measured and public-qualified, not fully private/native
qualified or installed. Do not choose a form on length alone.

## Confirmed Frame And Remaining Private Gaps

Selected diagnostic allocates the original280-byte frame directly from C.
It saves paired f20..f31 at frame-relative0x10,0x18,0x20,0x28,0x30,0x38;
S0..S3/RA at0x44,0x48,0x4C,0x50,0x54. Both frame size and physical saved homes
now agree. Saved values/ABI/SP restore in the bounded guest cases; exact original
internal register roles and saved-value lifetimes are not claimed.

Declaring the actual typed delta before the coordinate workspace restores
the delta-Y store at SP+0x110, eight bytes below incoming SP. Original and
candidate stores agree in address/width/value across no-work, fallback and curve
cases at both stack phases. On active/fallback paths each reads that home once.
On the no-work path original reads it once but the candidate reads it zero times.
That private read-prefix mismatch remains an explicit failed matching boundary.

Other selected active-path private stores, excluding saves and delta-Y:
0x58,0x5C,0x60,0x68,0x6C,0x70,0x80,0xA4,0xA8,0xAC,
0xC4,0xD0,0xD4,0xD8,0xE0,0xE4. Retail's complete layout in Note1197 and
reads-homes.json remains the reference; equal offset numbers alone do not prove
equal values or vector roles. Entire final private memory and input-read order
still differ. Full access-order/fault-prefix/hardware equality is not claimed.

Public read multisets agree for the selected diagnostic: six endpoints once,
epsilon once, threshold once on active paths and ten step reads on the curve
path. Each step read follows that point's Z store and its two trig calls.
Endpoint/threshold snapshots and fresh step mutations retain their original
public behavior. No public-only agreement substitutes for missing private proof.

## Fresh Qualification

[Workspace suite](../../tools/tests/test_game_owner_points_threshold_curve_workspace.py):
all nine final tests pass in83.977s after seed isolation and explicit step-order
checks. Reuse the original reference/oracle/native/connected/data helpers.

- 76 full forms,912 bounded public cases/1,824 executions; zero diagnostics
  and zero local pool bytes. No measured form is retail-byte-exact.
- Selected full matrix:1,056 cases/2,112 executions across12 geometries,
  11 thresholds,four flags and two stack phases. Every original178 and
  candidate188 word reached; public memory, ordered stores, callback arguments,
  results and saved ABI state agree with the independent bounded model.
- 96 mutation/opaque-return cases/192 executions and four effective compiled
  semantic negatives; retain strict threshold rounding and return propagation.
- 512 actual native32 cases using the complete selected C and bounded trig
  helpers; curve float/argument words and actor canaries qualify.
- Original full81-word dispatcher:12 connected cases; real full157-word
  initializer:six connected fallback cases. Its628 linked bytes remain exact.
- Four independent symbol sets/eight links/48 cases/96 executions;
  all seven relocation uses agree by kind/symbol. Semantic, not byte equality.
- Actual copied owner:16 other raw bodies, relative relocations and pools
  unchanged; target raw bytes/relocations equal the isolated188-word candidate.
  Zero diagnostics. The actual padder rejects candidate0x2F0 bytes versus
  retail0x2C8:40-byte/ten-word overflow. Nothing is installed.
- Eight explicit private/read-footprint cases retain the real delta-Y store
  and record the no-work private-read mismatch and other private/input gaps.
- Fresh make tools-check passes. Source, linked ELF, guard manifest and progress
  CSV SHA-256 remain the Note1196/1197 baseline; no production rebuild required.
  Protected data189,088 bytes/720 owners remains exact, registered pointer and
  both constants unchanged. New production guards0.

Trig/FCSR/hardware/live acceptance remains separate. Unchanged wider neighbor
receipts are prior evidence, not fresh tests. Fresh matcher:
Game2,746/4,816 (57.02%), total3,419/5,489 (62.29%), Init492/492 and
Debugger181/181 exact, zero drift/2,070 different. Root README totals remain
correct and unchanged; keep diagnostic narratives in this note and the indexes.

## Bank And Resume

Tools4668149 banks the two authored files before consumer docs/pin. Only absent
new files are mirrored to the independently dirty older checkout: HEAD remains
ddbdd16b53ce60b054fb6e11bf0649a41f48375a, both tracked dirty fingerprints unchanged,
150 entries become152. No overwrite, reset, older commit or push.

Fresh graphify update . refuses39,187-to-17,406 node shrink and preserves
19,398 nodes from2,972 still-existing out-of-corpus files. Retain version and
zero-node warnings; no force, purge or install. Await the detached consumer
postcommit hook and fresh terminal receipt before reporting a clean checkpoint.

Scoped checkpoint audit:20 documents/4,020 relative links, zero broken.
All24 affected authored tooling files parse in both checkouts and have exact
older mirrors; two are newly authored for this fitting turn.

Ignored receipts: conker/build/game-owner-points-threshold-workspace/ and
conker/build/game-owner-points-threshold-workspace-test/.

- [x] Qualify complete workspace/lifetime forms and recover original frame/saved homes/delta-Y store.
- [x] Preserve explicit overflow/private/read boundaries and bank tools before parent docs/pin.
- [ ] Recover no-work delta-Y read and remaining vector/scalar homes before combining the shorter185-word form.
- [ ] Close FP roles, private lifetimes, input schedule and all178 words; qualify full private memory and faults.
- [ ] Install only after whole linked owner/ELF/data/guard-history audit; keep wider Game goal active.
