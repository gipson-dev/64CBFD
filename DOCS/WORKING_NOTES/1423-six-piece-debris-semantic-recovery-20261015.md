# Six-Piece Debris Semantic Recovery

Date: 2026-10-15. Resume from consumer **2052cc07**, tools **de7c6d8**,
both initially clean. Bank tools **b88e200** first, then the consumer pin
and this handoff. **This is a pre-install recovery checkpoint, not a new
byte match.** Production source, guard CSV, ELF and matching counts stay fixed.

## Steps

1. [x] Audit func_15170B90, the 96-byte packet consumer, the live vector/kind tables and the reference source's incorrect widths and call arguments.
2. [x] Recover typed semantic C with real packet fields and explicit reserved bytes; preserve six unsigned staged IDs, full-word non-table IDs and signed high-half RNG values.
3. [x] Measure full-owner source/layout/profile screens without changing production flags, headers, assembly or other functions.
4. [x] Qualify bounded packet sequences, provider mutations, native32, effective negatives and all 75 frozen/live inputs.
5. [x] Reject installation on the oversized target, different frame and typed-ring neighbor change; bank four tools files before consumer documentation/pin.
6. [ ] Resolve the original 205-word / frame-0x120 target shape and saved-role lifetimes without artificial locals, volatile workarounds or invented calls.
7. [ ] Recover the ring func_151718F0 or otherwise establish its genuine compatible definition before installing its typed caller. Do not bypass the ABI with an incompatible cast or silently change the neighboring placeholder.
8. [ ] Qualify any proposed normalization, all 96 literal packet bytes, caller/rebase and connected-consumer boundaries as appropriate; then rebuild, audit every ELF byte and refresh official counts before installation credit.
9. [ ] Continue every broader Game/additional-source, func_1516D400 and inherited-stack func_1516FE1C queue.

## Recovered Contract

**func_15170B90**, VA **0x15170B90**, ROM **0x19E040**, has **205 words /
820 bytes**, frame **0x120**, ending at **0x15170EC4** with no separate
padding word. Its production owner remains the placeholder in
[generated_19E040.c](../../conker/src/game/generated_19E040.c).

The [experiment](../../tools/experiments/game_six_piece_debris.py) holds the
corrected six-input candidate, retaining address names rather than inventing
unproven retail names:

```c
void func_15170B90(u8 *actor, s32 baseKind, s32 variant, s32 options,
                  u8 flags, s32 context);
```

Snapshot signed halfword coordinates at actor +0x10/+0x12/+0x14 and the
float coefficient D_800A6F94. Initialize the packet's fixed fields once,
not inside the loop. Repeat six times:

- Bit 2 of options has priority: copy exactly six live bytes from D_800A6F80 to a local staging object each iteration and select its unsigned byte. Otherwise retain the entire baseKind word, adding the index with 32-bit wrap when bit 1 is set.
- Call func_1518C900 with that full word. Only after lookup, load the current triple from flat float table D_800A6E90. Add the original coordinate snapshot to form position.
- Velocity is X/Z times the snapshotted coefficient, and abs(Y) times that coefficient plus 7. Make six zero-argument func_150ADA20 calls, using the **signed** high half: three velocity perturbations scaled by 2^-14, then three spin values scaled by 5/65536.
- Store the asset result and low kind byte, then call func_15168BE4(packet, byte flags, word context). Advance the vector pointer by three floats.

Finally call func_151718F0 with origin X, origin Y-80, origin Z, radius 70,
**integer 500**, float bits **0x3B960000**, integer 0, integer 10, byte flags
and word context. This uses two FP-register arguments followed by A2/A3
and six stack words under O32. Set **one byte** at actor +0x6E afterward.
Retail snapshots flags once and reloads context for each call; it also
reloads the actor pointer home after the ring. The current candidate does
not yet match those private-home and saved-register lifetimes.

The reference at
`Another Source/CBFD-Recompiled/conker/conker/src/game/game_19E040.c`
remains unchanged/reference-only. Its coordinate reads, unrelated local
adjacency, truncated asset ID, unsigned RNG shifts, invented RNG arguments
and wide actor-flag store are not imported. Use the existing typed
func_150ADA20 name; do not adopt the reference's unbound random_u32 alias.
The fabsf declaration/intrinsic follows the existing functions.h convention.

## Packet Boundary

Actual [func_15168BE4](../../conker/src/game_1944C0.c) tests asset +0x40,
allocates a record and bcopy's **all 0x60 bytes** to record +0x90 on success.
The producer does not initialize four bytes at +0x44..+0x47 or two tail bytes
at +0x5E..+0x5F. Explicit reserved byte members preserve those holes; do not
zero-fill them. Later fixed fields may retain a submit provider's writes.

| Offset | Contents |
| --- | --- |
| 0x00 / 0x0C | Position XYZ / initially-zero rotation XYZ |
| 0x18 / 0x24 | Velocity XYZ / spin XYZ |
| 0x30 / 0x3C / 0x40 | Initially-unit scale XYZ / lifetime 60 / live asset word |
| 0x44 / 0x48 | Four uninitialized bytes / three snapshotted coefficients |
| 0x54..0x5D | Mode 2, alpha 255, zeros, duration 60, live kind byte, variant byte and two zeros |
| 0x5E..0x5F | Two uninitialized bytes |

