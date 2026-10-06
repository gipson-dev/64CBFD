# Game Effect Dispatch Match

Date: 2026-10-06
Baseline: `20cd977f` ([Note 1060](1060-game-effect-dispatch-investigation-20261006.md)).
Continue the Game matching goal; this note qualifies the previously investigated
effect dispatcher, not the implementations of its classifier/effect helpers.

## Recovered Contract

`func_15141A7C`: **100 words / 400 bytes**, frame **0x48**, VA
**0x15141A7C..0x15141C0C**, ROM **0x16EF2C..0x16F0BC**, owner
[`game_16EE20.c`](../../conker/src/game_16EE20.c). Replace the false zero-return
body with effect-only `void func_15141A7C(u8 *actor, s32 context)`.
The unchanged 11-word `func_15071DC8` forwards the live actor/context globals
and ignores incidental V0; there is no native scalar-return contract.

Preserve the disable byte, actor classification, live actor+0x184 flags,
mask/context helpers, repeated classifier lookup, signed selected index and
positive signed count. Dispatch the selected effect or positive-count helper;
then load the live actor+0x2F4 head and search key0x1A. For each found node,
load record+0x10, read its selector+0x28 **twice**, and forward the signed s16
payload+0xE. After callbacks, reload the live private cursor and its next+0x14.
No new bounds, clamps, second-null checks or termination guards.

Owner-local callback views adapt the existing SDK s32/struct32 tables. Shared
headers, table data, caller source, helper placeholder bodies and compiler
profiles remain unchanged. Keep the two classifiers' existing unspecified
local declarations while their placeholder definitions remain; typed external
helper declarations use the existing O32 argument shapes.

## Source Sequencing And Derivation

[Maintained compiler driver](../../tools/experiments/game_effect_dispatch_candidates.py)
uses the actual target label and SDK includes: eight live-selector/cursor/loop
shapes across four profiles, **32 controls**. O2/g3 shape110 and111 give
**100 words / frame0x48 / 25 differences**. Empty standalone diagnostics.

The earlier nested-call 21-difference source passes the bounded IDO guest
checks, but an expanded native fixture fails with return71 when a helper
changes the classifier callback. C does not order the function designator
after argument evaluation. Do not bank that source as portable live dispatch.
Explicitly finish the helper call in a scoped `classified` local before
reloading the callback. An unscoped two-statement form gives100/frame0x40/28;
the scoped form preserves100/frame0x48. Comma/designator and volatile-result
explorations are not selected. Native sequencing is acceptance-critical, not
an incidental compiler schedule preference.

**75 direct words / 25 expected-word guards**, no insertion or omission:

- Exchange S0/S1 only in the table/cursor phase0x90..0x170, before unchanged
  saved-register restores. Category/classifier lifetime has already ended.
- Restore the three prefix branch/delay pairs and their branch destinations;
  move the one live actor-head load into the shared initial-query block.
- Rotate the selected-index move/constant/branch at0x84..0x8C, correcting the
  branch displacement. At0xC4 use still-live V0 instead of its A3 copy.
- Permute0xE4..0xF8, moving HI16/LO16 metadata with the address words rather
  than embedding post-link addresses. Restore SP+0x3C cursor addressing at
  0x160 and copy live T8 at0x168 instead of the extra private slot reload.

All100 normalized words equal retail. Actual-object padding produces400 bytes
with the expected relocated pairs; alternate table addresses spanning HI/LO
carry boundaries also match the derived sequence. Stale expected-word and
relocation guards are rejected. The full-owner screen emits the same guard
rows as the standalone object, with the same three existing warnings.
An initial typed classifier declaration fails against the existing zero-arg
placeholder definitions; preserve those local declarations instead of changing
unrelated helper bodies. The initial stale-relocation negative had an incorrect
expected error regex; fixing the test to the actual diagnostic makes it pass.

## Bounded Qualification

[Eleven maintained tests](../../tools/tests/test_game_effect_dispatch_match.py)
compare raw C, normalized C and retail, not just retail against patched retail.

- **13824 three-body guest cases**: every category, -1/0/5/20 selections,
  signed count gates, four lists, disable gates, mutations and two SP phases.
  All100 target words reached on each body; full storage and calls agree.
- Raw C adds **13764 private cursor reads** at exactly offset0x168/opcode
  0x8FA4003C. Each is initialSP-12 and equals live T8. Only this proven extra
  event is removed from raw trace comparison. All other traces and complete
  memory, including private storage, agree. Normalized traces agree in full.
- **69632 three-body connected cases** execute the original45-word actor and
  57-word context classifiers, 3-word mask and23-word list search against the
  unchanged fixed switch tables. **128 helper words mapped /122 reached**;
  **110976 raw private reads** bound as above. Every identity byte, all32
  masked flags plus high-bit flags and eight world values are covered.
