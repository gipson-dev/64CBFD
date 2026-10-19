# Round-Robin Slot Selector Complete Match

Verified:2026-10-19. **Installed complete C recovery: all47 words /188 bytes
match retail, frame0, with no alignment tail or helper call.**

Finish `func_1508C9CC`, generated_B3020, VA `1508C9CC..1508CA88`, ROM
`B9E7C..B9F38`, following
[Note1586](1586-packed-row-dispatch-complete-match-20261019.md).
Consumer predecessor **657a6b51**, tools predecessor **7a6f9fa**. Bank tools
**cf919bf** before the consumer source/guards/docs/pin. No push.

## Complete Source And Caller

Read the context pointer from D_800D23B0 and signed byte count D_8008FD8C.
Advance the signed byte cursor at context+1702, truncating each increment
back to signed8. Reset it to0 when it is at or above the signed count.
Check the actor at D_800CC2D0 +slot*0x32C, in this order:

- Its first word must be nonzero.
- Its nested pointer+31C must be nonnull.
- Nested unsigned byte+84 must be nonzero, including80/FF.
- Its bit must not be set in unsigned-halfword D_800D18A0.

Return the **first eligible slot**, or -1 after the scan. Always store the
last checked slot byte back through the cached context pointer. Keep the
do/while first attempt: even zero or negative count checks one candidate;
do not add an early empty-count return. Slots16..25 cannot be excluded by
the16-bit mask. No incoming arguments, helper calls or stack frame.

Use `s32 func_1508C9CC(void)` with the retained address name and a concise
purpose comment, not an invented original symbol. The source retains the
existing integer/pointer32 ABI and ordinary unsigned `1U << slot` expression.
Native fixtures keep evaluated indices in0..25, matching the retained
26-record actor declaration. Guest-only sparse negative/wide indices test
the emitted MIPS byte conversion, address arithmetic and low5 shift count;
they do **not** establish portable C array/shift validity outside that domain.

The one retained direct call is VA **1509E488**, ROM **CB938**, in CB3D0.s /
func_1509E3DC. Its JAL0D423273 has a NOP delay. The actual following branch
and RA reload lead to the original SP+18/JR/NOP epilogue at1509E62C. V0 is
returned unchanged. The caller's production C is still a separate stub;
this change does not restore it or claim full dispatcher execution.

## Explicit Layout

Fifty source forms were compiled: loop/byte/shift forms, initializer order,
register hints, count width and cursor initializer placement. The selected
ordinary do/while body emits **47 words/frame0**,8 bindings, empty diagnostics
and14 real differences in both existing owner profiles. Register hints and
byte-count variants offered no better result. A masked-shift source adds a
word; do not silently clamp the original algorithm to fit a native fixture.
No volatile, dummy operation, physical-register binding or compiler change.

`game_round_robin_slot_layout.py` restores only:

- One closed GP cycle: source3->5,5->6,6->3, for the context/count/result
  roles. SlotA0 and all other roles are unchanged. Decode opcode-aware GP
  fields; do not rewrite shift amounts, immediates or zero registers.
- Independent opening words6..9 use origins7,8,9,6: move result -1 and the
  two address low halves before the count byte read. No branch or target
  moves, and count remains read before the cursor.
- Move the same three LO16 bindings with those instructions. Keep all8
  bindings and all47 instruction origins exactly once.

Fourteen expected-word/expected-relocation rows encode the result. No
insert_after, omitted instruction, branch repair or new operation. Gate on
the full raw hash, exact binding dictionary and normalized hash. Installation
also requires the exact qualified owner, old guard prefix and first-image
receipt. Original assembly, data, Makefile and shared padder remain untouched.

```text
raw:        2399eb522cb25f9ae26d3fa6f5cc64db50b1007bd0f2525f9eb007ffc7060dd7
normalized: 70dcb8f7279b1aeef68c4e544f63b2eb2955269bd87b271dada292fb9d46e2eb
```

## Fresh Qualification

All **nine pre-install tests pass in33.973 seconds** and **nine installed
tests pass in37.415 seconds**, without skips. Fixtures and selected map/
caller cases are reused coverage, not independent additional domains.

- **3,032 fixtures/two phases:6,064 paired literal executions**, agreeing in
  full GP/FP/LO, private/public memory, ordered events and return. Dynamically
  visit and statically compare all47 words. The same corpus checks the raw C object's
  public result/memory against an independent numeric circular-search
  reference. All256 cursor and count byte encodings occur in guest fixtures;
  sparse backing covers -128..127, not a claimed portable native array.
- **154 fired access-cut pairs**, each requested cut confirmed, plus **12
  guest alias pairs**. Redirect the cursor byte onto count, either mask byte,
  context-pointer storage, actor presence or nested readiness. Verify the
  cached pointer, delayed single-byte store and complete literal states.
  This is modeled guest access order, not a hardware exception claim.
