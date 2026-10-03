# Game Descriptor Record Constructor

Date: 2026-10-02

## Retail Contract

Recovered `func_151D2F00` in `conker/src/game_1FFF60.c` from its zero-return
placeholder. Retail occupies `0x151D2F00..0x151D2F90`, 36 words / 144 bytes,
at ROM `0x2003B0..0x200440`.

The four arguments are a descriptor pointer, signed payload size, unsigned
byte selector, and signed allocator argument. The routine calls
`func_15167A68(0x3E, arg3, arg1 + 0x30, 1, arg2, 1)`. Allocation failure
returns null without reading the descriptor or touching record storage.

On success it copies exactly sixteen bytes into record offset `0x10`, resets
the halfword at `0x20` and words at `0x24` and `0x28`, and clears bit `0x2`
in copied byte `0x18`. It preserves every other descriptor bit and returns
the allocated record pointer. The existing `struct224` supplies the record
fields; no shared type declaration is changed.

The inspected caller in `conker/asm/1BA1D0.s` checks this returned pointer for
null, then copies an additional payload to offset `0x30`. It supports the
constructor's pointer result and reserved-header size, not a global caller
ABI or gameplay qualification claim.

## Compiler Recovery

Volatile parameter declarations recover the retail four-argument home slots
without changing the containing object's compiler profile. The initial body
fits all 36 words. Moving the flag clear after the bookkeeping resets and
expressing its mask as `~2` recovers the retail `0xFFFD` mask and final store
schedule directly. An explicit size/selector temporary trial enlarges the
frame to `0x30` and changes allocation registers, so it is not retained.

The final semantic body emits the complete 36-word routine under the existing
`-O2 -g3` profile, including its `0x28` frame, both calls, null return path,
descriptor copy, field resets, and pointer return.

Six strict expected-word guards normalize a single closed scheduling rotation
at offsets `0x18..0x2C`: the homed fourth-argument load moves after the other
argument loads and constant setup. These stack locations are distinct and
none is written within the rotated region. All allocator argument values
remain unchanged, with each load and constant occurring once before the call.
No arithmetic, branch, field operation, relocation, or missing logic is
supplied by a guard. No instruction insertion, omission, or compiler override
is added.

## Behavior Verification

`tools/tests/test_game_descriptor_constructor.py` compiles the actual function
and actual `struct224` declaration with mocked allocator/copy functions.
Five tests cover:

- Shared record offsets used by this constructor.
- Allocation failure with a null descriptor, no copy, and no record writes.
- Exact allocator arguments, sixteen-byte copy, returned pointer, field
  resets, preservation of padding, and unchanged descriptor input.
- All 256 flag-byte values, clearing only bit `0x2`.
- Signed allocator arguments, zero/negative payload sizes, and selector
  narrowing to one byte at the call boundary.

Whole-record comparison checks both intended writes and preserved bytes.
This host-native fixture verifies the accessed offsets through `0x28` but
does not claim the shared structure's later pointer fields have the guest
ABI on a 64-bit host. Typed memory overlays use `-fno-strict-aliasing`.
No signed size-overflow, overlapping-copy, invalid-success-descriptor, or
gameplay qualification is claimed.

All five new tests execute and pass. All 80 repository tool tests and
`make tools-check` pass.

## Linked Verification

The full `make -C conker NON_MATCHING=1 all match-progress -j4` rebuild passes.
Independent linked-byte comparison confirms all 144 bytes match the pristine
ROM. SHA-256:
`a0081d25f6c8580ed1e26a0a5b9f97db03d35615219b29aa8286bd6530a8ffe1`.
The following `func_151D2F90` remains at `0x151D2F90`.

Both entire Init sections remain byte-exact after rebuilding: `.init` is
164,048 bytes and `.init_data` is 17,376 bytes. Their SHA-256 values remain:

- Code: `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`.
- Data: `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.

This is linked code/data evidence, not BSS, gameplay, or a full-ROM match.

## Progress and Resume

Conversion totals remain 5,461 / 6,042 C rows. Exact C now totals
3,249 / 5,461 (59.49%); Game is 2,576 / 4,788 (53.80%). There are 2,212
different C functions and zero address drifts. Init retains 47 assembly rows;
the supported compiler-generated Init queue remains complete.

Next ordinary Game target: `func_151DE85C`, 35 words / 35 real differences.
Keep `func_150A76F0` in the handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue. No sibling host-port
source, build, or runtime artifact was changed.
