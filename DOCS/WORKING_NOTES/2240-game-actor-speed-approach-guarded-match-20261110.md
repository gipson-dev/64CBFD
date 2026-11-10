# Game actor speed approach guarded match - 2026-11-10

`func_1505A3A8` replaces its zero-return C placeholder with the complete actor
speed approach routine. All **137 words / 548 bytes** match the original slot,
VA **1505A3A8..1505A5CC**, ROM **87858..87A7C**, with the original **0x10 frame**
and saved F20 pair at SP+8. Two checked guards exchange independent initial
rate multiplies. No insertion, omission, frame change, compiler-profile change
or Makefile change.

Production recount: **4,310 / 5,513 (78.18%)** total; Game **3,637 / 4,840
(75.14%)**; Init 492/492 and Debugger 181/181. Zero address drift, 1,203 still
different. **101 more matches** reach 4,411/5,513 and the active 80% goal.
Conversion CSV and converted-function counts remain unchanged.

## Source and ABI

Owner `conker/src/game_83300.c`; object `conker/build/src/game_83300.c.o`.
Original assembly `asm/nonmatchings/game_83300/func_1505A3A8.s` is retained.
The recovered interface is:

```c
void func_1505A3A8(f32 target_speed, void *actor_pointer,
                 f32 acceleration, f32 deceleration, u8 magnitude);
```

The mixed O32 arguments are F12 target speed, A1 actor, A2 acceleration bits,
A3 deceleration bits, and the fifth unsigned byte at entry SP+0x13. The actor
uses canonical `struct127` fields; only `xz_velocity` at actor+0x3C is written.
The current float-return declarations were placeholder artifacts. Both current
C call sites discard the result. Update the local forward declaration in the
owner and the declaration in `conker/src/game/generated_11FF10.c` to `void`.
All 12 functions, pools and register usage in that second owner remain equal;
its complete padded object is byte-identical before/after and in production.

The original seven callers do not read incoming F0 before a new definition,
a subsequent call, or the already recovered void water/stun parent returns.
That last path can retain incidental F0 bits. Guest checks compare those bits
to the original old speed without claiming they are a semantic C return value.
The two complete C parents, `func_150585F0` (680 bytes) and `func_150F34F4`
(3,836 bytes), remain byte-exact. Other placeholder parents remain uncredited.

## Actor motion behavior

Scale both rates by `D_800D1550[0]`. When D_800CC27C is nonzero, field 0x28 is
below 5.0f, and state is not 30, disable acceleration. State 1 adds modifiers:
water multiplies deceleration by D_800994C0 and sets acceleration to 2.0f;
field 0xA8 multiplies deceleration by 0.25f. Field 0x81 selects its 0x40/0x20
behavior: both bits force zero deceleration; 0x40 alone loads D_800994C4;
otherwise multiply by D_800994C8 and independently halve acceleration at
magnitude 46 and target speed at magnitude 91. Field 0xAE applies D_800994CC.

For a negative target and positive current speed, combine deceleration and
acceleration; for a negative target and nonpositive speed, use acceleration
as deceleration. For a nonnegative target and negative speed, combine the
rates into acceleration. Subtract deceleration when above target and clamp
against overshoot. Otherwise, apply D_800994D0 to acceleration when current
speed is greater than target minus one, then add and clamp. Retain ordered
float comparisons, single-precision rounding and direct actor field rereads.

The five retained constant words are 0x3ECCCCCD, 0x3FA66666, 0x3EB33333,
0x3E4CCCCD and 0x3C23D70A. Their existing data owners are preserved; external
loads keep the original relocation identities instead of creating new pools.

## Matching and complete image accounting

Raw semantic C emits exactly 137 words. Scale deceleration before acceleration
in source to recover F14/F20 allocation. Raw SHA256:
`9632a761e20e0b865998fdbaa2d43a218668b49a9a5470cf3bc7c9f4d066876f`.
All 14 binding sites match original assembly. Swap only word 8 / offset 0x20
(`46007382` to `4600A502`) and word 10 / offset 0x28 (the reverse).
Both operations read the same timestep and write separate float registers;
the intervening integer LUI is independent. No branch or binding movement.
Both target padders and full owner padding reproduce all retail words.

