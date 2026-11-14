# Game group output lookup private screen

Date: 2026-11-14. `func_15022024` remains a production zero-return
placeholder in `conker/src/game/generated_49D30.c`; the candidate is not a
credited match. Retail has 91 instruction words at `0x15022024..0x15022190`,
ROM `0x4F4D4..0x4F640`.

The routine checks a group-enable byte and scans its enabled records for type
2 and the selected actor's identity byte. On a match it clears two pairs of
output floats, then replaces each pair from the corresponding record values
unless that value equals the shared sentinel. The retail stream snapshots the
sentinel before its output writes, reloads each first output before copying it
to the second slot, and reloads the runtime record pointer after the first
non-sentinel pair. An empty group count returns without loading its enabled
record pointer. A direct caller at `0x1503B204` passes two stack output pairs,
an actor index, and group zero; computed or other external calls are not
excluded by this observation.

With the owner's `-O2 -g3 -Wo,-loopunroll,0` profile, the ordinary-pointer
candidate emits 86 words, with three at retail positions. A version with
volatile output pointers emits 88 words, with nine at retail positions. Retail
saves `s0`, `s1`, and `s2` in a 0x10-byte frame; these candidates save only
`s0` in an 8-byte frame. This qualifier is a code-generation experiment, not
proof that the original C was volatile. All 56 neighboring compiled functions,
normalized constant pools, and compiler diagnostics matched the baseline.

The retained independent big-endian guest model checks 972 cases per stream,
including a disabled group, zero count, disabled entries, wrong record type,
identity mismatch, a match at each of three indexes, finite and quiet-NaN
values, and six output/runtime overlap arrangements. Retail and both private
candidates agree in the sampled final memory and return values; three altered
retail instruction controls are rejected. In 432 additional access-trace
cases, the ordinary-pointer build differs from retail 63 times because it omits
output reloads; the volatile variant has no sampled public-access difference.
None of the streams reads the enabled pointer on the sampled zero-count path.
These cases use group zero, actor one, and a three-record fixture. The guest
model does not establish hardware FCSR exception behavior, unrestricted C
aliasing, guest fault prefixes, private-stack overlap, native behavior, or
complete caller behavior.

Tools commit `d84d3e9` retains the reproducible screen. Run it from the decomp repository root:

```sh
PYTHONPATH=. python3 -m tools.experiments.game_group_output_15022024_screen
```

The mounted and isolated sibling-overlay screens passed, as did `make
tools-check`; the sibling tools checkout's existing dirty paths were
preserved. Further work should recover a retail-length register/frame shape,
then qualify the emitted stream, caller, aliases/faults, padding and full
production image before installing or counting the function. The last
verified Game count remains **3,786 / 4,843 (78.17%)**, with **89** more
matches to 80% at the current denominator.
