# Working Note 1812 - Owner phase-pair callback match - 2026-10-29

`func_15108AB4` now advances two phases, wraps them into the angular interval,
computes their sine-scaled offsets, refreshes the owner timer and lookup value,
and returns 1 to keep its indirect callback active. Its previous C body returned
zero without performing those updates.

The recovered interface is `s32 func_15108AB4(u8 *owner)`. The original address
name is retained. The local variables and comment describe the recovered
behavior without guessing a game object name.

- Owner: `conker/src/game/generated_135D00.c`.
- Original: `conker/asm/135D00.s`, VA `0x15108AB4..0x15108B80`,
  ROM `0x135F64..0x136030`.
- Complete slot: **51 words / 204 bytes**, 32-byte frame, saved S0 and RA.
- Compiler output: **51 words**, with all 16 relocation bindings preserved.
- One expected-word guard swaps only the two source registers of the
  commutative unsigned `ADDU` at offset `0x2C`: `0x01C48021` to `0x008E8021`.
  Both forms compute the same modulo-32-bit address. No instructions are added,
  removed, or moved; no relocation changes occur. The other 50 words emit
  directly in the original order.

## State and caller contract

The state pointer is `owner + *(s32 *)(owner + 0x50) + 0xF8`. It remains in S0
across six calls. Phase values occupy state offsets 8 and 12, and the derived
outputs occupy offsets 0 and 4. The two phase updates independently read
`D_800BE9A4`; their speed constants are `D_800A2470 = 0x3DAF837B` and
`D_800A2474 = 0x3DA05BC0`. The amplitudes at `D_800A2478` and `D_800A247C`
both contain `0x40E35C2A` and are loaded after their sine calls.

The original ROM has no aligned direct JAL to this function and exactly one
aligned pointer to it, at ROM `0x22E6D8`: slot 0 of `D_80089C18`.
`func_1513B798` passes the owner in A0, handles lifetime expiry and callback
index -1, and releases the object if its callback returns zero. The current C
caller in `conker/src/game_168A90.c` used an unspecified-parameter callback table
and an empty argument list. It now declares `s32 (*D_80089C18[])(u8 *)` and calls
`D_80089C18[callbackIndex](arg0)` explicitly.

All 13 compact functions in that caller owner, its pools and bindings, and its
entire padded object remain unchanged. The two existing completion-flag spill
width guards at caller offsets `0x64` and `0x74` are retained. The caller's four
existing warnings are unchanged; the recovered target owner has none.

## Qualification evidence

The local evidence directory is `conker/build/game-owner-phase-pair-match/`.
The initial 547-file intake remains immutable. The three separately frozen
caller inputs are checked through their own pinned manifest, for **550 focused
inputs**. The complete seal contains **16,582 inputs** after adding the three
qualification modules to both tools copies.

Eight fresh canonical checks pass independently in the active tools checkout
and the older mirror. The shared project-tools checks also pass in both.

- **306 guest cases** cover all 51 target words, all three bodies (original,
  normalized, and raw compiler output), float access order, four clock aliases,
  signed state offsets, incoming argument-home changes, and complete memory,
  register and access-trace equality. Volatile GPR/FPR and HI/LO clobbers test
  the saved state-pointer lifetime.
- **384 connected cases** execute the complete original 104-word sine routine,
  24-word angular normalizer, 16-word timer updater, and 30-word value updater.
  This domain reaches 86 sine words and every word in the other three helpers.
  All four helpers are already byte-exact in the current linked image.
- **160 complete original-caller cases** execute its 41 words with callback,
  disabled-callback, lifetime-expiry, and retained-owner paths. The caller itself
  is already byte-exact in the current image.
- **128 native 32-bit SDK cases per optimization** pass at `-O0`, `-O2`, and
  `-O3` with trapping UBSan and valid aligned owner backing. Byte-based owner
  access uses `-fno-strict-aliasing`; surrounding storage is checked. Seven
  semantic mutations fail these checks as expected.
- **135 direct/connected fault prefixes** and **46 caller fault prefixes** agree
  in complete state, PC, delay context and access trace. The direct/connected
  set includes 27 delay-slot cuts.
- **30 cases across three GNU link layouts** preserve all 16 bindings and the
  single ADDU guard. **67 raw-word/binding corruptions** are rejected.
- **Eight compiled bad-body controls** have semantic counterexamples. The
  cached-clock control is distinguished by a guest global/state alias; private
  stack addresses are excluded from the decision.
- **188 whole-image corruptions** are rejected, including changes in the caller,
  callback table, neighboring function, symbol records, header, and file length.

Guest-only argument-home/global alias cases do not claim portable C behavior.
The native math calls are scripted to test the recovered C and its call order;
connected guest execution separately checks the original math implementations.
Infinite or unbounded angular-normalization inputs, arbitrary FCSR settings,
hardware parity and full gameplay are not claimed.

## Build, image and adoption

Actual Make recipes execute three commands for the target owner and three for
the caller owner. They reproduce the qualified target object and the unchanged
caller object. All **10 target-owner neighbors** are unchanged in compact and
padded views, with no pool change.

The independent complete ELF prediction matches the production build exactly:
**181 changed bytes = 166 target code + 1 function extent + 14 symbol/string
serialization bytes**, with **zero excluded bytes**. The metadata change is a
closed swap of existing definitions `D_80099814` and `D_8009EE64`; both names,
values, attributes and serialized positions are validated. All **6,056 function
addresses** and **6,055 other function bodies** are unchanged. All **189,088
protected Game data bytes across 720 owners** remain exact.

Tools were committed first as `289df16`. Production and native adoption pass
the full input seal. Each tools copy then runs two fresh installed checks and
reuses the other six only after confirming identical source, tools and artifacts.
The progress inventory CSV is unchanged. The inherited guard CSV prefix is
unchanged and exactly one new row is appended. No push is performed.

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler target | `e10684cfe0226bfc64fb5fc0ed076a9c9bb8dfbe80dc441b1dfc771d1ba526f5` |
| Normalized raw target | `a30a36903230ad4922e395bf5e950f91d1793d8b11f01f804ab2014d8ff6e211` |
| Recovered owner source | `9d44a5031364c66003f66408d72ac334331962d49e40b161f560ae2b5a871305` |
| Padded owner object | `1357cd2a29d9fe36576f6eabdf3a999f42aa4536f3b2006e002e20cd642e2089` |
| Produced/adopted ELF | `012521835d1ec8992937f707b4ff2fdfbb3bb9356d573383dff222b0f2ec3143` |
| Guard CSV | `1e58e8b29313c9ffe2b784379c53af9fdc8eb9152c9bb3d1e1a5fb832a5d26b6` |

The actual adopted ELF recount is **3,890 / 5,506 exact C functions (70.65%)**,
including **3,217 / 4,833 Game (66.56%)**, **492 / 492 Init**, and **181 / 181
Debugger**, with zero address drift and 1,616 remaining differences. The 75%
threshold is 4,130 exact C functions: **240 more** are required.

## Continuation

Inspect `func_1518AA10` next, starting with its full original body and callers.
The queue is a screening aid, not qualification. `func_1514E920` and
`func_151D7000` remain parked and uncredited. The latter still requires resolution
of its formatter return contract. The scoped Graphify refresh and final
independent seal are recorded beside this note's local build evidence; global
clustering and full-corpus re-extraction are not claimed.
