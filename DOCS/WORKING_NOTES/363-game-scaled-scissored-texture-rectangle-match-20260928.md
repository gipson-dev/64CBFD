# Game scaled scissored texture rectangle match - 2026-09-28

## Result

`func_151E86E4` is byte-exact across all 175 words and 700 bytes at
`0x151E86E4..0x151E89A0`. Fresh linked totals are 2,866 / 5,468 (52.41%)
overall and 2,294 / 4,790 (47.89%) in Game.

## Recovered behavior

The function writes a scissored texture rectangle into a `Gfx` display list.
When `D_8008FE1C` differs from `1.0f`, it scales the horizontal coordinates by
that value, scales the vertical coordinates by `D_8008FE20`, and divides the
corresponding texture steps by the same horizontal and vertical factors.

The project-provided `gSPScisTextureRectangle` macro then clamps negative
rectangle coordinates to zero. For clipped upper-left coordinates, it adjusts
the starting texture coordinates according to the signed texture steps. It
emits the `G_TEXRECT`, `G_RDPHALF_1`, and `G_RDPHALF_2` commands and returns
the display-list pointer advanced by three `Gfx` entries.

## Compiler boundary

The semantic wrapper and existing graphics macro reproduce all 175 retail
words apart from one independent floating-register allocation. Current IDO
keeps `D_8008FE20` in `$f2`; retail keeps the same loaded value in `$f12`.
Four relocation-aware guard rows normalize the load and its three consumers.
They do not change a global address, arithmetic operation, branch, delay slot,
command word, or memory access.

The guard table has 1,532 rows with zero duplicate
`(filename, function, offset)` keys. Exactly four rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x215B64` and pristine retail span at
`conker.us.bin+0x215B94` compare equal for all 700 bytes. Both have SHA-256:

`5cb9c62ff81b996c5f05763db1290f2287e0c0b4b5e4fadb2da230c16f7ade0a`

The focused build, exhaustive guarded-object rebuild, relink, fresh linked
matcher, direct span comparison, guard-table integrity audit, replacement and
outer builds, project-tool checks, unit tests, and whitespace check pass.
Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Recover adjacent
819-word Game `func_151E89A0`, currently measured at 807 real differences in
the fresh linked queue, before changing its implementation.
