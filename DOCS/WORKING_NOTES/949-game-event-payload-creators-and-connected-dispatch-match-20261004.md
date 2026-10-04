# Game Event Payload Creators And Connected Dispatch Match

Date: 2026-10-04. Starting HEAD: `1cd128ce`.

## Result

Finish the two preserved Game creator edits after banking the Init assessment
and rejected bitmap trial in Notes 947/948. `func_150E8A80` and
`func_150E90DC` now emit all **39 words / 156 bytes each directly from semantic
C**, with their original 0x48 frames and no instruction guards. The actual
dispatcher and timer caller are qualified with both real creator bodies.

This replaces two zero-return placeholders; it does not transition assembly
owners. Representation counts remain unchanged because the placeholders were
already counted as C. Fresh production matching gains two exact functions:
Game 2,609 / 4,790, total 3,282 / 5,463, zero address drift, 2,181 different.

Detailed changes stay in working docs. README changes are only its two affected
aggregate matching rows. Init production ownership remains unchanged.

## Recovered Bodies

Both creators take no arguments and return void. Each snapshots two float pool
values and positive zero into a twelve-byte `EventPayload113D60`, draws an
unsigned RNG word, calls the established nine-argument allocator interface,
and copies the payload to returned record offset 0x28 only when allocation
succeeds. Null allocation does not call `memcpy` or write an output record.

| Creator | Retail span | Lifetime | Allocator code | Float sources |
| --- | --- | --- | --- | --- |
| `func_150E8A80` | `0x150E8A80..0x150E8B1C` | `(u32)RNG % 41 + 30`, 30..70 | `0x33` | `D_800A137C`, `D_800A1380` |
| `func_150E90DC` | `0x150E90DC..0x150E9178` | `(u32)RNG % 26 + 5`, 5..30 | `0x36` | `D_800A13B0`, `D_800A13B4` |

The complete allocator tuple is:

```text
(s16 lifetime, s8 -1, s8 code, s8 -1, u8 1,
 u8 0, s32 12, u8 255, s32 1)
```

The first two payload fields retain generic offset names; their updater-side
meaning is not invented here. Their exact pool words remain physically owned
by the original data section:

| Address | ROM offset | Word |
| --- | --- | --- |
| `0x800A137C` | `0x245E3C` | `0x3400D959` |
| `0x800A1380` | `0x245E40` | `0x34ABCC77` |
| `0x800A13B0` | `0x245E70` | `0x3456BF95` |
| `0x800A13B4` | `0x245E74` | `0x34210FB0` |

Snapshots precede both the RNG and allocator calls; callback mutation of the
pool cells must not affect the already-captured payload. Each third field is
exact positive zero. No additional table or literal-pool ownership is introduced.

A bounded retail Game-code JAL scan finds one direct call to each creator:
`0x150E89F0` and `0x150E8A08`, both in `func_150E8930`. Its independent list
checks discard incidental callee results. This is a Game direct-call survey,
not proof that no indirect call or other section can reference these addresses.

## Compiler Shape

The initial array form has the correct 39-word length and 0x48 frame but places
the payload at sp+0x3C instead of retail sp+0x38. Changing only array to struct
does not solve this. Declaring the allocator-result pointer before the payload
restores the original local placement under the retail O2/g3 profile.

The final source uses a three-float record and result-first declaration order:
payload words at sp+0x38, +0x3C and +0x40; saved return address at sp+0x2C.
Independent IDO compilation/linking matches every raw word of both complete
retail slots. No scheduling, register or stack-offset patches are needed.
Use `SUBALIGN(4)` in the isolated linker script, especially for the second
creator's non-16-byte-aligned entry at 0x150E90DC.

```text
func_150E8A80 SHA-256
a12ffacda02632f104d3d156c22562edbfd667cf36f55e5d2c6e0196d6e93f0e
func_150E90DC SHA-256
b0eb5726602849246e4eb1a13f545554ec0033da5a591a561c3a39964ced1e0c
```

## Connected Qualification

`tools/tests/test_game_event_payload_creators.py` extracts the production
creators, dispatcher, timer and layouts rather than duplicating their logic.
Seven new tests cover:

