# Game Owner Threshold Curve Limit And Projection Home Qualification

Date: 2026-10-10

## Baseline And Scope

Continue after consumer c68983ac3c9f8a40a81c29e823b9fd43138286b2 and mounted
tools 7972c9378cfb247add00ca8a53df40bc2242b6a3, both verified clean.
[Note 1200](1200-game-owner-threshold-curve-private-vector-home-recovery-20261010.md)
banked a complete 178-word diagnostic with the retail frame/saved signature,
nine private vector write multisets/final values, full-path delta-Y boundary,
zero padding and 154 raw instruction differences. Keep that form immutable.

Target func_151B3FDC remains 178 words/712 bytes, VA0x151B3FDC..0x151B42A4,
ROM0x1E148C..0x1E1754, frame0x118. New complete scalar diagnostic qualifies
threshold/quarter copies, both reads each and final values at their original
homes, plus projection store/read/final value. It retains all prior qualified
vector/delta-Y boundaries and saved homes, but emits 186 words/744 bytes,
185 raw differences and overflows by32 bytes. Do not combine its private proof
with the previous form's slot proof as if one form passes both gates.

No installation, new production guards, matching credit or profile changes.
Production remains the false zero-return placeholder. Single Codex writer,
zero Claude calls; no OGL/Release/editor/save changes. Root README unchanged.

## Measured Source And Profile Forms

[Scalar-home driver](../../tools/experiments/game_owner_points_threshold_curve_scalar_homes.py)
reuses the complete semantic seeds, compiler, lifetime transforms, parsers,
linker and MIPS/native32 oracles. Measure 67 full source forms:
16 cast/member projection/delta/scalar forms, 16 direct-member/cached-vector
forms, 16 typed-limit/register/counter forms, 16 scalar-lifetime forms and
three gate-lifetime forms. All pass bounded public comparisons, not all private
gates. Source variants can emit identical objects; this is not 67 unique streams.

Direct volatile vector members with cached midpoint arithmetic remove address
casts but lose the original frame/homes. Making epsilon volatile or adding
register hints does not improve the reported shape. Endpoint/delta reuse can
reduce the frame or increase length. Do not pad a frame with unused arrays.

Introduce a meaningful OwnerCurveLimits record with two volatile float fields.
Store the actor threshold and squared-length quarter, then take two snapshots
of each before the branch: one pair participates in the fallback comparison,
the other in the minor-radius calculation. No dummy reads or discarded loads.
The second pair is read on fallback too, matching retail's private read boundary.
Use an ordinary vertical temporary rather than spilling projected.y merely
because projected.x has an address-taken store. Original source representation
is a fitting hypothesis, not proven source recovery.

| Complete Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Prior slot-fitting vector form | 178 | 0x118 | 154 |
| Scalar delta/cast projection | 178 | 0x120 | 156 |
| Above with private threshold/quarter scalars | 184 | 0x118 | 181 |
| Direct members/private threshold-quarter/down counter | 188 | 0xE0 | 187 |
| Typed limits/single snapshots/down counter | 182 | 0x118 | 180 |
| Typed limits/two snapshots/down counter | 187 | 0x118 | 185 |
| Above with ordinary vertical temporary (selected) | 186 | 0x118 | 185 |
| Separate comparison temporaries | 186 | 0x120 | 186 |

Also measure eight full profile forms: prior slot and selected scalar bodies
under O2/g3, O2, O1/g3 and O1. O2 with/without g3 retains the same measured
length/frame/difference counts. O1 slot form is 224 words/frame0xD8/219
differences; O1 scalar form is 229/frame0xE0/226. All eight pass bounded public
comparisons; no private or exact-match credit is inferred from these profiles.
Keep the existing production O2/g3 profile. Early difference computation does
not improve the shape and is not hardware/FCSR-qualified.

## Confirmed Private Boundaries And Remaining Work

Selected lifetime-vertical retains frame0x118, paired f20..f31 at0x10..0x38,
S0..S3/RA at0x44..0x54, and all nine qualified vector homes at0xE8..0x108.
Those vector write multisets/final words match on the full matrix, mutations
and rebases; vector write order remains unproven. Delta-Y at0x110 retains one
matching store/read/final word on every path, including no-work.

New qualified scalar homes:

| SP Offset | Value | Writes/Reads On Active Or Fallback Path |
| --- | --- | --- |
| 0x68 | threshold snapshot | one store, two reads |
| 0x6C | squared-length quarter | one store, two reads |
| 0xD0 | projected horizontal displacement | one store, one read |

Each scalar's write events, read multisets/widths and final word match retail
through the full matrix, mutations and rebases. No-work performs zero accesses
to these homes. The two limit reads each finish before fallback or the first
trig call. Native32 sizeof(OwnerCurveLimits)=8; field offsets0/4. This does
not claim identical interleaving with other accesses or full fault prefixes.

