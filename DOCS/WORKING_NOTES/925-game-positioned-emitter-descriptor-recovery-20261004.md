# Game Positioned Emitter Descriptor Recovery

Date: 2026-10-04. Starting HEAD: `5ae4bdf8`.

## Complete Helper Recovery

Replace `func_150E75A0`'s typed zero-return placeholder in `generated_113D60.c`
with its descriptor construction and `func_1515548C` submission. Retain the
Note 924 argument ABI. Return the submission result: retail preserves V0
through its epilogue, rather than forcing zero.

Snapshot global byte `D_80088A64`, copy the two input float words, and initialize:

| Descriptor offset | Value |
| --- | --- |
| 0x00 / 0x04 | Input position words |
| 0x08 / 0x0C | Scale argument twice |
| 0x10 | Global tag byte |
| 0x12 | Signed-halfword ID |
| 0x14 | Halfword from byte flags OR 0x40 |
| 0x16 / 0x18 | Low signed halfwords of size0 / size1 |
| 0x1A | 4 |
| 0x1B / 0x1C / 0x1D | 255 / 230 / 190 |
| 0x1E | Duration low byte |
| 0x1F / 0x20 / 0x21 / 0x22 | 255 |
| 0x23 | Opacity low byte |
| 0x24 / 0x28 / 0x2C | Words 1 / 0 / 0 |
| 0x30 / 0x34 / 0x38 / 0x3C | Words 7 / 60 / 128 / 32 |
| 0x40 / 0x41 | Bytes 0 / 10 |

Submit `func_1515548C(&descriptor,0,pair,mode,0,slot,context)`. Pair pointer,
mode and complete context are forwarded; there is no new null check or result
gate. Caller currently ignores this result, but the helper's return remains
faithful for other uses.

## Extent And Unwritten Bytes

Retail `func_1515548C` at `0x15155530` prepares a memcpy of 0x58 bytes from
the supplied descriptor to its allocated object's +0x10. This proves the
required source buffer extent beyond the highest field initialized here.
`EmitterDescriptor113D60` is 0x58 bytes, with reserved bytes beginning +0x42.
Byte +0x11 and +0x42..+0x57 stay unwritten, as in retail. The full downstream
copy therefore still transports original indeterminate bytes; do not describe
all descriptor bytes as initialized or fully understood. Tests read only
initialized fields and never assert values for the unwritten bytes.

Two-float `EmitterPosition113D60` aggregate assignment emits the original
style of word-copy instructions without an extra call. The first memcpy
source trial emitted an external copy call and additional scale spilling;
replaced with the aggregate copy. No artificial raw instruction emission.

## Production Shape

The final body has 74 words within the retail 76-word / 304-byte slot
`0x150E75A0..0x150E76D0`, ROM `0x114A50..0x114B80`. Original 0x88 frame,
entry and next-function address remain fixed. There are 69 differing aligned
positions: descriptor stack position, tag lifetime, narrowing loads and
register/scheduling differences remain. No target word guards or compiler
profile changes. This is semantic recovery, not a byte-exact match.

The second helper `func_150E76D0` retains its typed zero-return placeholder.
No complete downstream gameplay or visual behavior is claimed.

## Verification

Six new tests in `tools/tests/test_game_positioned_emitter_descriptor.py`:

- Every initialized field, pair identity, all submission arguments and input
  preservation, including full context and negative mode.
- Four result words times eight narrowing boundaries: 32 cases, including
  byte/halfword truncation, signed boundaries and null pair forwarding.
- Submission callback mutates position/tag sources after observing copies.
- Descriptor extent and all important member offsets.
- Real recovered dispatcher plus real recovered helper execute the positioned
  path, then stub only the downstream submission. Correct OR-0x40 flags,
  descriptor values and complete shared tail/call trace are checked.
- Warning-clean independent IDO build fits the retail slot, retains the frame
  and calls only the expected submission function; no copy-call dependency.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters -v -f
```

Sixteen distinct tests pass in 2.423 seconds, no skips. Host tests establish
bounded initialized-field/ABI behavior with finite inputs and stubbed final
submission, not guest execution, hardware, unknown tail semantics or visual
acceptance. Independent IDO check is footprint/call proof, not full equality.

Fresh matcher remains total 3276 / 5463 exact, Game 2603 / 4790, Init 492 / 492,
Debugger 181 / 181, zero drift and 2187 still different. Placeholder already
counted as C, so no conversion or exact count increase; README unchanged.
Status, index and update log refreshed. Init gates unchanged. No unrelated
edits, sibling adoption, host build, Release change or push.
