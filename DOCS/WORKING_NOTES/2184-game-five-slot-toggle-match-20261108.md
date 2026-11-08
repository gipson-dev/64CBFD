# Five-Slot Event Callback Direct C Match - 2026-11-08

`func_15100340` now matches all **73 words / 292 bytes**, including its
**0x50-byte frame**, directly from semantic C. **No guards** are added.
Total **4,253 / 5,513 (77.14%)**, Game **3,580 / 4,840 (73.97%)**,
Init **492 / 492**, Debugger **181 / 181**, with zero address drift.
There are 1,260 different converted functions and **158** additional exact
functions needed for 4,411 / 5,513 and the active 80% goal. Conversion totals
are unchanged.

## Source and callback interface

Owner: `conker/src/game/generated_12D7F0.c`. VA 0x15100340..0x15100464;
ROM 0x12D7F0..0x12D914. The zero-return placeholder becomes:

```c
void func_15100340(s32 view)
```

Its sole aligned pointer registration is `D_8008CD04[10]`, at
VA 0x8008CD2C / ROM 0x2317EC. The complete aligned pristine-image census
finds no direct J/JAL entry, interior entry or interior pointer literal.
The existing typed table is consumed by `func_151749F8`: its resource byte
at +B selects the callback; T9 loads the table entry at 0x15174A48, A0
reloads the parent's second incoming word from SP+1C, and JALR executes at
0x15174A50 with a NOP delay. The current semantic dispatcher names that word
`view`. The callback's result is unused.

The local five-byte `SlotIdentifiers15100340` type exposes only the copied
identifier bytes. The external object retains its original address and data
owner. There is no shared header, data-owner, caller or linker-symbol edit.
The file header now describes its recovered C and remaining assembly routine.

## Recovered behavior

Always copy five bytes from `D_80088BC0` into local SP+44 before testing
`view`. Retail identifiers are 9, 10, 11, 12 and 13. A nonzero full 32-bit
view returns after this copy. For view zero, increment unsigned byte
`D_800DD405` once, wrapping 255 to zero, then visit all five bytes in
`D_800BE500`.

For each byte, capture a threshold of **35** when zero or **70** when
nonzero, then call `func_150ADA20()`. Cast its full return word to unsigned
and compare the remainder modulo **1000** strictly below the captured
threshold. On success, reload the live state byte and XOR it with one.
Retain all higher bits; this is not a Boolean inversion. A nonzero resulting
byte dispatches command **0x18**. A zero result dispatches **0x1C**, then
**0x17**, in that order. Each call uses the corresponding local identifier
and zero as its third argument. Reload the local identifier between the
two off commands, as retail does.

The threshold precedes the RNG call, while the state reload follows it.
The local identifier snapshot precedes every helper call. A helper changing
global identifiers must not substitute a live global read for the snapshot.
Controlled guest-only changes to the local identifier qualify its repeated
read between the off commands; they are not presented as ordinary native
access to another function's private local object.

The RNG remains original restored assembly with a documentation-only C
equivalent in `game_DAE50.c`; it is not newly converted by this change.
`func_151616D0` has a semantic C implementation with u8/u8/s32 arguments
and forwards its packet through the event dispatcher. These helper bodies
are unchanged. Tests use bounded scripted helper returns and effects, rather
than claiming full execution of those transitive implementations.

## Direct compiler and whole-owner proof

The unsigned `random` result is a real local declared before the identifier
copy. This recovers the original frame and SP+44 array location. The first
source form had a 0x48 frame; declaring the meaningful RNG local before the identifier
copy produces every original word directly. There
is no artificial padding local, instruction rewrite or compiler change.
The conditional threshold expression also recovers the original branch and
its delay-slot assignment.

Raw relocatable C body SHA256:
`cb59d7df9047afeefab3430ba3ec5f7b8bcea748e38c8da9194fd73788644c9d`.
Retail linked body SHA256:
`a29688f80e22268c7aebde37d10bb3a7d6aa96cfaa7690c4073696af7590e091`.
Ten bindings cover the three global HI/LO pairs, one RNG call and three
event calls. The complete guard CSV remains byte-for-byte unchanged.
Seventy-three raw-word corruptions, ten altered bindings and 48 individual
register-metadata-byte corruptions are rejected.

