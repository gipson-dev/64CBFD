# Route Slot Reservation Direct C Conversion

Date: 2026-10-18. **Installed direct C match: all 61 words / 244 bytes exact.**

Convert `func_1508868C`, generated_B3020, VA `1508868C..15088780`, ROM
`B5B3C..B5C30`, after [Note 1579](1579-route-record-copy-direct-c-conversion-20261018.md).
Consumer predecessor `2334ab26`; tools predecessor `5d8bc93`. Bank tools
**c1fbc31** first, then the consumer source/docs/pin. No push.

## Complete Source And Interface

Recover `s32 func_1508868C(u8 *actor)`. Return -1 immediately for a null table,
nonpositive signed count or exhausted scan. Start with unsigned bit 1 and
reserve the first clear bit before adding the signed base byte to the scan
index. Reset its 0x84-byte record through func_15088824, then store state 1
and the actor's signed byte identity through two fresh table reads. Compute
the identity from the signed full-word actor/base-address difference divided
by 812, truncating toward zero. Keep the address name, descriptive locals and
one concise purpose comment; do not invent original source-name authenticity.

Preserve unsigned mask wrap: with count greater than 32, an all-ones mask
reaches a zero bit at scan index 32 and still calls the reset helper. Do not
clamp the count or treat a -1 result as proof of no allocation: signed base
-1 and free index 0 legitimately reserve/reset a record and return -1.
Explicit 32-bit integer address sums retain negative-base modular addressing
without introducing native pointer-overflow arithmetic.

The initial body has 61 words/frame0x28 and five differences: only a closed
T7/T8 allocation cycle around the mask update and signed base load. Moving
the mask reservation before base adjustment makes all five emit directly.
The selected source matches the original homes and branch-delay scheduling;
no register bindings, volatile, padding, new guards or compiler settings.
Raw unlinked code SHA:
`e210dced569cefd70a143318b56e106f5cd9f7a4c09901e14ab7a9a13aac9cc7`.
All 15 bindings and isolated/full/no-unroll/normal-profile output agree.

## Fresh Qualification

All **ten pre-install tests pass in 69.665 seconds**; all **ten post-install
tests pass in 20.162 seconds**, no skips. Overlapping guest/native cases are
not independent corpus additions.

- Run 1,496 inputs in both stack phases, covering all 256 count-byte values,
  all 256 base-byte values, every first-free position through bit wrap,
  exhausted/null tables and actor IDs. Compare independent public memory,
  result and call operands, plus complete modeled GP/FP/LO state, RAM and
  ordered accesses between retail and emitted source. All 61 words are visited.
- Connect all 33 real reset words, independently equal to the frozen ELF and
  ROM. The helper is straight-line and its exact C body is also fingerprinted.
  Normal nonnull allocating paths read the table three times; null paths once.
  Separately exercise bounded provider changes to table/count/base/mask and
  volatile registers, plus poisoned V0, without claiming unknown providers.
- Execute actual reset writes through overlapping mask/count/base globals.
  Also exercise incoming actor-home mutation and a state store that changes
  the table pointer before the actor-ID store. These are mapped guest witnesses,
  not native out-of-backing cases or portable private-stack guarantees.
- Pass 372 fired access-fault pairs across nine profiles and both stack phases.
  Include actual reset accesses for real-helper profiles; exclude observer and
  bounded provider internals from fault counts. Compare literal state/events;
  do not infer hardware exception behavior from this software instruction model.
- Run the same 1,496 inputs in freestanding native32 O0, O2 and O2+UBSan using
  the actual reset C and two 288-record banks. Compare all 76,032 bytes per case
  with 54,204 independently generated expected-byte patches, adapting only the
  helper's typed integer/float field byte order. Check result, table, mask,
  count/base and exact helper operands/count. The wrong-state control exits 21.
- Six ordinary executed source negatives fail public comparisons: unsigned
  count, initial bit 2, missing mask reservation, state 2, pre-reset cached
  table, and one post-reset table cached across both stores. Their executions
  complete; crashes/timeouts are not counted as semantic negative controls.
- Twelve guest pairs cover signed full-word actor differences, including both
  signed extremes and values around +/-812. Native backing is limited to the
  valid 26-actor array; arbitrary guest addresses are not native C inputs.
- Eight actual four-word caller windows cover both stack phases, success,
  exhaustion, null table and a successful allocation returning -1. The real
  window passes the actor, preserves the other index and constructs AT=-1;
  its following -1 branch is checked statically. The stop trampoline is
  synthetic and the complete caller is not executed.
- Independent original assembly has identical raw words/15 bindings. Three
  GNU maps exercise symbol/code addresses and HI/LO carries. Pass 32 paired
  code-rebased executions; changed-data-map execution is not claimed.

Reuse existing compiler, ELF, mixed-padder, SDK instruction and native32 tools;
no shared oracle or build-profile changes. No debugger, capture or Claude call.
The earlier compiler capture remains audit-only and was not rerun. The user's
confirmed disposable `Conkers` scratch file needs no recovery.

## Production And Progress

Both owner profiles preserve all 72 neighbors and pools; the actual mixed
padder preserves all 73 owner functions. The first private ELF is literally
unchanged, including metadata. Actual Make and installed audit reproduce it:
all 6,057 bodies/addresses fixed, all 189,088 protected Game-data bytes / 720
owners exact. Every frozen input except the declared owner-source change stays
fixed, including guards and Makefile. Existing duplicate generated_12D630
recipe warnings remain; this is not a warning-free full build.

Whole-ELF SHA remains
`44ecb171bef3c1e2c5f3afb2345953cf70d15224a51db37a1d4fc62c60105e0c`.
Owner-source SHA becomes
`cdb960c419dc4fee3c450de5c59dabc488e538cb1f1de75a3422f5c1d63b6521`.

This adds one C function / 244 bytes from already-exact assembly. Executable
bytes and the different-C count do not change. Fresh matching: total
**3669/5505 (66.65%)**, Game **2996/4832 (62.00%)**, Init **492/492**,
Debugger **181/181**, **1,836 different / zero drift**. Conversion: total
**5505/6044 (91.08%), 86.08% bytes**; Game **4832/5323 (90.78%), 85.44% bytes**.
Exclude repeated progress-CSV header rows. README gets aggregate rows only.

Both tools copies pass three setup tests and the smoke check; consumer
`make tools-check` passes. The three new files are identical ASCII and compile
as Python. Preserve all 1,307 prior mirror hashes and its ddbdd16 HEAD; add only
these three files, leaving 1,310 dirty paths, without a mirror commit/reset.
Post-commit graph preservation is a separate final gate in ignored
`conker/build/game-route-slot-reservation/graph-audit.json`.

```sh
python3 -m unittest tools.tests.test_game_route_slot_reservation_match -v
python3 -m tools.experiments.game_route_slot_reservation_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Next Target

This routine is finished and no GLOBAL_ASM pragma remains in generated_B3020.
That does not finish its nonmatching C stubs. Next audit `func_1508E6D0`, VA
`1508E6D0..1508E780`, ROM `BBB80..BBC30`, 44 words/frame0, currently a false
zero return with 42 linked differences. Read the complete 63-entry
`jtbl_8009DA94` at VA `8009DA94..8009DB90`, ROM `242554..242650`, and preserve
its repeated/default targets. The actual caller at 1509E4C8 loads a full-word
selector in the JAL delay slot and consumes the result. Qualify the complete
selector/default domain, recovered switch/pool layout and image/data gates
before installation. Broader Game work remains active; no host, frozen Release
or gameplay claim.
