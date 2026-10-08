# Game Zone Neighbor Selection Recovery

Date: 2026-10-06. Starting checkpoint: `ba88f6f4`.

Recover `func_1508B3F8`'s complete queued-zone/player selection body in
[generated_B3020.c](../../conker/src/game/generated_B3020.c), replacing its
false zero-return placeholder. Retail occupies **369 words / 1476 bytes**,
0x1508B3F8..0x1508B9BC, ROM 0xB88A8..0xB8E6C.

This is **semantic recovery, not a new byte match**. The installed complete C
body emits **367 words**, followed by two ordinary slot-padding nops, with
the correct **0x140 frame**. **340 real aligned-slot differences remain**.
No new guards, compiler override, overflow, insertion/omission or assembly edit.
The matching goal remains active.

## Retail Contract

- Cache the state allocation's selection array at +0x55C and queued-zone cursor
  at +0x1748. For signed D_8008FD8C players, replace every selection except -1
  with -2. The first/last reset loops retain fresh count reads after stores.
- Process the signed-byte queue count at state +0x1745. Each 12-byte zone holds
  its already-squared radius at +0 and signed-halfword XYZ at +4/+6/+8.
  Copy that radius directly into the visitor query's threshold; do not square
  it again.
- Start actor iteration at signed-byte D_8008FD90, with stride 0x32C. Strict
  height gates are `-100 < actorY - zoneY < 200`. The strict radial gate is
  `(actorX-zoneX)^2 + (actorZ-zoneZ)^2 < threshold + 100`.
  Equality and unordered floating comparisons fail these actor gates.
- For each eligible actor, initialize best ID to 255 and load D_8009DA5C as
  the distance minimum before the first helper call. Build one query per zone,
  at the first eligible actor, and reuse it for later eligible actors.
- Call height-band lookup with Y, then root lookup with XYZ, mode zero and the
  returned band as its fifth stack argument. Only return -1 suppresses visiting;
  other values are narrowed to a byte, including 255 and high-bit returns.
  Initialize count, clear exactly 32 visited bytes, then execute the complete
  connected `func_1508B2A8` visitor from [Note 1021](1021-game-record-neighbor-visitor-match-20261006.md).
- Scan the resulting signed count only when positive. Preserve the remainder-
  first/four-candidate shape. Each candidate's actor-relative X/Z squared
  distance must be strictly below both its zone-relative stored distance and
  the current minimum. Equal minima retain the first winner.
- A winning ID of 255 still suppresses publication. For another winner, load
  the table afresh, write state +0x5C + player*4 to one only if the old selection
  is not -2, and publish **node byte +7**, not the node ID. There is no comparison
  between old and new labels before writing the flag.
- After all zones, replace negative selections with -1 and clear the queue
  count through the current state global. Cached zone/selection cursors remain
  in the original allocation when an opaque helper replaces the state global;
  fresh flag writes, bounds and final queue clear use the replacement.

The shared private query layout is unchanged: 88 aligned bytes, with count
+0x2C, IDs +0x2E, distances +0x0C and visited flags +0x36. Biased byte cursors
stay within that allocation and retain the four-candidate scan without adding
an abstraction or enlarging the query. All nine saved GPRs/FP and six saved
FPR pairs are retained in the retail frame. Their allocation/live intervals
and the private query homes are not yet instruction-exact.

## Compiler Screen

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_zone_neighbor_selection_candidates.py)
freezes the straightforward indexed recovery independently of production.
**29 source forms / 58 profile controls** complete with empty diagnostics.
The existing generated_B3020 no-unroll profile remains unchanged.

| Form / Profile | Body Words | Frame | Real Differences |
| --- | ---: | ---: | ---: |
| Indexed / existing no-unroll | 249 | 0x138 | 333 |
| Indexed / default unrolling | 336 | 0x148 | 349 |
| Explicit four candidates / no-unroll | 371 | 0x140 | 323 |
| Remainder/pointer-end with Z reuse / no-unroll | 370 | 0x140 | 257 |
| Biased byte cursors / no-unroll (installed) | 367 | 0x140 | 340 |
| Installed form / default unrolling | 424 | 0x140 | 393 |

Splitting the height call, narrowing best, query declaration order, cached actor
coordinates and divide-by-one address controls do not close the match. The
370-word form has the lowest measured raw score here but exceeds the slot by
one word; it is retained as a next matching candidate, not installed through
an overflow or normalized by arbitrary omission. Default unrolling also
exceeds the slot for the selected manual-loop form and is not enabled.

Raw scores include length differences. A fitting semantic form is not evidence
that its stack/register schedule matches retail; do not check this function
off as byte-exact.

## Helper ABI Boundary

[functions.h](../../conker/include/functions.h) adds the parent's `void(void)`
prototype. The root lookup's existing placeholder definition now declares the
caller's three float and two integer argument positions, allowing the correct
O32 float-register/fifth-stack-word call. Retail lookup narrows mode/band to
signed bytes internally; recovering that body remains separate work.

