# Inline Descriptor Pair Callback Guarded C Match

Date: 2026-10-22

## Result

Recover `func_151BC5A4` in `conker/src/game/generated_1E73B0.c` from its
zero-return placeholder. Complete C emits **42 words, a 24-byte frame and
one call binding**. One checked commutative branch-operand guard makes the
linked body byte-exact. This is guarded C, not compiler-only matching.
No inserted instructions, dummy locals or compiler-profile changes.

VA151BC5A4..151BC64C / ROM1E9A54..1E9AFC, ends exclusive.
Preserve `conker/asm/1E73B0.s` and all existing GLOBAL_ASM bodies.
Raw unlinked body SHA-256:
`006f7d76bc4c09b30ad199c5bfea553ad2937600feda57d8287a2cc93df3a1e2`.
The old body was 12 bytes in a 168-byte slot. One additional exact match,
with the converted-C count and denominator unchanged.

Keep the address-based public name and descriptive parameters/comment.
Recover `void func_151BC5A4(struct102 *, s32 eventAddress, u8 command)`,
matching its existing caller declaration. Use local byte-pointer views for
the inline pair; do not reinterpret the generic struct's halfword fields as
the recovered word/tag layout or change the shared struct for this task.
Move the existing structs.h include above the canonical release-helper
declaration and cast the existing `func_151BFBFC` call accordingly.
All 56 other owner functions still emit identical code. No caller-source or
shared-header changes.

## Recovered Contract

Read the full inline word at owner+0x40 unconditionally, before testing the
command. For command zero, compare it with event word0. Equality skips both
byte loads and calls `func_1516972C`. Otherwise read event byte4 before owner
byte0x44, and call the helper if they match. Preserve OR short-circuiting.
Commands other than zero/0x2D still perform the initial owner-word read but
do not read the event payload.

For command0x2D, form the inline pair address, reload its word before reading
event word0, and keep that event word for the reverse update. If the first
event key matches, store event word4 to the inline word, then read event
byte9 and store the inline tag. Otherwise compare event word4 with the cached
state word; on equality store the cached first key, then read/store event
byte8. The first match wins. Late byte reads matter under overlapping records.

Store the full incoming command word at original SP+8 before masking it to
a byte. Guest home/alias cases qualify emitted ABI behavior, not portable C
parameter-storage guarantees. The real caller forwards a masked byte and
ignores the result. Historical source spelling is not unique.

The initial source emits 41 words with 37 differences. Establishing the
inline pointer early and reusing the first-key variable recovers all 42 words
and leaves only one commutative branch difference. Reversing the source
comparison does not change IDO's operand allocation. Do not pad the rejected
41/43/47-word variants or install their differing saved-register lifetimes.
An early mixed-declaration probe was rejected by IDO's C parser; it is not
qualification evidence.

## Guard And Binding

| Offset | Expected | Replacement | Meaning |
| --- | --- | --- | --- |
| 0x084 | 0x548A0005 | 0x55440005 | Swap a0/rs4 and t2/rt10 in bnel |

Keep opcode21, displacement5, target151BC640 and its delay instruction.
Full-register inequality is commutative. Derive the replacement from those
register fields, pin the entire raw body and bindings, reject changed inputs,
and append exactly one row with the old CSV prefix intact. The only binding
is R_MIPS_26 `func_1516972C` at offset0x40.

All 42 static words match; 41 are dynamically visited. The duplicate load at
151BC624 is statically unreachable and reproduced, not runtime-exercised.

## Caller And Helper

The prepared aligned retail input has one direct JAL at ROM16216C /
VA15134CBC in `func_15134C98`, and no aligned literal target pointer.
These are static-reference observations, not exhaustive runtime-target proof.
The graph supplies three relevant nodes/55 edges; source and instructions,
not graph edges alone, establish the call interface.

The original/current caller is 15 words, frame24. It reads owner byte0x28,
calls only for value1 and forwards the object, full event-address word and
byte command. Execute all its words over 160 phases with gates0/1/2/3/255
and poisoned command upper bits. Native checks compile the actual C caller.

Connect all 28 original/current `func_1516972C` words across 32 phases.
Exercise types0/1/2/255, pre-helper type mutation and reload, stride52 callback
lookup, callback and fallback paths. Keep `func_151696DC`, `func_15169804`
and the indirect release callback as bounded providers. No complete allocator,
free chain, hardware or natural-gameplay acceptance is claimed.

