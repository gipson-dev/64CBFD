# Game Actor Triangle Remap Recovery And Matrix Tail Restoration

Date: 2026-10-05. Starting checkpoint: `d047d0a1`.

This follows [Note 1011](1011-game-actor-buffer-copy-direct-match-20261005.md).
The complete `func_1502F490` body replaces its false zero-return placeholder.
It is semantic recovery, **not a byte match**. The required matrix leaf is
restored as original assembly because its retained continuation has a
register-specific interface that ordinary C does not express.

## Installed Production

| Function | Result | Body / Slot Words | Frame | Differing Words |
| --- | --- | ---: | ---: | ---: |
| `func_1502F490` | Complete semantic C | 298 / 302 | 0x160 | 275 |
| `func_150A7960` | Original assembly restored | 40 / 40 | 0 | 0 |

The transform occupies `0x1502F490..0x1502F948`, ROM `0x5C940`.
Retail has 302 words and frame 0x138; the old zero-return slot had 295
differing words. The selected default IDO form fits with four ordinary
trailing slot NOPs supplied by the existing padding tool. No compiler
override, expected-word guards or artificial body padding is added.

The reproducible screen contains **18 controls** (17 parent forms and one
ordinary-matrix control). Representative results:

| Form | Body Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Indexed baseline / flat points | 309 | 0x158 | 284 |
| Selected pointer transforms | 298 | 0x160 | 275 |
| Pointer vertex capacity 4 | 298 | 0x168 | 275 |
| Pointer vertex capacity 8 | 298 | 0x178 | 275 |
| Range do-loop | 296 | 0x160 | 279 |
| Pointer register locals | 298 | 0x160 | 275 |
| Range do-loop register locals | 296 | 0x160 | 279 |
| Ordinary C matrix leaf, rejected | 42 | 0 | 42 |

The 309-word baseline exceeds the slot and is never installed. Register
keywords do not improve the selected form. Larger vertex capacities increase
the frame, and the shorter range do-loop increases real differences. These
controls are evidence for the next layout investigation, not completion.

Source and reproducible controls:

- [generated_58F80.c](../../conker/src/game/generated_58F80.c): typed actor,
  16-byte signed-coordinate vertex and 12-byte unsigned range views; complete
  five-argument transform; layout cast at its existing coordinate-phase call.
- [generated_D4E10.c](../../conker/src/game/generated_D4E10.c): original matrix
  leaf assembly inclusion beside the already-retained trampoline/continuation.
- [Candidate driver](../../tools/experiments/game_actor_triangle_transform_candidates.py):
  bounded layout and semantic controls, including the rejected ordinary C leaf.
- [Focused tests](../../tools/tests/test_game_actor_triangle_transform_match.py):
  retail/raw-C/live-ELF execution comparisons, real matrix connections,
  independently written native reference and tail-register checks.

## Recovered Contract

1. Cache the actor ID at +0x04. Read `D_800C6070[id]` and return if null
   before reading the base, count or actor buffer. Construct three vertex
   pointers from `D_800D19A0[id]` and the three joint-indexed offset words.
2. Load the unsigned-halfword count from `D_800C5EF8[id]`. Scan the ranges
   in `D_800C5C08[id]` in order. For each unmatched vertex, accept unsigned
   address `>= start` and `< start + (count << 4)`, with 32-bit wrapping.
   Capture the first matching matrix index only. Return on count exhaustion;
   stop as soon as all three mask bits are set.
3. Only then cache actor +0x1D8. Return if that buffer is null, without
   reading +0x1D4. Test +0x1D4 for null. Transform all three vertices with
   the cached buffer, then freshly read +0x1D4 once for the second set.
   Keep the second base cached across its three calls. Vertex addresses and
   matrix indexes stay cached; each call freshly reads signed-halfword XYZ.
4. Call `func_150A7960` with seven arguments: matrix base plus index << 6,
   three converted float coordinates and three private output pointers.
   Build both sets' edges as point 1 minus point 0 and point 2 minus point 0.
