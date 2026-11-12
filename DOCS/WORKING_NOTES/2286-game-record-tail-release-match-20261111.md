# Record tail-release byte match

Date: 2026-11-11. `func_15114B94` replaces a zero-return placeholder in
`conker/src/game/generated_13D350.c`; the original assembly is in
`conker/asm/13D350.s`. Its 76-word slot spans VA
`0x15114B94..0x15114CC4`, ROM `0x142044..0x142174`.

The routine releases an attached object for an in-range record, marks that
record as released, then trims consecutively released records from the end of
the table while adjusting the associated count. The table pointer and count
are read again after the release helper. The caller `func_1508EE0C` ignores
the return register; the recovered interface is `void`.

The compiler emits 76 raw words. **51 expected-word guards, with no inserted
instructions**, normalize register allocation, scheduling and control flow to
the 76-word retail body and its relocation bindings. This is a guarded C
match.

Retail and raw C guest executions agreed with an independent expected-value
model across 1,080 cases, visiting all 76 retail words. SDK32 native O0/O2/O3
each passed those cases and 11 negative controls with undefined-behavior
sanitization. The original caller window passed 1,080 cases. The release helper
was modeled with synthetic table-pointer and count changes to verify reads
after the call; those mutations are stress tests, not claims about the helper.
The full caller and release helper are not qualified, nor is the unused return
register. Tests use valid disjoint record arrays and bounded counts; arbitrary
aliases, native or hardware faults and gameplay are outside these checks.

Both padders match independently assembled retail code and bindings; 12
rebased GNU links, 132 bounded access-cut triples and 102 corrupted-guard
rejections pass. Actual Make and a strict independent image comparison account
for **241 changed bytes** with zero exclusions. All 6,050 function
addresses, 33 neighboring functions and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `ce58cb3a512a885d2b1b8d32144530ee5dba79e84850de04da44e765c15642cf`. The existing complete-
ROM checksum mismatch remains.

Fresh actual ELF recount: **3,681 / 4,840 (76.05%)** Game and **4,354 /
5,513 (78.98%)** overall, zero drift. The Game-specific 80% target needs
191 more exact functions. Tools commit `f85b856f72cd0e42e7d392e57c0429813edc23e6`
precedes the consumer change.
