# Game Owner Threshold Curve Squared Copy And Physical Frame Gates

Date: 2026-10-10

## Baseline And Scope

Continue after consumer32ab171eb6483175ebdcd6f75c077bc4b177f950 and mounted
tools9ab2fae5c0a65af4e0aa32a63b724fee65e7cf9b, both verified clean.
[Note 1201](1201-game-owner-threshold-curve-limit-and-projection-home-qualification-20261010.md)
banked the limit/projection boundary in a186-word/frame0x118 diagnostic.
The earlier178-word slot form remains separate. This turn qualifies the first
squared-length copy and adds explicit gates against combining incompatible
frame and value proofs. Production remains the false zero-return placeholder.

Target func_151B3FDC is178 words/712 bytes, VA0x151B3FDC..0x151B42A4,
ROM0x1E148C..0x1E1754, original frame0x118. No installation, new guards,
matching credit or compiler profile changes. Single Codex writer, zero Claude
calls; no OGL/Release/editor/save changes. Root README unchanged.

## Complete Spill And Record Measurements

[Spill-home driver](../../tools/experiments/game_owner_points_threshold_curve_spill_homes.py)
reuses complete semantic seeds, lifetime transforms, compiler, parsers,
MIPS/native32 oracles, linker and actual owner/padder helpers. Measure40 full
forms:16 squared/endpoint/radius controls, eight meaningful record/array forms,
eight late-record scalar lifetimes and eight partial-midpoint/cursor forms.
All pass bounded public comparisons, not all private gates; source repetitions
can emit identical objects. No arbitrary unused arrays or frame padding.

Three-field squared/threshold/quarter records shift the limit homes. A fourth
real field carries the endpoint-Z snapshot: the compound assignment's ordinary
result participates in delta-Z, while the private field is read later for last.Z.
Reorder that meaningful record as squared/threshold/quarter/endpointZ. In its
complete form the first three float values land at the correct absolute homes.
Source representation remains a fitting hypothesis, not recovered original C.

| Complete Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Prior scalar diagnostic | 186 | 0x118 | 185 |
| Explicit second squared local home | 190 | 0x118 | 187 |
| Three-field measures record | 186 | 0x118 | 185 |
| Endpoint/squared/threshold/quarter record | 186 | 0x120 | 186 |
| Squared/threshold/quarter/endpoint record (selected) | 186 | 0x120 | 186 |
| Above with endpoint lifetime reuse | 185 | 0x118 | 183 |
| Above with squared delta-Y snapshot | 185 | 0x118 | 182 |
| Partial direct midpoint/down counter | 194 | 0x118 | 193 |

The185-word/frame0x118 alternatives lose the original squared/limit homes.
Direct-member midpoint/cursor forms increase length or change the frame.
Do not treat equal length/frame/difference counts as identical private layouts.
Both prior slot and scalar objects reproduce their complete text, function
symbols and relocations exactly in the new suite.

## Qualified Values Versus Rejected Frame

Selected late-endpoint-record emits186 words/744 bytes with frame0x120.
All nine vector write multisets/final words, full-path delta-Y store/read/value,
limit copies/two reads each, and projection store/read/final word remain correct
at their absolute addresses. The first squared copy has one matching4-byte
store/final word on active/fallback paths, zero reads, and no access on no-work.
This qualifies across the full matrix, mutation cases and independent rebases.

| Value | Original SP Offset (Frame0x118) | Selected SP Offset (Frame0x120) |
| --- | ---: | ---: |
| First squared copy | 0x64 | 0x6C |
| Threshold | 0x68 | 0x70 |
| Quarter | 0x6C | 0x74 |
| Projection | 0xD0 | 0xD8 |
| Vector homes | 0xE8..0x108 | 0xF0..0x110 |
| Delta-Y | 0x110 | 0x118 |

First squared home is incoming SP-0xB4 in both. Correct relative offsets alone
are not sufficient: the saved signature still uses paired f20..f31 at0x10..0x38
and S0..S3/RA at0x44..0x54, so every physical saved write is8 bytes too low.
The strengthened executed-event check proves the entire saved-write sequence,
including widths/values, equals retail translated downward8 bytes. Public ABI
restoration succeeds, but original private saved homes do not. Reject the frame.

Independent cross-check: prior scalar form passes the frame/vector/limit gates
but fails the squared-copy gate; selected passes the float-home gates but fails
the frame/saved-location gate. Neither can borrow the other's acceptance.
Actual owner/padder also rejects744 bytes against the712-byte slot (32 overflow).

