# Barrier Crossing Semantic Audit And Matching Boundary

Date: 2026-10-19

Matching status is superseded by [Note1603](1603-barrier-crossing-complete-match-20261019.md),
which installs all207 exact words. The measurements below describe this earlier audit.

## Baseline And Scope

Continue existing C `func_15086D94`, owner `generated_B3020`, after installed
Note1601. VA15086D94..150870D0, ROM B4244..B4580,207 words/828 bytes. The
**retail frame is144; installed C actually emits128**, despite the same207-word
length. Its102 real word differences are not merely an optimization-profile
choice. The initial isolated body is identical under normal/no-unroll profiles
and reproduces the installed target's complete linked words.

Consumer baseline f85ac854, tools baseline d3b35eb. New tools checkpoint
**5829d1a** is committed before this consumer's pin; no push. No production C,
guard, Makefile, assembly, progress CSV or ELF change is installed here.

```text
Source: 55493079cdf8df8d1e59d06e0ccfd9fb983798529ff6c2a91dfb5b788760be74
Make:   6e6563d792c110f74f44d615c62f04e87430aa0c0e44b1bd7817ffd6d91a8063
Guards: 1511ad9a4d25fd2dd8835143b187edc5c224ec6e89272eb4c5a8b45a074a8043
ELF:    ac9821636fcdf152a879c87120645fbc265991065a2b2568e545fc0126dd14ba
CSV:    16798cbd1f7d69f7ecdd8b7e0071ba9ea975a50652bd8797673d1ec2b500c9be
```

## Observed Contract

The function accepts five floats `(x,y,z,dx,dz)` and returns F0. Callers supply
F12/F14, the z/dx bit patterns in A2/A3, and dz at incomingSP+10. Four direct
assembly call sites are15085EE4,15086000,1508C4E0 and1509A810. These interfaces
were inspected; their complete caller workflows are not qualified here.

The height helper executes before count/node-pointer capture. The outer count
is signed16 and stays cached in S1. Nodes have16-byte stride, signed16 X/Z
at0/4, first-node category byte6, five neighbor bytes9..13 and type byte14.
Both endpoint types must equal1. Only the first node's category is checked.
Neighbor255 skips a slot rather than terminating the list; `i<neighbor` filters
duplicate directions, but there is no `neighbor<count` clamp.

The initial line crossing uses ordered sign tests, including zero on the
nonnegative side. The tangent projection excludes the first endpoint and
includes the second. Preserve the signed coordinate interpretation and exact
float32 operation grouping.

**Return the last crossing fraction, not the minimum or last accepted one.**
The retail private fraction is not initialized; it becomes defined on every
line sign crossing before the edge-span acceptance test. An earlier accepted
fraction0.5 followed by a rejected0.75 crossing returns15 for a20-unit move,
not the minimum distance10. Native positive-return paths in these fixtures
define the C fraction; no portable C private-poison or NaN-payload claim is made.

The actual20-word height helper looks up a category byte at D_800D237C after
its threshold scan; its result is not simply the threshold ordinal. Connected
tests supply backed thresholds and nonidentity category mapping. A positive
infinite y would walk beyond the supplied infinite sentinel and is excluded
from that connected-helper corpus; opaque-provider nonfinite tests are separate.

## Compiler Boundary

`game_barrier_crossing_candidates` freezes the exact installed inputs and
screens count caching, coordinate captures, expression/declaration order and
assignment lifetimes. No dummy local, volatile qualifier, physical-register
binding or production guard is added.

```text
Initial:           207 words / frame128 /102 differences
Start-first:       207 words / frame144 / 97 differences
Selected aliasing: 207 words / frame144 / 68 differences
```

`selected_body()` reproduces the measured `absolute-first` assignment form.
Raw SHA256:5ced5ffdcdffbf7d558c66534c3d350bb2f69c075f039c436fee68d72d0e3f98.
Both copied owner profiles emit that same target payload and all five bindings.
This is an uninstalled, still-nonmatching candidate, not a new byte-exact match.

The first literal private difference is **fired access12**, the minimum's
initial store: retail writes frameSP+50/incomingSP-64; selected writes
frameSP+58/incomingSP-56. All prior literal memory/GP/FP state agrees. Thirteen
successively fired cut pairs establish that boundary. Matching frame/length
therefore does not establish private-state identity. FP roles and scheduling,
including the rotated-normal copy and later projection operations, remain open.

## Fresh Qualification

Seven tests pass in12.766s:

- 105 fixtures,630 completed guest runs across retail/initial/selected and two
  stack phases. Finite return bits, NaN classification, public memory, helper
  arguments and saved GP/FP/SP/RA lifetime agree.
- Six native32 O0/O2/O3 runs with UBSan and nine effective negatives: returning
  the minimum, clamping neighbors, nonzero-type gates, truncated category,
  second-category filtering, either endpoint inequality, unsigned coordinates
  and stopping at255. The corpus preserves post-helper count/pointer/field
  mutations and the last rejected-crossing counterexample.
- 66 connected actual-height runs visit all20 helper words. These execute real
  instructions against explicitly supplied tables, not retail level-data or
  complete gameplay acceptance.
- 198/207 target words visited. The unvisited offsets270,274,278,27C,280,284,
  288,28C,290 are in the negative endpoint-projection tail. Do not claim full
  instruction coverage or infer those words can be removed.
- Both copied owner profiles preserve all72 neighbors and relocation-owned
  pools. The actual padder retains both existing normal overrides, all73
  addresses/extents and every non-target owner byte. No new guards. The padded
  target deliberately retains its68 differences and fails exact-match credit.

Shared `make tools-check` and Python syntax checks in both local tools copies
pass. Only three absent task files were copied to the older standalone mirror.
Its HEAD ddbdd16 and all1,392 pre-existing dirty leaf hashes remain unchanged;
no mirror commit/reset/stash/clean. Original source/Make/guard/ELF/CSV fingerprints
are verified, and fresh matching remains **Game3011/4832 (62.31%)**,
**total3684/5505 (66.92%)**,1,821 different/zero drift. Init492/492 and
Debugger181/181 stay exact. Owner63/73 exact; conversion5505/6044 unchanged.
Root README is unchanged. No host/frozen Release operation, dependency change,
REA setup, Claude call or save operation was involved.

## Resume

1. Keep this function as the target. Resolve minimum home SP+50 first with
   frame144 and207-word extent preserved; do not treat the passing public
   fixtures as permission to replace arbitrary instructions.
2. Recover the FP lifetimes/rotated-normal copy and dependency schedule from
   the complete original assembly. Retain the last-crossing return quirk and
   all five relocation bindings. Keep count-caching/source-shape screens
   separate from confirmed retail code.
3. Require complete word matching and private/fault, alias, actual caller,
   independent GNU rebase, actual Make/padder and strict whole-image gates
   before production installation or aggregate credit. Wider Game work remains
   active; neither this recovery nor frame agreement completes the function.

```sh
python3 -m tools.experiments.game_barrier_crossing_candidates --lifetimes
python3 -m tools.experiments.game_barrier_crossing_candidates --assignments
python3 -m unittest tools.tests.test_game_barrier_crossing_recovery -v
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Frozen inputs, compiler variants, qualification receipts, copied/padded owners
and local graph snapshot/audit belong under ignored
`conker/build/game-barrier-crossing/`. Post-commit graph maintenance is separate
from byte-match evidence.
