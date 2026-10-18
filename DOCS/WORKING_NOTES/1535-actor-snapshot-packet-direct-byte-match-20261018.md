# Actor Snapshot Packet Direct Byte Match

Date: 2026-10-18. Consumer predecessor **65278bf2**, tools predecessor
**4d3a3d8**. Restore **func_151AB930**, owner `generated_1D6E80`, VA
**0x151AB930..0x151AB9C8**, ROM **0x1D8DE0..0x1D8E78**. The wider Game
matching goal remains active; this is one completed function.

## Recovery And Stack Layout

Replace the false no-argument s32 stub with commented **void C taking an actor
byte pointer**. A local struct captures the actor pointer, unsigned byte at
+0x3B, promoted unsigned halfword at +0x84, 0.0f, the original D_800A9014
float, 3.0f and the selector helper's returned byte. D_800A9014 is
**0x3ECCCCCD / 0.4f**; its existing data/source are unchanged.

The struct is **0x1C bytes**, at **SP+0x28** in the original **0x48-byte frame**.
Offsets **5..7 and 25..27** are six inherited padding bytes, not initialized
fields. The original copies all 28 bytes after allocation succeeds. Do not
zero-fill, narrow the copy, or claim the native C padding representation is
deterministic. The exact compiled guest code, not a portable C padding rule,
proves this retail behavior.

The first complete C form already has the correct 38 words/frame/schedule;
only eight packet-home offsets differ by +4. Moving the destination-pointer
declaration before the local struct puts it at the original home. This second
form emits **all 38 words directly under unchanged O2/g3/MIPS2/o32**: no guards,
profile overrides, instruction insertion/omission, padder or Makefile changes.
All **40 raw owner neighbors**, relative bindings and compact pools stay fixed.
The owner emits no compiler diagnostics.

## Qualification And Padding Boundary

New tools: `experiments/game_actor_snapshot_packet.py` and
`tests/test_game_actor_snapshot_packet.py`. Ignored artifacts:
`conker/build/game-actor-snapshot-packet/`. Twenty inputs pin the whole ELF,
owner/caller sources, actual caller object, guards/ROM/assembly, build/layout,
symbol/header/data inputs and all four prepared compiler components.

All **seven pre-install tests pass in 37.838s**; all **seven installed tests
pass in 43.307s**:

```sh
python3 -m unittest tools.tests.test_game_actor_snapshot_packet -v
```

**6,000 paired guest cases** cover unsigned field boundaries, selector-byte
truncation, low/high actor pointers, two stack phases, null and unaligned
allocated destinations, and selector/allocator mutations after snapshots.
All 38 target words and all eleven actual SDK memcpy words are visited.
Public memory matches an independent field/order reference; candidate/retail
whole memory, registers and FPRs agree. All six copied padding bytes are
included and vary with the incoming stack pattern.

**70 extra guest probes** cover packet/return-spill aliases and raw constant
bit copies, including signed zero and nonfinite bit patterns. The reference
models the retail RA spill before aliased input reads. Allocation observations
and post-helper copy observations are distinct when a callback changes aliased
packet memory. Saved-RA-alias probes exclude mutations that would corrupt the
return address; this is an explicit valid-return boundary, not a C safety claim.

Native32 **O2/O0 with UBSan** each pass **2,592 cases**, checking semantic
fields, full eight-argument factory calls, failure and external canaries.
Only the six padding bytes are excluded. Four signed-half/live-fields/live-scale/
short-copy controls exit with explicit wrong-result status23 in native tests
and change guest memory. A zero-padding form also passes native semantic checks
but changes copied guest bytes. The first shifted-home form is independently
rejected by guest memory comparison. These six guest controls prevent native
field-only checks from certifying a wrong retail packet representation.

Six independently assembled original/C links at three placements pass
**54 paired sequences**, rebasing the constant and all three helper targets.
All **38 raw words / five bindings / 40 live-and-frozen input mutations** are
corruption-gated; nested historical views are rejected. **1,920 fault prefixes
across 36 states** compare complete memory/register/FPR/call/PC state, including
actual memcpy accesses. These qualify emitted order in the bounded guest
model, not hardware MMU/FCSR policy or portable C fault semantics.

## Actual Caller And Helper Chain

The direct caller **func_1506FF50** loads D_800D154C and ignores the scalar
result. Its local forward declaration is corrected to **void(u8 *)** with an
explicit byte-pointer cast at the call. No shared header is edited. All
**328 raw caller-owner functions**, bindings and pools stay fixed; its complete
production object remains byte-identical. Existing **34 Warning712 and two
Warning709** diagnostics are unchanged after only scratch-basename and the
known one-line prototype-insertion adjustment. No new warning is introduced.

