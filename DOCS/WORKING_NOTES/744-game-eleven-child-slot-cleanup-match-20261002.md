# Game Eleven-Child Slot Cleanup

Date: 2026-10-02

## Scope and Retail Contract

Recovered `func_151B1918` in `conker/src/game/generated_1DD500.c` from its
zero-return placeholder. Retail occupies `0x151B1918..0x151B19A4`, 35 words /
140 bytes, at ROM `0x1DEDC8..0x1DEE54` in `conker/conker.us.bin`.

The routine has no defined return value. Its inspected callers ignore the
result, so the recovered declaration is `void func_151B1918(u8 *arg0)`.
The two existing wrappers retain their current signatures and gain explicit
pointer casts at this call; no shared declarations or types are changed.

Before processing children, retail clears the word at `0x30` and stores
positive float zero at `0xB8`. It then visits eleven consecutive 12-byte slots
at `0x34..0xB8` (exclusive). Each contains a child pointer and two words.
For each non-null child it calls `func_1516972C(child)` before clearing all
three slot words. Empty slots also have their remaining words cleared.

Traversal is forward, does not deduplicate repeated child pointers, and reads
each subsequent slot when it is reached. Callback mutation of the current
slot is overwritten by the subsequent clear; mutation of a later child can
therefore affect a later dispatch. The loop stops after byte offset `0x84`,
not after reaching a null child.

## Source and Matching Boundary

The local `CleanupSlot1DD500` recovers the guest's pointer-plus-two-word
layout. Separate payload and slot cursors preserve the saved-register
lifetimes seen in retail. A do/while loop retains the byte-count limit.

The existing `-O2 -g3` profile emits the complete 35-word routine with the
retail 0x30-byte frame and saved-register set. Six strict expected-word
guards normalize only:

- Offset `0x28`: the equivalent first-slot address, from `arg0 + 0x34` to
  `payloadCursor + 0x0C`, after the payload cursor was set to `arg0 + 0x28`.
- Offsets `0x44`, `0x50`, `0x54`, `0x58`, `0x5C`: the independent byte-counter
  increment moves after the slot clears, including the corresponding
  branch-likely delay slot on the null-child path.

The increment does not participate in callback arguments or memory accesses.
The same increment executes once on either path. No branch target, callback,
field offset, missing store, or missing loop body is supplied by a guard.
No instruction insertion, omission, or compiler override is added.

## Source-Behavior Verification

`tools/tests/test_game_child_slot_cleanup.py` compiles the actual recovered
slot declaration and function as a freestanding 32-bit host executable. This
keeps real four-byte pointers and the twelve-byte slot stride; it does not
substitute a wider host layout. Seven tests cover:

- Pointer/word size and actual C slot layout.
- All-empty slots with nonzero auxiliary words.
- All eleven children, forward release order, initial resets before callbacks,
  current-slot contents during release, and prior-slot clearing.
- Sparse children at the first, middle, and final slots.
- Repeated child pointers without deduplication.
- Callback mutation of the current slot, next child, and an unrelated byte.
- A second cleanup with no further release calls.

Whole-record byte comparison checks all writes and untouched sentinel bytes.
The fixture deliberately uses `-fno-strict-aliasing` for typed overlays of its
byte-addressed buffer. A first strict-aliasing host trial failed the repeated
cleanup case; the fixture does not claim portable arbitrary-host aliasing
behavior. It requires freestanding 32-bit compilation and execution support,
and explicitly skips if that capability is absent.

All seven cases execute and pass on this machine; all 67 tool tests pass.
`make tools-check` passes. These are source-behavior tests, not target gameplay
qualification or proof that duplicated children are safe for the real release
routine. The mock release records calls and does not free storage.

## Linked Verification

The full `make -C conker NON_MATCHING=1 all match-progress -j4` rebuild passes.
Independent linked-byte comparison confirms all 140 bytes match the pristine
ROM. SHA-256:
`d894a13d21d57a162c1a7b56e1ed6a75355d452c90d3c3c11e86978b7b9b5246`.
The next function `func_151B19A4` remains at `0x151B19A4`.

Both entire Init sections remain byte-exact after the shared-dependency
rebuild: `.init` is 164,048 bytes and `.init_data` is 17,376 bytes. Their
SHA-256 values remain:

- Code: `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`.
- Data: `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.

This is linked code/data evidence, not BSS, gameplay, or a full-ROM match.

## Progress and Resume

Conversion totals remain 5,461 / 6,042 C rows. Exact C now totals
3,247 / 5,461 (59.46%); Game is 2,574 / 4,788 (53.76%). There are 2,214
different C functions and zero address drifts. Init retains 47 assembly rows;
the supported compiler-generated Init queue remains complete.

Next ordinary Game target: `func_151BD21C`, 40 words / 35 real differences.
Keep `func_150A76F0` in the handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue. No sibling host-port
source, build, or runtime artifact was changed.
