# Color Progress Accessor Direct Match

Date: 2026-10-17. Completes the accessor handoff from
[Note 1470](1470-color-state-submit-direct-match-20261017.md).

## Direct C Recovery

`func_1517EF00` in `conker/src/game/generated_1AC2F0.c` now contains its
complete semantic C body rather than a zero-return stub. All **43 words /
172 bytes** emit **directly** from the existing normal O2/g3 profile and
match retail. No stack frame, VA **0x1517EF00..0x1517EFAC**, ROM
**0x1AC3B0..0x1AC45C**. No new guard, insertion, omission, compiler profile,
private constant pool or source diagnostic is needed.

The precise interface is `s32 func_1517EF00(s32 channel)`. A nonzero busy
byte returns directly without reading duration, ticks or mode. Otherwise,
a zero duration selects 255; a nonzero duration divides the signed low
32-bit product of ticks and 255 by signed duration, truncating toward zero.
Clamp only values above 255. Finally, zero mode inverts progress as
`255 - progress`, retaining its low 32 bits. Negative values and values
above 255 after inversion must not be narrowed or lower-clamped.

Unsigned multiplication/inversion preserve the retail wraparound result
without signed-overflow assumptions. Keep the signed DIV and its emitted
overflow BREAK; `INT_MIN / -1` is deliberately not a portable native C case.
The selected split busy/idle form matches directly. The initial nested form
has 41 words / 41 differences; a ternary screen has 44 words / 26 differences.
A signed-inversion screen has identical instructions but is not selected.

Raw text SHA-256:
**d66d0a02b48bea527d8547d34a8c33c9216e7e148eca9c55558313f49075b608**.
The independently assembled original has identical words and all **eight
relative HI16/LO16 bindings**. The actual normal padder also preserves every
word. All **27 raw/padded owner neighbors**, including the existing color
submitter and both local callers, remain unchanged. Existing caller
declarations already have the correct signed return/argument interface.

## Qualification

All **20 post-installation tests pass in 262.871s**: eight target tests,
three installation tests, and nine prior color/scan/setup installed tests.
After adding explicit helper-entry assertions, both composed caller tests
pass again in **3.385s**. The eight pre-installation tests passed in 95.170s.

- **12,840 paired original/C guest cases**, both stack phases, signed
  durations/ticks, wrapping products/inversion, busy short-circuiting, five
  global alias maps and sparse wrapped indices. Compare literal full memory,
  modeled GPR/FPR/HI/LO, calls, events, PC/delay and data-access state.
- **100 paired emitted overflow-trap cases** reach BREAK 6. Natural paths
  execute **42 words**. BREAK 7 is unreachable behind the stable zero-duration
  gate, but remains part of the complete 43-word exact-object/corruption gate.
  The scoped DIV/BREAK oracle is not hardware HI/LO, CP0 or portable C
  exception acceptance. Initial test diagnostics corrected the compiler's
  legacy BREAK immediate decoding, not the already exact production candidate.
- Three independent original and C links each match all 43 words across
  symbol HI16/LO16 carry boundaries. Aliased globals also use independently
  linked original and C objects with the same selected bindings.
- **11 positively fired original/C data-access fault prefixes** compare
  literal state, including prefixes ending before the overflow trap.
  This qualifies emitted access order, not portable C memory exceptions.
- Complete **12-word func_1517EFAC** predicate and **27-word func_1517F3A0**
  renderer wrapper execute with the actual helper in **528 paired cases**.
  Every local caller word executes, helper entry fires in every case, and
  signed results/RGB packets are checked. The renderer remains a bounded
  provider, not a rendering recovery.
- Complete **111-word func_151D8868** record-registration caller executes
  with the actual helper in **48 paired cases**, against an independent
  composed state/call reference. Helper entry explicitly fires. Other
  registration providers remain bounded; this is not full engine acceptance.
- **756 native32 cases per O2/O0 profile with UBSan**, each invoking the
  full leaf, predicate and renderer wrapper: **2,268 target invocations per
  profile**. Leaf and callers compile in separate units without LTO/fwrapv.
  Check the entire byte bank, canaries, return values and render packets.
- Eight effective native controls all compile and exit **22**, not signals
  or sanitizer traps: ignored/boolean busy, unsigned division, wrong scale,
  missing upper/invented lower clamp, reversed mode and narrowed return.
