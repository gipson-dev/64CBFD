# Game translated byte-scale matrix guarded match (2026-11-04)

## Outcome

`func_15158920` now replaces its zero-return placeholder in
`conker/src/game/generated_185560.c` with a typed matrix callback. It matches
all 64 retail words with the original 96-byte frame. Twenty-two checked word
rows normalize one closed compiler-local placement difference: the natural
matrix workspace starts at `sp+0x20`, while retail places the same 64 bytes at
`sp+0x18`. No instructions, calls, or owner words are inserted or omitted.

This is a source, callback-registry, compact/padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not visual matrix, actor placement, rendering,
save, gameplay, or PC-port acceptance.

## Recovered behavior and ABI

The O32 callback takes a fixed-point `Mtx` output pointer and a state pointer,
then returns one. It copies the 4x4 floating identity template `D_8008AE18`
into a private workspace, writes the state's X/Y/Z values from offsets
`+0x48`, `+0x4C`, and `+0x50` into translation row three, and multiplies the
nine 3x3 basis values by the state value at `+0xF8` times `D_800A6070`.
`D_800A6070` has bits `0x3B808081`, the binary32 representation used here for
`1.0f / 255.0f`. The completed matrix is converted by `guMtxF2L` and the
callback reports active with return value one.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x15158920..0x15158A20` |
| Retail ROM range | `0x185DD0..0x185ED0` |
| Owner | `generated_185560`, 36 neighboring functions |
| Body / retail slot | 64 / 64 words |
| Frame | 96 bytes |
| Relocations | 5: identity-template HI/LO, scale HI/LO, and `guMtxF2L` |
| Natural compact normalized SHA-256 | `8ef471c07b23eb554036678689f0104fc172fe6e932c1301fc2444117e78dfdf` |
| Linked retail body SHA-256 | `0e791b1d89b25c4101f93a49bf1e91321f423e4346392474aa79c5a8d916bea0` |

## Callback and binding evidence

The only aligned function pointer is at retail ROM `0x22F8D4`, in callback
registry slot `D_8008AE0C[2]`. There are no direct `jal` callers. The registry
ABI supplies the fixed-matrix output and state pointers and consumes the
integer active result. All five linked bindings resolve to their retail
targets: the two identity-template words, the two scale-coefficient words,
and `guMtxF2L`.

## Guarded-match boundary

The semantic source naturally emits 64 words, frame96, all five correct
relocations, and the retail instruction order. Its 22 positional differences
are only the closed `sp+0x20..sp+0x58` versus `sp+0x18..sp+0x50` matrix-local
cycle. The checked rows require both the natural compiler words and the exact
retail replacements, so source drift, guard-preimage drift, offset drift, or a
different compiler allocation fails closed. The guards do not create a call,
branch, operation, or side effect absent from the compiled C.

## Qualification

The permanent four-test suite establishes:

- 256 guest cases exercise the complete callback and cover all 64 words;
- native 32-bit O0, O2, and O3 each pass 4,096 cases, for 12,288 executions;
- nine independently compiled semantic controls are rejected;
- the callback registry, ABI, all five relocations, 22 checked rows, and all
  36 owner neighbors are fixed;
- the strict 6,052-function image changes only `func_15158920`, preserves all
  function addresses with zero exclusions, and changes no other body; and
- all 189,088 protected Game-data bytes across 720 owners remain exact.

The installed focused suite passes all four tests in 28.976 seconds. The
shared match-progress, generated-PC16, guarded-object, and protected-data suite
passes all 19 tests in 6.001 seconds. Qualification tools were banked first in
tools commit `1eabc81`.

## Production closure

The actual Make rule compiled every padded owner that depends on the shared
guard table, then linked `build/conker.us.elf` successfully. This broad rebuild
is the section-level guard audit: no unrelated guard preimage or owner padding
failed. The installed report confirms `source_installed: true`; the production
owner and full ELF equal the independently qualified artifacts. `make all`
then generated the binary and stopped only at the expected final retail SHA
check. The inherited duplicate `generated_12D630` recipe warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `0700ea1f2f261c354d0e11b7109026a1cd5b4b37361996fb24ad7d0ead24b78a` |
| Qualified / production linked ELF | `e63c1ec663abbde611b8a5d060fa0fe0e699ebb3fc43f8be5501a341d3d6ac3a` |
| Production rebuilt ROM image | `5be541242d089d047b11aeb34e2a503e6b146d779b18f339ddb5d21fa8324210` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `d78cc930f4ff8d14ec18f4b5f3ce4f5676de02292216bbd25f169b680232679f` |
| Guard table | `eb52f915409912b6fd2738b92b12917deed361ba97ff72f2de903e5d57221df4` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |
| Aggregate progress catalogue | `4f170efa6034414c9a2612153aac6ea69468b99f7523dde4a11370f8b07a2c99` |

## Recount

The fresh production ELF reports:

- Total: **4,141 / 5,512 (75.13%)**, zero address drift, 1,371 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,468 / 4,839 (71.67%)**, zero drift, 1,371 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **269 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,651 nodes against the retained 58,441-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained byte-identical with SHA-256
`8dd72cd35dc38b3d7855d43675d03306afb478103bff649f074563b60726c1ba`.
No forced refresh or dependency update was used.

An explicit eleven-path incremental rebuild with `force=False` then produced
58,453 nodes, 112,310 links, and 5,086 communities. Against the saved
pre-change snapshot, 58,438 / 58,441 old node IDs were retained, including all
IDs outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, and each has one uniquely relocated replacement
two lines later. Fifteen IDs were added: those three relocated headings, the
Note 2070 file and its ten indexed headings, and the
`TranslationScaleState15158920` type. The twelve-node and twelve-link net
additions are confined to the owned changes. The explicit-refresh graph
SHA-256 is
`f629a90a86f74b12623bf93d4c16e8ed34c6e1dfa7ee1c216f8beda2b983de42`.
A one-path refresh after recording this receipt retained all 58,453 scoped
node IDs and all 112,310 links with zero loss or replacement.

## Continuation

The seven smaller rows ahead of the ordinary queue remain the documented
handwritten/custom-ABI/boundary cases: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue with ordinary Game candidate `func_1515AA84`, then
`func_1515BE50`. Every candidate still requires source/ABI/caller, owner,
guest/native, actual Make, complete-image, protected-data, production recount,
documentation, and graph-retention gates before credit.
