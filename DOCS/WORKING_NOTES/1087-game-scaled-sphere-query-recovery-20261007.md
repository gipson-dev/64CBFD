# Game Scaled Sphere Query Recovery

Date: 2026-10-07. Baseline: `c05f617e`,
[Note 1086](1086-game-sphere-callee-allocation-match-20261007.md).

Recover the complete `func_15145AD8`, VA `0x15145AD8..0x15145C90`,
ROM `0x172F88..0x173140`, 110 words/frame `0x88`.
The [experimental body](../../tools/experiments/game_scaled_sphere_query_candidates.py)
now has the original ABI, frame and private-local offsets. It emits **111 words
with 72 aligned differences**, so it remains uninstalled. Production retains
the zero-return placeholder; no guard/profile/shared-header/padder changes and
no matching increment are claimed.

## Complete Caller Contract

Eight incoming positions: origin vector, direction vector, `struct127` actor,
first point, second point, first dimension pointer, second dimension pointer,
and center pointer. The recovered local prototype uses existing SDK/actor/vector
types; no shared declaration is changed.

1. Retail redirects each **non-null** incoming dimension/center pointer to a
   private local. Null remains address zero. Preserve this reversed-looking
   condition, including its argument-home and saved-register lifetime.
2. Connect the complete 41-word `func_1515C1A0` dependency: signed actor
   dimensions and adjusted position below ID `0xBB`, otherwise unit dimensions
   and unadjusted position. The helper is already a direct C match from Note 1037.
3. Reject zero second dimension, then zero first dimension, before reading the
   origin/direction, Y scales or point outputs. This is sequential lazy behavior.
4. Capture actor `0xE0` inverse Y scale and `0xDC` Y scale. Copy origin and
   direction into private vectors, scaling their Y components.
5. Connect the complete 50-word `func_15145128` normalizer in place, retaining
   its length and reciprocal outputs. Reject zero direction length.
6. Scale the queried center's Y and submit the complete nine-position
   `func_151451F0` call, including length as threshold and private distance
   outputs. Connect its real 126-word sphere callee and 13-word dot helper.
7. On success, reload both point-pointer homes and the saved private inverse,
   then rescale first Y followed by second Y. Rejection leaves prior point
   writes intact and performs no final Y rescaling.

The standalone compiler's structured `.mdebug` receipt confirms frame 136 and
these entry-relative locals, without dummy padding or unused components:

| Locals | Entry-Relative Offsets | Frame-Relative Offsets |
| --- | --- | --- |
| `center`, `radius`, `height` | `-12`, `-16`, `-20` | `0x7C`, `0x78`, `0x74` |
| `origin`, `direction`, `scaledCenter` | `-32`, `-44`, `-56` | `0x68`, `0x5C`, `0x50` |
| `length`, `first`, `second` | `-60`, `-64`, `-68` | `0x4C`, `0x48`, `0x44` |
| `scale`, `inverse`, `reciprocal` | `-72`, `-76`, `-80` | `0x40`, `0x3C`, `0x38` |

The first 34 words are already direct. The dimension call relocation remains
at `0x58`. The normalizer and wrapper call relocations are at raw `0x100/0x16C`
instead of retail `0xFC/0x168`; their symbol identities remain correct.
The extra word cannot fit the original slot. Do not remove or rewrite a branch,
patch private offsets or change an owner profile merely to force installation.

## Compiler Controls

The maintained driver reproduces **71 controls**, all without isolated
diagnostics, none byte-exact:

- 60 source/branch/commutative-order controls over O2/g3, O2, O1/g3 and O1.
  Selected straight O2/g3: 111 words/frame `0x88`, 72 differences.
  Its O2 control is 110 words/frame `0x88`, but still 52 differences.
  Nested forms may fit 110 words only with the wrong `0x80` frame; combined
  gates may emit 109 words but change the branch shape and retain differences.
- Seven meaningful origin/direction/scaled-center union views retain the
  selected 111-word/frame `0x88`/72-difference result.
- Four explicit normalizer-pointer preparations emit 111 words and enlarge
  the frame to `0x90` or `0x98`, 94 differences. `register` hints do not fix it.

The remaining problem includes the second zero-check/address-preparation
schedule and a shifted later body. These differences are not yet classified as
closed register/scheduling normalizations. No proposed target guards exist.

## Qualification

