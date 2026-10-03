# Game Look-At Matrix: Semantic Recovery

Date: 2026-10-03. Baseline: `e794a42`.

## Result

`func_15047390` replaces its empty body with the complete semantic look-at
matrix builder. Local libultra `tools/ultralib/src/gu/lookat.c` (`guLookAtF`)
provides the established basis/translation algorithm. Full retail assembly
inspection establishes additional exact-zero normalization fallbacks that
must not be omitted by copying the stock SDK body unchanged.

This recovery remains non-matching: 188 body words plus two padding nops fill
the 190-word / 760-byte slot, with 171 differences. The emitted frame is
`0x70`, versus retail `0x50`; register/stack allocation and scheduling still
need matching work. No new word guards, compiler profiles, or assembly
substitutions were introduced. Aggregate coverage/matcher totals are unchanged.

## Recovered Contract

1. Call `guMtxIdentF` first. Arguments are passed by value and survive helper
   mutation of the caller's parameter storage.
2. Compute target minus eye, call `sqrtf` on its left-associated squared norm,
   replace the returned length only when exactly equal to zero, and normalize
   with `-1.0f / length` for the SDK positive-Z-behind-camera convention.
3. Compute right as up cross look, normalize with `1.0f / length`, and apply
   the second exact-zero fallback. Recompute up as look cross right and apply
   the third normalization/fallback.
4. Publish basis columns and negative eye-dot-basis translation. Explicitly
   publish the final column `(0,0,0,1)` after the helper calls.

Negative zero satisfies the fallback comparison. Small nonzero lengths are
not clamped. NaN does not satisfy the zero test; do not introduce defensive
sanitization or fallback axes that change retail behavior.

The three fallback words at `D_80098D60`, `D_80098D64`, and `D_80098D68`
are all `0x3A83126F`, approximately `0.0010000000474974513`, independently
read from retail ROM offsets `0x23D820`, `0x23D824`, and `0x23D828`.
They remain distinct globals and are loaded after the corresponding helper
returns. Single-precision division reflects the original `div.s` operations.

The SDK header makes `sqrtf` intrinsic. A bounded `#pragma function sqrtf`
before this body and restored `#pragma intrinsic (sqrtf)` after it preserve
the three original helper-call boundaries without changing other routines.
This follows the existing directive convention in `game/done/game_75950.c`.

## Linked Measurement

| Item | Measured result |
| --- | --- |
| Guest interval | `0x15047390..0x15047688` |
| Retail ROM interval | `0x74840..0x74B38` |
| Slot | 760 bytes / 190 words |
| Emitted body / padding | 188 words / 2 nops |
| Different word positions | 171 |
| Following symbol | `func_15047688 = 0x15047688`, unchanged |
| SHA-256 of recovered slot | `a51dfba63390629a82930451adc2ade4c1d2bb277813c89181ed588f650d6f06` |

The linked body contains ordinary `sqrtf` calls at `0x15047400`,
`0x150474A4`, and `0x15047544`. These are recovered-code call locations,
not the retail locations. The separate 120-byte fixed-matrix wrapper remains
byte-exact with SHA-256
`0cdac7420c30fb7ffb285532cd9eb11efa7e9393128437b51f3561c5670edace`.

## Verification

Twelve source-extracted freestanding 32-bit tests in
`tools/tests/test_game_look_at_matrix.py` compare the actual body with an
independent vector/matrix reference using SSE single-precision square root.
Tests check an axis-aligned camera, 128 general cameras, orthonormality,
eye-to-origin transformation, coincident eye/target, zero/parallel up vectors,
small nonzero lengths, each zero/negative-zero fallback, post-helper constant
loads, NaN propagation, by-value parameters, complete matrix publication after
helper mutation, and the actual fixed-matrix wrapper's float-matrix handoff.

Identity and square-root helpers are instrumented; square roots normally use
hardware `sqrtss`, with selected return overrides to isolate fallback behavior.
`guMtxF2L` is a capture mock in the wrapper test. Numerical comparison uses
relative/absolute tolerance `1e-5`; it is not a MIPS floating-point bit-parity
claim, validation of the conversion helper, or rendered camera acceptance.

Commands completed successfully:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest tools.tests.test_game_look_at_matrix
python3 -m unittest discover -s tools/tests
make tools-check
```

All 374 repository tool tests pass. Nineteen prior exact neighbors remain
retail-identical, as does the fixed-matrix wrapper. Six prior non-matching
actor/terrain/entity hashes remain unchanged. The 5,712-byte collector,
504-byte producer, and 16-byte return closure remain exact. Both complete
Init sections match retail with the lengths/hashes in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).
No host-port build, compressed-ROM build, guest execution, or gameplay test
was performed.

## Progress / Next

Inventory remains total 5,463 / 6,042 C rows (90.42%), 1,931,472 / 2,256,728
C bytes (85.59%); Game 4,790 / 5,321 C rows (90.02%), 1,760,036 / 2,072,880
C bytes (84.91%). Matcher remains total 3,268 / 5,463 exact (59.82%) and Game
2,595 / 4,790 exact (54.18%). Zero drift; 2,195 different C rows remain.
README and aggregate tables are unchanged; detailed updates stay in DOCS.

Next recover empty reflection look-at builder `func_15047700`. A local
`guLookAtReflectF` reference exists in `tools/ultralib/src/gu/lookatref.c`.
Its retail opening contains an explicit eye/target equality test, so inspect
the complete edge-case branch, normalization, `LookAt` byte publication, and
matrix-store contract before implementing. Do not assume it is identical to
the stock SDK reference or simply reuse this routine's zero-length guards.
This matrix builder's byte matching and guest/runtime qualification remain
open alongside actor/terrain/entity matching.
