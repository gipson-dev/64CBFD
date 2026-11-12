# Game segment-binding byte match

Date: 2026-11-11. `func_150C8600` replaces a zero-return placeholder in
`conker/src/game/generated_F5800.c`; the original assembly is in
`conker/asm/F5800.s`. Its 76-word slot spans VA
`0x150C8600..0x150C8730`, ROM `0xF5AB0..0xF5BE0`.

The function examines ten records, clamps each signed choice to the supported
resource range, resets invalid groups, loads the chosen resources and emits
ten segment bindings. The two group-table pointers are captured before the
loop, while the active record pointer is read again on each iteration.
`func_1510B9D0` uses the returned display-list cursor.

The compiler emits 75 raw words. **45 expected-word guards and one inserted
instruction** normalize register allocation, scheduling and control flow to
the 76-word retail body and its relocation bindings. This is a guarded C
match.

Retail and raw C guest executions agreed with an independent expected-value
model across 264 cases, visiting all 76 retail words. SDK32 native O0/O2/O3
each passed those cases and 12 negative controls with undefined-behavior
sanitization. The original caller window passed 264 cases. The resource loader
was modeled, with synthetic record-pointer and table-pointer mutations to
check the loop's access order; those mutations are stress tests, not claims
about the real loader. The full caller and resource loader are not qualified.
Tests use valid disjoint record arrays and display-list storage; arbitrary
aliases, hardware faults and gameplay are outside these checks.

Both padders match independently assembled retail code and bindings; 12
rebased GNU links, 428 bounded access-cut triples and 90 corrupted-guard
rejections pass. Actual Make and a strict independent image comparison account
for **233 changed bytes** with zero exclusions. All 6,050 function
addresses, 18 neighboring functions and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `7af9f106881f8840f3389ed303932788c0a84a944706d2081d52021b0c7cd9c2`. The existing complete-
ROM checksum mismatch remains.

Fresh actual ELF recount: **3,680 / 4,840 (76.03%)** Game and **4,353 /
5,513 (78.96%)** overall, zero drift. The Game-specific 80% target needs
192 more exact functions. Tools commit `f00099f569da1888caaa98ec11920fa2c3237a8b`
precedes the consumer change.
