# Game Actor Height-Result Builder: Semantic Recovery

Date: 2026-10-03. Baseline: `af8832a`.

## Result

`func_1504715C` replaces its zero-return placeholder with the recovered void
actor-to-height-result builder. It is not byte-exact: 85 emitted body words
plus four padding nops fill the original 89-word / 356-byte slot, with 76
differing positions. No new guards, profiles, shared-header changes, or assembly
substitutions were introduced. Existing conversion/matcher totals are unchanged;
the placeholder was already counted as non-matching C.

## Signature / Layout Evidence

The live callers in `game_A28B0.c`, `game_981E0.c`, `generated_1C1150.c`, and
`generated_1F4650.c` use the routine as an output builder without consuming a
return. Two existing declarations explicitly say `void`. The zero-index
assembly path does not define a normalized return. The recovered signature is
therefore void, with result first and actor second, not the placeholder's
invented no-argument `s32` function.

Local `HeightActor71820` records only the recovered fields: X/Z at `0x14`/
`0x1C`, flags at `0xF8`, height at `0x180`, metadata at `0x184`, nine stored
halfword coordinates at `0x18C`, and the one-based entity index at `0x1A0`.
`HeightCoordinates71820` is 18 bytes with halfword alignment, preserving the
stored-copy type behind retail's `lwl/lwr` and `swl/swr` sequence. Result layout
and the existing 160-byte entity stride are unchanged.

## Recovered Contract

1. Publish actor height first, then read actor flags. Bit `0x00200000` selects
   synthesized vertices; every other flag bit alone retains stored vertices.
2. For synthesis, truncate X, height, and Z toward zero before writes. Emit
   `(X+1000,Y,Z+1000)`, `(X-1000,Y,Z)`, `(X+1000,Y,Z-1000)` as nine signed
   halfwords. Otherwise copy exactly the eighteen stored coordinate bytes.
3. Reload metadata after vertex writes, cache it before publishing result
   flags `6`, and then publish the metadata. Read the entity index afterward.
   This ordering matters for the tested overlapping source/output layouts.
4. For nonzero index, publish state `2` and the entity pointer using index minus
   one and stride `0xA0`, then call `func_15145C90(index-1)`. Normalize raw
   integer truth and merge it into result flags after the helper returns.
   The post-call flag load observes helper mutation.
5. For zero index, publish state `1`, zero value, and flags with bit 1 set.
   Preserve result padding at `0x16` and `0x1E` in either branch.

The helper's definition returns normalized 0/1 as `u8`; this slice retains the
existing implicit-call convention rather than imposing a slice-wide prototype
that changes retail's raw-zero comparison. Tests use a raw-integer mock to
verify the caller's emitted truth contract, not to claim the real helper emits
arbitrary wide values. API declaration cleanup remains separate work.

## Linked Measurement

| Item | Measured result |
| --- | --- |
| Guest interval | `0x1504715C..0x150472C0` |
| Retail ROM interval | `0x7460C..0x74770` |
| Slot | 356 bytes / 89 words |
| Emitted body / padding | 85 words / 4 nops |
| Different word positions | 76 |
| Following symbol | `func_150472C0 = 0x150472C0`, unchanged |
| SHA-256 of recovered slot | `71bf7ba77a2560447da2aa7680f075c3e739881d66c756d36655f775ae5d24af` |

The earlier uncached metadata form had 84 body words plus five nops and 72
differences, but did not preserve metadata-before-flags ordering under aliasing.
It is not the accepted source. No broad normalization is justified by either
word count. Byte matching remains open.

## Verification

Twelve source-extracted freestanding 32-bit tests in
`tools/tests/test_game_actor_height_result_builder.py` check all field offsets,
coordinate alignment/size, stored/synthetic vertices, truncation/order, signed
halfword wrapping, each of the 32 actor flag bits, padding and surrounding
bytes, every entity index 1..65,535, pointer/state publication before helper
entry, raw truth normalization, all 256 post-helper flag mutations, and three
selected source/output aliases covering height-before-flags and metadata
after-vertices/before-flags ordering. Only `func_15145C90` is mocked.
Partial-overlap stored-structure copies, invalid/nonfinite float-to-integer
inputs, and guest execution are not qualified by these host tests.

Commands completed successfully on the finalized source:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest tools.tests.test_game_actor_height_result_builder
python3 -m unittest discover -s tools/tests
make tools-check
```

All 354 repository tool tests pass. Eighteen prior exact neighbors remain
retail-identical. Five non-matching terrain/entity query hashes are unchanged.
The 5,712-byte collector, 504-byte producer, and 16-byte return closure remain
exact. Both complete Init sections match retail with the lengths/hashes in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).
No host-port build, compressed-ROM build, guest execution, or gameplay test
was performed.

## Progress / Next

Inventory remains total 5,462 / 6,042 C rows (90.40%), 1,931,264 / 2,256,728
C bytes (85.58%); Game 4,789 / 5,321 C rows (90.00%), 1,759,828 / 2,072,880
C bytes (84.90%). Matcher remains total 3,267 / 5,462 exact (59.81%) and Game
2,594 / 4,789 exact (54.17%). Zero drift; 2,195 different C rows remain.
README and aggregate tables stay unchanged; detailed updates remain in DOCS.

Next recover retained `func_150472C0`, the 52-word descriptor-to-height-result
builder. Its inspected body copies height from offset `0xC`, stored coordinates
from `0x44`, and metadata from `0x60`. It derives flags/state from byte `0x59`
and copies value from `0x5C`, reloading state input after output flags are
published. Recover its caller/source layout and preserve that reload before
conversion. Matching this actor builder and the terrain/entity queries remains
open alongside runtime qualification.
