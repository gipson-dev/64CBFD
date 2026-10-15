# Counter Preset Guarded Match

Date: 2026-10-15. Finish the private/emission gap from
[Note 1401](1401-counter-preset-semantic-recovery-and-private-schedule-gap-20261015.md)
without narrowing the full additional-source / Game objective.

## Result

Replace `func_1516EED4`'s zero-return stub with the recovered four-input void
counter-gated factory preset in `conker/src/game/generated_19A8B0.c`.
**All 84 linked words / 336 bytes are byte-exact**, VA `0x1516EED4`, ROM
`0x19C384`, frame `0xD0`. Raw semantic C remains **85 words / 76 positional
differences**. This is a **guarded match**, not direct raw C matching.

Preserve the original signed slot < 4 gate, unsigned counter-byte load,
signed-word threshold and counter clear before allocation, including null
allocation. Preserve the complete 49-word packet, full slot/last inputs and
unsigned low flag byte. Use the existing scalar global declaration privately;
no shared header or caller prototype is changed. Keep the address-based name
and concise semantic/guard comment. The archived caller ignores the result;
no whole-caller or gameplay qualification is claimed.

## Closed Compiler Normalization

The compiler emits the complete semantic routine. Normalize only its known
index/register lifetime, without copying a retail instruction body into C:

- **35 register-allocation replacements** apply the closed ten-register cycle
  `8 -> 25 -> 24 -> 15 -> 14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8`.
  Preserve the opening T6 index lifetime before its later register cycle.
- **One branch displacement adjustment** crosses the omitted word.
- **One guarded omission** removes the redundant incoming-index load at raw
  +0x28. The following pointer add becomes the retail branch delay, including
  the rejected path's V0 pointer value. Frame, saved RA and argument homes are
  unchanged; the final actor-word store remains in the call delay slot.
- **One identity call-binding guard** preserves the unchanged JAL relocation.
  All three table-HI16/LO16 and callee bindings are explicitly checked.

Append **38 expected-word rows** mechanically from the validated compiler
object. Preserve every byte of the old mixed-line-ending CSV prefix. No
profile, volatile declaration, inline assembly, semantic field or FP guard
is introduced. `normalize` rejects unknown complete raw words or relocations;
the production padder also rejects stale physical guard words/bindings.

Raw target SHA-256:
`898c7e35028b16b935e6af23ea92bebb10b329ea42d5ebcac359af50c57f00a0`.
Raw relocations are +0x18 HI16 / +0x1C LO16 for `D_800DD2A0`, and +0x13C
R_MIPS_26 for `func_1516D99C`; the latter moves to +0x138 after omission.
The old unguarded recovery and strict direct-match rejection remain intact.

## Fresh Qualification

**All 14 installed checks pass in 138.988 seconds**:

- **3,240 paired guest cases**, 1,386 accepted / 1,854 rejected, now match
  complete registers, private RAM/stack, memory/call events, LO, FP values/
  condition, visited instructions and provider observations. Cover two stack
  phases, three provider clobber modes and signed slot/threshold boundaries.
  All 84 words are visited; rejected paths do not read the counter byte.
- **138 paired fired guest-memory fault prefixes** match literally, including
  partial state. Every injected fault fires. This qualifies emitted guest
  ordering, not portable C fault semantics or hardware behavior.
- **40,960 native32 cases per O2/O0 profile** execute the same C body over
  all 256 counter bytes, ten signed thresholds and eight genuinely backed
  indices. The capture provider checks all 49 words and pre-call clear;
  real narrow-field factory storage is qualified separately below.
- **Ten effective compiled guest/native negatives** remain unguarded and
  all fail the semantic checks. Normalization rejects every altered body;
  guards cannot conceal a changed predicate, width, clear or packet constant.
- Three **independent original/normalized text, table and call rebases** match
  all 84 words across signed-low carry boundaries. **24 full-private aliases**
  cover incoming homes, outgoing storage and a preserved saved-RA byte.
  These are backed synthetic guest fixtures, not actual game-index validity
  or portable C alias claims.
- **128 actual current factory/allocator-chain pairs** match full private
  states: 85 rejected, ten null and 33 registered. Execute the real 125-word
  factory and 28-word allocator wrapper from the current linked ELF. Verify
  initialized record fields and provider-entry counter clear. Lower heap/
  registration providers remain modeled; the current chain uses no inverse.
- Reject all **85 raw-word flips**, nine relocation changes, **38 stale
  physical guard words**, three physical binding changes and every one of
  the **38 appended guard-row mutations**. Preserve all 29 owner neighbors,
  raw sizes/bytes, pools and relative relocations.
- Validate all **52 production input states**, 52 immutable-before capture
  corruptions, all three exact successor inputs/captures, source-text and
  six physical code/symbol/provider/counter-binding/data corruption controls.
  Freshly verify all **801 original archive fingerprints**.

