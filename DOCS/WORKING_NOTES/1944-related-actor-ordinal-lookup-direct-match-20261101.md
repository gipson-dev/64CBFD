# Ordinal actor-link lookup restored directly from indexed C

`func_15072208` now emits all **58 retail words directly from C**, with no
stack frame, guards, assembly insertion, omission or compiler-profile change.
The complete 232-byte slot is exact under the existing O2/g3 owner profile.

Production Make and the live Windows-checkout recount agree on **4,017/5,506
(72.96%)**, Game **3,344/4,833 (69.19%)**, Init 492/492 and Debugger 181/181,
zero address drift and 1,489 different. **113 more matches** are needed for
the active 4,130/5,506 threshold. Tools were committed first at `731d592`.

## Recovered operation and interface

Owner/source: `game_981E0`, `conker/src/game_981E0.c`.
VA **15072208..150722F0**; ROM **9F6B8..9F7A0**.
The existing `struct127 *func_15072208(struct127 *, s32)` declaration is
correct and unchanged. Descriptive parameter/local names replace the null
placeholder: owner, ordinal, ownerIndex, matchIndex and slot.

The signed owner index is `(owner - D_800CC2D0) + 1`, using the original
0x32C-byte actor stride. The routine searches slots **0 through 24** in the
26-record declared pool, compares the unsigned byte at +0x65 (`unk65`), and
returns the zero-based ordinal match. It returns NULL if no requested match
exists. Negative ordinals cannot match. Slot 25 is the exclusive scan bound;
this observation does not assign a gameplay role to that record. No activity,
actor-type, owner-null or range gate is added.

A simple indexed `for (slot = 0; slot < 25; slot++)` recovers the retail
compiler's peeled first record and four-way unrolled remainder. Manual peeling
and pointer-loop forms generated extra loops or retained loop counters. The
selected body uses no manual unrolling, volatile accesses or layout filler.
The existing pointer-return function parser does not recognize this return
spelling, so the tool validates and replaces the exact old placeholder only.

## Object, padding, Make and complete image

The isolated semantic C is warning-free. Its raw body SHA-256 is
`979ea9947a5c569243ceeac2837e3e1e11a1422b1323f19adebc0b4e34e7b4db`.
Eight pinned relocation fields derive the pool aliases from `D_800CC2D0`.
The original assembly names the equivalent +0x65, +0x32C and +25*0x32C
addresses separately as D_800CC335, D_800CC5FC and D_800D121C. The oracle
preserves these relationships and independently relocates the complete pool;
raw binding names are not falsely claimed identical between C and assembly.

All **327 other raw and padded owner functions** and owner pools are unchanged.
The 36 inherited owner warnings remain unchanged. The actual five-command Make
recipe produces the qualified padded object byte for byte. Shared headers,
Makefile, layout, word guards and conversion inventories are unchanged.

Independent whole-ELF prediction changes only the 232-byte target slot and
its symbol extent from 20 to 232 bytes: **191 changed bytes total**, no
metadata reordering and no exclusions. An initial shadow link used a renamed
object; the owner has overflow code, causing the linker to synthesize a FILE
symbol from that basename. Using the actual Make object's original basename
eliminates that diagnostic filename difference without altering any image data.

All **6,056 function addresses** and **6,055 other linked bodies** remain fixed.
All **189,088 protected Game data bytes / 720 owners** remain exact.
Production ELF SHA-256:
`de2f98e649839cc9c13431342b06e4bf64ac072b6e41617c775eb1afac243678`.
Native installation changes exactly the selected source, padded owner object
and ELF. All other prior 17,506 sealed inputs remain unchanged before the
explicit tools/documentation/commit refresh. There are 1,003 focused frozen inputs.

## Instruction, caller and native qualification

- **1,452 guest cases / 5,808 executions** across original assembly, isolated C,
  padded owner and actual Make object. Three code/pool address layouts cross
  HI/LO carry boundaries; all registers, reads, memory and saved state agree.
- All **54 reachable words** execute. Four duplicate count updates after
  unconditional returns (+0x6C, +0x8C, +0xAC, +0xCC) are structurally unreachable
  and remain present. The routine performs no writes or helper calls.
- Cases cover first/last/absent/multiple matches, excluded slot 25, large and
  negative ordinals, high link bytes, and signed division truncation. Invalid
  or misaligned owner byte deltas are explicitly guest-only instruction tests.
- ROM-wide aligned census finds **seven JALs and zero pointer literals**:
  ROM4B3F0 / PC1501DF40; ROM5B4F0 / PC1502E040;
  ROM9B094 / PC1506DBE4; ROM9F6A0 / PC150721F0;
  ROMA852C / PC1507B07C; ROMC5F24 / PC15098A74;
  ROMEB208 / PC150BDD58. Duplicate assembly views are not additional sites.
- **412 caller cases / 1,648 executions** qualify six original bounded call
  windows plus the complete original eight-word `func_150721E8` wrapper.
  The wrapper's 24-byte frame and saved return address survive the real nested
  call. These are interface/window claims, not complete surrounding gameplay.
- **1,008 defined-domain native cases at each of O0/O2/O3**, with UBSan and
  explicit size/field-offset assertions. Owner pointers stay within the pool
  or its legal one-past boundary. Six effective controls catch an owner-index
  error, scanning slot 25, skipping slot zero, a wrong link field, an ordinal
  off-by-one, and narrowing the ordinal to a byte.
- Both tools copies pass six fresh focused tests before and after installation,
  plus their shared checks. Byte/binding pins, body corruption and unrelated
  image corruption are rejected. Prior unchanged neighbor suites are reused
  through exact body/pool identity, not reported as freshly executed.

## Artifacts and next boundary

`conker/build/game-related-actor-lookup-15072208-match/` contains the frozen
inputs, compiler screens, original assembly object, selected isolated/owner
objects, actual Make commands, independent first link, caller census,
runtime qualification, tests, installed recount, Graphify proof and bank receipts.
Public tools are `game_related_actor_lookup_match.py`,
`game_related_actor_lookup_oracle.py`, and `test_game_related_actor_lookup_match.py`.
Graphify receives a scoped AST refresh retaining prior nodes and valid edge
occurrences; no full-corpus extraction or reclustering is claimed.

Next ordinary C placeholder: **func_150746F0**, same owner, VA150746F0,
ROMA1BA0, 61 words, 32-byte frame. Audit its complete routine and callers
before selecting a void/return contract or reconstructing its actor lookup
and helper arguments. The scalar smoothing and other private candidates remain
uncredited. No Claude calls, host/editor/Release changes or network push.
