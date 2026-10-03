# Game Reflection Look-At Matrix: Semantic Recovery

Date: 2026-10-03. Baseline: `5e33a49`.

## Result

`func_15047700` replaces its empty body with the complete reflection look-at
matrix builder and `LookAt` direction/color publication. The local SDK
`tools/ultralib/src/gu/lookatref.c` establishes the basis/translation algorithm;
the complete retail interval in `conker/asm/71820.s:3663` establishes additional
degenerate-vector branches. Copying stock `guLookAtReflectF` unmodified would
omit those branches. This implementation uses the existing `LookAt` type and
`FTOFRAC8` graphics macro, without a new math abstraction.

The result is a semantic recovery, not a byte-exact match. The emitted body
is 282 words plus six padding nops in the 288-word slot, with 245 differing
word positions. Frame size is `0x78`, versus retail `0x68`. No new compiler
profile, word guard, or assembly substitution was added.

## Retail Contract

1. Call `guMtxIdentF` first, then compute target minus eye. If `xAt == xEye`
   and both Y/Z differences equal zero, substitute look `(0,0,1)` before
   normalizing with `-1.0f / sqrtf(squared_length)`. Preserve the original
   X comparison; do not silently replace it with a generic epsilon test.
2. Compute right as input up cross normalized look. Test its squared length
   before square root. A nonzero squared length takes normalization; zero
   selects right `(1,0,0)`. Underflow of a nonzero vector's squared length
   also selects this fallback.
3. Recompute up as look cross right. Again test squared length before square
   root. Zero selects up `(0,1,0)`; otherwise normalize. These branches are
   not the three post-square-root constant fallbacks in `func_15047390`.
4. Convert right/up to six signed direction bytes through `FTOFRAC8`:
   multiply by 128, upper-clamp to 127 using the SDK comparison, truncate
   toward zero, and retain the low byte. There is no extra lower clamp.
   NaN fails the less-than comparison and selects 127 before conversion.
5. Set each light's first eight bytes, with the second light's green and
   copied-green bytes set to `0x80`; other color and explicit pad1/pad2 bytes
   are zero. Do not clear pad3 or the union's four trailing bytes per light.
6. Publish basis columns, negative eye-dot-basis translation, and the final
   column `(0,0,0,1)`. Parameters remain passed by value across the identity
   helper. The fixed wrapper passes the float result to `guMtxF2L`.

The three square roots compile as intrinsic `sqrt.s` operations, consistent
with retail. No helper-call boundaries or artificial guards are introduced.
Negative zero satisfies the zero comparisons. NaN does not take a zero-length
fallback. Coincident cameras therefore differ intentionally from the earlier
look-at builder. A degenerate +X look/zero-up combination can select both
fallback axes even though the resulting basis is not orthogonal; no corrective
axis choice absent from retail was added.

## Linked Measurement

| Item | Measured result |
| --- | --- |
| Guest interval | `0x15047700..0x15047B80` |
| Retail ROM interval | `0x74BB0..0x75030` |
| Slot | 1,152 bytes / 288 words |
| Emitted body / padding | 282 words / 6 nops |
| Different word positions | 245 |
| Following symbol | `func_15047B80 = 0x15047B80`, unchanged |
| Recovered slot SHA-256 | `6f418d9398b2f8924cf84cc8088fa10c9fe5f42c049eb996ff814c8758bff497` |

The fixed wrapper's complete 128-byte slot remains exact, including two padding
nops after its 30-word body. SHA-256:
`96f8a653366d399cc78995298c69c600c4845bf2b1dd7d8d4a60df4497feacca`.
The preceding look-at slot retains its 171 differences and prior hash from
[Note 781](781-game-look-at-matrix-semantic-recovery-20261003.md).

## Tests And Regression

Fourteen tests in `tools/tests/test_game_reflection_look_at_matrix.py` extract
the actual production builder and fixed wrapper. The host fixture mirrors the
SDK's 16-byte Light / 32-byte LookAt layout and extracts the actual MIN and
FTOFRAC8 definitions from the repository header. Its separate vector reference
checks all sixteen matrix values and all thirty-two light bytes.

Coverage includes an axis-aligned camera, 128 general cameras, orthonormality
and eye-to-origin mapping for a regular camera, coincident eye/target,
X equality without coincidence, zero/parallel up, simultaneous right/up
fallbacks, squared-length underflow, direction truncation, full colors and
untouched padding, negative-zero coincidence, NaN behavior, by-value arguments
through identity-helper mutation, and the actual fixed-wrapper handoff.

Host numerical comparison uses SSE single-precision square root and a `1e-5`
relative/absolute tolerance. The identity helper is instrumented; the host
sqrt function counts operations in the source fixture, not retail helper calls.
`guMtxF2L` is a capture mock. These tests do not prove MIPS floating-point bit
parity, conversion-helper correctness, arbitrary overlapping output buffers,
invalid/out-of-range float-to-integer conversion, or rendered acceptance.

Completed successfully:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest tools.tests.test_game_reflection_look_at_matrix
python3 -m unittest discover -s tools/tests
make tools-check
```

All 388 repository tool tests pass. Nineteen earlier exact routines and both
matrix wrappers remain retail-identical. Seven previous non-matching slot
hashes (look-at, actor result, four entity queries, and terrain query) remain
unchanged. The 5,712-byte collector, 504-byte producer, and 16-byte return
closure remain exact. Both complete Init sections independently match retail:
164,048 code bytes and 17,376 data bytes, with the hashes in
[Note 782](782-init-pause-resume-conversion-assessment-20261003.md).

## Progress And Next

Aggregate inventory and matcher totals are unchanged: 5,463 / 6,042 C rows;
3,268 / 5,463 exact; zero drift and 2,195 different C rows. Game remains
4,790 / 5,321 C rows and 2,595 / 4,790 exact. The empty body was already
counted as C, so README tables are unchanged; detailed progress stays in DOCS.

The trailing matrix pair completes this slice's two empty matrix-builder
recoveries, not the entire slice. Next inspect the earlier placeholder cluster
beginning with `func_15044380`, especially its actor-preparation dependency
`func_15044660`, before claiming the dispatcher is functional. Recover actual
signatures, actor fields, context iteration and helper contracts from full
assembly; do not preserve the zero-return prototypes as recovered interfaces.
Matrix/actor/terrain/entity byte matching remains open. Init's two small leaves
remain deferred under Note 782; this is not a new Init conversion.

No compressed-ROM build, guest execution, host-port build, or gameplay test
was performed. The sibling port and frozen Release artifacts were untouched.
