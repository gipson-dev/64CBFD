# 1746 - Matrix-bound point interpolation direct C match

Verified: 2026-10-27. Target `func_1519E304`, owner `generated_1CA420`.
VA `1519E304..1519E3BC`; retail ROM `1CB7B4..1CB86C`.

## Result and recovered behavior

Replace the zero-return placeholder with the complete 46-word /184-byte routine.
The ordinary O2/g3 profile emits every word directly: zero new guards, frame
0x28 and one R_MIPS_26 call binding at byte +76 to `func_15143134`.
The complete owner preserves all 22 neighboring functions and its pools.

`MatrixPointBinding` describes only the measured owner pointer at +0, unsigned
matrix index at +5 and three-float point at +8. Read the owner's matrix-table
pointer at +0x1D4. A missing table returns zero without reading the index, point,
output or stack float arguments. Otherwise select the indexed 64-byte matrix,
transform the bound point with `func_15143134`, and write each coordinate as
`(transformed - origin) * amount + origin`, then return one.

The early failure return recovers retail's branch orientation and duplicate
index-load word. A pointer to 64-byte arrays recovers the original ADDU operand
order naturally; a byte-pointer/shift variant misses that operand order. The
rejected positive-if and address-shape experiments remain in the ignored stage.
Shared headers, compiler flags and other bodies are unchanged. Existing duplicate
`structs.h` includes in this owner remain untouched.

## Six-argument O32 interface and callers

The recovered interface is `s32(MatrixPointBinding *, f32 *, f32, f32, f32, f32)`.
Binding and output enter in A0/A1; X/Y bits enter in A2/A3, while Z and amount
are at incoming SP+16/+20. Positive execution saves X/Y in incoming homes +8/+12;
binding/output occupy +0/+4. The transformed local vector is incoming SP-12..-4.
The helper may clobber caller-saved registers. Preserve the post-call output and
float-argument reloads and sequential transformed-coordinate reads after stores.
Private stack/home overlap is qualified at the guest-machine boundary.

The aligned retail census finds exactly three JALs and no matching pointer
literal: `1519D190` (ROM `1CA640`), `1519D4E8` (`1CA998`), and `1519D560`
(`1CAA10`). Tests execute their authentic windows and return consumers:

- `1519D0C8..1519D1A0` uses a stack binding, stack output, zero origin and amount
  one. Its earlier owner-home seed matches the original `1519D090` store.
- `1519D4B8..1519D4F8` uses S2 binding and S1+0x10 output, zero origin and amount
  one; the original flag-4 skip route is also checked.
- `1519D52C..1519D570` loads the origin from S1+0x10/+0x14/+0x18, amount from
  binding+0x3C, and writes back to S1+0x10; the existing-V0 skip is checked.

The containing callers remain large unrestored placeholders. These bounded
windows establish the six-argument envelopes and branch consumers; they do not
qualify complete callers or award them C-matching credit.

## Qualification

Both tools copies execute all eight fresh canonical methods with zero errors,
failures or skips. The primary takes 3.452s; exact mirror timing is retained in
its receipt. Both `check_project_tools.py` checks pass.

- 976 guest cases cover all 256 matrix-index bytes, signed zero, subnormals,
  infinity and qNaN model inputs, plus separate float32 subtract/multiply/add
  rounding. Complete original/recovered private machine states agree.
- 45 words are reachable through the normal entry. Retail's duplicate load at
  word 15 /byte +60 is unreachable there. All 46 literal words remain exact;
  do not confuse the public coverage count with a missing instruction.
- 80 alias/home cases cover ten output layouts, four helper mutation modes and
  two stack phases. Sparse null-table cases need neither point/index/output
  storage nor stack floats. Private frame/home aliases are guest-only evidence.
- Native32 O0/O2/O3 each pass 620 vectors, three output alias choices, typed
  six-argument direct/indirect calls, trapping UBSan and eight effective negative
  controls. Finite/signed-zero outputs are bit-exact; NaNs use classification.
  The native helper is a bounded transform contract, not full helper acceptance.