- **288 registered-cursor mutation cases** qualify callback updates to the
  cursor address while its owner call is live. Do not cache the pre-callback
  node. This is a legal in-lifetime alias, not arbitrary private-frame mutation.
- **70848 actual32-bit native C cases**: full actor/node/record/table/call-log
  storage, four external alias layouts, signed count endpoints, signed payload
  endpoints, contexts, live flags, table/record/link mutations and registered
  cursor updates. The expanded classifier-table mutation exposes the original
  sequencing bug; the explicit scoped source passes. GCC's initial inlined
  fixture correctly warns about a leaked local cursor address; the bounded
  search provider is noinline and clears registration at terminal search.
- **864 three-body connected caller cases** and **240 native wrapper cases**
  forward the actual globals through the unchanged caller and verify effects.
- Nine changing-classifier cases distinguish a compiled cached-lookup negative.
  Null second targets and missing storage produce strict guest model failures;
  cyclic lists exhaust the bounded guest instruction budget. Disable gates
  avoid actor reads even when actor storage is absent. No invalid native calls,
  native infinite loops or hardware exception/termination claims.
- Ten other compiled semantic negatives each run432 cases; every one changes
  storage, calls, live accesses or mapped-access validity. Cached-selector and
  stale-cursor negatives cannot pass solely on final numeric results.

The initial negative loader split overlong object text at absolute helper
symbols and failed with KeyError. Read structured ELF text using object symbol
size, and execute overlong controls at a disjoint same-region guest entry.
Unsupported ISA is never counted as semantic-negative success. The initial
caller case-count assertion1728 was incorrect; the actual product is864.
These harness corrections are followed by successful terminal reruns.

Classifiers, positive-count work and effect callbacks remain bounded models
where not connected to original guest instructions. This does not restore
their placeholder C or establish host adoption, gameplay or hardware behavior.

## Production Verification

Explicit `make -j4 VERSION=us build/conker.us.elf` passes. Relative to
`20cd977f`, all6059 slot addresses/extents remain fixed; **only
func_15141A7C changes**, and its entire100-word slot equals retail. The11-word
caller is unchanged. Target SHA-256:
`d6be9e58a07a263cd5cea9f8ff7c9145cb60fb3c15d5ff810be901cb9985eb18`.

All10760 prior CSV rows are unchanged;25 new rows bring the total to10785.
Protected `.init` (164048 bytes), `.init_data` (17376), `.debugger` (19800)
and `.game_data` (189088) sections retain their addresses and hashes. All720
Game-data owners are exact, zero differing bytes/owners. Full-owner warning
comparison is **3->3**, the same codes/source sites, zero new warnings.
The thirteen retained-test changes update only global CSV row totals.

Regenerate `progress.csv` and run the direct linked-image matching tool:
**3336/5464 (61.05%) total**, **2663/4791 (55.58%) Game**, **2128 different**,
zero drift. Init492/492 and Debugger181/181 remain exact. Converted counts are
unchanged:5464/6042 total,4791/5321 Game; byte percentages85.57%/84.89%.
`make match-progress` first tries the complete-ROM SHA gate and stops because
the overall image is still unfinished. This function match is not a complete
retail-ROM checksum claim; the direct matching tool succeeds after CSV refresh.

All **48 focused post-link tests pass in495.394 seconds**, no skips/errors/
failures:11 new dispatcher tests, nine projection tests, nine event-dispatch
tests, nine envelope tests and ten retained metadata gates. A final production
test portability edit replaces its historical Git-object dependency with a
canonical SHA-256 of the independently verified10760-row prefix; that updated
test separately passes in3.480 seconds. Shallow checkouts need no old Git object.

**43 documents /3473 relative links /zero broken**. `make tools-check`, syntax
and diff checks pass. Required build, audit, regression and documentation
sessions are terminal before checkpointing. Ignored audit, measurements and
test receipts remain under `conker/build/game-effect-dispatch-test/`.

## Next Function

Continue with **`func_15141C0C`**,45 words /180 bytes, no frame, VA15141C0C,
ROM16F0BC. It loads unsigned actor byte+4 and classifies two identity ranges
through the fixed45-entry and89-entry switch tables at800A5218/800A52CC.
Default is11. Recover source switch groups and preserve both original table
owners/targets; the connected proof above does not recover its C body.
Next context classifier `func_15141CC0` is57 words atROM16F170 with world
overrides and a16-entry table. Qualify one function before another broad batch.

No sibling source/build/save, frozen Release, runtime launch, host adoption,
hardware/gameplay acceptance or push change. Root README aggregates only.
