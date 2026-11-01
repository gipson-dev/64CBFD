# Polygon plane clipping restored directly from C

`func_15185DD4` now emits all **84 words and four table-address relocation
bindings directly from C**, with its original 56-byte frame and no guards,
insertions, omissions or trailing alignment words. It reuses `ClipVertex`
and declares typed classifier/interpolator pointers for the two existing
callback tables. The recovered interface is
`ClipVertex *func_15185DD4(ClipVertex *vertices, s32 count, u32 plane,
ClipVertex *out)`.

Production Make and an independent Windows-consumer ELF recount establish
**4,008/5,506 (72.79%)** exact C functions, Game **3,335/4,833 (69.00%)**,
zero drift and 1,498 still different. Init remains 492/492 and Debugger
181/181. The guard and conversion-inventory CSVs are unchanged. The active
75% target is 4,130/5,506: **122 more matches** remain.

## Behavior and source recovery

VA 0x15185DD4..0x15185F24; ROM 0x1B3284..0x1B33D4. The routine captures
`D_8008D498[plane]` and `D_8008D4C0[plane]` before the loop. Starting with
the last input vertex as previous, it classifies each current/previous pair,
inserts a crossing when classifications differ, copies each retained current
vertex as five words, and returns the final output cursor. Both interpolation
paths consume the callback's returned cursor rather than assuming a fixed
advance. The whole 20-byte copy includes the two retained vertex bytes.

The previous address uses explicit unsigned word arithmetic:
`count*sizeof(ClipVertex) + vertices - sizeof(ClipVertex)`. This preserves the
guest address calculation for nonpositive counts without forming an out-of-
array C pointer through subtraction; it is qualified for the 32-bit target
and native32 harness. Nonpositive counts still load both callback pointers
but never access a vertex or call a callback. Plane indices are caller-supplied
table indices; qualification covers all ten valid entries, not invalid indices.

The first semantic candidate had the correct 84-word length and frame but
five differences. Reversing the commutative address-add operand order recovers
one word. Assigning the current pointer after the two callback loads recovers
four opening scheduling words and the original LO16 positions. Together these
natural C changes match the entire routine without normalization.

## All ten callback contracts

The interpolation/classification tables contain ten entries and 18 distinct
original routines. Their predicates are:

| Index | Original predicate | Interpolation routine |
| --- | --- | --- |
| 0 | Y>Z | `func_15185454` |
| 1 | X<-Z | `func_1518557C` |
| 2 | Y<-Z | `func_151856A8` |
| 3 | X>Z | `func_151857DC` |
| 4 | Z>`D_800D3688` | `func_151858FC` |
| 5 | Z<`D_800D368C` | `func_15185A28` |
| 6 | X<=0 | `func_15185B54` |
| 7 | X>0 | `func_15185B54` |
| 8 | Y>0 | `func_15185C6C` |
| 9 | Y<=0 | `func_15185C6C` |

All interpolation entries take previous/current/output vertex pointers and
return the next output cursor. An independent rounded reference models the
actual plane equations and original coordinate constraints, including forced
equal/opposite coordinates and the two live depth constants. The guest suite
executes all 18 original routines without service models: **608/608 callback
words and 84/84 parent words** are reached.

There are 200 root cases / 400 executions across all ten entries, both stack
phases, polygon transitions, empty counts and twenty sparse negative-count
cases including INT_MIN. The sparse cases have no input-vertex mapping and
still return correctly. Complete output bytes, calls, cursor and saved
GPR/FPR/SP state agree. Callback arithmetic is tested in a finite domain with
representable conversions; hardware FCSR/invalid-conversion behavior is not
claimed.

Four original JALs occur at ROM 0x1B361C,0x1B36C8,0x1B377C,0x1B37DC in
`func_15185F24`; no aligned literal pointer is found. Their call/return windows
start at VA 0x1518616C,0x15186218,0x151862CC,0x1518632C and contain
11,7,6,7 static words respectively. Seventy-two cases / 144 executions verify
that each returned cursor is reduced to an output count by division by 20,
with the original counter advances and stores where present. Pre-call argument
and saved-register state are explicitly supplied to these bounded windows.
The entire outer caller and natural reachability through its earlier setup
are not claimed as executed or recovered.

There are 176 fired access-prefix cases, two independently linked code/table
placements with signed-low16 carry boundaries and 40 rebased executions,
plus three in-place whole-copy cases with all vertices retained. These do
not claim arbitrary overlapping-buffer clipping or portable C fault behavior.

## Native callback and mutation checks

Native32 validates the parent C control flow using typed callback contracts,
separate from the guest suite's original geometric callbacks. O0/O2/O3 each
pass **880 cases under UBSan**, checking all input/output bytes, canaries,
event order and argument identities. All ten table selections are exercised.

Cases include signed nonzero predicate returns, negative/empty counts,
callback cursors that advance by two vertices, and writable test-table
mutations during the first classifier call. The correct body retains its
captured callbacks after those mutations. Production table data is unchanged.

Eight compiled controls are effective: wrong polygon closure, a wrong negative-
count result, positive-only predicate interpretation, reversed interpolation
endpoints, ignored callback cursor, a shortened vertex copy, classifier-table
reloads and interpolator-table reloads. Obsolete local declarations were removed
from the two reload controls so the negative programs compile under the normal
warning-as-error harness; no warning flags were weakened.

## Owner, full image and banking

Complete-owner compilation and the actual normal three-command Make recipe
reproduce the independently padded object with no owner diagnostics. All 31
neighbors and pools remain fixed, including both restored axis helpers. The
full build retains the pre-existing duplicate `generated_12D630` recipe
warning; a warning-free full build is not claimed.

The initial literal image predictor exposed ten metadata bytes: adjacent
`D_8008D4C0`/`D_80088740` symbol records and their equal-length strings swap
serialization order. The predictor validates the exact named records and
string offsets, then models this closed permutation. It does not exclude
metadata. The final prediction and production ELF agree literally across
all **283 changed bytes**, including the ten metadata bytes and target extent
12->336. Every address and all 6,055 other linked bodies remain fixed.
Protected Game data is exact across 189,088 bytes and 720 owners.

The full 17,419-file predecessor seal has only the expected target source,
target object and ELF differences, with no unplanned dependent-object changes.
Seven fresh target tests pass in both tools copies, both shared checks pass,
and the installed production suite passes. Tools `f7e5208` are committed before
the consumer pin. The older mirror's inherited changes are preserved and are
not committed. Nothing is pushed.

Production ELF SHA-256:
`34e824ea6d29f33b9763fce7f1ac1703aa2894414fadc6092754e80c6144a456`.

With prepared inputs and the retained target stage:

```sh
python3 -m unittest tools.tests.test_game_polygon_plane_clip_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-polygon-plane-clip-15185DD4-match`. Key receipts are
`preparation.json`, `runtime-qualification-v10.json`, `production-v17.json`,
`production-seal-changes-v17.json`, `installed-audit.json` and
`native-production-recount.txt`. Current Native/cache seals and the final
banking proof are retained there. Scoped Graphify refresh preserves prior
valid nodes and edge occurrences, archives obsolete stub return relationships,
and makes no full-corpus extraction or global reclustering claim.

Next screen: `func_151857DC`, the 62-word X=Z interpolation entry at table
index 3. Reuse the qualified vertex/callback contracts while checking its
specific arithmetic order and original root behavior. Existing private
candidates remain uncredited.
