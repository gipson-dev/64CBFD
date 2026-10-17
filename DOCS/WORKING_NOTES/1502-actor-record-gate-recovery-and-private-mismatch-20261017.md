# Actor Record Gate Recovery And Private Mismatch

Verified 2026-10-17. Consumer predecessor912b5cba; tools predecessor3daba3b.
Both active checkouts began clean. Prior goal turn was progress: two complete
restorations were banked. This turn banks reproducible recovery/rejection
evidence, not another exact function. Preserve all production code and the
older standalone tools mirror's independent dirty state/HEADddbdd16b.

## Target And Semantics

Continue `func_150F2A60`, owner `generated_11FF10`, original
`conker/asm/11FF10.s`, VA150F2A60..150F2C8C, ROM11FF10..12013C,
139 words/556 bytes, frame0x40. The production zero-return placeholder remains
unchanged. The real routine has an unused argument with an incoming home and
no deliberately established C return value; the candidate uses a `void` body.

When D_800CC5EC is nonnull and its byte0x120 is zero, search IDs250 then249 via
func_151149AC. Subtract the reloaded D_800DBEF4 base from the lookup result,
divide the signed32 difference by160 with truncation toward zero, and test
the low bit in the reloaded D_800DBF94 table. The retail code does not add a null-result
check; do not invent one. On the first flagged record, optionally refresh the
selected actor at D_800CC2D0+(byte(D_800CC40C)-100)*812, clear D_800CC49A, then
make the original reset/sound/refresh/mode calls and stop scanning.

Whether or not either record qualifies, find object type14 and take its0x2E4
word or zero. Reload D_800BE4F0 before each of four handle operations, passing
(value,0), (0,-value), (value,0), (-value,0). The actual six-word func_15196318
writes low bytes at handle0x12/0x13 only when the handle is nonnull. The initial
working label "overlay" was unsupported; the banked purpose comment says
**handle offsets**, without inventing a subsystem identity.

## Exact Measurements, Not A Match

The complete ordinary semantic body emits137 words/frame0x40, raw SHA-256
`28c65059860b7a8f40b59166beecbfbe9fecf1c6b7b392a130d9a74d42dcf125`.
There are118 unequal overlapping words and a two-word extent deficit. Linking
the normal owner padder's complete139-word slot gives **120 differences**.
Both raw and padded copies preserve all11 neighboring routines and normalized
owner pools. These checks do not authorize installation.

Seven source/profile screens are reproduced by the committed experiment:

| Screen | Words | Frame | Unequal Overlap Words |
| --- | ---: | ---: | ---: |
| Ordinary O2/g3 semantic body | 137 | 0x40 | 118 |
| Same body, no unroll | 137 | 0x40 | 118 |
| O2 without g3 | 136 | 0x40 | 134 |
| O1 | 126 | 0x38 | 124 |
| Named record index | 137 | 0x40 | 115 |
| Explicit retry label | 138 | 0x40 | 122 |
| Object assignment in condition | 137 | 0x40 | 118 |

Other local scratch screens (typed actor array, do/while, early returns,
integer/indirect gates, scan-first and stop-index assignments) also fail.
Do not repeat those solely for equal counts. O1 begins with a conditional
gate before its prolog; frame extraction must find the actual negative SP
adjustment, not negate the first instruction's immediate. The scratch
first-word frame metric for that profile was invalid and is not reused.

Two independent private-contract discrepancies are measured:

1. After two actual instruction accesses, retail has saved S4 at SP+0x38;
   the candidate has saved S5 there. Fault cut2 rejects the complete private
   state before any provider runs. Retail saves S0..S4; candidate saves S0..S5.
2. Retail reads D_800CC5EC twice before the byte gate; the candidate reads it
   once and caches it. Public agreement cannot establish the same fault/access
   contract. Retail also retains signed SLTI(counter,2), while the candidate
   holds bound2 in S5, and retail rematerializes the actor-array address where
   the candidate keeps it in saved S0 across success calls.

These are measured facts. A proposed common register-pressure/CSE cause is a
hypothesis until a fired normal compiler capture establishes it. No forced
registers, dummy padding, volatile declarations or wide instruction guards.