Raw/native acceptance compares **90 initialized bytes**, not a portable
value for the six initial indeterminate bytes. Provider-seeded hole values
are checked on subsequent submits. A future normalized/retail literal
comparison must include all 96 bytes and their initial guest stack residue.
This checkpoint does not claim general indeterminate-copy semantics or
that downstream consumers ignore those bytes.

## Measured Compiler Gap

| Candidate | Words | Frame | Length-inclusive differences |
| --- | --- | --- | --- |
| Selected normal O2/g3 | 210 | 0x128 | 205 |
| Saved byte flags | 210 | 0x128 | 205 |
| Earlier coefficient snapshot | 210 | 0x128 | 204 |
| Reordered real FP temporaries | 210 | 0x130 | 204 |
| Word flags plus byte snapshot | 212 | 0x130 | 203 |
| O2 without g3 | 208 | 0x128 | 201 |
| O1 | 249 | 0xD0 | 248 |

The selected raw stream SHA-256 is
`d6b82be73d6ada072ac7fab93cc77d66bf625b1589535dad2478381dd4e54671`.
It has no diagnostic or data/rodata pool. Its 205 difference metric means
**200 same-offset mismatches plus five excess words**, not 205 transformable
body words. Source/profile screens are measurements, not separately qualified
replacements or permission to change production profiles.

Typing the legacy ring placeholder correctly adds four argument-home stores:
SWC1 F12 at SP+0, SWC1 F14 at +4, SW A2 at +8 and SW A3 at +12. Its body
grows **12 -> 28 bytes**; the original three words remain after those stores.
All **seven other neighbors**, their sizes/relative relocations and normalized
pools stay unchanged, including the installed rectangle wrapper. The test
explicitly checks this rejected boundary rather than relaxing a protection
gate. Keep the ring's provisional s32 return/stub status explicit; its actual
effect-only return definition remains a separate reconstruction task.

An attempted no-unroll profile was rejected by the reused asm-processor
argument parser before compiler execution. It is not a measured compiler
profile and was removed from the profile-screen command. The initial fabsf
link failure was resolved with the existing intrinsic pragma. The initial
native harness hex-token spelling `0x5E+i` was corrected to separate tokens;
no production source or compiler option was changed for either fixture issue.

## Fresh Qualification

All **five tests pass in 32.683 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_six_piece_debris -v
python3 -m tools.experiments.game_six_piece_debris --screen
python3 -m tools.experiments.game_six_piece_debris --profile-screen
```

- **1,440 full sequences / 2,880 model runs** compare retail and selected raw C independently against a reference. Cover option priority, full-word/wrapping IDs, negative/extreme coordinates, byte flags, two stack phases, three RNG rotations, zero lookup results, lookup-time live table mutations, later RNG global mutations and submit-time packet mutations. Every one of retail's 205 and the candidate's 210 instructions executes. Each sequence checks six lookups, 36 RNG calls, six packets, ten physical ring words and the final byte store.
- **Native32 O2/O0, 1,024 cases each**, use separate translation units and selected-C UBSan traps, verify struct size/offsets, all initialized packet bytes, provider-seeded reserved bytes, call sequence, formal ring inputs and surrounding actor bytes. No native first-hole value, physical upper-bit, FCSR or hardware claim.
- **Ten compiled guest and native negatives fail effectively**: unsigned RNG, byte-truncated asset ID, wrong option priority, missing abs, wrong spin scale, aligned wide actor store, wrong ring integer, cached kinds, reset fixed fields and vectors read before lookup.
- All **75 captured and live input hashes** are unchanged. Four effective capture corruptions fail. The production owner, guards, ELF, progress CSV, headers, assembly, tables and external reference remain byte-identical.
- Both copies pass Windows syntax and all **eleven shared WSL padder checks**; consumer `make tools-check` passes. Standalone padder tests use unittest **discover**, not the consumer's tools.tests module prefix. New debris suites require the tools repository mounted in the consumer layout.

These are bounded model/native observations, not a symbolic equivalence proof,
literal private-memory comparison, fault-prefix proof, arbitrary provider
mutation theorem, rebasing qualification, connected real allocator/bcopy
execution, hardware or gameplay acceptance. Those boundaries stay open before
any guarded installation. No broader unchanged function suite is called fresh.

## Banking And Resume

Tools **b88e200** contains four new experiment/oracle/native/test files. Keep
the older mirror at HEAD **ddbdd16**, preserve all **747 initial dirty-file
hashes**, and copy four absent owned files hash-equal, giving **751 paths**.
Do not reset, commit or rewrite that independent checkout.

No guest/host build or launch is needed for this pre-install checkpoint.
The protected full-image baseline is unchanged by SHA-256; matching numbers
are the unchanged Note 1422 measurement, **not a newly run progress report**:
Game **2,911/4,828 (60.29%)**, total **3,584/5,501 (65.15%)**, different
**1,917**, drift **0**. Root README stays untouched. No push, Claude call,
host-port or frozen Release operation.

Resume the shape/lifetime gap using the preserved captures under
`conker/build/game-six-piece-debris/`. The typed ring is a genuine prerequisite,
not a reason to drop its prototype or cast around the ABI. Keep this target
and all wider matching queues active; no new match is credited here.
