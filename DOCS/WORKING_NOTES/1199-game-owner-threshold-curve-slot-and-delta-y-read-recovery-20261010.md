# Game Owner Threshold Curve Slot And Delta-Y Read Recovery

Date: 2026-10-10

## Baseline And Scope

Continue after consumer e53a2c7e69499b1e5d2882638e6e985660c4d248 and mounted
tools4668149b79a0349222d636009f9b1ac5ceaee095, both verified clean.
[Note 1198](1198-game-owner-threshold-curve-frame-and-delta-y-fitting-20261010.md)
banked the original frame/delta-Y store, but its selected188-word body overflowed
and omitted the private read on the no-work path.

Target func_151B3FDC remains178 words/712 bytes at VA0x151B3FDC..0x151B42A4,
ROM0x1E148C..0x1E1754, frame0x118. This turn makes progress with a complete
slot-fitting diagnostic and the full-path delta-Y store/read/value. Production
remains its false zero-return placeholder; no installation, guards, matching
credit or profile changes. Single Codex writer, zero Claude calls. No OGL,
Release, editor or save changes; root README totals remain correct and unchanged.

## Complete Vector And Read Fitting

[Vector driver](../../tools/experiments/game_owner_points_threshold_curve_vectors.py)
reuses the immutable original recovery seed, typed volatile delta-Y, compiler,
workspace and lifetime helpers. Express horizontal normal, projected displacement
and normalized projected direction as meaningful vector records. Their original
source representation is a hypothesis, not proven source recovery. Unused vector
components are not read, initialized or used as arbitrary frame padding.

Read delta.y into the real normalization temporary before the short-circuit gate,
and use that snapshot for midpoint Y. This ensures the private read occurs even
when the horizontal displacement gate selects no work. Do not add a dummy load:
the loaded value participates in the active calculation.

Measure72 complete forms:32 vector/private/endpoint/epsilon forms,24 workspace
read/projection/register-hint forms,16 cached-midpoint forms. All qualify in bounded
public comparisons; repeated source variants can emit identical bodies. This is
72 measured source forms, not72 distinct instruction streams or private proofs.

| Full Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Ordinary snapshot/register scalars (selected) | 170 | 0x118 | 173 |
| Ordinary snapshot/private threshold-quarter | 176 | 0x118 | 172 |
| Above with volatile epsilon read | 177 | 0x118 | 167 |
| Workspace reads/register scalars | 181 | 0x118 | 176 |
| Workspace reads/private projected-X store | 180 | 0x118 | 171 |
| Cached midpoint/private radii | 191 | 0x100 | 190 |

Selected source emits680 bytes, original280-byte frame and original saved-home
signature directly from C. Actual padder fits the712-byte slot with32 zero-padding
bytes. That proves extent only: padded zeros do not replace the missing original
instructions, private values or complete178-word match.

Workspace-read forms place stores at all nine original relative/midpoint vector
offsets, but introduce S4 and shift the saved-register homes. This footprint is
measured, not full private-value qualification. Cached/volatile midpoint forms
instead reduce the frame or increase instruction count. Do not combine these
facts into an unsupported claim that one candidate matches the whole workspace.

## Confirmed Delta-Y Boundary And Remaining Gaps

Selected frame0x118 saves paired f20..f31 at0x10..0x38 and S0..S3/RA at
0x44..0x54, matching physical homes. The volatile delta-Y store is at SP+0x110,
eight bytes below incoming SP. Its address, width, value, one read per invocation
and final word agree on all three paths and both stack phases in the full matrix,
mutations and rebases. The no-work zero-read gap from Note1198 is closed.

This does not establish identical read ordering or fault prefixes. The selected
body also keeps a delta-Y copy at0xA4, where retail eventually keeps squared length;
other stack values differ. Its active-path private stores, excluding saves:
0x58,0x60,0x64,0xA4,0xB0,0xB4,0xDC,0xE4,0xEC,0xF8,0x104,0x110.
Compare against the complete original footprint in
[Note 1197](1197-game-owner-threshold-curve-recovery-20261010.md) and reads-homes.json.
Most original vector/radius/threshold/quarter/projection homes remain unmatched.
Input read ordering and internal FP/GPR roles/lifetimes also differ.

