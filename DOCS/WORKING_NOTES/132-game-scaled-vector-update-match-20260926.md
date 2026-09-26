# Game scaled-vector update match - 2026-09-26

## Result

`func_151C4510` is byte-exact across all nineteen words at
`0x151C4510..0x151C455C`. The linked matcher reports
`2644 / 5483 (48.22%)` overall and `2076 / 4794 (43.30%)` game, with one
address-drift blocker and 2,838 total differing C functions. Debugger remains
complete at `181 / 181`.

## Destination lifetimes

The function scales source float components at offsets `0x04`, `0x08`, and
`0x0C`, then adds them into destination fields `0x34`, `0x38`, and `0x3C`.
The previous direct expressions allowed IDO to load each destination shortly
before its update. Retail retains the first two values across the first
calculation and preloads the third value immediately before the first store.

Explicit `x`, `y`, and `z` locals expose the destination lifetimes. Fifteen
guarded words restore retail's precise FP preload order, including the third
load before the first store, plus its register allocation, multiplies,
additions, and stores. The final schedule therefore reproduces retail's
overlap behavior. The entry and return words already match; no words are
inserted and no relocations move. The patch table contains 951 unique rows
with no duplicate keys.

## Evidence

The final linked and pristine 76-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x1F1990`
- retail `conker/conker.us.bin+0x1F19C0`
- SHA-256 `71f59522176e0647ccd14b5e9bd7c261e6249c18b24b2140074b3e91a02e96f8`

The focused object build, exhaustive nonmatching rebuild, fresh direct matcher,
outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation translation,
calls, declaration, and symbol metadata for this function, with no separately
maintained host implementation to update. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Continue with 20-word `func_150C78E0`. Its existing C checks flag `0x04` at
object offset `0x73`, derives a high-half mask from `D_800DBEF4 + 0x21C`,
stores the result at object offset `0x3C`, and calls `func_151150BC`. The fresh
matcher reports fifteen real differences, so begin with the compact register
and branch schedule.
