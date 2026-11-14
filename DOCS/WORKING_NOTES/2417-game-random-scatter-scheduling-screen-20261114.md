# Game random-scatter scheduling screen

Date: 2026-11-14. `func_1517AA20` is still a zero-return production
placeholder in `conker/src/game/generated_1A7260.c`. Retail occupies
87 instructions at `0x1517AA20..0x1517AB7C`
(ROM `0x1A7ED0..0x1A802C`). This private screen changes no production
source and is not credited.

The routine rejects a radius below 12, obtains four random values per
iteration, forms two horizontal offsets, computes a size from an unsigned
remainder and the half-radius, and calls `func_1517A644`. Its original
caller window at `0x1518384C..0x15183880` supplies a float, three
integer coordinates converted from floats and a stack count. This observation
does not qualify the complete caller, random generator or helper.

The earlier screen in [Note 2400](2400-game-attachment-effect-private-screen-20261113.md)
produced 91- or 97-word bodies through an incompatible function-pointer cast.
This screen replaces that cast with a typed helper definition and moves the
halfword conversion of the third input after the radius check. Under the
existing IDO profile, the selected private body is 85 words, with 51 words
at the same positions as retail; the original frame and the prologue through
the radius check align. The unsigned additions in the candidate avoid signed
overflow for its horizontal sums. The candidate is still two words short and
its loop-register allocation, call schedule and remaining instruction words
differ.

The typed helper definition has its own unresolved consequence: IDO changes
the unfinished `func_1517A644` stub from 12 to 28 raw bytes by adding four
argument-home stores. Retail also homes those arguments, but that observation
does not make the changed stub or its aliases equivalent to the original
helper. The nine other raw owner functions, normalized pools and diagnostics
are unchanged. The helper remains a placeholder, and changing it requires
its own interface, caller, object and image audit.

No guest, native, exceptional-float, RNG, alias, fault-prefix, padder or
full-image behavior is qualified by this scheduling screen. In particular,
the C float-to-integer conversion needs explicit investigation for NaNs,
infinities and out-of-range values. Do not install this candidate based on
its instruction count or positional agreement.

Tools commit `a3b833a` preserves the selected source shape and a screen
bound to 92 owner, header, compiler, assembly, ROM and build inputs:

```sh
PYTHONPATH=. python3 -m tools.experiments.game_random_scatter_1517aa20_schedule_screen
```

The screen passed in the mounted checkout and isolated sibling tools overlay;
`make tools-check` passed. The sibling's pre-existing edits were preserved.
The scoped Graphify update for the tools file reported no tracked source to
rebuild and retained all 60,121 prior node IDs; this was not a full-corpus
re-extraction.

Next, recover the two missing retail words and the loop register/call schedule,
resolve the helper interface without silently changing another function, and
qualify finite and exceptional floating behavior, caller and helper contracts,
guest/native cases, padding and the linked image. The last production recount
remains Game **3,792 / 4,843 (78.30%)**, total **4,465 / 5,516 (80.95%)**,
with zero address drift and **83** more Game matches to 80%.
