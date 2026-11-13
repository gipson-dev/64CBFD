# Game view-scaling configuration match

Date: 2026-11-13. `func_1500E738` replaces the placeholder in
`conker/src/game_3BA70.c`. Its 86-word retail body spans VA
`0x1500E738..0x1500E890`, ROM `0x3BBE8..0x3BD40`.

The routine sets two independent selector/factor pairs from the active view
configuration. The first recognizes modes 0, 1 and 2/3, leaving its existing
values untouched for other modes. The signed-byte second mode selects factors
from 1 through 1/16, with the default returning to selector 0 and factor 1.
The sole aligned direct retail caller, `func_15007B3C`, ignores the result;
the recovered interface is `void`.

IDO emits every retail instruction directly. The compiler also emits a
temporary 16-entry jump table, while retail already has the equivalent table
at `jtbl_800961D0_game`. All 16 compiler table relocations resolve to the same
case addresses as that existing table. Two checked HI16/LO16 relocation guards
bind the emitted body to the retail table; no instruction words are changed,
inserted or omitted. The compact compiler object contains the temporary table,
but the padded production owner does not emit it. The existing special
no-unroll profile for `func_1500E5C0`, all five other owner functions, and the
Makefile remain unchanged.

Tools commit `985f87a` supplies the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_view_scale_1500e738_match -v
```

The suite compares 2,048 input pairs per retail and raw guest body and reaches
all 86 words. Native 32-bit O0/O2/O3 each pass 2,048 cases with trapping UBSan
and five effective semantic controls. The original caller is exercised through
the target and the next helper boundary in 420 cases per retail/padded body;
this is a bounded caller prefix, not execution of the entire initialization
routine. Another 37 retail/padded guest fault prefixes include six delay-slot
cuts. Four stale guard preimages reject, and eight GNU links cover four symbol
layouts. These checks do not establish live gameplay behavior.

All nine checks pass in the mounted tools checkout and an isolated sibling
overlay. The overlay uses mounted fallbacks and is a hybrid check. The
sibling's 2,434 pre-existing dirty paths remain unchanged, and shared project
tool checks pass.

The production build and independent full-image audit pass with 367 changed
bytes and zero exclusions. Four explicitly predicted symbol-metadata reorder
groups account for the non-code metadata changes. Only this function changes
among 6,051 linked bodies, every address remains fixed, and all 189,088
protected Game-data bytes remain identical. Of 698 fingerprinted linked source
objects only `game_3BA70.c.o` changes; the debugger object and conversion CSV
remain identical. The scoped Graphify refresh retains all 60,046 prior node
IDs and does not claim a full-corpus extraction.

Fresh production recount: Game **3,768 / 4,843 (77.80%)**, total
**4,441 / 5,516 (80.51%)**, zero address drift. **107** further Game matches
are required for 80% at the current denominator.

Next screen: `func_15016850` appears to load unique asset IDs from 0x30-byte
records. The initial private C forms and diagnostics are retained under
`conker/build/game-unique-asset-load-15016850-screen/`; the closest extents
are 85 and 83 words against 84 retail words. The 85-word form has 79
same-position differences.
Preserve its live count reload, duplicate scan and persistent helper output;
it remains unqualified and receives no match credit.
