# Game Matrix Decomposer Guarded C Conversion

Date: 2026-10-11. Recover complete func_1503E5F8 in
conker/src/game/generated_6B320.c, replacing its last GLOBAL_ASM reference.
VA 0x1503E5F8..0x1503E82C, ROM 0x6BAA8..0x6BCDC: 141 words / 564 bytes.
Semantic C emits 141 words with frame 0xC0 and no constant pool. Seventy-eight
words match directly; 63 relocation-aware expected-word guards restore retail
allocation and scheduling. This is not a direct C match. No word insertion,
omission, recipe/profile/shared-header/caller change or raw-instruction C body.
Original assembly remains untouched. The existing standard-generated recipe
automatically replaces GLOBAL_ASM processing when this owner loses its last
pragma. Entire installed ELF is identical to the pre-conversion baseline.

## Baseline And Contract

Consumer 11706d9f36c011725497cbe6613e06b2e98597c5 and mounted tools
dbc0f0d69a8443f0c93dc4a4f07fcb68c7fc4e69 were clean at entry.
[Note 1287](1287-game-matrix-forward-direct-match-20261011.md) left this
already linked-exact assembly body, excluded from the C-converted census.
Use the established workflow: scoped retail/caller audit, bounded source
screen, independent semantic and linked qualification, tools-first commit,
then consumer source/docs/gitlink. Codex is the sole writer; zero Claude calls.
Reuse existing IDO, structured ELF/object/pool parsers, MIPS/native32 harnesses
and both production padders. Do not add another broad conversion batch.

Recover a void ten-pointer matrix decomposer with nine position/rotation/scale
outputs. Copy all 64 matrix bytes before writing outputs. Export row-three
XYZ, then compute each of three row-vector lengths, substitute the cached
fallback only for zero, store scale and normalize that copied row. Cross rows
one/two and dot row zero; negative handedness negates the live scales in order
and copied XYZ vectors, preserving the fourth elements. Compute pitch from
asin(-matrix[0][2]); nonzero cosine selects two atan calls, zero selects the
gimbal branch with one atan call and zero Z angle. Multiply final angles by
the cached radians-to-degrees factor. Trig routines are retail approximation
helpers, not interchangeable host-libm implementations.

Initial position pointers are cached before bcopy. Scale pointers reload from
incoming homes after bcopy, then stay cached across vector calls. Angle pointers
reload late, after trig. Fallback D_80098918 loads once after position stores;
factor D_8009891C loads once after angle calls, before all final stores. Their
actual bits are 0x38D1B717 (approximately 0.0001) and 0x42652EE0 (57.295776).
Repeated output pointers and aliases to these globals must preserve ordered
stores and single-load lifetimes; duplicate scale negations can cancel.

The mixed O32 vector-scale ABI uses source pointer in A0, scalar bits in A1,
destination pointer in A2. Four actual vector bodies are connected: cross19,
dot12, length11 including sqrt.s in the return delay slot, and scale13.
No external sqrt call. Preserve original 0xC0 frame, S0..S6 and F20/F22/F24
saved-pair lifetimes and unreachable duplicate SZ store at target +0xCC.
All 140 reachable target words execute in qualification; +0xCC never executes.

## Source Screen And Guards

Straightforward source emits 139 words/frame 0xB0/138 differences. Adding the
middle-row anchor gives 141/frame 0xB8/81 differences. A natural four-float
cross workspace and separate final factor recover frame 0xC0. The selected
clear named-argument source emits 141/frame 0xC0/63 differences under existing
O2/g3. Compact no-unroll produces the same result; O1/g3 and O1 produce
180/frame 0x88/178 differences. A parameter-reuse variant reaches 61 but was
not selected. An explicitly scoped negative-loop limit reaches 42 only under
compact no-unroll; its default output grows to 184/185 words. Flat arrays,
member workspaces, Row structs, register parameters and scope/anchor variants
do not yield a qualified direct match. The search is bounded, not exhaustive.

