# Paired Scrolling Tile Windows Direct Match

Date: 2026-10-17

Continue consumer **e7c4e714**, tools **72f748d**, after the fade audit in
[Note 1481](1481-overlay-fade-packet-recovery-and-reload-gap-20261017.md).
Install **func_150CF5E8** directly from semantic SDK C. All **38 words**
match retail with no instruction guards, compiler profile or pool changes.
The separate fade constructor remains original assembly and receives no credit.

## Complete Recovered Routine

- Owner: `conker/src/game/generated_FC5F0.c`.
- Original: `conker/asm/FC5F0.s`.
- VA **0x150CF5E8..0x150CF680**, ROM **0xFCA98..0xFCB30**.
- **38 words / 152 bytes**, no frame, helper call or floating operation.
- Proper interface **Gfx *(Gfx *commands)**, matching the recovered dispatcher
  declaration. Replace the false zero-return placeholder; retain its address
  symbol and add one succinct texture-window comment.

Emit two gDPSetTileSize commands, for tiles 0 and 1. The respective upper-left
S/T coordinates come from D_80088890/D_80088894 and D_80088898/D_8008889C,
shifted arithmetically by seven and masked to twelve bits by the SDK macro.
Both lower-right coordinates are **0x47E**. Advance exactly two Gfx entries
and return the advanced pointer. Add the missing signed D_8008889C declaration.

Keep the second pair of coordinate reads after the first command stores.
Guest output/global aliases prove those late reads observe changed storage;
do not cache all four values before emitting. Native tests use valid distinct
Gfx/global objects, not a portable-C claim about those guest aliases.

Raw target SHA-256:
`5e376248f17483071efebaf43bfbc4ceb287b94da2fe4aace524549da1005da0`.
All **eight HI16/LO16 bindings / four anchors** are pinned. The normal padder
preserves the complete direct match, all **24 raw/padded owner neighbors**
and all owner pools. No caller source, original assembly or build rule changes.

## Qualification

All **eight final installed tests pass in 38.987s**:

- **1,974 three-way guest cases**, original/raw-C/padded-C: independent
  reference, all memory, exact read/store order, return pointer, saved and
  modeled private state, both stack phases and all 38 natural words.
- **384 native32 cases per O2/O0 profile**, full SDK body and separately
  compiled typed caller, UBSan, both aligned output positions, boundary and
  generated coordinate words, complete command canaries and preserved globals.
  All eight effective controls exit 22, not a signal or sanitizer trap.
- Three independent original/C rebase pairs, all four anchors, signed low
  carries and shared storage. All 38 words compare equal in each pair;
  **672 state cases** execute the identical linked words.
- **112 three-way positively fired fault prefixes**, all eight memory accesses
  across seven aliases and both stack phases: 336 fired instances with full
  modeled equality. Not portable C faults, CP0/FCSR or hardware timing proof.
- **168 three-way original caller cases**, actual call/delay/consumer windows
  at 0x1510BB7C, 0x1510BDD8 and 0x15113B70, executing the complete leaf.
  The A0 delay-slot transfer and advanced V0/S0 consumer behavior are checked.
  These are not the complete larger dispatchers or natural gameplay.
- All 38 target-word controls, nine binding controls and **178 protected input
  entries / 165 distinct paths** reject corruption. The corruption fixture is
  cached only within injection tests; all live inputs are re-read afterwards.
- First complete source/image prediction, exact function-size-only symbol
  change, whole data audit and ten strict successor/fixture corruption controls.

The seven fade tests plus two reset image/successor checks pass freshly in
**54.048s**. A downstream mirrored-renderer candidate/context check also passes
in **5.319s**. They use only the exact recognized tile successor to validate
their preserved predecessor fixtures; they do not claim the entire current
ELF is unchanged. Other renderer/compiler suites are prior evidence, not fresh
broad regressions. No renderer or fade matching credit is added.

## First Whole Image

