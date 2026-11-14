# Private Game matrix-phase candidate

**Update:** The candidate was subsequently qualified and installed; see [Note 2396](2396-game-matrix-phase-update-match-20261113.md).

Date: 2026-11-13. `func_150F1A00` in `generated_11C2B0` remains a
zero-return placeholder in production. The 82-word retail body occupies
`0x150F1A00..0x150F1B48`, ROM `0x11EEB0..0x11EFF8`. The candidate is not
installed and is not counted as a byte match.

The retail routine copies three halfword rates, selects one from actor flags,
advances a shared signed phase with wrapped tick arithmetic, passes a
single-precision angle to `cosf`, and uses the result to scale three columns
of each of three matrix rows. The matrix pointer is read from the actor after
the cosine call. The alternate source has incompatible rate, phase and matrix
types and is not used as matching evidence.

The private semantic C candidate compiles to 82 words under the owner profile,
without diagnostics. Its 43 owner neighbors and constant pools are unchanged;
18 words match at the same positions after relocations are bound. This is not
a byte match: register allocation, scheduling and loop structure still differ.
Other screened loop shapes and a no-unroll profile did not establish a match.

Tools commit `7ba66ba` provides a repeatable, input-pinned screen:

```sh
python3 -m unittest tools.tests.test_game_matrix_phase_150f1a00_screen -v
```

The original retail stream and private C stream each pass 480 guest cases
against an independent single-precision model. The cases cover flag priority,
phase wrap, tick boundaries and a `cosf` stub that may change the actor's
matrix pointer. Four incorrect versions are rejected. The floating constants
and stubbed cosine results in this screen are synthetic; this does not validate
the real `cosf`, native C behavior, memory-fault order or gameplay. An aligned
Game-ROM scan finds one direct call, at `0x15034700`; executing its original
caller window remains outstanding. The existing caller prototype returns
`s32` although the retail caller ignores the return, so its ABI should be
corrected and the entire caller object rechecked during qualification.

Both mounted and independent sibling tools runs passed, as did `make
tools-check`; the sibling's pre-existing dirty paths were preserved. Next,
reduce and explain the instruction differences, qualify the caller, native
and guest behavior including access faults, both padders and rebased links,
then run actual Make and an independently predicted full-image comparison
before considering production installation and recount.

Production remains Game **3,779 / 4,843 (78.03%)**, total **4,452 / 5,516
(80.71%)**, with zero drift and **96** more Game matches needed for 80% at
the current denominator.
