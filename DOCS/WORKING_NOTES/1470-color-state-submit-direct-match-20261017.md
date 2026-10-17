# Color State Submit Direct Match

Date: 2026-10-17. Completes the real color helper handoff from
[Note 1469](1469-sequence-event-scan-installed-guarded-match-20261017.md).

## Direct C Recovery

`func_1517EE40` in `conker/src/game/generated_1AC2F0.c` now contains its
complete semantic C body rather than a zero-return stub. All **48 words /
192 bytes** emit **directly** from the existing normal O2/g3 profile and
match retail. Frame **0x8**, VA **0x1517EE40..0x1517EF00**, ROM
**0x1AC2F0..0x1AC3B0**. No new guard, insertion, omission, compiler profile,
private constant pool or source diagnostic is needed.

The recovered interface is
`void(s32 red, s32 green, s32 blue, s32 duration, s8 mode, s32 channel)`.
Retail reads the fifth argument as a signed byte at incoming stack + 0x13;
red is homed as a full word and RGB stores truncate to bytes. The routine
publishes when the signed mode differs, the signed counter is below its
limit, or the busy byte is nonzero. Otherwise it leaves all public state
unchanged. Publication writes green/blue/red, duration, zero counter, mode,
then clears busy in the original order.

Both C caller declarations now use the precise signed-byte mode:
`generated_49D30.c` and `generated_1A0100.c`. Their instruction bytes and
relative bindings are unchanged. Preserve **27 raw/padded helper-owner
neighbors**, all **57 raw/padded scan-owner functions**, and all **five
raw/padded teardown-owner functions**: **89 unchanged routines** in total.
The complete guard manifest is byte-identical, including its 298 CRLF lines.

Raw text SHA-256:
**3fc4ac5a61a8d3a7bd976be0860b1847317b50340157c306f3e69e302b0c41d7**.
The independent original object has identical words and all **16 relative
HI16/LO16 bindings**. The actual normal padder also preserves every word.

## Qualification

All **17 final tests pass in 216.960s**: eight focused recovery tests,
three installation tests, and six previous scan/setup installed tests.

- **3,712 paired original/C guest cases**, including both stack phases,
  signed modes, arbitrary argument padding, signed time boundaries and six
  controlled global alias maps. Reach every word and compare literal full
  memory, GPR/FPR/LO, events, PC/delay and access state.
- Three independent original and C links each match all 48 words across
  symbol HI16/LO16 carry boundaries. Alias fixtures also independently link
  original and C code with the same explicitly selected bindings.
- **59 positively fired original/C access-fault prefixes** compare literal
  machine state. This qualifies emitted instruction order, not portable C
  exceptions or hardware CP0 behavior.
- Execute the complete **32-word func_15172CA8** teardown caller and actual
  C helper in **40 paired cases**, including the signed -1 gate and both
  mode/duration submissions. Every caller word executes.
- Execute the complete **219-word sequence scan** with the actual C helper
  in **24 paired cases**, comparing an independent composed state/call
  reference. The query engine remains a bounded provider, not restored here.
- **280 native32 cases per O2/O0 profile with UBSan**, compiling the full
  leaf and actual teardown caller in separate units. Check the entire state
  bank, slot payload, padding and canaries. No fwrapv or LTO.
- Eight effective native controls all compile and exit **22**, not signals
  or sanitizer traps: unsigned mode/state, inclusive/unsigned time comparison,
  skipped busy gate, wrong RGB stride/red, and wrong alias-sensitive order.
  The unsigned-mode control keeps its caller/callee prototypes compatible.
- Native alias cases use same-width views; cross-endian byte/word aliases
  and arbitrary fifth-argument padding are explicitly guest-only. Fixture
  channels 0..3 do not establish arbitrary retail indices as valid.
- Every raw word, binding and unexpected binding is rejected by the exact
  object gate. All **144 protected production inputs** reject unknown changes.

