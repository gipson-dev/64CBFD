# Game Area Sampler Qualified Recovery

Date: 2026-10-06. Baseline: `f6198eeb`,
[Note 1073](1073-game-point-transform-assembly-to-c-match-20261006.md).
Recover and qualify `func_151432BC` without installing an incomplete match.
Production source, compiler profiles, shared headers, guard CSV and root README
remain unchanged. This checkpoint adds no converted or byte-exact function.

## Recovered Contract

Retail: 254 words / 1016 bytes, frame `0x50`, VA `151432BC..151436B4`,
ROM `17076C..170B64`. Five inputs: descriptor, x output, z output, upper-y
output, lower-y output. The fifth argument arrives in the caller's stack home.
The routine has no meaningful return value. The production zero-return stub
and its false no-argument declaration are still present until matching closes.

The local descriptor must use signed halfwords at offsets `0,2,4,6,8,A`:
x, y, z, radius, height, width. Angle at `0x10` is a float; flags at `0x15`
are an unsigned byte. Existing shared `struct208` instead has unsigned
halfwords and an integer at `0x10`; do not reuse it or broadly modify it.
The candidate uses a local 24-byte descriptor and the existing 48-byte
`struct209` scratch layout. Low two flag bits select the path once.

| Mode | Ordered Calls | Outputs |
| --- | --- | --- |
| 0 | Integer RNG, shifted angle helper, direct angle helper, float RNG | Radial x/z; top y+height; bottom y |
| 1 | Integer RNG, shifted angle helper, direct angle helper, float RNG | Radial x/z; top y+height; bottom y-height |
| 2 | Shifted angle helper, direct angle helper, two float RNG calls | Rotated rectangular x/z; top y+height; bottom y |
| 3/default | None | Descriptor x/z; top y+height; bottom y-height |

The first angle sample calls `func_151423D8` with `(angle-64)&255`; the second
uses the retained angle byte. The actual table runs from1 to0 over a quadrant:
the direct sample is cosine-shaped, not sine-shaped. Keep the shifted/direct
names in the reference to avoid reversing these two inputs.
Modes 0/1 retain the low byte of the full-width integer RNG result.
Mode 2 multiplies the float angle by `D_800A5644`, converts to unsigned 32-bit
integer, then retains its low byte. Preserve that unsigned conversion rather
than substituting a signed cast. The original conversion saves/restores FCSR,
tries signed conversion, then subtracts `2^31` for the unsigned upper half,
and uses `FFFFFFFF` on its modeled invalid paths.

Descriptor fields remain live after callbacks and between output stores.
Callback mutations and output/descriptor aliases can affect later results.
Vertical sums/differences are signed integer operations before float conversion.
Do not cache all fields or all four output results at entry. Arithmetic uses
separately rounded float operations, not fused multiply-add.

## Compiler Evidence

[Maintained driver](../../tools/experiments/game_area_sampler_candidates.py):
38 forms across four SDK profiles, 152 measurements. Controls cover the
commented-draft if chain, switch/local selector, masks, float-double shape,
scratch order, early returns, tangent temporary, goto exits, RNG temporaries,
separate samples, signed flags, volatile scratch/angle fields, integer scaling
and explicit radius casts. None emits an exact slot.

The selected switch/early-return form emits **252 words, frame `0x50`,
109 raw positional differences** under unchanged O2/g3. There is no new pool.
The copied production owner emits identical target bytes/relative relocations.
This is not merely a standalone translation-unit artifact.

Most positional differences are consequences of two shortened block exits:

- Retail mode 2 stores bottom-y at `15143504`, branches at `15143508`,
  and reloads RA in its delay slot at `1514350C`. Candidate branches at
  `15143504`, stores bottom-y in the delay slot, and shares the final RA load.
  The next block therefore starts four bytes earlier.
- Retail mode 0 likewise stores bottom-y, branches and reloads RA in the
  delay slot at `151435CC/D0/D4`. The candidate again shares the final RA load.
  Mode 1 and the common epilogue start eight bytes earlier.
- Both circle paths also schedule the RNG-byte store differently. Retail
  stores a0 before subtracting 64; C stores the retained v0 after subtract/mask.
  The byte, helper ABI and public behavior agree, but the instructions do not.

