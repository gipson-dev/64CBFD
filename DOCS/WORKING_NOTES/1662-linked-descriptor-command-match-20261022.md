# Linked Descriptor Command Callback Guarded C Match

Date: 2026-10-22

## Result

Recover `func_151A4CE0` in `conker/src/game/generated_1D0840.c` from
its zero-return placeholder. Complete semantic C emits **42 words/frame24
with one call binding**. One checked guard swaps only a commutative bnel's
two register operands. The padded/linked routine matches all42 retail words.
This is guarded C, not compiler-only matching. No inserted instructions,
dummy locals, compiler-profile change or handwritten function emitter.

VA151A4CE0..151A4D88 / ROM1D2190..1D2238, ends exclusive.
Preserve `conker/asm/1D0840.s` and the callback table. Raw unlinked body:
`71b594efac93aab9e59600f70f308163b8d25a7f65182506d5ab52112b7c7b99`.
The predecessor was three words/12 bytes in a168-byte slot. Restoring
semantics gains one exact match without changing converted-C denominators.

Keep the address-based public name, descriptive locals and purpose comment.
Use `void func_151A4CE0(u8 *owner, s32 eventAddress, u8 command)`.
The real dispatcher passes a32-bit event-address word; retain that interface
and cast to a local byte-pointer view. Add `void func_151A4E9C(u8 *);`.
No shared header, neighboring call-site or helper implementation changes.

## Recovered Contract

Unconditionally capture the linked-record pointer at owner+0x98 before
testing the command. Command zero reads the linked record's full word first,
then event word+0. If they match, skip both byte reads and transfer flags
through `func_151A4E9C(owner)`. Otherwise compare linked byte+4 with event
byte+4, in that order, and call the same helper on equality. This is an OR
gate, not an AND, and the word comparison must not be narrowed.

For command0x2D, capture event word+0 before reading the linked record's
current word. If they match, copy event word+4 to the linked record, then
read event byte+9 and store it at linked+4. Otherwise, if event word+4
matches the captured current word, copy the captured first event word and
then read/store event byte+8. Keep byte reads after word stores. When both
keys match, the first path wins. Preserve cached pointers/values under
overlapping records. Other command bytes do not dereference the linked
record or event, although the owner+0x98 pointer access is unconditional.

Preserve the full incoming command word at original SP+8 before masking
to a byte. Poisoned direct-entry homes and stack aliases are emitted guest
ABI tests, not portable C parameter-storage guarantees. The real dispatcher
also preserves its incoming home and passes a masked command to the target.

A shared signed local starts as the promoted command and later holds the
comparison key. A notification-path shared-value variant produces15 differences;
the selected inline release comparison leaves only one branch operand swap.
Reversing the source comparison or using the command directly does not remove
that final word difference. Historical C spelling is not uniquely established.

## Guard And Binding

| Offset | Expected | Replacement | Treatment |
| --- | --- | --- | --- |
| 0x084 | 0x546B0005 | 0x55630005 | Swap rs3/v1 and rt11/t3 in the same bnel |

Both words retain opcode21, displacement5, target151A4D7C and the same
delay instruction. Equality/inequality of full registers is commutative.
Derive the replacement from the register fields; pin the whole raw body
and binding, reject changed inputs, and append exactly one CSV row while
preserving every byte of the previous manifest prefix.

The binding is `R_MIPS_26 func_151A4E9C` at body offset0x40.
All42 static words match;41 are dynamically visited. The duplicate load
at151A4D60 is statically unreachable and reproduced, not runtime-exercised.

## Actual Caller And Helper

The prepared aligned retail input has one literal target pointer, ROM22EE70:
slot8 of the20-entry `D_8008A390` table at8008A3B0. There is no aligned
direct target JAL. Treat this as static-reference evidence, not exhaustive
proof about computed runtime targets. Graph context has three nodes/seven
edges; actual source, table bytes and instructions establish the calls.

Original/current `func_15147D1C` is18 words/frame24. It loads a signed
word index at owner+0x20, reads the callback without clamping, skips NULL
and forwards owner/event-address/byte-command. Execute every word across
160 phases with NULL slots0/1/19, target slot8, bounded other slot2 and
poisoned command upper bits. Native arrays use backed in-range indices;
do not invent an out-of-range clamp or claim portable C OOB behavior.
The other callback's implementation is not qualified.

