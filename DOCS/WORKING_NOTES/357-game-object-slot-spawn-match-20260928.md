# Game object-slot spawn match - 2026-09-28

## Result

`func_151E7F60` is byte-exact across all 163 words and 652 bytes at
`0x151E7F60..0x151E81EC`. Fresh linked totals are 2,860 / 5,468 (52.30%)
overall and 2,288 / 4,790 (47.77%) in Game.

## Recovered behavior

The function releases the previous object in the selected `D_800E0BA0` slot,
allocates a descriptor, and fills it from the indexed `D_800AB57C` object
entry and `D_800AB940` position entry. The position index advances once when
the current mode byte is seven. Descriptor type `0x24` is selected for object
ID `0x53`; all other IDs use type `0x0E`.

After object creation, the one-based result selects `D_800CC2D0[result - 1]`.
The function stores that object in the slot, sets its state byte and flags,
copies the table scale to both scale fields, and optionally allocates and
zeroes a `0x1C0`-byte auxiliary block for IDs zero and `0x80`. Table object ID
`0x3B` receives the one-based slot tag. The table setup byte and animation
setup call complete initialization.

## Compiler boundary

The semantic C emits all substantive retail operations, registers, branches,
calls, global addresses, and instruction order. IDO chooses an 88-byte frame
for the recovered local layout while retail uses 80 bytes. Twenty-four guarded
words normalize only the frame size and the resulting argument/local stack
offsets; they do not replace behavior, control flow, registers, relocations,
or call targets.

The guard table has 1,511 rows with zero duplicate
`(filename, function, offset)` keys. Exactly 24 rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x2153E0` and pristine retail span at
`conker.us.bin+0x215410` compare equal for all 652 bytes. Both have SHA-256:

`f4cfd6fbbab3328dad19b95e18360a746ca00efd75770c63d0d54cca12644440`

The focused object build, exhaustive relink, fresh linked matcher, direct span
comparison, guard-table integrity audit, broader replacement and outer-ROM
builds, project-tool checks, all unit tests, and whitespace check pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Recover adjacent
41-word Game `func_151E8214`, currently measured at 39 real differences in the
fresh linked queue, before changing its implementation.
