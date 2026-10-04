# Game Object Position Sound Adapter And Init Return Contract

Date: 2026-10-04. Starting HEAD: `15f5a059`.

## Recovery

Replace `func_1509F6E8`'s zero-return placeholder in `generated_CBDB0.c` with
the retail object-position sound adapter. Resolve the object through
`func_1505EEF4(arg1)`. On null, return zero without coordinate reads or sound
submission. Otherwise truncate float coordinates at 0x14/0x18/0x1C to signed
32-bit temporaries and submit:

```c
func_10010F88(arg0, arg2, 0, 0, 0, x, y, z, arg3, arg4)
```

The complete 37-word / 148-byte body at `0x1509F6E8..0x1509F77C` emits directly
from C without guards. Its frame is 0x30; original null branch, incoming spills,
grouped coordinate loads, truncation registers, ten-argument stack layout,
call delay slot and epilogue all match. The next already recovered adapter
`func_1509F77C` remains at its original address and is not edited.

## Return Contract Correction

The adapter forwards the sound call's result. The shared `func_10010F88`
declaration and Init definition incorrectly described that wrapper as void.
Retail calls `func_10010E78` and preserves its returned handle in `$v0` through
the epilogue. Correct `functions.h` and `init_EB00.c` to `u16`, explicitly
returning `func_10010E78(...)`. Its existing narrow argument types are unchanged.

The Init wrapper remains byte-exact across all 29 words / 116 bytes at
`0x10010F88..0x10010FFC`, directly from C with no target guards. Shared-header
dependents were rebuilt successfully; the existing call sites which ignore
the return do not acquire new behavior. No unrelated declaration cleanup.

The Game slice retains its existing non-prototyped call convention, which emits
full 32-bit coordinate/trailing stack words before the callee's signed-halfword
loads narrow them. The Game fixture records this ABI boundary with wide-word
stubs; a separate Init fixture tests the recovered narrow forwarding and u16
return contract. This is not a global migration of legacy implicit declarations
or a claim that all cross-module prototypes are now recovered.

## Fresh Verification

```sh
make -C conker build/src/game/generated_CBDB0.c.o build/src/init_EB00.c.o -j2
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_object_position_sound_adapter tools.tests.test_game_status_record_reset tools.tests.test_game_menu_state_reset -v -f
```

Both objects and the dependent production ELF/progress refresh succeed.
Thirteen tests pass in 0.977 seconds, no skips. Four new tests cover:

- Null lookup: exactly one lookup, zero return, no sound submission/dereference.
- Four coordinate triples spanning fractional signs, signed-halfword boundaries,
  and representable signed-32 endpoints; full forwarded words and fixed zeros.
- Five handle results 0/1/0x7FFF/0x8000/0xFFFF, and the Init wrapper's eleven
  forwarded arguments including its prepended zero and signed/unsigned fields.
- Independent warning-clean IDO builds and links for both complete retail slots,
  without project padding or instruction normalization.

Host cases are finite, representable float inputs. NaNs, infinities, invalid
float-to-int conversions, FPCSR exception state, MIPS hardware and gameplay are
not qualified by those fixtures. Direct guest byte equality preserves retail's
`trunc.w.s` instructions; no substitute conversion routine is introduced.

Independent extraction of the fresh production ELF confirms target bytes,
addresses and absence of target CSV guards:

| Function | Words | SHA-256 |
| --- | ---: | --- |
| `func_1509F6E8` | 37 | `ea19233d137f7a513761d3c6abb556c6ce86ec98cb772b3ac7a233fa6e814f97` |
| `func_10010F88` | 29 | `c0cf41fd12c1495f309124e7177102e56961d6df8ec56238583c384998564db9` |

Whole Init sections also equal the pristine image after the header rebuild:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| `.init` | 164048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| `.init_data` | 17376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

Existing legacy pointer/integer compiler warnings and the duplicate recipe
warning remain. The new isolated fixtures compile warning-clean. Project tool
and whitespace checks pass. No full repository test suite or ROM build claimed.

## Fresh Aggregate Snapshot

Conversion counts remain 5463/6042 total, 4790/5321 Game, 492/539 Init and
181/182 Debugger: this replaces an already C-counted placeholder.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3273 / 5463 (59.91%) | 0 | 2190 |
| Game | 2600 / 4790 (54.28%) | 0 | 2190 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

README changes are limited to the two aggregate rows. The fresh ELF represents
the current worktree, including preexisting uncommitted actor/timeline source;
those changes are preserved, not reviewed or included in this recovery commit.
No sibling-port artifact, Release change or push. The qualified experimental
Init decoder and its 528-byte fitting/reservation gates remain unchanged.
