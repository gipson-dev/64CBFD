# Camera reset direct byte match

Date: 2026-11-11. `func_15127EB8` replaces an empty placeholder in
`conker/src/game_14FF90.c`; original assembly remains in
`conker/asm/nonmatchings/game_14FF90/func_15127EB8.s`. Its 77-word body spans
VA `0x15127EB8..0x15127FEC` and ROM `0x155368..0x15549C`, with a 0x20-byte
frame. The C compiler emits all original words directly, with no new guards.
The obsolete commented non-matching draft was removed.

The routine resets camera-related state, clears four position values, updates
per-slot view and actor state, and invokes four existing helpers. If the actor's
selector byte is nonzero, it chooses `D_800CC2D0[selector - 1]`; the old
commented draft omitted the one-based adjustment. The active slot and actor
pointers are reloaded after helper calls as in retail. Names describe the
observed operations; the full meanings of the helper calls remain separate.

Validation covers 128 guest cases reaching all 77 words, including modeled
helper mutations of the child, slot, view table, and actor. There are also 128
defined SDK32 native cases per O0/O2/O3 with UBSan and eleven effective
negative controls. Six original call sites passed 144 bounded-window cases.
Another 48 cases connect the 34-word original camera helper; its nested call
and the other external helpers remain modeled. Tests cover slots 0 through 3
and actor selectors 0 through 3. Larger C shift counts, arbitrary helpers,
complete parent functions, hardware fault behavior, and concurrent access are
not qualified.

Both object padders match independently assembled retail code and pass 16
rebased GNU links and 104 bounded access-cut comparisons. Actual Make and a
strict complete-image comparison account for **265 changed bytes** with zero
exclusions. All 44 neighboring functions, 6,050 function addresses, and
189,088 protected data bytes remain unchanged. Existing compiler warnings in
the owner are unchanged. The actual ELF SHA-256 is `12b75cade2af524b309e841edf047d3309a5369c05d9cc11ec3ced0cc19ec10f`.
The existing full-build checksum mismatch remains; this function match does
not imply a matching complete ROM.

Fresh actual ELF recount: **4,332 / 5,513 (78.58%)** overall and **3,659 /
4,840 (75.60%)** Game, zero drift and 1,181 different. The 80% target needs
79 more exact functions. Tools were committed first as
`c6a51fd4b198e72f52c6d85f8914dc9bce854d5a`; the consumer change is separate.
