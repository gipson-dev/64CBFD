# Game Owner Point Initializer Zero Read And Induction Audit

Date: 2026-10-09

## Result And Boundary

Continue complete func_151B3A7C from
[Note 1186](1186-game-owner-point-initializer-frame-and-private-home-fit-20261009.md).
VA0x151B3A7C..0x151B3CF0, ROM0x1E0F2C..0x1E11A0, retail157 words/628 bytes.
Parent baseline9406bbf9, mounted tools977010c; both clean initially.
The previous goal turn made committed fitting progress. Single Codex writer,
zero Claude calls, no host/OGL/Release/save/editor changes or push.

The [new driver](../../tools/experiments/game_owner_points_initializer_induction.py)
recovers explicit second-vector stores without the prior extra public zero reload.
Interleave the initial scale and position updates using their real dependencies.
Selected complete diagnostic body has158 words/frame0x60 and110 word differences.
It keeps SP+0x44 position and SP+0x08 saved-FP homes and all ten private advances.
Actual public read footprint/multiplicity now matches retail:13 reads per call.

**Not installed: one word too long.** The actual owner/padder rejects632 bytes
against the628-byte slot. No guard, profile, production source or conversion/
matching credit changes. Preserve the earlier full-slot157/frame96/137-difference
body separately; this158-word diagnostic does not supersede its slot fit.
The second vector's velocity label remains a candidate name, not recovered meaning.

## Source And Instruction Evidence

Keep typed position copies and the actual actor prefix. Use three explicit f32
second-vector stores at record offsets12/16/20, addressed from actor+0x48 and
the24-byte index. This lets IDO retain a separate zero-store address cursor instead
of coupling it to the position-copy base and reloading zero from public memory.
No new dependency, fake frame padding, assembly binding or literal-word lookup.

Selected staging:compute step.x, advance position.x, compute step.y, advance
position.y, compute step.z, advance position.z. All scales still load after the
complete first record stores. Subsequent positions use repeated binary32 additions;
no index-times-step replacement. Ten records and ten private advances are retained.
Keep final fresh flag-byte read, clear only bit2 and return1.

The old full-slot loop has one extra zero-load instruction executed twice, at
actor+0xA4 and actor+0x104. The new body makes neither read. A fresh negative
comparison detects both old reads; the new footprint gate is not vacuous.
Read order, FP exception ordering and hardware/FCSR behavior remain separate.

Both retail and the new body begin the four-record loop at offset0x11C:
71 setup words. Retail loop has79 words and tail begins0x258; new loop has80
words and tail begins0x25C. Both have seven tail words, but not all words/registers
agree. New offset0x238 emits SLT AT,A1,V1 and0x254 BNEZ AT; retail directly
branches on the integer counter/end at0x250. This is the remaining one-word
**structural length** boundary, not a claim that only one word differs overall.

## Discriminating Controls

135 complete forms are screened over four geometry patterns/two stack phases.
Only the selected diagnostic receives full qualification; ordinary fixture
agreement is not full alias/native qualification for every control.

| Complete form | Words | Frame bytes | Differences |
| --- | ---: | ---: | ---: |
| Prior full-slot typed chain |157|96|137|
| Typed loop zeros separated |156|96|151|
| Direct not-equal termination |235|96|230|
| Raw second-vector stores/chains |159|96|141|
| Explicit raw second-vector stores |158|96|115|
| Selected raw stores/interleaved first updates |158|96|110|
| Masked counter diagnostic |157|96|114|

Do not choose the masked counter simply for its lower raw difference count.
It adds a redundant ANDI and still reads public zero data; it is not recovered
retail control. Typed-loop separation removes a word but leaves the setup short.
Direct equality/inequality and goto forms add a four-record remainder path;
moving the real counter update between record copies does not remove it.
Alternative point origins, signed/unsigned-difference predicates, scalar-zero
locals, chain permutations and copied-position access forms do not finish the fit.
Some diagnostic views use shifted/negative indexes; guest observations for these
are not portable-C/native qualifications. The selected body uses ordinary actor
offsets and the actual in-bounds typed point array.

Selected regular profiles:O2/g3 158/frame96/110; O2 158/frame96/91;
O1/g3 and O1 291/frame56/291. Keep production O2/g3 unchanged.
No-unroll0 screen covers the initial44 control forms; no-unroll1/2/4 controls
on three named bodies likewise do not recover the slot. Their extra screens
are measurements, not production profile changes or full qualification.

