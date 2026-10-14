# Game Actor Burst Packet Direct Match

Verified locally: 2026-10-14. This is retail guest matching, not host-port,
hardware or complete-game acceptance. Keep the wider Game goal active;
preserve frozen host Release, real saves, unrelated work and older tools history.

## Target And Baseline

- `func_1506A5F0`, owner `conker/src/game/generated_97AA0.c`.
- VA `0x1506A5F0..0x1506A6FC`, ROM `0x97AA0..0x97BAC`.
- Complete67-word /268-byte routine, frame `0x78`, ordinary O2/g3/MIPS2.
- Consumer `9ffab1512c8cec3ab12a07b3df812c46a3a2e2db`, tools
  `7f557cd8ab1951e280f8dbe061a0af04acc001d1`; both active trees initially clean.
- Before source SHA-256
  `c84410d77e5e56f893997cd7de2b1ee15a6be993dc7434dafd7ee264bedffb65`.
- Before ELF SHA-256
  `9ba0f2793d2c40711359d86135f7408814827df987aae711c5dc153922ec9772`.

The older mirror begins at ddbdd16 with457 recorded dirty-path fingerprints.
Ignored snapshots and receipts are in
`conker/build/game-actor-burst-packet-match-test/`; all snapshot bytes are
validated against their pinned manifest before qualification.

## Recovered Packet

Replace only the zero-return callback and add its local packet type, six float
declarations and four-slot consumer prototype. Reuse the existing SDK include.
The callback accepts an actor pointer and unused second32-bit argument, then
submits `func_151A6F00(&packet,1,255,1)` without adding an actor-validity gate.

The complete315-word retail consumer establishes the mixed field widths and
mode1 read boundary. The type is naturally four-byte aligned, size0x5C; the
actual local starts SP+0x1C, RA SP+0x14, incoming homes SP+0x78/+0x7C.

| Packet Offset | Assignment |
| --- | --- |
| 0x00 | signed short count3 |
| 0x04/08/0C | raw actor float bits from actor+0x14/18/1C |
| 0x10 | signed short duration90 |
| 0x14 | raw D_80099A10 bits, frozen value0x43178000 |
| 0x18/1A/1C/1E | signed shorts0,255,-64,40 |
| 0x20/24 | D_80099A14 /D_80099A18 bits |
| 0x30/34/38 | float zero direction components |
| 0x3C/40/44 | D_80099A1C /D_80099A20 /D_80099A24 bits |
| 0x48 | float zero assigned using integer literal0 |
| 0x4C/50 | float constants-4.0f /8.0f |
| 0x54/55 | zero bytes |
| 0x56/58 | signed shorts50 /25 |

All14 holes remain untouched: bytes02/03,12/13,28..2F,5A/5B. In particular,
28/2C are actual alternate-mode float fields, not universally unused memory.
The mode1 consumer never reads them. Do not zero the aggregate or manufacture
values for its unwritten fields. Native qualification inspects assigned fields
only; guest hole/cut qualification is not a portable-C padding promise.

The simplest complete field-order body with `packet.unk48 = 0.0f` emits66 words
and35 differences. Changing only that assignment to `packet.unk48 = 0` recovers
all67 words, including retail's second independent FP-zero materialization.
The float value remains identical; the compiler's typed expression differs.
Double literal0.0 and explicit(f32)0 also match. This is measured source-form
provenance, not proof of the original source spelling.

The final40-form screen has four exact O2/g3 entries: selected-integer-zero,
last-zero-0, last-zero-0.0 and last-zero-f320. Select ordinary integer0.
Archive the earlier16 and36 screens separately:88 measured forms total.
Plain selected O2 without g3 emits66 words; O1 emits77. Chained-zero controls
can change length and frame; decode the unique real negative SP adjustment
instead of assuming the first word. No volatile declarations, dummy locals,
profile changes, assembly replacement or instruction guards are installed.

## Qualified Gates

Fresh pre-install run: **17 checks pass50.364s**, comprising the original13
target gates, two protected text checks and prior mode1/descriptor shapes.
Fresh installed run, with exact serialization gates added: **18 checks pass
100.732s**. Both tools copies pass project checks and Windows byte-compilation.

- **10,800 guest cases**: all12^3 raw actor triples, six independently varied
  coefficient axes, three provider behaviors and two SP phases. All67 words
  are reached. Independent reference ordering, complete modeled state,
  initialized packet bytes and public access/call traces agree.
