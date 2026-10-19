# Neighbor Row Builder Frame And Quad Loops

Date: 2026-10-19

## Checkpoint

Continue `func_1508A1BC`, VA1508A1BC..1508A6FC, ROM B766C..B7BAC,
from [Note1610](1610-neighbor-row-builder-recovery-and-private-boundary-20261019.md).
Consumer predecessor8aa8da98 and tools predecessor5b33fbe were clean.
Tools **f0db953** is committed before this consumer documentation/pin update.
The wider Game goal remains open; no push or host/frozen Release operation.

Recover the retail **168-byte frame directly from C**, without dummy storage,
volatile, physical-register bindings, a frame patch or a new compiler profile.
Inline the two temporary actor-address locals, preserve the integer-address
null test, and spell out the disabled fill, insertion shift and final fill
as four-way loops with their real remainder paths. Keep the final `used < 16`
guard; wide rows are still uncapped for insertion and skip final padding.

The selected source is in
[home candidates](../../tools/experiments/game_neighbor_row_builder_home_candidates.py),
with [focused tests](../../tools/tests/test_game_neighbor_row_builder_homes.py).
It uses the owner's existing primary no-unroll profile, not a new override.
Source screens, including register hints and declaration permutations, remain
experiments; only SELECTED receives the qualification below.

| Complete source | Profile | Words | Frame | Raw word differences |
| --- | --- | ---: | ---: | ---: |
| Note1610 initial | Primary |293|184|330|
| Note1610 byte-stride frontier | Normal |330|176|315|
| New SELECTED, explicit four-way loops | Primary |345|168|312|
| Same source, deliberately unselected | Normal |433|168|432|
| Retail | Original |336|168|0|

The selected routine is nine words longer, **not nine differences from exact**.
Its312 raw word differences and remaining private layout are not matching
credit. The normal profile unrolls the explicit blocks again and changes532
main-corpus profile/phase store traces; it is not selected for installation.
The selected primary agrees with ordered public stores throughout the corpus.

## Qualification

Eleven tests pass in42.843s in primary tools and43.780s in the standalone
mirror. Mirror module paths are checked; only the test input root is redirected
to prepared consumer inputs. `make tools-check` passes.

- 353 fixtures,2,106 completed original/raw profile-phase runs and12 fired
  checked-division prefixes. The main corpus visits326/336 retail words;
  this is not a full coverage claim.
- 99 native-safe fixtures at O0/O2/O3 with UBSan and eight effective semantic
  negatives. Preserve Note1610's nonfinite/invalid-conversion and division
  exclusions; no compiler-warning suppression or weakened sanitizer flags.
- Both complete owner profiles preserve all72 other functions and pools,
  including the typed caller. Three independent GNU maps pass27 completed
  runs;18 runs connect the original68-word field query and original table.
  The production helper remains a stub, not a qualified production chain.
- Six zero-actor-base guest runs execute the original null-address fallback.
  A removed-null-check negative changes public RAM. The explicit integer
  address comparison fixes native GCC's inlined-array `-Waddress` diagnostic
  while preserving identical MIPS bytes in both profiles. This synthetic
  address-zero map is excluded from portable native C acceptance.
- Effective guest negatives also reject an unsigned cursor and a lost
  wide-row padding guard. The latter fires an unmapped store on26 actors;
  the selected source completes that fixture and preserves the reference.

## Remaining Private Boundary

Six requested access-zero faults fire at both stack phases. Every model has
SP=callerSP-168, closing Note1610's frame-size boundary. Selected primary's
first requested write is callerSP-0x6C instead of retail callerSP-0x74:
RA is saved at frame+3C rather than+34. Selected primary also saves S8, absent
from retail. The unselected normal profile happens to share the first RA
write address, but has a different save set and is not literal/private exact.

Selected primary still spills nearest at SP+6C and uses RA for the original
distance, versus retail S7-nearest and S2-distance. Recover those lifetimes
and the retail table/cursor homes before treating a frame match as full ABI
or fault-prefix identity. No full private-RAM, arbitrary alias, FCSR/hardware
or gameplay acceptance is claimed. Note1610's bounded count/provider limits
remain; unchanged older suites are not presented as fresh broad reruns.

## Preserved State

No production source/assembly, guard history, Makefile/profile selection,
ELF, progress CSV or root README change. No production build, new conversion
or matching credit. All Note1610 production fingerprints remain exact;
the unchanged installed measurements are Game3015/4832,total3688/5505,
1,817 different/zero drift and owner67/73 exact. Init492/492 and
Debugger181/181 stay exact; conversion5505/6044,86.08% bytes.

Copy only the two absent new task files into the independent `64CBFD Tools`
mirror. All1,422 older dirty leaf hashes and HEADddbdd16b are verified after
its test run; do not commit/reset/stash/clean that mirror or overwrite
conflicting work. Primary tools and the consumer are checkpointed separately.

Receipts are ignored under `conker/build/game-neighbor-row-builder/homes/`:
`qualification/qualification-primary.json`, mirror `qualification.json`,
primary/mirror test logs, source screens and `graph-before.json`. Refresh
Graphify through the consumer commit hook and audit retained old/excluded
nodes before closing this checkpoint.

## Next Work

1. Continue this same function. Recover the retail save area and S7/S2
   lifetimes; table homes are groups78,count70,states64,neighbors60,scores5C,
   row start3C, selected offset40 and candidate offset44. Retain frame168.
2. Close GP/FP allocation, live primary-count rematerialization, address
   induction, three shift masks and branch-delay scheduling. Qualify any
   source-origin recipe; do not replace the body wholesale or change public
   access order to make the word count look closer.
3. Pass literal/private/access/alias, relocation, actual padder/Make and strict
   linked-image gates before replacing the12-byte stub. Preserve72 neighbors,
   all existing guards and protected data; only then rebuild and update README
   matching aggregates. The other five owner nonmatches remain separate work.
