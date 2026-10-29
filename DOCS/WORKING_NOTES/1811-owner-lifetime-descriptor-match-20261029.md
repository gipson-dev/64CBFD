# Owner lifetime descriptor: direct C match

Verified 2026-10-29. `func_150F6890` replaces its zero-return placeholder in
`conker/src/game/generated_1228D0.c`. All **51 instructions** emit directly
from semantic C under the existing IDO `-O2 -g3` profile. The complete
204-byte slot, 88-byte frame, argument homes and three external bindings match.
There are no guards, inserted instructions or alignment words.

The adopted ELF recount is **3,889 / 5,506 (70.63%)** byte-exact C functions:
Game **3,216 / 4,833 (66.54%)**, Init 492/492 and Debugger 181/181. Address
drift is zero; 1,617 C functions still differ. The 75% threshold is 4,130,
leaving **241**. The conversion inventory remains unchanged.

## Recovered behavior and interface

`void *func_150F6890(u8 *owner, s16 lifetime, s32 unusedSelector,
s32 unusedContext)` constructs a 60-byte owner-attached effect descriptor and
passes it to `func_15134DAC` with a zero context argument. It forwards the
constructor's pointer, including NULL on allocation failure. The original
four-argument interface stores all incoming argument homes; selector and
context are unused by this routine.

The packet retains the owner's identity byte at offset `0x3B`, the owner
pointer, attachment index 3, four zero floats, the raw global float
`D_800A1B70` (`0x40966667`), and the 8.5 and 1.0 float constants. It stores
mode 2, active duration 40, restart delay 16, and the requested signed lifetime.
The known callback indices are 5 and 8; two other callback indices are -1.
Unknown field meanings retain offset-based names. Unwritten padding remains
unwritten rather than introducing an initialization absent from retail.

The two final instruction differences were declaration errors: unsigned
fields made IDO load 255 instead of -1. The original reader `func_15134E48`
loads both output fields with `lb` and compares them with -1 before indexing
callback tables. Signed callback fields therefore recover both the actual
contract and the exact instructions. The assignment order also retains the
late halfword-zero store without a scheduling guard.

The full-ROM census finds one aligned direct call at ROM `0x54E1C` and no
aligned target pointers. Its parent, `func_150265CC`, remains a C placeholder.
The original ten-word window at `0x15027954..0x1502797C` checks a nonnull owner
and a positive gate, loads a signed halfword lifetime and a byte selector,
and supplies context 1. It discards the returned pointer and sets its own
success result to 1. The complete large script interpreter is not recovered
or qualified by this bounded window.

`func_15134DAC` is already semantic C and its current linked 39-word body is
retail-exact. It allocates a type-41 record with size 128, copies all 60 packet
bytes to output offset `0x18`, initializes the timer from the negated restart
delay, sets flags, and clears three float accumulators. The connected audit
executes that original body and the original 11-word `memcpy`; allocation
remains an explicit service boundary.

| Evidence | Value |
| --- | --- |
| Complete-slot VA | `0x150F6890..0x150F695C` |
| Complete-slot ROM | `0x123D40..0x123E0C` |
| Owner | 24 compact functions; all 23 neighbors unchanged |
| External bindings | HI16/LO16 `D_800A1B70`; JAL `func_15134DAC` |
| Raw/original body SHA-256 | `cf82ae22323ed1bf78ff436da1b3a795402d0f552811cb91e32f845ad16f0403` |
| Linked body SHA-256 | `ae328ab754633ddfba8b2d6f04e9a16299b961396fcc5268de11906ad7134aa6` |
| Adopted ELF SHA-256 | `e6af63004a57758664ba2af2ea3c311eda2a1be40ec2e3582f25407415674050` |

## Qualification and production audit

Both tools copies pass eight fresh focused methods and their shared tools
checks. After production, both pass two fresh installed checks and reuse the
six unchanged semantic checks by complete input/module/artifact identity.

- **503 guest cases** cover all 51 words, every identity byte, signed lifetime
  boundaries, arbitrary float bits, ignored arguments, and helper mutations.
  Full registers, RAM, traces and all 60 packet bytes agree with retail.
  Sparse addresses and incoming-home overlap are explicitly guest-only cases.
- **160 connected cases** execute all 39 constructor and 11 copy-loop words,
  including allocation failure and mutations before copying. **96 caller
  cases** cover all ten original window words, null/positive-gate rejection,
  signed lifetime loading, and the caller's discarded pointer result.
- **7,168 native32 SDK cases per profile** pass at `-O0`, `-O2`, and `-O3`
  with trapping UBSan and canaries. Native checks use valid objects and
  exclude indeterminate padding. Eight incorrect C bodies fail both native
  and compiled-MIPS checks, including a fabricated NULL return.
- **405 paired fault prefixes**, including 128 delay-slot cuts, agree in full
  state, trace, PC and delay state. This is emitted-instruction evidence,
  not a portable C fault-behavior claim.
- **72 cases across three GNU layouts** rebase the constant and helper,
  including signed-low carry boundaries. Original, raw C, padded and actual
  Make bodies agree. Fifty-four raw-word/binding corruptions are rejected.
- **238 whole-image corruptions** are rejected. The guard CSV is unchanged
  and independently fingerprinted; no new guard rows are installed.

This owner's actual Make rule has three commands: compile, generated-owner
padding, and assembly. It reproduces the qualified object. The ten existing
pointer/integer warnings in other owner functions are checked by exact
statement and diagnostic identity; the recovered target adds no warning.
All raw and padded neighboring bodies, bindings and pools remain unchanged.

The complete ELF changes by **185 bytes**: 156 target code bytes, one
function-size byte, and 28 symbol/string metadata bytes. Referencing the
recovered constant rotates two existing three-symbol GNU linker buckets.
The predictor validates all six original named definitions and serialized
slots before applying those exact permutations. No comparison bytes are
excluded. All 6,056 function addresses, 6,055 other bodies, and 189,088
protected Game data bytes across 720 owners remain fixed. Shared headers,
compiler profiles, guards and conversion CSV are unchanged.

The production Make build reproduces that independent whole-image prediction.
The native adoption checks 538 focused inputs and 16,575 sealed current inputs.
The older tools mirror retains all 1,874 inherited dirty paths plus the three
new qualification modules. Tools commit
`325527b202dfd9a6134d89a7dfea307c9f31df90` precedes the consumer commit.
No push is included.

Ignored evidence is in `conker/build/game-owner-lifetime-descriptor-match/`.
The final audit checks the banked state and the eleven-file Graphify refresh,
including previous-node and valid-relationship retention. Historical global
graph analytics are not represented as a fresh full-corpus scan. No emulator,
host-port or gameplay acceptance is inferred from these decomp checks.

Next inspect **`func_15108AB4`** in `generated_135D00.c`. The parked
`func_1514E920` and formatter-dependent `func_151D7000` remain uninstalled and
uncredited. The 75% matching goal stays active. Routine investigation used
zero Claude calls.
