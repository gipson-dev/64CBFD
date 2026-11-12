# Localized trail preset byte match

Date: 2026-11-12. `func_151DBAA8` replaces its assembly placeholder in
`conker/src/game_2062D0.c`; its original assembly is in
`conker/asm/nonmatchings/game_2062D0/func_151DBAA8.s`. The 75-word slot
spans VA `0x151DBAA8..0x151DBBD4`, ROM `0x208F58..0x209084`.

The routine copies a position into a localized trail packet, sets the preset
angle, timing and radius ranges, and passes the angular and localized packets
to `func_15153F18`. Both known caller windows in `func_150265CC` pass zero as
the fifth argument and ignore the return register; the recovered interface is
`void`. The packet's padding is not initialized by retail and is not treated
as an output by these checks.

The compiler emits 74 raw words. **68 expected-word guards and one inserted
word** normalize the result to the 75-word retail body and its relocation
bindings. This is a heavily guarded C match, not a direct compiler match.

Retail and raw C guest executions agreed with an independent expected-value
model across 1,134 cases, visiting all 75 retail words. Native SDK32 O0/O2/O3
each passed those cases and 16 negative controls with undefined-behavior
sanitization. Both original caller windows passed 216 cases each. The trail
helper was modeled; synthetic helper mutations stress the observations and
do not establish the helper's actual behavior. Checks cover initialized
packet fields and include unusual position bit patterns. They do not qualify
the helper, full parent, unused return register, arbitrary aliases, hardware
faults or gameplay.

Both padders reproduce independently assembled retail code and bindings; 12
rebased GNU links, 132 bounded access-cut triples and 136 corrupted-guard
rejections pass. Actual Make and the strict independent image comparison
account for **235 changed bytes** with zero exclusions. All 6,050 function
addresses, 61 neighboring functions and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `4911767da1a90c69fd9d2e1a0a2450a1433c6ef20252b8e249f5f5fb33faacb3`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **3,682 / 4,840 (76.07%)** Game and **4,355 /
5,513 (79.00%)** overall, zero drift. The Game-specific 80% target needs
190 more exact functions. Tools commit `3f7dc75cad9eb8e21c1aecf0cca2a012e0317914` precedes the consumer change.
