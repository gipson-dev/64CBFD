# Game Owner and Selector Event Handler

Date: 2026-10-02

## Retail Contract

Recovered `func_151BD21C` in `conker/src/game/generated_1E73B0.c`, replacing
its zero-return placeholder. Retail occupies `0x151BD21C..0x151BD2BC`,
40 words / 160 bytes, at ROM `0x1EA6CC..0x1EA76C`.

The callback has no defined return value. Its three arguments are a record,
an event payload, and an unsigned byte event code. The target payload pointer
is stored at record offset `0x98`. The initial target owner word is captured
before dispatch; target offset four holds the associated selector byte.

- Event zero: if the target owner equals event word zero OR the target selector
  equals event byte four, clear record byte `0x30` and set bit `0x8` in the
  halfword at `0x1E`. Preserve all other flag bits and target fields.
- Event `0x2D`: if the initial target owner equals event word zero, replace it
  with event word four and copy selector byte nine. Otherwise, if it equals
  event word four, replace it with event word zero and copy selector byte eight.
- Equal endpoints choose the first/forward remap arm. Unsupported event codes
  and unmatched payloads do not change the record or target.

The recovered function is `void`, with the retail unsigned-byte argument
width. No shared headers or adjacent routine bodies are changed.

## Compiler Trials

The initial straightforward if/else body emits 38 words. A switch variant
emits 39 words but changes dispatch shape; register storage hints do not
improve it. Expressing the zero-event comparison as a direct target-word
access recovers the initial owner copy and 39-word shape. An explicit
branch-local event-owner assignment instead grows to 43 words with a saved
register and is rejected by the fixed retail slot. An explicit return in
the flag-setting arm does not improve the final shape and is not retained.

The final source under the existing `-O2 -g3` profile emits all semantic
operations in 39 words. It needs no omitted logic supplied by matching tools.

## Strict Guard Boundary

Nine strict expected-word entries normalize the final C object:

- Closed owner/event register reuse, including the equivalent initial owner
  copy and one commutative equality comparison's operand order.
- Move the flag halfword publication out of the leaf return delay slot.
- Insert exactly one independent `nop` after that return, recovering the
  retail 40-word length. No semantic instruction is inserted or omitted.
- Adjust two branch displacements only for that inserted word; their logical
  destinations and conditions remain unchanged.

Guard offsets address the pre-insertion C object. The first full rebuild
correctly rejected a comparison guard at the wrong offset (`0x24`); fixing
it to the actual `0x28` resolves the stale-word check. A focused object
rebuild confirms the guarded retail sequence before the full linked check.

No compiler override, data placement, or branch condition is changed. The
source explicitly retains the original owner snapshot across remap stores.

## Behavior Verification

`tools/tests/test_game_owner_event.py` extracts the actual source body and
executes it in a freestanding 32-bit host fixture. Real four-byte pointers
preserve the record's pointer field at `0x98`; `-fno-strict-aliasing` permits
the fixture's typed overlays on aligned byte buffers. Eight tests cover:

- Zero-event owner match with preservation of unrelated flag bits.
- Selector-only zero-event match despite a different owner.
- Zero-event nonmatch with no writes.
- Forward and reverse remapping, including negative owner words.
- Equal-endpoint precedence and distinct selector bytes.
- Unmatched remapping and every unsupported nonzero byte event code.
- Target/event aliasing in both remap directions and the store/read order.

The ordinary cases compare every record, target, and event byte against the
reference, including sentinel padding and untouched input payload. The alias
cases check the affected words and selectors explicitly. The host is
little-endian; it tests native word and byte access semantics, not a raw
big-endian guest-memory replay. Capability checks explicitly skip without
freestanding 32-bit compiler/execution support.

All eight cases execute and pass on this machine. All 75 tool tests and
`make tools-check` pass. This is source-behavior evidence, not arbitrary host
ABI portability, invalid-pointer behavior, or gameplay qualification.

## Linked Verification

The corrected `make -C conker NON_MATCHING=1 all match-progress -j4` rebuild
passes. Independent linked-byte comparison confirms all 160 bytes match the
pristine ROM. SHA-256:
`7ecf1248e2a1c40a7ae144142070395acf72eae703c9eed90988db62ce77edee`.
The following `func_151BD2BC` remains at `0x151BD2BC`.

Both entire Init sections remain byte-exact after rebuilding: `.init` is
164,048 bytes and `.init_data` is 17,376 bytes. Their SHA-256 values remain:

- Code: `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`.
- Data: `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.

This is linked code/data evidence, not BSS, gameplay, or a full-ROM match.

## Progress and Resume

Conversion totals remain 5,461 / 6,042 C rows. Exact C now totals
3,248 / 5,461 (59.48%); Game is 2,575 / 4,788 (53.78%). There are 2,213
different C functions and zero address drifts. Init retains 47 assembly rows;
the supported compiler-generated Init queue remains complete.

Next ordinary Game target: `func_151D2F00`, 36 words / 35 real differences.
Keep `func_150A76F0` in the handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue. No sibling host-port
source, build, or runtime artifact was changed.
