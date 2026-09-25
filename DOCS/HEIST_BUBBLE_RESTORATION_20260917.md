# Heist bubble assembly restoration - 2026-09-17

Five original routines replace placeholders in `conker/src/game/generated_117490.c` through `GLOBAL_ASM`: `150E9FE0` (300 bytes), `150EA11C` (884), `150EA490` (112), `150EA500` (204), and `150EA5CC` (788). Their bodies are under `conker/asm/nonmatchings/generated_117490/`.

The non-matching guest replacement build and outer packaged ROM build both exit zero. All 2,288 linked and packaged instruction bytes match the original ROM. These changes restore the primary/companion Heist bubble owners, emission and rate update; this is not matching-C or complete rebuilt-guest runtime acceptance.

The corresponding normal native RelWithDebInfo build visibly produces bubbles in both underwater Heist loss cutaways, clears them on menu return, and passes repeat match entry, movement and actual Quit. Nine focused executable tests pass; the full 1,991-test suite retains four pre-existing failures and eight skips. Brightness remains open; the angular silhouette also occurs in inspected original frames and is not established as a port-only geometry defect. The original ROM, real saves and frozen native Release are preserved.

Full source, callback, build, runtime and limitation evidence is in [OGL Note 626](../../64CBFDOGL/DOCS/WORKING_NOTES/626-heist-bubbles-restored-and-live-lifecycle-qualified-20260917.md). Guest byte receipts are in `64CBFDOGL/.codex/heist-cutaway-effects-20260917/guest-byte-audit.json`.
