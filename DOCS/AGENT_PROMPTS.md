# Agent Handoff Templates

Use with [the workflow](AGENT_WORKFLOW.md). Replace bracketed fields and put
transient packets/answers in the existing ignored target build directory.

## Codex Task

```text
Objective / acceptance criteria: [one measurable function or behavior]
Repository / target / ROM version / profile: [identities]
Scope / excluded pre-existing edits: [paths and boundaries]
Baseline: [working note, HEADs, file/input fingerprints]
Evidence: [complete assembly, caller, code, bounded logs]
Open questions: [specific unknowns]
Claude budget: [0 routine; 1 justified analysis; at most 2 for distinct risk]

Resume from live scoped state. Investigate, implement and validate as the
single writer. Reuse project parsers/oracles/helpers. Separate facts from
hypotheses. Run focused gates and a linked audit; broaden regression tests
when the measured change affects shared behavior. Preserve dirty work,
private inputs, pins and frozen Release. Do not commit/push unless requested.
Return changes, exact locations, fresh tests, reused receipts, measured
progress, remaining limits and next target. Do not claim runtime parity.
```

## Claude Analysis

```text
Read-only, packet-only analysis: no tools, edits, commands, builds, tests,
Git mutations, installs, other agents or exploration outside this packet.
Decision needed: [one precise uncertainty and expected value of review]
Target / version / profile / baseline / packet SHA-256: [identities]
Functions / VA / ROM / paths: [locations]
Observed facts / reproduction: [bounded evidence]
Complete relevant code / assembly / definitions: [excerpts]
Checks already performed, including contradictions: [results]
Questions: [up to three tightly related questions]

Derive an independent interpretation before considering any preferred
explanation. Check sign/width, pointers, endian, ABI, ownership and ordering.
In 500-800 words or fewer, give conclusion/confidence/evidence, concrete
defects or labeled hypotheses, the smallest discriminating test, and any
minimal supported correction. Name missing context. No generic cleanup.
```

## Claude Diff Review

```text
Read-only, packet-only review. Do not edit, execute tools/tests, change Git
state or invoke other agents. Review only this task's actual change.
Objective / acceptance criteria: [required result]
Target / baseline / reviewed revision + fingerprint: [identities]
Scope / pre-existing changes excluded: [paths]
Task-only diff and relevant new files: [complete excerpts]
Necessary surrounding code / original assembly: [excerpts]
Fresh validation / reused prior evidence: [distinct receipts]
Unvalidated behavior / concrete regression concern: [limits]

Prioritize correctness, ABI/layout, lifetime/bounds, endian/sign, matching
regressions and acceptance violations. In fewer than 700 words, report each
actionable finding with severity, exact location, trigger, failure mechanism
and smallest correction or confirming test. Label uncertainty. If none,
say no actionable findings and name material limitations. Do not claim you
ran tests or infer runtime parity from a clean review.
```

## Codex Reconciliation

```text
Objective / acceptance criteria: [original task]
Reviewed packet / revision / fingerprint: [identity]
Changes since review: [none or exact differences]
Claude response: [answer]
Remaining call budget: [number]

Verify packet currency and each finding against live source, original
assembly and measured evidence. Mark accepted/rejected/unresolved with exact
support. Implement only supported scoped corrections; preserve unrelated
work and artifact policies. Run focused checks and audit the task-only diff.
Do not request another review automatically. Return finding dispositions,
changes, fresh and reused validation, uncertainty and actual call count.
```