## Qualification And Preservation

[Target suite](../../tools/tests/test_game_owner_points_initializer_induction.py)
uses the existing guest/native32/compiler/owner/relocation helpers. It explicitly
rejects installation even when bounded semantic comparisons pass.

- All135 forms pass eight ordinary fixtures each; zero compiler diagnostics/pool
  bytes. Selected complete-body profile comparisons also pass ordinary fixtures.
- Full selected guest coverage:2,048 cases/4,096 executions, all256 flags,
  four geometry bit-pattern sets and two stack phases; all157 retail and158
  candidate words reached, saved GPR/FP restored.
- Native32 actual selected source:8,192 finite cases, all actor and canary bytes.
- Independent scales/first-record constant aliases:44 cases/88 executions and
  six effective compiled negatives for flags/return/count/increment/scale/zero.
- Complete original81-word registered update:32 cases/64 executions; actual
  D_8008FAF8[0] pointer and one-argument success-return ABI retained.
- Four symbol sets/eight independent links:32 cases/64 executions, all six
  original relocation uses retained. Explicitly read157/158 words respectively.
- Copied actual owner:16 neighbors/pools/relative relocations unchanged, zero
  diagnostics; raw target equals isolated632 bytes. Actual padder rejects overflow.
- Four missing-byte faults/eight executions retain the bounded public prefixes;
  two missing unused bytes/four executions still return normally.
- Exact final private memory/footprint:16 cases/32 executions; original frame,
  SP+0x44 position/SP+0x08 saved-FP homes and no extra private writes.
- Native32 sizes/offsets retain the0x138 actor prefix,12-byte position and24-byte record.
- Public read footprint:8 cases/16 executions,13 reads per call, identical
  address/size multiplicities and no reads from the ten output records.

Initial suite run:12 tests in125.021s, one fixture failure. The reused typed-zero
negative did not change the new raw-store source. Adapt that mutation to the
actual first raw zero store; assert source replacement and compiled rejection.
Do not weaken the mutation gate or infer a production bug from this fixture.

Final fresh command:python3 -m unittest
tools.tests.test_game_owner_points_initializer_induction -v.
All12 tests pass in112.575s, zero skips, including all six effective negatives.

Production source/ELF/guards/progress SHA-256 remain exactly as Note1186.
Protected Game data remains189,088 bytes/720 owners, unchanged and exact.
Fresh make tools-check passes. No production rebuild is needed with unchanged
source/profile/data/guards; prior Note1184 build receipt is reused explicitly.
Fresh matcher:total3,416/5,489 (62.23%), Game2,743/4,816 (56.96%), Init492/492
and Debugger181/181 exact; zero drift/2,073 different. README aggregates unchanged.

Final explicit graphify update . exits1, refusing39,084-to-17,310 node shrink and
retaining19,398 nodes/2,972 existing files outside the scan corpus. Preserve
version/zero-node warnings and existing graph; no force/purge/install.
Ignored receipts live under conker/build/game-owner-points-initializer-induction/
and conker/build/game-owner-points-initializer-induction-test/.

Mounted tools563f37f1386ceb05bf360ccee6e46b9d0246659c commits the driver and
suite before the consumer documentation/pin. No push. Older standalone HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a remains unchanged; all126 existing
dirty entries and both tracked dirty-file hashes are preserved. Only mirror the
two absent authored files, yielding128 entries; no older commit/reset/push.
Fresh documentation check:173 documents/4,560 relative links, zero broken;
all93 authored tooling files parse and match their exact mounted/older mirrors.

## Next Match Boundary

Recover the direct integer counter/end branch while keeping the separate zero
cursor and complete158-word diagnostic contract. Recover the157-word slot from
real source/control shape, not an artificial mask, frame patch or retail lookup.
Then fit the remaining closed GPR allocation and independent FP/setup schedule.
The one-word overflow is not the entire matching problem:110 differences remain.
Any normalization requires closed lifetime/memory/control proof, effective
negatives and complete independently linked qualification before installation.
Hardware/FCSR/full cleanup/walker/live rendering/gameplay remain outside this audit.
The wider Game goal stays active.
