# Game Main Resource Loader Status-Join Experiment

Date: 2026-10-11. Target: the same complete func_1503CF20, VA
0x1503CF20..0x1503D368, ROM 0x6A3D0..0x6A818, 274 words / 1,096 bytes.
Owner: conker/src/game/generated_6A3D0.c. This is an experimental checkpoint,
not an installed improvement, conversion or byte match.

## Baseline And Decision

Consumer 3508017c15149cb0313c5842431a0cbec8d6ffb6, tools
e06635cede2a719f252ffdc5d76863075c1c4a3b. The installed complete recovery
from [Note 1261](1261-game-main-resource-loader-retail-length-improvement-20261011.md)
remains 274 words, frame 0x80 versus retail 0x78, 271 raw differences,
no guards. No production C, ABI, compiler profile, layout, guard or data edits.

Keep that verified baseline. A natural request-failure status return join
now selects retail's S6 status register, but the frame remains wrong and
the closest prefix-preserving form exceeds the slot. A smaller raw difference
count alone is not enough to replace the installed checkpoint.

## Controlled Measurements

New tools: experiments/game_main_resource_loader_flow_costs.py and
tests/test_game_main_resource_loader_flow_costs.py. All 31 candidates compile
the complete semantic routine with the existing retail O2/g3/no-loop-unroll
profile. No extra allocator switches, synthetic uses, cleanup pointer casts,
instruction guards, function truncation or production installation.

| Complete Candidate | Words | Frame | Raw Differences | Status Allocation |
| --- | ---: | ---: | ---: | --- |
| Banked late initialization | 274 | 0x80 | 271 | late S4 |
| Early initialization only | 287 | 0x80 | 262 | opening status spills, no S6 save |
| All early exits share status return | 268 | 0x88 | 262 | S6, changed opening branches |
| Request failure joins status return | 276 | 0x88 | 194 | S6, opening presence/identity returns retained |
| Presence and request join status return | 274 | 0x88 | 194 | S6, changed presence return |
| Request join reuses boundary for initial count | 273 | 0x88 | 261 | S7, eight saved registers |

The request-join change assigns failed = 1 and jumps to the final status
return on request failure, rather than returning literal 1 directly.
With otherwise unchanged early initialization, IDO saves S0..S6 and emits
the opening zero status in S6 at target offset 0x6C, matching retail's
status initialization offset. It still sets S6 rather than V0 on the
request-failure delay path. Separate local status instead of parameter scratch
keeps S6 but enlarges this form to frame 0x90 / 191 raw differences.

Moving initialization to the function opening, returning zero status at
presence, and register hints alone do not recover S6. Explicit gated event
do-loops do not remove the extra private count-pointer copy. A separate initial-count
temporary compiles identically to the request-join assignment form; reusing
boundary changes register pressure and moves status to S7. Do not install it.

Measured cause at the source/output boundary: the controlled request-failure
join selects S6 under this compiler/profile. The optimizer's internal cost,
live-range split and original source spelling have not been observed or proven.

## Diagnostic Limits And Fixture Correction

Read-only native compiler inspection found optimizer listing/why-uncolored
option strings. The local wrapper's verbose/show modes abort on an unsupported
fprintf timing format. Listing attempts terminate the optimizer with signal
11; -zdbug is rejected. Ordinary candidate compilation succeeds with zero
diagnostics. Do not modify the compiler or rely on absent listing output.
All diagnostic outputs are transient; no guest debugger/editor attachment.

The initial new semantic suite failed because oversized candidates linked at
the retail entry overlap the actual func_1503D368 helper address at +0x448.
The existing instruction oracle executes a call target inside its code map
instead of treating it as a bounded helper. This is a fixture address collision,
not evidence that the installed loader fails. Do not shorten candidate bodies
or bypass the helper call to make the test pass.

The final suite relinks complete candidates at isolated VA 0x15400000 and two
other nonoverlapping entries. Actual helper targets remain unchanged; globals
are independently rebased. The complete bodies pass unchanged after this
client-only fixture correction. No shared oracle or production code changed.

## Fresh Qualification

