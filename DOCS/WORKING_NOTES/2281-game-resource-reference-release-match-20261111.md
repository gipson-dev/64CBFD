# Resource-reference release byte match

Date: 2026-11-11. `func_15132444` replaces the zero-return placeholder in
`conker/src/game/generated_15F680.c`; the retail assembly is in
`conker/asm/15F680.s`. Its 75-word body spans VA
`0x15132444..0x15132570`, ROM `0x15F8F4..0x15FA20`.

The typed C routine decrements the global and indexed resource counts. On the
last reference it preserves a retained node, or releases its auxiliary data,
unlinks the node and frees its resource and node. It then runs the owner's
cleanup helper. The owner layout now names the resource ID and node at their
existing offsets; casts in the two callers preserve their emitted bytes.

The compiler emits 74 raw words. **37 expected-word guards and one inserted
instruction** normalize register allocation and control flow to the 75-word
retail body and its relocation bindings. This is a guarded, not an unguarded,
C match.

Retail and raw C guest executions agreed across 192 cases and visited 72 of
75 retail words. SDK32 native O0/O2/O3 each passed those cases and 11 negative
controls with undefined-behavior sanitization. The original `func_15132570`
and `func_1513259C` caller windows passed 192 cases each. Release, free and
owner-cleanup helpers were modeled, including mutations between calls; the
full parents and helper implementations were not qualified. The tests use
valid, disjoint list nodes and resources and non-overflowing reference counts;
arbitrary aliasing, concurrent mutation and native or hardware faults are not
qualified. The routine's return register is not qualified; both callers ignore
it.

Both padders match independently assembled retail code and bindings; 12
rebased GNU links, 119 bounded access-cut triples and 74 corrupted-guard
rejections pass. Actual Make and strict independent image comparison account
for **224 changed bytes** with zero exclusions. All 6,050 function
addresses, 30 neighboring functions and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `5cbbd3db1e5fa4811aab247286a2634f5eecd03af3dcfb3efa28e0bd215b4064`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,349 / 5,513 (78.89%)** overall and **3,676 /
4,840 (75.95%)** Game, zero drift and 1,164 different. The 80% target needs
62 more exact functions. Tools commit `bda3ef162e24b3cdec4d957dd4bd6633b85b4559`
precedes the consumer change.
