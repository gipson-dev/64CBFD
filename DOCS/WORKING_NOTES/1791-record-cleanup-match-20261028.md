# Shared record cleanup - guarded C match

Verified 2026-10-28. Restore func_15183C28 in generated_1B0740:
VA 0x15183C28..0x15183D28, ROM 0x1B10D8..0x1B11D8, 64 words / 256 bytes.
The normal O2/g3 profile recovers the complete routine and 32-byte frame.
Six expected-word guards normalize one closed private spill slot. This is a
guarded match; 58 of the 64 linked words emit directly from the selected C.
Keep the retail function name and the resource-release behavior comment.

## Behavior and shared storage

The recovered interface is void func_15183C28(s32 index). The existing table
contains eleven records, each holding five words. Load record word4 as a
resource-list pointer. If nonzero, call void func_1510D630(s16 *allocation)
and then clear that word. This happens before either special-index gate.

For index8, retain the backing allocation unless signed D_800DDF71 is -2.
For index9, if signed D_800DDF70 is -2 and D_800DDF20 is nonzero, free that
allocation with func_10004074(void *), then clear D_800DDF20 and D_800DDF98.
After the special case, reload the selected record's word0. If nonzero, free
it and clear both word0 and D_800DDF78[index]. Empty records do not clear an
unrelated display-list entry. Retain the live reads after helper calls.

These labels share actual storage:

| Retail label | Existing storage |
| --- | --- |
| D_800DDF20 | D_800DDE80[8].words[0] |
| D_800DDF98 | D_800DDF78[8] |
| D_800DDF70 | signed byte at D_800DDF68[8] |
| D_800DDF71 | signed byte at D_800DDF68[9] |

Native tests express these aliases using the same backing arrays. Guest
fixtures preserve the actual addresses. The heap free and activity decrement
services are bounded providers; complete heap behavior and gameplay are not
claimed. Both existing helper sources and linked bodies remain unchanged.

## Compiler and relocation boundary

An explicit record-pointer local initially produced 64 words with 21 register
and spill differences. Naming the resource pointer recovered the register
roles but enlarged the frame to40. Indexed record accesses with one resource
pointer local recover the original 32-byte frame and all register roles.
Only the saved record pointer differs: SP+0x18 instead of SP+0x1C.

The six guards cover all three stores and three reloads at offsets
0x30,0x3C,0x98,0xB0,0xC8,0xD8. They change only the immediate low bits of
sw/lw v1, moving that one closed spill to the original unused slot. Frame,
return-address slot, incoming index home at SP+0x20, opcodes, registers,
control flow and external bindings stay fixed. No word is inserted or omitted.
Every guard has an exact expected word and no relocation at its offset.

The retained assembly spells the D_800DDF20 load's address numerically at
0x15183CA8 and0x15183CB4. Their effective address is exactly 0x800DDF20:
0x800E0000 plus signed displacement -0x20E0. The independent assembly fixture
adds the missing HI16/LO16 annotations only in scratch; the production retail
assembly stays unchanged. C has17 bindings, including this recovered pair.
Three linked layouts test both the pair and all related alias offsets across
HI16/LO16 carry boundaries.

## Original caller and resource list

The retail census finds one direct JAL at ROM0x1B1470 / VA0x15183FC0, in the
252-word func_15183D28. Its delay slot passes the current s0 index; the result
is ignored. No aligned pointer literal names the cleanup target.

64 cases execute every instruction in the original16-word loop at
0x15183F98..0x15183FD8. It scans all eleven live flag/record pairs, calls only
when the flag is -2 and the backing pointer is nonzero, then advances both
cursors. Helper mutations may alter later rows. The parent C placeholder is
not restored or credited by this bounded route.

288 cases connect all25 original instructions of func_1510D630, including
negative/zero counts and positive resource-list loops with signed halfword
entries. The already matched helper decrements each resource and frees its
list. func_1510D694 and func_10004074 remain bounded downstream services;
their complete implementations are not executed by this target's guest test.

## Qualification and production

Both tools copies pass eight fresh canonical checks and shared tools checks.
After installation, each passes two fresh checks and reuses six semantic
checks only under identical module, input and prepared-artifact fingerprints.