The actual retail/production bodies are equal: **10-word caller**, **19-word
func_151D8E20**, **28-word func_151491F4 wrapper**, and **11-word memcpy**.
The selector returns 10 if D_800BE9F0 is zero and func_150A29C8(0,0x1C) returns
zero; otherwise it returns D_800E0A10. It is not an RNG. The allocator wrapper
forwards the eight public arguments while inserting its ninth-call -1 field.

**48 actual caller/helper chains** cover both selector gates, both downstream
query outcomes, three global selector bytes, allocation failure/success and
two stack phases. They check the complete expected packet, all six original
padding bytes, forwarded arguments, copy and saved ABI state. Only the inner
query **func_150A29C8** and allocator **func_15149130** are scripted boundaries.
This does not claim the complete allocation subsystem or gameplay is restored.

## First Prediction And Actual Build

Before production edits, substitute only the qualified owner in a copy of the
current full linker script. This predicts the **3,257,636-byte complete ELF**.
The separately qualified caller has an identical complete object, so its
declaration/cast does not alter that first ELF prediction. Original owner/ELF
fixtures remain immutable; the later caller-source fixture extends the same
prediction without rewriting its original owner/ELF successors.

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_1D6E80.c.o build/src/game_981E0.c.o \
    build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

The installed ELF equals that first prediction exactly: **119 changed bytes =
118 target-code bytes + one target symbol-size byte**, at file offset2926059.
Target st_size changes **12 -> 152**, with zero metadata exclusions. All
**6,057 bodies/addresses** and canonical symbol definitions are audited;
only the target body and extent change. Actual padded owner bytes/bindings
match qualification; the entire caller object stays fixed. Guards, Makefile,
headers and original constant/data sources remain fixed. Game data stays
**189,088 bytes / 720 owners / zero differences**.

| Prepared Artifact | SHA-256 |
| --- | --- |
| Complete installed ELF | `db45bf1c6025f9a265e35df1671986996d3e81230b2879d3187c890f3aeb30a1` |
| Complete owner source | `e6f4d1e63adc28a0a76e8e223fe26bc8ee47e160a7d0a99388129eba2006e9d0` |
| Corrected caller source | `07c26340d73cc90060d92e03c870b270e1f10141a9e02759f5a8e8f495ed6b45` |
| Unchanged caller object | `b4afd346661f95805348f9e1f28bf6b3bab6e43a11a68ce71020732da49767a2` |
| Raw target object | `fa3aed733b58109f80a3c4f3ba95c91a90381f4d6a2a550ddfffb0fa2de99fe4` |
| Linked target bytes | `bfbfff525419f43f36af3ad290aa7568e1cb80ca774e0ac7b95a1968881bbcd6` |
| Unchanged guard manifest | `625033dd1c2150ce2edb45badf13c05d09aa95b83a0c2b1231e092105d3fc2b3` |

The source/caller/ELF historical view rejects unknown/mixed or nested states,
retains physical raw reads for audit and leaves older fixtures/helpers/hashes
unchanged. Future work should freeze this new live baseline directly.

## Bank And Next Action

Tools **0f19fe7** is committed before the consumer source/docs/pin. Both local
copies pass eleven shared padder tests and project-tools smoke checks, four
Windows ASCII/AST parses and two exact task-file comparisons. Preserve older
mirror **ddbdd16**, all **1,196** initial dirty hashes and its history; add only
two absent paths for **1,198** dirty paths. No mirror commit/reset, push,
Claude call or host/frozen Release edit/build/launch occurs. Unchanged broad
neighbor suites remain prior receipts, not freshly rerun tests.

Fresh official totals: **Game 2,973/4,828 (61.58%)**, total
**3,646/5,501 (66.28%)**, **1,855 different**, zero address drift. Conversion
counts/bytes remain unchanged. Root README changes only two aggregate rows.

Scoped graph refresh completes at **42,432 nodes / 82,504 links / 4,077
communities**, preserving the **19,398 excluded nodes / 2,972 existing files**.
All old IDs survive except three shifted UPDATE_LOG heading IDs, whose labels
remain represented. The target resolves to source line165 and its caller to
line1144; this note has seven graph nodes. Graph outputs remain ignored local
research artifacts, not production inputs.

Next recover **func_15022848**, owner `generated_49D30`, VA
**0x15022848..0x150228E4**, ROM **0x4FCF8..0x4FD94**, **39 words/frame0x28**.
Only when the indexed byte at D_800C35EA is exactly one, clear D_800C3638,
iterate from zero while less than the live byte at D_800C363A+index, calling
func_15022398 then func_150222E0 with (ordinal,index), and set D_800C3638 to one
even for an initially empty count. Audit actual callers/helper contracts and
callback changes to the live count before choosing the C interface. Handwritten
func_150A76F0, both fade gaps, other gate, additional-source, caller and
inherited-stack work remain separate and open.
