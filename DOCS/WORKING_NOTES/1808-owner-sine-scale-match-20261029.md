# Owner sine scale and forwarded callback result: guarded C match

Verified 2026-10-29. `func_151B6254` replaces its zero-return placeholder in
`conker/src/game/generated_1E34C0.c`. Semantic C emits 47 instructions with
the retail 40-byte frame. Five expected-word/relocation guards restore two
scheduling groups and one nop, reproducing the 48-word body. Its three
alignment words remain separate and unchanged: the full slot is 51 words.

The adopted live ELF recount is **3,886 / 5,506 (70.58%)** byte-exact C
functions: Game **3,213 / 4,833 (66.48%)**, Init 492/492 and Debugger 181/181.
There is zero address drift and 1,620 C functions still differ. Reaching 75%
requires 4,130 exact functions, leaving **244**. Conversion inventory is unchanged.

## Recovered behavior

`s32 func_151B6254(u8 *owner)` advances the floating phase at `owner + 0x170`
by `D_800AA458 * D_800BE9A4`. While that phase is greater than `D_800AA454`,
it subtracts the period. Equality does not wrap, and negative phases remain
negative. It calls `sinf`, then reloads the base at `owner + 0x174` and the
gain `D_800AA45C`. The output is `base + sine * (gain * base)`, rounded at
each original single-precision operation. It stores at offsets `0x1C` and
`0x18`, in that order, and forwards `func_15133894(owner)`'s return value.

The period, rate and gain have retail bits `0x40C90FDB`, `0x3F0E5605` and
`0x3D79DB24`, respectively: approximately 2 pi, 0.556 and 0.061. The exact
operand ordering and post-call reloads matter. The recovered return is not
a constant success value: the helper can return a signed callback byte.

The original caller is slot six of the 100-byte `D_800898B0` table. Its
pointer is at ROM `0x22E388`. The qualified 13-word window in `func_151321D0`
reads the selector at owner offset `0x71`, skips zero, and dispatches through
the table. A nonzero callback result preserves its incoming gate; zero sets
the gate to one. The parent remains a C placeholder; no current C caller
or whole-parent/gameplay recovery is claimed.

| Evidence | Value |
| --- | --- |
| Body virtual range | `0x151B6254..0x151B6314` |
| Full slot virtual range | `0x151B6254..0x151B6320` |
| Body / slot ROM ranges | `0x1E3704..0x1E37C4` / `0x1E3704..0x1E37D0` |
| Owner | Two compact functions; neighbor `func_151B6010` unchanged |
| Compiler profile | Existing IDO `-O2 -g3` |
| External bindings | Eight HI16/LO16 bindings and two calls |
| Raw body SHA-256 | `df23a6e45a5207128491b62de3bb6f3140502ff2ce9036d870a63e85733b9a0c` |
| Normalized object body SHA-256 | `dd4115ac4a19a518d5d0d8ea0e395c9be360b6f157846bff86e2234c5682d64f` |
| Retail slot SHA-256 | `48558f99268979b2efcbee737b85d15931f88855b8c27ef1051249b08b56ceee` |
| Adopted ELF SHA-256 | `3af9d58526f734f4cd164f77f683c148f21367d4bb7f5f3f6c0a589f6890c7d3` |

Guards at raw bytes 4, 8 and 12 rotate the return-address save and the
period's HI16/LO16 load pair. Guards at raw bytes 164 and 168 move the final
output store ahead of the helper call and insert its retail delay-slot nop.
The period bindings move from 8/12 to 4/8, and the last call moves from 164
to 168. Internal branch displacements remain unchanged. No semantic operation
is added. The guard CSV retains its complete inherited prefix and appends
five rows; headers and compiler profiles are unchanged.

## Qualification

The private suite and both tools copies pass all eight methods, and both
shared tools checks pass. Production reruns two installed checks per copy
and reuses six semantic checks after complete fingerprint verification.

- 1,584 guest cases cover all 48 target words, phase boundaries, multiple
  wraps, post-call base/gain reloads, two stack phases and forwarded results.
  Original and normalized private states agree; raw C preserves public
  memory, call arguments, observations and return value.
- Thirty-two cases execute all 13 words of the original caller window.
  A compiled constant-return control fails its gate behavior when the helper
  returns zero, showing why the result must be forwarded.
- 432 connected cases execute the original sine and both downstream helper
  bodies. They cover 97 of sine's 104 words, all 80 words of
  `func_15133894`, and all 53 words of `func_151337C0`. Verified return
  values include 0, 1, 7 and -128. The geometry routine and selected event
  callback remain explicit ABI hooks; their full implementations are outside
  this qualification. The current exact-C sine and retained assembly helpers
  are unchanged and receive no additional matching credit.
- Native32 SDK tests pass 2,160 cases per `-O0`, `-O2` and `-O3` profile,
  with trapping UBSan, typed owner fields, full-object canaries and precomputed
  expected bits. Eight compiled incorrect implementations fail observable
  checks in both native and MIPS testing.
- Ninety-four paired access-fault prefixes include six delay-slot cuts and
  compare RAM, registers, trace, PC and delay state. Guest-only incoming-home
  and saved-pointer mutations are excluded from native C claims.
- Three GNU link layouts pass 48 cases. All 47 word and ten binding
  corruptions are rejected, along with ten actual-padder guard corruptions
  and 128 whole-image controls covering all four exchanged symbol records,
  both name blocks, target padding, neighboring code and protected inputs.

These are bounded single-precision and instruction-order checks. NaN
comparison paths are exercised without claiming hardware NaN-payload/FCSR
equivalence. Infinite or sufficiently large positive phases are not claimed
to terminate; the source preserves the retail repeated-subtraction loop.

## Production and preservation

The actual three-command owner Make rule reproduces the selected/padded
object without compiler diagnostics. The neighbor's body, bindings and pools
are unchanged. Production reproduces the qualified private image exactly.

Independent whole-image prediction accounts for **200 changed bytes**:
150 target-code bytes, one symbol-size byte and 49 metadata bytes. Metadata
changes are two closed permutations: `.L15032CC8_game_data` with `D_8009E774`,
and `D_800AA45C` with `D_800AA80C`. The first pair has different name lengths,
so the second name offset is rebuilt explicitly. Named definitions,
addresses, sizes, types and sections are otherwise unchanged. There are no
comparison exclusions or output-derived replacement bytes.

All 6,056 disassembled function addresses and 6,055 other bodies are fixed.
The 189,088 protected Game data bytes across 720 owners and the conversion
CSV are unchanged. 490 focused inputs and 16,554 sealed current inputs are
verified. The older tools mirror retains its 1,865 inherited dirty paths plus
the three new modules. Tools are committed first in
`f61c6c9fc19ef9173b4fb03a728a476f3bbb463e`; the consumer commit contains the
C recovery, guards, tools pin and measured documentation. No push or sibling
host/Release change is included.

Ignored receipts are in `conker/build/game-owner-sine-scale-match/`.
The post-commit `FINAL_AUDIT.json`, `BANKED_STATUS.json` and banked seal record
the independent audit. Graph refresh covers eleven changed files, retaining
old nodes and valid relationships. Current C calls, retained assembly helper
definitions and the original indirect caller are represented separately.
Historical global analytics are not presented as fresh full-corpus results.

## Next work

Inspect `func_151D5648` in `generated_200930.c`, the next unparked 51-word
placeholder in the measured queue. `func_1514E920` remains parked and
uncredited. The 75% matching goal remains active.
