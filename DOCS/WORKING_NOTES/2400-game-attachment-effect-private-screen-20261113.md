# Game attachment-effect private screen

Date: 2026-11-13. `func_150F97EC` remains a **production placeholder** in
`conker/src/game/generated_124920.c`; this investigation does not claim or
count a match. The 89-word retail slot occupies `0x150F97EC..0x150F9950`, ROM
`0x126C9C..0x126E00`.

The retail routine reads an attachment pointer at actor offset `0x1D4` and,
if present, transforms a fixed point using a matrix selected by the byte at
`D_80088B50`. It then draws two floating random values, two integer random
values and a third floating random value, in that order, before calling
`func_15102B38` with the transformed position and randomized parameters. The
slot byte is read again for the final call, so the model includes a helper
changing it between the two reads. The caller must supply a valid actor:
retail dereferences it before testing the attachment.

One original direct call is at `0x15028910` in `func_150265CC`; the bounded
window passes the actor already in `a0`, a stack-sourced byte in `a1` and 1 in
`a2`. An aligned Game-instruction census found this one direct call, and an
aligned literal-address scan of the prepared input found no target pointer.
These scans do not rule out computed or external calls.

The private O2 candidate captured by tools commit `7880db0` emits 87 words,
with a `0x68` frame and 14 same-position retail words. The 16 other compiled
owner functions, normalized pools and diagnostics are unchanged. In particular,
the compiler removes retail's `mul.s` by the literal `1.0f` before adding
`2.0f`; the candidate therefore does not establish exceptional floating-point
or FCSR equivalence. Its pointer locals and frame also differ. It is not safe
to promote or credit this candidate on a finite behavioral screen alone.

A local declaration experiment expands the scale array to three elements and
reorders the two addressable pointers. It restores the `0x70` frame and the
observed retail point/input/output stack locations, but still emits 87 words
and matches only 21 positions. Making the multiplier a volatile local produces
91 words with a `0x70` frame in the comparable two-element layout; it does not
reproduce the original instruction stream. The extra array element and
volatile local are shape experiments, not established original declarations.
Exploratory compiler-only O1/O2/O3 and O2 option checks used an O2 assembly
processor pass: O1 yielded 98 words and a `0x78` frame, while O3 and the two
tested O2 options retained the 87-word result. These are not qualified
production Make profiles; O3 also produced tool warnings.

The reproducible private screen is:

```sh
python3 -m unittest tools.tests.test_game_attachment_effect_150f97ec_screen -v
```

It passed in mounted tools and an isolated sibling overlay using available
sibling dependencies and mounted fallbacks. The independent modeled-helper
guest check covers 96 finite cases per retail/private stream and rejects three
altered-instruction controls. A three-instruction original caller window
covers 32 cases per stream. These checks cover the specified helper arguments,
random order, position values and selected global mutation; they do not prove
complete caller execution, actual helper behavior, unrestricted aliases,
exceptional floating-point behavior, fault-prefix equivalence, native C,
padding, whole-image identity or gameplay. `make tools-check` passed and the
sibling checkout's pre-existing dirty state was preserved.

Production source and counts are unchanged: Game **3,783 / 4,843 (78.11%)**,
with **92** further matches needed for 80%. Continue by recovering the
literal floating multiply and the complete retail local layout, then repeat
the remaining ABI, guest, native, padder and linked-image qualification gates.
The 87-word `func_1517AA20` is another possible target if that fitting work is
deferred. An initial private screen produced 91- or 97-word bodies while
preserving its ten neighboring compiled functions. Its helper
`func_1517A644` is currently a no-argument placeholder in the same source
file, so the experiment used an incompatible function-pointer cast to explore
the retail call shape. Those candidates are **not installable**, and their
floating conversions, random loop, helper ABI and callers remain unqualified.
The exploratory files are in ignored
`conker/build/game-random-scatter-1517aa20-screen/`.
