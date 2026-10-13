# Codex And Claude Decomp Workflow

Verified locally: 2026-10-08. Policy is durable; versions and receipts are a
dated observation. This adopts the supplied offline workflow for the retail
decomp, without installing a bridge or changing account settings.

## Ownership And Safety

Codex investigates, edits, compiles, tests, audits, reconciles reviews and
reports results. Only one agent writes to a checkout. Claude's default role
is a bounded, packet-only second opinion: no repository tools, edits,
builds, tests, installs, Git mutations or agent loops. A prose instruction is
not an enforced permission boundary; manual packet review is a documented
process, not a filesystem sandbox. Codex independently verifies every finding.

The workspace parent is not the decomp Git root. `64CBFD` owns source,
retail assembly, layout/guard manifests and notes. `64CBFD/tools` and sibling
`64CBFD Tools` are separate checkouts of `gipson-dev/64CBFD-Tools`; see
[tools ownership](TOOLS_REPOSITORY.md). Record each relevant HEAD, scoped
status and task-file fingerprint before changes. Preserve dirty work, ignored
reference inputs, probes, real saves, active editor state and existing pins.
No automatic stash, reset, clean, branch switch, commit, push or dependency
update. A new worktree does not contain existing uncommitted edits.

`64CBFDOGL` is a separate host port. This decomp workflow does not authorize
host changes. Keep its Release checkpoint frozen; ordinary authorized host
work uses RelWithDebInfo. Fresh explicit authorization is required to build,
modify or launch Release. Retail matching does not prove host/gameplay parity.

## Fast Evidence Loop

1. Resume from [current status](CURRENT_STATUS.md) and the latest target note.
   Record function/VA/ROM span, exact acceptance criteria and the relevant
   source/tools baseline once; inspect live state rather than assuming a
   previous handoff remains current.
2. Query the local Graphify graph when present, then inspect the complete
   retail routine, direct caller interface and actual owner/compiler profile.
   Mark measured facts, hypotheses and unknowns separately. Generated slices
   follow [the contributor guide](CONTRIBUTING.md), not blanket regeneration.
3. Reuse existing candidate, MIPS oracle, native32, relocation and padder
   helpers. Start with the smallest discriminating source/profile experiment;
   compile complete semantic bodies rather than inventing broad abstractions.
4. Run focused qualification before installation: width/sign, ABI, empty and
   boundary cases, aliases/access order, effective negative controls, copied
   owner neighbors, actual padding and independent symbol rebases as needed.
   A test-fixture failure is not automatically a production defect.
5. Install only the qualified body. Rebuild the linked ELF and progress CSV.
   Compare every function's body/address/extent, protected sections, data,
   guard history and conversion rows with the recorded baseline. Measure
   fresh aggregate progress; never infer it solely from the isolated candidate.
6. Scale regression coverage to the measured change. For a direct conversion
   with all linked bodies/data/guards unchanged, run the target suite after
   installation and shared tool checks. Reuse prior unchanged neighbor-suite
   receipts explicitly; do not call them fresh tests. Broaden to affected
   callers/neighbors for semantic/guard/profile changes, and broader suites
   for shared helper/ABI/build changes or any unexpected audit difference.
7. Review the task-only diff, update one detailed working note and concise
   current indexes, refresh Graphify after code changes, and leave a concrete
   next target. Root README gets aggregate rows only. Avoid duplicate long
   narratives in every index. Keep the wider Game goal open.

Do not cut correctness gates to claim speed. Cache/reuse evidence only when
its source/profile/input fingerprints are unchanged. Runtime setup, model
agreement and a passing host build are not exact-match evidence. Guest
fault-prefix tests qualify emitted instruction order, not portable C fault
semantics. Keep complete caller/hardware/gameplay acceptance separate.

## Local Validation Paths

The [2026-10-13 REA setup verification](REVERSE_ENGINEERING_SETUP.md) records
the connected Codex server and the current Windows Ghidra adapter's MIPS ELF
rejection. Provider readiness is not successful MIPS analysis; use the existing
matching tools below and do not repeat setup or install dependencies by default.

Windows PowerShell hosts WSL builds. Run these from the prepared `64CBFD`
root using `wsl --exec` (or directly inside WSL at the same root):

