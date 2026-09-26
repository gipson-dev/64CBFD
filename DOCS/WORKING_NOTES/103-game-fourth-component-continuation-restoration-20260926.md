# Game fourth-component continuation restoration - 2026-09-26

## Result

The false C placeholder for `func_150A7A14` is replaced by its original
thirteen-word assembly body across `0x150A7A14..0x150A7A48`. The linked C
matcher now reports `2615 / 5483 (47.69%)` overall and
`2047 / 4794 (42.70%)` game, with one address-drift blocker and 2,867 total
differing C functions. Raw assembly increases to 555 total and 524 game rows.

## Ownership

This routine is not an independent C function in the ordinary ABI sense.
`func_150A7A00` saves its caller's return address in `t9`, installs
`func_150A7A14` as a synthetic return address, and jumps to
`func_150A7960`. The continuation consumes `f0`, `f2`, and `f4` left by that
matrix-vector calculation, reads the fourth matrix column, stores the fourth
output component through the caller's stack argument, and returns through
`t9` rather than `ra`.

The prior `return 0` placeholder emitted only three meaningful words followed
by padding. No conventional C signature can faithfully express the inherited
FP-register state or synthetic return convention. The retained full slice in
`asm/D4E10.s` is authoritative, so its thirteen original words now live in
`asm/nonmatchings/generated_D4E10/func_150A7A14.s` beside the already restored
five-word trampoline head.

## Evidence

The rebuilt object matches all thirteen retail words. Linked
`conker/build/conker.us.bin+0xD4E94` and pristine retail
`conker/conker.us.bin+0xD4EC4` are byte-identical for 52 bytes and share
SHA-256
`75bbc5234eee00ae6d58550ab03989349ce347c30c8c2cea8403183d9f36c8d0`.
The complete linked trampoline pair at `0xD4E80` and retail pair at `0xD4EB0`
are byte-identical for 72 bytes and share SHA-256
`1611882974aba49c03d7f76982375a44733d639a2bae377e32e86a5880459bf0`.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. The patch table remains at 808 rows with zero duplicate
keys and no row for this function.

The `64CBFDOGL` sibling already contains host-specific handling, documentation,
and a focused fourth-component test for this trampoline family. No new donor
transfer applies. Its 1,659 existing dirty entries were left untouched. Frozen
Release was not built, modified, or launched; `build/Release/conker_pc.exe`
retains timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 19-word `func_150CFBEC`, now the first game row with thirteen
real differences. Inspect its source and retail/current instruction maps for
false-placeholder ownership before attempting source reshaping or guards.
