# Horizontal damping callback direct byte match - 2026-11-17

`s32 func_151AFEA4(DampingState151AFEA4 *state, void *context)` now replaces
the zero-return placeholder with the complete horizontal damping callback.
Its **106-word / 424-byte body emits directly from semantic C** under the
existing O2/g3 profile. The existing alignment NOP completes the **107-word /
428-byte slot**. The routine has no frame, guards, insertions or omissions;
the guard CSV remains byte-for-byte unchanged.

The independent actual-ELF recount is **4,538 / 5,514 (82.30%)**, Game
**3,865 / 4,841 (79.84%)**, Init 492/492 and Debugger 181/181. Address drift
is zero and 976 functions remain different. The active 85% goal needs
**149 further matches**. Converted functions/bytes and classifications are
unchanged. Root README receives only its two aggregate matching rows.

## Source, ABI and direct emission

Owner `conker/src/game/generated_1DCA70.c`, VA151AFEA4..151B004C for the body,
slot through151B0050, ROM1DD354..1DD4FC with alignment through1DD500.
The local structure names the horizontal velocity fields at +0x58/+0x60 and
the damping multiplier at +0xA8; all intervening bytes are retained padding.
The original dispatcher integrates those same velocity fields into position.
No shared structure or header ABI is changed.

The callback consumes the current `D_800BE9E4` word as an unsigned countdown,
applies one ordered X-then-Z multiplication per tick, and returns 1. Its
second argument is the dispatcher's context pointer; it is retained in the
interface and is not dereferenced. The original store of A1 to its incoming
home is emitted by IDO as part of the complete routine.

Creating `factor = &state->damping` before assigning `ticks` recovers retail's
V0 multiplier-pointer / V1 counter lifetimes and complete four-way unrolled
loop. Direct field expressions produced an 88-word cached-factor form.
Initializing the counter before the independent factor pointer produced
106 words with a V0/V1 allocation cycle. The selected pointer-first source
matches every word and both relocations without normalization. Unsigned
countdown avoids signed decrement overflow for high-bit input words.

Raw body SHA-256:
`18a89c5cb10c345d4b295eb71b4ba8f0fdb4e5d951e916be6036b675a1277c5d`.
Only the original HI16/LO16 pair for `D_800BE9E4` is bound. The complete
original assembly is independently assembled and agrees with the emitted
object; rebinding at the original address agrees with the retail binary.
The alternate-source draft was inspected only as a reference. Its false
integer views of floating fields and reconstructed compiler loops are not
adopted.

## Focused qualification

All **five final checks pass fresh in both tools configurations**, with zero
failures, errors or skips: **61.43s primary /
51.263s sibling overlay. The existing damping corpus and
instruction/native helpers are reused; this target's compilation and runs
are new.

- Complete owner compilation preserves all **six neighbors** and normalized
  pools. Both real padders process the complete owner and match all 106
  target words; all six padded neighbors retain their production bodies.
- **12 GNU links** cover the original and both padded objects across four
  relocation carry layouts. **108 controls** reject all 106 word corruptions
  and both changed relocation bindings.
- Original, raw and both padded streams each pass **440 guest cases** against
  the independent ordered per-tick reference. All 106 body words are visited;
  complete guest RAM, registers, access order and return value agree.
- **68 access cuts** and **240 high-tick prefix cuts** compare all four
  instruction streams, including 0x7FFFFFFF, 0x80000000 and 0xFFFFFFFF
  countdowns. Those prefixes do not claim completion of enormous tick loops.
- Native32 C compiles fresh at **O0/O2/O3**, each passing 440 finite/signed-zero
  cases under UBSan. Six effective controls reject X/Z addition, wrong factor,
  skipped odd ticks, copying the other velocity component and returning zero.
- `D_80089760[6]` points to this target. The **complete 428-word original
  `func_151303EC` dispatcher** executes **80 selected cases per stream**,
  including tick remainders, two stack phases, and velocity/acceleration flag
  combinations. It supplies the object in A0 and context at parent SP+0x48
  in A1; success bypasses removal. A return-zero control reaches
  `func_1516972C` as expected. These selected paths visit **82 of 428 parent
  words**; the other parent paths and its secondary helper are not qualified.

The first full-parent fixture incorrectly supplied a list where the existing
machine expects an address-to-word connection map. That test failed before
executing the parent body. The connection map was corrected; the focused
parent run and both complete final suites were rerun. The failed receipt is
retained and is not used for credit. Candidate C was unchanged.

Defined native coverage uses ordinary mapped, disjoint objects and the bounded
finite tick corpus. Native private-stack/nonfinite behavior, asynchronous
mutation, hardware traps, cycle timing and gameplay are not claimed. Direct
instruction identity preserves the original target's instruction/FP order.

## Actual build and production audit

The independent actual-Make shadow uses three owner commands: compile, pad and
assemble. The real production Make plan compiles only this owner, then relinks
and recounts. No prebuilt object is copied into production. The installed ELF
equals the independent prediction:
`a0d8b9d6b844eb3332a68c8b3dd9dd08dededef31047546784010c72c386eeb7`.

Strict complete-image accounting changes **326 bytes**, with **zero exclusions
and no metadata reorder allowance**. All other **6,050 function bodies and all
6,051 function addresses** remain unchanged. Exactly **one of 698 objects**
changes; all six neighbors remain exact. All **189,088 protected data bytes /
720 owners** are retained. Four effective corruption controls reject changed
symbol values, symbol-name bytes, protected data and target instructions.

Fresh post-install owner compilation agrees on all seven functions. The actual
production target passes another 440 guest and 80 selected complete-original-
dispatcher cases, visiting all 106 target words. Prior unchanged padder/link,
access-cut and native receipts are reused only with exact task/fixture hashes.
Production match-progress, tools-check and an independent actual-ELF recount
pass. The pre-existing duplicate generated_12D630 recipe warning is unchanged.

## Preservation and next target

There are **1,593 frozen inputs**: 1,586 retained/copied baseline inputs plus
seven additional observed dependencies. Snapshot hardlinks point only to older
immutable snapshots, never the live tree. Exactly three frozen inputs change:
source, owner object and ELF. The five maintained task files and actual imported
helpers are separately fingerprinted. Both tools configurations use those exact
task files; the sibling's **2,434 dirty paths / 343 scoped dependencies** remain
unchanged. Claude calls are 0. The host sibling has no source checkout to
synchronize and remains untouched, including Release/saves.

Evidence is under `conker/build/game-next-151afea4-private/adoption/`: paired
sealed checks/imports, direct object/assembly identities, both full-owner
padders, GNU links/controls, guest/access/native/parent matrices, actual Make
prediction, production audit/focus and recount. Native Graphify update exits
fail-closed on its reduced scan and retains all 65093 old
IDs. A scoped merge of five code files retains every ID and the explicit target
reference; this is not a full-corpus re-extraction. Commit tools before consumer
source, notes, aggregate README rows and pin, locally only.

Next inspect **func_151AFC88**, the 135-word remaining placeholder in the same
owner. The 85% goal remains active beyond this checkpoint.
