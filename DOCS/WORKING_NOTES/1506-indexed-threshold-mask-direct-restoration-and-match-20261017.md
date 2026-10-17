# Indexed Threshold Mask Direct Restoration And Match

Verified 2026-10-17. Consumer predecessor5f6bd71e; tools predecessor8a5bfb6.
Both active trees began clean. The preceding turn was progress: it established
actual opening-register reuse in the still-unmatched actor-record gate.
This turn restores an independent routine in the same owner directly from C.
Keep the139-word gate and both fade lifetime gaps open.

## Restored Function

func_150F33F8 in generated_11FF10, original asm/11FF10.s,
VA150F33F8..150F34A0 /ROM1208A8..120950,42 words/168 bytes, frame0.
It replaces the zero-return placeholder with the complete void routine:

- Select the0x9A0-byte record using the incoming signed32 index and the
  reloaded D_800DBFF0 base. Preserve the original32-bit integer address form;
  ordinary pointer addition exchanges the opening temporaries instead.
- Compare the record's float at0x300 against D_800A1970. A false or unordered
  comparison returns without reading the second float or mask pointer.
- If the float at0x2FC exceeds840.0f, set the selected bit; otherwise clear it.
  D_800D9A40 points to a **signed halfword**, not a word-sized mask.
- Retain the original function symbol and a concise purpose comment without
  assigning an unproven subsystem identity. The actual1510FD04 call passes S0
  in A0 and ignores a C return value; this is a checked caller window, not
  qualification of the complete unrecovered caller.

All42 words emit directly with the existing O2/g3 profile, eight relocations
and **no new word guards**. Raw SHA-256:
`f190d637af70139d106d0522a200f0a061c7c1aacd2e724ea3230c607e3e6204`.
Both raw and padded links match all42 retail words. All11 neighboring raw/
padded routines and normalized owner pools remain unchanged. The alternate
draft's word-sized float accesses and mask store were not imported blindly.

## Qualification

Seven final installed tests pass in16.055s; the pre-install suite passed in14.069s.

- 1,200 core cases cover threshold equality, unordered values, signed mask
  endpoints, low/high shift bits and two stack phases;216 sparse word-wrap/
  shift cases and160 alias cases preserve complete public effects.
- 480 selected access-fault prefixes compare retail/raw/padded complete modeled
  memory, registers, float registers, condition, LO, access order and PC state.
  An effective lazy-gate fixture omits the second float and mask-pointer bytes.
- Three independent symbol-rebase links pass36 cases. All three globals have
  independently varied high and low halves, including signed HI16 carry
  boundaries, with each HI/LO relationship preserved.
- Native32 O2/O0 each pass2,000 typed-record/caller cases with UBSan and mask
  canaries; six effective threshold/bit/gate controls fail as expected.
- The existing oracle needed a local NOR extension for the retail clear path;
  16 independently seeded operand pairs check it. No shared interpreter was
  changed. Hardware FP exception fidelity and portable C behavior for sparse,
  overflowing or out-of-range shift inputs are not claimed by the model.

## Complete First Image

The initial code-only metadata proposal was rejected and archived before a
successful first prediction existed. The private link revealed precisely one
three-symbol serialization cycle: D_800A1E50/D_80097BF0/D_800A1278 reorder as
(2,0,1). The final predictor checks their exact names, definitions, attributes
and permutation, not a blanket symbol/string-table exclusion.

The accepted first prediction accounts for **149** changed ELF bytes:
**124 code +one target-extent +24 metadata**, zero exclusions. The first normal
production build equals that complete prediction byte-for-byte:
`7bdbd79a0d8f8fa6c9da685c6aca39881442eb09e5725b7d52a9fb84659c8b94`.

All6,057 function bodies and addresses were compared: only func_150F33F8's
body/declared extent changes; all addresses remain fixed. All189,088 Game-data
bytes /720 owners remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The guard manifest, compiler profile, conversion CSV and other protected
inputs are unchanged.257 entries /237 paths are protected by the new freeze.

Six named before/after successor paths preserve the earlier actor-state and
record-gate historical views. Their exact predecessor/successor hashes and
immutable fixtures are checked;12 effective checkpoint-corruption controls
reject altered fixtures. Two affected historical checks pass freshly in
51.377s. These adapters reverse only this accepted successor; they neither
rewrite old first predictions nor claim that the current full image is the
older one. Unchanged broader-suite receipts are reused, not called fresh.

## Gate Research Retained

func_150F2A60 is not restored. Additional scratch screens reject:

| Screen | Words | Outcome |
| --- | ---: | --- |
| Direct normal O2/g3 | 137 | Reproduces wrapped code/functions/relocations/pools |
| Direct O1/g3 | 127 | Frame0x38, wrong private layout |
| Direct O2/g1 or g2 | 132 | Compiler warns optimization is disabled; wrong frame |
| no_const_in_reg | 121 | Five actor address loads but destroys required register roles |
| do_opt_saved_regs | 139 | Frame0x50 and129 unequal words; not a match |
| s16/u16/s8/u8 counter | 137 | Five saves and SLTI, but added truncations; actor base still cached |
| register s32 counter | 137 | Identical original raw hash |

The wrapper's earlier profile rejection was not itself compiler evidence;
direct calls used relative input/output paths and first reproduced the normal
object. These are rejected diagnostic screens, not new production options or
portable/private qualifications. Do not revisit them merely for equal counts.
The independent42-word restoration advances the wider Game queue while the
gate's original type/profile and address-rematerialization constraints remain
open in Notes1502..1505.

## Bank And Resume

Tools **6a6aca2** banks four new qualification/checkpoint files and four narrow
historical adapters. Test-only **9a968aa** strengthens the signed HI16 carry
rebases and is the final consumer tools pin. Both tools copies pass12
shared tests and smoke checks;16 ASCII/AST parses and eight task pairs pass.
The four mirror predecessor hashes were verified before copying. Preserve
1,120 unrelated mirror hashes,1,128 dirty paths and mirror HEADddbdd16b.
No mirror commit/reset, push, new Claude call, host or frozen Release action.
Finish the owned post-commit Graphify worker before closing.

Fresh matching totals: Game **2,963/4,828 (61.37%)**, total
**3,636/5,501 (66.10%)**,1,865 different and zero drift. Nominal conversion
counts are unchanged because the predecessor was already represented as C.
Root README changes only these aggregate matching rows.

- [x] Restore and directly match all42 threshold-mask words without guards.
- [x] Pass private/public/fault/rebase/native controls and the whole first image.
- [x] Preserve historical checkpoints, copied neighbors, data, guards and mirror.
- [ ] Continue func_150F3214's90-word/frame0x28 routine in this same owner.
- [ ] Keep func_150F2A60's139-word matching gap, both fade lifetime gaps and the
  wider Game goal open; no host gameplay/FP hardware claim follows from this.

```sh
python3 -m tools.experiments.game_indexed_threshold_mask
python3 -m unittest tools.tests.test_game_indexed_threshold_mask -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```
