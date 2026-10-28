# 1774 - Actor Volume Selection Match - 2026-10-28

The adopted Native ELF measures **3,852/5,506 exact C functions (69.96%)**,
Game **3,179/4,833 (65.78%)**, zero address drift and 1,654 different.
Only `func_150A2EE4` gains matching credit. The unchanged 75% threshold is
4,130 exact C functions, requiring **278 more**.

## Recovered routine and interface

`func_150A2EE4` in `generated_CDE80.c` occupies VA
`0x150A2EE4..0x150A2FA4`, ROM `0xD0394..0xD0454`: 48 words,
a 24-byte frame and seven bindings. The complete body emits directly from
semantic C under the normal O2/g3 profile, without new guards.

The interface is `s32(s32 actorIndex, s32 selector)`. Mask selector to
12 bits, then compare it against `D_800D3094` as unsigned. A selector
above that bound returns one. Otherwise, load the table pointer
`D_800D3098` and inspect byte +0x15 of its selected 52-byte record.
If the low two flag bits are not both set, return zero. A qualifying record
calls `func_150A2E4C` with its pointer and the selected actor's x/y/z
positions, forwarding the signed word result unchanged.

`D_800CC2D0` is an inline array of 26 canonical `struct127` actors,
with stride 812 and float positions at +0x14/+0x18/+0x1C. The new owner-local
extern matches the existing shared declaration. Shared headers remain
unchanged. The mixed O32 signature passes the record pointer and three float
bit patterns in GPR arguments; no float-to-integer conversion is introduced.

| Binding offsets | Symbol | Purpose |
| --- | --- | --- |
| +12/+16 | `D_800D3094` | Unsigned selector bound |
| +36/+56 | `D_800D3098` | Record-table pointer |
| +104/+108 | `D_800CC2D0` | Inline actor-table address |
| +160 | `func_150A2E4C` | Plane query |

## Original caller and retained helper

The complete ROM census finds one direct site, ROM `0xCDC10` / VA
`0x150A0760`, and no target pointer literals. The original parent is
`func_150A04D8` in `generated_CD860`. Its current C remains a
zero-return placeholder and its object is preserved.

Tests load the complete 317-word original dispatcher and execute its
command-13, actor-reference-kind-0x2000 route through the final return.
The route executes 46 distinct parent words. Its lookup provider
`func_1505EEF4` is bounded, returning an actor pointer. Original
instructions subtract the inline base, divide by 812, call this query and
propagate its result through the stack return join. All 162 cases pass.
This does not qualify other dispatcher routes or credit the parent.

All 38 words of retained `func_150A2E4C` equal retail and execute in
24 connected finite IEEE-single cases. Preserve the helper's existing
behavior: its third displacement is computed from the adjusted second
coordinate, not the incoming z argument. Existing helper guards remain
unchanged. No complete-gameplay or hardware FCSR claim is made.

## Complete owner and image

Preserve all 27 neighboring functions, raw/padded bindings and pools,
including two GLOBAL_ASM routines. The actual five-command Make recipe
preprocesses, compiles, post-processes, pads and assembles the complete
28-function owner with zero compiler diagnostics. The inherited duplicate
recipe warning for generated_12D630 remains unchanged.

Strict independent prediction permits exactly **158 changed image bytes**:
157 target code bytes and one target symbol-size byte (12 to 192), with zero
exclusions. Production reproduces that image. All 6,056 disassembly addresses,
all 6,055 other bodies, named ELF definitions, section geometry, map and C
inventory stay fixed. All 720 Game data owners /189,088 bytes remain exact.

## Behavioral qualification

Both tools copies pass eight fresh canonical methods and shared tools checks.
Production reruns two installed methods per copy; six semantic methods are
reused only after exact input, module and artifact fingerprint comparison.

- 2,562 guest cases cover full-word actor/selector inputs, unsigned count
  boundaries and equality, all 256 flag bytes, raw float payloads and 38
  stack/table/coordinate overlaps. All 48 words are visited; complete state
  and ordered traces agree. Guest wrap/alias cases are not portable C claims.
- Native32 O0/O2/O3 each pass 552,448 cases with trapped UBSan, all 4,096
  masked indices, all 26 canonical actors, all flag bytes, full storage
  fences and the actual two-input function-pointer type. All eight semantic
  negatives fail in each profile. The native helper is bounded; NaN payload
  forwarding is covered in the guest model, not claimed for host float ABI.
- 256 fired access-prefix pairs preserve state, trace, PC and delay context.
  Unmapped input tests verify early bounds skip the table/actor reads and
  inactive flags skip actor coordinates.
- Three real GNU layouts pass 54 guest cases using original, compiler and
  actual-Make objects. They exercise three HI/LO pairs and the J26 binding.
  Three raw/binding rejections, four actually compiled IDO semantic negatives
  and six full-image corruption controls reject changed behavior/evidence.

## Bank and continuation

Baseline consumer `6512752b`, tools `4264e56`. Tools are committed
first as `df938bc1e180a879078cae939489cdde612cc638`. The seal verifies 16,309 files and 310 focused
inputs. Preserve all 1,763 inherited dirty paths in the older independent
tools mirror, adding only the three target modules there. No mirror commit
or push. Host Release remains frozen.

| Artifact | SHA-256 |
| --- | --- |
| Adopted ELF | `e8697a890df7767b6735d4ceca7a9260b650ad275c1db9361c2f1f2073465f3e` |
| Padded owner | `01fbba0a8d4407d1af433c3185c139f3b6e3bc39c92f982def0b2554872b8f43` |
| Recovered source | `d642e9095b50c34d5624f03e16bf24e30cc00c1206b0a63b1aab4e4fe8f08b01` |
| Raw original/compiler body | `3102da592480e9abbe81c272c08d148adea860fca7f985c4d5d1b163938d7754` |
| Complete retail body | `8f5f5daa3897b38b76186df1307e83feb7c33849f1c27ad7465d57562f17c1af` |
| Unchanged guard CSV | `20131e428c071ea6d2cbee21968f122274bc71fb167a2a356b3033ff5582f8b9` |

Scoped Graphify closeout refreshes eleven changed C/Markdown/tool files.
Retain all 46,050 old nodes and all 94,484 old relationship contexts;
validate the s32 result, two parameters, seven bindings and original caller
route. Preserve outside-scope manifest freshness and historical communities.
Do not invent a current placeholder-parent call edge or claim full-corpus
extraction.

Next inspect the 48-word `func_150C5370`. The remaining queue has 1,525
placeholders, 120 semantic/other entries and nine unlocated screens; this is
triage only. Keep `func_1514E920` parked and uncredited and the 75% goal
open. Routine Claude calls: zero.

Prepared-checkout command: `python3 -m unittest tools.tests.test_game_actor_volume_selector_match -v`.
