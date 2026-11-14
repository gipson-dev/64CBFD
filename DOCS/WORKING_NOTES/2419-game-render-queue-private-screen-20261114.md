# Game render-queue private screen

Date: 2026-11-14. `func_15035FE8` remains a zero-return production
placeholder in `conker/src/game/generated_61D10.c`. Retail has 88
instructions at `0x15035FE8..0x15036148`
(ROM `0x63498..0x635F8`). This screen is not installed or credited.

The observed routine returns the incoming display-list pointer if the queue
count is zero. Otherwise it writes three graphics commands: set smooth
shading and shade, clear fog and LOD, and disable alpha compare. It walks
12-byte queue entries, skips entries whose byte 11 is nonzero, and calls
`func_1502CCFC` for each remaining entry with its matrix, slot, alpha and
three colors. The fourth color parameter is 255. The renderer reloads the
queue count after a helper call; a skipped entry uses the last loaded count.
Its caller in `game_45B80.c` consumes the returned display-list pointer.

The selected private candidate uses the SDK graphics macros for the latter
two commands and expresses the first command's retail store order explicitly.
Typed queue fields, unsigned queue-end comparison, ordered volatile field
loads and declaration order recover the helper parameter block at the same
guest address as retail. The candidate has the same 88-word length, but only
two words at the same positions. It uses a 0x70-byte frame versus retail's
0x68 and has different saved-register allocation and scheduling. All nine
other raw owner functions and normalized pools are unchanged; compiler
diagnostics are empty.

Retail and private guest streams agreed with an independent bounded model in
224 cases each, including empty queues, skipped entries, helper-driven count
growth and shrinkage, command output and helper arguments. The observed
public read/write order and helper parameter addresses also agreed in these
cases. Four altered retail-instruction controls were detected. The helper was
modeled, queue and output regions were disjoint, and the inputs were limited
to six entries. This does not establish unrestricted aliases, guest fault
prefixes, the complete renderer or caller, portable C behavior, hardware or
gameplay. The different frame and saved-register lifetimes remain material.

Tools commit `781ffa4` preserves the private source and a screen bound to
92 owner, header, compiler, assembly, ROM and build inputs:

```sh
PYTHONPATH=. python3 -m tools.experiments.game_render_queue_15035fe8_screen
```

The screen passed in the mounted checkout and an isolated sibling tools
overlay; `make tools-check` passed. The sibling checkout's existing edits
were preserved. A scoped Graphify update for the tools file reported no
tracked source to rebuild and retained all 60,125 previous node IDs; this was
not a full-corpus re-extraction.

Next recover the retail saved-register lifetime, 0x68 frame and instruction
schedule, then qualify aliases, fault prefixes, native C, both padders and
the full linked image before installing or counting the function. The last
production recount remains Game **3,793 / 4,843 (78.32%)**, total
**4,466 / 5,516 (80.96%)**, zero drift; **82** more Game matches are needed
for 80% at the current denominator.
