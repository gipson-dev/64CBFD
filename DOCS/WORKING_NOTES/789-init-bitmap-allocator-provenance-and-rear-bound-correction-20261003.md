# Init Bitmap Allocator Provenance And Rear Bound Correction

Date: 2026-10-03.

## Result

Following the bitmap caller-domain evidence in
[Note 788](788-init-bitmap-retail-caller-domain-and-edge-contract-20261003.md),
the heap initializer and allocator establish a conditional non-aliasing
contract: successful allocations from a valid initialized heap are above the
bitmap configuration storage. Six production-C host tests protect the
initialization and allocation paths. They also found and drove correction of
a twelve-byte rear-allocation arithmetic error in `func_10003C6C`.

This fixes semantic C, not a new assembly-to-C conversion. Init remains
492 C / 47 assembly rows. The bitmap and MMIO leaves remain assembly.

## Provenance

Startup `func_10001194` calls the RAM-limit selector `func_10003930` and then
heap initializer `func_10003BD0` before setup/bitmap clearing. The selector sets
the upper heap limit to `0x803F5000` or `0x807F5000`. The initializer roots the
physical chain, free-list head/tail, and largest-block pointer at `0x800E9D10`,
with initial size `limit - base - 0x14`.

The bitmap pointer/count/endpoint globals occupy `0x8003BE70..0x8003BE7F`, below
that heap base. In the ordinary setup sequence, the page allocation searches
from the tail with alignment class four; the bitmap allocation searches from
the head with class zero. Retail alignment offsets are 3, 7, 15, 63, 8191;
the corresponding signed masks are -4, -8, -16, -64, -8192.

Allocation splits derive new nodes from a selected valid block, and free-list
links retain those nodes. The free routine merges physical neighbors and
reinserts freed blocks; this preservation argument assumes valid allocated
pointers and uncorrupted links. It is not proof that arbitrary frees, memory
corruption, debug/external writes, or allocation failure cannot occur.

Therefore configuration aliasing is excluded for successful allocations from
the valid heap state covered here, not for every possible leaf invocation.
Keep the pointer snapshots/post-fill count reload characterized in Note 788.
Do not change the bitmap into a defensive early-return routine.

## Semantic Discrepancy And Correction

The existing C defined:

```c
blockEnd = (s32)block + blockSize + 0xC;
```

but the rear branch then computed `(blockEnd - roundedSize + 0xC) & mask`,
adding the header displacement twice. Retail at `0x10003E28` forms
`block + blockSize`; `0x10003E44..0x10003E4C` subtracts the requested size,
adds twelve once, and applies the mask. The corrected C rear expression is:

```c
alignedAddress = ((blockEnd - roundedSize) & savedAlignmentMask);
```

The initial mixed-direction host test failed with exit code one on the old
source because a small rear allocation extended beyond the fixture heap.
The one-line correction passes that test and all other allocation cases.

The prior linked guest image was already retail-exact through the legacy
normalization table, so this was a C-semantic discrepancy, not evidence that
the prior guarded guest image had the same arithmetic bug. The broad guards
in [Note 656](656-init-bidirectional-heap-allocator-match-20261001.md) are not
independent proof that the prior C semantics were correct.

## Guarded Layout Boundary

The corrected IDO body has 257 words rather than 258. The allocator's existing
function-scoped guard table is refreshed against the retained retail-layout
object: 231 stale-checked rows replace the prior 216. The emitted retail slot
is still 258 words / 1,032 bytes, with the layout tool's trailing nop completing
the return delay slot. No insertion/omission directive or compiler profile is
added. All other functions' CSV rows are unchanged, checked using structured
CSV comparison against the pre-edit commit.

This remains extensive legacy layout normalization, not a direct compiler
match or a claim that every replacement is solely independent scheduling.
Host tests exercise the corrected C without those word guards. The full linked
slot and complete Init sections require independent retail comparison before
banking the change. README aggregates must not increase for this correction.

## Host Test Coverage

`tools/tests/test_init_bitmap_allocator_contract.py` extracts the actual C
definitions of RAM-limit selection, heap initialization, `allocate_memory`,
the allocator, and largest-free-block recomputation. It uses the production
`struct54` layout and parses the alignment tables from the assembly data.

The fixture is freestanding 32-bit C with wrapping signed arithmetic and a
two-MiB test heap linked at the actual base `0x800E9D10`. Allocator cases use
that bounded test limit, not the entire production RAM range. Interrupt masking
and the fatal callback are instrumented stubs; these tests do not execute MIPS,
CP0/TLB setup, the actual fatal handler, the free routine, or gameplay.

Six tests cover:

- Both production RAM-limit choices and initial chain/free-list ownership.
- Every count 107..362: tail page allocation with class-four alignment, then
  head bitmap allocation through the real wrapper; payload bounds, separation,
  rounded size, physical/free-list consistency, and interrupt-mask restoration.
- Counts 1..64: the minimum-eight-byte rule and four-byte rounding.
- 128 mixed front/rear allocations, checking bounds and both linked lists after
  each operation. This is the regression that fails on the old source.
- Exhaustion: zero return, conditional fatal-callback behavior, error marker,
  and preserved list/mask state. Success must not be assumed after an allocation.
- All five alignment classes, both directions, and eight request sizes per
  combination, checking alignment, tags, payload size, and heap/list bounds.

All six new tests, all twenty focused Init tests, and the final full suite of
445 tool tests pass. Project tool checks and `git diff --check` pass.

The full `NON_MATCHING=1 all match-progress -j4` rebuild succeeds. The existing
duplicate Makefile recipe and source warnings remain; no stale guard failure
remains. Independent ELF extraction matches:

| Retail interval | Bytes | SHA-256 |
| --- | ---: | --- |
| Allocator `0x10003C6C..0x10004074` | 1,032 | `7b188602de53c31d0fc1e07510cee2edd09e91b94dff1e5a1f295a026afdcaea` |
| Entire `.init` | 164,048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| Entire `.init_data` | 17,376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

Twenty-seven earlier exact Game slots and nine prior non-matching hashes are
unchanged. Independent comparison also preserves the setter, return closure,
producer, and collector spans recorded in the preceding handoffs.

Fresh matcher aggregates remain 3,269 / 5,462 exact C overall, Init 492 / 492,
Game 2,596 / 4,789, and Debugger 181 / 181, all with zero drift. C/assembly
inventory and README aggregate tables are unchanged. No host-port build or
guest/gameplay qualification is performed.

## Next

Use the positive direct-call domain and conditional heap separation as evidence
for a new bitmap source/compiler hypothesis; do not repeat the completed
55-shape/profile matrix. Preserve assembly until the complete nineteen-word
leaf, ownership, and following address are proven. Indirect/external caller
reachability and corrupted heap state remain outside the established contract.
The other Init hardware/SDK/shared-frame boundaries and pending Game dimension
helper remain unchanged. The sibling host port and frozen Release are untouched.
