# Actor World Matrix Builder Direct Match

Date: 2026-10-15. Continue the whole additional-source/Game audit and the
matrix-builder boundary identified in
[Note 1388](1388-special-object-position-matrix-frame-and-guarded-match-20261015.md).
This is one completed function, not completion of the full remaining-source goal.

## Scope And Provenance

`func_1511490C` in `conker/src/game/generated_13D350.c` occupies
VA `0x1511490C..0x151149AC`, ROM `0x141DBC..0x141E5C`: 40 words / 160 bytes,
original frame `0x60`. Its old zero-return C placeholder was already counted
as converted. Preserve the original full-slice assembly and all neighboring C.

Start with clean consumer `4a36e432` and tools `c51788d`. Freeze 34 named
inputs in ignored `conker/build/game-actor-world-matrix/before-*`, extending
the preceding checkpoint with builder/scale/rotation source and assembly.
Every frozen input and manifest is fingerprint checked; do not recapture a
changed image as the baseline. Predecessor ELF:
`52b0efe2da54e3d78c4ad3ca102189d57d877ed313a245a055630650372133f6`.

The additional source contains callers but no definition of `func_1511490C`.
Reconstruct this missing dependency from retail, rather than label it a donor
import. The archive's `game_D5500.c` likewise retains GLOBAL_ASM for the lower
rotation provider; it is not available byte-matching C. Keep all original 801
archive fingerprints intact and distinguish source, assembly and modeled data.

## Direct C Recovery

Preserve the address-based function name and add a short purpose comment,
meaningful local names and one private scale-helper declaration. The routine:

- Builds the initial angle matrix through `func_151148A8(matrix, actor)`.
- Converts signed actor halfwords `0x10`, `0x12`, `0x14` to single precision.
  Adds the live float at `0x18` to Y, then writes matrix row 3's XYZ components.
- Builds a real local 64-byte scale matrix from the live floats at actor
  `0x2C`, `0x30`, `0x34`; these reads occur after the angle provider returns.
- Calls `func_150A7A48(scale, matrix, matrix)`, preserving the original
  in-place right-operand product and saved S0/S1 lifetimes.

Five complete-owner source forms have zero diagnostics. The first body has
the correct 40 words / frame `0x60`, but four FP allocation differences around
the Y conversion/addition. Writing the source expression as height plus signed
Y recovers all four original words. Explicit casts do not change the mismatch;
a named Y temporary changes the frame to `0x68` and is rejected. The accepted
body emits **all 40 retail words directly from C**, with three call relocations,
zero guards, no fake locals and unchanged O2/g3 flags and shared headers.

The actual generated-slice padder, assembler and linker preserve the match.
All 33 raw owner neighbors retain bytes, extents, relative relocation records
and normalized data pools. No guard manifest, layout or compiler profile changes.

## Fresh Qualification

All 14 final top-level checks pass in 146.515 seconds:

