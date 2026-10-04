# Game Linked Record Position Exit Layout Trials

Date: 2026-10-04. Starting HEAD: `4e4a5acb`.

## Hypothesis And Reproducibility

Continue Note 920's final return-tail investigation without touching production
source. `tools/experiments/compile_game_linked_record_exits.py` extracts the
actual production `func_150E6FAC` body and constructs five bounded source forms:

- Current if/else control.
- Explicit return after successful output, retaining else.
- Success goto a common return label.
- Early failure copy/return, followed by successful computation.
- Failure goto a fallback label, with success falling through to return.

Each is compiled under O2/g3, O2, O1/g3 and O1, linked at `0x150E6FAC` with
absolute helper addresses. Compare the whole body through the final JR RA
delay instruction against the 72-word pristine slot. Trailing section padding
is excluded; excess or missing body words count as differing positions.

## Measurements

Cells are body words / differing aligned positions, not semantic mismatch counts.

| Shape | O2/g3 | O2 | O1/g3 | O1 |
| --- | ---: | ---: | ---: | ---: |
| Control | 71 / 15 | 71 / 19 | 89 / 89 | 89 / 89 |
| Success return | 71 / 15 | 71 / 19 | 89 / 89 | 89 / 89 |
| Success goto | 71 / 15 | 71 / 19 | 89 / 89 | 89 / 89 |
| Failure return | 71 / 62 | 71 / 66 | 89 / 89 | 89 / 89 |
| Failure goto | 71 / 15 | 71 / 19 | 89 / 89 | 89 / 89 |

None matches. The return/goto variants canonicalize to the control's shared
RA-load tail under O2/g3. An early failure return places fallback ahead of
the computation rather than generating retail's duplicated RA load. O1
cannot fit the slot. Removing g3 does not resolve the tail and adds scheduling
differences. Do not adopt a whole-slice profile based on these failed fixtures.

## Verification

For each source shape, the driver runs the four existing host semantic tests
against that generated body: failed lookup, 35 RNG word/fraction combinations,
callback mutation and overlapping output. Twenty shape/test runs pass, no
skips. These qualify the fixture behavior, not guest execution of all twenty
profile outputs or hardware. All final guest compiler logs are empty.

```sh
python3 -m tools.experiments.compile_game_linked_record_exits
python3 -m unittest tools.tests.test_game_linked_record_position tools.tests.test_game_random_range_position tools.tests.test_game_object_position_sound_adapter -v -f
```

Driver retains sources, objects, ELF/binary output, disassembly and JSON
measurements under ignored `conker/build/game-linked-record-exits/`.
An initial diagnostic run exposed IDO's handling of absolute paths containing
spaces: it returned success without creating the object. The driver now passes
relative source/output paths from the repo root and requires object existence.
The final complete matrix ran successfully; that failed setup is not counted
as a compilation result.

Production source/profile/guard diffs are empty. No production rebuild or
fresh aggregate change is needed or claimed for isolated rejected trials.
Retain Note 920's direct C improvement and its exact-prefix test. README
snapshot and Init assembly/decoder gates remain unchanged. Unrelated actor/
timeline edits remain excluded; no sibling adoption, host build, Release change
or push. Further matching needs a new explanation for duplicated RA loads,
not repetition of the measured return/goto/profile forms.
