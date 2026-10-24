# Recorded-Input Playback Match

Date: 2026-10-24. Consumer predecessor `10b101ca`; tools predecessor
`2266dcbc`. Qualification tools committed first as
`6113d8c04105ccc03eedf25be6d72bdbe782bfdc`. No push requested/performed.
Routine work, zero Claude calls; no provider/dependency or host changes.

## Recovered Routine

`func_151DD8C0`, `conker/src/game/generated_20A990.c`, replaces the
three-word zero-return placeholder with complete recorded-input playback.
VA `0x151DD8C0..0x151DD96C`, ROM `0x20AD70..0x20AE1C`, exclusive body
ends: 172 bytes / 43 words / frame zero / twelve bindings. Preserve the
separate zero alignment word through VA `0x151DD970`, ROM `0x20AE20`.
Use a local six-byte sample view: signed X/Y bytes, tick halfword at +2,
button halfword at +4. Retain the original function/global names.

1. Capture the signed cursor and table pointer, then locate the current
   six-byte sample. Do not add an entry bounds or NULL-pointer gate.
2. Load X, capture the existing controller button halfword, store X, load
   and store Y, then capture the recorded button halfword. Only after that
   clear the gap byte and publish recorded buttons OR held Start (0x1000).
3. For signed cursor below 499 only, read the next sample's ticks and the
   previous signed tick word. If previous is strictly lower, store the low
   byte of their wrapping difference. Otherwise keep the cleared gap.
4. Read the current sample's ticks after the controller/gap stores and
   publish them. Increment the captured cursor with 32-bit wrapping,
   publish it, and clamp a signed result at or above 499 to 499.

Explicit unsigned subtraction/increment avoid signed integer overflow
without changing the emitted instructions. Native checks use fully allocated
array positions, including a valid negative index relative to an interior
base. Extreme guest cursor tests use mapped wrapping machine addresses;
they do not claim portable C out-of-array pointer semantics.

The actual caller passes no arguments and ignores V0. Keep the recovered
C interface void(void); raw volatile GPRs and fault-PC locations are not
equated with retail. Fitted/original complete private states do agree.

## Derived Normalization

Bounded screens cover the initial four forms, 96 declaration/cap/clock
forms, 16 shared-value/view forms and four return-value forms. The initial
draft cleared the gap before reading buttons; reject that alias-sensitive
shape. The selected source captures buttons first and emits 43 words at
normal O2/g3. No direct fit was found; this is guarded semantic C.

Validate the complete raw hash and all twelve symbolic bindings, then
derive forty expected-word rows with simultaneous register-field renaming:

| Role | Raw | Retail |
| --- | --- | --- |
| Captured index / record address | V0 / V1 | V1 / A0 |
| Held buttons and later next tick | A0 | V0 |
| Controller / gap addresses | A3 / T0 | A1 / A3 |
| Early table base / scaled offset | T7 / T6 | T8 / T9 |
| X / Y byte values | T8 / T9 | T0 / T1 |
| Recorded buttons / held Start mask | A1 / T1 | T2 / T7 |
| Combined buttons / gap difference | T2 / T3 | T3 / T4 |
| Final current tick | T4 | V0 |

The early A1 button lifetime ends before the unchanged late A1 clock-address
role. Early T7 table-base lifetime ends before the unchanged clamp-constant
role. Cursor-address A2 and next-index T5 stay fixed. No FPR/frame/save changes.

Swap independent initial address-setup words zero/one and four/five, carrying
their relocation records. Exchange only the operands of unsigned address
ADDU at word twelve. Move the independent 499 initializer from raw word19
to fitted word39, after the old mask value is dead. Derive the final branch
displacement from the permutation: old branch38/target41 becomes branch37/
target41, displacement three. Every memory access and its order is retained.
No inserted/omitted words, new profile, barriers, inline assembly or wholesale
assembly-body replacement. Guard rows carry exact old/new relocation specs;
append only, preserving every historical CSV byte.

Raw payload SHA-256:
`d8dcafa10c22e6b8d883039a1fa199ac38ac56a5d63f40c2d445379253114072`.
Resolved retail body SHA-256:
`0251b63941e9626382b95ebf45b6b0d0f3ceeadf00c7c7427e74733794fa0553`.
Full 44-word slot SHA-256:
`ef52073270f9e8922b45411803ec5ba3ff84ab79bafbd65bedab516f2d881f2e`.

## Caller And Qualification

