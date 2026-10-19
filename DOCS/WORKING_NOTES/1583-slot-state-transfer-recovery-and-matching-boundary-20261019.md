# Slot-State Transfer Recovery And Matching Boundary

Verified: 2026-10-19. **Complete experimental C body; not installed or byte-exact.**

Continue `func_1508E89C` in generated_B3020 after
[Note 1582](1582-mode-dependent-type-code-complete-match-20261018.md).
VA `1508E89C..1508EB90`, ROM `BBD4C..BC040`, **189 words / 756 bytes**,
frame **0x50**. Consumer predecessor `34247408`; tools predecessor `8b851a0`.
Bank recovery tools **ad184da**, then the coverage-provenance correction
**a53e876**, then this documentation and the consumer pin at a53e876.
No production source, guard, build profile or ELF change; no push.

## Recovered Interface And Body

The actual caller at `1509E14C..1509E154` loads full words from S0+8 and
S0+12, the latter in the JAL delay slot. Recover
`s32 func_1508E89C(s32 destinationSlot, s32 sourceSlot)`; signed halfword
views apply only to the score helpers. Every retail return path produces
zero. Keep the original address name and a concise purpose comment; working
slot/state labels do not establish original source names or enums.

The complete experimental body preserves these assembly-derived operations:

1. Require unsigned `D_800D18A4[destinationSlot] >= 51` and a clear destination
   bit in halfword `D_800D18A2`. Clear the destination bit in D_800D18A0,
   set the lock bit, then set the source bit in D_800D18A0, in that order.
2. Read source score kind3 through func_150859AC, set destination kind2 through
   func_15085710, then reset source kind2. The helper argument casts are s16;
   subsequent indexing and actor selection still use the full original words.
3. If the global table's +0x18 flags are nonzero, clear the destination and
   set the source with fresh global reads. Copy source words to destination
   at +0x9C, +0x39C, +0x3DC and +0xEB0 when each **computed field address**
   is nonnull. These are not null tests on loaded pointer fields. Reload the
   table between stores; do not cache it across the operation.
4. After the +0xEB0 copy, reload the destination handle. If nonnegative, write
   the destination index into +0xF70[handle]. Always copy +0x16C0[source] to
   destination. Actor stride is 0x32C.
5. Save the destination state pointer's signed halfword +0x1AA, then call
   func_15062800(sourceActor, destinationActor). Do not retain the old state
   pointer through a helper that can replace it.
6. If mode D_800BE9F0 is 63 and destination actor byte +0x13C is at least100,
   save that byte minus100 before func_1509B570(D_800D2E48). If the returned
   script is nonnull, read the linked actor's +0x3B byte after the helper,
   subtract20 and update script+0x24B8/+0x24DC. The stored actor identity comes
   from signed actor-pointer difference divided by0x32C, not a narrowed slot.
7. Through fresh state-pointer loads, clear byte+0x84, set actor+0x125 to0x5A,
   restore the saved halfword and set state+0x1AF to0x40. Call
   func_15128774(actor->child318, actor), then increment the signed byte
   D_8008FD94. Return zero.

The final helper has **two arguments**, even though only A0 is loaded in its
JAL delay slot: A1 already holds the destination actor. Its recovered C in
`conker/src/game_14FF90.c` consumes both. Do not infer a one-argument ABI from
the last argument load. Use a local signed-byte view of D_8008FD94; the shared
variables header's different view is not changed by this experiment.

## Compiler Fitting Evidence

`tools/experiments/game_slot_state_transfer_candidates.py` preserves **27**
complete source forms. All screened diagnostics are empty. Initial C emits
189 words/frame80 with125 real differences. Typed actors/pointer difference
reduce that to103; inverse-before-source assignment and genuine local ordering
reach **189 words/frame80/100 differences**. No dummy padding, physical register
binding, volatile, scheduling guard or shared compiler change is introduced.

The qualified `FITTED` form is `homes-index-first`. Its raw SHA256 is
`6614844cb6c0714ad69f73adab4fa0214a709c66aeefac7aea114d0fcdc127fe`, with
26 relocation positions. Both complete-owner compiler profiles retain this
shape and100 differences while preserving all72 other routines and normalized
constant/table pools. The body's location and helper-call offsets agree;
equal length/frame/call offsets do not establish instruction identity.

The two typed-table screens, `address-table-fields` and
`address-table-elements`, emit the **identical raw body**, not an improvement.
Their field names/layouts are compiler experiments, not recovered shared types.
Named source-half locals produce frame88/105 differences. Signed-integer
address checks and cached field pointers also regress; retain their artifacts
rather than repeating them as untried hypotheses.

## Fresh Qualification And Limits

All **eight final tests pass in46.009 seconds**, with no skips:

- **950 fixtures**, including all byte levels/tags, signed halfwords/counters,
  mask/lock combinations, same-slot transfers, zero/nonzero table flags,
  negative/valid handles, mode gates, lookup null and helper mutation. Run each
  in two stack phases: **1,900 paired retail/C executions**. Compare public
  modeled memory, helper arguments/order and mask captures against an
  independent algorithm. Separate retail and candidate counters each visit
  **185/189 words**, not all189; neither counter is the union of both bodies.
