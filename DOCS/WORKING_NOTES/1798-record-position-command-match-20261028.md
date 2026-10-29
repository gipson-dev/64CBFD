# 1798 - Record position command: direct byte-exact C

Date: 2026-10-28.

`func_1509DDFC` now implements the record position command with its recovered
three-argument, signed boolean interface. All 50 words / 200 bytes emit directly
from semantic C, including the 40-byte frame, saved-register lifetime and five
symbol bindings. No guards, replacement words, assembly insertion, shared
declaration changes or compiler profile changes were added.

## Behavior and provenance

- Owner: `conker/src/game_CB1C0.c`; original assembly:
  `conker/asm/nonmatchings/game_CB1C0/func_1509DDFC.s`.
  VA `0x1509DDFC..0x1509DEC4`, ROM `0xCB2AC..0xCB374` (exclusive ends).
- Mode zero clears bit `0x2000` from the command's actor reference at `+8`,
  resolves its actor slot through `func_15084000`, then calls `func_15178BE4`
  with the low byte of the record ID, the actor's position pointer, and the
  signed command halfword at `+0xE`. Actor records use stride `0x32C`, with
  `x_position` at `+0x14` in `D_800CC2D0`.
- Mode one calls `func_15178C34` with the low byte of the ID and the command's
  full-word values at `+8`, `+0xC`, `+0x10`, and `+0x14`. The original helper
  narrows the last argument to signed 16 bits and packs the coordinate fields.
- Both supported modes return one. Every other full-word mode returns zero
  without dereferencing the command or rereading the incoming ID home.
- The existing SDK structures and helper declarations provide the types.
  The obsolete placeholder declaration, misleading stub comment, and old
  commented draft were removed. That draft incorrectly reversed the mode-one
  and default behavior. Seven neighboring functions remain unchanged.

The full-ROM census finds no direct JAL and one aligned callback pointer at
ROM `0x22CFB0`: entry seven of `D_800884D4`, corresponding to opcode eight.
The table is present in `conker/asm/data/22BEF0.rodata.s`. Two original dispatch
routes are qualified as bounded instruction windows:

- `func_150ADAF0`: 23 words at VA `0x150AE12C`, ROM `0xDB5DC`; 64 cases cover
  the zero-op gate and opcode eight. The window loads the mode from command
  `+4`, removes header bits `0xF000` from the record ID, and calls the table
  entry with the command pointer. JALR is at `0x150AE180`.
- `func_1509BFB0`: 12 words at VA `0x1509C0D8`, ROM `0xC9588`; 32 cases cover
  index seven, the caller's saved mode, and command backing at `D_800D2F60`.
  JALR is at `0x1509C100`. This parent remains retained assembly; the first
  parent remains a C placeholder. Neither is represented as a recovered C
  caller or credited as a complete parent function.

## Sequencing and matching

The record ID parameter is `volatile s32` to preserve the conditional incoming
argument-home reload after actor resolution. A nonvolatile control emits 49
words and performs an extra ID-home read on the invalid-mode path. Its sampled
public result is the same; it is a scheduling/access control, not an effective
functional negative. The qualifier is a matching mechanism and does not prove
the historical source used `volatile`.

An initial byte-exact candidate nested actor resolution inside another call's
argument expression. Native `-O0` callback mutation exposed an unspecified C
argument evaluation order: the command halfword could be read before resolution.
The final source explicitly assigns `objectIndex = func_15084000(...)` first,
then submits the position command. This preserves all 50 retail words and
guarantees the required halfword read follows resolution. Only the final,
sequenced source passed private v2 and canonical qualification and was adopted.

## Qualification

Eight fresh focused methods passed independently in each tools copy, followed
by each copy's shared tools checks. After production installation, two
source/owner/image methods ran fresh per copy; six semantic methods were reused
only with identical input, module and qualified-artifact fingerprints.

- 1,248 direct guest cases cover all 50 target words, every record-ID byte,
  full-word modes, delayed halfword and argument-home reads, and actor strides.
- 240 connected cases execute original `func_15084000`, `func_15178BE4`,
  `func_15178C34`, and `func_15178B98`: 82 literal words, 81 reachable words.
  The duplicate lookup load at `0x15178BCC` is unreachable and remains included
  in literal matching. The actor provider `func_1505EEF4` remains a bounded
  service in these cases, not a newly qualified complete helper.
- 96 original indirect caller cases cover the two windows above.
- 43,008 defined native32 cases per optimization (`-O0`, `-O2`, `-O3`) use
  actual SDK types and trapping UBSan. Nine semantic negative controls are
  effective and terminate without incidental faults.
- Native cases use valid backing for all 26 actors, including indices zero
  and 25. Synthetic guest negative-index, wrapping-address and incoming-home
  mutation cases are instruction observations, not portable C domain claims.
- 74 direct/connected and 55 caller fault-prefix pairs preserve complete
  observed state, PC and access trace. Fifteen direct cuts are in delay slots.
- Three GNU layouts and 108 rebased cases agree for original, isolated C and
  Make-produced objects; 55 raw-word/binding corruptions are rejected.
- The normal O2/g3 compiler, plain retail padder and assembler sequence uses
  three actual Make commands. Isolated and owner compilations add no diagnostics;
  all seven neighboring functions are preserved. The inherited duplicate
  `generated_12D630` Make recipe warning is unrelated to this target.

These tests qualify the target and specified original instruction windows;
they do not establish full-parent, gameplay or host-port acceptance.

## Literal image and production audit

Actual Make and production linking reproduce the independent complete-image
prediction: **153 changed bytes**, comprising **152 target-code bytes and one
target symbol-size byte** (12 to 200 bytes). No metadata reorder or excluded
bytes are needed. Nine image corruption controls are rejected. Headers and all
named symbol definitions remain identical except the target size.

All 6,055 other canonical function bodies, all 6,056 addresses, and 189,088
protected Game data bytes across 720 owners are preserved. The conversion CSV
and inherited guard manifest are byte-for-byte unchanged.

Predecessor consumer: `da53df76fdbfe0cd55641040eef4dd8e9e76a3cd`.
Tools committed first: `0d594c39d745b9ff48ca0d1e91c6f004a495d351`.
ELF SHA-256: `3207865bdc54d4a01f11b5043641e90d19191bc2d09755d6ad6ba419693ca585`.
The older tools mirror's 1,835 inherited dirty paths are preserved, with only
three new target modules. No push or sibling host/Release work.

## Measured progress and continuation

Actual adopted ELF: **3,876 / 5,506 C functions exact (70.40%)**;
Game **3,203 / 4,833 (66.27%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift. Remaining: 1,630 different; 254 more reach 4,130 / 5,506
and the 75% target. Remaining shapes: 1,501 placeholders, 120 semantic/other,
nine unlocated. The wider goal stays active.

Next inspect `func_150A019C` in `conker/src/game/generated_CD5A0.c` (50 words).
`func_1514E920` remains parked and uncredited. Ignored receipts, immutable
seals, post-commit graph retention proof and the continuation handoff live in
`conker/build/game-record-position-command-match/`. The graph refresh is scoped
to changed files and preserves historical context; it is not a full-corpus
extraction. Original assembly dispatch routes are recorded as annotations.

Claude calls: zero. README changes are aggregate rows only.
