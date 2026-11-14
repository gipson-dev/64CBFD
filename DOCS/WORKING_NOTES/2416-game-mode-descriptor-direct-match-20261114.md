# Game mode-specific descriptor direct match

Date: 2026-11-14. The C body of `func_150F5420` replaces a zero-return
placeholder and emits all 92 retail instructions directly, without word
guards. Its slot is `0x150F5420..0x150F5590` (ROM
`0x1228D0..0x122A40`) in `conker/src/game/generated_1228D0.c`.

The function builds a 0x3C-byte descriptor from three full-word inputs and a
mode, selects one of four asset addresses and mode-specific dimensions, then
returns the result of `func_15169968`. Packing uses full-word OR and
32-bit wrapping addition; it does not first mask the second argument or sum
to 16 bits. The function writes 51 descriptor bytes. Nine retained stack
bytes are not initialized by this routine; native tests exclude those bytes
while guest checks preserve and compare them.

The raw and both padded instruction streams and relocations match retail.
Both padder paths passed 12 GNU links across four target and independent asset
and callee symbol layouts. All 23 neighboring functions and normalized
constant pools remained unchanged. The compiler emitted the same existing
diagnostics after normalizing shifted source lines.

Retail, raw and padded guest executions agreed in 4,720 cases each, covering
four mode branches, full-word boundaries, null and non-null returns, two stack
alignments and modeled descriptor changes. The original 34-instruction
`func_15169968` / `func_15169900` provider path was connected in half
the cases; allocation and bcopy were bounded modeled services. Another 896
cases execute windows of both original callers, including their delay slots;
1,064 fired access prefixes compare full guest machine state. These checks do
not claim complete caller, allocator, hardware or gameplay behavior.

Native 32-bit C passed 3,430 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. Eight altered
source controls were detected. Layout offsets and the return pointer were
checked; indeterminate descriptor bytes were deliberately excluded from the
native comparison.

The actual production Make rebuild equals the independently predicted shadow
ELF. The strict image audit accounts for 398 changed bytes, including four
equal-address symbol metadata ordering groups, with zero exclusions. All
6,051 function addresses and 189,088 protected data bytes remain fixed; only
the target owner changed among 698 frozen linked objects. The existing guard
manifest and conversion CSV remain unchanged. A scoped fail-closed Graphify
refresh retained all 60,119 prior node IDs; this was not a full-corpus
re-extraction.

Tools commit `5dce870` contains the installed regression suite:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_mode_descriptor_150f5420_installed -v
```

The installed suite passed in the mounted tools checkout and the isolated
sibling tools overlay; `make tools-check` passed. Pre-existing sibling edits
were preserved.

Fresh production recount: Game **3,792 / 4,843 (78.30%)**, total
**4,465 / 5,516 (80.95%)**, zero drift. **83** more Game matches are needed
for 80% at the current denominator. The private `func_1515942C` candidate
in [Note 2415](2415-game-selector-mask-private-screen-20261114.md) remains
uncredited and needs its 95-word body reduced to the 90-word retail slot.
