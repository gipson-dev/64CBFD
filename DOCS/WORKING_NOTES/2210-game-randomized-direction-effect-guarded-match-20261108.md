# Randomized Direction Effect Guarded Match - 2026-11-08

`func_151B4EA4` replaces a false zero-return placeholder with the complete
direction reversal, ordered random draws and effect-constructor submission.
Semantic C emits all **79 words / 316 bytes**, retail's **0x70-byte frame**,
RA slot **SP+0x44**, and the original local/outgoing argument layout.
**Seven checked prologue scheduling guards** make the fitted routine byte-exact.

Production: Total **4,279 / 5,513 (77.62%)**, Game **3,606 / 4,840 (74.50%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. **1,234**
converted functions remain different. **132** more exact functions reach
4,411 / 5,513 and the active 80% goal. Conversion rows remain unchanged.

## Recovered behavior and ABI

Owner `conker/src/game/generated_1E2180.c`; original `conker/asm/1E2180.s`.
VA **151B4EA4..151B4FE0**, ROM **1E2354..1E2490**. Public interface:

```c
void func_151B4EA4(f32 *position, f32 x, f32 y, f32 z, u8 selector, u8 mode);
```

Capture scale `D_800AA3D4`, negate each incoming direction component, then
multiply by that captured scale. Store the vector at SP+0x60/+0x64/+0x68.
The five calls must remain in order: float RNG, integer RNG, integer RNG,
float RNG, integer RNG. Keep the two float results and first two integer
results at SP+0x4C/+0x58 and SP+0x50/+0x54 respectively. Cast integer draws
to unsigned 32-bit before modulo, preserving negative bit patterns as DIVU inputs.

After all five draws, load live size `D_800AA3D8`, then live spread
`D_800AA3DC`. Submit exactly 16 arguments to `func_151D9014`:
position, local vector, selector, firstFloat*spread+(-1), firstInt%31+20,
secondInt%101+155, secondFloat*152+109, lastInt&1, size, size, 0, 0, 1,
0, mode, 1. Each multiply and add remains a separate single-precision operation.
The position pointer and both incoming byte homes reload after the draws.
Later provider mutations cannot change the already-built direction vector.

The constructor's original 248-word assembly qualifies its pointer-or-zero
return and the full argument widths: pointers for 0/1, u8 selector 2, f32 term 3,
s16 duration 4, u8 alpha 5, f32 term 6, u8 variant 7, f32 size 8/9, u8 flag 10,
s32 word 11, u8 flags 12/13, u8 mode 14, s32 word 15. The C declaration uses
`void *` for its return. The sole aligned caller, exact 22-word
`func_151B4E4C`, consumes no target return, so the target and its existing
forward declaration both become void. The whole wrapper is executed in tests;
it builds its position vector locally and supplies owner bytes+0x58/+0xC.

## Closed prologue schedule and its limits

All 72 words outside indices 1..7 match directly. The closed permutation is
destination<-raw source: **1<-6, 2<-1, 3<-2, 4<-7, 5<-3, 6<-4, 7<-5**.
The scale HI relocation moves +0x18 to+0x04, and LO +0x1C to+0x10.
No instruction is inserted, omitted or renamed; frame, saved roles, local
spills, RNG call sites, all 16 constructor arguments and epilogue remain fixed.
Every raw byte and all 12 relocation records are pinned. Each raw-byte,
binding and guard-expectation corruption rejects rather than applying an
open-ended permutation. Existing guard history remains an exact byte prefix.

Raw memory access order is **different**: it stores RA, incoming position
home and incoming z home before loading scale. Retail loads scale first.
The four accesses commute only for mapped, disjoint scale/global and valid
private frame/home storage. The actual scale binding remains in the audited
protected data region; tested stack layouts and independent rebases are
checked explicitly for disjointness. All registers, private bytes and
subsequent execution reconverge after word 7. End-state comparisons apply
only the documented four-event permutation in both access/event ledgers.

Three deliberately aliased scale bindings, one for each store slot, produce
different results and are rejected by the address-domain check. Eight fired
prologue fault prefixes have independently predicted memory/access results.
Raw literal fault-prefix equivalence is **not** claimed. Separately, fitted
and retail code agree in full literal state across **102 fired fault-prefix
pairs**, including **18 delay-slot cuts**. Guest parameter-home mutations are
not claimed as portable native C behavior or hardware/gameplay acceptance.

## Qualification and bank

- **107 frozen inputs** pin the complete source/object, headers/compiler,
  retail input, layout, guards, caller and original helpers.
- **Five raw/padded neighbors** and pools remain fixed, including the existing
  GLOBAL_ASM routine. Both complete-owner padders agree across six functions.
  The actual **five-command Make recipe** includes assembly preprocessing and
  postprocessing, reproducing the qualified owner under existing O2/g3 with
  **zero C diagnostics**. Alternate O2-without-g3 and O1 profiles were rejected;
  the Makefile profile remains unchanged.
- Strict prediction of the **entire ELF** allows only this body/extent
  changing 28 to 316 bytes and three closed symbol-row/name pair exchanges:
  D_800AA3D8/D_800AA7A8, D_800AA3D4/D_800AEB54, D_800AA3DC/D_800AEB5C.
  These are **six metadata rows**, not exclusions. **280 changed ELF bytes,
  zero exclusions**, all **6,052 function addresses** fixed. Every other body
  and **720 protected owners  / 189,088 data bytes** remain fixed.
- **1,587 cases per body** cover every selector/mode byte, unsigned modulus
  boundaries, signed zero/float patterns, all five draws, captured direction,
  live constants, public aliases and guest incoming homes. All 79 words are
  visited. **32 complete caller cases per body** qualify the six-argument ABI.
- **64 connected cases per body** execute original integer RNG 18 words, float
  RNG 25, constructor 248, and memcpy 11. All four baselines are exact. Full 64-bit
  seed updates agree with the independent reference. Actual protected scalar
  and constructor data are used; a synthetic selector registry and the leaf
  selector callbacks/factory remain bounded. **230 constructor words** execute;
  complete coverage of every helper branch is not claimed.
- **Six independent GNU links /39 cases per body** qualify three HI/LO pairs,
  all six call bindings, and the relocated prologue schedule. The alias
  counterexamples use an additional six independently linked images.
- Native32 **O0/O2/O3 each pass 310 cases**, checking all 16 arguments, vector
  and position payloads, public mutations, call order and globals, with trap
  UBSan. All **16 compiled incorrect implementations** fail observably in
  every native profile and in guest tests. Private home cases stay in guest
  checks. No shared helper implementation changed.

Target compile/link/progress and production recount pass. The existing
whole-ROM checksum mismatch still makes `make all` exit 2. Eight focused
checks run freshly in both tools environments before and after installation.
Shared smoke is fresh in both; three unchanged regressions per copy are
reused only by exact helper/test fingerprints, not reported as fresh runs.

Receipts: `conker/build/game-randomized-direction-effect-151B4EA4-match/`.
Tools commit before the consumer pin. Sibling tools retain all 2,434 inherited
dirty paths; host Release stays frozen. Scoped Graphify refresh retains old
unscanned nodes with evidence; it is not full-corpus extraction.

Next: **func_15016170**, measured 80-word unmatched Game slot in game_43620
(77-word routine plus three padding words).
Its source/ABI/callers and matching shape still require fresh qualification
before installation or credit. The 80% goal stays active.

Production ELF SHA-256: `e601a065c74cc9f2a5d09ad85dcdfd8aaad302c545fc00a0697f7ba277719b1e`.

Guard SHA-256: `b336c9bb25157062b67cb9e39b43006d0ed7f2e8ed67cdc70ca13241ef8fded7`.
