# Game projection bounds private screen

Date: 2026-11-14. `func_1510AEE0` remains a production placeholder in
`conker/src/game/generated_137ED0.c`; none of the candidates is a credited match.
The retail body is 97 instruction words at `0x1510AEE0..0x1510B064`, ROM
`0x138390..0x138514`. Three alignment words extend the slot to
`0x1510B070`, ROM `0x138520`.

The routine transforms a point with a 4-by-4 matrix, negates the depth
component and returns 1 when it lies outside the supplied depth or projected
horizontal/vertical bounds. Otherwise it returns 0 and, for each non-null
output pointer, writes one minus the corresponding scaled absolute component
divided by depth. The original reads both projected components before writing
either output, and reloads the second output pointer after the first write.
An aligned Game scan finds four direct calls at `0x151767CC`, `0x15176830`,
`0x15177138` and `0x1517A448`; an aligned input scan found no literal target
pointer. These scans do not rule out computed or external calls.

Tools commits `e6a29db` and `d8398fc` retain three private candidates and
their checks. The first two emit 96 words and a `0x10` frame; the first has
27 words at retail positions, the staged-expression form has 15. A third
staged form makes the second output pointer volatile and emits the full
97-instruction body length, but only 17 words occupy their retail positions.
That extra qualifier is a code-generation experiment whose behavior and
original provenance need qualification. All three other compiled owner
functions, normalized pools and compiler diagnostics remain unchanged. No
version has an acceptable complete retail instruction stream yet.

An independent finite guest model checks 360 cases per stream, including
depth boundaries, two matrices, null and shared outputs, and outputs aliasing
the matrix; all three candidate streams agree with retail in these cases. Three
altered-instruction controls are rejected. A separate 16-case quiet-NaN
payload probe uses two explicit rules: left or right NaN operand wins, with
the quiet bit set. Under either assumed rule the first candidate differs from
retail in 12 cases; the two staged forms have no observed difference in these
samples. The actual hardware NaN-propagation rule is **not verified** and the
guest does not model FCSR exceptions. Earlier exploratory counts from the
host interpreter varied with execution context, so they are not hardware
evidence.

The mounted and isolated sibling-overlay suites passed, `make tools-check`
passed, and the sibling checkout's existing dirty paths were preserved. Run
the fingerprinted pre-install screen with:

```sh
PYTHONPATH=. python3 -m tools.experiments.game_projection_bounds_1510aee0_screen
```

Further work should recover the actual source shape and floating-point
operation order, including the volatile-output experiment, then qualify caller
behavior, exceptional values, native C, padding and the production image. The last verified Game
count remains **3,785 / 4,843 (78.15%)**, with **90** more matches needed
for 80% at the current denominator.