5. Freshly read input XYZ after all six calls. Compute the first weight
   from the X/Z determinant; zero determinant selects -100.0f. Reject weights
   outside [0,1]. Compute the second weight using the old second edge's Z;
   zero Z also selects -100.0f, followed by the same ordered rejection.
   **There is no additional sum-of-weights <= 1 gate.**
6. Blend the new edges. Replace old relative Y with the old edge blend.
   Perform ordered, fresh X/Y/Z read/modify/stores as
   `*axis += ((newBlend + newPoint0) - oldRelative) - oldPoint0`.
   Do not simplify that expression: the explicit finite single-precision
   rounding fixture produces 16.0f, while direct assignment produces 18.0f.

The external ID tables remain unsized. Synthetic 256-ID fixtures qualify
the byte-ID interface, not a claim that every retail table owns 256 records.
High joint 0x8000/0xFFFF guest fixtures qualify sparse addressing and the
full fifth argument, not a retail asset-bound assertion or native C domain.

## Matrix Leaf And Tail Interface

`func_150A7960` occupies `0x150A7960..0x150A7A00`, ROM `0xD4E10`.
Its original frame-free 40 words preserve A0/T9 and input F0/F2/F4.
All matrix inputs are loaded before the ordered output stores; each axis
uses `(m0*x + m4*y) + (m8*z + m12)`.

The retained five-word `func_150A7A00` saves RA in T9, sets RA to
`func_150A7A14`, and jumps into this leaf. The 13-word continuation consumes
the still-live matrix pointer and input FP registers to calculate the fourth
component, then returns through T9. An ordinary C XYZ helper emits 42 words
and breaks this live-register contract, even though its ordinary XYZ formula
agrees. That form is a negative control only, not production.

Restoring the leaf is necessary for the new parent C to receive initialized
point outputs. This is **retained assembly, not a C conversion or new C
byte-exact count gain**. The trampoline and continuation remain unchanged.

## Qualification

All **53 focused tests pass in 193.127 seconds, no skips**.
The complete actor, viewport, resource, matching and object/data-tool corpus
passes **355 tests in 829.704 seconds, no skips**. `make tools-check` passes.
Tracked and staged whitespace checks pass; all **2965** checked relative
links resolve across ten current/working-note/README documents. No test was
removed, skipped or restarted to bypass the longer compiler/filesystem run.

- **1715 completed three-way guest cases**: 1675 standalone cases and 40
  actual coordinate-phase/full-transform/matrix connections. Standalone cases
  cover all 256 ID bytes, joints 0/1/7, both O32 stack phases, unsigned interval
  edges, ordered early returns, weight boundaries, callback mutations,
  degenerate geometry, signed coordinates, output aliases, rounding and sparse
  high-joint rows. Compare complete external memory, ordered external writes
  and normalized seven-argument call logs; ordinary nonvolatile read scheduling
  is not required to match between compiler forms.
- **300 / 302 retail target words executed**. Duplicate `mtc1` words at
  `0x1502F7AC` and `0x1502F804` are unreachable through the normal function CFG:
  zero branches execute their preceding delay-slot transfer and land after the
  duplicate; nonzero paths branch around it. Do not report 302 executed words.
- **53 / 53 matrix-leaf/continuation words covered**, with the real five-word
  trampoline also executed in dedicated tail cases. Tail checks explicitly
  verify A0/T9/F0/F2/F4, as well as normal nonvolatile register lifetimes.
- **57344 native independent-reference cases**, plus **33 alias cases**.
  The freestanding 32-bit strict-warning fixture compares whole actor and
  vertex/matrix/table state, raw coordinate bits and callback logs. Native
  pointers remain within fixture objects; joints are 0..7. The explicit
  all-output-alias case produces 61.0f.
- Five incorrect semantic controls are rejected: inclusive range end, stale
  source base, extra sum-of-weights gate, stale old-relative Y, and simplified
  final X assignment. The ordinary C matrix control also fails the slot and
  retained tail-register contract.

These are bounded finite arithmetic/address/ABI checks. They do not establish
R4300 FCSR, traps, subnormals or legacy-NaN parity, complete retail asset-domain
safety, PC runtime behavior or gameplay acceptance. An explicit overlapping-
range first-match fixture is a useful additional gate before future loop changes.

