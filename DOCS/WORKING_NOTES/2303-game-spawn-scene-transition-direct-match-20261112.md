# Spawn scene transition direct match

Date: 2026-11-12. `func_1507DFE4` in `conker/src/game_A9D90.c`
replaces a zero-return placeholder. Its 76-word retail body occupies VA
`0x1507DFE4..0x1507E114`, ROM `0xAB494..0xAB5C4`. It emits directly from
semantic C with the original frame and no guards or insertions.

When the scene gate is not one, the routine queries a spawn record. Results
zero and one select transition sequences one and three; other results return
without a transition. It derives an angle from the returned byte, submits the
three position coordinates, temporarily changes scene context to `0x25`,
dispatches the sequence and restores the prior context. The sole aligned retail
JAL is in the `func_15007B3C` selection window; the second input is saved but
not read. The full caller is not qualified.

The original `func_15084D70` can return without writing the outputs. Retail
then reads prior stack contents; the C source retains uninitialized locals to
reproduce the retail instructions. **Reading those indeterminate values is not
defined portable C behavior.** Guest tests explicitly seed the relevant stack
slots; native tests cover only helper paths that initialize outputs.

Guest execution covers all 76 target words across 688 cases, including 48
unwritten-output cases and 24 executions of the original query's early-exit
path. A deliberately incorrect result load fails the unwritten-result test.
The full 22-word original position helper runs in connected cases and matches
the current ELF. The original selection window passes the same cases; the
scene dispatcher and most query paths are modeled. Native SDK32 O0/O2/O3 with
UBSan each pass 160 initialized-output cases and twelve effective negative
controls. Both padding paths reproduce the independently assembled retail
object and relocations. Twelve GNU rebased links and 75 bounded guest access
cuts pass. These checks do not establish portable C behavior for indeterminate
outputs, native or hardware fault behavior, the complete caller, or gameplay.

Actual Make and the independent linked-image prediction agree: 239 changed
bytes, zero exclusions or symbol-metadata reorder groups, all 6,050 function
addresses fixed, all 15 owner neighbors preserved, and all 189,088 protected
Game-data bytes unchanged. Actual ELF SHA-256: `58662b2901281a613cc0b50456c4aa9c5dcda95a65c8391d6cb72aa3a076abcc`. The
existing whole-ROM checksum mismatch remains.

Fresh ELF recount: **3,701 / 4,840 (76.47%)** Game and **4,374 / 5,513
(79.34%)** overall, zero address drift. The Game 80% target needs 171 more
matches. Tools commit `929f2171f0b9346d2be8253cf1e927fc23c99003` precedes this consumer change.
