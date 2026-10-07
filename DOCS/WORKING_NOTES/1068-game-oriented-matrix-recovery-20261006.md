# Game Oriented Matrix Recovery

Date:2026-10-06. Baseline:`bc0decb1`
([Note1067](1067-game-scaled-matrix-match-20261006.md)).
This checkpoint banks compiler recovery and qualification tools, **not a new
production match**. `func_15142600` remains a zero-return C placeholder in
[game_16EE20.c](../../conker/src/game_16EE20.c). Neither candidate is installed;
no word guards, frame rewrite, shared-header/profile or production change.

## Recovered Contract

Retail:142 words /568 bytes, frame0xB8, VA15142600..15142838,
ROM16FAB0..16FCE8. Twelve inputs:output Mtx pointer, two row factors, three
column factors, start point and end point. Original caller func_150B9D14 spans
30 words at VA150B9D14..150B9D8C /ROME71C4..E723C. It forwards row factors
from source+18/+1C, columns+2C/+30/+34, start+38/+3C/+40 and end+20/+24/+28,
then returns1. Last argument is stored in the jal delay at ROME7220.

Subtract start from end and normalize the three-component direction using
reciprocal sqrt of its separately rounded three-square sum. Form horizontal
left=(directionZ,-directionX); normalize its two components. Form up from
direction cross normalized left, then normalize up independently. Multiply
each component by its column factor, round, multiply by its row factor, round
again. Rows0/2 use row0; row1 uses row1. Translation is the original start
point, **not a negative view-matrix dot product**. Set [0][1] and the first
three fourth-column fields to0, [3][3] to1; call guMtxF2L(matrix,output).

Retail has no coincident/vertical-point fallback. Zero direction length or
zero horizontal magnitude propagates IEEE infinities/NaNs through the math;
do not clamp to identity or introduce an epsilon. Saved F20/F22, SP and RA
survive the sole helper call. No scalar result is consumed by the caller.

## Compiler Findings

[Maintained driver](../../tools/experiments/game_oriented_matrix_candidates.py)
reproduces eight source forms across four actual SDK profiles:32 controls,
empty standalone diagnostics, no exact candidate. It does not import ignored
scratch files or dynamically rewrite another driver's implementation.

| Control | Words | Frame | Differing Words |
| --- | ---: | ---: | ---: |
| Prior vector-local O2/g3 baseline |143|0xC8|138|
| Two-component horizontal, early first element, row-wise stores |142|0xB8|110|
| Maintained array-up, column-wise stores |142|0xB8|84|
| Maintained reversed struct-up, column-wise stores |142|0xC8|57|

The 57-word challenger differs **only in stack immediates**:every changed
word retains its upper16 bits and SP base. All arithmetic, FPR allocation,
instruction order, helper call at offset21C, and saved F20/F22 instruction
positions otherwise reproduce retail. The test checks that property word by
word; it does not normalize those differences.

The fitting frame0xB8 candidate still has84 actual word differences. The
closer challenger has an oversized frame. Neither is a completed match.
Its slot length alone does not justify installing it or counting progress.

Exploratory controls tested vector/array/scalar representations, identifier
names, declaration permutations, reciprocal literals, captured factors,
explicit normalized vectors and contiguous working-state layouts. A separate
normalized-up form preserves the non-stack sequence with44 differences but
frame0xD0; separate normalized-left forms grow to158 words. Meaningful aggregate
layouts can give frame0xB8 but151..157 words. Those are rejected controls,
not excuses for rewriting retail stack offsets.

Initial matrix-order scratch construction failed a regex on same-line
translation stores; correct the scratch generator and rerun it to completion.
An earlier array-initializer control was rejected by IDO's C restrictions and
was replaced with explicit assignments. Failed attempts are not passing
controls or acceptance evidence. Identifier-only controls did not improve
the earlier forms; don't resume that theory without new evidence.

## Qualification

[Eleven maintained tests](../../tools/tests/test_game_oriented_matrix_recovery.py)
pass in39.018 seconds, no skips/errors/failures:

- 32 compiler controls, including explicit assertions that the selected
  frame-fitting body is142/0xB8/84 and the stack-only challenger142/0xC8/57.
- **2448 three-body guest cases**:72 direction/sign/row/column/degenerate
  fixtures plus132 every-input special-bit fixtures, three source/output
  aliases, two stack phases and helper source mutations. All142 words covered
  in both candidates and retail. Compare known matrix fields, conversion
  destination, helper-entry external storage and every final external byte;
  poisoned volatile GPR/FPR state must leave all saved state intact.
- **1224 native caller cases per candidate**, two candidate bodies. Actual
  freestanding32-bit C, typed caller, hardware SSE sqrt, source/output aliases
  and helper mutations; complete external-byte comparison. Converter is a
  bounded float-payload capture, not the native SDK fixed converter.