```sh
python3 -m tools.experiments.game_node_group_swap_candidates
python3 -m tools.experiments.game_node_group_swap_candidates --profiles
python3 -m unittest tools.tests.test_game_node_group_swap_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

These use the prepared US big-endian retail input `conker/conker.us.bin`,
IDO 5.3, MIPS GNU binutils and native32 GCC. Candidate/test commands are
verified locally for this target, not a promise for an unprepared clone.
The normal profile is existing O2/g3. Preserve original assembly in
`conker/asm/` and layouts/guards in `conker/`. Ignored
`conker/build/<target>/` holds transient sources, packets and receipts.
Standalone tools checks and required consumer inputs are described in its
[README](https://github.com/gipson-dev/64CBFD-Tools/blob/master/README.md).

Optional text-measurer UOPT diagnostics: [Note 1300](WORKING_NOTES/1300-game-text-measurer-uopt-allocation-trace-20261012.md)
qualifies `python3 -m tools.experiments.game_text_measurer_uopt_trace --mode 6`.
It requires the exact prepared cc/uopt hashes and existing GDB, and operates
only on a newly owned compiler process. Never change/install a compiler to
bypass its fingerprint gate. Debug real-number output is suppressed, so
numeric timings are not valid. Complete driver exit and identical emitted
text/functions/relocations/pools are required before trusting the trace.
Mode5 and its integer forbidden/interference parser are also qualified in
[Note 1301](WORKING_NOTES/1301-game-text-measurer-forbidden-register-constraints-20261012.md).
Use `--mode 5` for those sets, not for suppressed real-number cost/timing fields.

Read-only UGEN load-node diagnostics are qualified in
[Note 1303](WORKING_NOTES/1303-game-text-measurer-ugen-register-node-observation-20261012.md):
`python3 -m tools.experiments.game_text_measurer_ugen_nodes --candidate late`.
The cc/uopt/ugen fingerprints, fired probe, child/driver exit0, cleanup and
normal-object identity gates are mandatory. Zero-event routes without an
effective positive control do not establish absence or matching progress.

Effectful source screens and their limits are banked in
[Note 1304](WORKING_NOTES/1304-game-text-measurer-effectful-predicates-and-upstream-call-save-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_logic_candidates --filter or-effects`.
These are non-installable experiments: public equivalence and219-word/frame
agreement do not replace saved-role/private/fault/owner matching gates.

