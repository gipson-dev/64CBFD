# View leaf/category state restored directly from C

Date: 2026-10-31. Target `func_1510FC34`, owner
`conker/src/game/generated_13BB20.c`, assembly `conker/asm/13BB20.s`.
VA `0x1510FC34..0x1510FD20`, ROM `0x13D0E4..0x13D1D0`.
All 59 words (236 bytes) emit directly from semantic C under O2/g3, MIPS2/O32.
There are no guards, insertions, omissions or alignment words. Its 32-byte frame
saves S0 at SP+24 and RA at SP+28. All 20 named relocation bindings agree.

## Recovered behavior and types

`void func_1510FC34(s32 view)` captures the view-record base, publishes the view
index, and truncates the record's X/Z floats at offsets +0x2F8/+0x300 to signed
32-bit integers. It republishes those integer-valued floats, asks the original
coordinate lookup for a leaf, publishes that pointer, obtains/publishes its
category, and compares the full signed category against the cached signed
16-bit entry. A difference writes its low 16 bits and notifies the view.
After that callback it independently checks the live flag for value 60 and
refreshes the view when equal. Callbacks can change globals; the saved view
argument remains live across them.

The private `ViewRecord` view deliberately contains only `bytes[0x9A0]`.
Typed record-array indexing recovers retail's T6/T7 allocation; flat byte-pointer
multiplication produced a closed nine-word register swap and was rejected.
No unverified record fields or shared-header layout were invented.

`func_1510FD20` has an observed pointer result and two signed coordinate
arguments. Its unfinished zero-return C definition is corrected from `s32` to
`u8 *`, without changing its original three emitted placeholder words. The
forward declaration keeps unspecified parameters to preserve that body. Its
68-word retail implementation is connected in tests; its C body remains
unfinished and receives no new matching credit. The already recovered category
walker `func_1510FE30` is unchanged.

## Measured qualification

| Check | Evidence |
| --- | --- |
| Direct compiler/slot words | 59 / 59; 20 named bindings; zero guards |
| Raw compiler body SHA-256 | `370af315e800cc6cfc5ab7aea6e3d93b300bb5ca3d590f0bdd89b5e67429db91` |
| Complete owner | All 13 other routines and pools unchanged |
| Actual Make | Five commands reproduce the qualified object; no target-owner diagnostics |
| Guest | 1,152 cases / 4,608 executions at three independent code/data layouts |
| Guest coverage/order | All 59 words; six aliases; 57 access-prefix cases, including six delay-slot cuts |
| Native32 | 65,536 cases each at O0/O2/O3; UBSan trapping; ten effective controls |
| Native state | Four view slots, all 256 callback modes, public state and provider logs, cached-array canaries and periodic record-byte checks |
| Original helpers | 1,536 cases / 6,144 executions using the 68-word leaf lookup and 25-word category walker |
| Helper coverage | 62 lookup words and 23 category words visited across null, leaf and branch trees, including signed relative offsets |
| Original caller | 192 cases / 768 executions; 14 original words; four ignored-return poisons |
| Canonical checks | Eight fresh methods pass independently in both tools copies; both shared tools checks pass |
| Installed checks | Two fresh methods in each copy; six unchanged semantic checks reused only under complete module/input/artifact fingerprint equality |

Native controls detect wrong coordinate offsets, untruncated float publication,
narrowed category comparisons, reversed cache gating, wrong cache indexing,
missing leaf publication, wrong refresh gating, wrong notification arguments,
and a flag captured before callbacks. Each exits through semantic mismatch.
Guest aliases/access-prefix checks describe emitted instruction behavior;
native cases use finite, valid f32-to-s32 conversions. Hardware FCSR behavior,
portable C alias guarantees, complete spatial-tree coverage and gameplay are
not claimed.

The aligned retail census finds one JAL at ROM `0x466F0`/VA `0x15019240`, in
`func_15019130`, and no aligned literal target pointers. Its original bounded
window `0x15019228..0x15019260` starts at view zero, skips a negative maximum,
and calls through the live inclusive maximum in `D_80082FA0`. It saves A0 in
the JAL delay slot and reloads it after return. Tests prove the return is
ignored and cover growing/shrinking bounds. This is bounded caller evidence,
not complete parent-function or gameplay acceptance.

## Linked image and production

The independent full ELF prediction has zero exclusions. Exactly 203 bytes
change: 198 target code bytes, one function-size byte and four symbol metadata
bytes. The sole metadata permutation swaps the closed adjacent named group
`D_800DBDD0`, `D_800DBDD8` at symbol-table offset `0x2B52A4`, order `(1,0)`.
Original names, fields and string-block contents are checked before prediction.
All other 6,055 function bodies and every function address remain unchanged.
Protected Game data is exact: 189,088 bytes across 720 owners.

A production preservation guard stopped after Make also regenerated
`sinf.c.o` and `debugger_258ED0.c.o`. A section-level audit proves that only
`.mdebug` differs; `.text`, relocations, symbol/string tables, register info and
options are byte-identical. Both regenerated objects and their frozen versions
are retained. The frozen objects were replayed only after that audit, followed
by a successful Make relink, strict image audit and installed checks. The first
and final Make-produced ELFs both equal the independent prediction; no loaded
or symbol bytes are excluded.

Adopted ELF SHA-256:
`c5097966846c828929e45c2f7697ec3a0e186734d0e571b4484a26fbf1ddf8ba`.
The actual adopted Native ELF was streamed back for recount and disassembled
independently. The existing C inventory and inherited guard manifest are unchanged.

## Banking and continuation

Tools commit: `ca2b7f38f4bf6ffa7ee6af64132614ddfefa3e95`, committed before the consumer source/pin/documents.
Primary tools and consumer are clean after banking; the independently dirty
older tools mirror is preserved and is not committed. No push is authorized.

Accepted total **3,983 / 5,506 (72.34%)**; Game **3,310 / 4,833 (68.49%)**;
Init 492/492 and Debugger 181/181; zero address drift and 1,523 still different.
The 75% threshold remains 4,130 exact C functions, so **147** further matches
are needed. Next queued screen: `func_1507BB28`. The full 75% goal remains active.

The private `func_151AE2BC` interpolation study remains uncredited and is
preserved under `conker/build/game-path-height-progress-151AE2BC-match/`.
Its rejected compiler experiments are retained in a verified compressed archive.
Do not repeat its broad register/declaration sweeps without a new hypothesis.

Reproduction artifacts and handoff:
`conker/build/game-view-leaf-category-1510FC34-match/`.
Canonical modules: `tools/experiments/game_view_leaf_category_match.py`,
`tools/tests/game_view_leaf_category_oracle.py`, and
`tools/tests/test_game_view_leaf_category_match.py`.
Run `python3 -m unittest tools.tests.test_game_view_leaf_category_match -v`
from the prepared consumer checkout. Historical qualification relies on the
retained target build artifacts; restore archived checkpoints when required.