Sixty-three fixed expected-word guards cover the closed register-allocation
cycle, prologue/save schedule, address reuse, negative-loop endpoint schedule
and final-store T-register cycle. They are not 63 independent scheduling
swaps. Relocations move with their words and validate original relocations.
The original guard manifest is a literal preserved byte prefix plus these
63 rows. No stale baseline/guard regeneration, dummy volatile padding,
fabricated condition, instruction drop/insertion or broad profile change.
Add only two local float globals and seven required typed helper declarations.

## Fresh Qualification

Nine pre-install tests pass in 14.054 seconds. Nine final installed tests pass
in 26.261 seconds. Final two literal-integrity/corruption-control gates pass
again after documentation in 1.846 seconds. All 4,417 relative links across
seven edited documentation files resolve; diff --check passes.
Receipts: conker/build/game-matrix-decompose-match-test/.

- 288 retail/raw/guarded cases: six matrices, six output-alias layouts, two
  stack phases, two controlled cosine results and two controlled pitches.
  Raw public memory/calls agree with the semantic reference; guarded complete
  memory/events/GPR/FPR agree with retail. Four vector helpers execute actual
  MIPS, with bcopy and trig remaining bounded controlled leaves.
- Twenty-six callback-lifetime cases cover post-copy scale homes, cached
  initial position/scale pointers, late angle homes, fallback/factor mutation,
  live copied-vector changes and handedness rereads. Required mutations are
  effective; changes to already-cached homes do not retarget those outputs.
  Private/incoming-home aliases are guest evidence, not portable C claims.
- Two independent links rebase ten symbols with HI16/LO16 carries in 72
  cases. All 1,350 fired fault pairs preserve complete retail/guarded state.
  Raw private-access/fault order is not claimed. A stale expected-word guard
  fails effectively. No hardware/FCSR or portable C fault claim.
- Six freshly compiled semantic controls fail: wrong fallback, handedness,
  pitch sign, gimbal gate, live coefficient reload and position row. Negative
  source is compiled independently without reusing positive guards.
- Both complete owner objects are diagnostic-free, pass GLOBAL_ASM processing
  and both actual production padders. All 21 neighbors, extents, relocations
  and normalized pools remain identical; both padded full objects are equal.
- Native32 O2/O0 each pass 432 cases using actual recovered C and vector math
  with SSE sqrt. Check all matrix rows, input/output canaries, alias layouts,
  fallback/factor mutation and ordered call protocol. Five native controls
  fail effectively. Trig remains controlled, not actual retail trig proof.
- Seventy-two cases execute the actual wrapper40, SDK conversion45/copy11,
  decomposer141 and four vector bodies. Remove the prior decomposer projection
  hook. The inner bcopy/trig hooks remain; this is not full gameplay/FCSR proof.
- Literal source/entire-ELF/extent/guard-prefix/progress/six-other-input
  gates pass. Corruption controls reject source, three ELF locations, guard
  prefix, duplicate guard and stale source without production mutation or
  frozen-baseline refresh.

Fixture issues corrected before acceptance include an invalid unused scoped
candidate, PowerShell's dropped empty --filter argument (use --filter=), and
an unused fallback in a native negative under -Werror. No production workaround.
The first PowerShell guard-promotion command failed to parse before writing;
its following source-only build was not accepted. Promote the qualified CSV
only after confirming the old manifest hash, preserving original line endings.

The subsequent dependency-wide rebuild exited zero but the literal ELF test
found 177 changed target bytes / 63 raw words, with no differences elsewhere.
A targeted -W src/game/generated_6B320.c rebuild through the unchanged normal
recipe applied the current guards and relinked; the next full installed suite
passed, with the entire ELF identical. Root cause of the earlier stale/raw
object is not proven; do not explain it as a confirmed timestamp/race issue.
The full rebuild also emitted existing unrelated CFE warnings and the known
duplicate generated_12D630 recipe warning; the target owner is diagnostic-free.

