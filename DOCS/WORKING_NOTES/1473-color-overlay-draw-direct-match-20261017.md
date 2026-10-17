# Color Overlay Draw Direct Match

Date: 2026-10-17. Consumer baseline **8eb2b57a**, tools baseline **83a87d2**.
Follow-through from [Note 1472](1472-color-channel-aggregate-direct-match-20261017.md).
Codex owns source, qualification and integration; **zero Claude calls**.

## Complete Recovery

**func_1517F08C**, in `conker/src/game/generated_1AC2F0.c`, is now a complete
direct SDK C match: **197 words / 788 bytes**, no frame, VA
**0x1517F08C..0x1517F3A0**, ROM **0x1AC53C..0x1AC850**. Preserve the existing
normal O2/g3 owner profile and original `conker/asm/1AC2F0.s`. There are
**zero new guards, profiles, private pools or compiler diagnostics**.

The real six-argument interface is `Gfx *func_1517F08C(Gfx *commands,
s32 alpha, s32 red, s32 green, s32 blue, s32 channel)`. Append pipe sync,
primitive-color combine, packed RGBA primitive color, other mode and the
viewport rectangle, returning the cursor **40 bytes** later. Emit all five
commands even when alpha is zero. The other mode uses the SDK translucent
blender with **coverage-save**, not its default coverage-full bits.

The viewport pointer is live `D_800BE628`, with **0x180-byte** rows and float
top/bottom/left/right at **+0x24/+0x28/+0x2C/+0x30**. All four coordinates
cast to **unsigned 32-bit** before rectangle packing. Retain each complete
IDO FCSR save/truncate/invalid/retry/restore expansion and the pointer reload
after publishing the first rectangle word. Do not cache the bounds early.

Raw text SHA-256:
**58cd710b808bd4c64bdc566eb77e92c8acef58cd8cf6dabf1179490a9e43bb62**.
The independently assembled original has identical words and exactly two
bindings: **+132 HI16 / +136 LO16 D_800BE628**. The normal padder retains
every word. Natural paths execute **193 words**; duplicate unreachable MFC1
words at **+0x12C/+0x1C0/+0x25C/+0x2E8** remain in the complete object gate.

Source screens distinguished cursor typing from semantic mode bits. A word
formal with a local Gfx pointer produces **187 words / 193 differences**.
A typed Gfx formal restores **197 words / one difference** with either
return type. Correct coverage-save bits then produce **197 / zero**. No
schedule patch or compiler-profile change is needed.

## Caller Interfaces

Local wrappers keep their existing word-cursor API, explicitly casting to
and from the typed leaf: **func_1517F3A0 (27 words)**, **func_1517F4D8 (35)**
and **func_15182768 (25 plus its existing trailing NOP)**. External owners
`generated_131620.c` and `generated_FF5C0.c` now declare the same six typed
parameters and cast their legacy cursors explicitly. Their callers are
**func_1510448C (26 words)** and **func_150D22F4 (32 words)**.

All five caller bodies are literally retail-exact and unchanged. The full
raw/padded owner comparisons preserve **27 + 4 + 7 = 38 other routines**.
The whole-image gate also protects the record wrapper's existing tail NOP.
No shared header or unrelated function is changed.

## Qualification

All **26 post-installation tests pass in 321.565s**: eight target tests,
three installation tests and fifteen prior aggregate/progress/color/scan/
setup installation tests. All eight pre-installation target tests passed
in **100.714s**. Fresh receipts are in the ignored target build directories.

- **2,328 paired original/C leaf guest cases** cover four initial control
  seeds, full-word sparse channels, unsigned fallback and negative-fraction
  conversions, field aliases, pointer redirections, incoming stack-home
  overwrites and cursor wrap. Compare full private memory, modeled registers,
  control, PC/delay, accesses, conversions, events, returned cursor and all
  packet bytes against an independent literal-command reference.
- **720 paired complete caller cases** execute all five real caller bodies,
  the actual 197-word leaf and the actual **43-word func_1517EF00** where
  appropriate. Explicitly enforce fired/skipped entries; no opaque helper
  substitutes. All caller words execute, including **24 zero-alpha emission
  pairs**. Check complete packets, state and returned cursor.
- **552 native32 cases per O2/O0 profile with UBSan** compile the actual SDK
  leaf, all five callers and progress body as separate units, without LTO or
  fwrapv. Check full output/view/color/packet state, padding and canaries.
  All eight effective controls compile and exit **22**, not sanitizer traps:
  zero-alpha suppression, wrong coverage, swapped colors/bounds, wrong
  channel/return, cached bounds and missing sync.
- Three independent original/C rebase pairs match every word across HI16/
  LO16 carry boundaries. **90 positively fired data-access fault prefixes**
  compare literal private and temporary control state through partial packet
  publication. These qualify emitted order, not portable C faults or CP0.
- All **197 word controls**, both bindings plus an unexpected binding, and
  **152 input corruption gates** reject unknown changes. Removing the final
  CTC1 at **+0x300 (0x44CDF800)** is an effective negative: a nondefault initial
  control seed detects leaked control state.

