# Game Owner Threshold Curve Recovery

Date: 2026-10-10

## Baseline And Scope

Continue after consumer f4c339b80722ab47a605759e93afd9301c2411c8 and tools
5a2c6f8fca1f43ebbf9c9861f1e36bbe7d6a805d, both active checkouts clean.
The preceding turn completed and banked the provider match in
[Note 1196](1196-game-linked-owner-position-provider-match-20261010.md).
This turn makes progress by recovering and qualifying the entire next callback;
the wider Game matching goal remains active.

func_151B3FDC: VA0x151B3FDC..0x151B42A4, ROM0x1E148C..0x1E1754,
178 words / 712 bytes, original frame 0x118. Registration D_8008FAF8[2] at
0x8008FB00, ROM0x2345C0, is verified from protected data and retail input.
The complete 81-word func_151B3184 invokes this one-argument callback.

The production source still contains its false zero-return C placeholder.
Only isolated/copy-owner diagnostics and tests change: no installation,
production guards, compiler profile changes or new matching credit. Root
README aggregate rows remain correct and unchanged.

Single Codex writer, zero Claude calls. Follow the offline workflow and
scoped graph query; reuse existing compiler, parser, MIPS/native32, padder,
initializer and data helpers. No OGL, Release, save or editor changes.

## Complete Recovered Behavior

Snapshot all six endpoint coordinates at actor+0x14 and actor+0x20.
Compute delta and test D_800AA3B0 < abs(deltaX) or < abs(deltaZ).
If both comparisons fail, return 1 without output writes or callbacks.
Retail epsilon bits are 0x38D1B717; NaN comparisons retain their false result.

Otherwise compute midpoint as start + delta*0.5, then both endpoints relative
to that midpoint. Normalize horizontal displacement and project the relative
endpoints onto it. Let projection be projectedEnd - projectedStart and vertical
be relativeEndY - relativeStartY. Form squared = projection^2 + vertical^2,
length = sqrt(squared), majorRadius = length*0.5, and the normalized projected/
vertical components. Read actor+0x138 once, before any helper call.

Compare that threshold against squared*0.25 with strict less-than. If smaller,
return func_151B3A7C(actor)'s result directly. Do not discard or replace the
helper return with 1 in the recovered source. The actual matched initializer
returns1; tests also qualify opaque result0/2/0xFFFFFFFF at the call boundary.

Otherwise minorRadius = sqrt(threshold - squared*0.25). Starting at angle0,
write ten XYZ positions at actor+0x48 with a 0x18-byte stride. Each iteration
calls sinf then cosf with the same angle. With along = majorRadius*cosine and
across = minorRadius*sine, retail uses both of these literal subtractions:

```c
h = along * horizontal - across * upright;
v = along * upright - across * horizontal;
```

Map h along the horizontal normal, add midpoint to XYZ, and leave velocities,
metadata and flags untouched except for modeled helper actions. Load
D_800AA3B4 after the point's Z store, then advance angle, including the last
iteration. Its protected bits are 0x3EB2B8C3. Do not snapshot the step before
callbacks: helper mutations must affect later angles.

## Compiler Evidence

[Candidate driver](../../tools/experiments/game_owner_points_threshold_curve_candidates.py)
compiles complete semantic bodies at the existing O2/g3 profile, with zero
diagnostics and no local pools. Seven positive source forms qualify in bounded
public-contract comparisons; none matches the original frame/private layout.

| Full Source Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Selected endpoint snapshots | 169 | 0x110 | 178 |
| Volatile midpoint/relative vectors | 179 | 0xB8 | 174 |
| Volatile threshold | 172 | 0x110 | 176 |
| Volatile squared length | 168 | 0x108 | 174 |
| Volatile relative vectors only | 174 | 0x108 | 169 |
| Volatile delta-Y | 180 | 0x108 | 171 |
| Volatile delta-Y and threshold | 180 | 0x108 | 176 |

Selected diagnostic: 169 words / 676 bytes, frame 272 rather than retail 280.
The actual padder fits it into the 712-byte slot with 36 zero-padding bytes,
but that is not a full-body match. Reject installation. No frame padding,
arbitrary private arrays or wholesale retail-word substitution is introduced.

## Fresh Qualification

[Recovery suite](../../tools/tests/test_game_owner_points_threshold_curve_recovery.py):
all nine tests pass in 16.307s after the final private/read-contract gate.

- 1,056 guest matrix cases / 2,112 executions cover 12 geometries, 11 thresholds,
  four flag patterns and both stack phases. Finite, epsilon equality/next word,
  NaN, infinity and overflow inputs qualify in the bounded low-word model.
  Independent reference agrees with original and candidate public memory,
  ordered public stores, complete callback arguments and return values.
- Every original 178 and candidate 169 word is reached across the three paths.
  Saved GP/FP state and SP restore correctly. Final private memory differs;
  this is explicitly tested, not ignored or described as matched.