Five retail scalar homes remain: endpoint-Z at0x5C, squared length at0x64/0xA4,
minor radius at0x98 and major radius at0xAC. Selected instead stores rootSquared
at0x70, major radius at0x98, minor radius at0x8C, endpoint-Z at0xAC and delta-Y
copy at0xA4. Extra delta-X/Z stores at0x10C/0x114 and limit copies at0x90/0x94
remain; the unnecessary vertical store0xD4 is removed. Default active fixture
has40 different private bytes; no-work still has20/19 by stack phase. This is
a bounded footprint, not a claim of monotonically improved whole memory.

Input read order, scalar spill scheduling, internal FP/GPR roles and complete
private memory still differ. Recover the five homes/values, eliminate extra
traffic and fit the full private-qualified body into178 words before matching
all instructions. Do not wholesale guard the 185 differing words or truncate
the body. Hardware/FCSR, actual trig, live gameplay and portable C fault
behavior remain separate/unvalidated.

## Fresh Qualification

[Scalar-home suite](../../tools/tests/test_game_owner_points_threshold_curve_scalar_homes.py):
all ten tests pass in70.750s, then final strengthened read-multiset/width run
passes all ten in82.186s. No failing correctness gate was weakened.

- 67 source forms/804 bounded cases/1,608 executions; zero IDO diagnostics/pools.
  Eight profile forms/96 cases/192 executions also qualify publicly.
- Prior complete178-word form reproduces its prior object text, functions and
  relocations exactly; frame280/differences154 unchanged.
- Full matrix:1,056 cases/2,112 executions; all178 original/186 selected words
  reached. Public stores/memory/calls/returns and saved GP/FP/SP qualify.
  Vector/delta-Y and all three scalar-home gates qualify in every case.
- 96 mutation/opaque-return cases/192 executions retain fresh step reads,
  endpoint/threshold snapshots and actual fallback return. Eight effective
  compiled negatives: four semantic, two prior vector/delta-Y private controls,
  and two limit-only controls. Single limit reads and swapped limit homes still
  pass public/vector/delta-Y gates before independently failing the scalar gate.
- Actual native32 complete C:512 cases, strict warnings preserved; bounded trig
  argument/output bits and whole actor canaries qualified. Separate native32
  pair-layout check passes.
- Full81-word original dispatcher:12 connected cases; actual157-word initializer:
  six fallback cases, all628 linked initializer bytes still retail-exact.
- Four symbol sets/eight links/48 cases/96 executions; seven relocation uses
  agree by kind/symbol and qualified private boundaries survive rebasing.
- Actual copied owner preserves all16 other raw bodies, relative relocations
  and pools; target matches isolated raw bytes/relocations. Actual padder rejects
  the744-byte symbol against its712-byte retail slot, as required.
- Eight explicit footprint cases reject whole private memory/input order
  equality while retaining read multisets and the new qualified homes.

Fresh make tools-check passes. Fresh match-progress retains the duplicate
generated_12D630 recipe warning and measures Game2,746/4,816 (57.02%),
total3,419/5,489 (62.29%), Init492/492 and Debugger181/181 exact, drift0,
different2,070. Production source/ELF/guards/progress hashes retain Note1196/1197
baseline; protected data189,088 bytes/720 owners exact, registration and both
constants unchanged. No production rebuild needed. Wider unchanged receipts
are prior, not fresh.

## Bank And Resume

Tools9ab2fae5c0a65af4e0aa32a63b724fee65e7cf9b banks the two authored files
before parent docs/pin. Mirror only absent newly authored files to the older
standalone checkout. HEADddbdd16b53ce60b054fb6e11bf0649a41f48375a and both
tracked dirty fingerprints unchanged;156 dirty entries become158.
No overwrite/reset/older commit/push. Both active checkouts must finish clean.

Fresh graphify update . refuses39,214-to-17,433 shrink and preserves19,398
nodes from2,972 still-existing out-of-corpus files. Keep version/zero-node
warnings; no force/purge/install. Await the fresh terminal detached parent
postcommit hook rather than treating an older log tail as current evidence.

Scoped audit:23 documents/4,049 relative links, zero broken. All30 affected
authored tooling files parse in both checkouts and have byte-identical older
mirrors; two are new this turn. Older tracked dirty fingerprints unchanged.

Ignored receipts: conker/build/game-owner-points-threshold-scalar-homes/ and
conker/build/game-owner-points-threshold-scalar-homes-test/.

- [x] Qualify limit stores/two reads/final words and projection boundary with original saved/vector/delta-Y homes.
- [x] Preserve prior178-word slot form; refuse actual32-byte overflow of the scalar-qualified form.
- [x] Qualify ten tests, eight independent compiled controls and connected/owner/rebase evidence.
- [x] Bank tools first and preserve production plus independent older work.
- [ ] Recover five remaining scalar homes, eliminate extra spills and fit178 words.
- [ ] Match FP/GPR lifetimes, exact accesses, full private memory/fault prefixes and all words before linked installation.
- [ ] Keep wider Game goal active; actual trig/hardware/live acceptance separate.