```sh
python3 -m tools.experiments.game_actor_world_matrix
python3 -m unittest tools.tests.test_game_actor_world_matrix \
  tools.tests.test_game_actor_world_matrix_candidates \
  tools.tests.test_game_actor_world_matrix_installed -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- 3,072 guest cases exercise signed extrema, live height/scales, signed zeros,
  provider mutations, both stack phases and three output/actor overlap layouts.
  All 40 words are reached. Complete modeled private states and independent
  public-memory/call references agree. Alias coverage is guest evidence, not
  portable C strict-aliasing or fault-semantics acceptance.
- 576 paired, fired parent-access cuts agree in complete modeled state. Opaque
  provider accesses are not counted as dispatched guest accesses. No hardware
  exception, nonfinite conversion or FCSR-equivalence claim is made.
- Native32 O2/O0 execute the actual builder C across 384 finite cases/profile,
  with explicit numeric halfword/FP endian bridges, all actor bytes, output
  canaries and ordered provider packets. Three effective guest/native returned
  controls reject unsigned coordinates, missing height and reversed product.
  The multiplication provider is the established bounded native product model.
- 256 guest connections freshly compile the existing direct 25-word angle
  wrapper and the scale C owner. Apply the scale owner's **three existing**
  scheduling guards through the production padder: its 20-word slot comprises
  19 body words plus one alignment NOP. Do not call its raw C a direct match.
  Execute the actual unchanged matrix-product assembly: 76 body words and two
  alignment NOPs. The two calls to `func_150A8050` remain modeled providers.
- Another 256 cases connect the actual 51-word position consumer, new 40-word
  builder, current angle/scale helpers, original product and 40-word point
  transform. Compare independently calculated coordinates and complete modeled
  state. All eight returned old-builder controls fail as expected, using the
  actual old ELF stub and a declared finite identity private-matrix seed.
- Three independent rebase pairs match the original isolated assembly, moving
  the routine and all three call targets separately. No normalization is used.

The native fixture initially missed the existing SSE `-mstackrealign` flag.
GDB locates its O2 crash at an aligned MOVAPS stack store in the bounded product
model; the existing native-helper compile recipe fixes it. A macro/field-name
collision and bypassing the scale padder were also harness errors, not target
source failures. Re-run the complete corrected qualification before banking.
Do not interpret the old stub's unseeded nonfinite matrix as a returned negative.

## Linked Audit And Progress

Independently construct the expected complete ELF from the old image, the retail
160-byte target slot and only its symbol extent `12 -> 160`. The normal build
equals it byte for byte: **123 changed bytes**, confined to target code/extent.
Every other ELF byte is fixed, without metadata exclusions or allowances.
All 189,088 protected data bytes / 720 owners remain exact.

| Input | SHA-256 |
| --- | --- |
| ELF | 3772196e96e4e1e09cbc7234ce6532e4d84e73661b4524a4c82cc31765158777 |
| Builder owner | 68d7d45a9b71049426ee12b4af3af36c7c7d455fb42bac2979e857eacc71fd89 |
| Unchanged guards | 311c81d50de789b4a51e3d27ac3ad2d0e0aabb9b07393ce004d34fdd1c822af2 |
| Unchanged progress CSV | 3ad7466c067bdb27e92248b8b237fb3dff392097ef3cd5d9a337d8268fbda091 |

All 34 current inputs are checked: two deliberate changes, 32 fixed inputs.
Effective controls flip every current input, source-text reads, seven real
in-file code/symbol/caller/helper/data locations and all before/after captures.
Only two exact known changed inputs are inverted for historical gates; corrupt
and unknown inputs are not mapped. The four preceding installed checks and
explicit historical caller/stub-boundary test pass, embedding the earlier
capture/view/actor/matrix gates and freshly checking all 801 archive files.
Current-image and actual consumer connections never use that inverse.

Fresh matching: Game **2,889/4,829 (59.83%)**, total **3,562/5,502 (64.74%)**,
different **1,940**, zero drift. Converted counts and bytes remain unchanged:
5,502/6,044 (91.03%), bytes 86.06%; Game 4,829/5,323 (90.72%), bytes 85.42%.
Init/Debugger remain 492/492 and 181/181 exact. README gets aggregate rows only.
The known duplicate generated_12D630 recipe warnings remain; the target owner
has zero compiler diagnostics. This is not a warning-free-project claim.

## Banking And Boundaries

Bank qualification tools `3e43b4a` before the consumer pin/source/docs. Shared
tools checks pass. Six owned files are syntax-checked in the standalone tools
copy and its three ROM-free checks pass. Gate the independent `ddbdd16` HEAD
and all 606 initial dirty fingerprints before copying only six absent owned
paths; preserve unrelated work and never commit/reset that mirror.
All 612 final dirty fingerprints are verified, including all 606 initial ones.
Seven documents / 4,925 relative Markdown links validate with none broken.

Full `graphify update .` refuses 19,276 nodes against the 41,056-node curated
graph, retaining 19,398 nodes from 2,972 excluded-but-present files. Keep the
fail-closed result and await the incremental commit worker, never force it.
Claude budget/calls: zero; direct compiler/assembly evidence settles this task.
No push, host source/build/launch, real-save/configuration or Release operation.

## Next Action

`func_150A8050` in `game_D5500.c` is still an empty production C body. Inspect
its 84-word retail slot, nonstandard saved-FP lifetime and six math-helper calls
before choosing semantic C recovery or identifying original handwritten code.
The archive supplies GLOBAL_ASM, not a recovered C implementation. Do not count
that assembly as C or infer initialized production angle matrices/gameplay from
the explicitly modeled rotation leaf in this checkpoint.

Continue that dependency and the wider failed-source/binding queue. Handwritten
Init hardware routines and the unmatched `func_1510BF60` seed remain separate
open work; this direct builder recovery does not complete the full goal.