Completed CFE/UOPT wire captures are qualified in
[Note 1305](WORKING_NOTES/1305-game-text-measurer-frontend-vreg-and-uopt-call-save-provenance-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_frontend_trace` and
`python3 -m tools.experiments.game_text_measurer_logic_candidates --carriers`.
Captures use normal compiler flags and newly owned children; require producer/
consumer completion, actual input paths, fired table probe, hash/marker-order
checks and complete normal-object identity. They remain non-installable.
Do not use failed `-K` or verbose intermediates as qualified receipts.

Carrier layout screens and register-role checks are qualified in
[Note 1306](WORKING_NOTES/1306-game-text-measurer-carrier-layout-and-register-role-qualification-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_logic_candidates --layouts`.
Equal shape/difference counts are not word identity; a T0 spill is not proof
of the font flag's lifetime. Verify complete words, actual call-boundary
state and captured homes before treating either as matching evidence.

Operand-aware wire decoding and source-marker limits are qualified in
[Note 1307](WORKING_NOTES/1307-game-text-measurer-wire-operands-and-source-marker-provenance-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_logic_candidates --compound`.
Raw metadata bytes remain evidence; interpret only descriptor-defined fields.
Do not equate the UOPT variable-table marker with a CFE VREG opcode or infer
a pre-call snapshot from a compound assignment without checking load order.

Font qualifier controls and actual initializer call-save are qualified in
[Note 1308](WORKING_NOTES/1308-game-text-measurer-font-controls-and-initializer-call-save-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_font_controls` under WSL.
These are not recovered volatile declarations: even 219/frame0x80/SP+0x68
still fails seven saved roles and the shared early zero. Equal counts do not
establish instruction identity. Run the repository helper checks under WSL;
native Windows py_compile is a separate syntax check.

Explicit assignment and separated predicate/effect controls are qualified in
[Note 1309](WORKING_NOTES/1309-game-text-measurer-explicit-assignment-and-predicate-boundaries-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_predicate_snapshot --defaults`
or `--assignments` under WSL. A passing space value or zero at the metrics call
does not prove the shared early reset: check the first ordinary text-byte read
as well. Equal counts still require complete word/relocation/pool comparisons;
all six forms remain rejected and no production declarations are changed.

Five-field switches and register-hint provenance are qualified in
[Note 1310](WORKING_NOTES/1310-game-text-measurer-switch-and-register-hint-provenance-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_switch_flags` under WSL.
Literal source-register VREG raw level 0 and anonymous temporary raw level 1
are distinct measured records, not proven equivalents or lexical-depth labels.
Require complete stream comparisons and fired register observations; these
statement forms still keep a saved S4 flag and fail retail's T0 lifetime.

Split default carriers and source-home call-save are qualified in
[Note 1311](WORKING_NOTES/1311-game-text-measurer-shared-zero-and-source-home-call-save-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_default_carrier` under WSL.
The split form recovers a common non-likely delay-slot zero and named M-24 /
SP+0x68 lifetime, but still fails seven saved roles and full 219-word layout.
Keep the static first-access proof separate from full instruction-fault parity;
do not pad or install the 218-word source on these partial results.

Disjoint address/height work and recovered opening roles are qualified in
[Note 1312](WORKING_NOTES/1312-game-text-measurer-address-work-lifetime-and-retail-save-roles-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_work_lifetime` under WSL.
The forward ternary form preserves all seven opening roles, common zero and
named SP+0x68 in frame0x80; 216/171 still fails full matching. Native pointer/
integer reuse is qualified only for the existing 32-bit ABI. Do not promote
the identity-assignment shape control or bypass remaining matching gates.

Repeated real predicates and the renewed instruction boundary are qualified in
[Note 1313](WORKING_NOTES/1313-game-text-measurer-repeated-predicate-and-font-load-fault-boundary-20261012.md).
Use `python3 -m tools.experiments.game_text_measurer_repeated_predicate` under WSL.
The 218/114 form has a literal 53-word metrics match and 710/768 exact named
access-cut states, but the ordinary font-pointer load still rejects it. Cached
predicates must be defined before the space jump too. Keep named-cut evidence
separate from all-input/private/PC/FCSR matching; do not pad or install.

Mode-selected callback dispatch is directly qualified in
[Note 1314](WORKING_NOTES/1314-game-mode-callback-dispatcher-direct-match-20261012.md).
Use `python3 -m tools.experiments.game_mode_callback_dispatch_candidates` under WSL.
Preserve the guarded do/while: invalid modes must not evaluate an uninitialized
selected pointer. Distinguish 152-byte function from its existing eight-byte
alignment tail; audit both literal slot and the expected symbol-size update.
Whole-ELF frozen fixtures advance only after an independent declared-change
image gate, with prior snapshots archived and semantic/corruption checks intact.

The event packet constructor is directly qualified in
[Note 1315](WORKING_NOTES/1315-game-event-record-constructor-direct-match-20261012.md).
Use `python3 -m tools.experiments.game_event_record_constructor_candidates` and
`python3 -m unittest tools.tests.test_game_event_record_constructor_match -v`
under WSL. Retain the raw flag word and its two independent tests. Compare
all20 seeded packet bytes in the guest ABI, but do not fix portable C padding
contents; incoming-home redirects are guest-only probes. The production owner
padder preserves a preexisting overflowing neighbor while the strict full-owner
padder rejects it; both isolated target padders match. Do not weaken or repair
an unrelated neighbor to manufacture a full-owner strict-padder pass.

The record rectangle predicate is directly qualified in
[Note 1316](WORKING_NOTES/1316-game-rectangle-bounds-predicate-direct-match-20261012.md).
Use `python3 -m tools.experiments.game_rectangle_bounds_candidates` and
`python3 -m unittest tools.tests.test_game_rectangle_bounds_match -v` under WSL.
Preserve ordered rejection rather than an inside conjunction; NaNs differ.
Round both signed dimensions to float32 in references, including INT_MAX.
Separate sparse full-word guest indices from valid native array indices, and
the authentic five-word caller store window from the unrecovered full caller.
All44 words match even though public paths visit43; retain the unreachable load.

The one-shot timer and SDK/native32 runtime boundary are qualified in
[Note 1317](WORKING_NOTES/1317-game-one-shot-timer-direct-match-20261012.md).
Use `python3 -m tools.experiments.game_one_shot_timer_candidates --controls`
and `python3 -m unittest tools.tests.test_game_one_shot_timer_match -v` under WSL.
Use the mutable clock expression, not the fixed-clock conversion macro; retain
unsigned64 overflow-before-division and the O32 alignment hole. The prepared
32-bit shared libgcc runtime supplies native division; do not install/rebuild
a compiler/runtime to bypass a missing precondition. Metadata permutations
require exact named-definition equality and closed byte accounting, never a
blanket symbol/string-table exclusion. Opaque providers do not prove interrupts.

The grouped descriptor/actor dispatcher is qualified in
[Note 1318](WORKING_NOTES/1318-game-grouped-actor-dispatch-direct-match-20261012.md).
Use `python3 -m tools.experiments.game_grouped_actor_dispatch_candidates --controls`
and `python3 -m unittest tools.tests.test_game_grouped_actor_dispatch_match -v`.
Read per-owner flags before copied-owner tests: generated_49D30 already disables
unrolling. Actor-first local declaration preserves the real SP+0x1C home.
Separate deliberate guest home overwrites from portable native helper mutations.
The actual caller/lookup/append instructions are connected evidence, not opaque
provider behavior; neither is a claim of full gameplay or hardware acceptance.

The indexed actor-type switch/table is qualified in
[Note 1319](WORKING_NOTES/1319-game-actor-type-dispatch-direct-match-20261012.md).
Use `python3 -m tools.experiments.game_actor_type_dispatch_candidates` and
`python3 -m unittest tools.tests.test_game_actor_type_dispatch_match -v`.
Retain the five-entry compiler table and original data owner via the scoped
RETAIL_RODATA_SYMBOL binding; a merged predicate is not direct-match credit.
Complete GLOBAL_ASM postprocessing in copied-owner tests. Archive and advance
only the exact ELF/two-line Makefile text receipts after literal image proof;
preserve all other text fixtures. The connected original caller does not qualify
its opaque large provider or restore that caller's production placeholder.

The live-mask matrix clear is qualified in
[Note 1320](WORKING_NOTES/1320-game-actor-matrix-clear-byte-match-20261012.md).
Use `python3 -m tools.experiments.game_actor_matrix_clear_candidates` and
`python3 -m unittest tools.tests.test_game_actor_matrix_clear_match -v`.
Keep raw18 differences separate from48-word normalized matching. Guard replacements
derive only a closed post-helper GPR cycle and integer addu operand order; preserve
all opcodes/immediates/relocations. Use actual end-symbol arithmetic for actor scans
(25 records here), and map all alias backing explicitly. The historical whole-CSV
count helper is stale for this manifest; do not weaken it or claim its legacy suites
pass. Pin the exact previous guard bytes and verify only the18 derived appended rows.
Archive/advance text ELF/guard receipts only after literal image/guard proof.

The actor callback's semantic recovery and unresolved frame are qualified in
[Note 1321](WORKING_NOTES/1321-game-actor-callback-dispatch-semantic-recovery-and-frame-boundary-20261012.md).
Use `python3 -m tools.experiments.game_actor_callback_dispatch_candidates` and
`python3 -m unittest tools.tests.test_game_actor_callback_dispatch_recovery -v`.
Keep81/0x28/eight frame differences separate from exact matching. Logical private-
frame rebasing in diagnostics is not binary normalization or hardware parity.
No frame guards are installed. Validate both owners for a typed caller prototype
change. The one permitted advisory's controls are independently rejected; its
switch-scratch inference is unproven. Inspect actual frame allocation next, then
all exact-match gates; no matching credit or README figure churn while totals agree.

That frame task is now directly matched in
[Note 1322](WORKING_NOTES/1322-game-actor-callback-dispatch-direct-match-and-frame-provenance-20261012.md).
Use `python3 -m tools.experiments.game_actor_callback_frame_trace --screens` and
`python3 -m unittest tools.tests.test_game_actor_callback_dispatch_match -v`.
The indexed-address source removes upstream named-local reservation while
retaining all81 original words/frame0x20. Compiler observation needs exact
cc/cfe/uopt/ugen hashes, fired frame watch, completed consumers/driver and normal
object/pool identity. Interpret captured descriptor-defined M records before
naming frame summands. Literal private-address/RAM/fault tests replace the old
affine comparison for this match; historical tests retain their original image
snapshot. Advance immutable text ELF receipts only after the independent literal
eight-byte whole-image gate, with all other protected inputs unchanged.

The actor command-stream writer is guarded-exact in
[Note 1323](WORKING_NOTES/1323-game-actor-command-stream-guarded-match-20261013.md).
Use `python3 -m tools.experiments.game_actor_command_stream_candidates --screens`
and `python3 -m unittest tools.tests.test_game_actor_command_stream_match -v`.
Distinguish raw96/62 from fitted97/frame0. Derive the register cycle, cursor-step
split and crossing-branch relocation from source; require exact expected words,
all guard corruption controls, both full-owner padders and independent rebases.
Preserve signed-byte and selected-record reads after aliased tag stores. Keep
finite signed-conversion/native32 backing and the real five-word caller window
separate from arbitrary FP inputs and full-caller/hardware acceptance. Unexpected
ELF serialization must be diagnosed with exact records, named-definition equality
and closed byte accounting; never exclude whole metadata sections. Advance text
ELF/guard pins only after the literal image and exact guard-prefix append gates.

The complete parent dispatcher is directly exact in
[Note 1324](WORKING_NOTES/1324-game-actor-command-dispatch-direct-match-and-table-layout-20261013.md).
Use `python3 -m tools.experiments.game_actor_command_dispatch_candidates --screens`
and `python3 -m unittest tools.tests.test_game_actor_command_dispatch_match -v`.
Distinguish original119/frame0x28 from the prior frame0x30 screen. First-result
declaration order resolves M-16->M-8/local16->8; require fired compiler captures,
unchanged executable hashes and traced/normal object identity. No frame guards.
Whole-owner pool packing is not isolated-section padding: the neighbor table
starts at148, whereas retail keeps a12-byte float/alignment gap and starts at160.
Translate exactly that neighbor LO16 addend, move the owner's rodata base to the
new parent table, and test original code/table rebases plus GNU HI/LO carries.
Require the entire ELF to equal the prior image with only parent instructions
and its symbol size updated. Advance text ELF/guard/Makefile fingerprints only
after those independent gates; archive the old fixture and preserve other inputs.
Public reachability covers117 words; two original duplicate loads are unreachable,
not omitted. Actual97-word child tests do not qualify opaque remaining providers.

The complete actor command finalizer is semantically recovered, not matched, in
[Note 1325](WORKING_NOTES/1325-game-actor-command-finalizer-semantic-recovery-and-matching-boundary-20261013.md).
Use `python3 -m tools.experiments.game_actor_command_finalizer_candidates` and
`python3 -m unittest tools.tests.test_game_actor_command_finalizer_recovery -v`.
Keep raw395/frame0x40/398 differences separate from retail405/frame0x48.
Full-word selectors, signed versus unsigned byte conversions, unsigned PRNG
modulo and pre-header value reads need effective negatives. Native vectors are
derived from the independently guest-checked reference, with numeric host-endian
halfwords; actor/output overlap is qualified in the guest, not claimed portable.
Provider mutation tests do not emulate the PRNG or hardware. Empty-channel
private witnesses reject literal frame equivalence; do not infer own-access
fault-prefix or saved-role parity from public output agreement. Metadata must
have exact named definitions and closed ordering accounting, never whole-section
exclusions. Advance only the protected text ELF pin after independent image proof.
Finish the same routine's length/homes/frame/scheduling next, with no new guards.

The same finalizer's original extent/frame and bounded live homes are restored in
[Note 1326](WORKING_NOTES/1326-game-actor-command-finalizer-extent-frame-and-home-restoration-20261013.md).
Use `python3 -m tools.experiments.game_actor_command_finalizer_fitting` and
`python3 -m unittest tools.tests.test_game_actor_command_finalizer_fitting -v`.
The accepted sign-0 source is405/frame0x48/342 differences, not exact. Captured
tag indices and explicit tail/sign/bounds shapes are real data/control flow,
not padding or physical-register bindings. A tail-source replacement must be
restricted after its unique store marker; broad text replacement can silently
change the earlier bounce test. Preserve the exhaustive byte sweep.
The unqualified403-word control has the same sampled output and three home reads;
it is a shape control, not an effective functional negative or proof that the
qualifier is necessary.160 incoming-home aliases/50 old-body failures establish
the bounded storage improvement. Compiler observation still needs fired gates,
exact executables, completed owned children and normal-object/pool identity.
Shape comparison ignores register fields and branch displacement for diagnosis
only; never install its output as a binary normalizer. Continue literal allocation/
scheduling/private/fault fitting before credit, with immutable image/data gates.

The next finalizer role milestone is
[Note 1327](WORKING_NOTES/1327-game-actor-command-finalizer-live-temporary-slot-restoration-20261013.md):
`python3 -m tools.experiments.game_actor_command_finalizer_roles` and
`python3 -m unittest tools.tests.test_game_actor_command_finalizer_roles -v`.
Existing declaration ordering restores six caller-live slots and cached-type
promotion reduces342->307 differences,405 words/frame0x48 unchanged. Derive
physical addresses from actual M records plus frame and verify live emitted
saves/loads; declaration predictions alone are insufficient. Old/new locals
both round to48, despite M definitions44/48. Keep80 private slot probes distinct
from actual retail PRNG behavior and160 retained home aliases distinct from
whole private RAM or fault parity. No guards or credit.269 changed ELF bytes
are target-only, with no size/metadata allowance; update the protected text ELF
pin only after literal proof. Continue the same307-difference function.

The finalizer's first literal fault-state boundary is measured in
[Note 1328](WORKING_NOTES/1328-game-actor-command-finalizer-opening-fault-boundary-and-fit-rejections-20261013.md).
Use `python3 -m tools.experiments.game_actor_command_finalizer_flow` and
`python3 -m unittest tools.tests.test_game_actor_command_finalizer_flow -v`.
46 screens offer no accepted fit; preserve production405/frame0x48/307.
At cut5, memory/events/FPRs/RA agree but GPRs already differ; the same selector
load is word9 in retail's branch delay slot and word27 in the source.
Use fired gates and dispatched words, never observer-generated faults or
public-only checks as full private-state proof. Recover the opening schedule
before treating later matching stack slots as whole-state agreement.
Flatten excerpt arrays explicitly in advisory packets: PowerShell can stringify
nested arrays as `System.Object[]`. Verify the actual packet before calling;
discard suggestions when source/assembly was absent. No new guards or credit.

The same finalizer's selector delay-slot and nested-noise fit is
[Note 1329](WORKING_NOTES/1329-game-actor-command-finalizer-selector-delay-slot-and-nested-noise-fit-20261013.md).
Use `python3 -m tools.experiments.game_actor_command_finalizer_opening` and
`python3 -m unittest tools.tests.test_game_actor_command_finalizer_opening -v`.
The combined source retains405/frame0x48/six slots and restores word9 while
reducing307->299 differences. Ordinary first alone is403 words; qualify the
combined incoming-home contract, not the qualifier in isolation. A406-word/
279-difference shape is not an installable match. Cut5 still differs in GPR3/7
and the full-fault equal-state count remains260/2,938; do not infer full parity.
Record a fault's actual dispatch word separately from positions of the literal
retail selector load; rejected controls can fault at a different load entirely.
An advisory cast is redundant and reordering regresses/overflows; local evidence
selects the fit, not advisory causal claims. Continue the same function's roles
under immutable image/data/ABI/private/fault gates before matching credit.

The scalar predicate and sampled cut5 restoration is
[Note 1330](WORKING_NOTES/1330-game-actor-command-finalizer-scalar-predicate-and-cut5-restoration-20261013.md).
Use `python3 -m tools.experiments.game_actor_command_finalizer_scalar` and
`python3 -m unittest tools.tests.test_game_actor_command_finalizer_scalar -v`.
Captured category is a byte0..255, so unsigned predicate views preserve results;
leave later signed numeric locals and full-word selectors intact. Inverted/
merged noise retains405/frame0x48/six slots and improves299->298 differences.
First14 words now agree and sampled cut5 closes;452/2,938 states agree, but
primary cut9 and disabled-primary cut7 still differ. No full fault/hardware credit.
Observe actual rldc operands/code, not a guessed register binding. Source
substitution must exclude declarations: a broad cached-variable rename creates
duplicate/undefined locals. Re-run corrected screens before reusing evidence.
Keep the same function and immutable image/data/ABI/private/fault gates.

Known build warning: duplicate generated_12D630 recipe definitions. Preserve
and report it; do not claim a warning-free full build. Use native
`graphify update .` from `64CBFD` after code edits; its existing local
version/scan warnings are separate from compiler diagnostics.

No emulator or live gameplay was exercised by workflow setup. For future
runtime tasks, verify the exact current executable/configuration and existing
Ares/WSL guest-debug handoff before attaching. Use disposable saves/config;
collect natural behavior evidence, not only process or input receipts.

## Selective Claude Review

| Task | Maximum Calls | Gate |
| --- | ---: | --- |
| Routine matching, discovery, fixture fixes, builds | 0 | Codex can settle it directly |
| Difficult assembly/ABI/lifetime uncertainty | 1 | One explicit unresolved decision |
| Substantial risk | 2 | Analysis and final review must resolve distinct questions |

These are workflow budgets, not subscription quotas. Honor stricter user
limits. Do not spend calls for repeated unchanged evidence or to supervise
routine commands. Before a call, record the exact question, expected value,
allowed scope and packet revision. Aim for 1,500-3,000 context words and
500-800 response words or less; preserve necessary complete code/assembly.
Exclude ROMs, binary dumps, secrets, huge logs and full conversation history.

Use [the four templates](AGENT_PROMPTS.md). Manual handoff always works:
Codex prepares the packet; the user submits it to an existing Claude Code
session with no repo actions; the answer returns to Codex for evidence-based
accept/reject/unresolved disposition. Do not apply suggestions by agreement.
Save packet SHA-256 and answer beside the ignored target receipts. Retry only
for a materially new question within budget, never automatically on quota or
auth failure. Do not switch billing, account, provider or model incidentally.

Local discovery: Claude Code 2.1.218 and Codex CLI 0.147.0 are installed;
their `--version` and `--help` were inspected without a model invocation.
Claude help documents `--print`, `--tools ""`, `--safe-mode`,
`--no-session-persistence`, `--strict-mcp-config` and `--output-format`.
`--bare` explicitly uses API-key/helper auth and is not a subscription
shortcut. No persistent automated helper is installed. Before invocation,
verify the current auth/provider route and effective packet-only capabilities;
do not infer them from a prior version/help receipt. No permission-bypass
switches or MCP bridge.

One bounded live qualification, 2026-10-12: [Note 1299](WORKING_NOTES/1299-game-text-measurer-instruction-fault-boundary-and-review-20261012.md)
records one attempted/completed review through existing claude.ai/firstParty
Pro auth, without API/provider overrides or account/model switches. Safe mode,
disabled built-in tools, strict MCP selection and no persistence produce
effective init tools=[]/mcp_servers=[]; the output records no tool use.
Packet, response and receipt are ignored diagnostics. This proves that one
tool-free call/output capture, not a persistent filesystem sandbox, general
integration or timeout/fallback handling. Reverify routing/capabilities for
future invocations and preserve the per-task call budget.

## Review Record

Store one short record in the target working note, not a growing central log:

```text
Task / decision:
Baseline HEADs + relevant source/profile/input fingerprints:
Claude budget / calls attempted / completed:
Reason to call, or reason zero calls suffice:
Packet path + SHA-256 / answer path:
Findings: accepted / rejected / unresolved, with evidence:
Fresh validation commands / results / elapsed time:
Prior receipts reused, with unchanged-evidence basis:
Unvalidated behavior / next target:
```

Call counts are not token usage. Report tokens/cost only when provided by
the invocation. Routine work still defaults to **zero Claude calls**; the
dated difficult-lifetime exception above used one. Keep commits and
tools-pin publication as a separate, explicitly requested action.
