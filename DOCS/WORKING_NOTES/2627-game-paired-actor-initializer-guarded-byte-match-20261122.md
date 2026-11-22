# 2627 - Paired-actor initializer guarded byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_151951E0` now contains its complete semantic C body. All **210 retail
words match through 15 expected-word guards**; raw C still differs at 15 words.
There are no inserted/omitted words. Fresh production is **4,609 / 5,528
(83.38%) total**, **3,936 / 4,855 (81.07%) Game**, zero address drift and 919
different converted functions. Init 492/492 and Debugger 181/181 are unchanged.
**90 more matches** reach 85%. The former placeholder already counted as C,
so this is matching credit rather than new converted-function credit.

## Source, ABI and behavior

Source `conker/src/game/generated_1C1150.c`; original
`conker/asm/1C1150.s:1511`. VA151951E0..15195528, ROM1C2690..1C29D8,
840 bytes/frame32, S0@SP14/S1@SP18/RA@SP1C. The recovered one-pointer ABI is
`void func_151951E0(u8 *actor)`. The original call site ignores the return value.

The routine clears health byte 1CA before the mode services, activates state 40,
sets field 3C=-3, and uses five unsigned32 RNG remainders for the original
actor's velocity/spin, paired velocity/spin and angular perturbation. The
allocator result is activated as state 40 with immunity/stunned bytes 255.
Identity, XYZ, facing, scales and six bytes 68..6D copy in the original order;
paired field 3C becomes 10. The final angular perturbation retains the original
float operations, unsigned conversion and FCSR save/restore shape, including
the original coefficient D_800A8704=5461.333496. The final rotation, flag OR
0FFF0000, link copy, resource registration and two ordered transitions follow.
No source/profile/header-wide changes or replacement assembly bodies are used.

## Original caller and allocator domain

The bounded retail census finds one direct JAL at150D0FD8 and no aligned loaded
function-pointer literals. The original caller `func_150D0E90` derives S1 from
first pool entry800CC2D0; nine origin instructions establish the pointer, and
the intervening instruction/ABI audit preserves S1. Its actual two-word
JAL/delay window passes S1 in A0. Seven continuation words ignore the return.
48 cases per stream and an effective missing-delay negative qualify this ABI.

**The current decomp caller remains a zero-return placeholder.** Its complete
596-byte slot is checked as three stub words plus zeros. Original caller
windows are executed for ABI evidence; current runtime connectivity and full
parent behavior are not claimed. Recover this 149-word caller next with its own
qualification rather than crediting it as part of this function.

The original 95-word allocator returns whole 812-byte pool records. Target state 40
excludes source slot 0 from free/recyclable scans, so actual target allocations
are slots 1..25. Original RNG and allocator code is checked against the current
ELF and executed in 444 cases per stream, selecting all 25 eligible slots.
The target connections execute 91 allocator words; three independent standalone
allocator cases cover the four first-slot paths excluded by source activation,
for 95/95 total. All 18 original 64-bit RNG words execute and five seed transitions
are independently checked. Two effective negatives alter record stride/RNG
shift. Lifecycle/reset and the other services remain contracted.

## Guards and complete image

Raw SHA256 `79d97d2a50592c6210c0ac17cc1fb857ea09e515b01f0dcc8262177d6a5821ac`.
Ten guards permute the same setup instructions, moving the identity load across
two disjoint flag-byte stores and rescheduling constants/pointer setup. The
whole-record domain is required: equal-base extra cases pass, while a deliberate
partial overlap witnesses raw/original disagreement outside the allocator's
contract. This is not an all-pointer-overlap equivalence claim. The other five
guards close two volatile register roles for flags and the captured link.
Float operations, 13 binding sites, frame and saved-register lifetime match.

All 28 other raw/padded owner functions and all compact pools are unchanged.
All previous 5,732,449 guard bytes remain an exact prefix; no neighbor guards
are modified. Both padders emit original target bytes/relocations.16 independent
GNU links cover all 13 bindings and HI16 carry boundaries; five controls reject
stale words/relocations, duplicate offsets and wrong replacements. Eight GNU
text-alignment bytes are explicitly zero, separate from the 840-byte body.

Actual mixed Make uses five commands under existing O2/g3 and reproduces the
qualified owner. Production Make/recount passes; the existing duplicate
generated_12D630 recipe warning remains. Complete ELF prediction is literal:
**664 changed bytes, zero exclusions**. The target body/12-to840 symbol size
and two closed metadata permutations account for every changed byte. All five
named symbol definitions/attributes and 55 name bytes are reconstructed.
All 189,088 protected GameData bytes/720 owners, other function bodies/addresses
and conversion rows are preserved. Production ELF SHA256
`c4874bb719f5b8a3e1b10601984344072e1cf1f0ae794f14c032a376ca761187`.

## Fresh validation and limits

- Guest: 848 cases per raw/normalized/original stream, independently varied
  five RNG outputs, all 256 identity bytes, whole-object aliases, mutable
  providers, two stack phases and explicit FCSR/unsigned conversion boundaries.
  Raw complete modeled end states agree in the qualified object domain.
  248 normalized/original access-fault pairs pass.
- 189 of 210 target words execute. The 21 remaining words are the original
  unsigned-remainder correction blocks and one unreachable duplicate transfer;
  all remain literally retail-exact. They are not reported as executed.
- SDK32 O0/O2/O3 each 328 typed-object cases under strict aliasing and UBSan.
  Independent guest-checked vectors compare every actor byte at every call
  boundary, helper writes, final objects and guard canaries. Eleven effective
  source negatives cover health/state, signed remainder, velocity, identity,
  scale, flag mask, link, resource and transition errors. Undefined negative
  float-to-unsigned C inputs remain guest-only.
- Both tools copies pass all five focused checks before/after installation,
  with exact Python and non-Python dependency fingerprints. Shared tools-check
  passes. Real sibling edits and dependency hashes are preserved. Unchanged
  neighbor suites are fingerprinted reuses, not claimed fresh executions.

Baseline consumer `c2809b8bfa050d6d2a1fdcd9fe06a7751efa21d0`, tools `12b7ec9fdaba9912f0d3af478a514cca20f54bac`.
Qualified tools commit `f2e579d8b6fb049b88d58bb4a527cc929fd183ee` is banked
before the consumer pin. No push, real sibling overwrite or host/Release build.
The available host scene input uses a different mapping and consumes binary
code, so no direct C import or gameplay acceptance is claimed. Zero Claude
calls; local source, ABI, compiler and execution evidence resolve this target.

Supplemental storage receipt `_cleanup-20261122-completed-banks/compression-audit.json`
checks 6,257 files in two older completed banks and 2,489 prior immutable inputs
around transparent NTFS compression. Bytes/sizes/times/membership and all Git
states agree, with zero deletion/relocation. Measured volume free space did
not increase in that interval; no recovered-space credit is claimed.

Continue with original caller `func_150D0E90` after this immutable checkpoint.
Older private candidates remain uncredited; the 85% goal stays active.

Graph maintenance: the native update exited 1 with all
70,496 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
70,564 nodes / 165,109 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