~~~sh
python3 -m tools.experiments.game_matrix_decompose_candidates --profiles
python3 -m unittest tools.tests.test_game_matrix_decompose_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker -j4 -W src/game/generated_6B320.c build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit And Progress

The entire ELF, including all code/data, metadata, function extents, section
headers and symbol/string tables, is identical to the baseline. Target extent
remains 564 bytes. Six other inputs stay identical: rodata assembly,
symbol definitions, undefined functions, retail layout, Makefile, original
ASM. Frozen baseline copies also stay identical. Generated progress CSV changes
only this
target's asm-to-c cell; the CSV remains an ignored build artifact, not a new
tracked file. Protected data: 189,088 bytes / 720 owners, zero differences,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | 48adc4b96517a4d4efe101817e092d6b343dbfa5aa462d2d639ddd85c17960c5 |
| Source after | 7d067bf47db4b3b766e880090fdfa6da9d1434f1f4ceebb9be269ae166f7f567 |
| ELF before/after | 4b4bece866646b9f453b958c1dccdd2f37e31f65dc2abaaa810b71f72a5d4071 |
| Guards before | 92f39fbf0bf509614ecff961e3a654e01d30c98666c3c65f224884f57102206e |
| Guards after | 0c28956baf37afeaa5129ad33cb532639375cfbee4fa8a8a6d479d8220adaf52 |

Fresh matching: Game 2,809/4,823 (58.24%), total 3,482/5,496 (63.36%),
Init 492/492 and Debugger 181/181. Zero drift / 2,014 still different.
Matching and converted functions each increase by one; converted bytes
increase by 564. Converted: total 5,496/6,044 (90.93%), 1,941,624/2,256,728
bytes (86.04%); Game 4,823/5,323 (90.61%), 1,770,188/2,072,880 bytes (85.40%).
Root README gets aggregates only, with detailed narrative here and indexes.

## Checkpoint And Next Body

Consumer, mounted and older shared tool checks and native py_compile pass.
Bank mounted tools 6bee2750e1d77b102ad376f69b81acab8b5fcb8c first, then
consumer source/guards/docs/exact gitlink; no
push. Older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all
67 prior hashes stay unchanged. Copy only two absent files with identical
hashes; dirty count 344 -> 346, final snapshot 69 hashes. Do not commit/reset
independent older history. Run target tests from the consumer, not the mirror.
Prior unchanged neighbor suites are reused from Notes 1287..1278 on literal
unchanged evidence, not reported as fresh runs.

Native graphify update . exits one on protective shrink refusal: 18,230
candidate nodes versus 40,009 saved. Preserve 19,398 nodes from 2,972
excluded but still existing files; no force/purge/install. Version and
empty-source warnings remain separate from compiler diagnostics.
Require the post-consumer-commit Graphify hook's fresh terminal Rebuilt receipt,
advanced log bytes/UTC and zero native workers. Launch alone is not completion;
do not force protective shrink, purge, install or modify accounts.

All 22 generated_6B320 functions are now C and their complete retail slots
match with existing guards. No GLOBAL_ASM/zero-return placeholders remain in
that owner. The adjacent generated_6C960 has four already exact functions.
Live scan of generated_6E770 finds six still-different functions, including
func_150412C0: 79 words / 78 differences, VA 0x150412C0..0x150413FC,
ROM 0x6E770..0x6E8AC. It is a genuine zero-return placeholder for a twelve-
command display-list setup leaf that returns its advanced Gfx pointer.
Next recover its SDK graphics macro contract, texture source D_80084930,
ordered stores and caller ABI; preserve the two already exact neighbors.
The graph resolved the neighboring cleanup symbol, but current retail/source
and literal slot scans are authoritative for this next target.

Existing guard removal (including these 63 words), actual copy/trig/hardware/
FCSR/renderer/gameplay acceptance and the full Game matching goal remain open.
No OGL Release/build/change, private input/save or editor/debugger mutation.