- Five new tests pass in 124.353 seconds; 31 unique complete candidates,
  zero compile diagnostics or data pools, source fingerprints recorded.
- 1,021 full-reference cases per candidate: 31,651 cases / 63,302 guest runs.
  All 273 reachable retail words execute; the duplicate compare at +0x48
  remains statically unreachable. No all-current-word coverage claim.
- Thirty live-loop/cleanup callback cases per candidate: 930 cases / 1,860
  runs; preserve live primary counts/bases, cached secondary count, events,
  helper return gates and callback-rebound cleanup slots.
- 8,928 ignored-incoming-word/identity/presence/extras cases / 17,856 runs
  over 96 independent links. The freshly compiled lost-request-error negative
  control fails effectively. Private request-output addresses are normalized.
- Installed-loader eleven-test suite passes freshly in 21.659 seconds,
  including aliases, public-access fault prefixes, effective controls,
  native32, both actual padders, all 14 owner neighbors, linked audit and
  the actual five-routine chain within its documented deeper-helper bounds.
- Build/CSV are up to date. Consumer, mounted and older WSL tools checks
  pass; new files pass native py_compile in both checkouts. Preserve the
  duplicated generated_12D630 recipe warning, not a warning-free build claim.

The uninstalled variants are not qualified for native32, owner installation,
padders, private-frame faults, deeper helpers, heap/hardware/rendering/gameplay
or 64-bit host behavior. Prior unchanged recovery/neighbor-suite receipts from
Note 1261 remain prior evidence, not fresh tests for these variants.

## Unchanged Linked State And Ownership

Source SHA-256 remains
25fd41ff70c4fb4db5c7649c74c27fbd4d72ed10831f95ffcb1abdaf75f18a52;
ELF SHA-256 remains
2129eb586ceac58a8201542a83a62601853a16d8589f49596fdeb137fb02fcaf.
The whole ELF is identical, not just neighbors. All 189,088 protected data
bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Guards, conversion CSV, rodata source, symbols, auto assignments and layout
retain their immutable checkpoint hashes in the new baseline receipt.
Root README is unchanged, SHA-256
0c2e0ab2781b9f7dcc9e86e79bbcc3f8b57d107ca28b02e51f524b8232a6f1cd.

Fresh matcher: Game 2,789/4,822 (57.84%), total 3,462/5,495 (63.00%),
Init 492/492 and Debugger 181/181, zero drift / 2,033 different. No credit.

Tools 9aa880b banks the two new authored files before the consumer pin.
Copy only those two absent paths to the older standalone sibling: dirty
entries 291 -> 293, HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and
all twelve protected existing hashes unchanged. Do not overwrite its older
tests, commit/reset its independent history or push either repository.
No OGL/Release/save/editor/private-input changes; Release remains frozen.

Native Graphify update after tool edits refuses unsafe shrink 39,772 -> 17,990,
retaining 19,398 nodes from 2,972 existing excluded files. Preserve these
protective, version and devcontainer warnings; no force/purge/install. The consumer commit's
detached hook must finish with fresh log growth/UTC, a fresh Rebuilt record
and zero actual Graphify/Python workers before close-out.

## Workflow And Next Work

Single Codex writer, zero Claude calls: compiler output and independent
references settle this bounded decision locally. No bridge/account changes.

Continue the same full func_1503CF20, not an easier neighbor. Use the
prefix-preserving request-join as a measured S6 reference, not installed C.
Preserve the existing continuous S5 count-pointer lifetime while removing the
extra private copy at target +0x1A0 (sw S5, SP+0x40) and event-opening reload
at +0x2B8 (lw T1, SP+0x40). The first event count uses T1; the later event
count still uses S5. This redundant transfer is observed, not a proven
register-lifetime split. Preserve every public access while resolving it.
Restore frame 0x78, request output +0x6C, main/word-index scratch +0x58/+0x5C,
half-index +0x4C and boundary scratch +0x68. Then reconcile original direct
request return and every delay/control join, requalify owner/padders/connected
caller and audit the whole linked ELF. Do not normalize 194 or 271 broad
layout/scheduling differences with guard rows. The wider Game goal stays open.