- **108 aliases**, including24 independently assembled/relinked original and
  emitted alias pairs: public actor/coefficient overlap, private packet fields
  and incoming homes. Retain actual retail read/store ordering.
- **72 required-byte prefixes**: every byte of all nine input words at both
  SP phases faults before submission. Removing every packet hole still works.
- **Six effective semantic controls**, guest and native: wrong count,
  coordinate, radius coefficient, kind, slot and signed angle.
- **20,736 native32 cases per profile**, O2 and O0: raw actor/coefficient
  patterns, four public alias arrangements, three provider behaviors, actual
  packet offsets and all seven input-arena canaries. Keep warning gates,
  SSE, stack realignment and no-strict-aliasing flags; do not read padding.
- **15 neighbors**, normalized pools and relative relocations remain fixed.
  Both complete owner padders agree and preserve the raw direct target.
- **Three carry-boundary links**,18 semantic cases, preserve all67 words,
  actual HI/LO carries for six data symbols and JAL encoding.
- **1,404 fired access pairs** across36 domains cover all39 root accesses.
  Provider accesses are excluded. The rejected float-zero form differs at
  effective cuts18..38 despite matching the final float values.
- Effective ELF header/slot/tail, prior mode1, target symbol name/size,
  source and guard corruptions remain rejected. All16 record/string corruptions
  across the exact serialization groups and a corrupted baseline definition
  are rejected without broad metadata exclusions.

Root float values are copied, not arithmetically transformed. Raw NaN payloads
do not qualify NaN arithmetic. Native proof is bounded32-bit behavior; guest
private aliases and fired cuts do not prove portable fault semantics, full
hardware FCSR, alternate rounding modes or hardware PC/BD.

## Original Consumer Boundary

Independently assemble and link the complete315-word func_151A6F00 from the
unchanged retail assembly, requiring exact ROM word identity. Production's
consumer is still nonmatching and its C body still returns zero. Do not confuse
test-connected retail execution with restoring that provider into production.

**24 connected cases** execute the actual38-word dispatcher/table0, complete
retail consumer and original11-word memcpy where reached. Verify table0 at
VA0x80086110 /ROM0x22ABD0, forwarded arguments, mode1 branch, three iterations,
six integer RNG calls and18 float RNG calls. Qualify factory failure, object
success/animation failure and both successes, with both SP phases, direct and
parent calls, and all14 root-packet holes removed. No consumer read touches
those holes in this declared mode1 domain.

RNG, trig, random-float, object factory and animation allocation remain bounded
hooks, not reconstructed/qualified game systems. The local DIVU/MFHI and finite
NEG.S decoding extensions have positive controls; zero divisors are explicitly
outside this connected domain. Original scalar/FP saved lifetimes and complete
original/source states agree under these hooks.

The first four-check attempt failed because the fixture omitted its real
memcpy call-record handler. Add that handler, not a production workaround;
the repaired consumer/opcode pair passes2 checks2.360s before the full run.
That initial failed run is not an acceptance receipt.

## Closed Linked Audit

The first strict image gate exposes three legal adjacent symbol/string
permutations. The complete20,318-row symbol table preserves every definition except the
target's declared size12 ->268. Test-only expected-image construction asserts
each exact definition, original record/string order, adjacency and offsets,
then applies only these three permutations:

| Before | After |
| --- | --- |
| D_80099A18, D_800962E8, func_150F00EC | D_800962E8, func_150F00EC, D_80099A18 |
| D_80099A20, D_800E0D20 | D_800E0D20, D_80099A20 |
| D_80099A14, D_800CC284, D_800A3D14 | D_800CC284, D_800A3D14, D_80099A14 |

Whole-image equality follows before parsing current symbol metadata, so a
malformed string offset cannot evade the corruption gate. No production bytes
are normalized or any metadata section excluded. Three fresh installed audit/
corruption checks pass9.339s before advancing the protected fixture.

Exactly **292 bytes change**:214 instructions, one target-size byte,35 symbol
record bytes and42 string bytes. Every other ELF byte, layout, pool, neighbor,
profile, guard-history byte and conversion row is fixed. All189,088 protected
Game data bytes across720 owners remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Installed Input | SHA-256 |
| --- | --- |
| Source | `995e422e3bd894456f6fbedb11ab374d493eb8ea6f522faf14a260fdc0295002` |
| ELF | `50b064c6d7af59a7a78eeece1a2b3c8e32b2886b1695097fd6b43044f2b092ee` |
| Guards, unchanged | `8b3792e3d9fe28cc2aec346ee217edc66cf5e5f7190f88193c3213183a5f3661` |
| Conversion CSV, unchanged | `14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b` |

