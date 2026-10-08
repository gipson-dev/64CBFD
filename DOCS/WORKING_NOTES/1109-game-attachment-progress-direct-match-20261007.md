# Game Attachment Progress Direct Match

Date: 2026-10-07

## Scope And Baseline

Continue Game matching from commit `2412839a` and
[Note 1108](1108-game-matrix-parent-lookup-direct-match-20261007.md).
Recover `func_1503327C`, retail **43 words / 172 bytes / frame `0x28`**,
VA `1503327C..15033328`, ROM `6072C..607D8`.
Its production body was a three-word zero-return C placeholder padded to
the 43-word retail span, with **40 instruction differences**. It was already
counted as converted, not semantically recovered or byte-exact.

The [production owner](../../conker/src/game/generated_5D2C0.c) now contains
the complete attachment setup/progress query. All **43 words emit directly
as retail** with the existing `-O2 -g3` / MIPS2 profile. No guards, instruction
insertion/omission, padding promotion, Makefile/profile changes or shared types.
One SDK-only declaration recovers the setup callee's six-word ABI.

## Recovered Contract

Read the attachment pointer at node `+0x48`; an absent attachment returns zero
without reading flags, progress, end, or the unused second incoming argument.
For an attachment, test its unsigned halfword flags at `+4`. When bit `0x8000`
is clear, call `func_1503F5B8(attachment, 0, 0, 1.0f, 0.0f, 1)` and reload
the attachment pointer through the node after the call.

The node incoming home is real: retail stores both incoming words, reads node
back from its home, and reloads that home after setup. A validating callback
can change it to another node. The second word is stored but never dereferenced;
null and otherwise invalid second-argument bit patterns remain accepted.

Return one when `attachment.end - 1.0f <= attachment.current`, using float
fields `+0x18` and `+8`; otherwise zero. Read the end before the current field.
The subtraction is single-precision. This is not an integer threshold or
double-precision reformulation. Ordered NaN comparisons are false in the
guest/native predicate models; FCSR exception/trap state is not qualified.

Do not add a node-null gate or a new attachment-null check after setup. Retail
requires the post-call node and attachment storage, and earlier setup effects
remain observable when a later read faults. Tests use valid native objects;
guest fault probes are not a native invalid-pointer safety claim.

## Profile And Source Evidence

The argument spills initially suggested an `-O1` hypothesis. Actual compilation
rejects that hypothesis: the ordinary source matches under the owner's existing
`-O2 -g3` profile, without any function-object selection or Makefile edit.

| Profile | Meaningful Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| `-O2 -g3` | 43 | `0x28` | 0 |
| `-O2` | 42 | `0x28` | 37 |
| `-O1 -g3` | 45 | `0x28` | 42 |
| `-O1` | 45 | `0x28` | 41 |

The [candidate driver](../../tools/experiments/game_attachment_progress_candidates.py)
retains sixteen comparison/mask/return/register forms. The
[ten tests](../../tools/tests/test_game_attachment_progress_match.py)
qualify **19 distinct source/profile combinations / 684 ordinary executions**.
Four source forms emit raw exact; current-first/end-first comparisons and the
register keyword do not change the selected body. Comparing the full masked
value with `0x8000` and using explicit return branches preserve retail's
instruction count. Simplified mask tests or boolean returns emit shorter bodies.
All-control incoming-home, fault, private and read-order equivalence is not claimed.

## Qualification

All **ten pre-install tests pass in 57.072 seconds**, zero skips/errors/failures:

- **45,000 guest cases plus two absent-attachment cases**, six flag patterns,
  25 current/end bit patterns, six setup mutation modes and both SP phases.
  Compare complete returns, ordered public reads/writes, public memory, setup
  ABI and both incoming homes against an independent reference; full C/retail
  GP/FP register files and instruction traces agree. Saved SP/GP/RA/FP checked.
  Only unvisited word is the unreachable branch-likely duplicate at index 11.
- **128 alias/unused-word cases**, self-attached node, null/high-bit second
  argument, pointer replacement, field mutation and unused-home mutation.
  This does not establish arbitrary private-stack alias equivalence.