[Ten tests](../../tools/tests/test_game_scaled_sphere_query_recovery.py) use the
existing instruction runner and an
[independent rounded-float/evolving-memory reference](../../tools/tests/game_scaled_sphere_query_reference.py).
Both original retail and experimental C execute all real connected helpers,
not seeded replacement returns.

- 12,672 finite geometry cases vary six centers, four signed radii, two
  heights, four scale pairs, three direction forms, eleven output-alias
  layouts and two stack phases. Compare every non-stack memory byte, ordered
  external writes, status and all helper argument tuples.
- 4,096 ID/redirection cases cover every actor ID byte, all eight null masks
  and both stack phases. Non-null inputs redirect to the original private
  slots; null probes deliberately map ordinary guest address-zero storage.
  This is not language-defined native null-pointer behavior or an MMIO claim.
- 216 private-local output windows and 1,024 seeded finite input cases retain
  observable output/status/call behavior. The reference intentionally does
  not qualify complete private helper prologues/return-address bytes or equal
  raw instruction-read timing; those remain separate installation gates.
- A natural first point at incoming `SP+0xC` changes the first-point home to
  float-four bits and the second-point home to zero. Final Y writes go to the
  mapped `0x40800004` and `0x00000004`, both yielding 6.5 with inverse 0.5.
  Do not freeze the point pointers across the helper chain.
- Missing required storage fails on mapped-memory checks. Zero dimensions
  still reject without accessing origin/direction, scale or point storage.
- 25,344 actual 32-bit native calls run the selected caller and real C
  dimensions/normalizer/wrapper/sphere/dot bodies. Four ID boundary values,
  four radii, two heights, four scale pairs, six centers, three directions
  and eleven external aliases compare all 1,920 storage bytes and status to
  an independent native algorithm. All optional inputs are non-null; native
  private-frame/incoming-home aliases are not modeled. These new caller
  fixtures keep the vertical adjustment zero; the dedicated dimension suite
  separately covers its signed extrema.
- Four effective compiled negatives detect ordinary null fallback, a late
  actor inverse read, missing direction Y scaling and missing second-output
  Y rescaling. The late-inverse alias retains status one but changes first Y
  from `0x408360DB` to `0x4286D88A`, second Y from `0x40BC9F26` to `0x42C1999B`.
  Tests bind actual emitted effects, not source-only differences.

Observed original coverage: caller **109/110**, dimensions **40/41**,
normalizer **41/50**, wrapper **49/53**, sphere **126/126**, dot **13/13**.
Caller `+0x90` is an unreachable duplicate load after unconditional rejection
and before the preceding taken branch's destination. Helper counts reflect
the real connected domain, not complete instruction execution claims.
All helper linked slots are separately bound byte-for-byte to retail.

The ten new tests pass in **45.498 seconds**, zero skips/errors/failures.
No all-float/FCSR/NaN-payload, arbitrary invalid pointer, full private-helper
frame, hardware, gameplay, host adoption or installed caller acceptance claim.

## Retained Baseline And Resume

The fresh retained-ELF audit preserves all 6,059 slot bytes/addresses/extents,
protected sections, 720 Game-data owners/189,088 bytes and all 11,006 guard rows.
Conversion and matching counts remain unchanged: total 5,466/6,042 converted,
3,355/5,466 exact; Game 4,793/5,321 converted, 2,682/4,793 exact; 2,111 different,
zero drift. Main README aggregate rows are already current and stay untouched.
No production rebuild is needed or claimed for these opt-in experiments.

All **72 focused recovery/allocation/frame/wrapper/projection/owner-pool/
dimension tests pass in 273.813 seconds**, zero skips/errors/failures.
Project-tool smoke checks, Python syntax, whitespace and final retained-ELF
audit pass. Documentation gate: 69 documents, 3,789 relative links, zero broken.
No sibling, frozen Release, real save, runtime or push work.

Next: recover a fitting 110-word source form under the existing O2/g3 owner
profile while retaining these slots,
live homes, helper contracts and bounded behavior. Extend vertical-offset and
private/helper-frame/read-timing evidence, then classify only closed compiler
differences. Finish copied-owner/pools, actual padder/relocation/stale guards,
narrow installation, US ELF rebuild, whole-slot/data/history audit and regression
gates before claiming a match. Do not move to a smaller substitute target.
Sampler `func_151432BC` and oriented `func_15142600` remain open.

Ignored receipts: `conker/build/game-scaled-sphere-query/` and
`conker/build/game-scaled-sphere-query-test/`.
