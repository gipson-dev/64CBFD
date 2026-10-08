# Game Projection Wrapper ABI And Frame Audit

Date: 2026-10-06. Starting checkpoint: `c7aede8c`.

`func_15144CEC` remains the production zero-return placeholder. This checkpoint
banks inspection and reproducible compiler controls, **not a semantic recovery
or byte match**. Retail is 101 words / 404 bytes, frame 0x48,
VA 0x15144CEC..0x15144E80, ROM 0x17219C..0x172330.

## Observed Contract

Retail accepts a float XYZ point, an XY output, optional Z/W/reciprocal output
pointers, and a byte view index. Null optional outputs use separate private
floats at root SP+0x44/+0x40/+0x3C. The helper receives eight arguments:
matrix at `D_800D9D10 + index*64`, three point floats, then four output pointers.
The leading matrix pointer means the three floats travel as integer argument
words, not leading F12/F14 arguments.

The retained helper chain is nonstandard: 40-word `func_150A7960`, five-word
`func_150A7A00` trampoline, 13-word `func_150A7A14` continuation. The trampoline
saves the caller return in T9 and installs the continuation in RA. The matrix
leaf computes/stores XYZ; the continuation computes/stores W and returns
through T9. All 58 linked words equal retail. Do not substitute an ordinary C
XYZ helper: A0/T9/F0/F2/F4 remain live across its synthetic return.

The wrapper caches W once after all helper output stores. It rejects
`D_800A56B0 <= W`, then `W <= D_800D9B20`, then zero. These rejected paths still
retain the helper's four stores. Accepted paths write reciprocal `1.0f/W`.
Camera fields use an explicit 0x180-byte view stride from `D_800BE628`:
screen X/Y multiply fields +0xC/+0x10 plus 5.0f; X adds field +0x34 and Y
subtracts from field +0x38. Y's product is computed before the X store;
reciprocal and the global camera base are read again after that store.
Output aliases can therefore affect the final Y calculation.

Existing `struct140` exposes the used field offsets but its complete apparent
size disagrees with its 0x180 comment; do not use typed array indexing or
globally repair this definition as part of the wrapper. The existing local
`func_150A7A00` declaration in `game_476D0.c` has an incorrect ten-argument ABI;
its draft caller is commented. Correct this declaration if installing a shared
helper prototype. No header is changed by this investigation.

## Compiler Controls

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_projection_wrapper_candidates.py) uses
real SDK/structure headers, existing O2/g3 and fixed retail external anchors.
The default run now contains all 20 measured controls: 16 pointer-home
qualifier masks, uncached-W and grouped-nonzero forms, and the latter two
with a volatile view index. All isolated diagnostics are empty.

| Forms | Body Words | Frame | Aligned Differences Including Overflow |
| --- | --- | --- | --- |
| Masks 0/2/4/6 | 101 | 0x50 | 85 |
| Masks 1/3/5/7 | 103 | 0x50 | 95 |
| Masks 8/A/C/E | 105 | 0x50 | 101 |
| Masks 9/B/D/F | 108 | 0x50 | 104 |
| Uncached W / grouped nonzero | 102 | 0x50 | 90 |
| Those two with volatile index | 106 | 0x50 | 94 |

No exact form. The initial body spills a cached view index across the helper,
uses different FP lifetimes and reuses the just-stored reciprocal for X;
equal body length alone is not matching or ordered-access qualification.
No source/profile/guard installation is justified by these receipts.
Ignored receipts: `conker/build/game-projection-wrapper/` and
`conker/build/game-projection-wrapper-audit/`.

## Audit And Boundary

[Three tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_projection_wrapper_audit.py) pass in
14.634 seconds, no skips. They reproduce all 20 compiler measurements, bind
the complete linked helper chain and its synthetic return, and confirm the
retail frame, production placeholder and absence of wrapper guards.
The initial run caught an incorrect test literal for the continuation's final
F18-to-T2 store; corrected against the pristine ROM and assembly, then rerun.

All 6059 linked slots, protected Init/Init-data/Debugger/Game-data sections
and 10646 guard rows equal the descriptor-measure checkpoint. All 720 Game
data owners / 189088 bytes remain retail-exact. `make tools-check` passes.
Production source, headers, data, profiles and matching aggregates are
unchanged: total 3314/5462, Game 2641/4789 exact, zero drift, 2148 different.
README needs no new narrative or count update. No sibling host source/build/
save/frozen Release change or push.

These are compiler/identity tests, **not connected execution, output-alias,
native C, finite-arithmetic, complete FCSR or gameplay qualification**.
Before replacing the wrapper, qualify ordinary output aliases, helper stores
before rejection, cached W, late camera/inverse reads, and matrix-fourth-column
aliasing across the retained continuation. Private-frame aliases and full
caller domains require separate boundaries. Do not normalize the entire
frame/body with arbitrary guards.

## Next Work

Continue Game matching with `func_1515C1A0`, a 41-word slot still represented
by a zero-return stub in `game/generated_188F90.c`; inspect its retail body
before choosing a source/ABI. This is a queued candidate, not a recovered
contract. Projection frame/lifetimes and the pair-clamp frame remain open.
The Game matching goal remains active.
