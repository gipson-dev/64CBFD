# Game handwritten PRNG step restoration - 2026-09-26

## Result

`func_150ADA20` is restored from its maintained behavioral C equivalent to the
original handwritten assembly across the complete 18-word, 72-byte extent
`0x150ADA20..0x150ADA64`. The fresh C-only matcher reports 2,684 / 5,482
exact functions overall and 2,116 / 4,793 in Game.

This is an ownership correction, not a new exact-C match. The exact numerator
stays unchanged while one false C row leaves the denominator. Fresh conversion
accounting is 5,482 / 6,038 C functions and 1,932,408 / 2,256,728 C bytes
overall; Game is 4,793 / 5,318 functions and
1,763,832 / 2,072,880 bytes.

## Recovered behavior

The routine advances the 64-bit seed at `D_800885B0` using a compact
xorshift-style sequence. It combines shifted portions of the seed, applies a
second shifted XOR, folds the low 12 bits of a right-shifted intermediate back
into the result, stores the new 64-bit seed, and returns its signed low word.

The verified behavioral C remains under `#if 0` beside the active
`GLOBAL_ASM`, preserving a readable description without misclassifying the
retail routine as compiler-generated C.

## Ownership evidence

The live IDO build of the equivalent C is 19 words, one word larger than the
retail slot. It CSEs the seed address into a persistent register, introduces
`lui`/`addiu`/`ld`, allocates the arithmetic across `v1` and `t` registers,
and emits a `nop` return delay slot. The padding tool therefore had to place
that C body in `.game_overflow` and leave a trampoline at `0x150ADA20`.

Retail instead uses the assembler's direct `ld a0, D_800885B0` expansion,
materializes a separate `lui at` for the store, executes its shift pairs in
strict source order, reuses only `a0`, `a1`, and `a2` for the arithmetic, and
places the final `dsra32` in the `jr ra` delay slot. Historical compiler
experiments already ruled out the plausible C variants and identified this
routine as handwritten; a later broad conversion pass had reintroduced the C
despite that surviving source comment.

## Exact-byte evidence

The linked ELF `.game+0xADA20` span at ELF file offset `0xEDA20` and pristine
retail `conker.us.bin+0xDAED0` span are both 72 bytes and compare equal. Both
hash to:

`040875e60d965f65ffa115c2fbc6a46afadd210d3daa55d6fd1ba1c1b5accfd2`

The focused object build, complete ELF link, fresh matcher, exact span
comparison, full replacement and outer builds, project-tool checks, all six
pad-tool unit tests, and whitespace audit pass. No gameplay runtime test was
required because the active linked body is the original retail code.

## Sibling audit

`64CBFDOGL` already contains the generated recomp implementation at
`recomp_out/.c`; no separately maintained host implementation needs a paired
change. Its 1,659 existing scoped dirty entries were left untouched. Frozen
Release was not built, modified, or launched; `build/Release/conker_pc.exe`
retains timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership,
keep 17-word `func_150721A4` parked as the known live-C compiler overflow, and
keep probable handwritten `func_15125628` outside the ordinary C queue.

Continue with 30-word `func_150CFE98`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior, relocations, and current object shape before editing source.
