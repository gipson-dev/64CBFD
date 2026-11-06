# Event height-threshold dispatcher match

Date: 2026-11-06. Continue the active 80% goal from consumer
`ee87641e4cbc85df8c4d05c2dc38393d6ea5c1c3` and mounted tools
`9c8ffc8ca6334ed909c2552a9663bd44b90adc80`, following
[Note 2127](2127-game-owner-position-request-direct-match-20261106.md).

## Recovered C and scheduling

`func_151CE51C` in `generated_1FA770` now matches its complete **70-word**
slot: VA `0x151CE51C..0x151CE634`, ROM `0x1FB9CC..0x1FBAE4`, 280 bytes,
frame `0x50`, saved RA at SP+0x14 and incoming actor home at SP+0x50.
The complete semantic C emits 72 words under the unchanged O2/g3/MIPS2/O32
profile. **18 expected-word guards**, including two scheduling omissions,
recover the retail stream. All four R26 bindings retain their original
callees. All **51 raw and padded neighbors**, pools and register metadata
remain unchanged. The owner has 52 actual function slots; the old shortlist
overcounted prototypes. Make and shared headers are unchanged.

The supported interface is `void(struct127 *actor, u8 *event)`. Lookup uses
the context pointer at event+0x18. A successful type-11 lookup calls the
existing position helper with a three-float position, radius and height.
The radius output is retained even though this routine only uses height.
The helper's real output initializes the vector's Y word at SP+0x48.

The recovered owner view retains flags u16+0x1E, fallback count u8+0x25,
signed count+0x2C, signed current/previous indices+0x2D/2E and table+0x94.
Each table entry is 0x1C bytes with its height at +4. Both paths require a
positive signed count. With flag8, previous-1 selects the entry; a negative
index falls back to unsigned fallback-count minus one. Dispatch occurs for
Y-height <= entry height. Otherwise current selects the entry and dispatch
occurs for entry height <= Y+height. Ordered comparisons reject NaNs. No
index clamp or additional pointer gate is invented. The dispatch remains
`func_1505D024(actor,0x60019,0,-1)`, with its real s32/u16 argument types.

Named center, extent, command, table and comparison intermediates recover
the retail frame without padding. The cleaner form recovers the opening instruction roles through word35;
three branch displacements differ until the omissions are applied. The remaining guards close six branch displacements, two
table-pointer register words, six compare/setup scheduling words, two
ordinary-branch/delay words and two omissions. The upper false branch uses
the existing shared saved-RA epilogue. The origin ledger accounts for every
emitted instruction and relocation; guard history is the old byte prefix
plus these 18 rows. No helper or algorithm body is substituted by the guards.

## Qualification

All eight checks pass before installation in both tools configurations and
again after installation against both actual helper copies. The sibling
overlay is confined to the ignored target directory. Its six tracked edits
and 2,428 untracked files remain unchanged. Both tools smokes are fresh.
Three unchanged shared suites per copy are exact-hash reuses from Note2124
(match-progress, word patches, PC16 padding), not fresh regression runs.

- **2,192 cases per body**, original/raw/normalized, compare complete memory,
  helper calls and ordered memory accesses. All 256 values of four byte
  fields, lookup/count gates, signed indices, unsigned fallback, owner and
  argument-home mutations, two stack phases and float edge cases pass.
  All 69 reachable retail words execute; the unreachable word is also
  pinned by the literal full-body comparison.
- Raw C executes at **0x15200000** in the model: its unpadded 72-word body
  overlaps the adjacent lookup at retail addresses. The normalized 70-word
  body fits the real slot. An initial raw-fixture overlap failure was corrected
  without changing C. Original/normalized complete states agree; raw C has
  matching memory/calls/access order, with no full raw PC/register claim.
- **143 own-access fault prefixes** compare literal original/normalized
  complete states, including both float outcomes and the shared RA epilogue.
  These are guest instruction checks, not portable C fault or FCSR proof.
- **260 cases per body** connect the original 39-word lookup and 41-word
  position helper. All 256 actor IDs, columns 0..103, both lookup phases,
  wrong-kind/context nodes, signed-half extremes and float outputs are checked
  against an independent complete-memory reference. **74 of 80 helper words**
  execute. Full helper-path, hardware and FCSR coverage are not claimed;
  the event dispatcher remains a bounded provider.
