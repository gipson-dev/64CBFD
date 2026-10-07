# Game Vector-Basis Recovery And Liveness Audit

Date: 2026-10-07

## Scope And Baseline

Continue from banked matrix-list match `5a764e3a`. Recover `func_15146078`,
owner [game_16EE20.c](../../conker/src/game_16EE20.c), VA
`15146078..151462C8`, ROM `173528..173778`: **148 words / 592 bytes**.
It is retained original assembly, not a zero-return C placeholder. This audit
does **not** install the experimental C or claim another converted function.

## Recovered Behavior

The [candidate driver](../../tools/experiments/game_vector_basis_candidates.py)
retains a complete semantic body:

- Reject all-zero input, treating both zero signs equally; return zero without
  touching either output or calling a helper. Unused output pointers may be null.
- Count zero coordinates in a byte and retain the last zero/nonzero axis.
- For exactly two zero coordinates, emit two positive Cartesian unit vectors.
  Nonzero X selects Y/Z, nonzero Y selects X/Z, nonzero Z selects X/Y.
  The output stores are sequential, including when their storage overlaps.
- Otherwise start with axis indices 1/2, swapping to 2/1 only when Z is the
  single zero coordinate. Store `first[0] = first[firstAxis] = 1` in retail's
  actual first-zero-index-then-selected-index order.
- Preserve the expression `-point[0] - point[firstAxis] / point[secondAxis]`.
  Moving the addition inside the division is a different algorithm, even if
  it appears a more conventional perpendicular-vector construction.
- Run cross products `(first, point, second)`, then `(second, point, first)`;
  normalize first and second in place, sharing the private length/reciprocal
  outputs; return one. The helpers' sequential stores remain observable under
  input/output aliasing.

The original 29-word cross product at `151450B4` and 50-word normalizer at
`15145128` execute as connected original instructions in the guest tests.
Native fixtures use their actual recovered repository C bodies, not hooks.

## Early Byte Liveness

Retail loads `sp+0x46` when X is zero and `sp+0x45` when X is nonzero.
These loads really execute and require mapped storage; they must not be
explained away as unreachable instructions.

Their initial values do not feed a live public axis choice. When the nonzero
axis is consumed, exactly two coordinates were zero, so the remaining
coordinate assigned that axis. When the zero axis is consumed, exactly one
coordinate was zero, so that coordinate assigned it. Y/Z assignments overwrite
the speculative initial values on every route that subsequently uses them.
All-zero input returns before the byte loads.

The maintained tests vary every byte value independently at each of the two
private byte locations, all eight zero/nonzero patterns and both stack phases,
for retail and selected C: **16,384 fixtures**. They also verify the exact
route-specific read addresses and **28 removed-byte faults**. Initializing
the axes is a source-shape control, not a recovered retail initialization.

## Open Match Boundary

The best ordinary body emits **144 words / frame `0x48` / 93 raw differences**
under unchanged O2/g3/MIPS2, no pool or isolated diagnostic. It uses length
`sp+0x40`, reciprocal `sp+0x3C`, zero-axis byte `sp+0x3A` and nonzero-axis byte
`sp+0x39`. Retail requires `sp+0x34`, `sp+0x30`, `sp+0x45`, `sp+0x46`.

The missing four words concern the special axis cases: the compiler keeps
floating zero live in F0; retail compares against zero in F2, then freshly
loads zero into F0 in those cases. There are also open GP allocation,
constant-copy, return/store and comparison operand-order differences.
This is not a two-word scheduling-only problem.

**118 source/profile controls**, none raw byte-exact, cover byte/word types,
initialization, declaration order, explicit/chained stores, cached X,
assignment placement, per-case returns, constant precision, vector/array
views, boolean gate shape, output pairs, names/scopes, register/volatile
controls and four existing compiler profiles. Double-zero forms promote the
comparisons and expand the frame. A volatile initialized X reaches 148 words,
but adds real stack traffic and still has 99 differences; coincident length
is not a source match and volatility is not installed.

**1,320 ordinary nonoverlapping public-effect candidate executions** qualify
110 single-precision forms on twelve bounded inputs. These controls do not
receive store-order, private-layout, full-memory or complete-alias equivalence.
Four double-promoted forms and four profile controls are measurement-only.

