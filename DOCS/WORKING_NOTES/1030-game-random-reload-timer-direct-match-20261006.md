# Game Random Reload Timer Direct Match

Date: 2026-10-06. Starting checkpoint: `52e9156c`.

**Game func_150D26F0 matches all 39 words / 156 bytes directly from C.**
Slot: 0x150D26F0..0x150D278C, ROM 0xFFBA0..0xFFC3C, frame 0x20.
The zero-return placeholder in
[generated_FFBA0.c](../../conker/src/game/generated_FFBA0.c) is replaced by
the flag-gated decrement/dispatch/random-reload body. Existing O2/g3 profile;
no new guards, profile override, header/metadata/data change or overflow.

## Record And Ordering Contract

The record starts at object+0x28. Its recovered prefix contains command,
base, range and timer words at +0/+4/+8/+0xC, then a parameter-block address
at +0x10. `parameters[1]` names only the start of an unknown-length trailing
block; it does not establish the full runtime record size. Native checks
bind field offsets and 32-bit pointers, not a claimed complete actor layout.

If object byte +0x78 bit 0 is clear, return without reading the step global
or changing the record. Otherwise subtract `D_800BE9E4` from the timer with
32-bit wrap, store the result, and test its signed interpretation. A result
of zero is not expired. Unsigned fields avoid signed-overflow assumptions.

On negative result, dispatch `(command, record+0x10, object[0xC], object[1])`
to `func_150D278C`, then call `func_150ADA20`. Only afterward read range and
base, computing `(u32)random % (range + 1) + base` with wrapped 32-bit addition.
Do not pre-capture those fields across callbacks or use signed remainder.

If range is 0xFFFFFFFF after callbacks, the denominator wraps to zero.
IDO's unsigned remainder sequence retains retail `break 7` at 0x150D2774,
after both calls and before the final timer store. Do not add an invented
clamp or fallback. C modulo zero remains undefined at the language level;
the specific compiled target path is qualified instruction-by-instruction.
Tests do not claim hardware trap delivery or exception-handler acceptance.

The retail updater does not define a status return. The recovered public
signature is void; no promise is made about caller-saved V0 on inactive or
non-expired paths. The actual dispatch helper remains a zero-return C
placeholder in this slice; qualification uses bounded dispatch/RNG callbacks,
not complete effect execution or a connected random engine.

## Compiler Controls

[Timer driver](../../tools/experiments/game_random_reload_timer_candidates.py)
measures **19 source forms under four profiles: 76 controls**, all with empty
compiler diagnostics. The initial unsigned-array body emits 39 words, frame
0x28, 14 differences. Reversing final addends reduces that to seven but does
not recover the frame/private home. Register hints, pointer assignment,
scopes, return declarations and volatile controls fail to produce the match.

The typed record produces all **39 words exactly**, including the 0x20 frame,
private record-pointer home, countdown branch delay and unsigned reload tail.
Both final-addend forms match under O2/g3. Plain O2 emits 38 words with 35
differences; O1/g3 emits 42 with 38 differences and is oversized. These
controls are not installed. The signed-remainder control adds retail-incompatible
signed division handling and is also rejected. The selected typed body is
separately frozen in the driver; receipts are ignored under
`conker/build/game-random-reload-timer/`.

## Qualification

[Eight timer tests](../../tools/tests/test_game_random_reload_timer_match.py)
compare retail, direct typed C and the 14-difference array C body with an
independent byte-memory reference:

- **896 gate cases**: eight flags, eight timers, seven steps and both stack
  phases, including signed boundaries and wrapped subtraction.
- **1920 reload cases**: six ranges, five bases, eight RNG words, four callback
  mutation modes and both phases. Include high-bit unsigned dividends,
  wrapped bases, and fields mutated at either/both call boundaries.
- **48 trap cases**: eight RNG words, two phases and zero denominator present
  initially or introduced by either callback. Check partial memory, call
  sequence and absence of a reload store before retail break 7.
