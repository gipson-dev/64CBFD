# Game Text Measurer Explicit Assignment And Predicate Boundaries - 2026-10-12

## Scope

Continue `func_150428D4` from consumer `ec97d32e` / tools `01a4cd8f` and
[Note 1308](1308-game-text-measurer-font-controls-and-initializer-call-save-20261012.md).
The previous turn was verified progress, not a wait or an external blocker.
Retail remains 219 words / frame 0x80; production remains the 199-difference
placeholder. Preferred `flag-branches-captured` stays 222 / 0x80 / 146,
rejected. Latest actual match remains `func_15042C40`, Note 1292. No installed
source, guard, profile, matching credit, totals or main README change.

## Assignment Spelling Controls

The earlier named compound flag is loaded after the metrics call. Replacing
`useFont |= predicate` with `useFont = useFont | predicate` is a concrete test
of whether spelling alone changes that snapshot. The new tool retains five
metric fields, the existing owner profile and real flag initialization. All
forms remain non-installable; no fabricated metric field or computed-zero state.

```sh
python3 -m tools.experiments.game_text_measurer_predicate_snapshot --assignments
python3 -m tools.experiments.game_text_measurer_predicate_snapshot --defaults
python3 -m unittest tools.tests.test_game_text_measurer_predicate_snapshot -v
```

| Explicit Assignment Form | Words | Frame | Differences |
| --- | ---: | --- | ---: |
| Named | 226 | 0x90 | 197 |
| Inline address accesses | 230 | 0x90 | 222 |
| Scoped initializer | 227 | 0x90 | 222 |

Named and scoped objects exactly match their respective earlier compound
controls' text/functions/relocations. The inline-address object does not:
36 words differ despite equal counts. Its function/relocation maps and all
pool sections are identical. The initial overbroad identity test failed here;
full comparisons exposed the real difference, and the test now explicitly
checks all 36 positions rather than accepting identity from counts.

Fresh complete compound/explicit-named captures both contain CFE 18,960 bytes /
861 records and UOPT 18,456 / 825. The source flag M-44 first load is at CFE
byte 4760 in compound and 4776 in explicit, after the metrics CUP at 2816.
Neither UOPT output has rstr/rlod. Thus explicit binary spelling alone does not
create the required pre-call register snapshot in these two measured forms.
This is not a claim about all expressions or a specific optimizer deletion pass.

## Separate Boolean And Effects

Three new forms compute the ordinary-glyph Boolean separately from the space,
newline and metrics effects. The right-hand effect dispatch uses the existing
Boolean for newline selection, avoiding another text-byte read. A third form
discards the zero-valued effect result instead of OR-ing it back into the flag.
This is genuine predicate/effect restructuring, not a dummy register dependency.

| Pure Ordinary Predicate Form | Words | Frame | Differences |
| --- | ---: | --- | ---: |
| OR update, direct font | 228 | 0x90 | 220 |
| OR update, local font address | 226 | 0x88 | 221 |
| Discard effect result, direct font | 222 | 0x88 | 214 |

All fail the retail shape/role gates; none replaces the preferred seed.
The discard-effects form spills/reloads T0 at words 77/83, SP+0x58, not
SP+0x68. It saves nine data registers including S8, hoists the space constant
in S6 and the font address in S7, and moves the baseline output to S8.
There is no literal shared `or T0,zero,zero` instruction.

Its isolated space-width read and metrics call do observe T0 zero, but the
first ordinary text-byte reread observes T0=1 where retail observes zero.
The observer fires on `A` in both phases, before that load, and separately
checks space and `AB\n\xA8`. Events/GPRs/FPRs/memory equal the unobserved model;
public memory/calls equal the byte-addressed reference. Therefore neither a
space-only observation nor a zero at the metrics call proves the shared
post-normalizer zero. No new full instruction-fault qualification is claimed.

The discard-effects capture has CFE 18,392 bytes / 829 records and UOPT
18,192 / 813. CFE declares one VREG M-48 at byte 1520, level 1 / length 4.
UOPT emits R8 rstr M-48 at 2984, metrics CUP at 3000 and rlod at 3016.
Frame 0x88 minus 48 maps to SP+0x58. This is a real upstream call-save, not
an inferred UGEN pressure-handler event, but it is still the wrong lifetime.

All three captures use normal flags and newly owned compiler children only.
Driver/producers/consumers exit 0; actual argv, fired initialized-table probe,
complete nonempty streams, marker order/hashes and cleanup are checked.
Text/functions/relocations and the union of all pool families preserve each
normal baseline. All four prepared compiler fingerprints remain exact.
No compiler source/binary edit, rebuild, installation, existing debugger attach,
native memory write, diagnostic compiler flag or failed `-K` reuse.

## Qualification And Bank

Six new tests pass in 26.729 seconds, no skips. All six distinct bodies pass
4,530 public comparisons with the actual normalizer and metrics helpers,
including all bytes in both phases, null/empty/control/newline/extended cases,
aliases/scales, font-pointer aliasing and a finite fractional factor. Wrong
space-width, mutually exclusive modes and cross-mode filter controls reject.
Fresh isolated prior font-control regression: six tests in 16.382 seconds,
2,265 comparisons, no skips. All twelve tests pass; 6,795 combined comparisons.
No new full private/fired-fault/native/owner/neighbors/padder/link/rebase match
qualification. Earlier full-20 receipts apply only to unchanged original bodies.

Tools `54ded39c2315d5fb3f9949414f90c80424513e38` is committed first; this note,
five concise indexes, confirmed workflow command and exact consumer pin follow.
Both CLI modes run successfully. WSL consumer/mounted/older tool checks and
Windows py_compile pass. Existing shared tools are not edited.

Older tools HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` remains unchanged.
All 91 prior task fingerprints are preserved; exactly two previously absent
files are synchronized and hash-checked. Dirty368 becomes dirty370, with 93
task fingerprints recorded. No older commit/reset/stash/history duplication,
unrelated reversal, OGL/Release/ROM/save/config/editor change, additional Claude
call or push.

Nine frozen production inputs and protected 189,088 bytes / 720 owners remain
unchanged with effective corruption controls. Game stays 2,813 / 4,823 (58.32%),
total 3,486 / 5,496 (63.43%), drift zero; conversion totals/main README remain
unchanged. Final bank requires fresh post-documentation and post-commit immutable
checks, resolved links, clean active repos and the consumer hook's fresh terminal
Graphify Rebuilt receipt with advanced log bytes/UTC and zero workers. Preserve
existing graph/version/scan-size warnings; no force/purge/install.

All 4,536 relative links across eight checked documents resolve. Initial
post-documentation immutable/corruption tests 05/06 pass in 1.488 seconds;
repeat those controls after the final bank.

## Next

Keep the same target and full Game goal active. Do not repeat these six source
forms or infer that all C is exhausted. Preserve the correct ordering: shared
T0 zero must precede the ordinary text-byte reread as well as the space-width
read; an eagerly materialized true ordinary predicate violates that boundary.
Use the operand-aware records to recover the anonymous/default-zero merge
without creating extra constant/font-address saved lifetimes. The complete
219/frame0x80/seven-role/SP+0x68 routine and all final private/fired-fault/native/
owner/seven-neighbor/pool/both-padder/independent-link/rebase/literal whole-ELF/
data/guard-prefix gates must pass before installation or totals.
`func_150417AC` follows only after a real match here.
