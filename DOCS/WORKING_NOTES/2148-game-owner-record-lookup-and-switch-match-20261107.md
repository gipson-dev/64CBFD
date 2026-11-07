# Owner/tag record lookup and constructor dispatch matched

Date: 2026-11-07. Continues [Note 2147](2147-game-selected-impact-sprite-and-frame-match-20261107.md)
from consumer `8989619280ec12ef53e20086dabb0830a7e1e693` and tools
`af6a350da363a9f0747021ed97e2ac07b3c6c5b4`, toward the active 80% goal.
This turn contributes one fully qualified match.

## Recovered interface and behavior

`func_1518BA90` in `conker/src/game/generated_1B8F40.c` replaces its zero-return
placeholder with **89 words / 356 bytes** of complete semantic C. VA
`0x1518BA90..0x1518BBF4`, ROM `0x1B8F40..0x1B90A4`. Interface:
`void *(u8 *owner, u8 priority, s32 context)`. The real frame is72 bytes, with
the28-byte request at SP+28, saved RA at SP+14 and incoming priority at SP+4C.
No artificial padding local or frame guard is needed. Raw C differs in two
independent scheduling words; two checked relocation-aware guards make the
complete padded body byte-exact.

NULL owner returns immediately. Otherwise, the routine walks two row chains in
order: table `D_800DCE50`, row stride0x1A0, head at+7C, record next at+8.
The address of `D_800DD190` is the table-end sentinel (base+0x340); its signed
counter value is not read. For each record, owner pointer+24 is tested first.
A pointer hit returns without reading either tag. Otherwise, unsigned owner
byte+3B is compared with record byte+28. The first pointer or tag hit wins,
including a tag hit earlier than a later pointer hit. Owner tags remain live
per node; record/owner aliases and both complete rows are tested.

Only after both chains miss does it read unsigned owner byte4. Types0..4
construct a default request with four10.0f values, inclusive choice limits5/0,
mode5 and subtype19. Type7 uses the three original float constants plus5.0f,
choice limits4/55 and the same mode/subtype. All other byte values return NULL.
The owner pointer and live tag are stored last, before passing request,
priority and context to the already recovered `func_1518BCD0`. Its result,
including allocation failure, is returned unchanged.

The request names describe measured roles: `firstBase`, `firstRange`,
`secondBase`, `secondRange`, and two inclusive choice limits. The original
consumer `func_1518BD60` calculates base+random*range for each pair and samples
the inclusive limits. This does not credit that consumer's still-stubbed C.
The27 defined request bytes are checked. Byte1B is deliberately unwritten and
copied by the original constructor; native fixtures initialize it only after
checking the defined fields. No portable value is claimed for that byte.

The aligned retail census finds one direct JAL, ROM0xC5A0C / VA1509855C, no
pointer literal and no tail jump. Its original eight-word argument/result
window passes owner S1, priority255 and context0. The guard-zero path skips
the call; the enabled branch returns1 independently of the helper result.
The complete parent remains outside this recovery.

## Guard, table and owner closure

The source keeps the ordinary O2/g3 profile. Both predecessor and qualified
owners compile without C diagnostics. Two ADDIU address completions at byte
offsets2C/30 exchange along with their LO16 bindings. Their HI16 bindings remain fixed; all11 other relocation sites keep their
offsets, with the two .rodata labels retargeted to the preserved table anchor. The two instructions have no
intervening memory access or trapping operation, and their complete register
state rejoins before the first row-head read. Raw C, retail and normalized C
therefore compare with identical full private state and fault prefixes.

The recovered switch emits exactly nine table entries. The unreachable
`case -1` preserves the retail table shape; the unsigned input cannot select
it. Offsets from the function entry are164,256,256,256,256,256,312,312,172.
The new target-specific Make binding names the preserved `jtbl_800A7410`.
The raw48-byte .rodata pool consists of nine zero-addend R_MIPS_32 relocations
and12 zero padding bytes; the complete pool is audited before the padder uses
the retail anchor. It is not copied over the adjacent three float constants.
Those constants retain bit patterns4030A3D7/40BEB852/404D70A4. Native builds
disable only GCC's switch-outside-range warning for the documented unreachable
case; IDO production needs no warning exception or optimization change.

All eight raw and padded owner neighbors, their bindings, and all padded
allocatable pools are unchanged. Raw pools differ only by the verified switch
pool. Raw .options/.reginfo payloads remain fixed; the .options name offset
changes33 to41 as .rodata is added to the section-name table, and its file
offset follows object geometry. No other section-header field is relaxed.
The complete guard CSV predecessor is preserved byte-for-byte, with two rows
appended. All109 core/header snapshots remain checked.

## Qualification and production evidence

Eight checks pass freshly both before and after installation in both tools
configurations:

- **2,065 guest cases per body**, retail/raw/padded, cover all256 unsigned
  owner kinds, both row heads, all six chain positions, pointer/tag ordering,
  owner-node aliases, incoming homes, provider mutations and copied float bits.
  All86 reachable root words are visited. Word26 is a dead duplicate next load;
  words41/42 are the unreachable case-minus-one return.
