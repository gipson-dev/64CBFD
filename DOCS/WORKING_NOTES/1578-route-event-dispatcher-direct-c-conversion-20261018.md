# Route Event Dispatcher Direct C Conversion

Date: 2026-10-18. **Installed direct C match: all 53 words / 212 bytes exact.**

Convert `func_150880F8`, generated_B3020, VA `150880F8..150881CC`, ROM
`B55A8..B567C`, after [Note 1577](1577-route-actor-event-direct-c-conversion-20261018.md).
Consumer predecessor `0d4c48c6`; tools predecessor `eabe57c`. Bank tools
**7bc7dfc** first, then the consumer source/docs/pin. No push.

## Complete Source And Interface

Recover `s32 func_150880F8(s32 recordIndex, s32 reason)`, keeping both external
arguments full-width. Return zero without dereferencing a record when the
table is null. Otherwise form the modular 0x84-byte record offset and signed
byte actor slot, dispatch state 0 to the real `func_1508802C`, propagate its
status, transition state 1 to state 2 with actor sentinel 0xFF, then stamp and
increment the signed-byte counter. Other record-state bytes skip the event
transition but still stamp/increment. Preserve the address name, meaningful
locals and one concise purpose comment. Original assembly is retained.

The initial named table/state temporaries emit 53 words/frame48/seven
differences. Reusing the table local as the record restores frame32 but changes
31 words, so it is not selected. The direct global-table test plus indexed
record expression, without a separate table/state local, emits the original
53 words/frame32 directly. Both source table reads coalesce into the original
single load; index-first address addition preserves operand order. No original
volatile qualifier, physical register, padding, guard or compiler flag is added.

Counter reads remain after the transition/provider and on both sides of the
record stamp. A real public alias makes the state-byte write change the counter;
an early-counter snapshot is an effective negative. Do not invent a functional
negative for merely caching two counter reads when no intervening observable
change occurs: the actual two-read access order is independently asserted.

Raw unlinked code SHA:
`a222a2eac943e70a0f266df106590d9b45dcbd5d88de6eeebfc736d50120ba92`.
All seven bindings and isolated/full/no-unroll/normal-profile output agree.

## Fresh Qualification

All **eight strengthened pre-install tests pass in 25.195 seconds**; all
**eight post-install tests pass in 38.606 seconds**, no skips. The earlier
27.181-second run precedes the explicit counter-read assertion and the native
control restricted to this parent. Do not sum overlapping corpora.

- Run 1,760 cases in both stack phases with the actual 51-word installed child,
  independently checked against ROM. Cover all 26 actor slots, all 256 record
  state bytes, all 256 counters on states 0/1/2, all 256 reason low bytes with
  nonzero high bits, full-width extremes, blocked children and null tables.
  Provider mutations clear the global table and change the counter, verifying
  the saved record and the post-call read. Compare independent reference public
  memory/returns/calls, plus retail/source modeled GP/FP/LO state, complete RAM,
  ordered accesses and snapshots. All 53 target words are visited; nonnull
  paths have exactly two counter reads, null paths none.
- Run the same 1,760 inputs through actual parent and child C in freestanding
  native32 O0, O2 and O2+UBSan, checking 18 scalar/call observations per case.
  Native backing has 32 records and 26 actors. A parent-only wrong-state control
  exits 21. No libc/dependency installation or broad shared-helper change.
  Native observations do not prove every padding/private byte or unknown alias.
- Pass 550 fired own-access fault pairs over five aliases, three states and
  both stack phases, including a valid private-home alias. Public aliases also
  pass the independent reference. Private-home evidence qualifies emitted guest
  instructions, not portable C private-stack alias behavior.
- Exercise all 256 signed actor-slot bytes and five modular index values in
  261 additional guest-artifact pairs. These out-of-backing cases are not native
  C domain or valid gameplay claims. Preserve signed loads and full-width ABI.
- Four ordinary executed source negatives fail public comparisons: narrowed
  reason, ignored child status, early counter and wrong state transition.
  Do not credit a crash, timeout or instruction-budget failure.
- Independently assemble original retail source; its raw code and all seven
  bindings equal C. Three GNU maps cover independent data/call addresses and
  HI/LO carries. Pass 36 paired code-rebased executions with real child code.
  Data rebases are static checks, not changed-data/provider runtime acceptance.

The event submission below the real child remains a bounded provider. No
compiler capture, debugger, Claude call, emulator or hardware/FCSR validation.
Prior unchanged neighbor/child receipts are preserved rather than described
as newly run broad suites.

## Production And Progress

Both full owner profiles preserve all 72 neighbors and pools, and the actual
mixed padder preserves all 73 owner functions, including the normal-profile
projection and the two remaining GLOBAL_ASM routines. The first private whole
ELF is literally unchanged, including metadata. The real Make build and the
installed audit reproduce the same image: all 6,057 bodies/addresses fixed,
all 189,088 protected Game-data bytes / 720 owners exact, all frozen inputs
except the declared owner-source change fixed. Guards and Makefile stay exact.
The duplicate generated_12D630 recipe warnings remain; not a warning-free build.

Whole-ELF SHA remains
`44ecb171bef3c1e2c5f3afb2345953cf70d15224a51db37a1d4fc62c60105e0c`.
Owner-source SHA becomes
`ec3fd9786e52b63698d7d2a723e31479f0941441e7b25c523bda71c92272fb3b`.

This is an exact-ASM-to-C conversion: add one C function / 212 bytes, without
changing executable bytes or reducing the existing different-C count. Fresh
matching: total **3667/5503 (66.64%)**, Game **2994/4830 (61.99%)**,
Init **492/492**, Debugger **181/181**, **1,836 different / zero drift**.
Conversion: total **5503/6044 (91.05%), 86.06% bytes**; Game
**4830/5323 (90.74%), 85.43% bytes**. Exclude repeated CSV header rows when
aggregating. Root README changes only these aggregate rows.

Both tools copies pass three setup tests and their smoke check; consumer
`make tools-check` passes. Three new files are identical ASCII and AST-valid.
Preserve all 1,301 prior mirror hashes and its ddbdd16 HEAD; add only the three
owned files, leaving 1,304 dirty paths, without a mirror commit/reset. Post-commit
graph preservation is a separate final gate in the ignored `graph-audit.json`.

```sh
python3 -m unittest tools.tests.test_game_route_event_dispatch_match -v
python3 -m tools.experiments.game_route_event_dispatch_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

This routine is finished. Next audit retained `func_150885EC`, VA
`150885EC..1508868C`, ROM `B5A9C..B5B3C`, 40 words/frame0x28. It copies a
0x84-byte record with bcopy, preserving the destination ID/state and reloading
the current table after the provider. Qualify copy direction, overlap, table
mutation and restore ordering before conversion. Broader Game work stays open;
no sibling host/Release changes or whole-game acceptance claim.
