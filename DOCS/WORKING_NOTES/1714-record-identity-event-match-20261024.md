# Record Identity Event Match

2026-10-24. Fully qualified, installed, production-built, adopted and freshly
recounted. Complete semantic C matches with eleven derived expected-word
guards. This is guarded C, not a compiler-only match. The wider 75% exact-C
goal remains active.

## Target And Baseline

- Function `func_151B1FAC`, owner `generated_1DD500`.
- Body VA `0x151B1FAC..0x151B2058`; ROM `0x1DF45C..0x1DF508`.
- Body: 172 bytes / 43 words, frame `0x18`, one call binding at `+0x94`.
- Preserve two alignment words through VA `0x151B2060` / ROM `0x1DF510`:
  the full slot is 180 bytes / 45 words.
- Consumer predecessor `e21dba1ea3200e468789d3f038226f1c0607d583`.
- Tools-first commit `912930842717f4646a57dbf429691b8113cdf50a`.
- Original assembly stays in `conker/asm/1DD500.s`; normal O2/g3 is unchanged.

Capture verifies 16,018 old native/cache files and 55 focused immutable inputs.
The updated seal covers 16,022 files, including all 1,454 linker objects.
Use the existing PSBBN stdin/tar bridge, not project reads through DrvFS.
Focused snapshot SHA-256:
`9d01e99af20d445770635cae419787038f23b0eac0e0bd57e5e1d1411f60332a`.

## Recovered Semantics

[The source](../../conker/src/game/generated_1DD500.c) now implements
`void func_151B1FAC(struct260 *record, s32 eventAddress, u8 command)`.
Add the required `structs.h` include; preserve the owner's existing
`void func_1516972C(void *arg0)` declaration. Do not insert a conflicting
`struct102 *` helper declaration. The first owner compile caught the missing
record-type include; correcting the proposed owner required no shared-header,
compiler or ABI change.

Private `RecordIdentity1DD500` exposes only the opaque signed 32-bit identity
at record `+0x28` and key byte at `+0x2C`. Do not expand the shared `struct260`
header into a guessed complete payload schema.

Command `0x2D` is handled first. Capture the saved identity before reading
the first event word. If that word matches, store event word two as the new
identity, then read event byte nine as the key. Otherwise, if word two matches,
store word one, then read event byte eight as the key. The first match wins
when both words match. The identity store must precede the key read because
packet aliases can change that byte.

For command zero, the original reads the event's first word before the saved
identity. Release through `func_1516972C(owner)` if the words match OR the
saved key equals event byte four. A word match skips both key reads. Unsupported
command bytes access neither packet nor saved identity in emitted guest code.
The full incoming A2 word is stored at incoming SP+8 before its low-byte mask.
Guest fault/access-order evidence is not a claim about portable C faults or
invalid-pointer behavior.

## Actual Caller And Registry

The original 74-entry table is `D_8008A8D8`, VROM `0x22F398`, preserved in
`conker/asm/data/22EF80.rodata.s`. Its one target pointer is slot 17 at VROM
`0x22F3DC` / VA `0x8008A91C`. The aligned prepared-image scan finds no encoded
direct JAL sites. `variables.h` already declares the canonical
`void (*)(struct260 *, s32, u8)` callback interface.

Retained `func_15149434` in `src/game/done/game_1765E0.c` is independently
confirmed byte-exact across all 23 words / frame `0x18`, VA
`0x15149434..0x15149490`, ROM `0x1768E4..0x176940`. It loads unsigned selector
byte `+0x13`, retains its negative/range checks, clamps out-of-range indices
to NULL slot zero, and masks A2 before its indirect call. The callback's own
incoming home is at outer incoming SP-16, distinct from the caller's SP+8 home.

No matching original caller ASM filename was found; qualification uses captured
authoritative ROM bytes and the retained C/ELF, not a guessed assembly file.
The caller source, complete caller object, registry and existing helper remain
unchanged and receive no second matching credit. Other event providers are
bounded argument/mutation/clobber contracts, not recovered full executions.

## Checked Normalization

The complete 43-word body and sole `R_MIPS_26` binding to `func_1516972C` are
checked before derivation. Append exactly eleven rows while retaining the old
guard CSV prefix byte-for-byte:

- Words 10, 11, 12, 20 and 22 exchange the retarget path's A0/V1 identity
  roles. Word 20 also commutes its equality comparison operands.
- Words 29 and 30 restore event-before-state load order. Map the event word
  from T2 to V1; word 31 commutes the renamed equality comparison.
- Words 33, 34 and 35 map the following key roles T3 to T2 and T4 to T3.

No instruction is inserted or omitted; no branch displacement or binding moves.
Keep unreachable duplicate-load word 19 literally. All 42 reachable words are
visited, and all 43 body words plus the complete 45-word slot match after the
actual padder and assembler.

- Raw-body SHA-256:
  `c85a7adaeb83153172857e9ba8072d604a6cc280a4d393976cdd93d92eef2f35`.
- Retail 45-word slot SHA-256:
  `f9ee778e70b6e751f4c79bf0c1cdedff3320258dec82f318832e7a9bf78af354`.
- Qualified padded-object SHA-256:
  `f32d5579c9eeaae254ba907dd9c306b385576634dbae284e2e632ad7d65bf457`.

