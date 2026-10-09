# Game Effect Allocation Core Match

Date: 2026-10-09

## Result

Continue [Note 1150](1150-game-effect-record-constructor-match-20261009.md)
under the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and zero
Claude calls. Restore false-zero `func_15147A80` in
[generated_174BF0.c](../../conker/src/game/generated_174BF0.c):
VA 0x15147A80..0x15147C4C, ROM 0x174F30..0x1750FC,
**115 words / 460 bytes / frame 0x38**, directly byte-exact from complete
semantic C with **zero target guards**. Correct the local core declarations
and explicit word/address casts in
[generated_175250.c](../../conker/src/game/generated_175250.c) and
[game_1897A0.c](../../conker/src/game_1897A0.c), leaving every caller
instruction unchanged. The generated_204660.c direct caller already has the
recovered interface and needs no source edit.

Start from clean parent ef1b5214 and mounted tools 658b615. The baseline ELF
is the exact Note 1150 artifact, SHA-256
`479ab6cadef42c95c2b96c3de72d6d33dd6a01d7b7159613cbb5c8fc320fc0be`.
The full-ELF audit permits only this core's 460-byte slot and its own
symbol-size field **12 -> 460** to change. All 6,058 slot addresses/extents,
every other function body and every other ELF byte stay unchanged, including
protected data and all caller bodies. Conversion CSV bytes and all **11,475
guards** remain unchanged. New ELF SHA-256:
`67d19ec4a6bc4d4aec25153efaf0fe09971064147defa5ee984c791e3f7d8404`.

The removed placeholder already counted as C: no converted-function or
converted-byte credit. Fresh matching totals advance exactly one:
**5,484 converted / 3,399 exact (61.98%)**, Game **4,811 / 2,726 (56.66%)**;
Init 492 / 492 and Debugger 181 / 181 exact, zero address drift and
**2,085 different**. Root README changes only its two aggregate matching
rows. The 144-word `func_151DA6F8` stays at **61 actual differences**;
this core's restoration does not close that matching gate or the wider goal.

## Recovered Contract

Recover the eleven-word O32 interface: request pointer, payload-byte word,
per-entry byte word, full-word active/first/second values, resource size,
full-word value, nullable optional-record pointer, byte channel and full-word
context. Core **argument 8 is a 36-byte record address**, not an extra-byte
count. The preceding wrapper's existing word named extraBytes transports this
address; its call now makes that cast explicit. Preserve that wrapper's public
word interface and byte-exact body rather than rename unrelated callers.

Read request+0x15 as an unsigned byte and multiply by the entry-size word;
read request+0xE as an unsigned halfword. Choose kind **0x4D** when bit 0x40
is set, otherwise **0x22**. Compute the allocation size as **160 + payload
bytes + count*entry bytes**, with unsigned low32 product/sum. Call the existing
func_15167A68 with all six words: kind, full context, computed size, 1,
byte channel, 1. Use its existing void-pointer return declaration.

Null allocation returns immediately, without reading the full request,
optional record or resource-count global. On success:

- Publish payload at created+0xA0 into +0x98, and payload+payloadBytes into
  +0x94. Use the published field for the latter expression.
- Copy all **28 live request bytes** into +0x10. Clear +0x2C..+0x2E and
  store the low active/first/second bytes at +0x2F..+0x31.
- When optional is nonnull, copy **nine words / 36 bytes** into +0x60
  through +0x83, using retail's three-word unrolled block-copy loop. Otherwise
  clear **only byte +0x7C**, preserving the other 35 bytes.
- Store full resource size at +0x34, full value at +0x50 and zero state byte
  at +0x38. Clear exactly four resource entries at +0x3C..+0x48 and the
  trailing pointer at +0x4C.
- When resource size is nonzero, iterate **i <= live D_80082FA0**, calling
  func_1515D480 with the original full resource word and storing every returned
  pointer, including zero. Reload the signed global bound after every call.
  Then call func_1515D440 even when the initial bound was negative, and store
  its result at +0x4C. No invented helper-failure abort or count clamp.
- Zero the three float words at +0x54..+0x5C and bzero exactly **16 bytes**
  at +0x84. Return the original allocation pointer, not a helper result.

The typed 160-byte header describes actual offsets and allocation-prefix
extent, not original field names or gameplay meaning. Padding is not initialized
merely to improve fitting. Prepared 32-bit target pointer conversions preserve
word/address transport; large sizes and record bounds are not portable invalid-C
acceptance claims. Resource-count qualification uses signed bounds **-2..3**
and live mutations to -1/3, within the four-entry header. Wider counts are not
clamped by the source and are not newly claimed valid native object accesses.

## Complete Source Fitting

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_effect_allocation_core_candidates.py)
provides **68 complete ordinary forms**: request-count ordering, conditional
kind shapes, pointer publication, declaration/type choices, full typed header,
state-store permutations and index lifetime. No truncated prefix, fake padding,
fixed-return replacement or broad retail-word normalizer.

The straightforward byte-offset form emits **117 words/frame0x38/114
differences**. Moving the unsigned count product into a meaningful local
reaches **115/0x38/50**; explicit else reaches **115/0x38/41**. Reusing the
published payload field removes one extra address-arithmetic word. The unsigned
kind local preserves retail's V0 lifetime and reaches **115/0x38/3**.
Ordering resource/value/state stores then resolves all three independent
scheduling words **directly from C**, without guards. The selected kind is
u8; an equivalent u16 experiment also reaches three differences. No volatile
kind or register patch is installed.

