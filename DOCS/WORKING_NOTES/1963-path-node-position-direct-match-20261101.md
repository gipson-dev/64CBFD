# Path-node position command recovered directly from C

Verified 2026-11-01. `func_15077DBC` emits all **56 retail words directly from
C**, with **no frame or word guards**. Repeating the existing typed path-node
lookup before each coordinate assignment replaces the old cached node pointer
and recovers the original live actor/table accesses. The interface stays
`void(void)` and the shared `PathNode8` type is retained.

Production Make and independent Windows actual-ELF recount report
**4,033/5,507 (73.23%)** total and **3,360/4,834 (69.51%)** Game, zero address
drift and 1,474 different. Init remains 492/492; Debugger remains 181/181.
Converted inventory stays 5,507/6,045, Game 4,834/5,324. The threshold is 4,131:
**98 additional exact C functions are needed**. The wider goal remains active.

## Routine and direct compiler shape

- Source/owner: `conker/src/game_A28B0.c`, `game_A28B0`.
- Original `conker/asm/nonmatchings/game_A28B0/func_15077DBC.s` is retained.
- VA `0x15077DBC..0x15077E9C`, ROM `0xA526C..0xA534C`, 224 bytes.
- Eight relocation bindings; no shared headers, profiles or layout changes.

Command byte `D_800D1890` updates actor byte `unk21E` unless it is sentinel
`0xFA`. Each X/Y/Z assignment separately reloads current actor `D_800D154C`,
path-table pointer `D_800D2104`, unsigned group byte `unk13F`, node byte `unk21E`
and the group's row pointer. Signed halfwords at row+node*8+8/+10/+12 become
float positions at actor+0x14/+0x18/+0x1C. Stores may alias a pointer or later
coordinate input, so the three separate lookups matter.

The existing eight-byte `PathNode8` view expresses these accesses as
`table[group][node + 1].x/pad2/z`. Four source forms emit the complete retail
payload and bindings without normalization. Equivalent halfword-table indexing
forms retain 56 words but differ at 23 words; the simplest typed form is selected.
Raw SHA-256:
`ab7ab595da2b0ed12ddbb1861a2511d81fa64cdde227156113596e27d9aa2921`.

Complete original ASM, isolated selected C, raw/padded owner and actual Make
payloads agree. There are no inserted/omitted words, volatile filler or new guards.
Corrupted payloads, missing bindings and repeated source installation reject.

## Behavioral and original caller checks

- **10,752 guest cases / 43,008 executions** cover three rebases, seven alias
  layouts, both stack phases and all 256 command bytes. All 56 words execute.
  Signed coordinate extremes, sentinel retention and unsigned group/node bytes
  are covered. Four programs—original ASM, padded owner, actual Make and isolated
  C—agree in full modeled memory, registers, FP state and access traces.
- Alias cases relocate the actor pointer after X/Y/Z stores, overwrite the
  global path-table pointer, overlap outputs with signed coordinate input, and
  replace the selected row pointer. Independent reference evaluation reloads
  the actual memory after each store. Caller-saved dead results are compared
  too because all four programs have identical instructions.
- **70 fault prefixes / 280 executions** agree in complete modeled state.
  These establish emitted guest access order, not portable C fault semantics.
- Three separately compiled controls—cached actor, cached table and the original
  cached-node source—each fail an appropriate alias case. This confirms that the
  recovered reloads are behaviorally relevant.
- Native O0/O2/O3 each pass **2,048 cases**, UBSan, complete actor canaries and
  unchanged path storage. Seven compiled controls are effective: wrong sentinel,
  unsigned X/Y/Z, swapped X/Z, wrong node index and missing Z store. Pointer
  aliases are guest-qualified; native tests use valid disjoint C objects.
- The initial freestanding native O2 harness faulted at an aligned SSE stack
  store in `_start`. GDB identified the entry-stack alignment assumption. The
  harness now uses `-mstackrealign`; this changes no production/compiler profile.

Census finds exactly one aligned root pointer, ROM `0x22B454`, corresponding to
`D_80086730[153]`; there are no aligned direct JAL/J sites. The original
29-word caller window `0x1507BD00..0x1507BD74` is pinned against retail and the
baseline ELF. **120 cases / 480 executions** cover command153 and skip opcodes
247/255, both stack phases and four ignored-return poisons. All 28 reachable
words execute; the duplicate load at window+0x20 is unreachable. The window
copies all four payload bytes even though this root consumes only the first,
then advances the packet five bytes; skips advance one. Root return values do
not affect the caller. This is a bounded window, not full dispatcher emulation.
The root has no nested helper. Hardware/gameplay and full FCSR behavior remain
outside these tests.

## Owner, complete image and adoption

All **210 raw/padded neighboring functions** and normalized pools remain fixed.
The owner's **14 warnings remain 14**, with unchanged warning kinds and source
expressions. The actual five-command Make recipe produces the independently
qualified padded object under the unchanged retail profile.

The independent literal ELF predictor replaces only the 224-byte target slot
and changes its symbol extent from160 to224. The original canonical slot already
contains enough alignment space; no overflow movement or deletion occurs here.
The complete first-link and production ELF match that prediction with **zero
exclusions**. Corruption controls cover target instructions, symbol metadata
and unrelated image bytes. All **6,055 function addresses**, **6,054 other
bodies** and **189,088 protected Game bytes / 720 owners** remain fixed.

Production reviews all **17,621 predecessor sealed inputs**. Only source, its
owner object and the ELF change; guards, map, layouts, headers and unrelated
objects remain identical. Installed ELF SHA-256:
`88e4bf6ae8be845c8f97fd94e26cd88298b65df9e361abe359d976e3a5dd2898`.

Six focused tests per tools copy pass before and after installation, both shared
tool checks pass, and the Windows actual-ELF recount independently confirms the
new total. Only three identical owned modules are added to the older tools
mirror; its existing dirty state is preserved. Tools are committed before the
consumer. No push is performed. Root README receives aggregate rows only.

## Evidence and next target

`conker/build/game-path-node-position-15077DBC-match/` contains 1,059 frozen
focused inputs, 26 canonical artifacts, screens, owner/Make/image evidence,
guest/native/caller results, independent Windows recount and final bank receipts.
Early private preparation flags are historical; BANKED_STATUS records adoption.
Historical archived checkpoint tests require explicit restoration.

The advertised `func_15076DF4` and adjacent simple commands were already exact;
the fresh nonmatching list selected this command instead. Next audit
`func_150781F4`, the 54-word path-distance branch command. Inspect its captured
mode byte, integer radius conversion, square-root intrinsic and notification
interface, plus the existing private overflow body. Do not count its current C
or assume the previous overflow-removal closure applies unchanged.
