# Owner payload buffer constructor direct C match

Verified 2026-10-29. `func_15190770` is restored from its zero-return placeholder
in `conker/src/game/generated_1BA1D0.c`. VA `0x15190770..0x15190840`, ROM
`0x1BDC20..0x1BDCF0`: 52 words / 208 bytes, 56-byte frame. All instructions
emit directly from C under the existing O2/g3 profile. Zero guards, alignment,
insertions, omissions or shared-header/profile changes.

## Recovered contract and source changes

`void *func_15190770(struct185 *payload, s32 extraBytes, u8 priority, s32 context)`
captures the owner pointer and owner+0x3B ID in a local notice, invokes
`func_15191B8C(notice,14)`, then allocates kind32 with context, size
`extraBytes+0x300`, direction1, priority low byte and final flag1.

Allocation failure returns null. Success copies the possibly modified 12-byte
input at output+0x10, sets cursor/end pointers to output+0x30 / output+0x300,
clears fields+0x20 and+0x1C, zeroes 0x2D0 bytes at+0x30, obtains the selector
from `func_151D8E20`, stores its low byte at+0x2C and returns the output pointer.
Notice padding is not initialized or asserted as portable C data. The notice
begins at frame+0x2C / incoming SP-12. Inputs are reloaded from homes after
notification/allocation, matching the original guest order.

The existing `struct185 *` contract is retained. The local C caller explicitly
casts its embedded payload pointer. `game/done/game_3F560.c` now declares the
same pointer-returning constructor prototype. The latter changes compact
compiler symbol metadata; both executable functions, relocations, constant
pools and its complete actual-Make padded object remain unchanged. Its two
inherited warnings and the target owner's four inherited warnings are
preserved; no new warnings. No additional C function is credited.

Raw body SHA256 `c50acbdeedfa5e49c6cbdf4616ead32da415538f74a3e1041ab78a61d37d966f`.
Five call bindings: notify56, allocate96, memcpy128, bzero164, selector172.

## Qualification

- Eight fresh canonical checks plus shared tools checks in each tools copy.
  Two fresh installed checks per copy; six semantic checks reused only with
  identical source/module/input/artifact fingerprints.
- 1,282 guest cases cover all priority/identity bytes, success/failure,
  provider modifications, argument-home reloads, pointer/source changes,
  overlapping buffers and guest wrapping arithmetic. All 52 instruction
  addresses are covered; complete state, memory, call and access traces agree
  between retail, selected C and padded C.
- Native32 SDK O0/O2/O3 each pass 5,120 defined cases with trapping UBSan,
  output/source canaries and representable extra-byte arithmetic. Nine compiled
  semantic controls reject. Notice padding is excluded from portable checks.
- 84 cases execute all 11 original memcpy words. Allocation, notification,
  zeroing and selector services are bounded; no allocator/hardware/gameplay
  acceptance is inferred.
- All four aligned full-ROM JALs are accounted for: `0x3F64C`, `0x54C64`,
  `0x1BEE00`, `0x1D8DB8`; no aligned pointer registrations. Original complete
  caller bodies `func_1501214C` (26 body words plus3 padding), `func_151918BC`
  (49 words) and `func_151AB854` (51 words) pass72,24,36 integration cases.
  The script caller `func_150265CC` passes36 cases through its original
  three-word window at `0x150277B0`, with explicit preconditions: A0 points to
  the constructed packet and A1 is zero. No complete script execution claim.
- 90 guest fault-prefix pairs include20 delay-slot cuts. These qualify guest
  instruction order, not portable C faults or hardware FCSR behavior.
- Three GNU layouts pass54 cases with all original/selected/padded/Make images
  and five call bindings equal. 57 raw/binding and228 whole-image corruption
  controls reject. Both owners use actual three-command compiler/padder/as paths.

## Whole-image audit and progress

The independent full-image prediction equals the production ELF. Complete
delta151 bytes =150 target instruction bytes +1 target extent byte; zero
metadata changes or exclusions. All6,056 addresses,6,055 other function bodies,
189,088 protected Game bytes/720 owners, guard CSV, conversion inventory and
map remain fixed. The main owner preserves60 neighbors; the declaration-only
caller preserves its entire padded object and both functions.

Fresh live-ELF recount: **3,900 / 5,506 (70.83%)**;
Game **3,227 / 4,833 (66.77%)**; Init492/492; Debugger181/181; zero drift.
**230 more** reach4,130 /5,506 (75%).
ELF SHA256 `ca2136210cc2b6554c27c2dc888afe2af11a237094a8df6ca47c8e15317bf9d7`.
Object SHA256 `2a71091263c8affa17c4d9153427227a583e51509c41e4b77b0501c8471d6554`.
Tools committed first as `01183bc`; consumer follows this note. No push.

## Resume

Evidence: `conker/build/game-owner-buffer-constructor-match/` contains650
focused frozen inputs, the16,652-file seal, canonical/installed receipts,
strict image prediction, actual Make, live recount and graph/final audits.
The older tools mirror retains1,907 inherited dirty paths plus3 new modules.
Root README changes only aggregate rows. Graph refresh is scoped; no
full-corpus extraction/global analytics refresh is claimed. The75% goal stays
active. Next screen `func_1509CA98`; next note1823. `func_1514E920` and
`func_151D7000` remain parked/uncredited.
