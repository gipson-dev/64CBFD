# Game Descriptor Height-Result Builder: Direct Match

Date: 2026-10-03. Baseline: `9936cd3`.

## Result

`func_150472C0` converts retained assembly ownership to its complete semantic
void descriptor-to-height-result builder. All 52 words / 208 bytes match retail
directly under the existing compiler profile. No new guards, profiles,
shared-header changes, or assembly substitutions were introduced.

The initial semantic source differed only at two word positions: the compiler
interchanged equivalent flag contributions `1` and `2`. Reordering those
source expressions produces the original register/contribution order. Both
contributions use the same state predicate without intervening stores; no
behavioral difference or word substitution is introduced.

## Contract / Provenance

The inspected original caller `func_150DA67C` at guest call address `0x150DAA74`
passes a stack output record and descriptor pointer, then continues without
using `$v0`. The builder has no meaningful return contract; its recovered
signature is void with result first and descriptor second.

Local `HeightDescriptor71820` records height at `0xC`, eighteen halfword
coordinate bytes at `0x44`, state at `0x59`, value at `0x5C`, and metadata at
`0x60`. Total modeled size is `0x64`. The existing halfword-aligned
`HeightCoordinates71820` and 36-byte result layout are reused.

1. Publish height, copy exactly the eighteen coordinate bytes, and publish
   metadata. Preserve result padding at `0x16` and `0x1E`.
2. Evaluate the three state-equals-one flag contributions and publish flags
   `7` for state `1`, otherwise `0`.
3. Reload the descriptor's state after the flag store, then publish normalized
   result state `1` or `0`. Do not cache it across publication.
4. Read descriptor value after the state store and publish it unchanged.

The metadata/state/value order is observable in the aligned overlap tested
below. The final linked instructions retain the original state reload.

## Exact Measurement

| Item | Measured result |
| --- | --- |
| Guest interval | `0x150472C0..0x15047390` |
| Retail ROM interval | `0x74770..0x74840` |
| Slot / emitted body | 208 bytes / 52 words, no trailing padding |
| Different word positions | 0 |
| Following symbol | `func_15047390 = 0x15047390`, unchanged |
| SHA-256 | `a0ba6a237f37f14247f41247b40d88b7008285c283bf76196f906dd5a0b5eb42` |

Independent ELF-function comparison includes the return delay slot.

## Verification

Eight tests in `tools/tests/test_game_descriptor_height_result_builder.py`
include seven source-extracted freestanding 32-bit behavior/layout cases and
one explicit source-order check. No callees are mocked: the builder is a leaf.
Coverage includes all 256 state values, complete output/source comparison,
all 65,536 signed halfword values across nine vertices, padding/surrounding
bytes, full metadata/value preservation, NaN/infinite/signed-zero height bits,
and an aligned source/output overlap whose vertex copy aliases exactly.
That overlap proves state is read after metadata publication and value after
flag/state publication. The separate source check and exact linked comparison
cover the post-flag state reload. Arbitrary partial-overlap coordinate copies
and misaligned guest records are not qualified.

Commands completed successfully on the finalized source:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest discover -s tools/tests
make tools-check
```

All 362 repository tool tests pass. Eighteen prior exact neighbors remain
retail-identical. The non-matching actor-builder hash from Note 779 and five
terrain/entity query hashes remain unchanged. The 5,712-byte collector,
504-byte producer, and 16-byte return closure remain exact. Both complete
Init sections match retail with the lengths/hashes in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).
No host-port build, compressed-ROM build, guest execution, or gameplay test
was performed.

## Progress / Next

Fresh inventory: total 5,463 / 6,042 C rows (90.42%), 1,931,472 / 2,256,728
C bytes (85.59%); Game 4,790 / 5,321 C rows (90.02%), 1,760,036 / 2,072,880
C bytes (84.91%). Matcher: total 3,268 / 5,463 exact (59.82%); Game
2,595 / 4,790 exact (54.18%). Zero drift; 2,195 different C rows remain.
Remaining assembly is 579 total rows, including 531 Game rows. README contains
only aggregate updates; detailed progress remains in DOCS.

Next investigate empty matrix builder `func_15047390`. A local SDK reference
exists at `tools/ultralib/src/gu/lookat.c` (`guLookAtF`). Compare the complete
retail body, normalization constants/precision, helper calls, and matrix-store
order before using that reference; availability alone is not retail provenance
or a matching claim. Actor/terrain/entity byte matching and runtime
qualification remain open alongside this semantic recovery queue.