- **144 connected cases per body** execute all30 original caller,142 builder
  and115 original guMtxF2L words. Cardinal directions, asymmetric exact scales,
  aliases and two stack phases qualify all12 forwarded argument words,
  return1 and complete fixed packing. Conversion is restricted to finite,
  exactly integral, signed32-bit representable results after multiplication
  by65536; no fractional/FCSR-mode/NaN/out-of-range conversion acceptance.
- Nine compiled negatives change a known matrix field or call on valid
  mapped storage:placeholder, missing converter, reversed direction, wrong
  cross sign, omitted up normalization, wrong row/column, view translation
  and wrong output pointer. Native integer-load negative changes known matrix
  values under the corrected float prototype; numeric conversion is rejected.
- Missing source fields, private matrix or output fail strict mapped-memory
  gates. No hardware fault or native out-of-bounds claim.
- Actual padding retains568 bytes and the R_MIPS_26 at21C; alternate converter
  linking changes exactly that call word, without guards or alignment-tail
  inclusion.
- Both copied builder owners retain93 functions:92 neighbors' raw bytes/
  relative relocations, private pools and two existing warnings unchanged;
  target raw bytes/relocations equal its standalone candidate.
- Copied caller owner retains all **eight** functions' raw bytes/relocations,
  pools and zero warnings; the typed caller retains all30 retail words after
  resolving its single call relocation. The proposed pointer/float prototype
  and three float loads do not alter guest instructions. This correction is **not yet
  installed** in [generated_E5E90.c](../../conker/src/game/generated_E5E90.c).

Arithmetic NaNs are classification-compared only in the first3x3 matrix;
translation bits, zero fields and final1 remain exact. Private full-memory/
trace identity is not claimed across different layouts. Guest sqrt/divide/
negation use bounded binary32 models; no N64 FCSR flags, exception behavior,
subnormal hardware modes, native NaN payload or gameplay/rendering acceptance.

First eight-test run failed four guest gates because the inherited interpreter
did not implement neg.s. Add sign-bit inversion locally to this fixture, not
the shared interpreter; all eight pass in16.274 seconds. Add controls, actual
padding and copied-builder gates; final eleven-test bundle passes above.
No production fix was needed for that harness correction.

## Baseline Preservation

Production source, root README and guard CSV remain unchanged from bc0decb1.
Read-only ELF audit compares all6059 slots and four protected sections with
the banked Note1067 manifest; no rebuild is needed for this tools-only work.
All10809 guard rows retain canonical SHA-256
`e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a`.
All720 original Game-data owners /189088 bytes remain exact.

Documentation check:50 documents/3559 relative links/zero broken. Project
tool checks, scoped Python syntax and diff checks pass. All28 focused tests
pass in74.658 seconds, no skips/errors/failures:these11 tests, the previous12
matrix tests and five actual-padder tests. Final receipt is in the ignored
directory.

No new function is converted or matched. Banked aggregate remains exact
3342/5464 (61.16%), Game2669/4791 (55.71%),2122 different, zero drift;
converted5464/6042 total and4791/5321 Game, bytes85.57% total/84.89% Game.
Do not change root README percentages for an uninstalled candidate.

Ignored receipts:`conker/build/game-oriented-matrix/` (exploratory and
maintained screens) and `conker/build/game-oriented-matrix-test/` (qualification,
layout differences, copied owners, audit and documentation receipts).
No sibling source/build/save, frozen Release, runtime launch, host adoption,
full ROM checksum, gameplay acceptance or push.

## Resume Here

1. Start from maintained `up1-columns1-early0` under O2/g3:142 words, frameC8,
   57 stack-only differences. Its non-stack instruction sequence is already
   correct; avoid restarting mathematical reconstruction or broad profiles.
2. Recover meaningful private-local layout. Retail position=SP28/2C/30,
   surviving deltaZ=3C, raw horizontalZ=44, raw upZ/Y/X=48/4C/50,
   normalized directionZ/Y/X=68/6C/70, matrix=78..B4. Challenger deltaZ=40,
   horizontalZ=48, up=4C/50/54, matrix=5C..98, direction=B8/B4/B0.
   A 20-byte gap before the direction suggests normalization temporaries,
   but their exact source types/lifetimes remain a hypothesis.
3. Require the original142 words/frameB8 from legitimate C declarations and
   lifetimes; do not install a57-word stack/frame normalization workaround.
   Reuse the maintained three-body/native/connected/padding/owner tests.
4. Once a matching candidate is ready, install the typed builder **and** local
   caller correction together, then rebuild/audit slots, original data and
   guards; rerun neighboring regressions and refresh actual progress.

Keep the Game-matching goal active. This is a coherent recovery checkpoint,
not a pause or completion of func_15142600.
