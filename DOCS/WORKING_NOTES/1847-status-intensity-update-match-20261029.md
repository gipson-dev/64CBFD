# 1847: Status intensity update match

Date: 2026-10-29. Target `func_151E530C`, owner `generated_20AE20`.
VA `0x151E530C..0x151E53E8`, ROM `0x2127BC..0x212898`: 220 bytes / 55 words.

The zero-return placeholder becomes a complete void routine. Mode byte
`D_800E0B94 == 2` exits immediately. Otherwise a nonzero intensity byte
`D_800E0B96` decays by the low word of ticks `D_800BE9E4` times unsigned rate
`D_8008FD74`. The subtraction wraps to 32 bits, is interpreted as signed,
clamps negatives to zero and stores its low byte. Unsigned arithmetic makes
that retail wrap explicit without C signed overflow.

After decay, a nonnull `D_8008FDD4` record with signed byte+0x2B equal to zero,
positive float+0xC and float+8 above 0.5 replaces the intensity. It computes
`(level - 0.5f) * 524.0f`, truncates to s32, clamps values >=256 to 255 and
stores the low byte. The comparison gates, read order, both clamps and
signedness emit directly from C. Both prototype and definition now say void;
all eight original direct callers ignore the result.

All 55 words and ten relocations emit directly with the existing O2/g3 profile.
This is a leaf: no frame, stack access, saved registers, incoming homes,
outgoing homes or helper calls. No guards, insertions, omissions, frame
adjustments, shared-header or compiler-profile edits. The guard manifest and
conversion inventory CSV bytes remain unchanged.

- Eight fresh canonical methods pass in each tools copy, plus shared checks.
  Installed checks rerun two methods per copy; six semantic methods reuse
  only complete input/module/artifact identity.
- Guest: 8,984 cases / 26,952 original/raw/padded executions agree in literal
  full state and cover every instruction. Coverage includes all 256 values of
  mode/intensity/rate/record-flag bytes, low-word integer wrap, signed clamp,
  sparse exits, signed zero, subnormals, float thresholds, finite extremes,
  infinities and quiet NaNs. Fifty access-prefix comparisons pass.
- Nine sparse executions demonstrate that mode2 needs only its mode byte;
  zero intensity with null record needs no ticks/rate/record fields; a record
  with nonpositive activity needs no level field. Three layouts / 72 rebase
  cases and 24 guest alias cases pass, including intensity overlapping the
  record gate or a level byte so decay affects later reads.
- Native32 O0/O2/O3 each pass 7,648 defined-conversion cases with UBSan and
  explicit float-cast-overflow sanitization. Eight controls are rejected on
  5,086 fixtures safe for every tested variant: inverted mode, wrong signed
  lower clamp, wrong decay arithmetic, inverted record gate, inclusive active
  or level boundary, wrong upper cap and wrong scale. No invalid native cast
  or native alias acceptance is claimed.
- The guest corpus includes 96 invalid-conversion cases. The bounded guest
  model uses the signed indefinite word 0x80000000; these are not native C
  acceptance or hardware FCSR/exception-mode emulation. Reaching an invalid
  cast remains outside the defined portable C conversion domain.
- Full-ROM scan finds exactly eight JALs, no aligned full-pointer words.
  Each original two-word JAL/delay window runs 16 cases, including the
  `func_151E2284` delay-slot byte store. Sources: `func_151DE6D4`,
  `func_151DE8F0`, `func_151E2284`, `func_151E4264`, `func_151E43DC`,
  `func_151E4E64`, `func_151E82B8` and `func_151E83E8`. Earlier caller gates
  are preconditions; no complete parent or gameplay execution is claimed.
- Complete owner compile/padding preserves 59 neighbors and pools. Three
  actual Make commands reproduce the object with zero C diagnostics. The
  inherited duplicate-recipe Make warning remains. All 230 raw-byte/binding
  controls and 240 whole-image corruption controls reject.
- Strict independent prediction equals production: 140 changed bytes = 139
  target code + one symbol extent, zero metadata changes or exclusions. All
  6,055 other linked bodies and all function addresses remain fixed. Protected
  Game data stays exact across 189,088 bytes / 720 owners.

Fresh adopted-ELF count: **3,924/5,506 (71.27%)**, Game **3,251/4,833 (67.27%)**,
Init492/492 and Debugger181/181, zero drift. **206** more to 4,130.
Tools committed first: `5723650d485a78cd591475f90271fee6453f521e`. No push. Root README gets aggregate rows only.

The scoped eleven-file AST refresh retains or uniquely relocates all 49,955
prior nodes and preserves 103,574 valid old directed relationships. One old
s32 return relationship retires for the recovered void interface. All eight
original call windows and the leaf ABI are source/binding checked. Outside
manifest rows and analytics remain historical; no full-corpus extraction.

Artifacts: `conker/build/game-status-intensity-update-match/`. Next screened
target `func_150D2374` needs full qualification. Parked candidates remain uncredited.
The older tools mirror retains 1,979 inherited dirty paths plus three new files.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls. The 75% matching goal remains active.