Note 1469's broader unchanged setup/query/scan receipts remain prior evidence,
not newly run suites. All of their caller bodies, helper instruction words,
data and guards remain unchanged; the focused tests above additionally
exercise the newly compiled helper in both real C caller paths. Full color
rendering, sequence-engine and gameplay acceptance remain separate.

## Complete Installation

Before production edits, reproduce the predecessor image from captured
normal link inputs, then independently predict every first image/owner/
caller byte. The only canonical definition change is this function's size
**12 -> 192**. Two exact symbol-order groups pin names, order, definitions
and string extents. There are **zero metadata exclusions**.

The normal development build recompiles and pads only the **three affected
owners**, links and regenerates progress. Its complete ELF equals the first
prediction byte for byte:
**ae0e0b359077e8a6a85a465b173b4d8bf4de55f395e51e77a02464ef9602f014**.
Of **215 changed ELF bytes**, **165** are the target code, **one** its
extent, and **49** exact symbol/string serialization. Existing duplicate
Makefile recipe warnings remain; this is not a warning-free build claim.

Installed helper owner:
**b8f159e15a63d7dcd69eb9fd972a98cab9055ed69fceff0ad103e955628498e2**.
The two caller owners and all four before/after fixture pairs are pinned
in `color_state_submit_checkpoint.py`. Protect **144 inputs / 140 unchanged
inputs**, the entire unchanged guard manifest, and **189,088 Game-data bytes /
720 owners / zero differences**. Previous scan/setup exact-successor tests
pass through the new adapter; unknown successors remain rejected.

## Progress And Bank

Fresh official matching: Game **2,942/4,828 (60.94%)**, total **3,615/5,501
(65.72%)**, still different **1,886**, zero address drift. Init remains
**492/492**, Debugger **181/181**. Conversion stays **5,501/6,044 functions /
86.04% bytes**; the former stub already counted as C. Conversion CSV bytes
are unchanged. Root README changes only its two aggregate matching rows.

Tools **aecf777** banks nine files before the consumer pin. Both copies have
identical pairs and **18 ASCII/AST checks**. Eleven WSL standalone padder
tests pass per copy: active **0.033s + 0.024s**, mirror **0.033s + 0.019s**;
tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **978 unrelated initial
dirty-file hashes** and its independent history. Two existing task files
are updated, seven added: **987 final dirty paths**. No mirror commit/reset,
push, Claude call, dependency/configuration change, host-port build/launch
or frozen Release action.

Prepared-checkout reproduction, sequentially:

```sh
python3 -m tools.experiments.game_color_state_submit_installation
make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1
python3 -m unittest tools.tests.test_game_color_state_submit \
  tools.tests.test_game_color_state_submit_installed \
  tools.tests.test_game_sequence_event_scan_installed \
  tools.tests.test_game_sequence_record_setup_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover the complete direct C leaf, signed mode interface and exact store/short-circuit behavior.
- [x] Preserve all 48 words/16 bindings, 89 surrounding routines and every guard byte without new profiles or normalization.
- [x] Qualify guest/native state, actual teardown/scan callers, aliases, effective controls, rebases and fault prefixes.
- [x] Freeze the first whole-image/source/caller prediction before edits, then build and pass all 17 tests and exact data/input gates.
- [x] Measure fresh progress, update README aggregate rows/indexes/roadmap and bank tools first.

Next: **func_1517EF00**, the adjacent color-progress accessor still represented
by a zero-return stub in the same owner: **43 words / 172 bytes**, no stack
frame, VA **0x1517EF00..0x1517EFAC**, ROM **0x1AC3B0..0x1AC45C**. Recover its
busy-byte fast path, signed scaled division, upper clamp and mode-dependent
inversion, including division/overflow boundaries rather than only nominal
timing. Keep the query engine, adjacent sequence work, timing's **141
differences**, wider Game/additional-source matching and full gameplay open.

Subsequent completion: [Note 1471](1471-color-progress-accessor-direct-match-20261017.md)
restores func_1517EF00 as a complete 43-word direct C match, with signed
arithmetic/trap qualification, actual caller chains and a code/size-only
whole-image audit. The next handoff advances to func_1517EFDC.
