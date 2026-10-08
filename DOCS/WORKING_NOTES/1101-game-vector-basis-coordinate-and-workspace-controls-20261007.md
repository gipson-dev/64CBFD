# Game Vector-Basis Coordinate And Workspace Controls

Date: 2026-10-07

## Scope

Extend [Note 1100](1100-game-vector-basis-recovery-and-liveness-audit-20261007.md)
from banked `ce7fc332`. The target remains `func_15146078`, its original
148-word assembly in [game_16EE20.c](../../conker/src/game_16EE20.c).
This is an experimental-source audit, not an installed conversion or match.
The adjacent lighting-dispatch recovery is a separate batch.

## Additional Controls

The [driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_vector_basis_candidates.py) adds
68 meaningful source forms to the existing 118 source/profile controls:

- 32 coordinate forms: cached Y/Z classification, a named quotient, nested
  all-zero gating and X initialization versus assignment. All remain 144 words;
  frames are `0x48` or `0x50`, with no improvement over the 93-difference fit.
- 12 workspace forms: a local record containing all eight genuinely used
  fields, with natural padding only. These emit 161 words/frame `0x40`/153
  differences. The record is a source-shape experiment, not an inferred
  original datatype. Extra byte stores do not recover retail's scalar layout.
- 24 seed-expression forms: explicit X refresh after the first output stores,
  named numerator/denominator/quotient and assignment placement. These emit
  144 words/frame `0x48` or `0x50`, with 93 or 94 differences.

All **186 controls** remain raw nonmatching. The selected experimental body
stays **144 words / frame `0x48` / 93 differences**. The four missing words,
floating-zero lifetime and private scalar offsets from Note 1100 remain open.
No guard, volatile installation, insertion, omission or private-offset patch
is justified by these measurements.

## Qualification

The [maintained recovery suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_vector_basis_recovery.py)
now executes **2,136 ordinary nonoverlapping candidate fixtures**, up from
1,320. This qualifies public effects for 178 single-precision controls on
twelve bounded inputs. Four double-promoted forms and four compiler-profile
controls remain measurement-only. It does not promote every control to
store-order, full-alias or private-layout equivalence.

The selected-body gates from Note 1100 also re-pass: original connected
cross-product/normalizer instructions, full public traces, actual native helper
C, complete original caller, private-byte liveness, required storage and both
private-output overlap counterexamples. The installed basis assembly is still
byte-exact; no basis production source, profile, header, guard or README
aggregate changed.

```sh
python3 -m tools.experiments.game_vector_basis_candidates --group coordinates
python3 -m tools.experiments.game_vector_basis_candidates --group workspace
python3 -m tools.experiments.game_vector_basis_candidates --group seed
python3 -m unittest tools.tests.test_game_vector_basis_recovery tools.tests.test_game_vector_normalizer -v
```

All **19 tests pass in 151.122 seconds**, zero skips/errors/failures.
Continue the ordinary floating-zero lifetime and real private scalar layout
recovery before replacing the original assembly. No sibling port, frozen
Release, real-save, runtime, hardware or push action.
