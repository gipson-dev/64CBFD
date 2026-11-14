# Game quaternion-to-matrix private screen

Date: 2026-11-14. `func_1504A140` remains a zero-return production
placeholder in `conker/src/game/generated_770F0.c`; no candidate is a
credited match. Retail has 89 instructions at `0x1504A140..0x1504A2A4`,
followed by three padding words through `0x1504A2B0` (ROM
`0x775F0..0x77760`). A direct caller is present at `0x150397E8`; the full
caller contract and computed or external calls remain unqualified.

The function reads four floats and writes a quaternion-derived matrix,
leaving output elements 12 through 14 untouched. Retail computes its norm's
last addition as `w*w + ((x*x + y*y) + z*z)`. The earlier private draft in
[Note 2307](2307-game-position-interpolation-candidate-screen-20261112.md)
reversed those final operands. That distinction can affect NaN payloads even
when ordinary finite results agree. The exact IEEE behavior of the target has
not been established by this screen.

Four candidate shapes were compiled with the owner's `-O2 -g3` flags. The
original and corrected scalar forms emit 86 words and have 8 and 9 words at
retail slot positions, respectively; both use a `0x68` stack frame. The
corrected nine-element temporary-array form emits 92 words with 11 words at
retail positions and a `0x58` frame. A direct-input-read array form reaches
retail's `0x48` frame but emits 97 words, with seven at retail positions; it
also introduces repeated input reads. All three neighboring compiled owner
functions, normalized constant pools and compiler diagnostics are unchanged.
These are isolated compiler screens, not actual Make or padded-image results.

An independent big-endian model checks 1,280 finite cases per stream: 256
four-component inputs with nonzero finite norms and five distinct input/output
overlap arrangements. All four candidate streams agree with the retail stream
and the model in final public memory. Three altered retail instructions are
rejected by the corpus. A separate probe checks 80 quiet-NaN inputs under each
of two explicitly assumed propagation rules: left or right NaN operand wins,
with its quiet bit set. The original draft differs from retail in 14 and 26
cases respectively; the corrected scalar differs in zero under either rule;
the corrected array differs in 50 and zero; and the direct-read form differs
in 50 and 34. These modeled outcomes do not establish the hardware NaN rule
or FCSR exception behavior.

The mounted and isolated sibling-overlay screens passed, as did `make
tools-check`; the sibling tools checkout's existing dirty paths were
preserved. Tools commit `e0f9d39` retains the screen. Run it from the decomp
repository root:

```sh
PYTHONPATH=. python3 -m tools.experiments.game_quaternion_matrix_1504a140_screen
```

Further work should recover the retail frame, access order and arithmetic
schedule in the same source shape, then qualify exceptional values, aliases,
fault prefixes, private-stack overlap, native behavior, the caller, padding and
the full production image before installing or counting the function. The
fresh production recount remains Game **3,786 / 4,843 (78.17%)**, with
**89** more matches to 80% at the current denominator.
