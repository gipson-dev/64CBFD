# Active record lookup match

Verified 2026-10-29. `func_1509CA98` replaces the zero-return placeholder in
`conker/src/game/generated_C9EC0.c`. VA `0x1509CA98..0x1509CB68`, ROM
`0xC9F48..0xCA018`: 52 words /208 bytes, no stack frame or alignment words.

## Recovered behavior and scheduling

`s32 func_1509CA98(u32 key)` scans204 existing20-byte records in groups of four.
A record is active when its first word is nonzero. Its lookup key is
`((u32)field4 & 0x1FFFFFFF) + 1`; the first matching index is returned, or204
when absent. High three flag bits are ignored. The routine only reads memory.
The explicit unsigned cast preserves compiler bytes and avoids native signed-
comparison warnings. The existing type and globals remain unchanged.

The source keeps the existing O2/g3/-Wo,-loopunroll,0 profile. Changing to the
default profile expands this manually unrolled loop to141 words. Eleven bounded
declaration/initialization variants were screened. The selected index-first
form matches50/52 raw words; two relocation-aware expected-word guards exchange
the independent mask completion and table-address completion at offsets12/16.
The LO16 relocation moves with its ADDIU. No opcode, operand, register, branch,
instruction count, word multiset, insertion or omission changes. This is a
checked scheduling normalization, not a raw direct-C byte match.

Raw SHA256 `18dd8078c405cec410edda45b8af30c21e8b62310bd2ffbf5b5e27b2b0333631`.
Normalized/original raw SHA256
`818ce7241e76826cf6e9e1527c9a9e5d12561624e6230882bec3390049b4d642`.
Global `D_80087430` bindings: raw HI16/LO16 at0/12, retail at0/16.

## Qualification

- Eight fresh canonical checks plus shared tools checks in each tools copy.
  Two fresh installed checks per copy; six unchanged semantic checks reused
  only under complete module/input/artifact fingerprints.
- 932 guest cases cover every record position, absent keys, inactive matching
  keys, duplicates, negative active words, all high flag values and key bounds.
  All48 reachable words are covered. Four duplicate instructions at offsets
  64/104/144/184 are unreachable in the original. Original/raw/normalized
  complete state, memory and access traces agree; the table is unchanged.
- Native32 SDK O0/O2/O3 each pass6,563 cases with trapping UBSan and full-table
  canaries. Seven effective semantic controls are compiled independently by
  native GCC and IDO; every control terminates and has a behavioral witness.
- All four full-ROM JALs are accounted for:6D11C/6D130/6D168/6D41C; no aligned
  pointer registrations. All belong to original `func_1503FB40`, whose current
  C remains a placeholder. Four original windows at1503FC64/FC74/FCB4/FF68
  contain4/5/3/3 words and pass96 cases each (384 total). Third-window precondition:
  A0=80080000; fourth: S3 holds request minus one. Results are consumed later.
  No complete-parent, gameplay, hardware or portable C fault claim.
- 405 fault-prefix groups include156 delay-slot cuts. Three GNU layouts pass
  60 cases; actual Make, original and normalized images agree, with the raw
  independent setup exchange explicitly retained and checked.
- Four real-padder stale-word/relocation controls,54 raw/binding corruption
  controls and212 full-image corruption controls reject. Existing guard CSV
  bytes are preserved, with exactly two new target rows appended.
- Actual Make compiler/padder/assembler: three commands, no diagnostics.
  All18 neighboring functions and constant pools are unchanged.

## Production audit and progress

The complete production ELF equals the independent prediction:159 changed
bytes =158 target instruction bytes +1 target extent byte; metadata0,
exclusions0. All6,056 function addresses,6,055 other bodies,189,088 protected
Game bytes/720 owners, conversion inventory and map remain fixed. Other objects
are unchanged; inherited guard consumers are pinned while rebuilding the target.

Fresh live-ELF recount: **3,901 /5,506 (70.85%)**;
Game **3,228 /4,833 (66.79%)**; Init492/492; Debugger181/181; zero drift.
**229 more** exact C functions reach4,130 /5,506 (75%).
ELF SHA256 `199b50f0b01713d4d7a472cb13aed15a40e8cf24eb8ae1630abd25d8bd2278ed`.
Object SHA256 `55f024c78d24352f5339d64398bc20368de005bc2f8a0802e3d721b868bca5f7`.
New guard CSV SHA256 `84c233dfd374f8ba8b4f66dca69b180bc2b8b3813b7a1a594d72f88130ba0306`.
Tools committed first as `8242b0f`; consumer follows this note. No push.

## Resume

Evidence: `conker/build/game-active-record-lookup-match/` contains652 focused
frozen inputs,16,659 sealed inputs, canonical/installed receipts, strict image
prediction, actual Make, recount and graph/final audits. The older tools mirror
retains1,910 inherited dirty paths plus3 new modules. Root README changes only
aggregate rows. Graph refresh is scoped; no full-corpus/global analytics claim.
The75% goal stays active. Next screen `func_151738C4`; next note1824.
`func_1514E920` and `func_151D7000` remain parked and uncredited.