- Native overflow division is excluded and separately guest-trap tested.
  Native alias views are same-width; cross-width aliases and sparse indices
  are guest-only. Native fixture channels 0..3 do not establish arbitrary
  retail indices as valid.
- All **43 raw words**, eight bindings plus an unexpected binding, and all
  **146 protected production inputs** reject unknown changes.

Broader unchanged predecessor semantic suites remain prior evidence, not
freshly run suites. Their bodies/data/guards are unchanged; their nine
installed-image tests are freshly run through the exact-successor adapter.
Full rendering, sequence-engine and gameplay acceptance remain separate.

## Complete Installation

Before production edits, reproduce the predecessor ELF from captured normal
link inputs, then independently freeze the first complete image/source
prediction. The normal build recompiles/pads only the affected owner and
regenerates progress. Its entire ELF equals that first prediction:
**a60f00d845f899cba20f347ad139c9d7232460d28f0e7ca8a730e2a5d16efe07**.

Of **125 changed ELF bytes**, **124** are target code and **one** is the
function-size update **12 -> 172**. Every other ELF byte is identical:
no symbol/string reordering and **zero metadata exclusions**. All canonical
definitions are unchanged except this size. The complete guard manifest is
byte-identical. Existing duplicate Makefile recipe warnings remain; this is
not a warning-free build claim or a fresh whole-ROM checksum qualification.

Installed source owner:
**334e3ca5a98e9483199d71812028c0b26fdcb4e36c014c724a499957b88ed799**.
Protect **146 inputs / 144 unchanged inputs**, both before/after fixture
pairs, and **189,088 Game-data bytes / 720 owners / zero differences**.
The prior color checkpoint now recognizes only this pinned successor before
its existing inverse; unknown images, sources and fixtures remain rejected.

## Progress And Bank

Fresh official matching: Game **2,943/4,828 (60.96%)**, total **3,616/5,501
(65.73%)**, still different **1,885**, zero address drift. Init remains
**492/492**, Debugger **181/181**. Conversion stays **5,501/6,044 functions /
86.04% bytes**; the former stub already counted as C. Conversion CSV bytes
are unchanged. Root README changes only its two aggregate matching rows.

Tools **5298c5e** banks nine files before the consumer pin. Both local copies
have identical pairs and **18 final ASCII/AST checks**. Eleven standalone
padder tests pass per copy: active **0.033s + 0.022s**, mirror
**0.031s + 0.036s**; tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a** and all **985 unrelated initial
dirty-file hashes**. Two existing task files are updated, seven added:
**994 final dirty paths**. No mirror commit/reset, push, Claude call,
dependency/configuration change, host-port build/launch or frozen Release action.

Prepared-checkout reproduction, sequentially:

```sh
python3 -m tools.experiments.game_color_progress_installation
make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1
python3 -m unittest tools.tests.test_game_color_progress \
  tools.tests.test_game_color_progress_installed \
  tools.tests.test_game_color_state_submit_installed \
  tools.tests.test_game_sequence_event_scan_installed \
  tools.tests.test_game_sequence_record_setup_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover the complete signed C accessor with exact busy/division/clamp/inversion behavior.
- [x] Preserve all 43 words/eight bindings, 27 raw/padded neighbors and every guard byte without new profiles.
- [x] Qualify guest/native arithmetic, emitted traps, actual caller chains, aliases, controls, rebases and faults.
- [x] Freeze the first whole-image/source prediction, install, build and pass target plus predecessor installed tests.
- [x] Measure fresh progress, update aggregate rows/indexes/roadmap and bank tools first.

Next: **func_1517EFDC**, the adjacent channel-state aggregate still represented
by a zero-return stub: **44 words / 176 bytes**, frame **0x30**, VA
**0x1517EFDC..0x1517F08C**, ROM **0x1AC48C..0x1AC53C**. Recover its inclusive
live channel-limit loop, signed positive-progress test, positive float-state
fallback, -1-based tally and final limit equality. Preserve saved-register/F20
lifetime and qualify real calls to the newly restored accessor, including
negative progress and floating-point boundaries. Wider Game/additional-source
matching, the query engine, timing's 141 differences and full gameplay stay open.

Subsequent completion: [Note 1472](1472-color-channel-aggregate-direct-match-20261017.md)
restores func_1517EFDC as a complete 44-word direct C match with its original
frame/F20 lifetime, actual progress/sequence chains and code/size-only whole
image audit. The next handoff advances to func_1517F08C.
