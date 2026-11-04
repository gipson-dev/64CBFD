# Game active-view matrix callback direct match (2026-11-04)

## Outcome

`func_150F9AB0` now replaces its zero-return placeholder in
`conker/src/game/generated_126F60.c` with the typed active-view matrix
callback. Its complete 64-word / 256-byte retail body emits directly from C
with the original 120-byte frame and nine relocation words. No word guards,
instruction insertions, omissions, alignment changes, compiler-profile
changes, or inventory changes are required.

This is a source, callback ABI/dispatcher, raw and padded owner,
guest/native execution, strict whole-image, protected-data, production-build,
recount, and graph-retention result. It is not visual, RDP output, scene,
save-state, or gameplay acceptance.

## Recovered behavior and ABI

The shared callback dispatcher supplies a display-list cursor, six binary32
values, and one context pointer. This callback intentionally ignores the first
three floats and context. It forwards the final three floats to
`func_15110360`, which builds a 4x4 matrix for the active view index. It then
selects the active 0x180-byte view record and truncates its left, top,
`right - 1.0f`, and bottom bounds for a black `func_15110544` fill.

Three SDK graphics macros append a pipe sync, raw other-mode pair
`0x002C0F / 0x0F0A4004`, and raw combine pair
`0x00357E6A / 0xFFFFFFFF`. The callback passes the resulting cursor and matrix
to handwritten renderer `func_150FB4C0` and returns that renderer's updated
`Gfx *` cursor.

The dispatcher passes eight callback arguments even though several callback
family members consume fewer. The installed signature represents all eight.
A seven-argument typed form and a `void` form happened to emit the same words,
but the `void` form would expose the final callee's surviving `v0` only by
accident. The retained dispatcher immediately reuses callback `v0` as its next
display-list cursor, and handwritten `func_150FB4C0` explicitly returns that
cursor, so the typed `Gfx *` result is the supported ABI.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x150F9AB0..0x150F9BB0` |
| Retail ROM range | `0x126F60..0x127060` |
| Owner | `generated_126F60`, 18 compact functions |
| Frame | 120 bytes |
| Relocations | 9: active-view index/base and three helper calls |
| Natural object body SHA-256 | `3e54faf09ba7dd2d8b56b6298561124c576c92b1c8dbb0b7494cc6c4944baac2` |
| Linked retail body SHA-256 | `3d737b9109021619780f4c531185db540abfaf7e7c36724ab7f684ca6f056eef` |

## Registry and dispatcher evidence

The retail ROM has no aligned direct `jal` to `func_150F9AB0`. Its sole
aligned address literal is ROM `0x22DC9C`, callback-table slot
`D_800891D8[1]`. Retained assembly `func_1510FEA0` selects this table from the
live category byte and performs the indirect call at `0x1511027C`.

The original 17-word dispatcher window was executed across 512 cases and two
stack phases. It passed the cursor, all six float words, and context pointer
exactly, selected table slot one, and copied the callback result back into
`a0` for the following display-list work. The dispatcher remains a current C
placeholder and receives no recovery credit here.

## Qualification

The candidate screen established that direct raw `Gfx` word stores retain the
correct 64-word length but differ in 25 frame/scheduling words. The recovered
SDK `gDPPipeSync`, `gDPSetOtherMode`, and `gDPSetCombine` macro shape naturally
emits all 64 retail words. Both the seven- and eight-argument typed forms are
byte-exact; the eight-argument form is installed because it represents the
observed dispatcher ABI.

The permanent five-test suite establishes:

- all 64 guest instructions execute across 1,024 cases and two stack phases,
  all four view indices, signed fractional bounds, varied unused arguments and
  rotations, all six command words, 64 forwarded matrix bytes, helper return
  cursors, and legal volatile GPR/FPR plus outgoing-home clobbers;
- 512 executions of the original table-dispatch window observe all eight
  callback arguments and the returned-cursor handoff;
- native 32-bit O0, O2, and O3 each pass 4,096 cases, for 12,288 executions,
  with undefined-behavior trapping and valid view/matrix/command backing;
- seventeen independently compiled semantic controls are rejected, covering
  all rotations, both active-view uses, four bounds, right-edge subtraction,
  all three SDK commands, renderer cursor/matrix forwarding, and return value;
- all 256 raw-byte mutations and all nine relocation-binding controls fail
  closed;
- the seventeen neighboring owner functions and normalized pools remain
  unchanged; and
- the qualified full ELF changes only `func_150F9AB0`, preserves every
  function address, has zero strict-image exclusions, and retains all 189,088
  protected Game data bytes across 720 owners exactly.

The installed five-test suite passes in 29.869 seconds. The shared
match-progress, guarded-object, generated-PC16, and protected-data suite passes
all 19 tests in 4.926 seconds.

## Production closure

The actual Make rule compiled, padded, assembled, and linked
`generated_126F60` from the installed source. The production owner and full
ELF equal the independently qualified artifacts. `make -C conker all -j2`
generated the ROM and stopped only at the expected final retail-ROM SHA check;
there was no compile, padding, assembly, link, or image-generation failure.
The inherited duplicate `generated_12D630` recipe warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `9aa0913de4adf8714b795f6f3fe9c4584d4d5fd5470cff73804c4d5cbf6494cf` |
| Qualified / production linked ELF | `4a45dfe2169c9424b9e8c392497ca524e5faea6b4755bcc816d53470165ffb21` |
| Production rebuilt ROM image | `4122d38be5a6f36ebda6757d38e700440ea12850d309253b416f57c147692981` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `b0944fa5233d40c0e81012640d6f08233f23090978b35110798b4aceb9bdeb7c` |
| Guard table | `2c94dfb97dbd6abd4bdab3c379ea92d6131a5a1f70a2d2c04d1608a4d80ab85a` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |
| Aggregate progress catalogue | `4f170efa6034414c9a2612153aac6ea69468b99f7523dde4a11370f8b07a2c99` |

## Recount

The fresh production ELF reports:

- Total: **4,138 / 5,512 (75.07%)**, zero address drift, 1,374 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,465 / 4,839 (71.61%)**, zero drift, 1,374 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **272 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,614 nodes against the retained 58,407-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained byte-identical with SHA-256
`07577bfa6abf4d9cb5d1e9b8c987160df718c02f18fdc4c07c6de9ad718c6e98`.
No forced refresh was used.

An explicit eleven-path incremental rebuild with `force=False` then produced
58,416 nodes, 112,275 links, and 5,087 communities. Against the saved
pre-change snapshot, 58,404 / 58,407 old node IDs were retained, including all
55,995 IDs outside the changed-path set. The three replaced IDs are
line-number-derived `DOCS/UPDATE_LOG.md` headings, and each has one uniquely
relocated replacement two lines later. Twelve IDs were added: those three
relocated headings plus the Note 2067 file node and its eight indexed
headings. The nine-node and eight-link net additions are confined to the new
working note. The explicit-refresh graph SHA-256 is
`34c001491e8c87c6a12918bd1f9b92802c2ba0ca1f1a1281ba865808ae581e67`.

A final note-only refresh retained all 58,416 existing IDs and added only this
section heading and its link, yielding 58,417 nodes, 112,276 links, and 5,078
communities. Historical global analytics are not represented as fresh
full-corpus extraction.

## Continuation

The seven smaller rows ahead of the ordinary queue remain the documented
handwritten/custom-ABI/boundary cases: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue with ordinary Game candidate `func_151218C4`, 67
words with 63 real differences in the fresh production image.
