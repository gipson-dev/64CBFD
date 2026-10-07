# Game Actor-Gated Packet Match

Date: 2026-10-07. Baseline: `5a9f4436`,
[Note 1076](1076-game-record-query-direct-match-20261007.md).
Recover `func_15143E94` from its zero-return C placeholder. No shared-header,
production-profile or padder-algorithm changes.

## Retail Contract

98 words / 392 bytes, frame `0x38`, VA `15143E94..1514401C`,
ROM `171344..1714CC`. Two full-word inputs: command and flags. Return a byte,
zero on either failed gate and one after packet submission, irrespective of
the submission helper's return value.

Snapshot `(s8)(D_80082FA0 + 1)`. The unsigned increment preserves the retail
ADDIU wrap without native signed-overflow undefined behavior. A nonpositive
signed-byte count reads no actors. Scan ascending `D_800CC2D0` records of
stride `0x32C`, unsigned health byte `0x1CA`, stopping at the first nonzero
health. Reset the signed-byte index and independently scan all indices up to
the snapshot count with `func_150A29C8(index, flags)`, stopping at its first
zero return. Do not begin that second scan at the healthy actor's index.

On success, read the live context index `D_800BE9E8` and pointer `D_800DBFF0`;
call `func_1512D748(base + index * 0x9A0, command, 1)`. Then initialize the
eight-byte packet at frame offset `0x28`:

| Offset | Value |
| --- | --- |
| `0` | Byte 1 |
| `1` | Untouched |
| `2` | Signed halfword `(first RNG & 15) + 20` |
| `4` | Byte `(second RNG & 3) + 4` |
| `5` | Byte 1 |
| `6` | Signed byte -1 |
| `7` | Untouched |

Keep both RNG calls in order, including the first two packet stores in their
delay slots. Submit with `func_151D8868(&packet, 0, 255, 0)` and set the result
byte at frame offset `0x37` to one. The submission helper copies all eight
packet bytes; clearing the two untouched bytes would change retail behavior.

The shared checker declaration narrows its arguments to u8/u16. Its original
body accepts complete incoming words. This owner isolates that legacy
declaration during header inclusion and declares the word ABI locally.
No shared header or other owner is changed. Use the existing real actor and
context structures in production; synthetic padded types belong only to tests.

## Compiler Recovery

[Driver](../../tools/experiments/game_actor_gated_packet_candidates.py) retains
116 measurements: 64 gate/declaration/flag/input-type controls, 48 short-flag
storage controls and four selected-profile controls. Additional disposable
screens explored packet representations, gate lifetimes and opening forms;
these are screening evidence, not installed or fully behavior-qualified forms.

The original word-flag candidate had 98 words but frame `0x40`. Short gate
flags recover frame `0x38`; result/count/index/flags before the packet recover
both original private offsets. Selected O2/g3 emits 87 exact words directly.
Eleven differences remain only in the opening `0x20..0x4C` initialization
window; no private frame/offset patch is used.

Eleven expected-word and expected-relocation guards normalize that closed
schedule. Count-load/add/shift/shift/branch dependencies remain unchanged.
The branch moves one word, so its relative displacement changes from 19 to
18, but its absolute taken target remains `15143F20`. Actor-base HI16/LO16,
stride initialization, result-byte clear and gate-zero initialization move
with their actual owners. Both fall-through schedules converge at `15143EE4`.
On the nonpositive branch, the retail delay slot sets volatile a0 to the stride;
the raw delay slot clears v0. That a0 value is unused before return. Do not
describe these as eleven identical branch/delay words or as a frame fix.

## Qualification

[Ten maintained tests](../../tools/tests/test_game_actor_gated_packet_match.py):

- 8192 paired raw-C/retail guest cases exhaust every count byte, four health
  positions, four checker-stop positions and both stack phases. Results and
  calls agree with an independent reference. Complete final mapped memory,
  interleaved external call/read/write traces and saved GPR/FPR state agree
  with retail.
  The private opening store/read ordering intentionally differs before guards.
- All 96 reachable words are covered. Two duplicated increments at `15143F04`
  and `15143F4C` are dead after branch-likely conversion, not executed coverage.
- 362 callback/RNG cases include full-word flags/commands, callback changes to
  the count and live context, zero/nonzero submission returns, all 16-by-4 RNG
  low-bit combinations and high-word count extrema. Caller-saved registers and
  FPRs are clobbered at every modeled external call.
- Nonpositive counts and failed gates prove lazy actor/context reads. Required
  unmapped reads fail closed. 32 poisoned-padding cases preserve byte1/byte7
  at submission. The full eight-byte payload is checked by the guest oracle.
