# Game Cached Quad Builder Match

Date: 2026-10-06. Starting checkpoint: `e3e8b52`.

Recover `func_15140190`, **134 words / 536 bytes**, VA
0x15140190..0x151403A8, ROM 0x16D640..0x16D858, frame **0xD0**, in
[game_169510.c](../../conker/src/game_169510.c). Replace the false zero-return
C stub with a semantic cached quad builder. Existing O2/g3 emits **129 words
directly**; five expected-word guards reorder independent first-corner setup.
No new profile/shared header/data/symbol/layout or broad conversion batch.
The [retail reference](../../conker/asm/nonmatchings/game_169510/func_15140190.s)
remains unchanged.

## Recovered Contract

Actor byte pointer, signed-halfword view, allocated vertex pointer return.
`func_151D5D60(actor+0x100, view, 0x40, &cursor, &fresh)` supplies escaped
cursor and fresh byte. Capture the original cursor for return. On null,
return null without copies, matrix setup or vertex writes; even fresh=255
does not bypass this gate. On a fresh buffer, copy actor+0xC0 twice, to the
live actor+0x100 indexed slot and its +0x40 half. **Reload the slot after the
first copy**; callbacks can change it and the actor dimensions.

Capture four private 12-byte corners from width/height +0x2C/+0x30:
(+,+,0), (-,+,0), (-,-,0), (+,-,0). Call orientation `func_150A8050` using
actor +0x40/+0x44/+0x48; then read live translation +0x34/+0x38/+0x3C
into matrix row three. For each corner, pass the private point's three output
addresses to `func_150A7960`, truncate transformed coordinates to signed
32-bit values and store their low halfwords as Vtx positions. Clear flags,
advance the escaped cursor by 16, preserving original-pointer return.
Texture coordinates and color bytes remain as initialized by copies, or
untouched on an existing buffer. No saturation, index clamp or eager snapshot
of caller-owned translation/buffer slots.

The matrix callee is retained assembly: **40 normal-return words**, Z stored
in its return delay. It is not the separate `func_150A7A00` tail contract.
Its arithmetic is `(m0*x + m4*y) + (m8*z + m12)` per axis, with each single
precision operation rounded independently. Guest qualification executes this
actual callee, not just an idealized matrix callback.

## Compiler Evidence

[Driver](../../tools/experiments/game_cached_quad_builder_candidates.py):
**six forms x four profiles = 24 controls**, real SDK types/fixed call anchors,
empty diagnostics. Selected O2/g3: 134 words/frame 0xD0/five differences;
plain O2: 134/0xD0/35. O1 profiles: 160/0xA8/160. Moving first Z initialization
after X/Y raises differences to eight. Naming point at function scope gives
22 differences, because it changes stack allocation. Declaring point inside
the loop recovers saved-register lifetimes and the retail branch-delay update.
Outer success block gives 130 words/97 differences; early-null return gives
132/108. A 32-bit counter gives 132 words/frame 0xD8/130 differences.

Earlier ignored screens under `conker/build/game-vertex-attribute-initializer/`
bounded branch diamonds, byte declaration order, pointer scopes and corner
initialization. No alternate profile/forced instruction body was installed.

Only offsets **0xB4..0xC4** differ. The raw five-word sequence is:
move matrix pointer to A0; zero private corner Z; load actor width; store
private corner X; load actor height. Retail loads width; moves matrix pointer;
stores X; loads height; zeros private Z. Same instructions, registers and
data dependencies; no calls/branch/relocations, and private Z does not alias
caller-owned actor dimensions. Guards bind each exact compiler word and
replace only this closed independent schedule. All remaining 129 words,
including frame/save lifetimes, signed argument transport, loop counter and
branch delay, match directly. No insertion/omission/trampoline.

## Qualification

[Six tests](../../tools/tests/test_game_cached_quad_builder_match.py):

- All 24 compiler controls and exact five-word permutation bound.
- **864 guest cases / two bodies** execute selected raw C and retail plus
  actual matrix assembly. View low-halfword/high-bit transport, null/success,
  fresh 0/1/255, three linear matrices, fractional/signed/halfword-overflow
  dimensions, two stack phases, slot/width mutation after the first copy,
  translation mutation after orientation and escaped-cursor redirection.
  Independent byte reference checks complete external storage and original
  return. Compare all ordered external accesses and normalized call traces;
  **all 174 caller/callee words** covered. Saved GPR/FPR/SP/RA checked.
