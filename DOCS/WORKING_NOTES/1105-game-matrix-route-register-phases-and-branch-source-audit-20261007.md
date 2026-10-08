# Game Matrix-Route Register Phases And Branch Source Audit

Date: 2026-10-07

## Scope And Baseline

Continue `func_1514654C` from semantic-recovery commit `cd88e7c8` and
[Note 1104](1104-game-matrix-route-private-layout-and-semantic-recovery-20261007.md).
Retail remains **120 words / frame `0xA0`**, VA `1514654C..1514672C`,
ROM `1739FC..173BDC`.

The [production owner](../../conker/src/game_16EE20.c) is unchanged: complete
C120, matrix `sp+4C`, resolver outputs `sp+90/+8C`, **60 raw word differences**,
no guards. This follow-up installs no new C, instruction normalization,
compiler profile, shared header, conversion-ledger or root README change.

## Recovered Register Phases

The [branch driver](../../tools/experiments/game_matrix_route_branch_candidates.py)
separates the temporary actor bank from the selected matrix. It reuses the
actor variable for the later output cursor, while retaining the lookup-node /
input-cursor reuse from Note 1104. These are disjoint pointer lifetimes, not
dummy frame padding or a private-offset patch.

Experimental `phase-primary0-keyrepeat-order0` now recovers:

- **Seventeen opening words directly exact**, including descriptor S0,
  actor S2 and the original saved-register stores.
- Initial actor bank in V1, rather than the installed candidate's saved S0.
- Selected matrix in **A1**, with the four-word null-matrix/conversion block
  directly equal at the corresponding shifted location. No extra matrix-to-A1 move.
- Lookup node and point-input cursor in **S1**, actor and point-output cursor
  in **S2**, late counter S0 and count S3.
- The entire **sixteen-word point loop directly exact** at C `+168..+1A8`
  versus retail `+16C..+1AC`; all eight epilogue words also emit as retail.
- Actual private matrix/primary/secondary addresses remain `sp+4C/+90/+8C`.

This is **C119 / frame `0xA0` / 74 full-slot word differences**, not a
120-word match. Its isolated alignment nop is not a meaningful extra body
word. The larger position-based difference count is mostly shifted blocks;
it does not establish a better full-slot byte match than installed C120/60.
Keep this qualified phase form experimental, without inserting a word.

The remaining source issues are more tightly isolated:

- C loads the lookup key into A1 and uses a zero-key branch-likely with the
  descriptor-bank load in its delay slot. Retail uses V0, a normal branch
  and the key-to-A1 move in its delay slot.
- Retail loads resolver primary before the attachment branch, then reloads
  it on the attached path. C's per-branch assignment moves the null-path
  primary read into the final branch delay. A simple prefix assignment
  instead folds the null branch and attached reload, producing C117.
- The delegated bank/index address addition has reversed commutative operands.
  This alone would be a narrow normalization question after the complete
  source fit is recovered; it does not justify changing the key or read topology.

Do not use sixty bulk guards, normalize branch/read order, insert a missing
instruction or promote the C119 form as a match. Byte matching remains open.

## Measured Controls And Maintained Tests

Retain **92 additional measured forms**, none raw exact: 27 matrix/key/primary
carriers, eighteen output-pointer phases, eighteen key/prefix/address views,
eleven array/struct/union/volatile storage forms and eighteen structured/label
flow forms. Together with Notes 1103/1104, **377 forms** are retained.

The first descriptor-carrier transform could overwrite the descriptor before
reading an attached lookup's matrix index. These forms now retain a separate
source descriptor before repurposing the formal. The incorrect generator
version was not installed or counted as passing qualification.

The two volatile-primary probes are diagnostic controls only, not evidence
that the original source used volatile storage. They still emit C118 and do
not justify inventing private-memory volatility in production. Alternate
array/struct/union output storage and explicit labels also fail to recover the
full original read/branch topology.

[Branch tests](../../tools/tests/test_game_matrix_route_branch_recovery.py)
reuse the established independent route/math oracle and original helpers:

- All **92 controls / 2,208 ordinary executions** qualify public effects.
  This does not assert lazy faults, incoming homes or private equivalence
  for every control, particularly forms with changed private allocation.
- The selected phase form passes **1,728 public-trace fixtures**, **336 home
  mutations**, **24 attachment changes** and **864 connected original-helper
  cases**, comparing actual private argument addresses and full return words.
- All **sixteen old private-matrix counterexamples** agree, plus **560
  additional matrix source/destination/resolver-output overlaps**.
- Five lazy gates, twelve required-storage faults and four guest-only
  wrapping indices retain the prior contract.
- **9,216 native 32-bit cases plus three lazy gates**, complete experimental
  C and actual SDK converter C; other callbacks remain bounded validating hooks.
- Copied owner: **89 functions / 88 unchanged neighbors**, identical normalized
  pools and the same two warning statements; target equals the isolated object.

No full stack-memory equivalence, complete resolver coverage, hardware FCSR
or PC-port acceptance is claimed. The production resolver is still a separate
zero-return placeholder. All **nine new tests pass in 114.007 seconds**,
zero skips/errors/failures. All **29 combined branch/layout/prior tests pass
in 419.377 seconds**, zero skips/errors/failures. Tools, Python syntax,
CLI help and scoped whitespace checks pass. The documentation checker verifies
**87 documents / 4,005 relative links / zero broken links**.

```sh
python3 -m unittest tools.tests.test_game_matrix_route_branch_recovery tools.tests.test_game_matrix_route_layout_recovery tools.tests.test_game_matrix_route_recovery -v
make tools-check
```

## Linked Boundary And Next Work

Compare against Note 1104's authoritative
`conker/build/game-matrix-route-layout-test/after.json`, not the earlier
placeholder snapshot. Production code is unchanged, so no rebuild is required
for this experiment/test/documentation batch. The full audit confirms all
6,058 symbols, 6,042 retail slots, sixteen overflows, 11,063 guards, protected
sections, 720 exact Game-data owners and the conversion hash are unchanged.

Matching stays **3,364/5,466 total (61.54%)**, **2,691/4,793 Game (56.14%)**,
**2,102 different**, zero drift; Init 492/492 and Debugger 181/181 exact.
Keep root README aggregates unchanged. Next source work should preserve this
qualified register-phase layout and address the key's normal-branch argument
move plus the mandatory primary/readback topology together. Production
resolver recovery can proceed as a separately scoped function batch; basis,
translator and sampler remain open. No sibling, frozen Release, save,
runtime/hardware or push action.
