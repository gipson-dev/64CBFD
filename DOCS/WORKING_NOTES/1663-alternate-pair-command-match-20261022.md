# Alternate Descriptor Pair Callback Guarded C Match

Date: 2026-10-22

## Result

Recover `func_151A8A78` in `conker/src/game/generated_1D4E00.c` from its
zero-return placeholder. Complete C emits **42 words, a 24-byte frame and
one call binding**. One checked commutative branch-operand guard makes the
linked body byte-exact. This is guarded C, not compiler-only matching.
No inserted instructions, dummy locals or compiler-profile changes.

VA151A8A78..151A8B20 / ROM1D5F28..1D5FD0, ends exclusive.
Preserve `conker/asm/1D4E00.s` and the callback-table data.
Raw unlinked C body SHA-256:
`24342373f56b08818933e9e52d1c1dab3e688ff65b9ff9831f9d355fc673dae1`.
The old body was 12 bytes in a 168-byte slot. Restoring it adds one exact
match without changing the converted-C count or denominator.

Keep the address-based public name, descriptive parameters/locals and purpose
comment. Recover `void func_151A8A78(u8 *, s32, u8)`, retaining the actual
event-address word interface and a local byte-pointer view. Include
`structs.h` and declare `void func_1516972C(struct102 *);` canonically.
No shared header, neighboring call site or helper implementation changes.

## Recovered Contract

Capture the state pointer at owner+0x60 unconditionally. For command zero,
read the event word before the state word. On equality, skip both byte reads
and call the release helper. Otherwise read event byte+4 before state byte+4
and call the helper if those bytes match. Preserve OR short-circuiting and
full-word comparisons. This event-first byte order differs from the already
banked slot-1 handler; reversing it changes two additional instructions.

For command0x2D, capture event word+0 before the current state word. If they
match, copy event word+4 to state+0, then read event byte+9 and store state+4.
Otherwise, if event word+4 matches the captured state word, copy the captured
first event word and then read/store event byte+8. The first path wins when
both keys match. Preserve late byte reads and cached pointers/values under
overlapping records. Other command bytes do not dereference event/state,
although the owner+0x60 pointer load remains unconditional.

The full incoming command word is stored at original SP+8 before the byte
mask. Guest home/alias probes qualify emitted ABI behavior, not portable C
parameter-storage guarantees. The real dispatcher passes a masked byte.
The shared signed local starts as the command and later holds a full key.
Historical source spelling is not uniquely established.

## Guard And Binding

| Offset | Expected | Replacement | Meaning |
| --- | --- | --- | --- |
| 0x084 | 0x546A0005 | 0x55430005 | Swap v1/rs3 and t2/rt10 in bnel |

Keep opcode21, displacement5, target151A8B14 and the delay instruction.
Equality/inequality of full registers is commutative. Derive the replacement
from those register fields; pin the entire raw body and bindings, reject
changed inputs, and append exactly one row with the old CSV prefix intact.
The binding is `R_MIPS_26 func_1516972C` at body offset0x40.

All 42 static words match; 41 are dynamically visited. The duplicate load
at151A8AF8 is statically unreachable and reproduced, not runtime-exercised.

## Caller And Helper

The prepared aligned retail input has one literal target pointer at ROM23442C:
slot2 of `D_8008F964` at8008F96C. The table is
`[NULL, func_150F07E4, func_151A8A78]`; there is no aligned direct target JAL.
These are static-reference observations, not exhaustive runtime-target proof.
The graph supplies three relevant nodes/54 edges; actual source, table bytes
and instructions establish the calls, not graph edges alone.

Original/current `func_151A8A20` is 22 words, frame24. It reads owner byte
+0x5C, clamps indices >=3 to zero, skips NULL and forwards the owner, full
event-address word and byte command. Execute every word over 160 phases
using slots0/1/2/3/255 and poisoned command upper bits. Native checks compile
the actual C dispatcher. Slot1 is already banked separately, but this suite
uses a bounded spy for that other callback rather than re-executing its body.

