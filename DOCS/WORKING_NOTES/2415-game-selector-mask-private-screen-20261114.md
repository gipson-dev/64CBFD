# Game selector-mask private screen

Date: 2026-11-14. `func_1515942C` remains a zero-return production placeholder
in `conker/src/game/generated_185560.c`; no candidate is credited. Retail has
90 instructions at `0x1515942C..0x15159594` (ROM `0x1868DC..0x186A44`).

The routine calls `func_1514ECE0` for key `0x13` using the actor's linked list
at `0x2F4`. If found, it reads five selector bytes at offsets `0x2C..0x30` in
the node's data, forms a bit for each, and tests whether their combined bits
are contained in the masks selected by five signed halfword arguments. The
value `-1` selects an entire field mask. The MIPS variable-shift instruction
uses only the low five shift bits; the private C explicitly masks shift counts
to express that behavior without out-of-range C shifts.

With the owner's `-O2 -g3` profile, the first semantic candidate emits 98
words, 16 at retail positions, with the retail `0x40` frame. It agrees with
retail on sampled return values but changes the public byte-read order in
2,048 of 4,096 cases. A revised candidate arranges the reads in retail order
and declares the local pointer and result byte in the order that recovers
their retail stack homes. It emits 95 words, 18 at retail positions, with the
same frame. It remains five words too long and is not installable as a match.
All 36 neighboring compiled functions, normalized constant pools and existing
compiler diagnostics remain unchanged in these private compiles.

In 4,096 modeled cases per stream, retail and the revised candidate agree on
return values, public memory and ordered public accesses. This includes
signed selector boundaries, byte-valued fields, missing/found lookups, and a
modeled helper that changes incoming argument homes. An additional 512 cases
connect the original 23-instruction `func_1514ECE0` lookup, and 512 use the
original seven-instruction caller window at `0x1507F128`; public returns and
accesses agree in both screens. In 102 private-stack overlap cases, modeled
return values and full access traces agree. Four altered retail instruction
controls were rejected. These cases do not establish unrestricted aliases,
all guest fault prefixes, full caller behavior or hardware execution.

The private C passed 328,960 native 32-bit cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. The corpus tries
every signed 16-bit value in each selector and every byte value in each field,
with the other inputs held to the documented fixture values. A shift-mask
mutation was rejected in both aliasing modes. These native tests use a modeled
lookup and are not a retail binary comparison.

Tools commit `2583bdd` retains both source shapes, the fingerprint-bound
screen and its tests. With the recorded 91 owner, compiler, header and build
inputs still present, run from the decomp root:

```sh
PYTHONPATH=. python3 -m tools.experiments.game_selector_mask_1515942c_screen
```

The screen passed in the mounted tools checkout and an isolated sibling
overlay; `make tools-check` passed. The sibling checkout's prior dirty paths
were preserved. A scoped graph update for the added tools reported no tracked
files and skipped rebuilding; all 60,117 previously recorded node IDs remained.

Next, recover a 90-word source/profile and retail instruction schedule while
preserving the five-bit shift behavior, frame, local homes and ordered reads.
Then qualify guest fault prefixes, padding, independent relocations, actual
Make and the full production image before installing or counting the routine.
The last verified production recount remains Game **3,791 / 4,843 (78.28%)**,
total **4,464 / 5,516 (80.93%)**, zero drift; **84** more Game matches are
needed for 80% at the current denominator.
