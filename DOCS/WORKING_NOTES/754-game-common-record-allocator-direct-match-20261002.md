# Game Common Record Allocator: Direct Match

Date: 2026-10-02

## Result

`func_15044964` now replaces its null-return placeholder with the complete
common-header allocator and tail-list registration routine. All 49 words /
196 bytes match retail directly under the existing generated-slice profile.
No word guards, compiler override, or overflow body is required. Its caller
`func_150448D0` remains byte-exact across all 37 words / 148 bytes.

The checkout began clean at `3a8b637`. Source owner:
`conker/src/game/generated_71820.c`; retail reference: `conker/asm/71820.s`.
Routine span: `0x15044964..0x15044A28`.
ROM span: `0x71E14..0x71ED8`.

This closes the placeholder dependency documented in
[Note 753](753-game-position-scale-constructor-direct-match-20261002.md),
but is not guest-runtime or gameplay qualification.

## Recovered Contract

The routine calls the existing Init heap wrapper:

```c
record = (PositionScaleRecord71820 *)allocate_memory(size, 1, 0, 0);
```

The request size is forwarded unchanged; there is no new size validation.
On failure, it returns null without record initialization or list writes.
On success it writes only the common header:

| Offset | Width | Value |
| --- | --- | --- |
| `0x00` | Guest pointer word | Null next link |
| `0x04` | Halfword | `arg2`, low sixteen bits |
| `0x06` | Halfword | `x`, low sixteen bits |
| `0x08` | Halfword | `y`, low sixteen bits |
| `0x0A` | Halfword | `z`, low sixteen bits |
| `0x0C` | Byte | `type`, low eight bits |
| `0x0D` | Byte | `arg4`, low eight bits |
| `0x0E` | Byte | `arg3`, low eight bits |

Byte `0x0F` and all constructor-specific fields from `0x10` onward are
untouched. The leading padding in the existing record declaration is now
represented by the next link, owner field, coordinates, and three header
bytes. The 32-byte guest record size and every existing constructor offset
remain unchanged. Field labels do not establish meanings for individual bits.

After allocation and initialization, the routine loads `D_800CBE00`. For an
empty list it publishes the new head. Otherwise it traverses next links and
updates only the existing tail's link. It returns the original allocated
record pointer. No sorting, extra clearing, duplicate detection, or cycle
handling is added. Valid allocation size and acyclic list ownership remain
caller contracts, as in retail.

The slice uses a locally typed pointer declaration for the list head and the
existing guest `s32` return ABI for `allocate_memory`; no broad shared-header
or heap implementation changes were made. Live inspection confirms the Init
heap wrapper forwards to its recovered implementation, not a zero-return stub.

## Direct-Match Source Shape

The first semantic traversal reused one variable for the loaded head and
current cursor. The compiler coalesced those lifetimes, emitted 48 body words,
and changed the retained result/head registers. A separate `head` variable,
followed by `next = head->next` and `current = head`, restores the full retail
49-word lifetime and branch shape directly. No expected-word normalization is
needed for the resulting function.

## Behavior Evidence

`tools/tests/test_game_common_record_allocator.py` extracts the actual record
declaration, allocator body, and constructor body. Ten freestanding 32-bit
tests preserve the guest link and pointer-return widths. Only the low-level
heap allocation call is mocked for these new tests.

Coverage includes:

- All common-header offsets and guest record size.
- Allocation failure on empty and populated lists, with no extra writes.
- Exact heap arguments, including an unchanged negative request on failure.
- Empty-list publication and original returned identity.
- Single-node and four-node tail insertion, preserving previous payloads.
- Word-to-halfword and word-to-byte narrowing with out-of-range inputs.
- Preservation of byte `0x0F` and every extension byte through `0x1F`.
- A list-head change made by the allocator mock before returning.
- Repeated allocations of distinct records, preserving insertion order.
- The actual constructor calling the actual common allocator on success and
  failure, checking all 32 output bytes and the existing chain.

The prior constructor fixture was updated to extract the recovered tagged
record definition and still passes its seven independent tests. The initial
new fixture accidentally matched the allocator forward declaration rather
than its definition; a definition-only extraction pattern fixed that fixture
compile failure. No production behavior change was made in response to it.

These tests do not execute the real heap, guest gameplay, undersized successful
allocations, cyclic lists, or downstream list callbacks.

## Verification

- Focused generated-slice build passes.
- `make -C conker NON_MATCHING=1 all match-progress -j4` passes.
- All ten new tests and all 116 tests under `tools/tests` pass.
- `make tools-check` passes.
- Independent linked extraction matches all 196 allocator bytes and
  reconfirms all 148 constructor bytes.
- The following routine stays at `0x15044A28`.
- Both entire Init sections remain exact: 164,048 code bytes and 17,376
  initialized-data bytes, with the unchanged hashes in Note 749.

Allocator span SHA-256, identical for linked and retail bytes:

```text
33111489d4c76d8e70aacb48382d5264fa1e4d3132171bb5a96a3c0cba44c43c
```

Fresh exact C counts are Total 3,253 / 5,461 (59.57%) and Game 2,580 /
4,788 (53.88%). Init remains 492 / 492, Debugger 181 / 181. Address drift
is zero and 2,208 Game C rows remain different. C conversion totals are
unchanged because the old placeholder already counted as C. README changes
are limited to the aggregate exact/different table.

No compressed-ROM replacement build or gameplay qualification was performed.
The sibling host port and its frozen Release artifacts remain untouched.

## Resume

Continue this record lifecycle at `func_15044A28`, the 84-word list processor
currently at 81 retail-slot differences. It consumes the newly recovered
header bytes and links; recover callback dispatch and unlink/release behavior
before claiming the complete lifecycle is restored. `func_15044B78` also
remains a downstream placeholder. Other ordinary candidates include
`func_1508B20C` and `func_1509F6E8`.
