# Ring-entry updater byte match

Date: 2026-11-11. `func_151BC64C` replaces the zero-return placeholder in
`conker/src/game/generated_1E73B0.c`; the original assembly is in
`conker/asm/1E73B0.s`. Its 82-word retail body spans VA
`0x151BC64C..0x151BC794`, ROM `0x1E9AFC..0x1E9C44`.

The typed C routine ages entries in a circular buffer, removes expired
entries, reduces a fade byte when fewer than ten ticks remain, and publishes
the current entry's three values or zeroes. Its early exit returns zero when
the count is below two and the relevant flag is set; otherwise it returns
one. The fade target is **remaining timer times 25**.

The compiler emits 81 raw words. **29 expected-word guards and one inserted
instruction** normalize control flow, register allocation and scheduling to
the 82-word retail body. The complete guarded body and relocation bindings
match retail. This is not an unguarded C match.

Retail and raw C guest executions agreed in 2,068 bounded cases, including
signed timer and tick extremes, and visited 78 of 82 retail words. SDK32
native O0/O2/O3 each passed those cases and nine negative controls with
undefined-behavior sanitization. The original `func_15147740` dispatch
window and bounded full-parent paths each passed 2,068 cases through
`D_8008A200[10]`; the release helper was modeled and unrelated dispatcher
branches were not qualified. Inputs use valid, aligned, disjoint owner,
tick and ring storage with in-range indices; arbitrary aliasing, concurrent
mutation and hardware faults are not qualified.

Both padders agree with independently assembled retail code and bindings;
12 rebased GNU links, 112 bounded access-cut triples and 58 corrupted-guard
rejections pass. Actual Make and strict independent image comparison account
for **238 changed bytes** with zero exclusions. All 6,050 function
addresses, 56 neighboring functions and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `80515772558b9ceabba98132cf6f776bcdfbcc4baccd61f14facd9593da4e9c4`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,344 / 5,513 (78.80%)** overall and **3,671 /
4,840 (75.85%)** Game, zero drift and 1,169 different. The 80% target needs
67 more exact functions. Tools commit `c0d745db06b7780609631b89d60f2a851254f118`
precedes the consumer change.