Selected public read multisets match original: each endpoint and epsilon once,
threshold once on active paths, ten step reads after each point's Z store and two
trig calls on the curve path. Endpoint/threshold snapshots, literal subtractions,
fresh step updates and propagated fallback returns retain the complete contract.
Entire private memory, complete access ordering and all178 words remain required
before installation. No portable C fault, real trig/FCSR/hardware/live claim.

## Fresh Qualification

[Vector suite](../../tools/tests/test_game_owner_points_threshold_curve_vectors.py):
all nine tests pass in68.404s. The independent negative-source binding then gets
a final focused rerun:one test passes in4.773s. Its scoped source patch produces
the same selected-body controls under the suite and independently outside it.

The first run failed one test in68.948s because the inherited plus/minus negative
searched obsolete scalar names and therefore made no source change. Correct the
vector expression, assert source and emitted words differ, and rerun. This was a
test-fixture defect, not evidence to relax the semantic gate or change production.

- 72 complete forms/864 bounded cases/1,728 executions; zero diagnostics/pools,
  no original-byte-exact form. Immutable seed and selected170/280/173 discriminator.
- Selected full matrix:1,056 cases/2,112 executions, all original178 and candidate
  170 words reached. Public memory/stores/callback arguments/returns and saved
  GP/FP/SP state agree; actual delta-Y store/read/value qualifies in every case.
- 96 mutation/opaque-return cases/192 executions. Four effective compiled semantic
  controls reject plus instead of minus, stale step, quarter-from-radius rounding
  and discarded fallback return. A fifth full-source control passes the public
  contract but omits the no-work private read; the delta-home gate rejects it.
- 512 actual native32 cases with complete selected C/bounded trig helpers;
  curve float/argument bits and whole actor canaries qualify.
- Full81-word original dispatcher:12 connected cases; actual157-word initializer:
  six connected fallback cases, all628 linked initializer bytes still exact.
- Four independent symbol sets/eight links/48 cases/96 executions; all seven
  relocation uses agree by kind/symbol, and delta-Y home remains exact.
- Copied actual owner:16 other raw bodies, relative relocations and pools unchanged;
  target raw bytes/relocations equal the isolated candidate. Zero diagnostics.
  Actual assembled padded object has680-byte target symbol and712-byte slot.
- Eight explicit public-read/private-footprint cases retain the selected delta
  boundary and explicitly reject whole private-memory/input-order equality.

Fresh make tools-check passes. Production source/ELF/guard manifest/progress CSV
SHA-256 remain the Note1196/1197 baseline. Protected data189,088 bytes/720 owners
stays exact; registration and both constants unchanged. New production guards0;
no production rebuild needed. Fresh matcher remains Game2,746/4,816 (57.02%),
total3,419/5,489 (62.29%), Init492/492 and Debugger181/181 exact,
zero drift/2,070 different. Wider unchanged suite receipts are prior, not fresh.

## Bank And Resume

Toolsb403c1c1fce857fcac173fa1889b4708e540629a banks the two authored files before
consumer docs/pin. Mirror only absent new files to the independently dirty older
checkout: HEADddbdd16b53ce60b054fb6e11bf0649a41f48375a and both tracked dirty
fingerprints unchanged;152 entries become154. No overwrite/reset/older commit/push.

Fresh graphify update . refuses39,196-to-17,415 node shrink and preserves
19,398 nodes from2,972 still-existing out-of-corpus files. Retain version/zero-node
warnings; no force, purge or install. Await detached consumer postcommit hook and
fresh terminal receipt before reporting a fully banked clean checkpoint.

Scoped audit:21 documents/4,030 relative links, zero broken. All26 affected
authored tooling files parse in both checkouts and have byte-identical older
mirrors; two are new for this turn.

Ignored receipts: conker/build/game-owner-points-threshold-vectors/ and
conker/build/game-owner-points-threshold-vectors-test/.

- [x] Fit complete semantic body into the slot while retaining original frame/saved homes.
- [x] Qualify real delta-Y store/read/value on every path and reject public-only negative.
- [x] Bank tools before parent docs/pin; preserve production and independent older work.
- [ ] Recover remaining actual vector/scalar homes and private values without shifting saved homes.
- [ ] Recover FP/GPR lifetimes, exact input/private access scheduling and all178 words.
- [ ] Qualify full private memory/fault prefixes and whole linked owner/ELF/data/guard history before installation.
- [ ] Keep wider Game goal active; real trig/hardware/live acceptance remains separate.
