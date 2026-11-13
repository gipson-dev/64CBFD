# Game trajectory target screen and initializer return ABI

Date: 2026-11-13. The matched slot initializer `func_1505D1C4` now explicitly
returns the result of `func_1505C7D8`. Its three existing C declarations use
the same `s32` return type. This corrects an ABI inconsistency found while
investigating `func_150E1570`; the initializer was previously declared `void`
even though the retail trajectory helper uses its return register.

Retail `func_1505D1C4` calls `func_1505C7D8` at `0x1505D298` and does not
modify `v0` before returning at `0x1505D2B0`. Its nested routine explicitly
places its result in `v0` on both final paths at `0x1505CFD0` and
`0x1505CFD8`. The initializer still restores the saved current-object byte
after the nested call. The corrected source emits the same complete 61-word
initializer with no new guards.

A shadow actual-Make compile of the initializer and all three declaration
owners produced four byte-identical objects and an identical complete linked
ELF. A production actual-Make rebuild then confirmed all 1,454 linked objects,
the entire ELF, binary and progress CSV were byte-identical to their frozen
inputs; the shadow audit checked all 6,050 function bodies and addresses and
protected Game data. Native 32-bit UBSan checks covered 144 combinations at
each of `-O0`, `-O2` and `-O3`, including negative and boundary returned
values, saved current-object bytes, and an intervening helper mutation. The
checks model the nested routine and do not claim gameplay or hardware testing.
The existing duplicate `generated_12D630` Make recipe warning remains.

`func_150E1570` in `generated_10EA20.c` is still a zero-return placeholder,
not an installed match. Retail at VA `0x150E1570..0x150E17F4` uses a
224-byte frame and 161 body words. It builds a look-at matrix, scans 25
`0x32C`-byte actor records, chooses the first smallest nonzero signed geometry
result after filtering active/health/immunity and excluded indices, then
calls `func_1505D1C4`, copies the source's `+0x76` halfword to the selected
actor and returns the initializer's result. If the source is null, the source
index becomes -1, but a selected result still dereferences it afterward.
These observations are retail disassembly findings, not portable null behavior.
The alternate auto-decompiled source misreads several byte and signed-halfword
fields and is not suitable for direct adoption.

An ignored private source screen at
`conker/build/game-nearest-line-actor-150e1570-screen/` emits 160 words with
the retail 224-byte frame; variant `w00.c` also has the retail matrix at
`sp+0xA0` and result slot at `sp+0x88`. A simple order-only raw-word diagnostic
finds 133 ordered equal words against the linked retail image; unlinked
relocations and reordered instructions limit its interpretation. Saved
register roles, one missing control-flow word and exact scheduling remain
unresolved. Retail and raw `w00` guest instruction streams agree across 1,500 finite
modeled cases with modeled matrix, geometry and initializer helpers; an
independent eligibility and signed-score check covers exclusions, health,
immunity, source index, ties and negative scores. The initializer hook mutates
the source halfword before it is copied. These are bounded helper models, not
full geometry, alias, caller, fault, linked-image, hardware or gameplay
acceptance. The source remains uninstalled and uncredited. Continue with native
and alias controls, connected callers and exact word/relocation fit before
adopting it. No Claude call was needed.

Game remains **3,741 / 4,842 (77.26%)**, total **4,414 / 5,515 (80.04%)**,
zero drift, and **133** further Game matches are required for 80%. These totals
are unchanged from Note 2351 because all linked output was identical.

The scoped Graphify refresh retained or relocated all 59,967 prior nodes,
with 59,969 afterward. Two pre-existing historical annotations were restored
after refresh and verified; 31,816 nodes were retained fail-closed. This was
not a full-corpus extraction.
