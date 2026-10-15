# Record Color Fade Semantics And Compiler Gap

Date: 2026-10-15. Predecessor consumer **d9a5aa61**, tools **2be3d9f**,
both active trees clean. The previous goal turn was verified progress:
func_1516FA88 was restored and committed. Continue the complete additional-
source audit and Game matching objective; do not substitute this candidate
qualification for completion of either the function or the broader goal.

## Steps

1. [x] Preserve current production inputs, archive and independently dirty older tools mirror.
2. [x] Recover complete retail fade/size/interpolation semantics and correct the archival width/sign errors in an isolated C candidate.
3. [x] Measure compiler shapes and retain explicit instruction/private-state gaps instead of forcing an install.
4. [x] Qualify independent public semantics, all byte shift/phase values, bounded aliases, effective controls, native defined behavior and independent rebases.
5. [x] Verify staged callback integration with current dispatcher/cleanup and original table, without claiming the actual stub executes the recovered behavior.
6. [x] Reject through the strict match gate and real padder; preserve all 57 production states and matching credit, bank tools first and update working docs only.
7. [ ] Resolve the exact-match/compiler gap and qualify the complete installed image before adopting C; retain the full additional-source/Game queues.

## Target And Recovered Semantics

**func_1516FBCC**, VA **0x1516FBCC**, ROM **0x19D07C**, **97 words /
388 bytes**, leaf with no stack frame. Original [19A8B0.s](../../conker/asm/19A8B0.s)
starts at line 2747. Production [generated_19A8B0.c](../../conker/src/game/generated_19A8B0.c)
still contains its **three-word zero-return placeholder**. The original
**D_8008CBA0 slot 4** points at this entry. No source/guard/profile/ELF change
is adopted in this checkpoint.

The archival `game_19A8B0.c:933` is useful semantic material, not a byte-exact
donor. Its premature u8 fade temporary, widened byte accesses, halfword size-
step loads and signed target-color casts are wrong for retail. Recover:

- Keep the fade/clamp/completion value signed **32-bit** until the byte store. A full-word value of 256 can store byte zero yet must not take the zero-completion exit.
- If byte 0x24 is nonzero, grow by the wrapping global step times 16 and cap only signed values at/above 256. Otherwise subtract global step shifted by **byte 0x2F modulo 32** and clamp signed negatives to zero.
- Advance width/height halfwords 0x14/0x16 by signed **byte** steps 0x2D/0x2E times the repeatedly read global step. Preserve narrowing at the stores and the width reload.
- Keep retail's **duplicated width-only test**, not a guessed width-or-height test. If width is nonpositive, clear both halfwords and return 1. A negative height alone does not cause completion.
- Add the current global step to phase byte 0x2C using 32-bit wrapping arithmetic; cap signed values at/above 128 to 127. Interpolate the three colors from **unsigned** bytes 0x26..0x28 toward **unsigned** bytes 0x29..0x2B, using the wrapped doubled phase and arithmetic division/shift by 256. Store only the output bytes at 0x1C..0x1E and return 0.

The compiler retains two width branches. They test the same unchanged
register; therefore **0x1516FCC0 is unreachable** in ordinary execution.
The original execution tests cover all **96 reachable words**, not an
invented 97-word coverage claim. Keep the dead retail instruction for a
future complete byte match.

## Compiler Gap And Installation Rejection

| Form | Words | Length-Inclusive Word Differences | Selected |
| --- | ---: | ---: | --- |
| Defined masked C | **98** | **89** | Candidate only |
| Unmasked shape diagnostic | **97** | **65** | No |

The selected body preserves defined wrapping math and masks the byte shift
count. IDO emits an extra **ANDI at function+0x60** before SLLV, even though
the MIPS instruction already ignores high shift-count bits. The selected C
also has different V0/V1 lifetimes, size-step temporaries, and an independent
color-load/multiply/LO schedule. These are real private/instruction
differences, not address drift.

Removing the C mask is only a diagnostic: counts 32..255 would leave the C
shift undefined and the remaining 65 differences are not solved anyway.
`archival_shape()` likewise explicitly retains archival overflow/shift UB
and is **shape-only**, not selected semantic C. Do not replace the function
with raw retail words or silently remove the defined mask for a shorter row.

The actual production padder rejects the candidate with:

```text
patched func_1516FBCC is 0x188 bytes but its retail span is only 0x184
```

The direct-match qualification gate rejects it as well. No guard CSV rows,
compiler profile edits, local padding, incompatible prototypes or production
assembly replacement are added.

## Fresh Qualification

All **10 checks pass in 26.686 seconds**, exit 0, on the final pre-bank code.

