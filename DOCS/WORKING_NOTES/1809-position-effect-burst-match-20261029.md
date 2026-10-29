# Position effects and randomized burst: direct C match

Verified 2026-10-29. `func_151D5648` replaces its zero-return placeholder in
`conker/src/game/generated_200930.c`. All **51 instructions** emit directly
from semantic C with the original 48-byte frame and five call relocations.
There are no new guards, inserted instructions or separate alignment words.

The adopted live ELF recount is **3,887 / 5,506 (70.60%)** byte-exact C
functions: Game **3,214 / 4,833 (66.50%)**, Init 492/492 and Debugger 181/181.
There is zero address drift and 1,619 C functions still differ. Reaching 75%
requires 4,130 exact functions, leaving **243**. Conversion inventory is unchanged.

## Recovered behavior

`void func_151D5648(f32 *position, u8 kind, s32 mode)` first calls
`func_151D5514`, then `func_151D3FF4`, with the position, kind and mode.
It samples `func_150ADA68` for a float and `func_150ADA20` for an integer,
in that order. It finally calls `func_151541B8` with the position, the float
sample multiplied by four and increased by twelve, coefficient `1.6409999f`,
the unsigned integer remainder modulo 56 plus 200, `0.0f`, kind and mode.
The final factory pointer result is discarded.

The coefficient has retail bits **`0x3FD20C49`**. Writing `1.641f` instead
emits the next float, `0x3FD20C4A`. Declaring the unsigned integer temporary
before the float also recovers the original float stack home at `SP + 0x28`.
The source preserves the repeated argument loads across helper calls.

The full retail ROM census finds one aligned direct call at `0x55F50` and
no aligned target pointers. Its original parent is `func_150265CC`, still a
C placeholder in `generated_50D80.c`. The 13-word window at
`0x15028A7C..0x15028AB0` copies three position floats to its stack, supplies
the byte at `SP + 0x773` and mode one, then discards the target result and
branches to `0x15029BA4` with `V0 = 1`. No current C caller or complete
parent recovery is claimed.

| Evidence | Value |
| --- | --- |
| Body / full-slot virtual range | `0x151D5648..0x151D5714` |
| Body / full-slot ROM range | `0x202AF8..0x202BC4` |
| Owner | 28 compact functions; all 27 neighbors unchanged |
| Compiler profile | Existing IDO `-O2 -g3` |
| Call relocation offsets | 28, 44, 52, 60 and 180 bytes |
| Raw and original object-body SHA-256 | `a13fdeb94700740a64eafae1c74968b287ef59601a996218f390a7f4696989c6` |
| Retail linked body SHA-256 | `5b74d3322e82539b7d7bf896c45a5b6dfb7b383e79763760c46540dd83d16b57` |
| Adopted ELF SHA-256 | `c5a6aaa4f456945acddc61bade7f17188756d3cd3195b4af1dd77b8d416b0f8d` |

The two initial effects and final factory remain retained assembly providers.
The random helpers are also retained `GLOBAL_ASM`; their disabled C descriptions
in `game_DAE50.c` do not count as recovered definitions. Local declarations
recover their actual interfaces without changing their source or shared headers.

## Qualification

The private suite and both tools copies pass all eight methods. Shared tools
checks pass in both copies. Production reruns two installed checks per copy
and reuses six semantic checks after verifying complete input, module and
qualified-artifact fingerprints.

- 886 guest cases cover all 47 reachable target instructions, signed-bit and
  unsigned boundaries, two stack phases, legal volatile register clobbers and
  public position changes. Four retained unsigned-to-float correction words
  are unreachable because the modulo result plus 200 is always 200..255.
  All 51 retail instructions remain present. Guest-only incoming argument-home
  mutations verify pointer, kind and mode reloads; they are excluded from
  portable native C claims.
- Sixty-four cases execute all 13 original caller instructions and confirm
  the copied position, argument widths, fixed mode and discarded result.
- Ninety-six connected cases execute all 25 instructions of the original
  float generator and all 18 of the integer generator, including the shared
  64-bit seed, call order and state updates. The float multiplier at
  `D_8009F740` has bits `0x37800080`. An initial fixture assumption of
  `0x37800000` was rejected against the frozen ELF; `rng_v2.py` and the
  canonical suite use the verified value. The three effect providers remain
  explicit ABI hooks, so complete effect/gameplay execution is not claimed.
- Native32 SDK tests pass 2,016 cases each at `-O0`, `-O2` and `-O3`, with
  trapping UBSan, typed position storage, canaries and precomputed expected
  call order, float bits and memory. Eight compiled incorrect implementations
  fail in native and MIPS tests: missing first effect, swapped effects,
  signed remainder, wrong width, rounded coefficient, wrong integer offset,
  nonzero float parameter and reversed generator order.
- Ninety-two paired fault prefixes include eighteen delay-slot cuts and
  compare complete RAM, registers, trace, PC and delay state. These qualify
  emitted instruction order, not portable C fault behavior.
- Three GNU link layouts pass 72 cases with all five calls rebased. All
  51 body-word and five binding corruptions are rejected. The 229 strict
  whole-image controls cover every target byte, its symbol record, adjacent
  code, helper code, protected data and truncation. The unchanged guard
  manifest is also fingerprinted and corruption-tested.

These are bounded instruction and single-precision checks. They do not claim
arbitrary hardware FCSR or NaN-payload equivalence.

## Production and preservation

The actual five-command owner Make rule runs assembly preprocessing, IDO,
assembly postprocessing, padding and assembly. It reproduces the qualified
object without diagnostics. All 27 neighboring bodies, relocations and pools
are unchanged. Production reproduces the independently predicted image.

The complete image changes by **157 bytes**: 156 target-code bytes and one
symbol-size byte, changing its recorded size from 12 to 204. There are zero
metadata changes and zero comparison exclusions. Every other named definition
and all ELF headers remain unchanged; no output-derived replacement bytes
are used in prediction.

All 6,056 disassembled function addresses and 6,055 other bodies are fixed.
The 189,088 protected Game data bytes across 720 owners, conversion CSV,
guard CSV, compiler profiles and shared headers remain unchanged. The audit
checks 515 focused inputs and 16,561 sealed current inputs. The older tools
mirror retains its 1,868 inherited dirty paths plus the three new modules.
Tools were committed first as `ffcb7cd93bf2f9c6b86ab37687afd7f8e1ee4694`;
the consumer commit contains the C recovery, tools pin and measured docs.
No push or sibling host/Release change is included.

Ignored evidence lives in `conker/build/game-position-effect-burst-match/`.
The post-commit `FINAL_AUDIT.json`, `BANKED_STATUS.json` and banked input seal
record the independent audit. The eleven-file graph refresh preserves old
nodes and valid relationships, retiring only the placeholder's obsolete
`s32` return relationship. Actual C calls, retained assembly providers and
the original assembly caller remain separately identified. Historical global
analytics are not presented as fresh full-corpus extraction.

## Next work

Inspect `func_151D7000` in `generated_203E20.c`, the next unparked 51-word
placeholder in the measured queue. `func_1514E920` remains parked and
uncredited. The 75% matching goal remains active.
