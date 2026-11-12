# Release-chain motion callback byte match

Date: 2026-11-11. `func_1518FC84` replaces a zero-return placeholder in
`conker/src/game/generated_1BA1D0.c`; the original assembly is in
`conker/asm/1BA1D0.s`. Its 80-word slot spans VA
`0x1518FC84..0x1518FDC4`, ROM `0x1BD134..0x1BD274`.

The callback initializes the linked child's velocity and randomized motion
fields from its parameters, sets its timer, event and flags, or releases the
child if parameters are absent. The original `func_151D3130` dispatch passes
the owner's own position as the vector argument. Helper calls are sequenced so
their mutations of parameters are visible at the same points as retail.

The compiler emits 76 raw words. **30 expected-word guards and four inserted
instructions** normalize register allocation and control flow to the 80-word
retail body and its relocation bindings. This is a guarded C match.

Retail and raw C guest executions agreed across 776 cases, visiting 78 of 80
retail words. SDK32 native O0/O2/O3 each passed those cases and 12 negative
controls with undefined-behavior sanitization. The original dispatch window
passed 384 owner-vector alias cases. Release and random helpers were modeled,
including parameter mutations between calls; the full parent and helper
implementations were not qualified. Tests use finite floating-point inputs,
valid disjoint owner/child/parameter storage, and the documented vector alias.
Zero divisors, arbitrary aliases, concurrent mutations, native or hardware
faults and the callback's unused return register are not qualified.

Both padders match independently assembled retail code and bindings; 12
rebased GNU links, 168 bounded access-cut triples and 60 corrupted-guard
rejections pass. Actual Make and a strict independent image comparison account
for **246 changed bytes** with zero exclusions. All 6,050 function
addresses, 60 neighboring functions and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `530ed0e07e472f0f5f157a8b94ab1c33adb2d5324d34e1dad8769b575b5e6cc2`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,350 / 5,513 (78.90%)** overall and **3,677 /
4,840 (75.97%)** Game, zero drift and 1,163 different. The 80% target needs
61 more exact functions. Tools commit `07eb0c6dc7364175010796b292387fb342bf757b`
precedes the consumer change.
