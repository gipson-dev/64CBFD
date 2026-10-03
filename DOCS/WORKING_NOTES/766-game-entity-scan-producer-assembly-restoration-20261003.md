# Entity Scan Producer: Shared-Register Assembly Restoration

Date: 2026-10-03. Baseline: `a38108e`.

## Restoration Boundary

The dependency closure is three exported entries, not all of `D3040.s`:

| Entry/span | VMA | ROM | Bytes |
| --- | --- | --- | ---: |
| Shared returns `func_150A64B8` | 0x150A64B8..0x150A64C8 | 0xD3968..0xD3978 | 16 |
| Producer `func_150A6568` and interior `func_150A66FC` | 0x150A6568..0x150A6760 | 0xD3A18..0xD3C10 | 504 |

These original instructions replace their zero-return placeholders through
three tracked assembly fragments. The ignored original reference is unchanged.
Other placeholders in this slice are outside this closure and remain untouched.
No new word guards, compiler override, or assembler-tool change was added.

The producer initially sets v0 to zero and stores zero through a2. If the
entity count `D_800DBEF0` is zero, it branches to the independent return at
0x150A64C0. Otherwise it saves s0..s7 and fp in f0..f8, consumes four caller
stack arguments, scans 160-byte records, and branches/falls through the interior
loop entry. That entry stores the accumulated secondary count through a2,
restores the saved registers, and returns the primary count in v0.

The loop entry is not an independent ordinary-ABI function. Restoring just
the first named producer span would leave its loop and register cleanup broken.
The earlier shared-return fragment contains only two jr/nop pairs, so restoring
it does not require restoring the unrelated preceding `func_150A6360` body.

## Cross-Fragment Branches

Two local targets become symbolic entry-plus-offset expressions:

- Empty list: `func_150A64B8+0x8` is 0x150A64C0; word stays `0x11C0FFD1`.
- Loop continuation: `func_150A6568+0xC0` is 0x150A6628; word stays `0x158EFFC8`.

All other branch targets are inside their fragments or refer to the exported
interior entry. Standalone linking at retail addresses checks the entire pair
of noncontiguous spans and decodes both cross-entry branch targets.

## Explicit Pointer Contract

`func_150A6500` remains matching C; its third argument is now `s32 *`.
Its producer declaration explicitly takes eight arguments, including the
secondary-count pointer and x/z endpoints with y bounds -10000 and 20000.

`func_15045714` now names/types its fourth argument `s32 *secondaryCount`
and declares the downstream C wrapper's signature. It resets context 2,
converts X/Z to signed halfwords, forwards that pointer, and stores the returned
primary count through its third argument. The existing retained wrapper passes
secondary output at stack slot 0x18 and primary output at 0x1C.

These declaration fixes preserve complete linked bytes:

| Function | Bytes | SHA-256 |
| --- | ---: | --- |
| `func_150A6500` | 56 | `be675159dec10194e305421bb202e9b9518ee517624b117e0f618135235deff0` |
| `func_15045714` | 108 | `84efd8a61af7f41170600c4e2a234589aa9723e0da7953b036a48ac0b383bb43` |

## Verification

All 213 tool tests, project checks, and diff checks pass. The full code build
and progress regeneration pass. Independent ELF extraction
confirms all 520 restored bytes equal retail:

| Span | SHA-256 |
| --- | --- |
| Shared returns, 16 bytes | `f10e5e336e5fb76e6def91eb6fe9dbb0a6adb09eaa07aced495e21d6525df078` |
| Producer/cleanup, 504 bytes | `e4e19a59547819b91826d68e9ea9d3802c274fea1eaa43aa0e4cb50a5e0aa135` |

Five new tests check assembly ownership, contiguous reference spans/hashes,
the initial/final output stores, standalone assembly/link bytes and branch
targets, and actual-source C pointer forwarding. The C fixtures mock only the
producer: they verify context 2 happens first, both counts and surrounding
canaries, signed coordinates, unsigned selector, forwarded bounds, and the
primary store's ordering when the two output pointers alias.

Original odd floating-register assembler warnings may occur under o32 defaults;
byte comparison checks those handwritten encodings unchanged. No guest
execution or natural gameplay qualification is claimed from these tests.

Both context-3 queries, both C forwarding helpers, the 5,712-byte collector
group, and both complete Init sections remain exact. The entity query remains
unchanged at 72 differences and hash
`b574cdd78a8c4921af83d6ca6393ee65f0bf0a3757df0ad2d4565cfadab8ff49`.

## Inventory / Next

Only the 504-byte producer group has its own inventory row. The 16-byte return
is an interior span of the existing coarse `func_150A6360` C row, so this
restoration removes one false C row / 504 classified C bytes, not three rows.
This is original-code restoration, not a new matching C conversion.

Fresh totals: 5,454 C rows / 1,928,216 bytes overall; Game 4,781 C rows /
1,756,780 bytes. Exact numerators stay 3,257 overall and 2,584 Game:
59.72% and 54.05%, zero drift and 2,197 differing Game rows.

The upstream missing-output-write gap from Note 765 is removed. It does not
prove a natural working wrapper/gameplay path. Next recover the retained
32-word `func_15045780` wrapper in C using the now-explicit primary/secondary
buffer contract, and separately improve the non-matching entity query.
The sibling host port and frozen Release artifacts remain untouched.

Follow-up: [Note 767](767-game-entity-height-wrapper-direct-match-20261003.md)
completes the then-pending wrapper conversion with a direct 32-word C match.
Natural gameplay qualification and the entity query's remaining differences
are still separate work.
