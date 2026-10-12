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