- 96 mutation/opaque-return cases / 192 executions qualify endpoint/threshold
  snapshots and fresh step reads after callbacks. Four effective compiled
  negatives reject plus instead of minus in v, a stale step snapshot,
  quarter-radius substitution and discarded fallback results.
- The quarter-radius control needs a real rounding discriminator. Geometry 3
  produces squared*0.25 bits 0x40C80001 but radius*radius bits 0x40C80000.
  Threshold 6.25 therefore selects different paths; do not call them equivalent.
- Native32 executes 512 cases with the complete selected C and bounded helpers,
  checking original guest angle/output bits on the curve path and whole actor
  canaries on every path. Includes endpoint/threshold/flag and step mutations.
- Full original 81-word dispatcher: 12 connected cases. Full original 157-word
  initializer: six actual connected fallback cases; all 628 linked initializer
  bytes are independently confirmed retail-exact. Trig helpers remain bounded
  models, not original sinf/cosf or hardware/FCSR/live acceptance.
- Four independent symbol sets / eight links / 48 rebase cases / 96 executions;
  all seven relocation uses agree by kind/symbol. Semantic agreement is not
  byte equality.
- Copied actual owner: target bytes/relative relocations equal the isolated
  candidate; all 16 other raw bodies, pools and relative relocations unchanged.
  Zero diagnostics; actual padder respects the 712-byte target span.
- Public read multisets agree: six endpoint words once, epsilon once,
  threshold once, step ten times. Each step read follows that point's Z store
  and its two trig calls. Input read ordering still differs, so no full access-
  order, fault-prefix, private-memory or hardware equivalence claim is made.

Fixture corrections: preserve byte canaries on no-write/fallback paths rather
than interpreting their untouched byte pattern as native little-endian float
words against the guest's big-endian word value. Reuse the existing owner's
fabsf pragma rather than duplicating it. Neither correction changes production
or weakens active-path float-bit comparisons. Failed native comparisons now
identify case, point, axis and expected/actual words.

## Private Layout Handoff

Both bodies save paired f20..f31 at frame-relative 0x10..0x38 and S0..S3/RA
at 0x44..0x54. Their physical homes still differ by the eight-byte frame gap.
Retail workspace observed on the active path:

- 0x5C: endpoint Z; 0x64 and 0xA4: squared length copies.
- 0x68: threshold; 0x6C: squared quarter; 0x98: minor radius.
- 0xAC: major radius; 0xD0: projection.
- 0xE8/0xEC/0xF0: relative end XYZ.
- 0xF4/0xF8/0xFC: relative start XYZ.
- 0x100/0x104/0x108: midpoint XYZ; 0x110: delta-Y.

Candidate instead spills endpoints at 0xD4/0xD8/0xDC, midpoint at 0x5C/0x60/0x64,
normal/projection/vertical at 0xB0..0xBC, and length/squared at 0xA8/0xAC.
Resume from the exact read/store footprints in ignored reads-homes.json,
not just the frame size. Recover the original private workspace and saved
value lifetime before closing FP roles, schedule and full 178-word fit.

## Bank And Production Boundary

Fresh make tools-check passes. Source, linked ELF, guard manifest and conversion
CSV SHA-256 equal the Note 1196 baseline; no production rebuild is needed for
this tools-only diagnostic. Protected data remains 189,088 bytes / 720 owners,
zero differences, with registered pointer and both constants unchanged.
Fresh matcher remains Game 2,746/4,816 (57.02%), total 3,419/5,489 (62.29%),
Init 492/492 and Debugger 181/181 exact, zero drift / 2,070 different.
Prior neighbor-suite receipts are unchanged prior evidence, not fresh runs.

Tools 0329f7097d84c79cd3769a31087da1158490c609 banks the two authored files
before parent docs/pin. Only absent new files are mirrored to the older checkout:
HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and both tracked dirty hashes
remain identical; 148 dirty entries become 150. No overwrite, reset, older commit
or push. Keep the root README free of diagnostic narratives and false credit.

Fresh graphify update . refuses 39,176-to-17,395 node shrink and preserves
19,398 nodes from 2,972 still-existing out-of-corpus files. Retain version/
zero-node warnings; no force, purge or install. Await the detached parent hook
before reporting a clean, fully banked checkpoint.

Scoped documentation audit: 19 documents / 4,011 relative links, zero broken.
Twenty-two affected tooling files parse in both checkouts and have exact older
mirrors; two are newly authored for this recovery.

Ignored measurements and receipts: conker/build/game-owner-points-threshold-curve/
and conker/build/game-owner-points-threshold-curve-test/.

## Resume

- [x] Recover and qualify the complete 178-word routine's three public paths.
- [x] Verify registration, original dispatcher and actual matched initializer.
- [x] Qualify native/guest/mutations/rebases/owner/read-footprint gates and bank tools.
- [ ] Recover original 0x118 frame, private workspace, saved-value lifetimes and input-read schedule.
- [ ] Match all 178 words without substituting a smaller public-only contract; qualify full private state and fault prefixes before installation.
- [ ] Install only after full linked owner/ELF/data/guard-history qualification; keep trig/hardware/live acceptance separate.