Selected profile results: existing IDO 5.3 O2g3 **115/0 differences**,
O2 **115/16**, O1g3 and O1 **153/149**, all frame0x38. No isolated compiler
diagnostics or pools. The target has five J26 call relocations and the actual
HI/LO pair for D_80082FA0; no layout, Makefile/profile, original assembly,
padder or word-patch CSV change is needed.

## Qualification

The [eight-test suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_effect_allocation_core_match.py)
reuses existing instruction oracles, native32 harness, owner compiler,
ELF/object/pool parsers and the actual generated-slice padder. Independent
memory and complete helper-call expectations supplement stream comparisons.

- **1,498 cases / 2,996 executions** compare complete selected/retail state,
  full high words, all 256 request-count bytes, signed resource bounds,
  optional/null allocation branches, live request/optional/global mutations,
  helper/home clobbers, original return and both SP phases. All **115 words**
  execute; complete GP/FP, memory and event states agree.
- **682 real missing-public-byte pairs** compare emitted fault prefixes;
  null fixtures need only request bytes +0xE/+0xF/+0x15 and private stack
  inputs. Six optional aliases cover request, created+0x60 self-assignment
  and the live created+0x10 record. These are emitted-access proofs, not
  portable alias/fault semantics or hardware traps.
- **76 complete compiled forms / eight samples each** include 68 ordinary
  forms, selected/three-schedule-word controls and **six effective negatives**:
  kind, request copy size, active byte, allocation size, zero length and cached
  resource bound. Each emitted stream first runs to completion; then the
  independent behavior check detects the negative. A fixture crash cannot
  count as a semantic negative.
- Preserve **10 core-owner neighbors**, and all **42 functions** across
  three direct-caller owners (11 / 8 / 23), pools and relative relocations.
  Existing diagnostic counts remain **7 / 0 / 0 / 4** across the four owners.
  Actual generated-slice padding emits all **460 bytes**, without `.space`
  or target guards. **Four independent GNU links / 288 cases** qualify
  actual HI/LO carry and J26 regions; retail-symbol owner output is exact.
- **65,536 actual native32 C cases** check full low16 patterns in high-word
  inputs, unsigned size product/sum, all header writes, bounded payload/end
  pointers, live resource bounds, optional/null cases, helper null returns
  and a **512-byte whole-object/canary comparison**. The 160/36-byte type
  sizes are checked. Allocation/resource/copy/zero helpers are bounded native
  fixtures; invalid sizes, actual helper allocation and gameplay are separate.
- **192 connected cases / 384 executions** run the complete emitted routines in the
  three direct callers (func_15147DA0 **70**, func_1515C2F0 **38**,
  func_151D7830 **63**) plus the banked **144-word trail constructor**, with
  selected/original complete 115-word core and actual linked **11-word memcpy**.
  Independently check complete allocator arguments, fixed flag bytes, copy
  lengths and return/owner publication. All 115 core words execute across
  these paths. Other allocator/resource/bzero helpers remain bounded;
  connected agreement does not make the trail's 61 differences exact or claim
  fresh exhaustive branch coverage of that unchanged caller. Its earlier
  standalone qualification remains a historical receipt.

Final pre-install eight-test run passes in **110.135s**. Aligning the allocator
declaration to its existing void-pointer return preserves the exact stream;
fresh profile/copied-owner checks then pass in **10.316s**. Final post-install
**eight tests pass in 73.219s**, no skips. Fresh **25 shared padder/linker tests
pass in 0.348s**, and both local tools checks pass. Preserve the duplicate
generated_12D630 recipe warning and seven unchanged production-owner diagnostics.
Historical whole-ELF suites are not blanket reruns against the new baseline.

Twenty-one mounted/mirrored tool files parse and match exactly. Scoped relative
link validation checks **137 documents / 4,180 links / zero broken** before
the parent commit.

## Receipts And Banking

Ignored `conker/build/game-effect-allocation-core-test/` receipts include
baseline.json, before.elf, before guards/progress, slot.json, guest.json,
faults.json, forms.json, owner.json, native.json, callers.json, linked.json
and after.json. Separate ignored screens live in game-effect-allocation-core/.
Preserve the captured baseline; commit no ROMs, binaries, generated temporary
sources, progress CSV or private state.

Per "Keep commited", mounted tools
**2807f5152553b763aaee45b927850fe72f8bc837** is committed first; parent
source/docs/gitlink pins exactly that commit. Mirror only the two absent new
files, checking exact bytes. Preserve older standalone HEAD ddbdd16, its
independent owner-pool/effect-test fingerprints, unrelated untracked paths
and history. No push, pause, reset or duplicate standalone commit.

Manual Graphify refresh refuses 16,940 nodes over retained 38,729, preserving
19,398 nodes from 2,972 excluded files still on disk. Do not force overwrite
or change dependencies/accounts. No OGL/Release, runtime/save/editor or bridge
work. Graph repair and hardware/gameplay remain open.

## Next Work

Recover neighboring false-zero **func_15147C4C**, VA 0x15147C4C..0x15147D1C,
ROM 0x1750FC..0x1751CC, **52 words / 208 bytes / frame0x38**, in the same
owner. It selects an optional input from flags, forwards a signed-halfword
argument, invokes func_151462C8 and conditionally dispatches an actor callback.
Alternatively continue the trail constructor's 61 real layout/register/
scheduling differences. Preserve this complete exact core and wrapper;
keep wider helper/hardware/gameplay acceptance as separate gates.
