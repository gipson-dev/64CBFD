# Decomp Agent Instructions

Read [the workflow](DOCS/AGENT_WORKFLOW.md), applicable local `CLAUDE.md`, and
the current function's working note before editing. Use the
[templates](DOCS/AGENT_PROMPTS.md) for bounded analysis and review.

Codex owns implementation and validation. Claude is an optional packet-only
reviewer, not a second writer. Routine work uses zero Claude calls. Preserve
pre-existing edits and private inputs; do not commit or change the tools pin
unless requested. Record exact matching evidence in working notes, keeping
function narratives out of the root README.

`tools/` is an independent repository. Inspect its own instructions and Git
state, and use its existing tests, parsers and domain helpers. A source-only
direct conversion still needs the focused qualification and linked audit
described in the workflow; do not repeat unchanged broad suites by default.