- 2,321 guest cases visit all64 target words and test all256 signed flag-byte
  values, all eleven defined rows, shared storage, provider mutations and
  sparse extreme indices. Original and normalized C agree in complete state,
  memory, calls and access traces. Unmodified raw C agrees in public memory
  and calls; its private spill addresses intentionally differ.
- Native32 O0/O2/O3 each pass16,384 cases with trapping UBSan, real pointer
  arguments, actual shared arrays and thirteen effective wrong-C controls.
  Extreme array indices remain guest-only.
- Thirteen IDO-compiled semantic negatives are rejected. The shared-clear
  witness includes a non-mutating free service so later writes cannot mask
  that control. Unsupported interpreter instructions cannot count as a
  successful negative control. The focused oracle implements signed LB;
  all256 flag values exercise its sign extension.
- 66 direct fault-prefix pairs and102 connected-resource pairs preserve
  complete state, PC, delay-slot state and access order after normalization.
  These do not claim portable C fault equivalence for the raw spill layout.
- Three GNU layouts pass144 cases. Eight raw/binding corruptions, all six
  padder expected-word corruptions and thirteen image corruptions fail closed.

The actual three-command Make recipe reproduces the qualified padded object.
Selected, owner and recipe compiler diagnostics are empty. The full build
retains the unrelated duplicate generated_12D630 recipe warning. All eight
other owner functions, relocations and constant pools remain unchanged.

The independent whole-image prediction accounts for exactly266 changed bytes:
204 target code bytes, two target-size bytes (12 ->256), and60 bytes in three
closed symbol/string permutations. The permutations involve D_80095B1C /
D_8009951C / D_8009EF1C, D_800DDF20 / D_80087320, and func_151137D4 /
D_8009E7E8. Every named definition is preserved except the intended target
extent. No ELF byte or metadata region is excluded.

All6,056 function addresses and6,055 other linked bodies stay fixed, along
with189,088 protected Game bytes across720 owners, ELF geometry, shared
headers, Makefile, map and conversion inventory. Six guard rows are appended;
the complete inherited guard prefix is unchanged. The16,435-path seal and390
focused inputs remain pinned through production.

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler body | 1374415707fa28a2254fe640eb95fd8d3b5ad2c66eeb34b5d7cdc7045d8a15f9 |
| Normalized relocatable body | 7ffe0b68d8e84e65af974c184575d72425ffc88c644416910fd0ea01d6de157b |
| Linked retail slot | 90705a513cb844fe9f21ee9e9784e038b2e4bbe4bc64c9e9a46c8c51ff5ac9f9 |
| Adopted object | 170ad43bd7b96ef042fa6ab132cb349aa6a23c698651bcd15fdc8e36307b9a5a |
| Adopted ELF | dce227dc1ef33e0567d6a20080514eb35c67c1208f39cbc5d0f1049292b68976 |
| Guard manifest | b157caa798b975e7e66b2613025c5f3ac127a3a32c12382b5ccf66bc08c99470 |

## Bank and progress

Predecessor consumer: a4237a6a7b50dfba2b186114dc79e0c79d6dccac.
Tools committed first: b59a7a41fd5e13d76562e2ddb4fafabf8b4cae87.
Bank source, six guard rows, tools pin and measured documentation together.
Preserve1,814 inherited dirty paths and three new files in the older tools
mirror. No push or mirror commit. Routine Claude calls:zero.

| Section | Byte-exact C | Address drift | Different |
| --- | --- | --- | --- |
| Total | 3,869 / 5,506 (70.27%) | 0 | 1,637 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,196 / 4,833 (66.13%) | 0 | 1,637 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

261 more exact functions are needed for4,130 /75%. Remaining shapes are1,508
placeholders,120 semantic/other and nine unlocated. Only func_15183C28 gains
credit. Next inspect the remaining252-word dispatcher func_15183D28 in this
owner; func_1514E920 remains parked and uncredited.

Evidence lives under conker/build/game-record-cleanup-match/: private source
screens, independent semantic/native qualification, actual Make preparation,
canonical and installed checks, production/adoption, actual ELF recount and
canonical function views. The closing handoff records the consumer commit,
scoped graph refresh and final audit. Root README receives aggregate rows only.
