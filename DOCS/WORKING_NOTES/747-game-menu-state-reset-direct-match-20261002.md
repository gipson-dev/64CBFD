# Game Menu State Reset Direct Match

Date: 2026-10-02

## Scope and Retail Contract

Recovered `func_151DE85C` in `conker/src/game/generated_20AE20.c` from its
zero-return placeholder. Retail occupies `0x151DE85C..0x151DE8E8`, 35 words /
140 bytes, at ROM `0x20BD0C..0x20BD98`.

The routine has no defined return value and takes no arguments. Its local
forward declaration and body are now `void func_151DE85C(void)`. The existing
caller `func_151DE7D4` ignores the result and remains unchanged.

Retail performs these operations in order:

1. Clear `D_800D2E40` before calling `func_1501C730(6, 0x1D, 0, 0, 1)`.
2. After that call, assign `D_800E0B94 = 3`, `D_8008FD80 = 1`,
   `D_8008FE28 = 2`, and `D_8008FDA4 = 0`.
3. Load the object pointer from `D_8008FDD4` and clear object byte `0x3E`.
4. Reload that pointer and assign object byte `0x2B = 5`.
5. Reload it a third time, read byte `0x2B` as signed, and copy it to `0x2C`.

The gate is cleared only before the external call. A gate change made by
that call is not overwritten afterwards. The object pointer is first used
after the call, so an object replacement made there is respected.

The menu-state label describes the inspected caller and neighboring state
setup; no specific complete gameplay transition is qualified here.

## Direct Matching Evidence

The first recovered body under the existing `-O2 -g3` slice profile emits
the complete retail sequence directly, including its frame, global address
relocations, three object-pointer loads, and signed-byte copy.

No expected-word guard, instruction insertion, omission, compiler override,
or shared type change is added. Independent comparison confirms all 140
linked bytes match the pristine ROM. SHA-256:
`4d8d573512d7816cffe741c9f343ee500e1434553ca94e2f864c8e4d4cab3bbe`.
The following `func_151DE8E8` remains at `0x151DE8E8`.

## Verification

`tools/tests/test_game_menu_state_reset.py` extracts and compiles the actual
body with globals and a mocked external call. Five tests verify:

- Exact submitted arguments and the pre-call gate clear, while the other
  state bytes still have their old values during the call.
- Final state-byte assignments.
- Changes to only the three specified object bytes, preserving every sentinel.
- External-call mutation: the gate mutation survives, the four later globals
  are overwritten as specified, and a replacement object is used.
- Repeated reset re-applies the state and submits the external call again.

The host fixture uses native pointers and models source-level byte behavior,
not guest pointer layout or concurrent mutation between individual accesses.
The three retail pointer loads and signed load are verified in the target
instruction sequence; host behavior tests alone do not prove that schedule.
No null-object or gameplay qualification is claimed.

- Full `make -C conker NON_MATCHING=1 all match-progress -j4`: passed.
- All 85 repository tool tests: passed, including all five new cases.
- `make tools-check`: passed.
- Entire linked `.init`: 164,048 bytes, byte-exact against retail.
- Entire linked `.init_data`: 17,376 bytes, byte-exact against retail.

Init hashes remain:

- Code: `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`.
- Data: `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.

This is linked code/data evidence, not BSS, gameplay, or a full-ROM match.

## Progress and Resume

Conversion totals remain 5,461 / 6,042 C rows. Exact C now totals
3,250 / 5,461 (59.51%); Game is 2,577 / 4,788 (53.82%). There are 2,211
different C functions and zero address drifts. Init retains 47 assembly rows;
the supported compiler-generated Init queue remains complete.

Next ordinary Game target: `func_1501CDC0`, 37 words / 36 real differences.
Keep `func_150A76F0` in the handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue. No sibling host-port
source, build, or runtime artifact was changed.