- Native32 **O0, O2 and O2+UBSan** each pass **2,520 fixtures**, checking all
  actor/node/context bytes remain unchanged except the cursor, plus **65,536
  extra calls** covering every mask against a fixed first-zero-bit numeric
  expectation. Qualify only backed0..25 indices. One extra zero actor26 is
  backed solely for the wrong-wrap negative, avoiding a crash-as-success.
  Retain stack realignment and no-strict-aliasing harness flags.
- Five executed C negatives (wrong wrap equality, missing ready check,
  missing mask, last rather than first selection, skipped first attempt)
  exit21. Positive profiles exit0; no signal/UBSan trap is counted as an
  effective negative.
- **116 actual caller-window pairs** execute all seven retained words:
  JAL/delay, branch/RA reload and epilogue. The caller frame is an explicit
  live-in; do not claim its earlier dispatch or entire routine was executed.
  The actual return propagates and saved roles/SP are checked.
- **Three independent GNU maps** agree for all47 words and8 bindings,
  including HI/LO carry boundaries. Execute **516 mapped cases** with code,
  every global, context pointer and nested objects rebased.
- Thirteen raw/binding/recipe corruptions reject. Six actual-padder manifest
  corruptions fire stale-word/relocation checks; three image mutations fail
  the strict verifier. Both owner profiles preserve72 routines and normalized
  pools. Actual padding preserves their bodies/addresses/pools. All seven
  expanded shadow Make commands agree; no source/build production edit is
  needed for that private Make qualification.

## Production And Commits

The first private link matches its exact complete-image prediction on the
first attempt. Production Make reproduces the same3,257,636-byte ELF:
**143 changed bytes =142 target-code bytes +one target-symbol size byte**
(12 ->188). No metadata permutation or broad exclusion. All other6,056
linked bodies, every address, all189,088 Game-data bytes /720 owners,
historical guard bytes and all other frozen inputs stay fixed.

The manifest-triggered rebuild succeeds with inherited duplicate
generated_12D630 recipe warnings and diagnostics from untouched code.
Both target owner profiles have empty diagnostics, not the entire build.
Retain its full ignored log at
`conker/build/game-round-robin-slot/integration/production-build.log`.
Git's existing CRLF advisory is not a CSV/build failure.

```text
owner:  66972bed4e1550955f49fb477d54b866bda66046d2b1f6d25a458e59fa5b7cd7
guards: c5c75bcb2a7775fe376378308fec352c35f41584f6c4c11b8121dc76acead55f
ELF:    6e6583fb815a0e3d160444feed792fdd05cab6cb7f7aedb4c92ccb282d8d59e2
```

Fresh matching: **Game3002/4832 (62.13%)**, **total3675/5505 (66.76%)**,
Init492/492, Debugger181/181, **1,830 different / zero drift**. Conversion
counts/bytes remain5505/6044 (91.08%),86.08% overall and4832/5323 (90.78%),
85.44% Game; the false placeholder was already counted as C.

Both tools copies pass three setup tests and smoke checks; consumer
`make tools-check` passes. The five new files are identical ASCII/Python-valid
in the standalone mirror. Preserve its ddbdd16 HEAD and all1,333 prior dirty
leaf hashes; add five task files for1,338 dirty leaves, no mirror commit or
reset. Post-commit graph preservation is separately retained in ignored
`integration/graph-audit.json`. No compiler capture, Claude call, REA setup,
sibling host or frozen Release action.

```sh
python3 -m unittest tools.tests.test_game_round_robin_slot_match -v
python3 -m tools.experiments.game_round_robin_slot_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Next Target

Fresh owner audit: **54/73 exact,19 different**. The complete remaining list
is retained in ignored `integration/owner-completion.json`; Note1586's20-name
list is historical and now excludes the finished func_1508C9CC.

Continue **func_1508DA1C**, VA `1508DA1C..1508DAEC`, ROM `BAECC..BAF9C`:
**52 words/frame8**,52 real differences, still a zero-return stub. The first
loop fills initial-context+EB0 with -1, bounded by a signed count+10 that is
reloaded through the current global context after each store. Keep the final
reloaded context for the next count+EA4 read when this loop ran.

The second loop resets five parallel arrays using **cached initial-context
output pointers**: F70=-1, FF0=0,10F0=-1,1070=1,12F4=0, in that store order.
After each group reload the global context and signed count+EA4; advance all
five outputs by4. Preserve the saved S0/-1 lifetime, signed nonpositive gates,
pointer/count alias behavior and original delay slots. A direct call is
VA1509E0F8 / ROMCB5A8 in CB3D0.s, JAL0D423687/NOP. Derive the actual return
interface instead of retaining the false zero result. The broader Game
decomp/matching goal remains active.
