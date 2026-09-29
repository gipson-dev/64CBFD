# Game optional-callback teardown pair byte match

Date: 2026-09-29

## Scope and behavior

`func_151A8584` and `func_151A85D4` in
`conker/src/game/generated_1D4E00.c` occupy adjacent 20-word, 80-byte spans at
`0x151A8584..0x151A85D4` and `0x151A85D4..0x151A8624`.

Both routines select an optional callback with the object byte at offset
`0x5C`. The first uses table `D_8008F94C`; the second uses `D_8008F958`. If
the selected entry is non-null, it is called before the shared
`func_151A8560` teardown. The routines then finish through distinct callbacks:
`func_15169804` and `func_15169824`, respectively.

## Compiler shape

Retail invokes the table entry without explicitly preparing an argument. The
incoming object remains in physical register `a0`, so the recovered table type
uses an old-style callback contract and calls the entry with no explicit C
arguments. The indirect-call delay slot saves `a0` only on the callback path;
the object is reloaded afterward and saved again in the shared teardown call's
delay slot for the final call.

IDO instead spills the object before the table lookup and reloads it through a
temporary. Each function therefore uses one expected-word omission for that
extra spill and ten guarded words to restore the selector registers, table
relocation, null branch, indirect call, and path-sensitive spill/reload order.
The frame, saved return address, both direct call relocations, final object
reload, and complete epilogue emit directly from semantic C. The two guard
sets are independent and name each function's distinct table and final call.

## Verification

- The focused generated-slice object builds with both complete retail
  instruction sequences.
- The complete ELF relink passes.
- Direct linked comparison reports zero differences in both 80-byte spans.
- `func_151A8584` shares retail SHA-256
  `0cddd7a739041989c01637e7f6cf128c15a6546ed7774eb55c6af2430650b3dd`.
- `func_151A85D4` shares retail SHA-256
  `51544c0fe63745d31a8fad4928ae9ff643e5c4d4ae4fbf9f13e495cc1e801dfe`.
- The authoritative matcher omits both functions from its non-exact list and
  reports `2,986 / 5,465 (54.64%)` overall and `2,411 / 4,789 (50.34%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game row. `func_1506EF5C` is now the
smallest non-exact Game function by real-word difference count; keep the
documented jump-table, handwritten-register, and Init SDK cases parked.
