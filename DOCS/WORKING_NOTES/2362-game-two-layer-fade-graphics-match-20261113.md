# Game two-layer fade graphics match

Date: 2026-11-13. `func_151ED09C` in `generated_215960.c` replaces its
zero-return placeholder with the recovered two-layer fade display-list
renderer. The 81-word body occupies VA `0x151ED09C..0x151ED1E0` and ROM
`0x21A54C..0x21A690`. Ten expected-word guards normalize register allocation
and an independent constant-materialization schedule; both supported padders
reproduce the complete retail instruction body and relocation bindings.

The routine emits an initial display-list command and a timer-derived white
environment color, calls the image-draw helper, writes a pipe sync, combine
mode, and a second environment color derived from the live fade byte, then
calls the helper again with a different image. It returns the display-list
pointer from `func_15096934`. The timer value is captured before the first
helper call, while the fade byte is read afterward; tests allow that helper
to change both globals and to return overlapping output buffers.

The target is entry 17 of `D_8008FFC0`. The bounded original indirect caller
window in `func_151E8620` passed 96 cases per stream with the mode set to 17;
the table entry is checked against the retail image. The test does not qualify
the complete parent or every source of the mode value.

The drawing helper `func_151ED430` remains a zero-return C placeholder, but
its declaration and placeholder definition now describe the observed eight
arguments and pointer return. Giving the placeholder named parameters causes
IDO to emit four argument-home stores. Four checked omissions remove those
stores so its padded body remains byte-identical to the previous placeholder;
they do **not** restore or match the helper itself. Its full implementation
and live rendering behavior remain unfinished.

Tools commit `69190d0` provides the focused checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_fade_graphic_151ed09c_match -v
```

An independent guest model passed 320 cases per stream across retail, raw C,
and both padded bodies, including timer boundaries, helper mutations and
buffer aliases. Retail and both padded bodies agree at 96 access-boundary
prefixes. Native 32-bit checks passed 160 cases at each of `-O0`, `-O2`, and
`-O3`, with UBSan and seven effective negative controls. Twelve GNU links
across three symbol layouts verified the guarded outputs and preserved helper
stub. The suite passed before and after installation in mounted tools and with
staged sibling dependencies; project tool checks passed. The image helper is
modeled in these checks, so they do not establish its complete behavior or
live gameplay output.

The actual production object and ELF equal the Make-planned audited shadow;
the other 1,453 linked input objects are unchanged. The strict full-image
prediction accounts for 276 changed bytes and one closed symbol-metadata
reordering with zero exclusions. Only this body differs among 6,051 functions;
all addresses and 189,088 protected Game-data bytes remain fixed. A separate
owner-section audit confirms the other 26 padded functions, data, ABI flags,
and register information are unchanged; text relocation and symbol tables
change for the newly referenced symbols.

The production recount reports Game **3,751 / 4,843 (77.45%)**, total
**4,424 / 5,516 (80.20%)**, zero address drift, and **124** further Game
matches required for 80%.
