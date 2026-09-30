# Game scripted-position effect dispatcher match

Date: 2026-09-30

`func_15076768` occupies 35 words and 140 bytes at
`0x15076768..0x150767F4`. The former zero-return placeholder is replaced with
the routine's semantic mode dispatch. Mode zero forwards the current actor at
`D_800D154C` to `func_15197A7C`. Mode one copies the actor's X and Z
coordinates into a local position, fixes Y at `-390.0f`, derives a nine-word
descriptor through `func_1504715C`, and calls `func_1514B364` with effect
arguments `0xFF` and zero. Other modes perform no action.

The recovered `void` return type and typed helper declarations reproduce the
retail frame, mode branches, floating-point constant, actor field accesses,
both call relocations, argument setup, and epilogue. Thirty of 35 words emit
directly from semantic C. The remaining five words are one closed independent
schedule: retail stores Y and X, loads and stores Z, then forms the descriptor
address in the first helper's call-delay slot. IDO instead forms that address
before the three position stores. Five stale-checked, non-relocating guards
preserve retail's ordering without changing the recovered behavior.

The focused object, exhaustive guard-dependent rebuild, complete relink,
authoritative matcher, and direct span comparison pass. The linked ELF and
pristine decompressed retail spans share SHA-256
`d67a510fcc3d0c50ccfad8e060acdc820a3c1fb2ce8bfa38a1304ccf5c60429b`.
The matcher advances exactly one row to `3,073 / 5,461 (56.27%)` overall and
`2,494 / 4,788 (52.09%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
35-word Game `func_1507F4C0`, the next ordinary matcher row.