An aligned full-ROM scan finds no literal target pointer and exactly one
JAL site at ROM `0x493B4` in `func_1501BBB8`. Execute its actual 15-word
mode/call window, VA `0x1501BEE0..0x1501BF1C`, ROM `0x49390..0x493CC`.
Either mode byte equal to two activates playback; preserve the saved T1
flag and post-call T2 step value seven. T2=7 on window entry is established
by the unchanged preceding parent loop. The larger parent remains a C
placeholder and uncredited; no native/full-parent/gameplay claim.

Both copies pass eight fresh checks before and after installation, with no
errors/failures/skips/reused checks. Pre-install primary/mirror:
8.356s / 8.290s; installed: 9.353s / 9.246s. Both shared tool checks exit zero.

- 2,720 original/raw/fitted/actual-Make guest phases cover all stick-byte
  values, twenty button masks, signed tick/cursor boundaries, wrapping
  extremes and eight sample/global alias layouts. All 43 words are visited.
- Execute the original mode/call window in 4,080 phases over every mode
  byte, both stack phases and ordinary/terminal cursors.
- Native32 O0/O2/O3 trap UBSan passes 1,728 complete allocated-storage cases
  per optimization and eleven effective defined wrong-C controls. Two
  separately compiled wrong capture-order bodies have actual guest
  counterexamples at gap/button and controller/current-tick overlaps.
- 156 fired root-access prefixes compare complete fitted/original private
  state and raw memory/events/saved state. Suppress next-record reads at
  terminal cursors; these are instruction-access, not portable C fault claims.
- 57 raw-word/binding/length corruptions, two real padder corruptions and
  historical-prefix corruption fail closed. Twelve GNU links compare
  original/raw/fitted/actual-Make objects at three symbol placements;
  72 rebased phases cover aliases and HI/LO carry boundaries.
- Twelve full-image corruption controls cover code, ELF edges and all nine
  rotated metadata definitions. All named definitions are independently
  preserved except the target function size.

## Strict Production Image

Actual ordinary three-command compiler/padder/assembler Make uses O2/g3
and preserves all three SDK neighbors, raw/padded pools and the complete
qualified object. Isolated diagnostics are empty; owner diagnostics stay
unchanged. Inherited duplicate generated_12D630 recipe warnings remain.

Independent and production links agree on exactly 192 changed bytes:
136 target code plus 56 metadata, with zero exclusions. Metadata is the
function size 12 to 172 and two explicitly predicted symbol/string cycles:

- Five names rotate left: D_800E0A70, D_8009A0A8, D_80099260,
  D_800A3560, D_800A3108.
- Four names rotate left: D_800E0A74, D_800E0A31, D_80099264, D_800A3564.

Check each predecessor definition, absolute value/type/size/section, 16-byte
symbol stride and 11-byte terminated string stride before constructing
those cycles. A named-definition multiset check permits only the target
size change, not new/deleted/retargeted symbols. No executable or data
exclusions and no unrelated image changes.

Production Make exits zero in 0.516s. Preserve all other 6,054 bodies/all
6,055 addresses and protected Game data: 720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Seal 15,986 files / 29 focused inputs / all 1,454 linker objects, advancing
the preceding checkpoint's four qualified overrides and adding two tools
modules in both copies. Preserve all 1,620 prior mirror dirty statuses/
hashes/HEAD; add only those two modules, now 1,622. Do not commit/reset
that older mirror. Use checked native stdin/tar bridges and the verified
Linux cache, no DrvFS project reads.

Audit live adoption with exactly four overrides: target source, guard CSV,
target object and linked ELF. Re-capture and freshly recount the actual
adopted native ELF, SHA-256:
`50db0c294d2f09be988d34eb44260fcb295c3a155c97e5e4b65ef56446505a76`.

| Section | Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,781 / 5,505 (68.68%) | 0 | 1,724 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,108 / 4,832 (64.32%) | 0 | 1,724 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% threshold remains 4,129 exact functions: 348 more needed. The live
queue has 1,595 placeholders, 120 semantic/other definitions and nine
parser-unlocated entries. `func_1510D8C0` already has Gfx* C and remains
separate. Next real placeholder `func_150B1EE0`, owner `generated_DF260`,
44 words, is not yet qualified. Existing `func_15014094` is another
semantic-C matching case. Private screens and the separate larger
`func_1509E730`, `func_1508CAD8`, `func_15169070` work stay uncredited.
README changes only its two aggregate rows; host Release, saves,
configuration and unrelated sibling work remain untouched.