- **864 native full-storage cases** execute actual caller C with the recovered
  semantic matrix C body, forwarding instrumentation, callback contracts and
  independent corner arithmetic. Entire actor and two guarded 160-byte
  buffers checked, including retained texture/color bytes and copied halves.
- **65536 native null cases** cover every signed-halfword view bit pattern,
  fresh=255, no indexed slot access or rendering callbacks. 32-bit pointer,
  two-byte halfword and 16-byte SDK-equivalent vertex layout checked.
- Six compiled negatives reject stub, missing flags, three corners, wrong
  translation/axis by actual memory/return; wrong size must fail the exact
  backend contract, not an unsupported-instruction assertion.
- Production source/complete slot/actual matrix binding; exactly five guards,
  with normalized complete words equal to retail.

Allocation/SDK copy/orientation remain bounded providers, not full backend,
hardware FCSR, orientation implementation, caller discovery, gameplay or host
adoption. No NaN/infinite/out-of-s32 coordinate acceptance claim. Native
backend instrumentation is noinline to keep the live escaped stack pointer
opaque to GCC; the production caller statements are unchanged.

## Linked Audit

Build/link/progress pass. Only the quad slot changes across **6059 function
slots**; all addresses and sizes fixed. Target SHA-256:
`876c497d2c655c72a0b20563e8729fc574792cfd563ae68cd57323384b573d53`.
Protected `.init`, `.init_data`, `.debugger`, `.game_data` unchanged;
**720 owners / 189088 bytes** remain retail-exact. **10660 existing guards**
preserved in order plus the five scheduling guards. Owner retains **48
identical preexisting warnings**, zero new after shifted-location normalization.
No warnings in the recovered builder; existing generated_12D630 recipe
warnings remain unrelated. Constructor and both recent helpers remain exact.

This was already counted as C, so converted totals stay **5464/6042** and
Game **4791/5321**, bytes **85.57% total / 84.89% Game**. Exact totals improve
to **3327/5464 (60.89%)**, Game **2654/4791 (55.40%)**, **2137 different**,
zero drift. Init492/492 and Debugger181/181 unchanged. README receives only
these aggregate measurements. Tools check, compileall and diff check pass;
**31 docs / 3341 relative links / zero broken**. All **66 focused post-link
tests pass in 741.875 seconds**, no skips. Ignored audit/after snapshots under
`conker/build/game-cached-quad-builder/`, starting from the attribute-helper
`after.json` checkpoint. Four existing tests' global guard-count assertions
advance to 10665; their per-function contracts are unchanged.

## Next Work

Recover adjacent **`func_15140410`, 167 words / 668 bytes**, VA
0x15140410..0x151406AC, ROM 0x16D8C0..0x16DB5C, frame **0x68**. Its current
four-signed-word zero-return stub is false. Retail takes actor plus two
three-float basis vectors and signed-halfword view, returning the original
allocated quad pointer. It shares the fresh two-copy/escaped-cursor backend
contract but constructs all four positions from **captured scaled basis
components** and **repeated live actor translation reads** instead of calling
the orientation/matrix helper. Preserve `(translation +/- widthAxis) +/-
heightAxis` operation order, saved F20/F22 lifetime and output alias behavior;
do not replace it with an idealized sum or eager snapshot of all translations.
Initial isolated screening completes **44 controls** under
`conker/build/game-cached-quad-builder/next-basis[-scales/-operands]/`. Scalar width/
height temporaries give the correct 167 words but wrong frame 0x70 and 33
differences. Inline the repeated scale reads, put fresh byte after six scaled
components: **167 words / correct frame 0x68 / eight differences** under
O2/g3; plain O2 has 17. O1 gives 210 words/frame 0x48/209 differences. The
eight words are an independent width-load/height-vector pointer load swap
at 0xA4/0xA8 and six commutative multiply operand orders. Reversing all six
source multiply operands recovers those retail orders directly: **167 words /
frame 0x68 / only two scheduling differences** under O2/g3, plain O2 eleven.
Reversing only first components gives six differences, only later components
four. All six scaled components still capture before vertex writes. This is
compiler evidence only: no candidate installed or behavior qualification/
match claimed for the next function. Start from
`next-basis-operands/reverse-all-o2g3.c`; test captured component lifetimes
and output/actor/basis aliases before considering those two independent loads.

No sibling source/build/save/frozen Release changes, runtime launch or push.
