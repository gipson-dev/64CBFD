# Game Event, Packet And Sound Dispatch: Direct Match

Date: 2026-10-04. Starting HEAD: `09e33c73`, clean tracked checkout.

## Production Recovery

Replace `func_150E8930`'s zero-return placeholder in
`conker/src/game/generated_113D60.c` with the complete semantic dispatcher.
All **84 words / 336 bytes** emit directly from C under the existing O2/g3
profile, with the original **0x38-byte frame**, no new instruction guards,
no profile change and no data-owner changes.

The recovered sequence is:

1. Copy the first two words of `D_80088A80` into a local `EventPair113D60`,
   then call `func_15169260(&pair, 2, 0, 0x1B)`. Retail words are 25 and 72;
   the following two zero words belong to the original global, not this copy.
2. Read unsigned byte `D_800BE9EB` after that call and submit
   `func_15164F0C(0, index, 0, 255, 1)`.
3. Build the existing eight-byte `RandomPacket113D60`: kind 1, unsigned RNG
   remainder modulo 21 plus 20 for duration, mode 1, a second unsigned RNG
   remainder modulo 6 plus 3 for count, index -1. Submit it with arguments
   `(0, 255, 1)`. Padding bytes 1 and 7 remain unwritten.
4. If `D_800DCDC4` is nonzero, call `func_150E8A80`. Independently check the
   global again before calling `func_150E90DC`; a callback can clear or replace
   the head. Do not cache the initial value or combine these into one gate.
5. Call integer RNG independently for each sound. Signed offset is
   `0x200 - (rng & 0x400)`, giving +512 or -512. Play sound `0x4C8` at volume
   `0x7FFF`, then `0x4CD` at `0x5DC0`; both use pan `0x40` and final argument 0.

The globals are declarations only. Their original storage and addresses are
unchanged. The two list-triggered routines remain zero-return placeholders;
this dispatcher recovery does **not** recover their payload creators or prove
the complete runtime effect pipeline.

## No-Argument Interface And Timer Caller

Retail never reads incoming argument registers before overwriting them. The
recovered interface is `void func_150E8930(void)`. The first trial retained an
unused pointer argument, causing IDO/g3 to spill `a0` into the caller argument
slot: 85 words against the 84-word budget. The production padding gate rejected
that body. No guard or truncation was used to make it fit.

Removing the unsupported parameter removes the spill and restores the complete
retail body. Update `func_150E88C0`'s call to the no-argument form; its timer
subtraction, strict-negative gate and pre-dispatch reset remain unchanged.
All **28 timer-caller words** still match retail directly, independently and
in the final production ELF. The assembly dispatcher caller at `0x1509D6E8`
also discards the callee result by reloading `v0` from its own stack afterward.

## Focused Tests

New `tools/tests/test_game_event_sound_dispatch.py` extracts actual production
layouts and the dispatcher/timer bodies for six tests:

- Thirteen unsigned boundary words for each packet draw and four independent
  sound-bit combinations: 676 dispatch cases. Check exact packet fields,
  volumes, sound IDs, signed offsets, four parent RNG calls and call order.
- Four list-state scenarios under two incidental callback result patterns:
  no head, unchanged head, first callback clears head, first callback replaces
  head. The second callback can also clear it without suppressing the sounds.
- Four pair/global mutation cases: the event helper sees the local snapshot,
  its writes do not alias the global pair, the later byte load sees callback
  changes, and a packet callback can publish or clear the list before its gate.
- Actual timer-to-dispatcher chain: positive, zero-boundary, negative, NaN and
  both infinity cases. Check strict gate, reset before dispatch and preservation
  of every record byte outside the four-byte timer field.
- Pristine retail call sequence, global pair words, unwritten padding and
  caller's discarded return.
- Independent IDO compile/link of both routines: all 84 and 28 words equal
  pristine retail directly, with no normalization.

The follow-up stubs' incidental zero/-1 results exercise ignored return values;
they do not establish return semantics for the unresolved production helpers.
The fixture's four RNG draws are the parent routine's draws under those stubs,
not a claim about the full pipeline once real helpers consume RNG themselves.
The callback mutations are adversarial interface cases, not claims that the
actual event/packet helpers necessarily perform those particular mutations.

Independent and production SHA-256 receipts:

```text
func_150E8930  194cad512419bf6f1851fc6905b56340e1812ab968ae5ac5955ea44d5c37d540
func_150E88C0  94893d3fec01a0867260d976a9d1cdfd0153235d3a20289e838f3e3cffc7c4e5
```

## Fresh Production Qualification

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 tools/check_game_data_layout.py conker/build/conker.us.elf
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_event_sound_dispatch tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters -q -f
```

Fresh production relink succeeds. **65 tests pass in 12.800 seconds, no skips**;
the six new tests also pass independently in 0.732 seconds. Existing duplicate
Makefile recipe warnings for `generated_12D630` remain unchanged.
`make tools-check` and `git diff --check` also pass.

Independent ELF32 section/slot parsing validates the ROM SHA-1 against YAML
and checks raw bytes without instruction or relocation normalization:

| Region | Retail-exact extent |
| --- | ---: |
| Complete Init code | 164,048 bytes |
| Complete Init initialized data | 17,376 bytes |
| Complete Game data | 189,088 bytes / 720 owners |
| Curve builder `func_150E7994` | 194 words |
| Curve update `func_150E7C9C` | 212 words |
| World-emitter dispatch `func_150E81A8` | 129 words |
| Existing payload creator `func_150E8854` | 27 words |
| Timer caller `func_150E88C0` | 28 words |
| New dispatcher `func_150E8930` | 84 words |
| Retained `func_150E7FEC` / `func_150E83AC` / `func_150E8470` | 111 / 49 / 237 words |

Fresh matcher: **Game 2,607 / 4,790 exact (54.43%)**, total **3,280 / 5,463
exact (60.04%)**, zero drift and 2,183 still different. Init remains 492 / 492
and Debugger 181 / 181 exact. Representation counts are unchanged because
the old placeholder already counted as C. README changes only the achieved
matching rows; details stay in working documentation.

## Handoff

- [x] Recover event/pair/packet/list/sound ordering and unsigned/signed widths.
- [x] Match the complete dispatcher and preserve the timer caller directly.
- [x] Qualify current production link, complete data and neighboring owners.
- [x] Update working docs and README aggregate matching rows.
- [ ] Recover `func_150E8A80`, the first list-triggered twelve-byte payload creator.
- [ ] Then recover `func_150E90DC` and qualify the actual connected creator chain.

These are native bounded interface tests and static guest byte/data checks,
not gameplay acceptance or a complete runtime helper-pipeline test. No Init
conversion, sibling build, Release change, real save modification, compressed
ROM promotion or push is claimed.
