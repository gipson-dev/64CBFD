# Note 2474: Private actor/effect binding recovery and retail frame

Date: 2026-11-15. Consumer baseline `71764bb154382070971a29822c70f1e5d669ee51`,
tools baseline `449daf3fb89b6ec4167d7695957d8992cfae4506`.
Continues [Note 2473](2473-game-actor-exit-effects-and-cartridge-check-match-20261115.md).

`func_150C4120` now has a complete private typed sender implementation,
**225 words / frame 0xF0 / 78 differing words**. This is **not installed and
has zero C matching credit**. Production retains its original GLOBAL_ASM.
All **859 frozen production inputs** are unchanged. Actual ELF recount remains
**4,506 / 5,514 total (81.72%)**, Game **3,833 / 4,841 (79.18%)**, Init **492 / 492**,
Debugger **181 / 181**, zero drift, **1,008** still different. At the present
denominator, **181** further matches reach 85%. That goal remains active.

## Scope and recovered records

Owner `conker/src/game/generated_F15D0.c`, VA `0x150C4120..0x150C44A4`,
ROM `0xF15D0..0xF1954`, **900 bytes / 225 words**, no alignment tail.
The private signature is `void func_150C4120(u8 *actor, s16 requestedLifetime,
u8 priority, s32 context)`. Widths follow the original argument-home stores,
signed halfword conversion and priority-byte reloads. The routine reads a
nonnull actor's type byte at +4 and identity byte at +0x3B. The complete
retained wrapper is qualified for effects and arguments; its propagated V0
return is deliberately uncredited pending its surrounding caller contract.

| Record | Bytes | Recovered content |
| --- | ---: | --- |
| Actor binding | 28 | Actor pointer, identity byte, zero fields, type-0x34 selector/state |
| Effect definition | 112 | Flags, lifetime, colors, palette byte, three vectors and coefficients |
| Random parameters | 16 | Four bytes plus scale and two floating-point extents |
| Palette snapshot | 16 | Four words copied before the random draws |

The binding uses selector -1/state 0, or selector 0x54/state 1 for actor type
0x34. A requested lifetime of -1 selects lifetime 300 and clears the active
flag. Other lifetimes retain their signed halfword value and set that flag.
The first constructor receives 28 payload bytes and allocates **68** bytes
including its 0x28-byte prefix. Its original 49-word body qualifies that word's
size role, despite the legacy C helper spelling it as a structure pointer.
That helper's global declaration and implementation are untouched.

After successful allocation, the routine copies the binding into record+0x28.
It copies `D_800A0340` before the first RNG call, uses seven full-width integer
draws and two float draws, and builds the definition. The two extent draws use
separate single-precision multiply/add/multiply steps with factor 0.25 and
scale 700. Three vectors copy `D_800A5480` after the palette-index draw but
before the flag draws. The final coefficient loads after those flag draws.
The second constructor receives a **112-byte** definition and **16** extra
bytes, allocates **184** bytes, and copies the definition at +0x10. The binding
link at primary+0x34 is written even when the effect allocation fails. On
success the random block copies to effect+0xA8.

The inspected alternate `Another Source/CBFD-Recompiled/conker/conker/src/game/game_F15D0.c`
is not imported. It contains an uninitialized stack-base expression, aggregate
copies through undersized pointer locals, word reads at byte fields and a
narrow RNG declaration. Retail instructions and actual helper interfaces are
the authority. Original symbol names remain intact; private records and locals
use descriptive names without inventing retail debug names.

## Compiler recovery

The initial typed candidate emitted 225 words but frame **0x108** and **153**
differences. Register hints and a wider lifetime alone did not reduce that
frame. Removing unnecessary scalar temporaries yielded 227 words/frame **0xE8**;
restoring the lifetime/active temporaries recovered **225 / 0xF0**, initially
with 142 differences. Reading identity immediately after recording the actor
recovered the opening schedule and reduced that to **103**. Placing lifetime
and active declarations above the definition recovers the aggregate stack
locations and reduces it to the selected **78** differences.

The selected raw body SHA-256 is
`9e5f094486ca28d5474da3caaf36efd497a0fc194379cc4cc9a6bf6ef3e0cda2`,
with **23** relocation binding locations. Object-file hashes vary with temporary
source/debug paths; the complete body pin is stable. All five owner neighbors
and normalized pools stay unchanged. The two existing pointer/integer warnings
in `func_150C4B08` / `func_150C4B34` are unchanged after normalizing only source
filenames and line numbers; no new diagnostics or neighbor fixes are hidden.

