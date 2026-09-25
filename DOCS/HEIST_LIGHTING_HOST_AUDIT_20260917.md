# Heist lighting host-gate audit - 2026-09-17

The native port skipped Heist's original authored lighting commands. Its host gate now admits kinds9/10/15/16 for the measured category1A/count68/world14 layout, and its host renderer selects the existing view-space CBFD lighting mode for Heist. No corresponding guest category restriction exists here.

`conker/src/game_36680.c` already uses `GLOBAL_ASM` for `func_15009334`. All676 bytes of `conker/asm/nonmatchings/game_36680/func_15009334.s` match fresh original-ROM extraction and the existing linked guest ELF, SHA256 `612b0077c3c367611284d6b2872e16a8719104e2acb68a2f04029996cf8f2577`. No guest source edit or rebuild is necessary for this host-only correction.

The normal native RelWithDebInfo run now contains34 authored lights and five ambient regions, visibly restores dim underwater loss-shot shading, and passes repeat entry, Continue movement, actual Restart and Quit. All39 focused checks and16 native heap captures pass; the full1,997-test suite retains four known failures/eight skips. Release and real saves are preserved. Full multiplayer and exact presentation/audio remain open.

See [OGL Note627](../../64CBFDOGL/DOCS/WORKING_NOTES/627-heist-authored-lighting-and-underwater-brightness-restored-20260917.md) for scope, original/native packet comparison, runtime evidence and limitations.
