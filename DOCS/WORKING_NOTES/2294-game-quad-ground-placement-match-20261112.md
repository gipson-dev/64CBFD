# Quad ground placement guarded match

Date: 2026-11-12. `func_15172B20` replaces a zero-return placeholder in
`conker/src/game/generated_19F150.c`; retail assembly is in
`conker/asm/19F150.s`. The 74-word body spans VA `0x15172B20..0x15172C48`
and ROM `0x19FFD0..0x1A00F8`, followed by two padding words.

The function offsets the supplied position using an angle and signed radius,
queries for a contact, returns zero if the query returns no contact or its
height equals the sentinel, and otherwise forwards the placement result.
The linked retail sentinel is `-10000.0f`; the modeled checks use a different
finite sentinel to exercise the equality gate independently of that value.
Its original `func_15171D4C` argument-preparation window supplies the vertex
pointer, floating coordinates and angle, radius, scale and image value.

IDO emits 72 raw words. Eleven expected-word guards and two inserted words
restore the retail local stack layout and branch structure; this is a
guarded C match, not a direct compiler match.

Retail and candidate guest execution agree with an independent model across
432 cases, covering 73 of the 74 retail instruction words. SDK32 native
O0/O2/O3 each pass those cases and five effective negative controls under
undefined-behavior sanitization. The original caller window passes 432 cases.
Trigonometric, contact-query and placement helpers are modeled; the complete
caller, helper internals, exceptional floats, arbitrary aliases, hardware
faults and gameplay are not established by these tests.

Both padders reproduce separately assembled retail code and bindings. Twelve
rebased GNU links, 95 bounded access-cut triples and 22 corrupted-guard
rejections pass. Actual Make agrees with the strict independent image audit:
265 changed bytes, zero exclusions, and two accounted symbol-metadata
reorders. All 6,050 function addresses, six owner neighbors and 189,088
protected data bytes remain unchanged. Actual ELF SHA-256: `f665aa51897e875d45e6604d581096bde8dc8588f2e8602d3c1e388eb8084635`.
The pre-existing complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **3,686 / 4,840 (76.16%)** Game and **4,359 /
5,513 (79.07%)** overall, zero drift. The Game 80% target needs 186 more
exact functions. Tools commit `735c1a6708d68234bc5afd30c1d90c33d72de846` precedes the consumer change.
