# Game Text Measurer UGEN Register-Node Observation - 2026-10-12

## Scope

Continue func_150428D4, original219 words/frame0x80, from consumer
6ee9c042d5879ef2abc2bbe3c2ad146fdf753391/tools
c28e130641cb8508110ebbe3349f81294105c557. No new source fit, installation,
guards, profile change or matching credit. Preferred seed remains
flag-branches-captured222/0x80/146, 12 bytes oversized and missing retail's
immediate post-normalizer T0 reset. Latest actual match remains
func_15042C40 in [Note 1292](1292-game-character-normalizer-guarded-match-20261012.md).
The previous eligibility distinction is in [Note 1302](1302-game-text-measurer-vreg-marker-and-memory-residence-20261012.md).

## Positive Observations

The new opt-in tools.experiments.game_text_measurer_ugen_nodes helper observes
f_load_cse at native0x430480 in the exact prepared UGEN. It reads only memory
and registers in newly owned compiler children; no runtime writes, compiler
rebuild, existing debugger attachment or package installation. All raw node
fields remain raw in the receipt instead of assigning guessed meanings.

| Candidate | Words / Frame / Differences | Fired Load-Node Events | Flag Reload And Test Register |
| --- | --- | ---: | --- |
| Early captured reference | 218 / 0x80 / 174 | 90 | S3, architectural19 |
| Late preferred seed | 222 / 0x80 / 146 | 90 | V1, architectural3 |

All observed load nodes have opcode82. Register-class nodes have
type_storage >> 5 == 3 and include raw44 byte offsets76 and12 for those two
architectural registers. Independent emitted-word checks find the SP+0x68
reload and final flag-test register in each body. This is a positive
observation of already assigned register-class load nodes, not a proof of
every pass's provenance or a unique source-variable identity for every node.
It supports returning to UOPT's live-range/assignment boundary rather than
assuming AS1 must choose this flag's register. It does not exhaust backend
or C-source possibilities.

Both complete compiler drivers exit0. Their diagnostic objects match their
own normal compiles in text, function metadata, relocations and the union of
rodata/rdata/data/sdata/literal/bss/sbss pools. Prepared cc/uopt/ugen hashes
remain exact. Debugger exit0 alone is not accepted. The installed marker,
nonempty parsed events, UGEN child exit0, breakpoint removal and driver exit0
must occur in that order. Tests additionally observe removal before AS1 exec.
A recipe review caught and fixed cleanup being outside the child-resume loop;
the final six-test run includes the corrected lifetime gate.

## Inconclusive Routes

The ignored f_spill_to_temp probe observed zero events in both seed222 and a
paired-normalizer-call counterfactual228/frame0x88. Although driver/object
identity gates passed, that counterfactual did not fire the spill probe and
is not an effective positive control. Do not infer the absence of a retail
temporary-spill route from these runs. An ignored broader register-route
probe observed90 load events but zero assign_vreg/check_vreg events per body;
the latter absences likewise do not qualify those probes. Only the positive
load-node observation is promoted to the tracked helper.

Transient exploration remains under
conker/build/game-text-measurer-uopt-investigation-20261012/. Qualified
helper receipts are under conker/build/game-text-measurer-ugen-node-test/.
All diagnostics are explicitly non-installable.

## Verification And Bank

Six focused tests pass in6.870 seconds, no skips. Effective controls reject
failed/incomplete drivers, missing/empty objects, absent/unfired probes,
bad child exits, cleanup outside the child lifetime, debugger errors,
malformed/impossible register nodes, changed text/function metadata/
relocations and each protected pool family, changed compiler fingerprints
and paths/symlinks escaping the ignored build directory. Read-only recipe
and production hashes are checked. Consumer make tools-check, mounted and
older check_project_tools, and Windows py_compile of both new files pass.
Frozen-production/corruption tests05/06 pass in1.823 seconds; all nine frozen
inputs and protected189,088 bytes/720 owners remain exact. Earlier unchanged
full20 public/native/owner/rebase/fault receipts are reused, not rerun or
called fresh. No Claude call or repeated packet review.

Tools7da0ac2ce413146c1a08e292827c243a198067e9 is committed first; consumer
notes, concise indexes and exact gitlink follow. The older standalone
checkout retains HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all82
saved file fingerprints. Exactly two previously absent task files are copied
without overwriting existing files: its dirty count becomes361 from359.
No older history commit/reset or push. Production source/ELF/guards/Makefile,
matching totals and root README remain unchanged. No OGL/Release/ROM/save/
config/editor/existing guest-debugger or prepared compiler-source changes.

Standalone Graphify update terminates with protective exit1: candidate18,363
versus saved40,141 nodes, retaining19,398 excluded-but-existing nodes from
2,972 files. Preserve the existing version/zero-node warnings; no force or
purge. Final reporting still requires the fresh terminal consumer post-commit
Rebuilt receipt, advanced cache-log bytes/UTC, zero native workers and clean
active repos. All4,501 relative links across eight checked documents resolve;
post-documentation immutable/corruption checks pass in1.581 seconds.

## Next

Keep the same target and full Game goal active. Use the qualified mode5
live-range/constraint evidence to discriminate the early flag's call-crossing
lifetime from the late V1 assignment. Any next semantic source experiment
must recover the shared post-normalizer T0 zero, call-only SP+0x68 spill/
early full-word reload and complete219 control flow. Do not repeat the
already rejected storage, conditional/declaration or profile variants, or
promote the zero-event spill probe to evidence. A real fit must pass all
private/fired-fault/native/owner/neighbors/pools/both-padders/independent-
links/rebases/literal whole-ELF/data/guard-prefix gates before installation
or totals change. No broad retail word-copy, padding or trampoline substitute.
func_150417AC follows only after this actual match.
