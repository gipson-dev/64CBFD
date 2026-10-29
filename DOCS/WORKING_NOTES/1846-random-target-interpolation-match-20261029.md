# 1846: Random target interpolation match

Date: 2026-10-29. Target `func_1518F384`, owner `generated_1BA1D0`.
VA `0x1518F384..0x1518F45C`, ROM `0x1BC834..0x1BC90C`: 216 bytes / 54 words.

The zero-return placeholder becomes a complete s32 actor callback returning 1.
Its embedded target record begins at object+0x110. Signed halfword flags at
+0x12C/+0x12E gate two independent random target initializations. A zero flag
calls `func_150ADA68`, reads the corresponding upper/lower bounds after the
helper, computes `random * (upper - lower) + lower`, and sets the flag to 1.
The second flag is checked after the first helper and target store, preserving
helper mutations. It interpolates object floats +0x30/+0x2C toward target
floats +0x128/+0x118 with `D_800A7B74`/`D_800A7B78` respectively.

The measured retail constant bits are 0x3EB7CED9 and 0x3E3E76C9, verified in
both the preserved Game-data ELF and checksum-verified retail ROM using the
Game-data mapping. They are named externs, not rounded decimal literals.
Keeping the random calls in their target expressions recovers the retail
pointer lifetime, register schedule and commutative multiply operand order.

All 54 words and six relocations emit directly from C with existing O2/g3.
The original 32-byte frame saves RA+20, uses incoming A0 home+32 and preserves
the target pointer at SP+24 across the second helper. There are 16 outgoing
argument bytes. No guards, inserted words, omissions, frame adjustments,
shared-header or compiler-profile edits. Guard and conversion CSV bytes stay
unchanged. The random helper remains its existing handwritten assembly; no
helper C credit is added.

- Eight fresh canonical methods pass in each tools copy, plus shared checks.
  Installed checks rerun two methods per copy; six semantic methods reuse
  only full input/module/artifact identity.
- Guest: 3,840 cases / 11,520 original/raw/padded executions agree in literal
  full state and cover all 54 words. Cases cover zero/positive/negative ready
  flags, signed zero, subnormals, finite extremes, infinities, quiet NaNs,
  distinct random results, both stack phases, and helper changes to fields,
  second-ready state and smoothing constants. Helper-boundary observations
  verify the preceding target store is visible before a second helper call.
- Native32 O0/O2/O3 each pass 1,920 cases with UBSan and reject eight controls:
  inverted first/second flag, wrong range, wrong target, omitted ready update,
  cached factors, wrong coordinate target and wrong return value. Native NaN
  payload equality is not claimed; finite values and signed zero compare bits.
- 108 access prefixes, three sparse ready-state executions and three layouts /
  144 rebase cases pass. The five-word original indirect dispatch window in
  `func_15113E54`, VA15113EE0 / ROM141390, passes 32 cases. It supplies the actor
  from S0 through A0, calls actor+0x38, ignores the result and advances FP.
  Callback installation is a precondition; no full parent execution is claimed.
- Full-ROM scan finds no direct JAL and one aligned full-pointer reference:
  table `D_80089D60`, index 12, ROM22E850 / VA80089D90. The data-source word
  and preserved linked data agree. The actual table installer is not executed.
- Complete owner compile/padding preserves all 60 neighbors and pools. Three
  actual Make commands reproduce the object. Four inherited CFE712 pointer/
  integer warnings in two `func_1518E4A0` and two `func_15190454` calls are
  checked exactly apart from file/line positions; no new warnings are accepted.
  The inherited duplicate-recipe Make warning remains. All 222 raw-byte/binding
  controls and 290 whole-image corruption controls reject, including every
  byte in the explicitly named metadata pair and associated string block.
- Strict independent image prediction equals production: 192 changed bytes
  = 181 target code + one symbol extent + ten named metadata bytes. The latter
  swap adjacent `D_80099418` and `D_8009EE18` symbol records/string names while
  preserving each named definition, address, type, extent and section index.
  The preimage and complete closed permutation are checked; zero exclusions.
  All 6,055 other linked bodies and all function addresses remain fixed.
  Protected Game data stays exact across 189,088 bytes / 720 owners.

The float oracle is a bounded float32 model, not hardware FCSR/exception-mode
emulation. The real PRNG seed transition, complete provider, parent, hardware
and gameplay session are not claimed as executed.

Fresh actual adopted-ELF count: **3,923/5,506 (71.25%)**, Game **3,250/4,833
(67.25%)**, Init492/492 and Debugger181/181, zero drift. **207** more to 4,130.
Tools committed first: `c758f9fff23f5e6b1d2791eab7812c5cc65c06a3`. No push. Root README gets aggregate rows only.

The scoped eleven-file AST refresh retains or uniquely relocates all 49,902
prior nodes and all 103,472 old directed relationships. The s32 interface is
retained, so no old return relationship retires. Both helper-call sites, the
callback-table word and original indirect dispatch window are source/binding
checked. Outside manifest rows and analytics remain historical; no full scan.

Artifacts: `conker/build/game-random-target-interpolation-match/`. Next screened
target `func_151E530C` needs full qualification. Parked candidates remain uncredited.
The older tools mirror retains 1,976 inherited dirty paths plus three new files.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls. The 75% matching goal remains active.
