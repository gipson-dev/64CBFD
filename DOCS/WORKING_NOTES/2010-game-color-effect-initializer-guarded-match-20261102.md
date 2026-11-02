# 2010 - Color-effect initializer matched as guarded C

Verified 2026-11-02. Production **4,077/5,511 (73.98%)**; Game
**3,404/4,838 (70.36%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,434 different; one zero-return placeholder is replaced by qualified
semantic C and is newly byte-exact. The active 80% target is **4,409/5,511**,
requiring **332 more**. This is progress toward that goal, not completion.

## Recovery and pool contract

`func_15187EC0` is the five-entry color-effect initializer at VA `0x15187EC0`
and ROM `0x1B5370` in `conker/src/game/generated_1B5370.c`. Its recovered O32
interface is:

```c
s32 func_15187EC0(s32 mode, f32 rate, u8 startRed, u8 startGreen,
                  u8 startBlue, u8 targetRed, u8 targetGreen, u8 targetBlue);
```

The signed counter `D_800DF7B4` selects a 36-byte record in the 180-byte
`D_800DF700` pool while the count is below five. The routine writes start RGB,
target RGB and a duplicated current RGB; preserves the three padding bytes and
the blend word; stores the complete mode and raw rate words; clears the final
12 state bytes through `bzero`; reloads and increments the global count; and
returns the appended index. Counts of five or more return `-1`. Retail does not
reject negative counts, so no lower-bound check, clamp, pool clear or invented
behavior was added.

The source now uses a local `ColorEffectRecord15187EC0` layout and descriptive
parameter names. The public declaration narrows the six RGB arguments to their
observed byte ABI. All three original direct callers compile and preserve their
retail argument setup. The numeric suffix remains in the type and function name
because no authoritative retail name is known.

## Guarded compiler closure and repaired access order

Fresh IDO emits the natural 52-word body with the retail 24-byte frame but 25
linked scheduling differences. The unguarded candidate reads `startBlue` before
the full-pool rejection. Retail performs the capacity branch first and groups
the byte loads in the accepted path. Exactly 25 checked expected-word
replacements close that schedule and restore retail's access order in the final
object; there are no insertions or omissions.

Three rows cross the pool-address HI/LO relocation transition. Their expected
and replacement relocation metadata is checked explicitly. The original link
and three independent rebases reproduce all 52 retail words, and independent
mutation of every expected word and relocation-bearing expectation produces 50
fail-closed cases.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `5c704119b6044bdd78458bc9350a0225369d75bc3b7c52502f50cea597cc68d4` |
| Qualified/production owner | `8aa2dfe67e89fb357206cbe88ef1a84c6492373d8752e4949a5ffcbd5fdcf5bc` |
| Qualified/production linked ELF | `e27a83e2af6dd164bcf80349f04257422c2fca30e10454f317937aae92b08870` |
| Raw candidate object | `2c60f7fef98a215cb730eee11b6850793b4ba827e264ac494090939a30f0e2d3` |
| Raw linked 52-word body | `d831e4b0d21e7128b6a11b34e89469f7e58c870bd62681cf3327780defc3e05e` |
| Retail/guarded 52-word slot | `1ef30ce7148ede89170c9bf16dd6439a9abe92110a935a8211f935222dc5` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |
| Guard manifest | `771bedc32e892847baf153ccc86666c56bbe0d00e12c320fdeeb8e858a5d2f00` |

## Semantic, caller, owner and image qualification

Six permanent tests pass in 21.441 seconds. The guest corpus covers **11,256
cases / 33,768 executions**, all 52 retail words, all byte values, raw float and
mode words, accepted/full counts, mapped negative-count behavior, aliases and
the original `bzero` route. The caller corpus covers **120 cases / 240
executions** across complete parents `func_15009BD0`, `func_15009C7C` and
`func_15009F74`. Native O0/O2/O3 each pass 1,760 cases for **15,840 total
executions**, with eight effective controls rejecting plausible wrong
implementations.

All five owner neighbors and their relocations remain byte-for-byte unchanged.
Strict whole-image prediction changes only the 208-byte target slot and its
symbol extent from 12 to 208 bytes, keeps every address fixed and uses zero
exclusions. Actual Make reproduced the qualified owner and predicted linked ELF
byte-for-byte. Changing the shared prototype forced a full dependency-corpus
rebuild; every generated, converted and libultra owner compiled, every existing
guard remained current, all three real callers passed the narrowed ABI, and the
final link succeeded.

The full `make -C conker all -j2` pipeline regenerated the development ROM and
stopped only at the expected final retail SHA-1 mismatch because the wider
decomp image is not yet byte-identical. Protected Game data remains exactly
189,088 bytes across 720 owners with zero different bytes, SHA256
`0bbc00e1adfac5ffe611f5be9c941575f87b341a77d808004603ac1cb87c670`.
This is instruction-level and bounded semantic proof, not natural whole-game
effect, rendering or gameplay acceptance.

The permanent experiment and qualification suites were committed first in the
tools submodule as commit `e201cb8`. The retained qualification stage is
`conker/build/game-color-effect-initializer-15187EC0-guard-match/`. This closes
the access-order limitation recorded in [Note 1973](1973-color-effect-initializer-private-qualification-20261101.md);
that earlier private candidate remains useful provenance but no longer defines
the production status. The root README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,121 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph SHA256
remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep
handwritten/custom-ABI work on its separate track, and keep every new candidate
private until source, ABI/callers, owner, guest/native, actual Make, complete
image, protected-data, production recount and documentation gates pass.
