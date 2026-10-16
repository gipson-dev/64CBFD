# Frame Timing Frontend Allocation Provenance

Date: 2026-10-16. Consumer predecessor **156f717d**, tools predecessor
**061bde1**. The preceding turn qualified the allocation and signed-zero
rejections in [Note 1451](1451-frame-timing-allocation-and-signed-zero-fit-boundary-20261016.md).
This turn identifies the actual compiler-phase boundary. **No production
source, ELF, progress, compiler profile or guard changes; no new exact match.**

## Observed Phase Boundary

func_15019F20 remains 191 body words / frame 0x18 / one trailing NOP, with
**141 actual slot-word differences**. Its owner is conker/src/game_45B80.c.
Reuse the prepared read-only CFE/UOPT/UGEN probes, wire decoder and captured
descriptor tables; do not install or modify a compiler or attach to a game.

Two final complete-owner captures finish with producer/consumer/driver exit0,
fired descriptor/load-node probes and cleanup. Complete parsed text, function
tables, relocations and pools equal the normal compile in both cases. All
109 live inputs stay unchanged. Exact source LOC markers bind these roles:

| Role | Installed Predecessor | Unsigned-Zero Control |
| --- | --- | --- |
| Byte divisor frontend home | M-2, L, one byte | Same |
| Total frontend home | M-8, L, four bytes | Same |
| Optimized byte register | R6 / A2 | R4 / A0 |
| Signed gate register | R4 / A0 | R3 / V1 |
| Extra unsigned gate register | None | R5 / A1 |
| Initial step register | R2 / V0 | Same |
| Accumulator register | R3 / V1 | Same |
| Residual address register | R9 / T1 | R8 / T0 |

The predecessor has 6,463 frontend and 6,950 optimized records for the whole
owner. Its target procedure has 276 / 427 records, selected by its exact ENT
and terminating END. The END has a different block number from ENT; do not
assume those numbers must match. The unsigned-zero control adds one frontend
conversion, giving 6,464 whole-owner / 277 target frontend records; optimized
record counts remain the same.

The residual address is already an **R9** rlda in UOPT output. Its symbol is
bound from the residual's exact source statement, and its register agrees
with the emitted HI16 instruction at **+0x64**. This rules out that register
choice first being introduced in UGEN. It does not explain why the unknown
original source rematerializes that address in separate branches.

Each capture observes **626 UGEN load-node events for the complete owner**.
Those events do not carry unique target-procedure identity; do not attribute
an arbitrary R9 event specifically to the residual. Phase/output bindings,
the actual emitted carrier and whole-object identity establish the result.
Unused wire words and generic decoded length fields are not interpreted as
allocation costs, source scope or hardware behavior.

```sh
python3 -m tools.experiments.game_frame_timing_frontend
python3 -m tools.experiments.game_frame_timing_frontend --variant unsigned-zero
```

## Discriminating Controls

Nineteen canonical, complete-owner controls test comparison promotion, an
unsigned view of the step word, a named step pointer, byte/word switches,
direct global divisor accesses, eight local declaration orders, and signed/
unsigned gate widths. None improves 141 differences; none is installed.
All 15 neighbors retain raw words/bindings, all frames stay 0x18, no private
pools appear. These are source/shape screens, **not functional qualification
of every candidate**.

- `divisor != 0U` does not remove signed promotion. The frontend adds its
  unsigned conversion, and UOPT materializes the extra R5 gate. The body is
  **190 words / 180 differences**, so reject this proposed fix.
- All eight declaration-order forms emit exactly the predecessor's raw
  words, as does the u16 gate. Do not repeat local ordering for this boundary.
- The signed s32 gate gives **189 words / 170 differences**; the s16 gate
  gives 190 / 178. Neither recovers retail's two-carrier schedule.
- A byte switch is 191 / 141 but not word-identical to the predecessor; the
  word switch is 190 / 168. Direct global divisor reads give 189 / 174.
- The unsigned step view is 191 / 142. Its named-pointer variant is **199
  words / 193 differences**, exceeding the slot; never pad/install it.

```sh
python3 -m tools.experiments.game_frame_timing_frontend --screens
python3 -m tools.experiments.game_frame_timing_frontend --step-words
python3 -m tools.experiments.game_frame_timing_frontend --switches
python3 -m tools.experiments.game_frame_timing_frontend --global-divisor
python3 -m tools.experiments.game_frame_timing_frontend --homes
python3 -m tools.experiments.game_frame_timing_frontend --signed-gates
```

## Qualification And Bank

All **five final tests pass in 72.853s**:

```sh
python3 -m unittest tools.tests.test_game_frame_timing_frontend -v
```

Fresh checks cover both completed owned captures, all 19 complete-owner
controls and all 15 neighbors per control. Reject **22** stream/table/lifecycle
corruptions, six role changes/removals, four procedure-boundary corruptions,
an unqualified capture, missing source marker and invalid variant. Revalidate
the untouched capture and restore successful receipts after negative tests;
do not leave their deliberately failed receipts as the resume state.

This is compile-time phase evidence, not retail hardware, Ares, gameplay,
complete private-state matching or recovery of the original source spelling.
The prior guest/native/alias/signed-zero/rebase/data-layout receipts are reused
because the production source and entire ELF remain byte-identical, not called
fresh runs. No normal guest rebuild is needed for this tools-only change.

Tools **dbca3c5** banks two files before the consumer pin. Both new files are
byte-identical in the active checkout and older mirror; Windows AST passes
for all four copies. Eleven shared padder tests pass in each checkout
(0.055s active; 0.031s + 0.020s mirror), and make tools-check passes. Preserve
mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **885** initial
dirty-file hashes and **887** final dirty paths; do not commit/reset it.

The full production ELF remains
**44fa0f9f11ce36d6aad05a9214d8b025c687e54bb6dbf9e857386e2f47f3ebd3**.
Keep Game **2,930/4,828 (60.69%)**, total **3,603/5,501 (65.50%)**, different
**1,898**, zero drift. Root README aggregates are unchanged. Zero Claude
calls, no push, no host-port change and no frozen Release action.

## Next Work

Keep func_15019F20's instruction match open. Its next fitting attempt needs a
new, discriminating source/dataflow hypothesis for the residual's allocation
and branch-local addressing, not a UGEN-only register fix or repetitions of
these type/order screens. Preserve Note 1451's signed-zero counterexample
and the separate zero-reciprocal access-order boundary.

For the next implementation pass, resume the adjacent **func_1501A220** in
conker/src/game_476D0.c: a still-zero-return view-initialization stub, retail
**95 words / frame 0x28**, VA **0x1501A220..0x1501A39C**, ROM
**0x476D0..0x4784C**. Its assembly stores incoming A0 and saves A1 for the final
callback. Audit its actual callers/return use, allocation sizes, live count
reloads, signed remainder/float arithmetic and existing constant ownership
before changing its interface. The old commented draft is a hypothesis, not
qualified C. This queued recovery does not complete the timing match or the
wider Game/additional-source objective.
