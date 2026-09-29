# Game list-node allocator wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_1514EBA4` in `conker/src/game/generated_179F30.c` spans 30 words and
120 bytes at `0x1514EBA4..0x1514EC1C`. It calls `func_15167A68` to allocate a
36-byte record, passing one, `arg2 + 0x20`, one, `0xFF`, and one as the
remaining allocator arguments.

Allocation failure returns null. On success, the routine clears the node links
at offsets `0x14` and `0x18`, stores the retained payload at `0x10`, stores the
signed key at `0x1C`, and returns the allocated node.

## Compiler shape

Reusing the existing `GameListNode` layout recovers the field stores directly.
Declaring the second parameter as native `s16` is required: the big-endian o32
argument home places the signed key at stack offset `0x26`, reproducing
retail's `lh` instead of an explicit narrowing sequence.

Twenty-four of the 30 words emit directly from semantic C. Two independent
three-word schedules differ under IDO and are normalized with expected-word
guards:

- Offsets `0x04C..0x054` move the retained-payload load before the two link
  clears.
- Offsets `0x058..0x060` store the payload and load the signed key before
  selecting the allocated node as the return value.

The guards change only instruction order among independent operations. The
allocator call, null branch, field values, call relocation, branch targets,
frame, and epilogue come directly from C.

## Verification

- The focused generated-slice object builds with the complete retail
  instruction sequence.
- The complete ELF relink passes.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `df64ed7a708de97209ab59c3300454d23b0b136d2f6536fd7590342c55353244`.
- The authoritative matcher omits `func_1514EBA4` from its non-exact list and
  reports `2,984 / 5,465 (54.60%)` overall and `2,409 / 4,789 (50.30%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game placeholder. Preserve the existing
parks for unresolved jump-table ownership, handwritten live-register
fragments, and the documented compiler-scheduling cases.
