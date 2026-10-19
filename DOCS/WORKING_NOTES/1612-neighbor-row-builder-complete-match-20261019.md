# Neighbor Row Builder Complete Match

Date: 2026-10-19

## Installed Result

Replace `func_1508A1BC`'s 12-byte zero-return placeholder with the complete
typed C neighbor-row builder. **All 336 words/1,344 bytes and the 168-byte frame
are now byte-exact**, VA 1508A1BC..1508A6FC, ROM B766C..B7BAC. This completes the
semantic/frame recoveries in [Note 1610](1610-neighbor-row-builder-recovery-and-private-boundary-20261019.md)
and [Note 1611](1611-neighbor-row-builder-frame-and-quad-loops-20261019.md).

The body keeps its signed cursor/equality wrap, captured tables/count/group,
fresh callback inputs, weighted score gates, equal-score insertion order,
uncapped rows, ID-only padding and unweighted minimum. It retains its original
address-based name with meaningful locals and a short purpose comment.
No handwritten instruction array, dummy storage, volatile, physical-register
binding, frame patch or new compiler-profile override is added to C.

The existing primary profile still emits 345 words/frame 168/312 raw word
differences. Its checked layout recipe, not a claim of direct compiler match,
produces the complete retail function. The ordinary 433-word profile remains
unselected; the three existing normal-function overrides stay unchanged.

## Closed Layout Recipe

[Layout](../../tools/experiments/game_neighbor_row_builder_layout.py),
[integration](../../tools/experiments/game_neighbor_row_builder_integration.py)
and [qualification](../../tools/tests/test_game_neighbor_row_builder_match.py)
retain 319 unique source origins, derive 17 forms and omit 26 source words.
The 345 guard rows contain 30 identity checks, 289 other non-omitted rows,
26 omissions and 17 insert-after cells. Every prior guard byte is preserved.

All 65 public memory instructions retain their source opcode and unique
origin. The removals are ten private save/spill operations, six pointer steps,
five redundant/cached address forms, three five-bit masks, one duplicated
null-distance definition and one coalesced zero-result copy. None is a public
load/store. Nearest moves from its private spill to S7; original distance
moves to S2, and S8 is no longer clobbered. Real caller-save homes preserve
row/index/neighbor values through the provider call.

Derived forms cover symbol-HI rematerialization, the annulled cursor shift,
live copies, captured table/count loads, three caller-save pairs, equivalent
negative-remainder/end induction and a duplicated minimum test. Register
splits, private-home permutation, equivalent base-plus-cursor accesses,
branch-delay scheduling and one commutative float multiply are explicit.
All 19 output bindings survive three independent GNU maps; 13 raw bindings,
every raw word and the final recipe digest are checked before output.

The two source null-distance constants are equal. Fold the likely-branch
copy into the retained fallback while preserving the unconditional mode
halfword read in the ordinary branch delay. Keep the signed divide checks
and both actual break codes. The local operand decoder explicitly handles
SRA, REGIMM, MFC1, TRUNC.W.S and DIV without treating break-code bits as GP
registers. All original assembly stays untouched.

## Qualification And Integration

All ten installed tests pass in 61.907s in primary tools and 52.405s in the
standalone mirror. Pre-install runs also pass in 50.237s/50.255s. Mirror module
paths are verified; only its test input root is redirected to prepared
consumer inputs. `make tools-check` passes.

- 353 fixtures/706 literal-private pairs, 2,106 completed original/normalized/
  raw runs and 12 fired divide-trap prefixes. The main corpus visits 326/336
  original words; the separate zero-address map executes the null fallback.
- 1,482 requested access-fault pairs all fire and match complete private
  state, including both stack phases and actual callback clobbering.
- 99 native-safe fixtures at O0/O2/O3 with UBSan and eight effective semantic
  negatives. Four completed guest frame aliases have four effective raw-home
  negatives; all earlier frame/save-area boundaries are closed.
- 18 original field-query helper runs,27 completed runs across three GNU
  maps and six zero-actor-base guest runs with an effective missing-null-check
  negative. All 19 normalized bindings are independently exercised.
- 358 stale raw/binding controls, two corrupted recipes, two actual-padder
  stale controls and four complete-image corruptions are rejected.

Both raw owner profiles preserve 72 other functions and pools. Actual padding
preserves all 73 owner addresses and all extents outside the target. The existing
seven-command Make shadow reproduces code/metadata and the unchanged three
override selections; no Makefile change. Its existing generated_12D630
duplicate-recipe warnings are inherited, not a new failure.

The production N64 build succeeds and exactly reproduces the first-link
prediction: **1,066 changed bytes = 1,064 target-code bytes + two target st_size
bytes**, with no other serialization allowance or section exclusion. All
6,056 other bodies, all 6,057 addresses and 189,088 protected Game-data bytes
across 720 owners stay fixed. The shared CSV dependency causes a broad object
rebuild, not a broad source-conversion batch. Progress CSV is unchanged.

Full gameplay/caller/hardware/FCSR acceptance is separate. The original
68-word field-query helper is connected in tests, but its production C body
remains a stub. Keep the documented bounded-count, synthetic guest-alias/
zero-base, nonfinite native-conversion and invalid-division exclusions;
do not present these model fixtures as full production-chain validation.

## Banked State

Tools `7899ba5` is committed before consumer source/guards/docs/pin. Consumer
predecessor `c0c09f56` and tools predecessor `f0db953` were clean. Only three absent
task files are copied into the independent mirror; all 1,424 older dirty leaf
hashes and HEAD `ddbdd16b` are preserved. No mirror commit/reset/stash/clean,
push, host/frozen Release, save, dependency or advisory-agent operation.

Fresh totals: **Game 3,016/4,832 (62.42%)**, **total 3,689/5,505 (67.01%)**,
1,816 different and zero address drift. Init 492/492 and Debugger 181/181 stay
exact. Owner `generated_B3020` is **68/73 exact**, with five remaining routines.
Conversion remains 5,505/6,044 (91.08%), 86.08% bytes. Root README changes only
its two matching aggregate rows; detailed updates remain in these notes.

```text
Source:   a5187038998c59d0630b480e8cc03e87e43aed40a6a27c9eeb8207e46bfd44ea
Manifest: e870831d0fe6d5562f156698a9c24d0af1f864fe95b8a1790bcdcf664be60dc4
ELF:      0462d68d9fe12d04c2d747b1f8877305f84bce1ac7793e24024268e6e06e07c7
```

Receipts remain ignored under `conker/build/game-neighbor-row-builder/homes/match/`:
pre-install/installed primary and mirror qualification JSON/logs, integration
qualification, Make-shadow, first-link, installed audit, fingerprints and the
fresh remaining-owner report. The consumer commit refreshes Graphify; audit
old-node and excluded-evidence preservation before closing this checkpoint.

## Next Function

Continue with **func_1508B3F8**, 369 words/frame 320, VA 1508B3F8..1508B9BC,
ROM B88A8..B8E6C. It already has a complete-looking typed
`NeighborVisitQueryB3020` C body and explicit four-candidate scan, but still
has 281 classified word differences. Inspect its entire assembly, current
compiler profile and query/helper interfaces before further matching; do not
assume its existing C or prototype guesses are fully qualified.

The other four owner nonmatches are `func_15086364` (539 words),
`func_1508A6FC` (678), `func_1508CAD8` (862) and `func_1508DC24` (681).
Keep the wider Game matching goal open.