- **64 cases per literal body** execute the original three-word caller window
  at VA0x150A276C, with actor in S1 and event in S0 as explicit preconditions.
  The sole JAL is ROM0xCFC20 in `func_150A25D4`. No tail or literal pointers
  are found. Full parent execution is not claimed; raw ABI is separately
  exercised through SDK/native callbacks and relocation checks.
- **Nine independent GNU links**, three layouts and 24 cases per body
  qualify all four R26 bindings. Both 280-byte retail/normalized symbols
  and the separate 288-byte raw symbol and alignment tails are pinned.
- **98,304 native32 SDK/UBSan calls** at O0/O2/O3 check every used offset,
  complete valid negative-index backing, all byte values, post-query changes,
  ordered NaNs, nullable actor with absent lookup, complete objects/tables
  and guards, direct calls and compatible callbacks. Ten wrong variants fail
  with checked42 and no diagnostic or trap.
- All 288 raw-byte corruptions, four binding corruptions, 18 stale guard
  expectations, two missing omissions and five image corruptions are rejected.
  The old stub and a wrong-command source fail the literal-origin gate.

Eight preexisting Warning712 diagnostics in unrelated owner functions are
preserved. Comparison normalizes only owned filename and shifted line numbers,
then requires exact diagnostic text. They are not suppressed or repaired.

One bounded Claude advisory was attempted/completed through verified
claude.ai/firstParty Pro, safe mode, tools=[] and MCP=[]. Packet SHA256:
`75fc1e0bae50135321ae28e348ece1cd5a77d93b02bcc1fd6bca04706a80f739`.
Its inline-table hypothesis yields 72 words/frame0x48 and regresses the table
loads to F4/F8. Moving the float pair earlier leaves 72/frame0x50 and the
same 36 differences. Both are rejected as exact-match solutions. Inspection
corrected the initial diagnosis: the chosen raw C already uses retail's FP
registers, and both streams load the pair before the count branch. No advisory
source edit is adopted. The saved successful response preceded a console-only
encoding error; no second call was made. Other profile/type probes remain
private controls. No compiler profile or incompatible declaration is adopted.

## Actual production

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Actual Make compiles only this owner, with the normal profile and its eight
unchanged warnings. Keep both old-dependency flags for scoped builds until
a deliberate broader rebuild; the appended guards affect only this target.
No unrelated timestamps are changed. The actual ELF equals the independent
**216-byte** prediction with **zero exclusions or metadata permutations**.
Only the function body and symbol size (12 to 280 bytes) change. All 6,052
addresses, conversion rows, progress.csv and 189,088 protected data bytes in
720 owners remain fixed. The wider unfinished image retains its expected
checksum failure and existing duplicate generated_12D630 recipe warning.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,197 / 5,512 (76.14%) | 0 | 1,315 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,524 / 4,839 (72.82%) | 0 | 1,315 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**213 more** matches reach the current 4,410 threshold for 80%. Fingerprints:

- ELF: `ccb55cd901f68c8b8a148bc1ab233a833fe693035b05f8ecc764bbd4d07ee974`.
- Owner: `aa90756a5eb33da4a96c7c7f02c96493cdb25b15c388ce0bf7dbf610a3808f30`.
- Code binary: `1b7a61af45f0d2219e4ca037ddd637b6e0d5d46c582307ab4f22eab603fd6c58`.
- Guard CSV: `d4dffc34fb8b6371d8090bffe66ef9c93b5216cb347facd74e694cb8e15cf833`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence is retained under `conker/build/game-event-height-threshold-151CE51C-match/`.
All 107 frozen matching inputs are audited. Graphify receives a scoped refresh
with old-node retention evidence; no full-corpus extraction is claimed.
Tools are committed before consumer source, guards, documentation and pin.

After the complete runs, the wrong-context native fixture was given an
adjacent typed pointer field, so its off-by-four read remains defined. The
focused native check passed again in both tools configurations; the other
seven checks retain unchanged module fingerprints and their full-run receipts.

Next static target: `func_15022528`, a remaining 70-word Game routine in
`generated_49D30`. Verify its actual owner/interface and current retail slot
before screening. It has no new matching credit. Preserve unrelated work,
private inputs/saves, handwritten `func_150A76F0` and frozen host Release.
The full 80% goal remains active.