## Linked Audit And Counts

Across **6060 function slots**, only `func_1502F490` and `func_150A7960`
change. No symbol, address or slot length is added, removed or moved.
The exact 50-word phase caller remains unchanged despite its type cast.
The exact copy, dispatcher, display scan and selector remain unchanged.
`func_1502BEE4` remains independently non-matching at **109 words**.

| Function | Linked SHA-256 |
| --- | --- |
| `func_1502F490` | `192c1a8d65837723d3ff99e977e1c75a7a5c328f237769e768060224c3f5f77e` |
| `func_150A7960` | `30f70048d0ec3e01c57fb1236ca47321995a732b3d00e54c45919cbf449a32c9` |
| `func_1502F3C8` | `7670792f2767a44c1bd1f768d17ac4fda43fb43c49125f8cf7787e10d7fa7c0d` |
| `func_1502F948` | `6453250c820339049c21dc029171201bae554c734b61fdbe8d89d4f9a096aaf6` |
| `func_1502BEE4` | `c32708201e59edf73b9986867a0afa76d7a8da115d8a38d0f703cbaa85422758` |

Complete Init code **164048 bytes**, Init data/rodata **17376 bytes**,
Debugger **19800 bytes**, and Game data **189088 bytes / 720 owners** remain
retail-exact. The patch CSV is unchanged: **10622 unique rows**, SHA-256
`b805f4aada0d4273b2af4ba67424da07de5bfc41e766449f29893b4b63bf011b`.

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3304 / 5462 (60.49%) | 0 | 2158 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2631 / 4789 (54.94%) | 0 | 2158 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion is **5462 / 6042 (90.40%)**, 1930764 / 2256728 bytes (85.56%).
Game is **4789 / 5321 (90.00%)**, 1759328 / 2072880 bytes (84.87%).
The denominators fall by one because the false C matrix placeholder is now
assembly. Exact C numerators do not increase. The 47 retained Init ASM routines
remain unchanged. README changes only aggregate measurements; detailed updates
stay in these docs. No sibling source/build/save/frozen Release change, host
transplant or push is made.

## Reproduction And Matching Handoff

```powershell
wsl python3 -m tools.experiments.game_actor_triangle_transform_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_triangle_transform_match tools.tests.test_game_actor_buffer_copy_match tools.tests.test_game_actor_attachment_phase_match tools.tests.test_game_actor_update_pass_match tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

Next: continue **`func_1502F490` byte matching**, not another placeholder batch.

1. Recover frame 0x138 and original private-array homes. Retail vertices are
   SP+0xF4, matrix indexes SP+0x114, six points SP+0xAC (72 bytes), edge A
   SP+0x94, edge B SP+0x7C, blend SP+0x120, relative SP+0x12C. Current selected
   homes are vertices +0x154, indexes +0x148, points +0x100, edges +0xE8/+0xD0,
   blend +0xB8 and relative +0xC4. Gaps alone do not prove larger retail arrays.
2. Recover inner SDK-loop lifetimes: retail keeps output XYZ pointers in
   S0/S4/S5, increments byte cursor S3 by 12 and stops at S7=36. Current C
   recomputes Y/Z pointers and uses a matrix-end condition. Screen coherent
   declaration/scope/loop shapes, then compare the full instruction schedule.
3. Preserve first-match ranges and fresh second-source semantics. Add explicit
   overlap controls when changing the range loop. Keep all complete-transform,
   phase and retained-tail checks, including ordered aliased coordinate updates.
4. Only install a genuinely improved fitting candidate after full slot/data
   audit. Do not normalize 275 words with guards or add fake body padding.
   Caller max-depth spill +0x78 versus retail +0x34 remains a separate open match.

The Game goal remains active with **2158 differing C functions**.

Post-checkpoint array/output-cursor controls are banked in
[Note 1013](1013-game-actor-triangle-layout-screen-20261005.md).
None improves this installed frame/difference baseline; production is unchanged.
