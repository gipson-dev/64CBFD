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
shortcut. No automated helper is installed: authentication/billing route,
packet-only enforcement, output capture and timeout behavior have **not**
been live-tested. Do not claim an enforced integration or invoke it until
those boundaries are verified. No permission-bypass switches or MCP bridge.

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
the invocation. Current setup uses **zero Claude calls**. Keep commits and
tools-pin publication as a separate, explicitly requested action.
