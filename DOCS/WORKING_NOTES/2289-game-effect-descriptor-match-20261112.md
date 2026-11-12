# Effect descriptor byte match

Date: 2026-11-12. `func_150C1E34` replaces a zero-return placeholder in
`conker/src/game/generated_EEE70.c`; its retail assembly is in
`conker/asm/EEE70.s`. The **72-word function body** spans VA
`0x150C1E34..0x150C1F54` and ROM `0xEF2E4..0xEF404`; three following
padding words extend the progress slot to `0x150C1F60` / `0xEF410`.

The routine assembles an effect descriptor from the input position, position
differences and scale, requests two color rows, supplies a bounded random field,
submits the descriptor, and returns one. Four original dispatch windows use
the `D_8008AA00` table. `func_151429E0`, `func_150ADA20` and `func_1518CA80`
were modeled in these tests; their internal behavior and complete callers were
not qualified. The `0.1757` double comes from `D_800A0228`. Uninitialized
descriptor padding is not treated as an output.

IDO emits 71 raw words. **48 expected-word guards and one insertion** produce
the 72-word retail body and relocation bindings. The three following padding
words were independently checked in the full 300-byte linked slot. This is a
guarded C match, not a direct compiler match.

Guest execution of both bodies agrees with an independent expected-value model
on 160 cases and visits all 72 retail words. SDK32 native O0/O2/O3 each pass
those cases and 14 effective negative controls with undefined-behavior
sanitization. Four original indirect-call windows each pass 32 cases.
The C explicitly converts through a signed 32-bit integer before narrowing to
16 bits, matching retail's conversion and store sequence. The corpus includes
values outside the 16-bit range; signed narrowing there is implementation-defined
in C and was checked for the selected SDK and native compilers. The tested
floating-point conversions stay within the signed 32-bit range. Arbitrary aliases,
exceptional or out-of-range conversions, hardware faults and gameplay remain
outside these checks.

Both padders reproduce the assembled body and bindings. Twelve rebased GNU
links, 75 bounded access-cut triples and 96 corrupted-guard rejections pass.
Actual Make agrees with the strict independent image comparison: **232 changed
bytes**, zero exclusions, and one accounted two-symbol metadata reorder.
All 6,050 function addresses, three neighboring functions and 189,088 protected
data bytes remain unchanged. Actual ELF SHA-256: `cfa1f2107975e9bf2fd38f62e0f90e825f1ab344f8ef069251f8e8d17d169a8c`.
The existing complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **3,683 / 4,840 (76.10%)** Game and **4,356 /
5,513 (79.01%)** overall, zero drift. The Game-specific 80% target needs
189 more exact functions. Tools commits `bcadefa` and `a7efc28` precede
the consumer change; the latter records the corrected 32-bit conversion stage
and expanded boundary corpus.
