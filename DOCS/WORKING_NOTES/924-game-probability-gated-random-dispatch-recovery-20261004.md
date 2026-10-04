# Game Probability Gated Random Dispatch Recovery

Date: 2026-10-04. Starting HEAD: `40149ed1`.

## Complete Caller Recovery

Replace `func_150E7290`'s zero-return placeholder in `generated_113D60.c`
with its full void three-argument body: byte index, byte slot and word context.
If the first float RNG sample is not strictly below `D_800A1340`, return with
no integer RNG or submissions. Strict less-than also rejects unordered NaN.

After passing the outer gate, snapshot both words of `D_80088A5C` (retail 4,5)
before the second float sample. Compare that sample strictly below `D_800A1344`.

### Positioned Path

Sample two offsets: float RNG times 300 plus -150, and float RNG times 200
plus -100. Sample another float, then four integer words in order: ID word,
two independent low-bit flags and duration word. Call `func_150E75A0` with:

- Two-float position pointer.
- Scale `(sample * 150 + 200) * D_800A1348`, read after the integer calls.
- Signed-halfword ID `unsignedWord % 201 + 500`.
- Flags 9 plus independently selected bits 2 and 4.
- Duration `unsignedWord % 26 + 100`, then 255, 64, 3, copied pair, mode 2,
  slot and complete context word.

Five float and four integer RNG calls precede this dispatch. Preserve source
temporaries and call order; evaluating multiple RNG calls in argument lists
would leave their ordering unspecified in C.

### Alternate Path And Shared Tail

On false/unordered inner comparison, sample one float and two integer words.
Call `func_150E76D0` with `(sample * 100 + 150) * D_800A134C`, the same unsigned
ID reduction, flags 9 and byte duration reduction, then the shared constants,
pair, mode, slot and context. Three float / two integer calls precede dispatch.

Both paths ignore the helper result and continue: `func_10010F30(0x360,
0x7FFF,0,0,0)`, then `func_15164F0C(1,index,0,slot,context)`.
Construct an eight-byte packet with byte kind 1, halfword at +2 from another
unsigned RNG `%26+25`, byte mode 1 at +5, byte count at +4 from another
unsigned RNG `%6+3`, and signed byte index -1 at +6. Submit through
`func_151D8868(&packet,0,255,0)`. Padding +1/+7 is not initialized or consumed
by the tests; retail leaves it unwritten. Do not silently initialize it.

All remainder operations explicitly cast the RNG word to u32, matching divu.
Global thresholds/scales remain loads at their original times. Retail words
for the four globals are `3B89A027`, `3F400001`, `3DCCCCCD`, `3DCCCCCD`.
No clamping, extra null handling, retry or callback-result gate is introduced.

## Adjacent Helper ABI Boundary

The two adjacent helpers previously had no-argument zero-return placeholders.
Establish call prototypes and matching placeholder signatures so the pointer/
float second argument to `func_150E75A0` uses A1 and the leading float argument
to `func_150E76D0` uses F12, rather than implicit double promotion. Signed
halfword IDs and byte flags/duration are explicit where the caller narrows them;
other stack constants retain word argument slots. Both bodies still return
zero and remain clearly marked unrecovered. This is not a claim of complete
helper type recovery or functional particle/gameplay presentation.

No shared header migration or unrelated caller edits. Both helper entries and
their next entry remain at original addresses after rebuilding.

## Shape And Verification

Production body has 195 words in the original 196-word / 784-byte slot at
`0x150E7290..0x150E75A0`, ROM `0x114740..0x114A50`. Frame remains 0x68.
There are 183 differing aligned positions: copy shape, local/register allocation
and shifted instructions remain unresolved. No target instruction guards.
This is full semantic caller recovery, not a byte-exact match.

New `tools/tests/test_game_random_dispatch.py` has five tests covering outer
equal/above/NaN rejection; inner equal/above/NaN alternate selection; all four
flag combinations with high-bit/negative RNG words; snapshot and callback
mutation timing; all submitted arguments, exact call traces, packet field
layout and a warning-clean independent IDO body/target/footprint check.
The standalone test required its missing u16 typedef and proper jump-region
bits in target decoding; both fixture issues are corrected in the final run.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters tools.tests.test_game_vector_random_parameters -v -f
```

Fifteen tests pass in 2.251 seconds, no skips. Synthetic thresholds/scales and
stubbed submissions establish bounded caller semantics, not retail RNG
distribution, NaN exception/FPCSR behavior, guest execution of all branches,
hardware or visual acceptance. Independent IDO test proves footprint, frame
and call target set, not full instruction equality.

Fresh matcher remains total 3276 / 5463 exact, Game 2603 / 4790, Init 492 / 492,
Debugger 181 / 181, zero drift and 2187 still different. Fresh ELF comparisons
confirm `func_150E6F18`, `func_150E70EC` and `func_150E71E4` remain byte-exact.
README aggregates do not change: this placeholder was already counted as C.
Next connected semantic work is the two typed but still unrecovered helpers.
Init gates unchanged; unrelated actor/timeline edits excluded. No sibling
adoption, host build, Release change or push.
