# Record planar phase offsets — guarded C match

Verified 2026-10-28. Restore `func_15131828` in
`conker/src/game/generated_15D730.c`: VA 0x15131828..0x151318E8,
ROM 0x15ECD8..0x15ED98, 48 words / 192 bytes, frame 24 with only RA saved.
The normal O2/g3 C body preserves the complete instruction layout and four
relocations. Two checked guards restore retail's floating multiply operand order.

## Recovered behavior and interface

`void func_15131828(u8 *record, f32 *amplitudes, u8 *phases, u8 *rates)`

For each of two channels, call `func_151423D8` with the phase byte minus
0x40, truncated to a byte. Multiply its result by the corresponding amplitude
and write the planar offsets at record +0x4C and +0x54. Advance the phase
bytes by their rates times the live `D_800BE9E4` tick word. Unsigned products
preserve the retail 32-bit wrap; byte stores truncate the final values.

The helper call is a separate statement before each amplitude load. An earlier
raw-exact expression left evaluation order unspecified and failed the native
O0 test when a bounded helper changed the amplitude. That candidate is rejected
and retained under `rejected-unsequenced-native/`. Both explicit operand orders
and four additional source shapes were screened; none was a direct raw match.
The chosen C retains explicit sequencing without artificial locals or storage.

Retail reloads the tick word after the first phase store and captures the second
phase before that store. Guest overlap checks qualify those exact emitted reads,
including phase/tick aliases and deliberately changed incoming argument homes.
They are not a portable C alias or fault-order guarantee.

## Two narrowly derived guards

Both guards exchange only fs/ft on a mul.s instruction. Opcode, result register,
position, surrounding instructions and relocations stay fixed. The existing
manifest is retained byte for byte, followed by these two rows:

| Offset | Compiler word | Retail word |
| --- | --- | --- |
| +0x3C | 0x46002182 | 0x46040182 |
| +0x70 | 0x46004282 | 0x46080282 |

The raw body SHA-256 is
`e7d3ebd81315a88742503cb9600ef1901aeeb1d9a0c4f4d77b88ff8cc4898220`.
The normalized body/original object SHA-256 is
`49c94c0df53326b2f9468b6c5067aa037f578b96a0eadce6622f1cdd96c385f0`.
Bindings remain +36/+80 J26 to `func_151423D8`, and +108 HI16 / +116 LO16
to `D_800BE9E4`. Guard derivation and the actual production padder reject
changed expected words or bindings. No insertion, deletion, branch fixup,
frame repair or relocation adjustment is used. Native tests use finite values;
no general NaN payload, FCSR or hardware exception claim is made.

## Original callers and retained helpers

The full ROM census finds four call sites and no target-address literals:

| Original caller | Call VA / ROM | Caller words | Executed cases |
| --- | --- | ---: | ---: |
| func_150AF6E4 | 0x150AF708 / 0xDCBB8 | 21 | 96 |
| func_150DA628 | 0x150DA64C / 0x107AFC | 21 | 96 |
| func_150E8824 | 0x150E8838 / 0x115CE8 | 12 | 96 |
| func_151D4D04 | 0x151D4D28 / 0x2021D8 | 21 | 96 |

All callers pass record, record +0xAC amplitudes, record +0xA8 phases and
record +0xAA rates. They ignore the target result and return their own 1.
The three longer wrappers then call `func_15131958(record +0x58, record[+0xB4])`
with the latter float passed as its raw O32 argument word. Their semantic C,
objects and legacy unused s32 target declarations remain unchanged. Current
caller ELF bytes equal retail, and every caller word and return path executes.

The retained 27-word trig helper, its 65-float table at 0x8009A220, and the
19-word damping helper are checked against the current ELF/retail evidence.
All 46 helper words execute. An additional 512 cases exercise the actual trig
helper across every input phase byte. Bounded mutable helper tests separately
stress sequencing; they do not claim the retained trig helper has side effects.

## Qualification and production audit

Both tools copies pass eight fresh canonical methods and shared tool checks.
After installation, each runs two fresh installed checks and reuses six semantic
checks only after exact module, frozen-input and qualified-artifact fingerprints.
The final canonical run also removes the test file's trailing blank line caught
by Git whitespace review; its refreshed fingerprints and receipts are retained.

- 2,777 guest cases, including 25 aliases, cover every phase/rate byte,
  wrapped tick products, late pointer reads and all 48 target words.
- 324 fired access-prefix pairs preserve complete state, trace, PC and delay slot.
- Native32 O0/O2/O3 each pass 6,144 cases and seven effective negative controls,
  with trapping UBSan, the actual four-argument void function pointer, complete
  record fences and input/output comparisons.
- Three GNU layouts pass 36 guest cases with original, guarded and actual Make
  objects, including independent J26 and HI16/LO16 rebases. Three raw/binding
  corruptions and four actual padder guard corruptions are rejected.
- Five actually compiled IDO semantic mutations fail expectations. Six strict
  whole-image corruptions are rejected.

The 31-function owner preserves all 30 neighbors, both GLOBAL_ASM routines and
all pools. The five-command actual Make recipe reproduces the qualified object
with zero compiler diagnostics. The full production build retains its known
duplicate generated_12D630 recipe warning; it is not a warning-free build claim.

The seal covers 16,343 paths and 348 focused frozen inputs. Independent image
prediction accounts for all 149 changed bytes: 148 code bytes and one symbol-size
byte (12 -> 192), with zero exclusions. All 6,056 function addresses, the other
6,055 bodies, and 720 protected Game data owners / 189,088 bytes stay fixed.
Shared headers, helpers, current callers, conversion inventory and inherited
guard bytes are preserved. No emulator or gameplay acceptance is claimed.

## Bank and measured progress

Predecessor consumer: `9734d51afe8a444e491c3e884c8f45a4bded0810`.
Tools committed first: `82cde4ea29d465784e7c8942095f38f134610c60`.
The older standalone tools mirror retains all 1,775 inherited dirty paths,
with only the three new qualification modules added. No push is performed.

Adopted ELF SHA-256:
`3c81e36f7918af9b6d8b869107e1cad4dd6de9b4bfa25ba5d3af2dcb9faea977`.
Guard manifest SHA-256:
`4d5db7992914b7209e0976f4569be48fd6b3b36a850fc0b35140fc097209b840`.
Raw receipts: `conker/build/game-record-planar-phase-match/`.

| Section | Byte-exact C | Different | Address drift |
| --- | ---: | ---: | ---: |
| Total | 3,856 / 5,506 (70.03%) | 1,650 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,183 / 4,833 (65.86%) | 1,650 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

These counts come from the adopted native ELF. The 75% threshold is 4,130 exact
C functions, leaving 274 more. Next inspect `func_15138BC0` in `game_161520`;
its 48-word queue entry is only a screen. `func_1514E920` stays parked and uncredited.