- One lazy absence case and **ten required-read faults**: node, flags, initial
  end/current, replacement attachment, replacement node, post-setup null node
  or attachment. Exact error, preceding public trace and partial effects agree.
- **45,000 native 32-bit cases plus one lazy gate**, actual complete C and a
  validating setup callback, four public mutation modes, three unused-argument
  forms, valid aligned storage. Compare return, calls, full callback argument
  bits and all object bytes. Includes zeros, adjacent float thresholds, large
  values, infinities, quiet NaNs and subnormals. Private-home mutations and
  FCSR exception state are separate from this native proof.
- Three effective compiled negatives: cache attachment across setup, omit
  threshold subtraction, or test the wrong initialization bit. Each changes
  return/calls without treating a fault as successful negative evidence.
- Copied owner: **40 functions / 39 unchanged neighbors**, zero warnings;
  target equals the isolated C, neighbor bytes/relocations and pools intact.
- Actual generated-slice padder: **172-byte meaningful body and retail slot**,
  no added padding, setup `R_MIPS_26` retained at `+0x58`; independently rebase
  function entry and callee and check the entire linked body.

The setup callee is a bounded validating callback, not connected full setup
execution or hardware/PC-port acceptance. The original function body is
executed completely by both guest instruction models.

The first qualification run exposed two fixture issues: the old placeholder
was incorrectly pinned as JR-before-clear rather than its actual clear/JR/nop,
and GCC rejected a misleadingly indented native-harness statement. Both were
corrected before recording the passing run; neither was a production edit.

All **42 installed attachment-progress/lookup/key-fit/resolver regression tests
pass in 265.112 seconds**, zero skips/errors/failures. Both complete actual-
wrapper connection suites, previous alias/home/native/source-fit/owner/padder
gates remain green. `make tools-check`, Python syntax, module CLI help and
staged whitespace checks pass. Documentation validation checks **91 documents /
4,043 relative links / zero broken links**. This is scoped guest/native/tool
qualification, not full setup-callee, FCSR, hardware or PC-port acceptance.

## Linked Audit And Progress

US ELF and ignored conversion CSV rebuilt through normal Makefile rules.
Compare against Note 1108's authoritative ignored checkpoint
`conker/build/game-matrix-parent-lookup-test/after.json`.
Only `func_1503327C` changes across **6,058 symbols / 6,042 retail slots**.
Its frame/body now match retail with zero differences. All **6,057 other
symbol bodies**, other slot addresses/extents, sixteen overflows, protected
Init/Debugger/Game-data sections, **720 exact data owners / 189,088 bytes**,
all **11,063 guard rows**, and the conversion CSV hash remain unchanged.
The build has only the pre-existing duplicate `generated_12D630` recipe warning.

Matching becomes **3,366/5,467 total (61.57%)**,
**2,693/4,794 Game (56.17%)**, **2,101 different**, zero address drift.
Init 492/492 and Debugger 181/181 remain exact. Converted function/byte
percentages do not change because this replaces an already-counted C placeholder.
Root README updates only the two aggregate matching rows.

New authoritative ignored checkpoint:
`conker/build/game-attachment-progress-test/after.json`, with `audit.py` / `audit.json`.

```sh
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_attachment_progress_match tools.tests.test_game_matrix_parent_lookup_match tools.tests.test_game_matrix_pair_resolver_key_fit tools.tests.test_game_matrix_pair_resolver_recovery -v
make tools-check
```

## Next Work

Continue Game matching; this is one completed function, not completion of the
Game section. The resolver `func_15031070` remains complete C84/frame `0x20`/
40 differences, including its missing meaningful V0-to-A1 key move. Matrix
wrapper key/primary-read, basis private layout, translator and sampler
boundaries remain open. The next local unrecovered bodies include attachment
setup/progress copier `func_150331B8` and node action dispatcher `func_15031A50`; inspect
their retail contracts before deciding the next matching batch.
No sibling, frozen Release, real save, runtime/hardware or push action.