- 66 access-fault prefixes fire and preserve complete private state and fault
  location. Twenty-four integrations execute both original and retained copies
  of the 98-word point helper, together with the actual original fixed-matrix
  converter, transform and translation routines. Float/fixed and zero-point
  routes are covered with bounded values and expected output/status checks.
- 60 original caller-window cases cover success, missing tables, both skip
  routes, high unsigned indices and two stack phases.
- Six independent GNU links across three layouts, including another JAL region,
  preserve the one call binding; twelve rebased guest cases agree. Three raw/
  binding negative controls fail closed. Seven full-image corruptions and three
  wrong-input cases are rejected.

The first canonical harness failed because the composed point-helper oracle
lacked the timing oracle in its inheritance chain. The corrected
`InterpolationOracle(PointOracle, TimingOracle)` supplies one consistent MRO.
The candidate C and prepared artifacts did not change. Failed v1 receipts remain
in `failed-canonical-v1/`; both accepted executions are v2.

The actual three-command owner Make recipe reproduces all 23 compact functions
and the full padded object. Production passes, retaining only the inherited
`generated_12D630` duplicate-recipe warning. Each tools copy then runs two fresh
installed owner/image methods and reuses six semantic methods only after module,
frozen-input, prepared-artifact and sealed-input fingerprints agree. Unchanged
broad suites are retained evidence, not fresh executions. No emulator, R4300
hardware, FCSR, rendering or gameplay acceptance is claimed.

## Production image and actual recount

The entire production ELF equals the independent predecessor prediction: exactly
141 target code bytes and one target symbol-size byte change, 142 total, with
zero exclusions or serialization allowance. All 6,056 function addresses and
6,055 other bodies remain fixed. Protected Game data remains exact across
720 owners /189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

All 113 focused inputs and 16,157 sealed Native/cache files are checked with
four declared source/object/ELF/map adoption paths. Conversion inventory and
guard-manifest bytes are unchanged. No guard rows are added by this recovery.

The captured, adopted Native ELF recount is 3,823/5,506 exact (69.43%):
Game 3,150/4,833 (65.18%), Init 492/492 and Debugger 181/181. Zero address drift;
1,683 C functions still differ. The 75% threshold remains 4,130 exact functions,
307 more. Remaining triage is 1,554 placeholders, 120 semantic/other and nine
unlocated entries; source-shape screening alone earns no matching credit.

## Checkpoint and reproducibility

Baseline consumer `b1a2cfae1f53ae526ae49389c62f830aa378319c`; tools
`3d000d5fe836ae8fcf10706a8a408db021b9f46a`. Tools are committed first in
`e1008a10162e36b51f34e1feca4d6a778026d1f8` and then pinned by the consumer.
Preserve the older mirror's 1,702 inherited dirty paths plus this target's two
new files. Do not reset it or duplicate its history. Nothing is pushed.

- Snapshot SHA: `bebc1127c05478cf77dc67dd9616bebfdda8b8603a246d810966fb72d91d955a`.
- Raw body SHA: `d3f708ca17f13cefc7214b251ba71b56b9cc335e29197ece8a3898a4bcd6d6bf`.
- Padded object SHA: `b93fd0dc7c1a65d5c3f5bbe0b68cb43e3c6428bf93ab68e51245c90b12be4a38`.
- Adopted ELF SHA: `16290cc7896c19c51ea6cc4473833d79af91be2764388a52c8cd37906b8988b5`.
- Reproduce: `python3 -m unittest tools.tests.test_game_matrix_point_interpolation_match -v`
  from the prepared consumer/cache. Ignored evidence is retained in
  `conker/build/game-matrix-point-interpolation-match/` with fresh PID-specific
  execution directories.

Codex owns implementation and validation; routine Claude budget is zero calls.
Refresh changed-source Graphify with checked node/relationship retention and no
full-corpus extraction claim. The 75% goal remains active. Next screened
placeholder `func_1514E920` in `generated_179F30` (47 words) needs its own full gates.
