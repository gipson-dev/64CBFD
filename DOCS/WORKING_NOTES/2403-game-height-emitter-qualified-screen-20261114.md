# Game height emitter qualification screen

Date: 2026-11-14. This extends [Note 2402](2402-game-height-emitter-private-screen-20261113.md).
`func_150E971C` remains a production placeholder and does not count as a
match. Tools commit `1bcc62d` retains the private candidate and checks below.

The earlier candidate called the integer random helper directly inside the
emitter's argument list. C does not specify the evaluation order of those
arguments. In the native32 screen, a random-helper stub mutates the actor's
tag before returning; GCC read the old tag in all six tested optimization and
aliasing configurations. Explicitly storing the random result before the
call fixes that observed ordering problem. The sequenced C emits 91 words,
67 already at their retail positions, and leaves 28 other compiled owner
functions and normalized pools unchanged.

A private proposal with 24 expected-word guards restores the retail frame,
stack offsets and descriptor-store sequence. Its complete 91-word stream
matches retail. The padder screen uses the Makefile's `D_800A1350` retail
constant binding; omitting that binding produces a different relocation in
neighbor `func_150E7C9C`. With the binding, all 28 other padded owner
functions match the production object, including relocations. The proposal
is not installed in the production guard CSV.

Validation of the private streams:

- An independent modeled-helper guest reference checks 160 cases per stream,
  including a quiet NaN comparison, all 40 descriptor bytes, helper
  mutations and three effective altered-instruction controls. It does not
  model FCSR exception behavior.
- The original 53-word movement helper is connected for 72 cases per stream;
  the original indirect caller window is connected for 48. Other helpers are
  stubbed, and these are bounded windows rather than complete call chains.
- Native32 runs 24 cases at O0, O2 and O3 with both alias modes and trapping
  UBSan. The sequenced candidate passes; three altered-source controls and
  the unsequenced candidate are rejected. The cases use disjoint objects and
  do not prove unrestricted alias behavior or native preservation of
  uninitialized stack bytes.
- The actual Make recipe in a private shadow, followed by an independent
  strict whole-ELF prediction, changes 270 bytes with zero exclusions. All
  6,051 function addresses remain fixed, only this function's body changes,
  and all 189,088 protected Game-data bytes remain exact.

Run the fingerprinted screen from the consumer root:

```sh
PYTHONPATH=. python3 -m tools.experiments.game_height_emitter_150e971c_screen
```

The screen requires the recorded pre-install ROM, ELF, owner source, compiler,
guard CSV and linked object; it fails closed if they change. `make tools-check`
passed, and the separate sibling tools checkout's pre-existing dirty state was
preserved. Further work should qualify the guard proposal and frame under both
padders, fault and stack-overlap boundaries, and the remaining native/guest
behavior; then run the production build, recount and documentation gates before
crediting any match. The last verified Game count remains **3,784 / 4,843
(78.13%)**, with **91** more matches needed for 80%.