## Focused Public Qualification

Five final recovery tests pass in17.302s. They intentionally prove the selected
public behavior and **reject** matching/private equivalence:

- 960 retail/candidate core cases cover null/blocked/open gates, both flags,
  selector-byte endpoints, object absence and five full-width result words.
- 400 sparse signed pointer-difference/provider-mutation cases cover negative,
  unaligned and wrapping guest differences; table/global/handle-bank reloads;
  and two stack phases. Sparse guest addresses are not portable C pointers.
- 16 cases connect the actual28-word lookup;24 connect both that lookup and
  the actual six-word byte-offset setter, including null handles, low-byte
  truncation and word NEGU behavior. Remaining providers are scripted.
- Native32 O2/O0 each pass256 separately typed caller cases with complete
  aligned objects, valid same-array subtraction, UBSan and four effective
  selector/axis negatives. Native cases exclude INT_MIN negation and sparse
  guest pointer arithmetic; they do not prove full C portability or private ABI.
- All253 protected entries /233 paths remain byte-identical, including every
  production source/guard and the complete ELF. All189,088 Game-data bytes /
  720 owners remain exact. There is no broad linked rebuild or new matching
  credit to infer from this research.

Harness corrections stayed outside production: the first mask-table fixture
accidentally reused the oracle's STACK address; sparse redirected tables needed
explicit backing; the native object fixture needed room for its0x2E4 field.
Failed fixture runs are not accepted receipts or production defects.

## Advisory Boundary

One packet-only advisory ran with tools disabled, safe mode, strict MCP config
and no session persistence; no tools or repository edits were made by Claude.
Session8749b53b-829b-4c5e-83cb-1e90716d5a9c. Complete original/candidate listings
were included; a first oversized local packet extraction was rejected before
any call, then the bounded packet was rebuilt successfully.

Two suggestions repeated the already rejected for-counter/typed-array forms.
The third, assigning the object result within the condition, was independently
compiled and emits exactly the original137-word candidate/hash. Reject it too.
The advisory's semantic-equivalence and allocation explanations are not proof;
the independent measurements and private counterexample govern the decision.
No setup, provider, account, dependency or billing configuration was changed.

## Bank And Resume

Tools checkpoint **b0ae735** banks the candidate and tests, followed by consumer
docs/pin. Both copies pass12 shared checks and smoke checks; four ASCII/AST
parses and two exact task pairs pass. Preserve1,116 unrelated mirror hashes,
1,118 dirty paths and mirror HEADddbdd16b. No standalone commit/reset or push.
Keep post-commit Graphify's retained19398 nodes /2972 existing excluded files,
require a fresh rebuilt receipt, and finish owned workers before closing.

The complete production ELF stays SHA-256
`f56e3591c3c86189f630e4b8d599d8cfd7920165766e0c309a310970cd12ba6a`;
Game data stays
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Existing progress remains Game2,962/4,828 (61.35%), total3,635/5,501 (66.08%),
1,866 different, zero drift. Root README is deliberately unchanged. The byte
identity of the unchanged ELF/CSV supports unchanged totals; this does not
claim a fresh full legacy suite or another production match.

- [x] Recover complete behavior and bank reproducible source/profile screens.
- [x] Qualify public/actual-helper/native domains and negative controls.
- [x] Demonstrate the private saved-word and global-read counterexamples.
- [x] Preserve production/data/guards, pass both tools-copy checks and bank
  a precise handoff without adding matching credit.
- [ ] Continue **this same func_150F2A60**. Use existing read-only IDO/UOPT
  capture patterns to inspect the normal candidate's bound2 promotion,
  actor-base live range and opening global-load CSE. Verify the exact compiler
  fingerprints, fired probes, child/driver completion and normal-object identity.
- [ ] Recover retail's139 words, five saved registers and initial read order;
  only then qualify the full private/fault/relocation and first-image gates.
- [ ] Keep both fade lifetime gaps and wider Game matching open. No host-port
  work or frozen Release action occurred.

```sh
python3 -m tools.experiments.game_actor_record_gate_recovery
python3 -m unittest tools.tests.test_game_actor_record_gate_recovery -v
make tools-check
```
