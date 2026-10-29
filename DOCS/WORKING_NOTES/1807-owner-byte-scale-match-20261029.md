# Owner byte scale and callback result: guarded C match

Verified 2026-10-29. `func_150C7670` replaces its zero-return placeholder in
`conker/src/game/generated_F4B20.c`. Semantic C emits 50 instructions with
no stack frame. Two expected-word guards move the existing success-result
assignment and retain the retail nop, reproducing the complete 51-word slot.

The adopted ELF recount is **3,885 / 5,506 (70.56%)** byte-exact C functions:
Game **3,212 / 4,833 (66.46%)**, Init 492/492 and Debugger 181/181. There is
no address drift; 1,621 C functions still differ. The 75% target requires
4,130 exact functions, leaving **245**. Conversion inventory is unchanged.

## Recovered behavior and interface

The routine follows the pointer at `owner + 0x170`, then the pointer at
that object's offset `0x14`. It reads an unsigned byte at the linked data's
offset `0x2F`, converts it to float and multiplies it by `D_800A04C0`.
It truncates the product to `u32`, stores the low byte at `owner + 0x70`,
and returns one. The scale's retail bits are `0x4013020D`, approximately
2.29700017. Explicit conversion to `u32` before the byte assignment preserves
the wrap for products above 255 without an out-of-range float-to-byte cast.

```c
s32 func_150C7670(u8 *owner);
```

Its original indirect route is slot six of the 32-byte `D_80089914` table,
whose target pointer is at ROM `0x22E3EC`. The qualified 16-word window in
`func_151321D0`, VA `0x15132278..0x151322B8`, calls with the owner pointer
when its selector is nonzero and the incoming gate is zero. A nonzero result
preserves that gate; zero sets it to one. The parent remains a C placeholder;
this work qualifies the original window, not the entire parent or gameplay.

| Evidence | Value |
| --- | --- |
| Target virtual range | `0x150C7670..0x150C773C` |
| Target ROM range | `0xF4B20..0xF4BEC` |
| Owner | Two compact functions; `func_150C773C` preserved |
| Compiler profile | Existing IDO `-O2 -g3` |
| Raw bindings | `D_800A04C0`, HI16 at byte 40 and LO16 at byte 44 |
| Normalized bindings | HI16 at byte 44 and LO16 at byte 48 |
| Guard at raw byte 4 | Keep `0x3C014F80`, insert existing `0x24020001` |
| Guard at raw byte 188 | Replace `0x24020001` with retail `0x00000000` |
| Raw body SHA-256 | `7338d6ce91693b653f5fb7d221fa51527fd673538205683b90f21ff66a8c6219` |
| Normalized object body SHA-256 | `2cf90d8c9259d597783d72619cfc435517ae1e96ed59766e54b9b32e6e8fd141` |
| Retail slot SHA-256 | `217bd2d89fb57cc1ae6089f13274ca0af13b8176e8b64a4e58a7ae254d1ddaed` |
| Adopted ELF SHA-256 | `c93de765466346ab35b5ef9e1e2635ef3486a425a94a1bd5a08fa836a42d74ae` |

The existing result instruction moves to retail byte eight. All internal
branch sources and destinations shift together, preserving their relative
offsets. No semantic operation is added. The guard CSV retains its exact
inherited prefix and appends two rows; no headers or compiler profiles change.

## Qualification

The private suite and both tools copies pass eight methods. Both shared
tools checks pass. Production reruns two installed checks per copy and reuses
six semantic checks only after full input, module and artifact identity checks.

- 1,616 guest cases cover every input byte, two stack phases, three saved
  FCSR patterns, 77 synthetic scale vectors and three alias layouts. Original
  and normalized executions agree in RAM, registers, trace and FCSR; raw C
  agrees in public memory and result.
- 47 of 51 original words are reachable in the qualified domain. Three
  instructions implement a negative-input correction that cannot follow
  the unsigned byte load; one duplicate `mfc1` follows an unconditional
  branch. All four unreachable retail words remain in the final slot.
- Sixty original-caller window cases exercise selector/gate skips and the
  valid callback. A compiled wrong-return control executes the otherwise
  unreachable failure arm and sets the gate, proving the result is consumed.
- Native32 SDK tests pass 3,072 vectors per `-O0`, `-O2`, and `-O3` profile,
  with trapping UBSan, typed pointer fields, canaries and precomputed expected
  bytes. Six compiled incorrect implementations fail observable checks.
  Negative, NaN and overflowing synthetic conversions are guest-only tests.
- Forty-five fault-prefix pairs include three delay-slot cuts and compare
  full RAM, registers, trace, PC, delay state and FCSR. These qualify emitted
  instruction order, not portable C fault semantics.
- Three GNU link layouts pass 48 cases, including signed low-address carries.
  All 50 word corruptions, both relocation corruptions and four actual-padder
  guard corruptions are rejected. Sixty-four whole-image controls include
  every byte of the two exchanged symbol records and their name strings.

FCSR claims are limited to bounded conversions and restoration of control
state. This is not hardware, arbitrary-rounding or NaN-payload qualification.
The final module suite was rerun in both copies after removing an extra EOF
blank line; its AST and qualification behavior were unchanged.

## Production and preservation

The actual three-command owner Make rule agrees with the selected/padded
object and emits no diagnostics. The neighbor's body, relocations and pools
are unchanged. Production reproduces the private image exactly.

Independent whole-image prediction permits **146 changed bytes**: 127 target
code bytes, one symbol-size byte, and 18 symbol metadata bytes. The latter
are an explicit two-entry permutation of `D_800A749C` and `D_8009E77C` in
the symbol/name tables. Their named definitions, addresses, sizes, types and
sections are unchanged. The predictor reconstructs this permutation from
the frozen input; it does not exclude metadata from comparison.

All 6,056 disassembled function addresses and 6,055 other bodies are
preserved, along with 189,088 protected Game data bytes across 720 owners.
482 focused inputs and 16,547 sealed current inputs are checked. The older
tools mirror retains 1,862 inherited dirty paths plus the three new modules.
Tools are committed first as `595e5bb26116f12e6d421b6d8a0e9a28feceacdf`;
the consumer commit contains the C recovery, guards, tools pin and measured
documentation. There is no push or sibling host/Release change.

Ignored receipts are in `conker/build/game-owner-byte-scale-match/`.
After the consumer commit, `FINAL_AUDIT.json`, `BANKED_STATUS.json` and the
banked seal record the independent audit. Graph refresh covers eleven changed
source/document/tool files, retaining old nodes and valid relationships.
The original indirect route is annotated separately from current C calls;
global analytics and full-corpus extraction are not claimed.

## Next work

Inspect `func_151B6254` in `generated_1E34C0.c`, the next unparked placeholder
in the measured queue, at 51 words. Qualify its interface, callers and owner
before adoption. `func_1514E920` remains parked and uncredited. The 75% goal
stays active.