Fresh Game **2,832/4,823 (58.72%)**, total **3,505/5,496 (63.77%)**,
different **1,991**, drift **0**. Converted functions/bytes stay unchanged
because the false-C placeholder was already counted. Root README updates only
snapshot date and two matching rows; detailed recovery stays in DOCS.
The pre-existing generated_12D630 duplicate recipe warning remains; no new
target diagnostics, ROM build, host launch or dependency installation.

Validate and archive all nine protected text snapshots plus manifest under
`actor-burst-packet-before-rebase/` before advancing only the independently
qualified ELF snapshot and one pin in both tools copies. Other eight inputs,
the guard pin and every immutable-input corruption control remain fixed.

## Banking And Next Work

Tools `23e45f5ece7ad270f6753dfbc5291f90704009d3` banks the two new tools and
one verified text ELF pin first; the consumer records that exact revision.
The older mirror retains HEAD ddbdd16 and456 of457 initial fingerprints.
Only its text test receives the verified pin; two absent byte-identical tools
bring its dirty count to459. No mirror commit, reset or push.

Direct Graphify update refuses18,849 proposed nodes versus40,627 retained,
preserving19,398 nodes from2,972 excluded-but-existing files. The existing
skill0.9.20/package0.9.26 and zero-node devcontainer warnings remain explicit.
Record incremental/post-bank receipts below; do not force shrink or install
another package to bypass the fail-closed gate.

Next **func_151A6F00**, owner `conker/src/game/generated_1D43B0.c`, line7:
VA0x151A6F00..0x151A73EC, ROM0x1D43B0..0x1D489C,315 words /1260 bytes,
frame0x168. Recover the complete count loop, four kind branches plus default, random/trig
calls, staged descriptor, object creation, conditional memcpy/animation paths
and saved-register lifetime. Reuse the packet/read-boundary and original link
receipts here, but broaden beyond mode1 before installing the consumer C body.
That placeholder remains unchanged. There are now no zero-return placeholders
in generated_97AA0, but other nonmatching routines and the wider Game backlog
remain open.

Reproduce in the prepared consumer under WSL:

```sh
python3 -m tools.experiments.game_actor_burst_packet_candidates --profiles
python3 -m unittest tools.tests.test_game_actor_burst_packet_match \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls \
  tools.tests.test_game_actor_vector_mode1_match.GameActorVectorMode1MatchTests.test_01_complete_direct_words_profiles_and_real_frame_measurement \
  tools.tests.test_game_actor_descriptor_spawn_match.GameActorDescriptorSpawnMatchTests.test_01_complete_direct_slot_two_screens_and_real_local_order -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Post-Bank Verification

Consumer `b3df40d18458ddcbbc7391249ae85d9b8bef1c24` banks the installed
callback/type, exact tools23e45f5 pin, aggregate date/rows and detailed docs.
Both active trees are clean before this receipt-only update. Seven fresh
post-bank checks pass **14.316s**: direct shape, literal image/protected
history, every fired own-access cut, image/source/guard/symbol corruptions,
closed serialization accounting and both protected text gates.

All four installed hashes above remain fixed. The exact292-byte accounting
and all20,318 symbol records retain the declared boundaries. Reuse the fresh
matching totals measured from these exact ELF/progress hashes; do not infer
credit only from the isolated candidate. All five Note1352 index links resolve.

The recovery commit's incremental graph hook finishes **40,637 nodes /81,116
edges**,3,719 communities, with no worker remaining. The fail-closed retained
19,398 nodes /2,972 excluded-but-existing files remain explicit. No forced
shrink, package replacement or graph output commit is performed.

Post-bank older-mirror inventory retains HEAD ddbdd16 and all459 post-update
fingerprints. The task changed only its independently verified text ELF pin
and two absent additions; all456 other initial fingerprints remain fixed.
No mirror commit/reset, push, ROM build or host Release work. The still-stubbed
func_151A6F00 in generated_1D43B0 remains unchanged; continue its full consumer
recovery next without reducing the wider Game goal to this completed callback.
