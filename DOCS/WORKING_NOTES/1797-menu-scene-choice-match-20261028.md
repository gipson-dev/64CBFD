# 1797 - Menu scene choice callback: direct byte-exact C

Date: 2026-10-28.

`func_151E4314` is recovered as a zero-argument `void` callback. The complete
50-word / 200-byte function emits directly from semantic C, using its original
32-byte frame and 20 symbol bindings. No replacement words, guards, assembly
insertion, compiler profile changes or shared declaration changes were added.

## Behavior and provenance

- Owner: `conker/src/game/generated_20AE20.c`; original assembly:
  `conker/asm/20AE20.s`. VA `0x151E4314..0x151E43DC`, ROM
  `0x2117C4..0x21188C` (exclusive end).
- Read the active menu state's signed byte at `+0x42`, use its ten-byte stride
  to select a signed byte in `D_800AB692`, and take the fallback for negative
  selections. That path does not read the mode or scene descriptor.
- Nonnegative selections index four-byte `MenuSceneChoice20AE20` records:
  signed 16-bit scene, signed normal sequence byte, signed alternate sequence
  byte. Any nonzero `D_800E0C00[0]` selects the alternate sequence.
- Call `func_1501D348(scene, sequence, 0, 0, 0)`, then set `D_8008FD80=1`,
  `D_800E0B94=5`, `D_8008FD8C=1`, and `D_8008FD90=1`, in that order.
  Negative selection calls `func_151E2834()` without those stores.
- The two final flag stores must remain separate statements for direct
  instruction order. A chained-assignment experiment produced 52 words and
  was rejected. Symbol names are preserved; the recovered type, fields and
  function comment describe their measured roles.
- Retail descriptor provenance is the six records at ROM `0x250264..0x25027C`
  in `conker/asm/data/250030.rodata.s`. Expanded synthetic test backing verifies
  signed indexing and conversions; it does not claim larger retail tables.

There are no direct ROM JALs or aligned full-pointer words for this callback.
Original installer windows in `func_151E1214` (`0x151E15D4`, 20 words) and
`func_151E1744` (`0x151E1E60`, 21 words) construct its address with HI/LO
instructions and store it in `D_800E0A88`. The four-word invocation window at
`0x151E5014` in `func_151E4EE8` loads that pointer and uses JALR; its epilogue
does not consume a return value. These parent C placeholders remain unchanged.
The transition and fallback services have bounded effects in the oracle;
full helpers, parent gameplay and host-port behavior are not newly qualified.

## Qualification

Eight fresh focused methods passed independently in each tools checkout,
followed by each checkout's shared tools checks. After production installation,
two source/owner/image methods ran fresh per copy; six semantic methods were
reused only under exact input, module and artifact fingerprints.

- 1,760 guest cases cover all 50 words, every byte pattern in five signed/mode
  fields, boundary halfwords, overlapping guest storage, stack phases, and
  callback mutation before the four state writes.
- 288 original installer cases followed by 288 original indirect invocations.
- 24,576 defined native32 cases per optimization (`-O0`, `-O2`, `-O3`), actual
  SDK types and trapping UBSan; all 12 semantic negative controls are effective.
- 31 direct and 23 caller access-fault prefixes preserve registers, memory,
  calls, access trace, PC and delay-slot state; five direct cuts are in delay
  slots. These are guest instruction observations, not portable C fault claims.
- Original, isolated C and Make-produced objects agree across three GNU link
  layouts and 120 rebased cases; 70 raw-word/binding corruption rejections.
- All 59 other owner functions and normalized pools are unchanged. Owner,
  isolated and actual Make compilations add no diagnostics. The existing
  normal O2/g3 compile, padder and assembler sequence reproduces the object.

Private v1 failed only on fixture transport of the controller halfword and
missing `-O` prefixes in native compiler arguments. Private v2 and both canonical
executions passed after those harness fixes, without changing candidate C.

## Literal image and production audit

The actual Make build reproduces the independent whole-image prediction:
**244 changed bytes**, consisting of 159 target-code bytes, one target symbol-size
byte, and 84 bytes in two closed symbol/name-order permutations. No bytes or
sections are excluded. The permutations are:

- `D_800AB7A4`, `func_15007360`, `D_8009DA04` -> function, second data symbol,
  first data symbol, starting at symbol offset `0x2BA144`.
- `func_151A2A14`, `D_8009E7D0` -> data symbol, function, starting at `0x2D4E84`.

Names, values, bindings and section definitions remain identical, except the
recovered target size grows from 12 to 200 bytes. Headers remain identical.
Every byte in the changed metadata windows is independently corruption-tested.
All 6,055 other canonical function bodies, all 6,056 addresses, and all 189,088
protected Game data bytes across 720 owners are preserved. The conversion CSV
and inherited guard manifest are byte-for-byte unchanged.

Predecessor consumer: `b1c66fb3799a41df737c182443d2794952e411e1`.
Tools committed first: `fd5ca02a8597a48e16740a857d3f476e544e169a`.
ELF SHA-256: `d22097c62aa0d5fd7dc7a9a09af298bb794df92bfb181119ea4f6d5f3ad357c6`.
The older tools mirror's 1,832 inherited dirty paths are preserved, with only
three new target modules. No push or sibling host/Release work.

## Measured progress and continuation

Actual adopted ELF: **3,875 / 5,506 C functions exact (70.38%)**;
Game **3,202 / 4,833 (66.25%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift. Remaining: 1,631 different; 255 more reach 4,130 / 5,506
and the 75% target. Remaining shapes: 1,502 placeholders, 120 semantic/other,
nine unlocated. The wider goal stays active.

Next inspect `func_1509DDFC` in `conker/src/game_CB1C0.c` (50 words).
`func_1514E920` remains parked and uncredited.
Ignored receipts, complete immutable seals, the post-commit graph refresh,
retention audit and continuation handoff live in
`conker/build/game-menu-scene-choice-match/`. Graph work is scoped to changed
files and retains historical context; it is not a full-corpus extraction.

Claude calls: zero; local source, ROM, compiler and execution evidence resolved
this routine without advisory review. README changes are aggregate rows only.