Reuse existing compiler, parser, padder, oracle, native32 and factory helpers;
no shared helper is edited. Prior unchanged suites and the 27-recipe source
screen remain historical receipts, not fresh tests here. Zero additional
Claude calls; retain the independently reconciled prior advisory in Note1401.

## Whole Linked Image And Progress

Predict the complete **3,257,636-byte ELF before installation** from the frozen
predecessor plus the original 336-byte target slot and symbol size `12 -> 336`.
The normal build equals that independent prediction byte-for-byte. Exactly
**252 bytes change**, all target slot/extent; **every other ELF byte is fixed**.
There are **zero metadata allowances** or ignored symbol sections.

The guard CSV is a shared build dependency, so the normal build recompiles
many existing owners and reports their existing SDK/type/profile warnings.
Do not repair unrelated sources or claim a warning-free whole build. The
isolated target compilation has zero diagnostics, and the complete image
audit closes the broader rebuild. The existing generated_12D630 duplicate
recipe warnings remain unchanged.

Of the 52 scoped inputs, only **ELF, owner and guards change**; **49 remain
fixed**, including progress rows, shared headers, original assembly and
configuration. The complete old guard prefix and **189,088 protected bytes /
720 owners** remain exact. This replaces an already-C-classified stub, so
converted counts/bytes do not increase.

| Installed Input | SHA-256 |
| --- | --- |
| ELF | f518dfd60ad98bd67a7eb72b5b92f29178586f207c0bf8b97656853b6f62b863 |
| Owner | ebe9a969fed7f6c9221332825d93709d2c70c0f8ce541c585161b5fe06738059 |
| Guards | 2a06a351699d625848c5022a68442a34333fc2f67c24409bd5fc465f38c996ff |

Fresh official matcher: **Game 2,898/4,828 (60.02%)**, **total 3,571/5,501
(64.92%)**, **1,930 different**, zero drift. Init remains 492/492 and Debugger
181/181 exact. These percentages are among converted functions, not overall
gameplay completion. Root README changes only the two affected aggregate rows.

## Banking And Next Work

Bank tools **a4ac643** before the consumer source/guards/pin/docs. Shared tool
checks and four-file Windows syntax pass. Preserve independent mirror ddbdd16
and all **665 initial dirty fingerprints**; copy only four absent owned paths
for **669 final paths**. Its standalone ROM-free compiler-gate check passes.
Do not commit/reset that older mirror or copy history into it.

The full Graphify update refuses **19,408 nodes against 41,187** and retains
19,398 nodes from 2,972 excluded-but-present files. Preserve that fail-closed
result; do not force a smaller graph or install an update. Await the actual
incremental commit workers. No push, host source/build/launch, account change,
software install or frozen Release operation.

Ignored evidence: `conker/build/game-counter-preset-match/`. Reproduce from
the prepared WSL consumer root:

```sh
python3 -m tools.experiments.game_counter_preset_match
python3 -m unittest tools.tests.test_game_counter_preset_match tools.tests.test_game_counter_preset_match_installed -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

Next recover **func_1516F024**, **103 words / 412 bytes**, ROM `0x19C4D4`,
frame `0x68`, in the same owner. Inspect its four local table copies with
partial-word tails, actual byte/halfword fields, full-word clamp before byte
stores, and two real helper interfaces. Do not import the archive's `void *`
locals, uninitialized `sp`, wrong field widths or premature byte accumulator
truncation as valid C. No next-function candidate is installed here.

Retain the inherited-stack renderer deferral and full
[failed-comment/binding/unanchored queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md).
The earlier 1,717-object audit is not rerun or reclassified as fresh evidence.
The complete additional-source / Game objective remains open.

## Post-Bank Verification

Consumer **be0f980a** banks source, guards, README aggregates, working docs
and the tools a4ac643 pin. All **14 post-bank checks pass in 50.628 seconds**,
including the whole independent image, all 52 input states, all 801 archive
hashes, every appended guard mutation and exact successor-capture controls.
Normal ELF/progress build is up to date. Raw C remains 85/76; all 84 linked
words are exact only with the documented 38 guards.

Both active checkouts are clean before this receipt edit. Recheck mirror
ddbdd16: all **669 final fingerprints** remain fixed, all **665 initial dirty
files** are preserved and all four owned copies equal active tools. Seven
documents resolve **5,009 relative links with zero broken**. The source
commit's actual incremental workers finish at **41,196 nodes / 81,291 edges /
3,799 communities**, without forcing the refused smaller full scan. No live
test/build/graph handle from that checkpoint remains. Continue func_1516F024
and the full source/Game queues; no whole-goal or gameplay completion claim.
