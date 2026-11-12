# Tile-fade callback byte match

Date: 2026-11-11. `func_150DFDD0` replaces a zero-return placeholder in
`conker/src/game/generated_10CD70.c`; the original assembly is in
`conker/asm/10CD70.s`. Its 75-word slot spans VA
`0x150DFDD0..0x150DFEFC`, ROM `0x10D280..0x10D3AC`.

The callback advances an active fade timer and returns 1 when the timer
expires. Otherwise it sets the owner's state and updates the first tile-size
command's coordinate word if a display list exists. It preserves the second
command word. `func_15030468` dispatches it through `D_800841C0[12]` and
uses its return value.

The compiler emits 71 raw words. **31 expected-word guards and four inserted
instructions** normalize register allocation and control flow to the 75-word
retail body and its relocation bindings. This is a guarded C match.

Retail and raw C guest executions agreed with an independent expected-value
model across 2,161 cases, visiting 73 of 75 retail words. SDK32 native
O0/O2/O3 each passed those cases and 13 negative controls with undefined-
behavior sanitization. The original dispatcher window passed 2,161 cases,
including the early-expiration path and its return value. The full parent is
not qualified. Tests use finite values within the conversion range, valid
disjoint records and terminated command lists; arbitrary aliases, malformed
lists, non-finite values, hardware faults and gameplay are not qualified.

Both padders match independently assembled retail code and bindings; 12
rebased GNU links, 48 bounded access-cut triples and 62 corrupted-guard
rejections pass. Both normal and `RETAIL_FUNC_150DFCA8` compiler profiles
were independently checked against their real Make outputs and neighbors.
Actual Make and a strict independent image comparison account for **232
changed bytes** with zero exclusions. All 6,050 function addresses, 12
neighboring functions and 189,088 protected data bytes remain unchanged.
Actual ELF SHA-256: `0b4a475a46c7c7a43b710dca7d6fd7a40b22790d5bcf6f75a09b0310e46ffe34`. The existing complete-ROM
checksum mismatch remains.

Fresh actual ELF recount: **3,679 / 4,840 (76.01%)** Game and **4,352 /
5,513 (78.94%)** overall, zero drift. The Game-specific 80% target needs
193 more exact functions. Tools commit `22c9070b74b460c797bc3065eddcba32b5373347`
precedes the consumer change.