Integer scaling recovers the 254-word count but has 158 positional differences
and changes the emitted arithmetic sequence. Reject it as a match. Sixteen
disposable break/return combinations also retained the 252-word result;
those redundant exit controls are not part of the maintained 152-form sweep.
No instruction insertion, block shifting, frame rewrite or broad word guards
are installed to hide the discrepancy.

## Qualification

[Ten maintained tests](../../tools/tests/test_game_area_sampler_recovery.py)
pass in 18.864 seconds, with no skips, errors or failures:

- 1024 independent-reference cases compare raw C and retail instructions:
  all modes/high flag bits, signed halfword extremes, zero dimensions, two
  stack phases, full-width RNG values, callback mutations and four output/
  descriptor alias arrangements. Ordered output writes, external memory,
  helper arguments and preserved GPR/FPR/SP/RA agree. Private traces and
  private scratch/home bytes are not asserted identical.
- 48 guest-only conversion cases exercise both integer stages, negative,
  infinite/NaN and out-of-range inputs, with selected incoming control words.
  FCSR restores before callbacks and return in the bounded model. Retail word
  `151433F0` is unreachable through these original conversion branches.
  Negative fractions between -1 and 0 truncate to zero rather than taking the
  failure path. Together with three ordinary-mode coverage probes, these
  cases cover all 251 reachable candidate words and 253 reachable retail words.
- 1536 cases execute all 27 original angle-helper words, every angle byte
  and both stack phases. The real 65-word lookup table comes from linked
  exact Game data; RNG results remain explicitly bounded models.
- 64 cases execute the complete 20-word original caller `func_151A8F1C`,
  sampler and original angle helper. Verify descriptor indirection, x/z
  output spacing, fifth argument and the caller's final upper-y copy.
- 256 freestanding 32-bit native typed-caller cases use the actual current
  angle-helper C body, finite nonnegative unsigned-cast inputs, output aliases
  and callback mutations. Verify descriptor/scratch sizes and field offsets.
  Do not execute undefined native negative/NaN/out-of-range unsigned casts.
- Six compiled negatives are rejected through external results/calls, not
  differences in private frames: stub, signed conversion, wrong shifted angle,
  wrong lower bound, unsigned halfwords and wrong rectangle span.
- Copied owner retains all 89 typed function symbols, all 88 neighbors'
  bytes/relative relocations, the 624-byte relocation-owned pool and the same
  two warnings. Missing required bytes fail closed; default mode does not
  access RNG, angle data or the angle multiplier.

The local conversion model handles truncation and the invalid flag needed by
these instruction paths. It is not general FCSR/exception/rounding-mode
emulation or hardware acceptance. Other whole callers, real RNG execution,
argument-home mutation, gameplay and 64-bit host adoption remain unqualified.

## Resume Steps

1. Recover the two retail per-path RA reloads through legitimate C lifetime/
   exit shape, retaining the current frame, arithmetic and unsigned conversion.
2. Recover the circle RNG-byte store schedule without changing the full-width
   RNG prototype or adding volatility to unrelated fields.
3. Re-run the maintained compiler sweep and ten behavioral tests. Once the
   complete slot shape agrees, qualify actual owner padding, relocation carries
   and any strictly limited expected-word guards before installation.
4. Replace only this stub/local declaration, retain the original assembly
   reference, rebuild and audit every linked slot/data owner/guard. Refresh
   aggregate progress only after a genuine production change.

## Checkpoint Receipt

The full maintained sweep measures 152 controls with no exact candidate.
Final sampler/point-transform/pool regression: 24 tests pass in 34.986 seconds,
zero skips/errors/failures. All 6059 linked slots, addresses/extents, protected
sections, 720 exact Game-data owners and 10842 guard rows remain the Note 1073
baseline. Copied-owner warning count remains two, with no new warning.
Tool and syntax checks pass; 56 documents / 3633 relative links / zero broken.
No production rebuild is needed for this tools/documentation-only checkpoint.

Matching totals stay Game2673/4792 exact (55.78%), 2119 different, zero drift;
converted Game4792/5321 (90.06%). Root README is untouched because no aggregate
changed. The previous 92-test post-link receipt remains historical; this turn
ran the focused 24-test regression, not a new 92-test suite.

Ignored receipts: `conker/build/game-area-sampler/` and
`conker/build/game-area-sampler-test/`. No sibling project, frozen Release,
save/runtime state or push. The Game matching goal remains active.
