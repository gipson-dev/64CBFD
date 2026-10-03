# Game Record List Processor: Direct Match

Date: 2026-10-02

## Result

`func_15044A28` replaces its zero-return placeholder with the complete
callback, delay, lifetime, unlink, and release-marking list pass. All 84 words /
336 bytes emit directly from C under the existing `-O2 -g3` profile. No word
guards, compiler override, or overflow body is required. Its constructor and
common allocator remain byte-exact across 37 and 49 words respectively.

The checkout began clean at `613e0e4`. Source owner:
`conker/src/game/generated_71820.c`; retail reference: `conker/asm/71820.s`.
Function span: `0x15044A28..0x15044B78`.
ROM span: `0x71ED8..0x72028`.

## Recovered Pass

For each record, retail loads the delay byte at `0x0E`, the unsigned callback
type at `0x0C`, and the traversal next pointer before any callback.

If delay is zero, call `D_80085E80[type](record)`. For any nonzero return,
reload the unsigned selector at `0x0D` and call `D_80085E8C[selector]()`.
The second call has no explicitly prepared arguments. Do not invent a record
argument from incidental caller-saved register contents.

If delay is nonzero, subtract the word at `D_800BE9E4`, clamp a negative
signed result to zero, and store the low byte. Reaching zero does not dispatch
the callback during that same pass; callback eligibility is based on the
initial delay load.

After callbacks or delay adjustment, reload the signed halfword at `0x04`.
This consumer establishes it as `lifetime`, correcting the provisional
`owner` field name from the allocator recovery. The guest layout is unchanged.
Lifetime `-1` is indefinite. Otherwise subtract the current tick word:

- If the signed result is positive, store its low halfword and retain the node.
- If nonpositive, unlink the record and call `func_100043B4((s32 *)record, 2)`.
  Do not store the expired arithmetic result into the record's lifetime field.

The existing Init `func_100043B4` updates heap metadata before the allocation,
with interrupt-mask protection. This is mode-2 release marking, **not immediate
memory deallocation**. Its implementation was inspected, not changed.

## Mutation and Arithmetic Contracts

Traversal uses the next pointer cached before callbacks. Unlinking instead
reloads `record->next` after callbacks. The retained predecessor is updated
only for surviving nodes, preserving consecutive deletions and head removal.
The unlink happens before release marking. This preserves retail behavior
even when a callback changes the current link; it does not make arbitrary
callback list mutation a generally safe ownership pattern.

The selector and lifetime are reloaded after callbacks. The tick value is
loaded independently for delay and lifetime arithmetic, and again on later
records, so callback and release-marker side effects remain observable.

Unsigned subtraction followed by conversion to guest `s32` models retail's
32-bit `subu` wrap before signed comparisons. This avoids C signed-overflow
undefined behavior. Positive lifetime results and nonnegative delay results
are narrowed by their stores; no upper saturation is added. Tests establish
these conversions on the supported 32-bit fixture/compiler, not every host ABI.

## Direct-Match Source Shape

The first semantic trial was 85 words and was correctly rejected by the
generated-slice span guard. Caching the type before the delay branch restores
retail's unconditional unsigned type load and branch-delay shift, removing
the extra scheduling word. Reusing the arithmetic `value` for the lifetime
load instead of a separate temporary restores its `$v0` register lifetime.
The resulting complete 84-word function matches without normalization.

## Behavior Tests

`tools/tests/test_game_record_list_processor.py` extracts the actual record
declaration and processor body into a freestanding 32-bit fixture. Fifteen
tests cover:

- Empty lists and ordered callbacks for indefinite lifetimes.
- Conditional second callback, including negative nonzero primary results.
- Delay clamping and waiting until the next pass after reaching zero.
- Positive lifetime decrement without removal.
- Head, middle, tail, and consecutive removals, preserving retained payloads.
- Head/link updates visible before release marking.
- Cached traversal despite a callback changing the current next link.
- Unsigned type/selector values and post-callback selector reload.
- Primary and second callback changes to lifetime.
- Tick changes from callbacks and release markers.
- Negative tick narrowing and full-word wrap at the signed boundary.

The fixture compares all bytes of four records, including padding and extension
fields, and checks callback/release order. Callback tables are deliberately
populated for all byte values to test unsigned decoding; this does not qualify
out-of-range selectors in the actual retail table. Real callback bodies, heap
marking side effects, cyclic lists, and gameplay are not executed by the fixture.

The existing common-allocator layout test was updated for the lifetime field
name and still passes. Constructor and allocator tests remain passing.

## Verification

- Focused generated-slice build passes after source-shape correction.
- `make -C conker NON_MATCHING=1 all match-progress -j4` passes.
- All fifteen new tests and all 131 tests under `tools/tests` pass.
- `make tools-check` passes.
- Independent linked extraction matches all 336 retail processor bytes.
- Constructor and allocator spans independently remain exact at 148 and
  196 bytes, with their unchanged hashes from Notes 753 and 754.
- The following routine stays at `0x15044B78`.
- Both entire Init sections remain exact: 164,048 code bytes and 17,376
  initialized-data bytes, with the unchanged hashes in Note 749.

Processor SHA-256, identical for retail and linked spans:

```text
74ca58d540a400c11803f77795123df91b094dd0cb5e8820f559569c454178d4
```

Fresh exact C counts are Total 3,254 / 5,461 (59.59%) and Game 2,581 /
4,788 (53.91%). Init remains 492 / 492 and Debugger 181 / 181.
Address drift is zero; 2,207 Game C rows remain different. Conversion totals
are unchanged because the placeholder already counted as C. README changes
are limited to aggregate exact/different counts.

No compressed-ROM replacement build or gameplay qualification was performed.
The sibling host port and frozen Release artifacts remain untouched.

## Resume

Recover downstream `func_15044B78` next: 91 retail words, currently 82
retail-slot differences. Its body remains a zero-return placeholder despite
the allocator, constructor, and list pass now matching. Inspect its player/
record data contract and return behavior before changing dependent callback
signatures or claiming a fully restored visible record lifecycle.
