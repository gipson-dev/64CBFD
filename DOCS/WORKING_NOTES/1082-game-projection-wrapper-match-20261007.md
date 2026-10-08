# Game Projection Wrapper Match

Date: 2026-10-07. Baseline: `28e0b289`,
[Note 1081](1081-game-projection-wrapper-lifetime-recovery-20261007.md).
Recover `func_15144CEC`'s101-word/frame0x48 semantic body from its zero-return
placeholder. No shared headers, production compiler profiles, helper bodies
or padder algorithms change.

## Compiler Recovery

Inlining the temporary view pointer removes one declared local. Reuse the
cached-depth float for the complete projected X result, and use the freed local
for Y's product. Capture both results before storing X; this preserves the
alias-sensitive Y scale and gives the scheduler independent work between the
floating multiplies. Do not move the Y product after X or retain stale inverse/
view-base values. The selected body fits101 words/frame0x48,37 aligned differences.

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_projection_schedule_candidates.py)
retains eight order/add/product controls across four profiles,32 measurements.
Four O2/g3 controls fit101 words/frame0x48 with37 differences; reversed capture
order adds a NOP and emits102 words/45 differences. O2 without g3 emits99/100
words but differs92 words; O1/g3 and O1 emit114/115 and113/114 words/frame0x40.
They are compiler controls, not alternative installed profiles.
An earlier16-form inline-view/X-product probe fits the frame but stays102 words.

64 words match directly. Thirty-seven expected-word/expected-relocation guards
normalize closed temporary-register allocation, commutative operand order and
one four-word independent pre-X-store schedule. Raw -> retail offsets:

| Raw Offset | Retail Offset | Operation |
| --- | --- | --- |
| 0x13C | 0x140 | Load X offset |
| 0x140 | 0x144 | Set successful return value |
| 0x144 | 0x148 | Multiply X by adjusted scale |
| 0x148 | 0x13C | Load Y scale |

No insertion, omission, branch/frame/private-slot/immediate change or helper
replacement. The two view-address guards preserve HI16/LO16 relocation ownership
and zero object addends; they change register fields only. All nine original
relocations remain at their original offsets with their original owners.

## Qualification

[Match tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_projection_schedule_match.py)
reuse the maintained lifetime corpus and add fitting-body/guard/owner/caller
checks. Raw C, original retail and guarded code are tested separately.

- 36864 guest cases cover256 poisoned-byte indices, eight null-output masks,
  nine aliases and two stack phases. External footprints, ordered writes,
  helper vectors, status and saved state match the independent reference.
  External read multisets agree between every external-write boundary; this
  preserves live dependencies without claiming identical independent read order.
- 384 depth/bound/mask/phase fixtures preserve lazy lower/view reads and zero
  gates. All58 real helper words and100 reachable wrapper words execute.
  Dead duplicate MTC1 at0xD8 is unchanged and structurally pinned.
- 512 helper-boundary index-home and eight view-pointer overlap probes retain
  matrix/view index distinction and the post-X view reload. Reciprocal/XY overlap
  retains the post-X inverse reload. Boundary mutations remain seeded probes.
- 512 additional cases let the real helper's W store overwrite the incoming
  index home. Matrix selection retains the original index, while the view uses
  the updated low byte, without an injected mutation. The independent reference
  now seeds/rereads that home rather than deriving it from its action list.
- 24 missing-required-field cases fail closed. Three compiled alias negatives
  still fail actual output values, including inline-Y's2.5 versus retail26.5.
- 92160 actual freestanding32-bit C calls cover all indices/null masks/nine
  aliases/five depth paths. All136 bounded footprint words and helper vectors/
  status match an independent native reference. Native fallback addresses are
  private to separate calls, not compared as shared guest-home identities.
- 1728 paired instruction-input traces close every guard under exactly the
  four-PC mapping above. Memory addresses, values, branch conditions, integer/
  floating operation inputs and helper inputs agree. Only commutative operands
  are sorted; subtraction, division and ordered comparisons retain operand order.
- 1536 connected cases execute the original11-word setup at `150CE270`, ROM
  `FB720`, including the index SW in JAL's delay slot. Original argument staging,
  three caller-owned scalar outputs, XY pointer and both six/eight-position
  call vectors agree. Prior point-transform context and return scaffolding are
  seeded/synthetic, not complete-caller or hardware acceptance.
- 4096 varied finite-coordinate/matrix/scale/offset cases exercise single-
  precision rounding, negative/fractional values, depth gates and aliases.
- Copied owner preserves89 symbols, all88 neighbors' bytes/relative relocations,
  normalized data/rodata pools and both original warnings. Raw copied target
  equals standalone C. Actual padder/link emits101 retail words with the same
  nine relocations and two global-address/HI16-carry layouts. Stale words and
  stale relocation metadata fail closed.

Twelve pre-install tests pass in90.034s, zero skips/errors/failures. The original
caller test subsequently passes in11.619s; varied finite cases pass in18.029s.
The natural W-home-overlap and original caller checks pass together in9.916s.
Finite output/dependency checks do
not claim raw independent read ordering, FCSR/exceptions, NaN payload behavior,
hardware execution, complete callers, gameplay or host-port adoption.

## Installation And Audit

Install only the recovered function/local helper declaration/typed prototype
and append37 guards. The prior10916 CSV rows are unchanged. Historical guard
checks explicitly pin the complete prior digest and append this exact guard set;
the previous secondary-table check still binds precisely its own two rows.
The old projection audit retains all20 compiler receipts and58 helper identities,
but now verifies the qualified production source/slot instead of the removed stub.

US ELF rebuild and complete linked audit pass. Only `func_15144CEC` changes
across6059 slots. Every address/extent, all protected .init/.init_data/.debugger/
.game_data sections and all720 Game-data owners/189088 bytes are unchanged.
All10916 prior guards are unchanged;37 additions total10953. The complete
101-word slot is byte-exact.

Matching becomes total 3353/5465 (61.35%), Game 2680/4792 (55.93%), 2112 different,
zero address drift. Conversion stays 5465/6042, Game 4792/5321. README updates
aggregate matching rows only.

All 206 production regression tests pass in 1005.830 seconds, with zero skips,
errors or failures. This retains the complete earlier 164-test suite and adds
the 16 match, three historical projection audit, ten lifetime and thirteen
triangle/helper tests. The final post-regression linked audit again changes only
the target across all 6059 slots, with data owners and historical guards intact.
Project-tool, Python syntax and whitespace checks pass. Documentation gate:
64 documents, 3727 relative links, zero broken links.

## Resume

Next forward placeholder: `func_151451F0`,53 words/frame0x28,
VA `151451F0..151452C4`, ROM `1726A0..172774`. Original inspection shows nine
incoming arguments: preserve arg3's float bits, skip the fifth threshold argument
when forwarding eight arguments to `func_151452C4`, then use two live float outputs
for sign/threshold acceptance. Qualify its lazy output reads and the real callee
contract before installing. This is inspection only, not a completed recovery.
The callee's original body also writes both points/distances before a final
dot-product sign check through the already recovered `func_15144A74`; a false
return is not evidence that those outputs were untouched. Preserve the wrapper's
post-call argument-home reloads, lazy second-distance reads and unordered
floating comparison behavior when qualifying this dependency.

`func_15144E80` remains its previously restored original assembly. Sampler
`func_151432BC` scheduling and oriented `func_15142600`'s27 private offsets remain
open. No sibling/frozen Release/save/runtime or push work; broader matching goal
stays active. Ignored receipts: `conker/build/game-projection-schedule/` and
`conker/build/game-projection-schedule-test/`.