Connect all 28 original/current `func_1516972C` words across 32 phases.
Exercise type0/1/2/255, pre-helper type mutation and reload, stride52 callback
lookup, callback and fallback paths. Keep `func_151696DC`, `func_15169804`
and the indirect release callback as bounded providers. No complete allocator
or free-chain behavior, hardware or natural-gameplay acceptance is claimed.

## Qualification

Tools: `experiments/game_alternate_pair_command.py` and
`tests/test_game_alternate_pair_command.py`, identical in both copies.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests,100.904s | 8 tests,115.788s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests,1.786s | 2 tests,1.795s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks per copy only under strict
source, raw/padded object, helper, input and complete-image identity.
They are not fresh installed executions. Both shared tools checks pass.

- 12,288 guest phases cover all 256 commands, four relation patterns, six
  full-word patterns, provider mutations and two SP phases. Another 224
  phases cover seven record/event/home aliases. Compare exact root accesses,
  calls/public state and modeled GPR/FPR/HI/LO/RAM/events across original,
  raw and guarded C, including volatile-register/FPR/HI/LO clobbers.
- Native32 O0/O2/O3 each pass 147,456 selected-body cases with trap UBSan,
  actual C dispatch, backed aliases and full arena fences. Eight defined
  wrong-C controls return23 at every optimization: command, OR/AND, forward
  word/byte, reverse word/byte, word width and alternate state pointer.
  Batch selected and renamed control functions into one translation unit per
  optimization: three native compiler invocations. The old stub is rejected
  by an actual missed state update. Native helpers are bounded effect spies.
- Six independent GNU links and 96 rebased phases qualify the call binding.
  Check 632 fired root-access fault prefixes, six stale-guard controls and
  five complete-image corruptions. No portable C fault/MMU equivalence claim.
- Pin 26 historical inputs plus the predecessor padded object. Preserve all
  22 owner neighbors, raw/padded pools and empty compiler diagnostics. All
  three productive shadow Make commands use normal O2/g3; skip cleanup only.

## Production

Seal 15,822 live/cache files, including all 1,454 linker objects. Preserve
all 1,538 pre-existing older-mirror dirty paths, statuses, hashes and HEAD;
add only two task files, leaving 1,540 dirty paths. Do not reset or commit
that independently dirty mirror. Commit tools first:
`14c2fc9e58328fa3bc597a889f90e98498151b91`. No push.

Normal Make rebuilds the owner, linked ELF and progress CSV in the verified
Linux copy. Mark only the qualified guard append old to avoid unrelated
rebuilds. Revalidate live inputs before adopting four generated outputs.
The linker script and conversion CSV remain unchanged.

The full independent ELF prediction is reproduced with zero exclusions:
**113 changed bytes =112 code bytes +1 target-size metadata byte**.
All other 6,054 bodies, all 6,055 addresses and all 720 protected Game-data
owners /189,088 bytes remain fixed. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`e45b10df237320b5ad91d5cc28b891a8cc9b8251a8a5418e809e4beda1d83bc8`.
Installed padded owner:
`2d0bec8e49d570b8c2f77995500f778de732ab622657d99052b8798c39992f3e`.

## Handoff

The standard live-ELF matcher reports total **3,731/5,505 (67.77%)** and
Game **3,058/4,832 (63.29%)**. Init492/492 and Debugger181/181 remain exact.
Zero address drift; 1,774 different. The 75% threshold remains 4,129 exact:
**398 more matches are needed**. Queue shapes: 1,643 placeholders, 122
semantic/other and nine unlocated entries. Next `func_1519E3BC` is screened
only, not edited or credited. Keep `func_1508CAD8`'s 862-word stub queued.

Root README changes only aggregate rows. Keep detailed progress here and in
concise indexes. Post-commit graph-worker and every-old-node retention audits
remain private receipts; retain existing excluded-corpus/large-HTML caveats
without claiming full re-extraction. Frozen host Release remains untouched.
