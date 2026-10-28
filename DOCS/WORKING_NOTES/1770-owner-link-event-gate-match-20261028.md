# 1770 - Owner Link Event Gate Match - 2026-10-28

The adopted Native ELF measures **3,848/5,506 exact C functions (69.89%)**,
Game **3,175/4,833 (65.69%)**, zero address drift and 1,658 different.
Only `func_150D596C` gains matching credit. The 75% target remains 4,130
functions, requiring **282 more** at the unchanged denominator.

## Recovered routine and interface

`func_150D596C`, in `generated_1028F0.c`, occupies VA
`0x150D596C..0x150D5A2C`, ROM `0x102E1C..0x102EDC`: all 48 words,
a 24-byte frame and one `R_MIPS_26:func_1516972C` binding at +88.
The complete semantic body replaces its zero-return placeholder. Reuse the
owner-local `EmbeddedOwnerLink` and `OwnerLinkEvent` views and the existing
release declaration without shared-header or compiler-profile changes.

The actual callback interface is `void(struct260 *, s32, u8)`. The initial
private u8-pointer draft was corrected after tracing the real registration.
Index 40 of the 74-entry `D_8008A8D8` table contains this callback at
VA `0x8008A978`, ROM `0x22F438`; this is the only retail pointer literal.
There are no direct JAL/J sites. The complete original and current 23-word
`func_15149434` dispatcher masks the command byte, reads unsigned owner
selector +0x13, clamps selectors 74..255 to slot zero and skips NULL entries.

Commands 0, 3 and 0x2F release the actor when the event first pointer equals
the embedded owner pointer, or the saved identity equals event byte +4.
That identity byte overlaps the second event pointer; preserve the retail
read, not event byte +8. Command 0x2D retargets first-to-second or
second-to-first with first-match priority. Each pointer store precedes its
identity read at event +9 or +8, which matters when packet and link overlap.
Other commands perform no owner or event loads in emitted guest code.
The original unused instructions at +104 and +152 remain present.

## Derived guards and complete owner

Four expected-word guards at +116, +120, +156 and +164 exchange the current
and first-pointer register roles and commute a symmetric comparison.
The first comparison at +124 is unchanged by exchange plus commutation.
No instruction, immediate, frame word or binding is inserted or omitted.
This is guarded C matching; the raw compiler output has four differences.

All 16 neighboring functions and their raw/padded pools are unchanged,
including six GLOBAL_ASM routines. The actual generated-owner Make recipe
runs five commands: preprocess, normal O2/g3 compile, postprocess, pad and
assemble. Its complete padded object equals the independent qualified object.

The strict image prediction permits exactly 134 changed bytes: 133 target
code bytes and one target symbol-size byte (12 to 192), with zero exclusions
or metadata reorder. Production reproduces that exact image. All 6,056
disassembly addresses, all 6,055 other bodies, named ELF definitions, the map
and C inventory remain fixed. All 720 Game data owners / 189,088 bytes remain
exact. The inherited duplicate generated_12D630 Make warning is unchanged.

## Behavioral qualification

Both tools copies pass eight fresh canonical methods and shared tools checks.
After production, each copy runs two fresh installed checks and reuses six
semantic checks only through exact source/module/input/artifact fingerprints.

- 12,288 guest cases cover every command and identity byte, nine alias layouts,
  high command bits, full incoming homes and complete supported-command
  pattern/match/key/alias combinations. Raw C public state agrees; normalized
  complete state agrees. All 46 reachable words are visited; all 48 literal
  words are checked.
- 13,568 original/current dispatcher cases cover every selector and command
  byte, every table entry, clamp/NULL behavior and aliases. They include
  2,324 actual target calls, and visit every caller word.
- 96 cases execute all 28 original/current release-helper words and verify
  the kind reload after bookkeeping mutation. Lower callbacks and other
  table providers remain bounded contracts and receive no new matching credit.
- Native32 O0/O2/O3 each pass 786,434 target and 131,072 dispatcher cases,
  including actual C dispatcher/release bodies, trap UBSan and 12 effective
  compiled semantic negatives. Heap-backed pointer storage, the canonical
  function-pointer type, disabled strict aliasing and aligned startup are explicit.
- 118 fired guest fault-prefix pairs compare complete states. Ignored commands
  need no owner/event mapping. These qualify emitted guest order, not portable
  C access-fault behavior or hardware/gameplay acceptance.
- Nine independent GNU links across three layouts verify rebased calls and
  18 execution cases. All 48 raw-word corruptions, binding/extent/history/real
  padder controls and six complete-image corruptions reject changed evidence.
  Four actual IDO negatives detect omitted release commands, wrong identity
  byte and premature owner reads.

Private fixture corrections are retained: the preparation extent assertion was
fixed to 192 bytes; stale native compiler outputs are no longer transported
over newer completed cache results; the native callback typedef was corrected
to struct260; and pointer values now vary the overlapping identity byte so
the early-read negative is effective. Final canonical executions use the
corrected source and fixtures; failed drafts receive no credit.

## Banked evidence and continuation

Baseline consumer `ef60bf0c`, tools `1387bd0`. The new tools commit is
`835f52a4b78e6a7513a136a9297b9d69bad73c6c`; tools are committed first.
The seal verifies 16,281 current inherited/owned files and 282 focused inputs.
Preserve all 1,751 inherited dirty mirror paths, adding only three target
modules there; do not commit that independent mirror or publish either repo.

| Artifact | SHA-256 |
| --- | --- |
| Adopted ELF | `770078348fa22c34f67079f94cf823adb8a7129f6ebc28e5340c0ee01d518d10` |
| Padded owner | `a717517d43873dc91c830f0eeb02414f9b9e5cdcede0dbba47669ca6b179f01e` |
| Recovered source | `61f4ef9feabf4222f04b482471575818bc4ce6c0d6f769d2165bd72df96b0eee` |
| Guard CSV | `20131e428c071ea6d2cbee21968f122274bc71fb167a2a356b3033ff5582f8b9` |
| Raw 48 words | `d4442fb858a37b234ea807400e9ce1acc999e674e2de2379a73230d283a0cc95` |
| Normalized original object | `7e7606c0922c47e7d1d66e805019056484411f8c944e0669f9acd9eb8d7583f1` |

Scoped Graphify closeout refreshes the eleven changed C/Markdown/tool files.
The retention gate must account for all 45,837 old nodes and 93,980 old
relationship contexts, retiring only the target placeholder false s32 return.
Outside-scope manifest rows and global analytics remain historical; this
is not a full-corpus extraction.

Next inspect `func_151A5070` in `generated_1D0840`. The remaining queue has
1,529 placeholders, 120 semantic/other definitions and nine unlocated screens;
it is triage only. `func_1514E920` stays parked and uncredited. Keep the 75%
goal open. Routine Claude calls: zero. Host Release remains frozen.

Prepared-checkout command:

```sh
python3 -m unittest tools.tests.test_game_owner_link_event_gate_match -v
```
