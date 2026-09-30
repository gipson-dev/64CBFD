# Game object-selector payload-wrapper twin byte match

Date: 2026-09-30

`func_151B1AB0` occupies 33 words and 132 bytes at
`0x151B1AB0..0x151B1B34`. It is the structural twin of `func_15192920`: null
owners are ignored, while a non-null owner contributes its pointer and byte at
offset `0x3B` to a 12-byte local payload whose final word is `0.0f`. The
function requests a record from `func_151491F4` with arguments
`(0x3C, -1, 0x15, 1, 0x11, 0x0C, 0xFF, 1)` and copies the payload to record
offset `0x28` when allocation succeeds.

The proven declaration order and volatile incoming pointer recover retail's
exact `0x38` frame, duplicate argument-home loads, and local payload slots at
`sp+0x28`, `sp+0x2C`, and `sp+0x30`. The only semantic differences from the
earlier twin are command type `0x3C`, overflow value `0x11`, and third argument
`0x15`.

Sixteen words emit directly from semantic C. Seventeen independently scoped,
stale-checked, non-relocating guards normalize the same closed IDO schedule as
the earlier twin. Retail performs the second owner load before preparing call
arguments, fills the payload before the overflow arguments, and stores the
selector before the allocation call with the zero float in its delay slot.
Branches, call relocations, values, local offsets, and failure behavior remain
unchanged.

The focused object, complete replacement link, outer `NON_MATCHING=1` ROM
build, and authoritative matcher pass. The linked ELF and pristine
decompressed retail spans share SHA-256
`244442f6df0e8eb0c7d7de8476d15861a355f5a958ab34ebbb0c4a24c2c26977`.
The matcher advances exactly one row to `3,067 / 5,462 (56.15%)` overall and
`2,488 / 4,788 (51.96%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
35-word Game `func_151CEA20`, the next ordinary matcher row.