## Qualification

Permanent tools are `experiments/game_record_identity_event_match.py` and
`tests/test_game_record_identity_event_match.py`. Both copies pass eight fresh
pre-install checks, with zero errors, failures, skips or reused checks:
246.932s / 275.552s. Shared tools checks pass in 3.058s / 1.667s.

- 7,168 guest cases cover every command/key byte, nine aliases, two phases,
  full incoming homes and the supported commands' crossed payload cases.
  No-op modes are partitioned because they do not read the payload. Raw C has
  the public semantics; fitted execution preserves complete private state.
- 10,752 original/retained caller cases cover all selector and command bytes,
  all real table entries, NULL/range gates, bounded providers and nested-home
  aliases. This is a partitioned guest corpus, not a full Cartesian claim.
- 32 connected helper cases visit all 28 original and retained release words,
  including late kind reload and callback/fallback paths. Lower providers
  remain bounded contracts, with no new helper credit.
- Native32 O0/O2/O3 with trap UBSan each pass 786,432 target cases and 131,072
  dispatcher cases, twelve effective semantic controls and the actual retained
  release C. Runtime coverage requires all 32 pattern/match pairs for every
  command. Typeless heap-backed fixtures retain the exact callback interface;
  no portable stack-alias or fault behavior is inferred.
- 59 paired fault prefixes, every unsupported command against unmapped fields,
  and actually compiled MIPS early-read, caller-bound and NULL-call negatives
  qualify emitted access and dispatch behavior.
- Reject all 43 raw-word corruptions, binding/extent/history controls and an
  actual padder corruption. Six independent GNU links across three layouts
  rebase the helper call; seven strict-image corruptions fail closed.

Review found an initial native fixture gap: `pattern = command % 8` could not
exercise equal event words at command `0x2D`. The owned run was deliberately
interrupted after its first four checks passed; no incomplete-suite credit was
taken, and no native child remained. The corrected tag-dependent pattern and
runtime coverage assertion passed both full fresh suites. Its incomplete log
is retained separately, not presented as a passing receipt.

After production, both copies pass two fresh installation checks in 11.293s /
3.148s. The six unchanged semantic checks are explicitly reused only after
identical sealed-input, module and qualified-artifact fingerprints, plus exact
production source/object/whole-image identity. They are not called fresh tests.
No test is skipped. These checks do not establish whole-provider gameplay or
hardware acceptance. Zero Claude calls; no provider/configuration changes.

## Production And Image Audit

The normal five-command GLOBAL_ASM Make recipe reproduces all 16 compact owner
functions and the complete padded object. All 15 neighbors, the one handwritten
routine and pools remain fixed. No compiler profile change is needed; inherited
duplicate `generated_12D630` Make warnings remain.

Independent full link and actual production Make agree on exactly 119 changed
ELF bytes: 118 inside the target slot and one target symbol-size byte
(`12 -> 172`). Zero exclusions or metadata permutations. Make exits zero in
16.818s. All 6,054 other linked bodies and every address remain fixed.
Protected Game data stays exact across 720 owners / 189,088 bytes, SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Qualified and adopted ELF SHA-256:
`a3b0f6e3ffbf59a8f0820c12386c5fc9ed1cb25f37b50d512fa26fb7c62f8e35`.
All 16,022 sealed files verify in production and native adoption, with only
four mutable paths: target source, guards, target object and ELF. Link script
and progress CSV remain byte-identical. Preserve the older mirror's 1,638
existing path statuses/hashes and HEAD, adding only the two owned modules.
Do not commit or reset that independently dirty mirror.

## Fresh Progress And Next Work

Actual adopted-native-ELF bytes are captured, streamed back and freshly
recounted with `match_progress.py`; only `func_151B1FAC` leaves the unmatched
queue. The recount exits zero in 5.202s.

| Section | Byte-Exact C | Different | Address Drift |
| --- | ---: | ---: | ---: |
| Total | 3,790 / 5,505 (68.85%) | 1,715 | 0 |
| Game | 3,117 / 4,832 (64.51%) | 1,715 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The threshold remains 4,129 / 5,505: 339 more matches to 75%. The ELF-pinned
queue has 1,586 placeholders, 120 semantic/other entries and nine parser-unlocated
entries. Unchanged source shapes are reused only under strict source and
whole-image identity; the queue is triage, not semantic/ABI qualification.
Next ordinary placeholder is `func_150F1020` in `generated_11C2B0`, 45 words.
Keep existing-C `func_15014094` separate. Existing `Gfx *func_1510D8C0` is a
parser miss, not a missing C body.

Equivalent full target qualification from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_record_identity_event_match -v
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

Use captured guard timestamps/Make inputs, not an unrelated broad rebuild.
The actual recount reads `qualified/live-recount.elf`, identical to the adopted
native ELF. Private runners/receipts live under
`conker/build/game-record-identity-event-match/`.

Root README receives aggregate rows only. The normal code-only commit hook
refreshes Graphify; audit old-node retention explicitly. The parent filters
`tools/`, so separate zero-API-token AST extraction covers the two tools modules
without claiming parent membership. The existing filtered-corpus warning is
not a clean full-corpus re-extraction or proof of old-edge preservation.
No push, host/Release, package or global configuration changes.