Endpoint-Z, second squared copy and both radius homes remain unqualified.
Selected endpoint-Z is at original-frame coordinate0x70 rather than0x5C;
major radius at0x98, minor radius at0x8C and delta-Y copy at0xA4 remain wrong.
Extra delta/limit spills, exact access order and internal FP/GPR lifetimes remain.
Default active private memory differs by80 bytes; fallback by76, including the
save-location shift. Do not claim overall private-memory improvement or matching.
Recover one complete frame/private/slot-correct form, then all178 words and
full fault prefixes before linked installation. Actual trig, hardware/FCSR,
live gameplay and portable C fault semantics remain separate/unvalidated.

## Fresh Qualification

[Spill-home suite](../../tools/tests/test_game_owner_points_threshold_curve_spill_homes.py):
all eleven tests pass in54.131s. Strengthen the saved-event check afterward;
its focused rerun passes in1.520s. Other ten test bodies/selected C are unchanged.

- 40 source forms/480 bounded cases/960 executions; zero IDO diagnostics/pools.
- Full matrix:1,056 cases/2,112 executions; all178 original/186 selected words
  reached. Public stores/memory/calls/returns and saved GP/FP/SP ABI qualify;
  absolute float-home gates qualify, physical saved homes explicitly do not.
- 96 mutation/opaque-return cases/192 executions preserve endpoint/threshold
  snapshots, fresh step reads and fallback return. Nine effective compiled
  controls: four semantic, four prior private boundaries and missing square copy.
  Missing squared store still passes public/vector/limit gates before its
  independent square gate rejects it.
- Actual native32 complete C:512 cases with bounded trig argument/output bits,
  whole actor canaries and strict warnings. Separate native32 record layout:
  size16, field offsets0/4/8/12.
- Full81-word dispatcher:12 connected cases; actual157-word initializer:six
  fallback cases, all628 linked initializer bytes remain retail-exact.
- Four symbol sets/eight links/48 cases/96 executions; seven relocation uses
  agree by kind/symbol and absolute qualified float homes survive rebasing.
- Actual copied owner preserves16 other raw bodies, relative relocations and
  pools; target matches isolated bytes/relocations. Actual overflow is rejected.
- Eight footprint cases reject whole memory/input ordering equality; four
  orthogonal frame/squared-copy cases show the real acceptance tradeoff.

Fresh make tools-check passes. Fresh matcher retains the duplicate generated_12D630
recipe warning and measures Game2,746/4,816 (57.02%), total3,419/5,489 (62.29%),
Init492/492 and Debugger181/181 exact, drift0/different2,070. Source/ELF/guards/
progress hashes retain Note1196/1197 baseline; data189,088 bytes/720 owners exact,
registration/constants unchanged. No production rebuild required. Wider unchanged
receipts are prior, not fresh.

## Bank And Resume

Toolsb71d5d023cc3959e2506ac306eefb00b7dc48a49 banks the two authored files
before parent docs/pin. Mirror only absent new files to the older standalone
checkout: HEADddbdd16b53ce60b054fb6e11bf0649a41f48375a and both tracked dirty
fingerprints unchanged;158 dirty entries become160. No overwrite/reset/older
commit/push. Both active checkouts must finish clean.

Fresh graphify update . refuses39,223-to-17,442 shrink and preserves19,398
nodes from2,972 still-existing out-of-corpus files. Keep version/zero-node
warnings; no force/purge/install. Await fresh terminal parent postcommit hook.

Scoped audit:24 documents/4,057 relative links, zero broken. All32 affected
authored tooling files parse in both checkouts and have byte-identical older
mirrors; two are new this turn. Older tracked dirty fingerprints unchanged.

Ignored receipts: conker/build/game-owner-points-threshold-spill-homes/ and
conker/build/game-owner-points-threshold-spill-homes-test/.

- [x] Qualify first squared-copy absolute home with all prior float boundaries in the frame-shifted form.
- [x] Prove physical saved-location shift and refuse frame/slot acceptance; preserve prior objects.
- [x] Pass eleven tests, nine compiled controls and strengthened saved-write rerun.
- [x] Bank tools first; preserve production and older independent work.
- [ ] Combine original frame/saved homes, float boundaries and178-word extent in one complete body.
- [ ] Recover remaining scalar homes/lifetimes, exact access/fault behavior and all words before linked installation.
- [ ] Keep wider Game goal active and hardware/live acceptance separate.
