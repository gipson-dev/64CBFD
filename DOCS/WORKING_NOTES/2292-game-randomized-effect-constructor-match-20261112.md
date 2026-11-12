# Randomized effect constructor byte match

Date: 2026-11-12. `func_151AE984` replaces a zero-return placeholder in
`conker/src/game/generated_1D92F0.c`; its retail assembly is in
`conker/asm/1D92F0.s`. The 76-word body spans VA
`0x151AE984..0x151AEAB4` and ROM `0x1DBE34..0x1DBF64`.

The routine scales the negated input vector, makes two float and two integer
random calls in their original order, then passes the resulting values to
`func_151D9014` and forwards its returned pointer. Its original caller window
in `func_151AE890` supplies the position, three floating values and two byte
arguments. Correcting the caller's three input types from integer bit-pattern
placeholders to `f32` left that caller's emitted instructions unchanged.

IDO emits 76 raw words. **17 expected-word guards and no inserted words**
normalize its scheduling and relocation bindings to retail. This is a guarded
C match, not a direct compiler match.

Guest execution of both bodies agrees with an independent model across 216
cases, reaching all 76 retail words. SDK32 native O0/O2/O3 each pass those
cases and 12 negative controls with undefined-behavior sanitization. The
original caller window passes 96 cases. Random generators and the effect
constructor are modeled; their internals, the complete caller, exceptional
floating values, arbitrary aliases, hardware faults and gameplay remain
outside these checks.

Both padders reproduce independently assembled retail code and bindings.
Twelve rebased GNU links, 96 bounded access-cut triples and 34 corrupted-guard
rejections pass. Actual Make agrees with the strict independent image audit:
**283 changed bytes**, zero exclusions, and one accounted two-symbol metadata
reorder. All 6,050 function addresses, 32 owner neighbors and 189,088 protected
data bytes remain unchanged. Actual ELF SHA-256: `359655e4df29fe5db8027dd990ae615cb26f6cb6a0c464c01c1c3dec6739dfd0`. The
existing complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **3,685 / 4,840 (76.14%)** Game and **4,358 /
5,513 (79.05%)** overall, zero drift. The Game-specific 80% target needs
187 more exact functions. Tools commit `c5a143913db3938d8f16c1a2e77f62b7dd50c2b9` precedes the consumer change.