- 18856 actual freestanding 32-bit native calls qualify the defined packet
  fields, typed word arguments, gates, snapshot/live behavior, RNG boundaries
  and unsigned increment extrema. Native padding values are not claimed.
- Four profile and 48 storage controls preserve bounded defined behavior;
  alternate layouts are not equivalent private-memory proofs. A narrowed
  checker signature demonstrably loses upper flag bits.
- Twelve cases execute the two original call/delay pairs at `150BAA8C` and
  `150BACB8`, connected to the recovered target. Check command5/flags4022 and
  the latter's float-store delay word. Earlier setup and return scaffolding
  are seeded/synthetic; these are not complete caller qualifications.
- Six compiled negatives detect missing health gates, inverted checker status,
  narrowed flags, a wrong RNG mask, zeroed packet padding and dependence on
  submission success.
- Copied owners retain all 89 symbols, all 88 neighbors' bytes/relative
  relocations, the relocation-owned 624-byte pool and the same two warnings.
  Raw target bytes/13 relocation identities agree with standalone C. Actual
  post-processing/padding emits all 98 retail words. Alternate addresses test
  HI16 carries and helper relocation targets; stale word/relocation guards fail.
- Production source, linked slot and the complete guard history are checked.

Synthetic fixtures map up to 127 actor health bytes to exhaust the signed-byte
count domain; this does not prove that retail's real 26-record actor array may
be indexed beyond its valid range. External helpers/RNG are modeled here, not
fully executed or accepted in gameplay. Bounded instruction/native tests do not
claim hardware behavior, complete callers or host adoption.

## Production Audit

US ELF rebuild passes. Across all 6059 linked slots, only `func_15143E94`
changes. Every address/extent and protected `.init`, `.init_data`, `.debugger`
and `.game_data` section is unchanged. All 720 Game-data owners / 189088 bytes
remain exact. The prior 10855 guards are pinned unchanged; eleven new
scheduling guards total 10866.

Matching: total3349/5465 exact (61.28%), Game2676/4792 (55.84%),
2116 different, zero address drift. Conversion remains total5465/6042 (90.45%),
Game4792/5321 (90.06%); the placeholder was already counted as C.
README updates aggregate matching rows only. Detailed results belong here
and in the update log.

All 131 expanded post-link regression tests pass in 692.507 seconds with zero
skips, errors or failures. After strengthening the interleaved external call
trace and correcting alternate-profile frame reporting, the final ten packet
tests pass again in 61.780 seconds, likewise without skips/errors/failures.
The corrected experiment driver scans for the actual negative SP adjustment;
O1 may perform global loads before allocating its frame. All 116 saved objects
were frame-audited; selected O2/g3 remains frame0x38, both O1 forms frame0x28.
The legitimate late-initialization storage generator was also corrected after
the unsigned-count change, and every storage variant now gets bounded behavior
and complete body-length checks. None of these test/reporting corrections
changes the installed candidate or its guards.

Final tool/syntax/diff checks pass. Documentation: 59 documents / 3668 relative
links / zero broken links. Final post-regression linked audit passes with only
the target changed, no address/extent/protected-data drift and all prior guards
unchanged. No sibling/frozen Release/save/runtime or push work.

## Resume

Next forward placeholder `func_1514401C`: 98-word leaf at ROM `1714CC..171654`.
Original inspection shows a low-u8 table index and mode flags, two word pointers,
live tick scaling and a fixed-point cursor bounded by `(table byte << 16) - 1`.
Recover upper/lower mode priorities, stop/reflection/wrap updates, pointer alias
read/write order, signed division/remainder and trap boundaries before installing.
This inspection is not a semantic C recovery or complete caller qualification.
Original caller `func_1515BAE0` in `asm/188F90.s` calls at `1515BB80`
(ROM `189030`): index byte at object `0x10`, velocity pointer at `0x1C`,
cursor pointer at `0x18`, mode byte at `0x12` loaded in the delay slot.
The following instruction masks the returned status to u8. First recover the
typed updater, then qualify distinct/aliased pointer semantics and mode/trap
boundaries, and finally connect this original setup/call/delay fragment before
installation. These addresses are static inspection, not caller execution.
Sampler `func_151432BC` still needs two path-local exits/circle-byte scheduling;
oriented `func_15142600` still has 27 private-layout differences. Neither is
installed. No sibling project, frozen Release, save/runtime or push work.

Ignored receipts: `conker/build/game-actor-gated-packet/` and
`conker/build/game-actor-gated-packet-test/`. The broader matching goal stays active.
