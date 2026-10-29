# 1795 - Record prefix activity matched directly from C

Date: 2026-10-28

`func_150969A0` in `conker/src/game/generated_C3E20.c` now has the recovered
interface `s32 func_150969A0(s32 count)`. A signed nonpositive count returns
zero without reading the table. Otherwise it scans flag bytes in
`D_800D2DC0` at a 0x24-byte stride, returning one at the first nonzero flag
or zero when the prefix is clear. The source names and comment describe
that behavior without changing the established function or global names.

All 50 instructions emit directly from the normal IDO `-O2 -g3` profile.
There is no frame, guard, omission, shared-header change or compiler-profile
change. Four relocations form two HI16/LO16 pairs to the table. The compiler
unrolls by four and retains the remainder loop, branch-likely loads, and
three unreachable duplicate loads at body offsets `0x78`, `0x8C`, `0xA0`.
All 47 reachable instruction addresses are covered; all 50 words match.

## Qualification

| Check | Result |
| --- | --- |
| Target | VA `0x150969A0..0x15096A68`, ROM `0xC3E50..0xC3F18` |
| Body / slot / frame | 50 / 50 words, no frame |
| Complete owner | Seven functions, six neighbors and all pools unchanged |
| Actual Make | Three commands reproduce the qualified padded object |
| Direct guest execution | 9,646 cases; exact return, complete state, and ordered read trace |
| Sparse guest memory | 45 cases with only required flags mapped; no speculative flag or padding read |
| Original caller | 540 cases covering all eight words of its bounded window |
| Native32 | 216 defined-object cases per `-O0`, `-O2`, `-O3`, nine controls, trapping UBSan |
| IDO negative controls | Ten compiled counterexamples terminate with incorrect results |
| Access fault prefixes | 58 direct + 26 caller prefixes, including 37 direct delay-slot cuts |
| GNU layouts | Three layouts, 462 executions, 54 body/binding corruption rejections |
| Tools copies | Eight fresh methods and tools checks per copy; two fresh installed methods plus six strictly fingerprinted semantic reuses |
| Strict whole image | 148 changed bytes: 147 target code bytes and one symbol-size byte; zero exclusions |
| Protected Game data | All 189,088 bytes across 720 owners preserved |
| Linked inventory | All 6,055 other bodies and all 6,056 canonical addresses unchanged |
| Diagnostics | Zero owner/target diagnostics; unrelated duplicate `generated_12D630` Make warning unchanged |

The existing reset clears 0x6C bytes and the existing updater iterates three
records. Native tests therefore use a 108-byte table. Large native counts
are tested only with a guaranteed early hit within those three records.
Guest fixtures provide longer backing storage to exercise all unrolled and
remainder paths; that does not establish a larger retail allocation or
portable behavior outside valid C objects. Tests check all flag-byte values,
negative counts including INT_MIN, duplicate hits, exact first-match reads,
and the absence of writes.

The ROM census finds one direct caller at `0x15096F18` (ROM `0xC43C8`) in
`func_15096D78`, and no aligned function pointers. The eight-word window
loads the count from `8(s0)` in the call delay slot. A nonzero result skips
`func_15096A68`; a zero result calls it with the same live count. Both routes
clear `v0` before continuing at `0x15097588`. The second routine is a bounded
provider in these tests; its volatile-register, argument-home, return-value
and memory effects are exercised. Both parent and provider C remain
placeholders, with no additional matching credit. Complete parent execution
and gameplay acceptance are not established by this window.

## Banked progress

Tools commit `a8467f5` precedes the consumer commit. The inherited guard CSV
and C inventory are unchanged. The live adopted ELF recount is:

| Section | Byte-exact C | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,873 / 5,506 (70.34%) | 0 | 1,633 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,200 / 4,833 (66.21%) | 0 | 1,633 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% goal remains active: 257 more matches are needed to reach 4,130.
Remaining queue shapes are 1,504 placeholders, 120 semantic/other, and nine
unlocated. Inspect `func_15133C58` next, without credit until qualification.
`func_1514E920` remains parked and uncredited.

Only the two aggregate matching rows change in the root README. Detailed
progress belongs in this note and the DOCS indexes. An eleven-file scoped AST
refresh follows the consumer commit, with old-node and directed-relationship
retention audited before graph adoption. No full-corpus extraction or global
community/centrality recomputation is claimed.

Local evidence: `conker/build/game-record-prefix-active-match/`. ELF SHA-256:
`c1bc01a42ee33d3adf16f4340db37d94ba50b44a463dbea05f7b9f0ccb84030d`.
Padded object:
`cd75b99855e0645d4d4402e144e90c1076ff3c5daa15b025681daf0514b00e6f`.
The older standalone tools mirror retains all 1,826 inherited dirty paths
plus three qualification modules, 1,829 total. No mirror commit, reset, push
or host-port change is part of this recovery.
