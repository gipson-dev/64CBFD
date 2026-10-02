# Init audio subframe builder match

Date: 2026-10-01

`func_1001FB40` occupies 296 words and 1,184 bytes at
`0x1001FB40..0x1001FFE0`. Its previous compiled body returned zero even though
the audio frame path uses it to build the command stream for every configured
auxiliary bus.

The recovered routine optionally lets `func_151F2E88` supply the opening
commands, otherwise clears the main and auxiliary output buffers. It finds the
last auxiliary bus with an active effect, rotates that selection across all
configured buses, and invokes the main-bus filter handler for each subframe.
It then emits the original mixer commands selected by `D_800428C4` and
`D_800428C6`.

When the selected bus has an active effect, the routine refreshes deferred
effect state through `func_1001CF38`, emits the ADPCM-table and two pole-filter
commands with physical state addresses, and clears the refresh flag. The
returned pointer is the first free audio command after the complete subframe.

The decisive source recovery was the original SDK command-macro shape.
`aClearBuffer`, `aMix`, `aLoadADPCM`, and `aPoleFilter` reproduce the retail
block-scoped command temporaries, stack slots, stores, and two unfilled branch
delay slots. Keeping both loop updates in the second `for` increment clause as
`i++, selectedBus++` reproduces the retail footer schedule. The resulting
`-g` compact object is exactly 296 words and matches every retail word and
relocation directly from C. No expected-word guards, inserted words, or
function-specific object overrides are used.

The normal padded-object build and complete linked ELF both match. Direct
comparison of `0x1001FB40..0x1001FFE0` reports zero different bytes. Both
1,184-byte spans share SHA-256
`092c988cb1f4f75ee8947a2e663b9b103ce8eaf84ccc12a28ca1ea2f0392f145`.
The full repository relink, focused tool checks, and `git diff --check` pass.

The matcher advances to `3,157 / 5,456 (57.86%)` byte-exact C functions
overall and `474 / 487 (97.33%)` in Init, with zero address drift and 13
different Init C rows. The next smallest measured Init candidate is the
280-word `func_1000D2F8`, currently different in 275 words.
