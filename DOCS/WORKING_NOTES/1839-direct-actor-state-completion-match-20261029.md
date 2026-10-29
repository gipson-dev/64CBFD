# 1839: Direct actor state completion match

Date: 2026-10-29. Target `func_150BE210`, owner `generated_EB340`.
VA `0x150BE210..0x150BE2E8`, ROM `0xEB6C0..0xEB798`: 54 retail words.

The zero-return placeholder is replaced by a complete one-pointer void callback.
It skips when the low two bits of actor byte +0x73 equal 3. Otherwise it calls
`func_1511650C(actor,1,0x62C,500.0f)`, then reads the potentially changed actor
fields. Flag bit 4 at +0x4F selects adding float +0x64 to +0x84; the other path
clamps +0x84 above 270.0f. A strict comparison above 360.0f completes the state:
clear then set its two low bits, clear float +0x64 before calling
`func_100111C8` with the unsigned +0x74 halfword, then clear that halfword.
The helper can change fields; in particular, writes made by the final helper
after the speed clear remain observable. The initial state gate is not rechecked
after the first helper. No unrelated actor fields are modified.

All 54 words emit directly from semantic C with the default retail O2/g3 profile.
The initial byte mask `0xFC` left one immediate different. Recovering its promoted
`~3` expression produces the original `andi 0xFFFC` and closes the match. The
original 32-byte frame saves S0 and RA at +0x18/+0x1C; no incoming argument homes
are reloaded. No word guards, insertions, omissions, frame adjustments or compiler
profile changes are added. The complete inherited guard CSV remains byte-identical.

The retail function includes an unreachable duplicate `mtc1 at,f2` word at
function offset +0x60 / VA 0x150BE270. Static control flow certifies it is
unreachable from the ordinary function entry, and dynamic coverage equals all
53 reachable words. The byte comparison still includes the complete 54-word
body, including the unreachable word. No coverage or image exclusion is used.

The aligned ROM scan finds no direct JAL encodings and one full pointer at ROM
0x22D9A8 / VA 0x80088EE8. This is index 50, stride 12, of `D_80088C90`, with
the other two entry words zero. Original script code in CBDB0.s installs the
first word at actor+0x38. The original 5-word dispatch window in
`func_15113E54`, VA 0x15113EE0 / ROM 0x141390, loads that callback, passes the
actor pointer, ignores v0 and increments its loop counter. Earlier parent gates
are preconditions; complete parent execution and additional caller conversions
are not claimed. Computed/encoded references are not excluded by the aligned scan.

Validation passed:

- Eight fresh checks independently in both tools copies, plus shared tools
  checks. Installed checks rerun two methods per copy; six are reused only by
  complete input/module/artifact identity.
- 17,286 guest cases / 51,858 executions compare original, raw C and padded C
  in full registers, FP state, RAM, calls, events, memory traces and HI/LO. They
  cover unsigned/high state bits, signed zeros, 270/360 boundaries and adjacent
  floats, infinities, quiet NaNs, helper field mutations, unsigned handles and
  both stack phases. All 53 reachable words execute; the static CFG accounts
  for the remaining scheduling word.
- Native32 O0/O2/O3 each pass 8,643 cases with UBSan and reject seven controls:
  whole-byte gate, inclusive completion, wrong clamp, cached pre-helper phase,
  late speed clear, omitted stop and an incorrect state recheck. Stop-boundary
  observations check state, zero speed and the full unsigned handle. Native
  NaN payload equality and hardware FCSR behavior are not claimed.
- 72 dispatched memory-access prefixes agree in literal state. The completed
  state path needs only its state byte, valid stack and return context; no float
  fields, handle or helpers. Three GNU layouts pass 432 cases. The original
  indirect dispatch window passes 108 cases.
- All 216 raw-byte and two binding corruption controls reject. The complete
  compact/padded owner preserves seven neighbors and pools. Three actual Make
  commands reproduce the qualified object, with zero C diagnostics. The
  inherited duplicate-recipe Make warning remains.
- Strict independent full-image prediction equals production: 154 changed
  bytes = 153 target code + 1 target extent, zero metadata rearrangements or
  exclusions. All 6,055 other linked bodies and all function addresses stay
  fixed. Protected Game data stays exact across 189,088 bytes / 720 owners.

Helper contracts are bounded and use the caller-observed arguments. Their
implementations receive no new C credit, and this is not gameplay/hardware
acceptance. The Init stop helper's void/u16 declaration matches its restored
definition; the other helper remains a separate unfinished implementation.

Fresh adopted-ELF recount: **3,916/5,506 (71.12%)** total,
**3,243/4,833 (67.10%)** Game, Init 492/492, Debugger 181/181, zero drift.
The conversion inventory CSV is unchanged. **214** more matches reach 4,130.
Tools commit first: `2ba33fccbbb24926966c3dcefd6143afe126caec`.

Scoped native AST refresh retains or uniquely relocates all 49,543 old nodes
and accounts for all 102,737 old directed relationships. The old target s32
return reference retires against its recovered void signature. Source/binding
validation records the two helper calls, registration and actual dispatch
window. Outside-scope manifests/communities remain historical; no full extraction.

Artifacts: `conker/build/game-actor-state-completion-match/`.
Next screened target `func_151C56A4` still needs qualification. Parked private candidates
remain uncredited. The older mirror preserves 1,955 inherited dirty paths plus
three new tools. No push, host-port, Release, save/editor or memory changes.
Zero Claude calls.