- 104 standalone lifetime fixtures: all residues plus signed/unsigned boundary
  words, exact nine allocator arguments and surrounding-byte preservation.
- 82 allocation-failure fixtures: RNG and allocator still run, but no copy
  or record-byte modification occurs.
- 56 snapshot fixtures with RNG/allocator pool mutations, signed zero, finite
  values, quiet NaN and infinities. All three copied float words stay exact.
- 144 actual dispatcher/creator-chain fixtures: initial and packet-published
  list heads, first-allocation head clearing/replacement, second head clearing
  and all four allocation-success/failure combinations.
- 24 actual timer/dispatcher/creator fixtures: strict timer gate, reset before
  dispatch, finite/NaN/infinite inputs, allocation failures and timer byte fence.
- Original slot/frame/call/literal checks and absence of guards for both creators.
- Fresh independent IDO matches of all 39 words per creator.

In the actual connected chain, packet setup consumes two RNG words. Each
invoked creator consumes another word even if allocation fails. The two
subsequent sound submissions therefore bring the total to four words without
creators, five when the first allocator clears the list, or six when both
creators run. The first allocation failure alone must not suppress the second
creator. Trace and argument checks use those actual positions, not the older
parent-only fixture's four-word sequence.

The existing dispatcher test's isolated creator stubs now return void, matching
the recovered interface. Its head-gate matrix varies second-callback clearing
instead of testing incidental integer return values. Historical Note 946's
earlier fixtures remain historical; the connected production-body tests above
supersede its creator-placeholder qualification boundary.

Allocator, pair/event/packet submission, RNG, sound and `memcpy` are fixture
boundaries. This proves the tested creator/caller contracts and exact retail
instruction emission, not complete effect updating or guest gameplay.

## Fresh Production Verification

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_event_payload_creators tools.tests.test_game_event_sound_dispatch tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters -q -f
python3 tools/check_game_data_layout.py conker/build/conker.us.elf
make tools-check
git diff --check
```

Fresh compile, object padding, production relink, progress and matcher succeed.
The existing duplicate-recipe warnings for `generated_12D630` remain unchanged.
**72 combined tests pass in 18.146 seconds, no skips.** The thirteen creator/
dispatcher tests also pass independently in 2.542 seconds.

An independent ELF32 big-endian MIPS parser validates pristine ROM SHA-1
against YAML and compares linked bytes without relocation normalization:

| Verified production region | Bytes / words | Different |
| --- | ---: | ---: |
| Complete `.init` code | 164,048 bytes | 0 |
| Complete `.init_data` | 17,376 bytes | 0 |
| Complete `.game_data`, 720 owners | 189,088 bytes | 0 |
| Curve builder/update | 194 / 212 words | 0 |
| Retained `0x150E7FEC`, `0x150E83AC`, `0x150E8470` owners | 111 / 49 / 237 words | 0 |
| World dispatcher `func_150E81A8` | 129 words | 0 |
| Existing creator `func_150E8854` | 27 words | 0 |
| Timer `func_150E88C0` | 28 words | 0 |
| Dispatcher `func_150E8930` | 84 words | 0 |
| Both new creators | 39 / 39 words | 0 |

The full Game-data SHA-256 remains
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
No complete Game-code byte-exact claim is made; 2,181 represented C functions
still differ. Converted-function and converted-byte aggregates are unchanged.

## Checkpoint And Next Step

- [x] Replace both preserved creator placeholders with semantic, direct-matching C.
- [x] Recover the no-argument void interfaces and qualify the complete payload copies.
- [x] Test actual dispatcher/timer chains with both production creator bodies.
- [x] Rebuild/link and preserve complete Init and Game-data images and exact neighbors.
- [x] Update only achieved aggregate matching rows in README.
- [ ] Inspect `func_150E8B1C` next, then the sibling `func_150E9178` placeholder.
- [ ] Establish their actual updater/callback-table contracts before claiming
  the complete allocator/update pipeline or assigning meanings to payload fields.

The unfinished Game edits preserved in Notes 947/948 are now qualified and
included in this checkpoint. Init's rejected bitmap/MMIO candidates and
connected decoder/glyph gates remain separate. No host-port/Release build,
real-save modification, compressed-ROM promotion, gameplay acceptance or push.
