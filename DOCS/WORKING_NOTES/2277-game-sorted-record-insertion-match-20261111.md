# Sorted-record insertion byte match

Date: 2026-11-11. `func_150241B4` replaces a zero-return placeholder in
`conker/src/game/generated_50D80.c`; the retail assembly is in
`conker/asm/50D80.s`. Its 81-word retail body spans VA
`0x150241B4..0x150242F8`, ROM `0x51664..0x517A8`.

The typed C routine inserts a 12-byte record before the first equal or greater
signed sort key, shifts later records, and advances the count. If the table is
full, it calls `func_15024130` with the count and context and resets the count.
The existing record padding is preserved by the structure copies. The known
caller discards the return register; its value is not qualified.

The target uses a no-unroll compilation profile while its ten neighboring
functions retain the usual profile. The compiler emits 79 raw words. **44
expected-word guards and two inserted instructions** normalize the body and
bindings to the 81-word retail function. This is a guarded, not an unguarded,
C match. The US-only Makefile rule selects the alternate object for this
function; the other object lists are unchanged.

Retail and raw C guest executions agreed across 989 cases and visited 80 of
81 retail words. SDK32 native O0/O2/O3 each passed those cases and 11 negative
controls with undefined-behavior sanitization. The original `func_150242F8`
caller window passed 989 cases; the helper was modeled and the full parent was
not qualified. The tests use valid, aligned, disjoint sorted-record storage;
arbitrary aliases, concurrent mutation and native or hardware faults are not
qualified.

Both padders agree with independently assembled retail code and bindings;
12 rebased GNU links, 175 bounded access-cut triples and 88 corrupted-guard
rejections pass. The actual scoped Make build and strict independent image
comparison account for **247 changed bytes** with zero exclusions. All
6,050 function addresses, ten neighboring functions and 189,088 protected
data bytes remain unchanged. The production build matches the independent
prediction; this was a scoped rebuild, not a clean full build. Actual ELF
SHA-256: `ddb7c2117bcaa246e69fcba0399f04fadc16507e1ee95464cb84f651764b5247`. The existing complete-ROM checksum mismatch
remains.

Fresh actual ELF recount: **4,345 / 5,513 (78.81%)** overall and **3,672 /
4,840 (75.87%)** Game, zero drift and 1,168 different. The 80% target needs
66 more exact functions. Tools commit `3764d3e967b8d3823db256bd92c2ac5b27d05253`
precedes the consumer change.
