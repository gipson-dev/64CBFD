# 1981 - Embedded integer oscillator pair recovered as guarded C

Verified 2026-11-01. Production now **4,048/5,507 (73.51%)**, Game
**3,375/4,834 (69.82%)**, Init492/492 and Debugger181/181. Zero address drift,
1,459 different; **83** more exact C functions are needed to reach4,131/5,507
and75%. This checkpoint adds two matches without changing the C inventory.

## Recovered functions and contract

| Function | Owner | VA span | ROM start | Words / frame / guards |
| --- | --- | --- | --- | --- |
| `func_150C5E0C` | `generated_F3270` | `150C5E0C..150C5EFC` | `F32BC` |60 /40 /6|
| `func_151AB090` | `generated_1D6E80` | `151AB090..151AB180` | `1D8540` |60 /40 /6|

Both zero-return placeholders are replaced by `s32(u8 *input)` callbacks.
The local `EmbeddedIntegerOscillator` view is32bytes at owner+B0; its
notification byte is+4, base/amplitude/target are+8/+C/+10, signed remaining,
minimum and range halfwords are+14/+16/+18, and gain is+1C. Owner+24 is a
signed32-bit rate. The ordinary domain requires an aligned owner of at least
D0bytes, live typed fields and a disjoint callee-private stack frame.

Capture the notification's boolean before clearing its full byte. Subtract
live `D_800BE9E4` modulo32bits, narrow through the remaining halfword, and test
the narrowed signed value. On expiry, call integer RNG, then read live signed
range+1 and minimum; reset with unsigned remainder plus minimum. Call floating
RNG, then load live amplitude/base and publish the renewed target. Finally
convert the live signed rate to binary32, subtract, multiply by live gain,
truncate toward zero and add modulo32bits. Return the captured notification.
Unsigned countdown and output addition avoid C signed-overflow undefined behavior.

## Source sequencing discovery

The initial nested expression compiled correctly under IDO but failed the
native provider-mutation test: GCC O0 could evaluate range before the integer
RNG call. In the counterexample, the provider changes range32767 to7 and
minimum32767 to-123; premature range evaluation produces17644 rather than-116.
The adopted source uses a separate `randomValue` assignment before the remainder
statement. Floating RNG likewise has its own full expression before amplitude
and base are read. Its result uses the target field as temporary storage;
IDO removes the intermediate store and emits retail's single target store.
The qualified domain excludes volatile/concurrent observers of those C fields.

The two additional scalar-local form grew the frame to48 and was rejected.
The selected sequenced source remains60words/frame40 with raw payload SHA256
`011ba6f3f9cb1f60d7823aa80c3fc75fb5f2cf2d68576ac95086f88df745957f`.
The original earlier unsequenced source and all failed screens remain private
build evidence, including the initially incorrect RNG scale assumption.

## Six guards per function

The complete raw payload and its four symbol bindings agree between owners.
Only two private spill lifetimes move within the existing40-byte frame:

| Instruction offset | Raw private slot | Retail private slot | Lifetime |
| --- | --- | --- | --- |
|44,54,90|SP+18 word|SP+1C word|oscillator pointer, one store and two reloads|
|50,5C,98|SP+23 byte|SP+27 byte|captured notification, one store and two reloads|

Both destinations are otherwise unused. SP never escapes; every source and
destination access was enumerated. No instructions, frame adjustments,
register bindings, missing operations or padding were inserted. Twelve
append-only expected-word CSV rows normalize those closed lifetimes. Three
independent GNU links per function qualify clocks with signed-low carry and
both RNG calls at independent addresses; originals were independently assembled.

## Fresh qualification