Strict literal whole-ELF prediction accounts for **455 changed bytes**:
the target code, its declared symbol size growing from 32 to 548 bytes, and
three closed GNU symbol/string record permutations. The exact groups are
`D_80038080` / `D_8009D670`, `func_151BC580` / `D_8009D6A0`, and
`D_800994CC` / `D_800997E4` / `D_8009EECC`. Rebuild these records and their
contiguous strings from the old image; check every named definition, allowing
only the target size change; then require the complete expected byte sequence.
No excluded sections or ranges. Header/section geometry stays fixed.

All 6,050 function addresses remain fixed. Only the target's canonical body
changes. All **88 non-target owner functions**, empty pools and register usage
are preserved. The **8 inherited compiler diagnostics** remain, with none added.
The actual five-command ordinary O2/g3 Make pipeline equals the independent
owner and image prediction. Production rebuilds the target and declaration
owner; the latter's object stays identical. All **189,088 protected bytes /
720 data owners** stay exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Prior guards and conversion CSV stay fixed. The existing duplicate
`generated_12D630` recipe warnings and expected full-ROM checksum exit 2 remain.

## Qualification and limits

- Guest: **2,878 cases per body / 8,634 executions**, 12 independent rebases,
  and **2,878 raw/retail access-trace pairs**. Coverage is 135/137 words;
  two original duplicate instructions are unreachable. Exhaust all 256 values of
  magnitude and each of the five byte flags. Exercise state 30, the 5.0f
  threshold, reversals, target clamps, near-target boundaries, signed zeros,
  subnormals, extremes, infinities and quiet NaNs. Output NaNs compare by class;
  retained actor/global bytes compare exactly. Check the complete actor/globals,
  saved F20, stack/caller homes and incidental F0. Physical global/output aliases
  are guest-only extensions, separate from typed native objects.
- Native SDK32: **2,862 cases at O0/O2/O3**, UBSan, and **24 effective controls**
  per profile. An initially ineffective timestep control exposed a corpus gap:
  water overrides acceleration. Add independent dry timestep cases before
  accepting the control. All 24 now produce observable witnesses.
- Compiler/padder controls: 24 effective IDO mutations, all **151 raw-word and
  binding corruptions**, both stale guards, seven complete-image corruptions,
  and four independent GNU links / 12 executions. Malformed-image parser
  rejections count only as image rejection, never semantic witnesses.
- Callers: seven original JAL sites, no J or aligned pointer entries; **168
  original-window executions across 33 words** verify actual mixed arguments,
  stack loads/stores and delay slots. Original F0 liveness paths are recorded.
  A further **24 complete 170-word water/stun parent executions** connect the
  actual motion child, using independent motion/parent models. Remaining
  providers are bounded fixtures, not recovered provider algorithms.

Six focused tests pass before and after installation in each tools environment.
Shared smokes are fresh; three unchanged regressions per copy are explicitly
reused with matching helper/test fingerprints. The 762 frozen inputs include
the historical water-oracle ELF constant fixture used by the parent model.
Sibling tests use a read-only overlay and preserve its 2,434 pre-existing dirty
paths. Routine work uses zero Claude calls.

The scoped Graphify refresh requests both C owners and six new modules.
The initial code pass retains all 59,639 existing nodes and updates to 113,065
links; actual positions for 71 owner C functions and 12 caller C functions,
plus 18 retained ASM functions, are audited. The six new Python modules have
zero indexed nodes under the current scan filters; that coverage gap is
recorded rather than treated as completed extraction. The scan also retains
31,816 historical nodes from 3,754 files under its fail-closed policy. This is
a scoped code refresh. Gameplay and FCSR/hardware acceptance remain separate.
Evidence: `conker/build/game-motion-approach-1505A3A8-match/`.

Keep the 80% goal active and commit tools before the consumer pin. Next is the
actor audio-handle router `func_15060778`, in the same owner. Its current
171-word / 0x50-frame body remains different from the 174-word / 0x58-frame
retail routine. Recheck complete assembly, helpers, callers and existing notes
before fitting it. Private candidates receive no credit.
