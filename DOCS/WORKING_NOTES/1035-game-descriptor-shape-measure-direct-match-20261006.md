# Game Descriptor Shape Measure Direct Match

Date: 2026-10-06. Starting checkpoint: `6474c718`.

**`func_1514462C` matches all 56 words / 224 bytes directly from C.** Slot
0x1514462C..0x1514470C, ROM 0x171ADC..0x171BBC, no frame. Replace the false
zero-return placeholder in [game_16EE20.c](../../conker/src/game_16EE20.c),
correct its [public prototype](../../conker/include/functions.h) to
`f32 func_1514462C(struct134 *)`, and declare the two referenced floats in
[variables.h](../../conker/include/variables.h). Existing O2/g3; no guards,
profile override, metadata/symbol-anchor/data change or overflow.

## Recovered Calculation

Read the byte at descriptor+0x15 and use its low two bits. Dimensions at
+6/+8/+0xA are read as **signed halfwords**, even though the pre-existing
`struct134` fields are unsigned. Explicit signed field views preserve those
loads without globally changing the descriptor definition.

| Mode | Calculation |
| --- | --- |
| 2 | Signed float conversion of the wrapped 32-bit product of +6, +8 and +0xA |
| 0 | Float conversion of the integer square of +6, times `D_800A5698`, then times float +8 |
| 1 | Float +6 times `D_800A569C`, then times +6, then times +6 again |
| 3 | Return 1.0f; no dimension or coefficient read |

The unsigned box product intentionally wraps before the final signed 32-bit
interpretation and float conversion. Multiplying three floats or relying on
overflowing signed C arithmetic does not preserve the retail operation.
The two float paths preserve a single-precision rounding boundary at each
multiply. Do not reassociate into a precomputed cube or height-times-square.
These are measured expressions, not an assertion about the full caller's
geometric meaning or valid shape dimensions.

Retail coefficient bits are **0x40490FDB** at 0x800A5698 and **0x3F860A92** at
0x800A569C. Tests compare pristine-ROM words against the linked Game-data
section. Their anchors already exist in `undefined_syms_auto.txt`; no new
address mapping or data object is introduced.

## Compiler Controls

[Driver](../../tools/experiments/game_shape_volume_candidates.py): real SDK
and descriptor headers; six box operand orders times two cylinder operand
orders under O2/g3, O2, O1/g3 and O1, **48 controls**, empty isolated diagnostics.
The selected source's height/depth/width expression yields retail's ordered
width/height/depth loads after compiler reassociation of the unsigned product.
Its cylinder expression likewise preserves retail's floating operand order.
Exactly one O2/g3 form matches directly; the other eleven have 1..4 differences.
The initial width/height/depth, cylinder-right draft had four differences.
Plain O2 produces 57 words; O1 forms 66 words with frame 0x10, all oversized.
No experimental profile is installed. Ignored receipts:
`conker/build/game-shape-volume/`.

## Qualification

[Six tests](../../tools/tests/test_game_shape_volume_match.py) use unchanged
shared guest runners, an independent mathematical/ordered-access reference,
and the actual recovered C with the real descriptor layout in native fixtures:

- **21504 guest cases**, retail/selected/alternate source bodies. Signed
  extrema, positive/negative/zero dimensions, all 256 flag bytes, two stack
  phases, retail coefficients and five synthetic finite coefficient pairs.
  Results, exact selected-retail ordered reads, complete memory footprints,
  no helper calls and saved register/SP/RA lifetimes are checked.
- The alternate four-difference source has the same qualified final results
  but **5376 different access traces**. The selected body matches the retail
  trace, not merely the returned numbers.
- All **55 reachable words** execute. The load at 0x1514468C is structurally
  unreachable: masked-zero dispatch's taken likely branch goes to 0x15144690,
  while the preceding mode-2 branch skips to the shared return path. Tests
  bind this load and both branch words; complete direct byte equality also
  includes this otherwise unexecuted word. No false 56-word coverage claim.
- **10752 native cases** compare exact float result bits and every byte of
  the 40-byte descriptor, including sentinel fields. Layout/offset checks use
  the actual repository descriptor definition. SSE single-precision and
  contraction-off qualification includes signed zero coefficients.
- Negative controls detect the zero stub, unsigned dimensions, missing flag
  mask and converting to float before the wrapped box product.

Five pre-install tests pass in **16.814 seconds**, no skips. The complete
post-link suite passes **all 58 tests in 94.861 seconds**, no skips: measure,
pair clamp, indexed state-save, timer, packet, linked-record tail/position,
random-range and position/sound regressions. This is bounded
aligned ordinary-memory/finite-arithmetic evidence, not full caller domains,
MMIO or concurrent inputs, arbitrary NaN/Inf/subnormal/FCSR modes, hardware
execution or gameplay acceptance.

## Whole Linked Audit

The header-triggered NON_MATCHING ELF/progress/match-progress rebuild passes.
Compare all **6059 linked slots** against the banked pre-edit checkpoint:
only `func_1514462C` changes; every address and slot size stays fixed.
Init, Init data, Debugger and Game data are byte-for-byte unchanged. All
**720 Game data owners / 189088 bytes** remain retail-exact; all **10646 guard
rows** are identical and ordered. The target has no guards and all 56 words
are direct. Linked target SHA-256:
`f9c049b7e07b9b46eb34513f494e55513a4d59600f33bb06f6c754e1d4a20496`.

An independent warning check compiles both the committed source **and its
committed headers**, then the new source/current headers. This avoids testing
the old integer-address definition against the new pointer prototype. The
same three owner warning IDs/messages/source expressions remain: 709 at
`func_1516972C(arg0)`, 712 at `func_15141E38(arg0, arg2)`, 709 at
`func_15144B34(arg0)`. No target warning. The broad rebuild also reports
warnings in other unchanged owners and the existing duplicate generated
recipe; no project-wide warning-free claim is made.

README aggregate rows are updated, with no recovery narrative appended:

| Section | Byte-Exact Converted Functions | Drift | Different |
| --- | --- | --- | --- |
| Total | 3314 / 5462 (60.67%) | 0 | 2148 |
| Game | 2641 / 4789 (55.15%) | 0 | 2148 |
| Init | 492 / 492 (100%) | 0 | 0 |
| Debugger | 181 / 181 (100%) | 0 | 0 |

Converted counts/bytes remain unchanged because the old stub already counted
as C. No sibling host source/build/save/frozen Release change or push.
Root `make tools-check` and `git diff --check` pass. Documentation check:
3162 relative links across 18 documents, zero broken.

## Next Work

Inspect `func_15144CEC`: live source is still a zero-return placeholder,
retail is 101 words / 404 bytes, slot 0x15144CEC..0x15144E80, frame 0x48.
It wraps the matrix helper at `func_150A7A00`, optional float outputs and
near/far/zero gates before projection stores. Recover its actual ABI and
qualify the helper's unusual output contract before replacing its stub.
No connected-helper or complete projection acceptance is claimed here.
The pair-clamp saved-pointer frame/return tail remains explicitly open in
[Note 1034](1034-game-pair-clamp-saved-register-backend-audit-20261006.md).
The Game matching goal remains active.