- **1408 native 32-bit cases**: 448 gate and 960 reload/mutation cases.
  Check the complete 160-byte actor backing storage, prefix offsets,
  call arguments/order/count and global mutation. Native execution excludes
  modulo zero; its target trap is tested only by the guest runner.
- Negative controls detect missing dispatch, wrong flag bit and early field
  capture. Production checks bind the selected source, all 39 words, global
  load anchors and absence of target guards.

All non-trap cases cover 38 words; trap cases exercise the remaining break.
Together **all 39 retail words execute**. Guest tests compare every non-stack
byte, ordered external writes and calls, and saved GPR/FPR/SP/RA state at
normal return. They additionally require the decrement store before dispatch,
one gated step read, and range/base reads after the RNG call. Callback models
clobber caller-saved registers; no preservation assumption hides missing spills.

The existing TriangleOracle is unchanged. A local subclass adds only unsigned
DIVU, MFHI and the exact break-7 instruction needed by this leaf. This is a
bounded instruction oracle, not a new full emulator or a gameplay acceptance
claim. Native fixtures use the actual selected C body.

All **seven pre-install tests pass in 14.846 seconds**, no skips. All **35
post-link tests pass in 20.151 seconds**, no skips: eight timer tests, eight
packet tests, six linked-tail tests and thirteen linked-record/random-range/
sound regressions. The preceding packet checkpoint also passed its broader
92-test suite. Shared generated-slice/guard tools are not changed here.

## Linked Audit

The before receipt equals the preceding **6059-slot** checkpoint. All names,
addresses and lengths survive. **Only func_150D26F0 changes**; all other 6058
slots, including its dispatcher and the exact packet wrapper/callee, remain
identical. Target SHA-256:
`c1467f763cbd2f413164980c67fa4e311341e85d5c54ca231d4324aa73401a4e`.
Ignored before/after/audit/behavior receipts live under
`conker/build/game-random-reload-timer-test/`.

Init 164048 bytes, Init data 17376 bytes, Debugger 19800 bytes and Game data
189088 bytes are unchanged. Fresh Game-data audit checks all **720 owners**:
zero different bytes/owners. All **10646 guard rows** stay identical and
ordered. Build/progress/match-progress and project tool checks pass; the
existing duplicate generated_12D630 recipe warning remains.
No sibling source/build/save/frozen Release change or push.

Whitespace checks pass. **3100 relative links across thirteen documents**
pass, zero broken. No generated build/screen/receipt output is committed.

Fresh counts: total **3312/5462 exact (60.64%)**, Game **2639/4789 (55.11%)**,
Init **492/492**, Debugger **181/181**, zero drift, **2150** different Game C.
Converted function/byte totals do not change. README receives aggregate rows
only; detailed recovery updates remain in docs.

## Reproduction And Next

```sh
python3 -m tools.experiments.game_random_reload_timer_candidates
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_random_reload_timer_match tools.tests.test_game_effect_packet_wrapper_match tools.tests.test_game_linked_record_tail_match tools.tests.test_game_linked_record_position tools.tests.test_game_random_range_position tools.tests.test_game_object_position_sound_adapter -q -f
make tools-check
git diff --check
```

Wait for relinking before production tests. Next ordinary Game candidate:
**func_15123934**, 38 words, still a zero-return placeholder in
[game_14FF90.c](../../conker/src/game_14FF90.c), confirmed from live source.
[Retail assembly](../../conker/asm/nonmatchings/game_14FF90/func_15123934.s)
gates an indexed 16-bit state slot, saves current halfword/word fields into
per-index lanes, installs three new words, marks the slot and calls
`func_15125394` before returning one. Recover the distinct 2-byte and 4-byte
indexing, sequential overlap semantics and callback ABI; do not use the
commented draft's incorrect whole-struct indexing.

The edge helper remains at 102 differences; full Game matching stays active.
The exact packet-callee audit correction is in
[Note 1029](1029-game-float-reference-packet-wrapper-direct-match-20261006.md).
No push.
