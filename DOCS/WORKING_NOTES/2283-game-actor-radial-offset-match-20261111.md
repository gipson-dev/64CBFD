# Actor radial-offset update byte match

Date: 2026-11-11. `func_1514BE20` replaces a zero-return placeholder in
`conker/src/game/generated_176A00.c`; the original assembly is in
`conker/asm/176A00.s`. Its 76-word slot spans VA
`0x1514BE20..0x1514BF50`, ROM `0x1792D0..0x179400`.

The function interpolates an actor's secondary point toward a point 100 units
above its origin, normalizes the resulting direction and places the secondary
point 100 units from the origin. If the direction has zero length, it copies
the origin. Its argument is a typed actor pointer; the existing integer-typed
wrapper converts its argument explicitly without changing its emitted code.

The compiler emits 72 raw words. **64 expected-word guards and four inserted
instructions** normalize register allocation, stack layout and scheduling to
the 76-word retail body and its relocation binding. This is a guarded C match,
not a direct compiler match.

Retail and raw C guest executions agreed with an independent expected-value
model across 216 finite-input cases and visited all 76 retail words. SDK32
native O0/O2/O3 each passed those cases and nine negative controls with
undefined-behavior sanitization. Two original caller windows passed 216 cases
each with the normalizer modeled. Another 217 cases executed the original
retail `func_15145128` helper, including one zero-length path, visiting 41 of
its 50 words. The full callers and other helper paths are not qualified;
arbitrary aliases, non-finite values, hardware faults and gameplay behavior
are outside these checks.

Both padders match independently assembled retail code and its binding; 12
rebased GNU links, 171 bounded access-cut triples and 128 corrupted-guard
rejections pass. Actual Make and a strict independent image comparison account
for **235 changed bytes** with zero exclusions. All 6,050 function
addresses, 35 neighboring functions and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `ca5ab5ffedd98d094244fffd6ce26bdce4188e1fca923820211e747719a57f47`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,351 / 5,513 (78.92%)** overall and **3,678 /
4,840 (75.99%)** Game, zero drift and 1,162 different. The 80% target needs
60 more exact functions. Tools commit `4d0daea7c1395ad3935bac13e6922f2754c57264`
precedes the consumer change.