## Qualification

Tools: `experiments/game_inline_pair_command.py` and
`tests/test_game_inline_pair_command.py`, identical in both copies.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests,147.985s | 8 tests,118.930s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests,1.829s | 2 tests,1.832s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks per copy only under strict
source, raw/padded object, helper, input and complete-image identity. They are
not fresh installed executions. Both shared tools checks pass (0.109/0.098s).

- 24,576 guest phases cover all 256 commands, two upper-word patterns, four
  relation patterns, six full-word patterns, provider mutations and two SP
  phases. Another 224 cover seven inline/event/home aliases. Compare exact
  root accesses, calls/public state and modeled GPR/FPR/HI/LO/RAM/events
  across original, raw and guarded C, including volatile-state clobbers.
- Native32 O0/O2/O3 each pass 147,456 selected-body cases with trap UBSan,
  the actual C caller, backed aliases and full arena fences. Eight effective
  wrong-C controls return23 at every optimization: command, OR/AND, forward
  word/byte, reverse word/byte, word width and incorrect inline address.
  Use the established -fno-strict-aliasing harness flag for generic memory
  views; this does not change production flags or establish ISO object-layout
  portability. Batch selected and controls into three compiler invocations.
  The old stub is rejected by an actual missed state update.
- Six independent GNU links and 96 rebased phases qualify the call binding.
  Check 606 fired root-access fault prefixes, six stale-guard controls and
  five full-image corruptions. No portable C fault/MMU equivalence claim.
- Pin 39 historical inputs, including the owner's 12 GLOBAL_ASM sources,
  plus the predecessor padded object. Preserve all 56 neighbors and raw/padded
  pools. Isolated diagnostics remain empty; owner diagnostics are unchanged.
  Actual Make uses five productive commands, including both normal O2/g3
  asm-processor passes. Skip cleanup only. The initial three-command adapter
  correctly rejected this owner; the corrected path is executed and verified.

## Production

Seal 15,830 live/cache files, including all 1,454 linker objects. Preserve all
1,542 old mirror dirty paths, statuses, hashes and HEAD; add only two task
files, leaving 1,544 dirty paths. Do not reset or commit that mirror.
Commit tools first: `e3608fc5a8fb86a3270bb5505d8981c293aaac12`. No push.
Routine Codex-only qualification uses zero Claude calls.

Normal Make rebuilds the owner, linked ELF and progress CSV in the verified
Linux copy (0.539s). Mark only the verified target-only guard append old to
avoid unrelated rebuilds. Revalidate live inputs before adopting four
generated outputs. The linker script and conversion CSV remain unchanged.
Retain the duplicate generated_12D630 recipe warning and six pre-existing
Warning712 pointer/integer diagnostics in neighboring legacy wrappers.
This is not a warning-free build; no new diagnostics are introduced.

The independent full-ELF prediction is reproduced with zero exclusions:
**117 changed bytes =116 code bytes +1 target-size metadata byte**.
All other 6,054 bodies, all 6,055 addresses and all 720 protected Game-data
owners /189,088 bytes remain fixed. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`e01971fcd5a34ce1aa2e9cb914941e93b2798bb1824118e6f6140b1b161a48cc`.
Installed padded owner:
`fbe2076fee07c1b9b787a541916838ba13ab129a7d53046299d2942cd953d87a`.

## Handoff

The standard live-ELF matcher reports total **3,733/5,505 (67.81%)** and
Game **3,060/4,832 (63.33%)**. Init492/492 and Debugger181/181 remain exact.
Zero address drift; 1,772 different. The 75% threshold remains 4,129 exact:
**396 more matches are needed**. Queue shapes: 1,641 placeholders, 122
semantic/other and nine unlocated entries. Next `func_150049A4` is screened
only, not edited or credited. Keep `func_1508CAD8`'s 862-word stub queued.

Root README changes only aggregate rows. Detailed progress stays here and in
concise indexes. Post-commit graph-worker and every-old-node retention audits
remain private receipts; retain the excluded-corpus/large-HTML caveats without
claiming full re-extraction. Frozen host Release remains untouched.
