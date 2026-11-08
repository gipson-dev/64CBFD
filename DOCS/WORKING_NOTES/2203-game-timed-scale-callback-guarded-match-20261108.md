# Timed Scale Callback Guarded Match - 2026-11-08

`func_151B5E94` replaces its false zero-return placeholder with a complete
timed sound/scale callback that forwards its downstream status. Semantic C
emits **77 words with the original 0x48-byte frame**; **seven checked guards**
recover the **78-word / 312-byte retail body**, including one inert delay NOP.
This is a guarded C match, not an unguarded compiler match.

Production: Total **4,272 / 5,513 (77.49%)**, Game **3,599 / 4,840 (74.36%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. There are
**1,241** converted functions still different and **139** more exact functions
needed for 4,411 / 5,513 and the active 80% goal. Conversion rows are unchanged.

## Recovered behavior and observed result contract

Owner `conker/src/game/generated_1E30A0.c`, original `asm/1E30A0.s`.
VA **151B5E94..151B5FCC**, ROM **1E3344..1E347C**. Interface:

```c
s32 func_151B5E94(u8 *owner);
```

1. Increase the float phase at +0x170 by `D_800AA434 * D_800BE9A4`, rounding
   the separate multiply and add to single precision. Store and reload it.
2. If the phase is strictly greater than `D_800AA438`, store positive zero and
   call the existing sound adapter with O32 arguments
   `(0x502, 24000, 0, 0, -1, trunc(x), trunc(y), trunc(z), 100, 500)`.
   Coordinates are the three floats at +0x38/+0x3C/+0x40. The established SDK
   prototype consumes signed halfwords for the final coordinate/range values;
   the literal adapter verifies their sign-extension and argument homes.
3. Read the live phase again after sound. If it is strictly less than
   `D_800AA43C`, call `sinf(phase)`, reload the saved state pointer, live base
   at +0x174 and gain, and evaluate `base + sine * (gain * base)` with the
   original floating operation order. Otherwise use the live base directly.
4. Store the two scale fields at **+0x1C then +0x18**. Return the full status
   from `func_15133894(owner)` after restoring S0, RA and the frame.

Constant bits are `3F80418A`, `41EF3333`, `41490FDB`, `3D4CCCCD`, at
ROM24EEF4/24EEF8/24EEFC/24EF00 for D_800AA434/438/43C/440 respectively.
These are measured values, not newly approximated floating literals.

The sole aligned entry pointer is `D_800898B0[5]`, VA800898C4 /ROM22E384.
An aligned full-ROM entry/interior census finds no direct J/JAL references.
The actual consumer is the 13-word VA15132244..15132278 window of
`func_151321D0` in 15F680.s. It reads unsigned selector +0x71, skips zero,
calls with A0=owner and homes its gate at SP+0x23. It **tests V0** afterward:
zero sets the gate to one; a nonzero result preserves the restored gate.
A compiled constant-result implementation fails this observable contract.

Reuse the already-banked sine-scale recovery in Note 1808 / `func_151B6254`,
including its original caller and helper models. This target has its own
sound trigger, phase reset and bounded pulse interval; the related loop's
different period and constants are not copied into this function.

## Exact emission and independent image prediction

The selected ordinary C expression order reproduces the retail floating
arithmetic directly. Natural output is 77 words with 13 relocation bindings.
No volatile, inline assembly or compiler profile change is introduced.
The retail O2/g3, MIPS2/O32 profile is retained without diagnostics.

Seven expected-word guards derive only:

- The false-path dead FP scratch role F0 to F2, across its definition/uses.
- Moving the +0x18 output store before the independent unconditional branch.
- An inert branch-delay NOP, and the corresponding false-edge displacement.

The branch/store join retains the same control-flow destination. The final
helper relocation moves from raw +0x118 to fitted +0x11C through insertion;
binding identities and all semantic operations are preserved. The original
redundant load at VA151B5FA4 is unreachable and remains literally present.
All **77 reachable words** are visited; all **78 literal words** match.
Raw private FP scratch/fault PCs are not equated with retail; fitted/retail
complete state is checked. No semantic operation is inserted or omitted.

Isolated and owner words/bindings agree. The complete owner has three
functions; both neighbours, pools and exact register-mask union are preserved.
Both padders and the actual **three-command Make recipe** agree.

The literal whole-ELF prediction changes **294 bytes**, with zero exclusions.
It accounts for the target body/extent and three closed symbol/name groups:

- D_8009D480 / D_8009D7D0 exchange.
- D_800AA434 moves after D_800A0618, D_800A0248, D_8009FE48 and D_80096A48.
- D_800AA9C4 / D_8009CF80 exchange.

All nine metadata definitions and their strings are reconstructed from frozen
predecessor rows; actual output metadata is not copied or exempted. Every
named definition remains the same except the target extent. All 6,052
disassembled function entries retain their addresses, and all 720 protected
data owners /189,088 bytes remain exact. The entire inherited guard CSV is
an unchanged literal prefix with seven target-only rows appended.

## Focused qualification

All eight checks pass before and after installation in the mounted tools
and in a read-only overlay for the sibling tools checkout:

- **4,488 guest cases per body** compare original, raw C and fitted C against
  an independent byte-memory model. This covers equality boundaries, reset,
  negative/zero/subnormal/nonfinite phases, live sound/sine mutations, saved
  state-pointer reloads, output order and status forwarding.
- **168 alias cases per body** include global/record overlap and guest-only
  saved-pointer/home mutations. **482 fired fault-prefix pairs**, including
  **22 delay-slot cuts**, compare complete fitted/retail RAM, registers, trace,
  PC and delay state. Portable C fault behavior is not claimed.
- **288 original caller cases per body** qualify selector zero/slot5, gate
  restoration and zero/nonzero statuses across the real 13-word window.
  The complete parent remains outside this qualification.
- **288 connected cases per body** execute original helpers: sine 100/104
  words, all 80 words of `func_15133894`, all 53 of `func_151337C0`, and all 29
  of the sound adapter `func_10010F88`. Statuses include 0, 1, 7 and -128.
  Sound-inner, geometry and selected event implementations remain bounded
  ABI providers; full sound/gameplay/FCSR correctness is not claimed.
- **Nine GNU links /72 rebased cases per body** independently bind original,
  raw and fitted objects, exercising signed HI/LO carry edges and call rebases.
- All 308 one-byte raw corruptions, all 13 altered relocation identities,
  all 7 changed guard expectations, and selected whole-image/metadata
  corruptions are rejected. All 12 compiled semantic/return controls fail
  observable guest checks; the constant-return control also fails the caller.
- Native32 **O0/O2/O3**, **1,512 cases per profile**, trapping UBSan, typed
  sound arguments, callback return values, helper observations and whole-owner
  canaries pass. All 12 incorrect implementations are detected. Numeric
  fields are initialized from guest bit patterns while byte canaries remain
  byte arrays. Guest-only private-pointer/global aliases and nonfinite phases
  are excluded from native claims; arbitrary NaN payload/FCSR hardware
  equivalence is not claimed.

Production object/ELF equal the independent prediction; the authoritative
linked recount gives the totals above. The existing whole-ROM checksum
mismatch still makes `make all` exit 2. Target build/link/progress and recount
pass. The inherited duplicate generated_12D630 Make warning is unchanged.
Fresh shared tool smoke passes in both copies; three unchanged regressions
per copy are reused by exact helper/test fingerprints, not called fresh.

## Bank and next boundary

Receipts: `conker/build/game-timed-scale-callback-151B5E94-match/`.
The 109 frozen inputs, original assembly, ROM, conversion CSV, shared headers
and build profile remain preserved. The sibling tools checkout's 2,434
inherited dirty paths are unchanged; the host Release remains frozen.
Tools commit before the consumer pin. The scoped Graphify refresh retains
existing unscanned nodes with evidence; it is not full-corpus extraction.

Next: **func_150C5568**, owner `generated_F2820`, the next 79-word unmatched
Game routine in the measured queue. Its retail body/ABI/callers/profile must
be audited before drafting, adoption or credit. The 80% goal remains active.

Production ELF SHA-256: `e595c99dbd582c24acb4a4d8f470d8ed7a77e33c778c29f3e1c0cdaa13d336ac`.

Production guard SHA-256: `a5900bb1585998e2024fbf36baa3b92518f40789fa4d6c0937f2050f25eaab8b`.

Raw C SHA-256: `25a11fe76c1a2ced5c49cbd13e3b708c95cd3550a3f6a1a5b71a41241d2cba89`.