- **768 additional connected cases per body** execute all65 retained helper
  words: constructor36, byte-copy11 and integer RNG18. Installed helper bytes
  equal retail. The allocator receives `(31, context, 68, 1, priority, 1)`;
  NULL returns immediately. Success copies28 bytes to record+10 and stores
  two original64-bit RNG draws masked to31 at+2C/+30. Guest-only constructor
  home aliases redirect the copy source or mutate the already captured context.
  Allocator remains bounded; no additional helper C is credited.
- **187 fired access cuts**, including66 delay-slot cuts, compare complete
  memory/register/FPU/HI/LO state, trace, PC and delay markers for all three
  bodies. Minimal mappings prove lazy NULL, pointer-hit, tag-hit and unsupported
  kind behavior. These qualify emitted guest accesses, not portable C faults.
- **24 original caller-window cases per body** include both guards, supported
  and unsupported kinds, successful/failed allocation and connected helpers.
  **Six independent GNU links** exercise all13 bindings in three layouts,
  including signed low16 carries. Nine linked switch entries per image and
  twelve rebased execution cases per body agree.
- SDK **native32 UBSan** passes O0/O2/O3 with1,309 cases per profile and all19
  effective negative controls. Checks include the27 defined request bytes,
  result identity, captured arguments, float bit copies, all node/owner/table/
  output fences and constructor mutations. The native table-boundary names
  are expressed as one array and its end, retaining the actual retail object
  relation; an initial assembly-only alias let GCC fold a distinct-object
  fixture assertion. The corrected fixture passes all optimized profiles.
- All356 raw-byte,13 binding, two raw-pool and six whole-image corruptions
  are rejected. The former zero-return stub fails the semantic comparison.

Both tools copies also pass fresh shared smoke checks. Three unchanged shared
regression receipts are reused only after exact test/helper fingerprint checks.
The sibling uses its own compiler/parser/padder/base oracle/native command;
its missing pool auditor and tracked64-bit RNG executor are explicit,
fingerprinted mounted fallbacks. New modules use a disposable overlay and do
not overwrite the sibling. Windows Git checks its inherited2434 dirty paths.
Claude calls:0. No hardware/gameplay acceptance is inferred from these checks.

Actual Make recompiles only this owner once, with zero C diagnostics. Its ELF
equals the literal **324-byte prediction with zero exclusions**. The only
body change is this routine, symbol size12 to356. Two explicit metadata groups
reorder five named symbols/strings: `(D_800A7434,D_8008F750,D_8009E714)` in
order1,2,0 and `(jtbl_800A7410,D_800CBD78)` in order1,0. Complete definitions
are preserved. No section or metadata range is excluded from comparison.
All6,052 function addresses, other bodies, progress.csv and189,088 protected
Game bytes across720 owners remain fixed. The inherited duplicate12D630 recipe
warning and expected unfinished-ROM checksum exit2 remain.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,218 / 5,512 (76.52%) | 0 | 1,294 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,545 / 4,839 (73.26%) | 0 | 1,294 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**192 more** matches reach the current4,410 threshold for80%.

- ELF: `31b57da8521d3c4694656926e081fc2adc198ee3cf32292a6855c9e5c20d2266`.
- Binary: `944e8ddfeb0cd64ffb3b625ce25ea6652a7e1511083c6b93a9909e6257b317e9`.
- Guard CSV: `07f10c774595f08f62fd8b543daa18417a7d6f175d623720f77446be2ab0132e`.
- Makefile: `4e252a768e0bbb7b7c29dcdefb9bc54c94788dc62c3ce486864d817a7efadd5c`.

Reproduce with `python3 -m unittest tools.tests.test_game_owner_record_lookup_match -v`.
Receipts live in `conker/build/game-owner-record-lookup-1518BA90-match/`.
Production Make freezes shared dependency timestamps using
`-o retail_word_patches.us.csv -o Makefile` while still reading the audited
new table binding and guards. It then runs ELF/progress, expected unfinished
image `all`, and `match-progress NON_MATCHING=1`.

Tools commit precedes source/Make/guards/docs/pin. README receives aggregate
rows only. Historical status-index text is checked unchanged as UTF-8.
Graphify refresh is scoped/fail-closed, retaining prior nodes outside changed
paths, rather than claiming full-corpus extraction.

## Next target

Continue with **func_1518BD60**, the214-word two-channel effect-record updater
in this owner, VA1518BD60..1518C0B8 / ROM1B9210..1B9568. Its original0x120-byte
frame saves S0..S7/FP/RA and F20..F28. Each channel subtracts the live global
tick from its timer; valid owner/actor/tag gates control sampling and effect
construction, then previous signed coordinates are converted to float.
The recovered request's two random base/range pairs and inclusive limits now
provide typed inputs for this consumer. Its aligned callback literal is at
ROM2305B4, with no direct JAL sites; the214-word body contains nine JALs to
integer/float RNG, the byte-angle helper and the existing effect factory. Inspect its descriptor, all15 effect
arguments, unsigned RNG divisions, provider ordering and result backlink
before drafting and qualifying C. It remains a zero-return placeholder and
receives no credit here. Preserve handwritten150A6FA0/150A76F0, unrelated work,
private inputs/saves and frozen host Release. Keep the wider80% goal active.
