# Game Position/Scale Overlap Wrapper Return

Date: 2026-10-02

## Result

`func_15044CE4` now explicitly returns `s32` and forwards
`func_15044B78(arg0)`'s result. Its complete 23-word / 92-byte retail span
continues to emit directly from C without guards or a compiler override.
This closes a source-level callback return contract, not a new matching row:
the earlier `void` source happened to leave the correct guest result in `$v0`.

The checkout began clean at `b2700ab`, eighteen commits ahead of origin.
The only production edit is the wrapper's return type and explicit return.
Six new tests extend the existing overlap fixture. No declaration elsewhere
or new word-patch entry is required.

## Contract Evidence

The existing list pass calls `D_80085E80[type](record)` and uses its signed
result to decide whether to dispatch the secondary callback. The original
three primary callback pointers at `D_80085E80`, independently checked against
ROM `0x22A940`, are:

```text
0: func_15044B78
1: func_15044CE4
2: func_15044D40
```

The wrapper's retail body at `0x15044CE4..0x15044D40` (ROM
`0x72194..0x721F0`) copies three signed position halfwords, loads one signed
scale halfword, divides it by 32 with truncation toward zero, and stores that
value to all three extents. It then calls the overlap test, restores `$ra` and
`$sp`, and returns without overwriting `$v0`.

The recovered C now expresses that same result forwarding rather than relying
on a compiler's incidental preservation of a return register after a `void`
call. The actual overlap predicate returns zero or one; synthetic signed
results in the isolated wrapper fixture test forwarding, not new gameplay
return values.

## Load/Store Timing

- Both input pointers are cached before any record-coordinate stores.
- The three position loads/stores remain sequential, so an overlapping source
  can observe earlier destination writes.
- The scale halfword is read after all coordinate stores. If it aliases a
  coordinate field, the copied coordinate supplies the scale value.
- Negative scale values divide toward zero, unlike the arithmetic half-height
  shift in the overlap routine. In particular, `-33 / 32` is `-1`.
- All three extent stores complete before calling the overlap test.
- No validation, null guard, extra input load, or unrelated field write is added.

## Tests

The existing actual-source extraction fixture now also extracts the wrapper
definition. Six tests cover:

1. Exact result forwarding and exactly one overlap call after all stores.
2. All 65,536 signed-halfword scale values, checked against an independent
   sign/magnitude shift oracle, with input and pointer preservation.
3. Preservation of all unrelated record bytes and distinct input buffers.
4. Sequential overlapping coordinate reads/writes using the same aligned
   record/halfword-array union, without pointer arithmetic beyond a scalar.
5. A scale pointer aliasing a coordinate field, proving its post-copy read.
6. The actual wrapper calling the actual overlap body for an interior point,
   an exact boundary, zero scale, and a negative scale producing a zero bound.

Only external angle helpers are mocked in the integrated test. The isolated
wrapper tests mock the overlap call to inspect dispatch timing and result
forwarding. They use the same freestanding 32-bit fixture and stack alignment
policy documented in
[Note 757](757-game-oriented-record-overlap-match-20261002.md).

## Verification

The full `make -C conker NON_MATCHING=1 all match-progress -j4` build passes.
The focused suite has 22 tests; the complete tool suite has 153 passing tests.
Project checks and `git diff --check` pass.

Independent retail comparisons confirm all six spans remain exact:
constructor 148 bytes, allocator 196 bytes, list processor 336 bytes,
overlap 364 bytes, position/scale wrapper 92 bytes, and angle wrapper 48 bytes.
The following function remains at `0x15044D40`. Position/scale wrapper SHA-256:
`37ca0b9557fb759016a6023c73fee1e8eb5acaf0ff92967480af03dd4bfabaf1`.

Independent extraction confirms the entire Init code (164,048 bytes) and
initialized data (17,376 bytes) remain identical to retail. Matching totals
remain Total 3,255 / 5,461 (59.60%) and Game 2,582 / 4,788 (53.93%), with
zero address drift and 2,206 differing C rows. README aggregates therefore
remain unchanged; detailed updates stay in the working documents.

No compressed-ROM build, guest execution, gameplay qualification, sibling
host-port edit, or frozen Release artifact change was performed.

## Next Target

Continue ordinary semantic recovery at `func_150450CC`, the next untouched
zero-return placeholder after the already recovered/retained callback group.
Its slot is 144 words / 576 bytes at `0x150450CC..0x1504530C`, ROM
`0x7257C..0x727BC`. A fresh linked comparison reports 135 differing word
positions. Recover its real argument types and result-record layout from the
complete assembly/callers before writing the body; matching totals do not
prove any part of that placeholder is semantically complete.