**func_15085DF8 still returns zero and is not semantically recovered.** IDO g3
adds exactly four argument homes at caller SP +0/+4/+8/+0xC: F12, F14, A2 and A3.
The previous three-word zero-return sequence follows unchanged; four fewer
padding words preserve its complete 168-word slot. A linked-prefix and two-
stack-phase instruction test binds the homes, store order and zero result.
This is a related ABI change, not an unchanged-helper-byte claim.

Qualification models height/root lookup and bzero at bounded opaque boundaries,
clobbering caller-saved GPRs and FPRs. The recursive visitor itself is real
connected retail code. Do not treat this body recovery as qualification of the
full production lookup/caller/gameplay chain or a PC-port transplant.

## Qualification And Linked Audit

[Qualification tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_zone_neighbor_selection_match.py)
pass **14 tests in 68.607 seconds**, no skips, against the final installed build.
The tests
compare retail, the installed source shape and the independently frozen indexed
body against an independent float32/reference traversal. The fixtures verify
complete non-stack memory, ordered external writes and ordered calls; they do
**not** establish universal equality of optimized external read histories.

- **2990 three-way guest cases** cover signed player/start/queue bounds,
  strict/equality/NaN/infinity gates, root failure and byte narrowing, all
  candidate counts 1..8, remainder/four-way scans, ties and publication.
- Root-helper mutations cover future actor/count/queue/minimum/selection/node
  state. Eighteen replacement-base cases bind retained old cursors versus fresh
  state/table globals. Negative-start fixtures are guest address tests, not
  claims of strict-C/native array portability.
- Dedicated scan fixtures cover **369/369 parent words** and **84/84 visitor
  words**, including visited-bit suppression and the final quad winner update.
- **1424 source-extracted 32-bit native footprints** compare complete state,
  actor and node storage, globals and an ordered call digest against independent
  references. Includes 128 wide-query fixtures with all candidate counts.
- Compiled repeat-query, missing-queue-clear and inclusive-distance negative
  controls fail the retail contract. Compiler inventory/fit/profile, installed
  source/prototype/slot, no overflow/no guards and lookup homes are asserted.
- The shared TriangleOracle gains BLEZL/BGTZL support. Eight focused sign/delay
  probes bind both taken execution and non-taken annulment. Signed-byte load
  support is local to this parent fixture; no broad emulator claim.

All **60 shared-oracle regression tests pass in 257.150 seconds**, no skips:
triangle transform, actor context dispatch, position/radius append, record
neighbor visitor, dispatcher matching and native dispatch. An initial run hit
the ELF during relinking; it was rerun after the successful terminal build.
The historical full corpus is not rerun wholesale.

Fresh ELF/progress/match-progress targets succeed. Existing unrelated warnings
appear during the broad header rebuild; this is not a warning-free build.
The complete **6059-slot audit** retains every symbol, address and length.
Exactly two slots change: the recovered parent and the proven four-home prefix
of the still-placeholder lookup. Every other slot is byte-for-byte unchanged.

Parent slot SHA-256:
`d989cb56f2ca88212baf6057c723eb7da47f9796700150201a6892d8f211d6f5`.
Lookup stub slot SHA-256:
`23cf17e7c08e18784128e51544026d3077405872fc8b37df1320bd7b41680d76`.
Ignored before/after/audit receipts live in
`conker/build/game-zone-neighbor-selection-test/`; the 58-control inventory is
`conker/build/game-zone-neighbor-selection/screen.json`.

Init **164048 bytes**, Init data/rodata **17376 bytes**, Debugger **19800 bytes**
and Game data **189088 bytes / 720 owners** remain retail-exact. All **10643 CSV
guard rows** are unchanged. No data ownership or emitter/padding rule is relaxed.

Exact totals remain **3308/5462 (60.56%)**, Game **2635/4789 (55.02%)**, Init
**492/492**, Debugger **181/181**, zero address drift and **2154 different Game C**.
Conversion counts are unchanged because the old placeholder already counted
as C. README aggregates/date remain accurate and are not inflated by this recovery.

`make tools-check`, whitespace and **3019 relative links** across nine
current/working documents pass; zero broken links.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_zone_neighbor_selection_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_zone_neighbor_selection_match -q -f
wsl python3 -m unittest tools.tests.test_game_actor_triangle_transform_match tools.tests.test_game_actor_context_dispatch_match tools.tests.test_game_position_radius_append_match tools.tests.test_game_record_neighbor_visit_match tools.tests.test_game_record_dispatch_match tools.tests.test_game_record_dispatch -q -f
wsl make tools-check
git diff --check
```

Run the linked-image tests after the build finishes, not during ELF replacement.
Next recover this parent's private query/selection/counter homes and constant-
address register lifetimes; the retained 370-word form needs one word removed
through real source shape, then remaining allocation/scheduling work. The lookup
body is a separate remaining semantic gap, not a reason to count the parent as
matched. The triangle boundary from [Note 1017](1017-game-actor-triangle-cached-iterator-audit-20261005.md)
also remains open.

No sibling source/build/save/frozen Release change, host transplant or push.
The full Game matching goal remains active.