Original/current `func_151A4E9C` is12 words at ROM1D234C..1D237C.
Connect all instructions across96 phases. Clear owner flag0x2 at halfword
+0x1E, zero owner byte+0x30, then read linked byte+0x30 and perform the
two ordered stores of old|1 and old|5. Preserve all other bits. This is
flag transfer, not deallocation or a lower release-provider chain.
The helper has no further calls and its complete current body is exact.

## Qualification

Tools: `experiments/game_linked_descriptor_command.py` and
`tests/test_game_linked_descriptor_command.py`, identical in both copies.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests,81.728s | 8 tests,106.595s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests,1.792s | 2 tests,1.795s | 0 / 0 / 0 |

Reuse the other six pre-install checks per copy explicitly and only under
strict source, raw/padded object, helper, input and complete-image identity.
They are not fresh installed executions. Both shared tools checks pass.

- 12,288 guest phases sweep all256 commands, four relation patterns, six
  full-word patterns, provider mutations and two SP phases;224 more phases
  exercise seven descriptor/event/home aliases. Compare exact root accesses,
  calls/public state and complete modeled GPR/FPR/HI/LO/RAM/events across
  original, raw and guarded C, including volatile clobbers.
- Native32 O0/O2/O3 each pass147,456 selected-body cases with trap UBSan,
  the real C dispatcher, full arena fences and backed aliases. Eight defined
  wrong-C controls each return the expected23 sentinel at every optimization:
  command, OR/AND, forward word/byte, reverse word/byte, word width and
  alternate state pointer. The old stub is rejected by an actual missed update.
  Native helper callbacks are spies; the actual flag helper is qualified above.
- Batch the selected body and eight renamed controls into one translation
  unit per optimization, using three native compiler invocations rather than
  a separate compile for each control. Each control must fail its own run;
  a shared runner verifies every expected sentinel, not just a final digest.
- Six independent GNU links /96 rebased phases cover the binding. Check632
  fired root-access fault prefixes, six stale-guard controls and five complete
  image corruption controls. No portable C fault/MMU/hardware equivalence claim.
- Pin27 historical inputs and the old padded object. Preserve22 owner
  neighbors, raw/padded pools, its GLOBAL_ASM member and empty diagnostics.
  All five productive shadow Make commands use normal O2/g3; skip cleanup only.

## Production And Handoff

Seal15,818 live/cache files, including all1,454 linker objects. Preserve all
1,536 pre-existing older-mirror dirty paths, statuses, hashes and HEAD;
add only the two task files, leaving1,538 dirty paths. Do not reset or commit
that independently dirty mirror. Tools `853c97594c3707565be94acce22b3f3bab352e55`
are committed first; no push.

Normal Make rebuilds the owner, ELF and progress CSV in the verified Linux
copy. Mark only the checked guard append old to avoid unrelated rebuilds.
After live-input revalidation, adopt four qualified generated outputs.
Linker script and conversion CSV remain unchanged.

Production reproduces the entire independent ELF prediction with zero
exclusions: **113 changed bytes =112 code bytes +1 target-size byte**.
All other6,054 bodies, all6,055 addresses and all720 protected Game-data
owners /189,088 bytes remain fixed. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`3056711542d3c6c9f57f7d848e21ce57f79fee6b2438757f7f1ee0e406fdc225`.
Installed padded owner:
`fbccadbdf0bd7e6a3f51eba4edabd2fb99729d0026b06c343317864429274626`.

The standard matcher against the live ELF measures total **3,730/5,505
(67.76%)**, Game **3,057/4,832 (63.27%)**, Init492/492 and Debugger181/181
exact, zero drift and1,775 different. The75% threshold remains4,129 exact:
**399 more matches are needed**. Queue shapes:1,644 placeholders,122
semantic/other and nine unlocated entries. Next `func_151A8A78` is screened
only, not edited or credited. Keep the862-word `func_1508CAD8` stub queued.

Keep detailed progress here and in concise indexes; root README changes only
the two aggregate rows. Post-commit graph-worker completion and every-old-node
retention audits remain private receipts. Retain the existing excluded-corpus
and large-HTML warnings; do not claim full corpus re-extraction. Preserve
frozen host Release. No natural gameplay, rendering or full-game acceptance.