- **3,586 original/C public-state pairs** agree with independent arithmetic. Cover every fade byte, every phase byte, every byte shift count, signed byte steps, overflow/clamp boundaries, full-word-256/stored-zero completion and negative-height-only behavior. All 96 reachable retail words execute.
- All **3,586 full private states differ**. Compare **27 fired fault-prefix pairs**; **26 differ**. These are deliberate private-parity rejection evidence, not passing fault-equivalence tests.
- **20 bounded physical global-step alias pairs** agree publicly. Keep this guest-memory evidence separate from a portable C object-layout or hardware claim.
- All **eight freshly compiled guest negatives** are effective: fade truncation, widened fade load/store, unsigned width/height steps, invented height completion, signed interpolation target and byte-only completion.
- **Native32 O2 and O0, 131,074 cases each**, pass the independent full-record reference with undefined-behavior trap instrumentation enabled. All eight semantic negatives compile and fail with controlled exit 10 or 11; no crash is accepted as a semantic counterexample.
- **Three separately assembled original/C rebases**, including signed-low-half carry addresses, preserve public semantics. They do not prove byte or private equality.
- All **29 owner neighbors** retain bytes, extents, relative relocations and normalized pools. Both the strict gate and the actual oversized-slot padder rejection are tested.
- All **801 original archive fingerprints** are freshly checked, and all **57 production input hashes** remain unchanged. The prior whole-source 1,717-object audit remains historical, not a new recompilation or donor-import claim here.

## Staged Dispatcher Integration

Freshly compare current dispatcher **48 words**, cleanup **28 words**, the
original nine-pointer callback table and slot 4 with retail. Verify the
actual current callback is still the three-word placeholder.

Insert the candidate or original callback **only into the guest oracle**.
Across **128 paired cases**, including **60 cleanup paths**, both staged
callbacks agree with an independent public record/call reference through
the current dispatcher and cleanup bodies. Cover null/non-null bindings,
two stack phases, counter expiration, Y advancement and clear-before-unlink
ordering. This checkpoint uses release type **0**; it does not newly qualify
the type-1/type-2/default-destructor branches. The lower unlink helper
remains opaque. Do not call this actual installed callback execution,
full caller restoration or natural gameplay parity.

## Banking And Continuation

Tools **64fcc0d** is banked before consumer docs/pin:

- `tools/experiments/game_record_color_fade.py`
- `tools/tests/test_game_record_color_fade.py`

Preserve older mirror **ddbdd16**, all **695 initial dirty fingerprints**,
and add only two absent hash-equal owned copies, for **697 final paths**.
Windows syntax and standalone candidate checks pass in both copies; shared
`make tools-check` passes. Do not commit/reset that mirror. Root README,
source, ELF, guards, profiles and progress rows stay untouched. Matching
remains **Game 2,903/4,828 (60.13%)**, **total 3,576/5,501 (65.01%)**,
different **1,925**, zero address drift. No new C conversion/match credit.
No push, dependency/account change or host/Release operation.

Reproduce in the prepared consumer WSL checkout:

```sh
python3 -m tools.experiments.game_record_color_fade --measure
python3 -m unittest tools.tests.test_game_record_color_fade -v
make tools-check
```

Without `--measure`, direct qualification must continue to reject this
candidate until the actual match criteria are met.

Next, retain the defined shift semantics while resolving the extra mask
instruction, then recover the temporary lifetimes and color-load/LO schedule
from the recorded raw object/disassembly. Any bounded MIPS normalization
must prove the mask redundancy, complete dependency/lifetime closure,
branch offsets, relocation movement, private/fault behavior and original
rebases; do not replay a broad retail word array. Before adoption, require
the correct 97-word extent, real padder pass and complete predicted-image
closure. The production callback remains open until those gates pass.

Keep the full
[additional-source repair/binding/unanchored queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md),
remaining callbacks/callers and inherited-stack renderer deferral open.
This semantic candidate is progress toward the original objective, not its
completion and not a completed FBCC conversion.

## Post-Bank Verification

Consumer **d65ea282** banks the candidate handoff, working indexes and tools
**64fcc0d** pin. All **ten post-bank checks pass in 32.988 seconds**, exit 0.
The selected candidate remains 98 words / 89 length-inclusive differences;
both exact-match and actual oversized-slot gates still reject it. All 57
production hashes, original archive hashes, public/native/rebase/staged-chain
evidence and explicit private/fault differences remain qualified. No source,
ELF, guard, profile, conversion row, root README or matching-credit change.

Both active trees are clean before this receipt edit. All **697 final older-
mirror fingerprints** remain fixed, preserving the **695 initial dirty
paths** and two owned copies; HEAD remains ddbdd16. Seven scoped docs resolve
**5,043 relative inline links, zero broken**. The source-commit graph update
completes at **41,291 nodes / 81,399 edges / 3,834 communities**, retaining
excluded-but-present inputs rather than forcing a smaller scan. Continue
FBCC's compiler gap and the full additional-source/Game objective.

## Exact-Match Resolution

[Note 1411](1411-record-color-fade-proven-normalization-and-match-20261015.md)
resolves the installation gap without removing the C mask or replaying a
retail word array. Eighty-four bounded guards apply a proven mask omission,
branch-span repair and closed temporary/color/LO normalization; all 97 padded
words, literal private/fault behavior, original rebases and the complete ELF
are exact. The callback is now installed and its actual slot-4 chain passes.
The candidate measurements and rejection above remain historical; continue
func_1516FD50 and the complete additional-source/Game queues.
