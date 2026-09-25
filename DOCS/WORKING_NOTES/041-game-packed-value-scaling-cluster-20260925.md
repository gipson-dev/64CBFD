# Game packed-value scaling cluster - 2026-09-25

## Result

`func_1516F8EC`, `func_1516F91C`, and `func_1516F984` are byte-exact across
their complete 12-, 12-, and 16-word linked extents. The fresh C-only matcher
reports `2558 / 5489 (46.60%)` overall and `1990 / 4800 (41.46%)` game. One
init function remains blocked by address drift; 2,930 total and 2,810 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Twin packed-byte scalers

`func_1516F8EC` and `func_1516F91C` contain the same operation at neighboring
field pairs: combine a signed high byte and unsigned low byte, scale the
packed value, then store its shifted high and low bytes. Each maintained C
body had the correct 12-word structure and multiplication behavior but used
`t6`/`t7` for the opposite pre-multiply values and `v1`/`t8` instead of
retail's `t0`/`t9` post-multiply chain.

Reversing the commutative packing expression and introducing an explicit
shifted result were inert. Explicit high and shifted lifetimes were also
optimized back to the same object. Those experiments were reverted. Six
expected-word-guarded, non-relocating normalizations per function now select
the two identical retail temporary chains while preserving the compact C.

## Scaled field wrapper

`func_1516F984` calls `func_1516F94C`, scales the signed field at offset
`0x18`, shifts it by eight, and stores it back. The compound source expression
allocated the reloaded factor, field value, product, and shifted result to
`t7`, `t6`, `t8`, and `t9`. Splitting the expression into explicit load,
multiply, shift, and store assignments gives retail's `t6`, `v0`, `v0`, and
`t7` lifetimes naturally. No guarded patches are used for this function.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_19A8B0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

All three targets are absent from the non-exact list. The patch table has 512
rows and no duplicate filename/function/offset keys. Independent complete-span
linked/retail SHA-256 values are:

| Function | Bytes | SHA-256 |
| --- | ---: | --- |
| `func_1516F8EC` | 48 | `14f75b532b0413ab490bcefb7a8284c1b024c1f476b4d4ec44fd8863a6faf20c` |
| `func_1516F91C` | 48 | `945027373a1829e0654f87630cee13b194b1c9dbc9223732fe401112ae258580` |
| `func_1516F984` | 64 | `b5801f5ad4d78f055901441ec1f91ee55401dae43b813741b7d87d3b5a2ba1c5` |

The `64CBFDOGL` sibling contains these functions only in generated recomp
output and symbol configuration. These IDO source/allocation changes do not
transfer to hand-maintained host source. Its dirty worktree was left
untouched, and its frozen Release configuration was not built or launched.

## Next boundary

The six-difference game queue is complete. The next listed game target is
68-word `func_15019BB8` with seven real differences, followed by 14-word
`func_1509F6B0` and 14-word `func_150C7930` in the same tier.
