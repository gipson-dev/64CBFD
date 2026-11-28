# Reference distance/vector gate direct byte match - 2026-11-28

`func_15184DF0` in `conker/src/game/generated_1B1600.c` replaces its three-word
zero-return placeholder with **109 words / 436 bytes emitted directly from C**,
VA `0x15184DF0..0x15184FA4`, ROM `0x1B22A0..0x1B2454`. The original frame is
**40 bytes**, with no slot tail, insertion, omission or new guard. The interface
is `s32 func_15184DF0(s32 actorIndex, s32 recordIndex, f32 *x, f32 *y, f32 *z)`.

Actual production: **4,726 / 5,528 (85.49%) total**, **4,053 / 4,855 (83.48%)
Game**, Init 492/492, Debugger 181/181. Zero address drift; 802 still different.
Conversion rows and denominators are unchanged. **250 more matches** reach the
active 90% target of 4,976/5,528. This adds exactly one direct C match.
Previous consumer `10fe8f3a`; tools packet `81f01fbf650c41e8da70193eb1ab72656213c3e6` was committed first.

## Recovered source and floating-point order

The routine caches the selected actor's three coordinates from inline
`D_800CC2D0[26]` (stride 0x32C). It subtracts reference coordinates +0x2F8/
0x2FC/0x300 from `struct108 *D_800DBFF0` (stride 0x9A0), truncates the three
binary32 differences to signed words, and submits them to `func_150AD9A0`.

If the signed result is >=2001, it clears `D_800D3688`, reads that global back
into `D_800D368C`, and returns zero. Otherwise it calls `func_15184150` with
actor index and three output pointers, then loads **`D_800A7378` once**. Its
retail coefficient bits are **0x3FA66666**. It scales x, y, z sequentially using
that cached value. If any resulting output is zero, it clears the globals and
returns zero; otherwise it returns the saved distance. Signed zero, sequential
output aliases, callback mutations and coefficient/output aliases are preserved.
There is no commutative FP rewrite, regrouping, reciprocal or reassociation.

Caching actor coordinates recovers retail's exact FP loads, subtraction operands
and truncation schedule. The declaration order **actorX/actorY/actorZ, distance,
scale** also recovers the 40-byte frame and distance spill at SP+0x18. The
selected source has no padding array, volatile storage or register binding.
All sixteen code binding positions match directly. The original unreachable
word at index **104** is retained exactly; there are **108 reachable words**.

## Caller ABI and bounded providers

The aligned prepared-ROM scan finds one direct JAL at ROM **0x1B3FCC** /
VA **0x15186B1C**, in original `func_15186794`. Its complete **711-word** body is
pinned to the ROM, while qualification executes the **11-word window**
`0x15186B08..0x15186B34`, with rejection boundary `0x15187160`.

The window passes actor index in A0, record index in A1, x at caller SP+0xD8,
y at SP+0xD4, and z at SP+0xD0 through the fifth argument slot. It branches on
the returned Boolean condition and updates its iteration value in the delay
slot. All eleven window words and 108 reachable child words execute in
**1,918 fixtures x four streams / 7,672 connected executions**. Both pointer-
setup and forced-return controls reject, and all three stack outputs are checked.
The complete original parent is not newly qualified.

Original provider evidence pins **32 handwritten code words** for
`func_150AD9A0` and **134 words** for `func_15184150`. The former consumes three
signed integer words and produces the low32 result; the latter consumes actor
index and three float pointers. Its return is ignored here. Both providers are
**opaque boundaries** in these tests; their complete execution is not credited.
The unrecovered same-owner helper retains its existing non-prototype declaration/
definition: no neighboring stub or shared header is altered to install this
caller. Native qualification supplies the recovered provider interfaces in
separate translation units.

## Qualification and linked acceptance

- SDK/native32: **9,086 cases each at O0/O2/O3**, signed cutoff boundaries,
  finite fractional coordinate differences, 26-actor/three-record layouts,
  ten valid typed float alias modes, seven scales and eight provider vectors.
  Callbacks mutate coordinates, reference pointer, coefficient and globals.
  Independent Python binary32 expectations patch the expected objects; every
  byte of **21,112 actor bytes / 7,392 record bytes**, outputs, coefficient,
  globals and pointer identity is checked. Six semantic controls fail with
  exit 42, including cast-before-subtract, cutoff equality and coefficient reload.
  Strict aliasing, trapping UBSan, LTO types, round-to-nearest SSE and disabled
  contraction/excess precision pass.
- Guest: **9,294 cases x four streams / 37,176 executions**, all 108 reachable
  words, and exact retention of unreachable word 104. Literal complete normal state,
  ordered accesses and **3,260 fault-prefix quadruples** agree across original
  GNU-linked retail, raw C and both padded streams. Twelve alias modes include
  192 guest-only argument-home/pointer-global cases, negative/wrapping guest
  indices, three sparse pointer domains and both stack phases. Four semantic
  mutations reject. Provider side effects are explicit atomic boundaries.
- Both complete padders reproduce the frozen before owner and the same selected
  whole object. All **31 raw/padded neighbors**, pools and SDK32 type layouts
  stay fixed. The actual **three-command** Make
  recipe uses the existing **-O2 -g3 -Wo,-loopunroll,0** profile. No source profile,
  Makefile, guard, shared header or assembly change is required. No compiler/
  assembler warning is introduced; six unrelated duplicate-recipe warnings remain.
- **16 actual GNU links** independently rebase code, data globals and both calls,
  including signed HI16/LO16 carries. Every one of the 109 words and 16 bindings matches.
- Independent frozen-before-C plus original-target-ASM full-image prediction
  equals private and actual production Make output: **326 changed bytes, zero
  exclusions, no metadata permutation**. Only the target body/size changes.
  All **720 protected data owners / 189,088 bytes**, other linked bodies,
  addresses, extents, guard history and conversion rows stay fixed. Eleven
  image mutations reject, including unreachable word 104, ordered FP instruction,
  distance spill, RA save, neighbor, coefficient, original JAL, named extent/
  coefficient value and ELF header.
- Five complete packaged tests pass in both closed tools roots before and after
  installation: **20 fresh checks**, equal reports and audited import/data
  closures. Shared `make tools-check` passes. The real dirty tools sibling and
  all preserved dependency fingerprints remain intact.

ELF SHA256: `c1f0913f46a6b9af526e097334c56852a6abc79c7679390906dd8df5fd2315a0`.
Native scope uses finite, valid signed-float conversions and mapped typed objects.
Guest-only aliases/fault prefixes are additional machine evidence. These oracles
do not establish hardware FCSR exception flags, enabled FP trap behavior, invalid
float-to-integer conversion semantics, complete-provider or visible gameplay
acceptance. The emitted 109 words nevertheless remain byte-exact, without guards.

README changes are its two aggregate rows only. Graph refresh uses scoped AST
extraction with all previous IDs and qualification metadata retained, not
full-corpus extraction. Final graph/hook/immutable-bank receipts live in
`conker/build/game-reference-distance-vector-gate-15184df0-private/`.
Host applicability is assessed read-only; no host edit/build/launch and Release
stays frozen. N82 `func_1514EECC` remains parked. No push or subagent is used.

Next: continue ordinary unmatched Game matching from the sealed N93 bank.