The guest FP oracle reuses the existing bounded invalid-flag conversion
model. It is **not** full hardware FCSR/inexact/exception-enable, denormal,
NaN-payload, MMIO or CP0 qualification. Native cases use finite defined
unsigned casts, valid channels and aligned output. Pointer-cell redirections,
private incoming-home overwrites, invalid/nonfinite casts and fill-word-to-FP
aliases are guest-only probes, not portable native C claims. Full renderer,
pixel and gameplay acceptance remain separate. Broader unchanged semantic
suites remain prior receipts; their fifteen installation checks are fresh.

## First Complete Image

Capture the normal link script and all three normal owner objects before
production edits. Reproduce the predecessor byte-for-byte, then independently
link the three qualified padded objects. Freeze that **first** complete
image/source prediction before installation. The existing six-argument stub
has a measured **28-byte** symbol, not the generic 12-byte stub assumption;
the prediction validates exactly **28 -> 788** before any production edit.

The normal build recompiles/pads only these three owners, links successfully
and regenerates progress. The entire **3,257,636-byte ELF** equals the first
prediction. Exactly **539 bytes** change: **537** target instruction bytes
and **two** symbol-size bytes. No symbol/string reordering, metadata exclusions
or unrelated image differences. All canonical named definitions are unchanged
except the target size. Every previous guard byte and conversion CSV byte
is identical. Existing duplicate Makefile recipe warnings remain; this is
not a warning-free build or a fresh whole-ROM checksum claim.

Installed SHA-256 values:

```text
ELF                  cab895122f114cbfe41572410c714d016d6b75244bd3434fb6d26c453d60c1c1
generated_1AC2F0.c    4cef4ff1b1cb1f393a391225a9d6dbebfafee3d2f73873c831ef273d455b43de
generated_131620.c   ed0fdab2c81a5f3c17dca256cf55a0c46056526122375a9042651808dcd094bf
generated_FF5C0.c    4a614a105b01975d0dbfe6ef6752e1763ffe79ac6a872d24b1fa53c286a0a7aa
guard manifest       5084330509403cb54c534e06be40b8417b97e95addf3dd362f843e4235b58b35
```

Protect **152 inputs / 148 unchanged**, all four before/after fixture pairs,
and **189,088 Game-data bytes / 720 owners / zero differences**. The prior
aggregate checkpoint recognizes only this exact pinned successor before its
original inverse; unknown image/source/fixture/metadata changes still fail.

## Progress And Bank

Fresh official matching: Game **2,945/4,828 (61.00%)**, total **3,618/5,501
(65.77%)**, still different **1,883**, zero address drift. Init remains
**492/492**, Debugger **181/181**. Conversion stays **5,501/6,044 functions /
86.04% bytes**; the previous stub already counted as C. Root README changes
only its two aggregate matching rows.

Tools **33dda28** banks nine files before the consumer pin. Both local copies
have nine identical task pairs and **18 ASCII/AST checks**. Eleven standalone
padder tests pass per copy: active **0.036s + 0.021s**, mirror **0.029s + 0.031s**;
tools-check passes. The two existing mirror task files match the committed
tools baseline and their captured live hashes before copying. Preserve mirror
HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a** and all **999 unrelated initial
dirty-file hashes**. Two existing task files update and seven are added:
**1,008 final dirty paths**. No mirror commit/reset, push, Claude call,
dependency/configuration change, host-port build/launch or frozen Release action.

Prepared-checkout reproduction, sequentially:

```sh
python3 -m tools.experiments.game_color_overlay_draw_installation
make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1
python3 -m unittest tools.tests.test_game_color_overlay_draw \
  tools.tests.test_game_color_overlay_draw_installed \
  tools.tests.test_game_color_channel_aggregate_installed \
  tools.tests.test_game_color_progress_installed \
  tools.tests.test_game_color_state_submit_installed \
  tools.tests.test_game_sequence_event_scan_installed \
  tools.tests.test_game_sequence_record_setup_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover the full SDK overlay and typed pointer interface directly from C.
- [x] Preserve all 197 words/two bindings, five callers, 38 surrounding routines and every guard byte.
- [x] Qualify actual caller/progress chains, unsigned/alias/control cases, native controls, rebases and faults.
- [x] Freeze the first whole image/source before edits, build and pass all target and predecessor installation tests.
- [x] Measure fresh progress, update aggregate rows/indexes/roadmap and bank tools first.

## Next Target

**func_1517F564**, in the same owner: **111 words / 444 bytes**, frame
**0x30**, VA **0x1517F564..0x1517F720**, ROM **0x1ACA14..0x1ACBD0**. Recover
its complete global pulse/palette wrapper, both gates, six-byte palette-pair
interpolation, pulse helper and channel-zero call to the restored renderer.

Resolve the **SP+0x20 blend lifetime first**. Retail at **0x1517F5B4** reads
that private float before the pulse branch; the complete routine has no
observed preceding store. Pulse-on later sets the blend register to zero,
whereas pulse-off retains the loaded value. This is an unresolved retail
lifetime/uninitialized-local boundary, not permission to invent a zero blend
or claim native definedness. Inspect full caller/private-stack provenance
and the pulse helper before choosing source. Preserve the retained conversion
branches and signed/FP/control boundaries. Wider Game/additional-source
matching, the query engine, timing's 141 differences and full gameplay stay open.

Follow-through: [Note 1474](1474-pulsed-overlay-private-lifetime-audit-20261017.md)
proves the inherited pulse-off dependence through real retail helper/caller
chains and rejects zero/undefined-local adoption. The same wrapper remains
open; this audit changes no production bytes or matching totals.