The **109 frozen inputs** include the complete owner, retained GLOBAL_ASM,
caller/helper sources, original dispatcher/table data, all SDK headers,
assembler includes and compiler/link inputs. The other raw and padded
function, data pools and all register metadata remain unchanged. Strict and
production padders agree across the complete two-function owner. Its actual
five-command Make recipe reproduces the qualified object with the unchanged
retail O2/g3 profile and zero C diagnostics.

Three independent GNU links qualify global and helper rebases, including
signed low-half carries and R_MIPS_26 calls. Nine guest cases execute those
independently linked objects. The literal full-ELF predictor allows exactly
**207 changed bytes**, with **zero exclusions** and no symbol/string
permutations. Only this body and its restored symbol-size field change;
all 6,053 function addresses, other bodies, 720 protected-data owners and
189,088 protected bytes remain fixed. Four corruption controls reject
changes to code, header, size metadata and protected data.

## Execution and production evidence

Both tools configurations pass six focused checks before and after
installation in four sequential fingerprinted runs. The sibling uses a
scratch overlay for these three new files, with read-only helper fallbacks
recorded explicitly. Its HEAD and 2,434 inherited dirty paths are preserved.
Both configurations pass fresh shared smoke checks. Three unchanged shared
synthetic regressions per configuration are reused under exact helper/test
fingerprints; they are not reported as fresh runs.

- **3,098 guest cases** cover every state and counter byte, full-width views,
  unsigned RNG boundaries, both thresholds, strict equality, all-slot outcome
  combinations, six aliases and both stack phases. Helpers clobber volatile
  GPRs, floating registers, HI/LO and argument homes. Independent expected
  effects and call packets pass; retail and raw C states and ordered reads
  are identical.
- All **72 reachable words** execute. BREAK 7 at **0x151003D8** is unreachable
  because S3 is the nonzero constant 1000, preserved across helpers by ABI.
  That original defensive trap word remains present and is not credited as
  executed. **176 executed access-fault cuts** compare complete literal
  target states; full helper fault behavior is not claimed.
- **128 connected cases** execute the original 13-word callback-table,
  argument-load, JALR/delay and post-return branch window. A poisoned void
  return leaves the caller's observed behavior unchanged. Full execution
  of the larger parent is not claimed.
- **2,362 native cases per executable** pass O0/O2/O3 with trapping UBSan,
  32-bit pointers and five-byte identifiers. All public globals and event
  packets are checked. Thirteen effective controls reject a stub, ignored
  view, signed roll, inclusive comparison, exchanged thresholds, missing
  phase increment, four-slot scan, wrong modulus, Boolean toggle, stale
  state, live global identifiers, wrong second command and reversed off
  commands. Aliases and private-local mutations remain separate guest tests.

Production recompiles exactly one C owner, then links the exact predicted
ELF. Compilation/link and the fresh recount succeed. `make all` retains its
expected checksum exit 2 while other functions remain unmatched. The
Makefile, compiler profile, guard CSV and `progress.csv` remain unchanged.
README changes contain aggregate table rows only.

Production ELF: `fb078ed1821b645c2d9f5f636c2450eb4fc0f6a8734f6fe672f7cdc8f83d7b91`.
Binary: `7f895c604f7a6965ebcdb729bf1bd66b814301341c5d297d8a00de347917f2cb`.
Owner: `77585a8bef42ab1a5f1e1933ecdc19705bf9c5f9b90a8800a74d0cc6f27f026e`.
Unchanged guard CSV: `931b6ca3673b8157c374871d9065dffbf39d419211960ab9383c6503808f7f25`.

## Resume boundary

Next candidate: `func_1504ADD0`, a 73-word routine in `game_77AD0.c`.
Its current ECTS-derived actor-loop body remains unmatched. Recover and
qualify the retail 25-slot traversal, active/current-slot globals, player
record selection, temporary six-byte fallback and actor-type callback.
It is uncredited pending full caller, owner, execution and image gates.
The smaller handwritten/nonstandard-register cases remain separate work.

Scratch receipts: `conker/build/game-five-slot-toggle-15100340-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
retains unscanned existing nodes and audits changed-path relocations; it is
not a full-corpus extraction. Frozen host Release artifacts are untouched.
