# Motion-ring integrator byte match

Date: 2026-11-11. `func_151CD674` replaces a zero-return placeholder in
`conker/src/game/generated_1FA770.c`; its retail assembly is in
`conker/asm/1FA770.s`. Its 82-word body spans VA
`0x151CD674..0x151CD7BC`, ROM `0x1FAB24..0x1FAC6C`.

The typed C routine integrates a circular set of positions and velocities,
retires entries below a threshold, clamps the surviving entry and publishes
the owner's three source words. It returns zero on its count/flag early exit
and one otherwise.

The compiler emits 81 raw words. **50 expected-word guards and one inserted
instruction** normalize register allocation, scheduling and control flow to
the 82-word retail body and its relocation bindings. This is a guarded, not
an unguarded, C match.

Retail and raw C guest executions agreed across 1,856 finite cases and visited
78 of 82 retail words. SDK32 native O0/O2/O3 each passed those cases and nine
negative controls with undefined-behavior sanitization. The original
`func_15147740` dispatch window and bounded full-parent paths each passed
1,856 cases via `D_8008A200[9]`; the release helper was modeled and unrelated
dispatcher branches were not qualified. Inputs use valid, aligned, disjoint
ring storage with in-range indices and finite arithmetic; arbitrary aliasing,
concurrent mutation, nonfinite arithmetic and hardware faults are not qualified.

Both padders match independently assembled retail code and bindings; 12
rebased GNU links, 144 bounded access-cut triples and 100 corrupted-guard
rejections pass. Actual Make and strict independent image comparison account
for **285 changed bytes** with zero exclusions. The ELF symbol table
contains a documented ordering exchange between `.L1514EA98_game_data` and
`D_8009D4E0`; its identities and values remain accounted for. All 6,050
function addresses, 51 neighboring functions and 189,088 protected data bytes
remain unchanged. Actual ELF SHA-256: `a321ec297d4dc3b6bdf98f88e92676076e2f10c6e49d6da3831ca99eb28bd85e`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,346 / 5,513 (78.83%)** overall and **3,673 /
4,840 (75.89%)** Game, zero drift and 1,167 different. The 80% target needs
65 more exact functions. Tools commit `963162e0d2d0c01e381eb5acd55850a115ddaac5`
precedes the consumer change.