- **46 extra guest-only pairs** cover full-word/modular slot boundaries and
  the four computed-null field addresses. These intentionally out-of-backing
  guest states are not claimed as portable C inputs or native coverage.
- Native32 **O0, O2 and O2+UBSan** each pass the950-fixture numeric corpus,
  checking71 named observations per fixture. Use the existing stack-realignment
  and no-strict-aliasing harness policy. The256-actor backing is a fixture
  allocation to cover all byte tags, not a claim about retail actor population.
  Three actually executed source controls (wrong source mask, wrong restored
  halfword and wrong final helper actor) exit21; positive variants exit0.
- **16 paired actual three-word caller windows**, using the original full-word
  loads and JAL delay slot, pass with a synthetic stop trampoline. The whole
  caller and subsequent dispatch are not executed.
- Both owner profiles preserve72 neighbors/pools and every frozen input.
  The two typed-table screen controls are freshly compiled and byte-identical
  to the qualified nonmatch.

The provider contract is explicit and bounded. GET can replace the table and
alter masks/level; SWAP and LOOKUP can replace the destination state; LOOKUP
also changes the tag and linked actor byte; FINISH can replace the counter.
Caller-saved GP/FP registers and LO are poisoned. **These tests do not execute
the real game helpers or establish whole-game, hardware, arbitrary alias,
complete ordered-read or private-RAM equivalence.**

The literal private/fault test deliberately records a **failed matching gate**.
At the first GET, retail SP+0x1C/+0x20/+0x24 contain sourceHalf/sourceBit/
inverseDestination; raw C places them at +0x18/+0x1C/+0x20. Retail destination
pointer spill+0x2C is also not the raw+0x1C home. Saved halfword+0x48 and linked
byte+0x3F do match. In the default fixture the original three words are
`[5, 32, 0xFFFFFFF7]`, versus raw `[32, 0xFFFFFFF7, 0xA5A5A5A5]`.
All72 sampled access cuts actually fire; only five full states agree, and
the first divergence is cut5. Passing this regression test means that the
nonmatch witness remains effective, **not** that private/fault parity passes.

## Production And Repository Boundary

Production func_1508E89C remains the zero-return C stub with185 linked word
differences. Do not install this candidate, generate broad normalization from
the100-word diff or take byte-exact/conversion credit for this checkpoint.
The source/guards/ELF SHA256 values remain respectively:

```text
dea4dfd12a77af3cc6f98c79d89b8854f1d6e13b56e83fb0beb7771a3d09daed
2bccb21a86652810e61c0522563b25ad229a791c1acc397a8989344810d6816e
f384fac3ed0d844cbe5f1c6165ff7ac36a3690bc62c157c7bcf9c63e14728f5e
```

Fresh match-progress remains **Game2998/4832 (62.04%)**, **total3671/5505
(66.68%)**, Init492/492, Debugger181/181, **1,834 different / zero drift**.
The existing duplicate generated_12D630 Make recipe warning remains; this is
not a new warning-free production rebuild. No production rebuild was needed.
README aggregate rows stay unchanged; this note owns the function narrative.

Both tools copies pass their three repository setup tests and project smoke
checks; consumer `make tools-check` passes. Copy only the three new ASCII,
Python-valid files into the independently dirty standalone mirror. Preserve
its ddbdd16 HEAD and all1,316 prior leaf hashes; it now has1,319 dirty leaves,
without a mirror commit/reset. Post-commit graph preservation is audited
separately in ignored `conker/build/game-slot-state-transfer/graph-audit.json`.
No compiler capture, Claude call, REA setup, sibling host or Release action.

## Resume This Same Routine

1. Run the suite below; reuse `FITTED` and the preserved27 screens as evidence.
   Fit the first-helper temporary spill block and destination pointer home
   through justified source lifetimes/types. Do not invent an unused local
   merely to shift stack allocation.
2. Recover retail's `ADDIU temporary,V0,field; BEQZ temporary` shape at all four
   computed-address checks. Raw C uses `LI AT,-field; BEQ V0,AT`, with one
   earlier constant hoist. Typed field/element views already fail to change it.
3. Resolve remaining allocation/scheduling cycles, then qualify literal
   private/fault state, real helper boundaries, full-owner/padder and rebased
   code/data behavior before any installation. A guarded layout would require
   its own exact expected-word/relocation and equivalence proof, not a blind
   replacement of100 words.
4. Only after those gates, install and reproduce the complete first/production
   image with all other bodies, addresses, data and historical guards fixed;
   refresh matching rows. The broader Game goal remains active.

```sh
python3 -m unittest tools.tests.test_game_slot_state_transfer_recovery -v
python3 -m tools.experiments.game_slot_state_transfer_candidates --screens --filter address-table
make -C conker match-progress NON_MATCHING=1
make tools-check
```