- Guest root corpus:1,738 cases across both roots and three layouts,
  10,428 cases /31,284 executions comparing original, normalized and raw C.
  All59 reachable words per root execute; the remaining word is retail break7.
  Full modeled memory, GPR/FPR, calls, access traces, HI/LO and PC/delay state
  agree after the private-slot mapping.186 access-prefix triples and12
  pre-DIVU zero-divisor triples pass. No hardware divide-zero HI/LO, FCSR or
  portable C fault claim; the branch/break structure remains intact.
- The private-slot projection tracks write provenance and subsequent caller
  reuse: original cleanup calls can overwrite the retired frame. A final
  unconditional slot swap was insufficient and was replaced by lifetime-aware
  projection. Clock aliases and incoming-home mutation cases are guest-only.
- Original RNG helpers:18 integer and25 floating instructions, unchanged in
  production; all43 executed across432 cases /1,296 executions. Independent
  64-bit seed recurrence and literal retail float scale `0x37800080` pass.
  This scale is approximately1/65535, not the initially assumed1/65536.
- Native32:818 cases per target at each O0/O2/O3, all untouched owner bytes
  and surrounding fences checked, typed field offsets asserted, UBSan enabled.
  Nine effective controls per profile reject lost/uncleared notification,
  wrong remaining gate, signed RNG remainder, wrong inclusive endpoint,
  premature range capture, wrong float order, wrong gain and signed-add overflow.
  Nonfinite/out-of-range float-to-int casts are outside the qualified domain;
  no generated root corpus case required exclusion.
- Actual caller is `func_1513C060`, not the separate195-word dispatcher
  `func_1513CFE4`. An aligned complete-ROM census finds no direct JALs and
  only literal pointers22E74C/22E750, slots7/8 of the14-entry table80089C70.
  The full188-word original parent is loaded; bounded no-fade/no-animation-wrap
  cases execute89 words.3,072 cases /9,216 executions cover active gating,
  timer expiry, notification return, scripted cleanup acceptance/rejection,
  and both original17-word cleanup routines, all34 instructions executed.
  Four old-target-stub return counterexamples are rejected. Release/detach
  lower providers are scripted. The parent remains a12-byte production stub;
  complete-parent parity and gameplay acceptance are not claimed.

## Owner, build and complete-image proof

All9 first-owner and40 second-owner neighbors match before/after, both raw
and padded. Constant pools are unchanged; no compiler diagnostics. Each actual
generated-owner Make pipeline executes five commands and reproduces its
independently qualified padded object. Retain `pad_generated_object` with
F3270.s and1D6E80.s; preserve their existing assembly-backed cleanup routines.

Independent prediction changes only the two240-byte retail slots and both
symbol extents12->240. The entire produced ELF equals that prediction:
`05b63fbbce7c8dc92744419c597d3a01bbbc3840a19eee4fa22d9fbc96779d93`.
All6,052 function addresses,6,050 other bodies, the entire named-definition
multiset, map and protected189,088 data bytes across720 owners remain fixed.
There are zero image exclusions and no metadata permutation adjustments.

Five focused public methods and shared tools checks pass in each tools copy.
After actual production Make, two installed compile/image methods per copy pass;
unchanged pinned semantic checks are explicitly reused, not called fresh.
The full17,759-file prior seal changes in exactly the two sources, their two
objects, guard CSV and ELF. No unplanned dependent object changes. Windows
adoption independently verifies sealed inputs before copying reviewed files,
then recounts the actual installed ELF through WSL. Both recounts report the
same4,048/5,507 and zero drift. Thirty-nine canonical preparation artifacts
are pinned; the focused input snapshot contains1,089 files.

## Next work and boundaries

Continue `func_150C673C` in generated_F3BA0.c, original asm/F3BA0.s: the fresh
production recount lists60words and57 real differences. It is still a stub;
no private candidate or matching credit has been assigned. Preserve all parked
private experiments, especially sound-start's unresolved epilogue. Current
75% goal stays active. No host-port or frozen Release changes are required:
these are guest callbacks and the host sibling has no implementation change
in this checkpoint. Tools are committed before the consumer pin; no push.