The first **55 words** match literally. The first discrepancy is word 55,
the saved destination pointer: raw `0xAFA40034`, retail `0xAFA40030`.
Later differences include the first-flag scratch home, register allocation
after the two remainder calculations and the palette/vector/definition store
schedule. Equal word count and frame do not qualify these replacements.
No word guards, insertions, omissions or production profile changes are added.

## Fresh verification and limits

`python3 -m unittest tools.tests.test_game_actor_effect_binding_150c4120_recovery -v`
passes freshly through both the mounted and sibling tools paths. The selected
candidate passes **512 guest cases / two streams** with all 225 retail words
visited. Both original factories (**49 + 61 words**) and original memcpy
(**11 words**) execute in the guest; allocator and zero/RNG providers are
bounded models. This is not a claim that every helper branch was visited or
that the actual RNG implementations are connected.

Cases cover both stack phases, lifetime/priority width boundaries, all first/
second allocation outcomes, actor-type gates and callback mutations of actor,
palette, vectors and coefficients. Seven copied padding bytes remain
uncredited: binding offsets 5..7 and 0x17, definition offsets 0x67/0x6A/0x6B.
All other public bytes, ordered calls and defined packet bytes compare.
Full literal private state, exceptional FP behavior and fired fault-prefix
agreement are not yet claimed.

Native32 passes **512 cases each at O0/O2/O3**, UBSan traps, with **nine effective
controls** per profile: lifetime sentinel, actor selector, random width, extent,
coefficient choice, palette index, effect flags, context and copy length.
Typed native factory models check all arguments and packet fields; they are
not native restorations of those helpers. The sender's actual full C body is
compiled. The original ten-word wrapper `func_1514F568` at VA
`0x1514F568..0x1514F590`, ROM `0x17CA18..0x17CA40`, passes **512 cases / two
streams**, with a wrong-context control. Return-value propagation remains open.

The final complete suite passes in
**41.497 s mounted** and
**47.973 s sibling**.
`make tools-check` passes. The native fixture's earlier negative control
removed the only use of the definition and correctly failed `-Werror`; it was
replaced with a wrong-context call, preserving meaningful typed execution.
No compiler-warning gate was weakened.

## Preservation and checkpoint

All **859** frozen source/header/compiler/layout/guard/object/ELF inputs stay
byte-identical, including all **698** production objects. The production ELF
remains `f6500a14961e2c876619e1491b0245c7b5ec2f81fd7efe43f58ab345ef229939`.
The previous protected-data/image audit therefore remains applicable by exact
image identity; no new production Make or full-image adoption is claimed.
Fresh actual recount agrees with the unchanged root README, which is not edited.
Five documentation indexes receive one concise entry with all old bytes retained.

Tools commit **`de154c556ed11c749e9348c70b06e338833cd0ad`** precedes the consumer documentation/tools-pin commit.
The five-file ignored overlay leaves sibling HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, its **2,434 dirty paths** and status
SHA-256 `a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`
unchanged. Scoped AST refresh covers five new tool files, retains all
**61,892 old IDs**, and records **61,933 nodes /
116,038 links**, zero lost IDs. This is not full-corpus extraction.
No host-port source/build applies; frozen Release is untouched. Nothing is pushed.

Evidence is retained under `conker/build/game-actor-effect-binding-150c4120-private/`:
`production-baseline/`, selected `recovered.c/.o`, reports, native executables,
`raw.s`, `word-differences.json`, the earlier `initial-typed/` archive and the
frame/expression/hybrid/identity/declaration screens. These probes are ignored
workspace artifacts, not additional restored production source.

## Continue here

1. Reproduce the private suite above. Keep the 859-input baseline and all five
   neighbor bodies fixed; retained GLOBAL_ASM remains production authority.
2. Start at word 55 and the destination/first-flag scratch homes (retail SP+0x30
   / SP+0x34). Recover the post-remainder register lifetimes and palette/vector
   store schedule. Inspect `raw.s` and `word-differences.json`; do not treat 78
   differences as two independent scheduling words or install broad guards.
3. Complete the root/wrapper return-use audit. Qualify any proposed normalization
   with complete body/binding pins, precise liveness and seven-padding-byte
   accounting, exceptional FP and fired prefix controls as applicable.
4. Before adoption, require both padders, actual Make, independent strict-image
   prediction with zero exclusions, production audit, installed checks and actual
   recount. Only then update matching/conversion totals and commit source/guards.

Continue this function. The 85% total matching goal stays active.
