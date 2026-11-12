# Animated texture packet renderer match

Date: 2026-11-12. `func_15167C58` in `conker/src/game_1944C0.c`
replaces a zero-return placeholder. Its 75-word retail body occupies VA
`0x15167C58..0x15167D84`, ROM `0x195108..0x195234`. The C body emits 75
words with the original frame and helper interfaces; 42 expected-word guards
normalize compiler temporary-register allocation and the independent render
mode table-read schedule. There are no inserted words.

The callback selects a texture frame from the animation phase, prepares the
texture, copies five signed screen-packet fields and an alpha byte from the
state, configures the render mode, and returns the result of the projected
packet renderer. The original `func_151674F8` renderer window dispatches it
from descriptor 3 at `D_8008B4A8` and uses the returned display-list pointer.
Only this dispatch window is qualified, not the full renderer.

Retail sign-extends the mode byte before comparing it with positive 255, so
the branch selecting mode 9 is unreachable for every byte value. Guest tests
exercise 240 cases and visit 72 of 75 retail instructions; the three unvisited
words are that unreachable branch. They cover signed animation indices, all
mode-byte sign categories, helper mutations and original dispatcher behavior;
helpers are modeled. Native SDK32 O0/O2/O3 with UBSan each pass 40 valid cases
and ten effective negative controls. Both padding paths reproduce independently
assembled retail instructions and relocation bindings, and reject 84
deliberately corrupted expected words. Twelve GNU rebased links and 105 bounded
guest access-cut triples pass. These tests do not establish native or hardware
fault behavior, the complete renderer, or gameplay.

Actual Make and independent linked-image prediction agree: 226 changed bytes,
zero exclusions or symbol-metadata reorder groups, all 6,050 function
addresses fixed, all 41 owner neighbors preserved, and all 189,088 protected
Game-data bytes unchanged. Actual ELF SHA-256: `b22b3c750933b965f25ff2524454bd40fac84eb209deb1dcedda6cf0fe5dbeb1`. The
existing whole-ROM checksum mismatch remains.

Fresh ELF recount: **3,700 / 4,840 (76.45%)** Game and **4,373 / 5,513
(79.32%)** overall, zero address drift. The Game 80% target needs 172 more
matches. Tools commit `d84f225a1a1602a1d359085ba4ef9d7d945a60c8` precedes this consumer change.