Before editing production, freeze the source, normal owner object, link script
and all inputs. Reproduce the entire baseline ELF, then prelink the complete
qualified SDK candidate. Independently predict only its original 152-byte
slot and the symbol extent change from 12 to 152 bytes. Freeze the first
complete prediction before installation, with no metadata exclusions.

The normal rebuilt ELF equals that prediction exactly:

- **127 target instruction bytes**, **one function-size byte**, **128 total**.
- No symbol/string permutation, data change or excluded metadata.
- No other function body, address or extent changes.
- Game data remains **189,088 bytes / 720 owners / zero differences**.
- Guards, compiler profile, Makefile, retail layout and conversion CSV are
  unchanged. This was already counted as nominal C, despite being a stub.

ELF SHA-256:
`db9a07f4e5fc3278dfbb357c401fe5d314653f40b41bced82425a32a8c3ba58c`.
Owner SHA-256:
`d4862cd0a6f2803bbdc8da758cbde092ed8e437846b96532fc55f09d1e66b21f`.
Only these two exact successors and their verified before/after fixtures are
recognized by the adapter. Unknown current bytes still fail closed.

## Fade Compiler Follow-Up

The owned, fingerprint-locked capture of func_15182670 completes CFE, UOPT,
UGEN, assembler and driver with exit 0. Its isolated body reproduces the full
owner's exact **53-word** raw target, bindings and code. No compiler is changed.
Local source, scripts, captures and decoded records remain under ignored
`conker/build/game-overlay-fade/duration-selected/`.

CFE contains **three LOD J/P, length 2, offset 18 (0x12)** records for duration.
The observed UOPT output still contains **all three**, and adds a VREG record
for that same halfword. UGEN ultimately emits **one LH**. Thus the reduction
occurs after the observed UOPT stream, not by CFE/UOPT deleting two LODs.
This places further investigation at backend virtual-register residency;
it does not establish the original source or an independently proven cause.

Byte-pointer, byte-cast and packet-union shapes remain the same 53 words.
Word/unsigned/sign-roundtrip forms can produce 54 words, but add a private
SP+0x30 spill and reload the wrong home instead of retail's three incoming
LHs. Typed-prototype and register-hint variants do not fix the gap. Debug
profile comparisons likewise fail; g1/g2 explicitly report no optimization.
Do not install any of these or disguise the difference with volatile/guards.

## Progress And Bank

Fresh official matching: Game **2,949/4,828 (61.08%)**, total
**3,622/5,501 (65.84%)**, still different **1,879**, zero address drift.
Init **492/492** and Debugger **181/181** remain exact. Nominal conversion
counts/bytes stay unchanged. Root README receives only its two aggregate rows.

Tools **6737b65** banks six new files and four narrow predecessor/test updates
first. Ten exact task pairs and **20 ASCII/AST checks** pass across both copies.
Eleven shared padder checks pass per copy: active **0.024s + 0.031s**, mirror
**0.018s + 0.029s**. Consumer tools-check passes.

Preserve standalone mirror HEAD **ddbdd16b** and **1,037 unrelated initial
dirty-file hashes**. Update only four exact-predecessor task files and add
six files, for **1,047 dirty paths**. No mirror commit/reset, push, extra
agent, dependency/provider change or host/frozen Release action. Existing
duplicate Makefile recipe warnings remain. Compiler scratch is disposable;
diagnostic driver paths must remain relative to avoid IDO's space truncation.

Prepared-checkout checks, sequentially:

```sh
python3 -m tools.experiments.game_scrolling_tile_installation
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_scrolling_tile_windows -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

- [x] Replace the placeholder with the complete 38-word direct SDK routine.
- [x] Qualify live reads, aliases, typed caller, actual call sites and whole ELF.
- [x] Locate the fade load-reduction boundary without granting it C credit.
- [ ] Recover neighboring **func_150CF680**, **96 words / frame 0x98**,
  including its full constructor argument block and actual 16-byte copy.
- [ ] Keep the 54-word fade, 633-word renderer, deferred pulse lifetime and
  wider Game/additional-source queue open; natural gameplay remains separate.