Two explicit private-output overlap fixtures demonstrate different requested
output values between selected and retail. Consequently private-offset guards,
instruction insertion/omission or bulk word replacement would conceal a real
unrecovered boundary. No production source, profile, header or guard is changed.

## Maintained Qualification

[Ten recovery tests](../../tools/tests/test_game_vector_basis_recovery.py) bind:

- **3,456 guest cases**, 216 coordinate triples, eight sequential aliases,
  two stack phases, actual original helpers, independent binary32 final
  storage/write/call predictions, matching public read/write traces and
  preserved saved registers/F20. All **142 executable wrapper words** are
  covered; six unreachable/default-only words remain explicitly excluded.
  All 29 cross-product words and 41 normalizer words execute. Nine normalizer
  words belong to unused null-optional-output or unreachable routes.
- **432 complete original-caller cases**, all 25 `func_1514FB98` words,
  original callee, actual helpers, boolean gate and all seven forwarded ABI
  words to the following bounded `func_1514F8F8` hook. The hook is not claimed
  to implement that follow-on renderer.
- **1,728 freestanding 32-bit native cases**, actual selected C and both actual
  recovered helper bodies, bit-exact independent expected storage and fences,
  all eight aliases, strict warnings-as-errors and SSE binary32 operations.
- **416 float-pattern fixtures** covering zero signs, subnormals, infinities
  and quiet/signaling NaN bit inputs. Axis routes have exact output checks;
  all-equal general routes check classification/call order only. This does
  not establish FCSR exceptions or hardware NaN payload propagation.
- The private-byte sweep and removed-storage gates above, **16 zero-input /
  null-output fixtures**, two private-layout counterexamples and five compiled
  semantic negatives with actual output/return/call counterexamples. Unexpected
  faults are not accepted as negative detections.
- The production target remains its complete byte-exact original assembly,
  with no target guard rows. Measurement and qualification artifacts remain
  ignored under `conker/build/game-vector-basis*/`.

```sh
python3 -m tools.experiments.game_vector_basis_candidates --group lifetime
python3 -m tools.experiments.game_vector_basis_candidates --group registers
python3 -m unittest tools.tests.test_game_vector_basis_recovery tools.tests.test_game_vector_normalizer -v
make tools-check
```

All **19 combined recovery/normalizer tests pass in 114.064 seconds**, zero
skips/errors/failures. The earlier 112-control ten-test run passed in 124.582
seconds; the final run additionally includes all six register/volatile controls.
Tools, Python syntax and scoped whitespace checks pass. The documentation
checker verifies **82 documents / 3,958 relative links / zero broken links**.

Initial harness corrections fixed an incorrect relocation-container assertion,
the linked-ELF loader invocation and unclosed CSV stream. Helper coverage now
explicitly excludes the unused optional-output paths rather than claiming every
helper word. Ordinary chained-store controls check nonoverlapping final effects,
not retail store order; the selected body's separate alias/trace gate retains
that stricter requirement. Failed exploratory runs are not qualification.

## Linked Audit

The current US ELF snapshot is identical to the banked matrix-list snapshot:
**6,058 symbols / 6,042 retail slots / 16 overflow symbols / 11,061 guards**.
All bodies, addresses, extents, protected section hashes and conversion-file
hash stay unchanged. All **720 Game-data owners / 189,088 bytes** remain exact.
No rebuild was needed because production/build inputs were not edited.

Matching remains total **3,363 / 5,466 (61.53%)**, Game
**2,690 / 4,793 (56.12%)**, **2,103 different**, zero drift. Init remains
492/492 exact and Debugger 181/181 exact. Root README aggregates remain
unchanged; this audit's detail belongs here, not in the root README.

## Continue

1. Recover the ordinary source lifetime that allocates input X to F0 and
   comparison zero to F2, allowing fresh case-local zero loads. Do not count
   volatile-X length coincidence as progress toward retail shape.
2. Recover the real private scalar layout and second-axis constant materialization
   in C. Re-run the private overlap counterexample before considering guards.
3. Once all 148 words, frame and scalar offsets are recovered, qualify copied
   owner neighbors/pools, actual padder, four rebased call relocations and a
   full linked audit before installation or conversion-count updates.
4. Translator `func_15142314` scheduling and sampler `func_151432BC` per-path
   RA/RNG lifetime remain open; no new claim for either in this audit.

No sibling port, frozen Release, real-save, runtime, hardware or push action.
