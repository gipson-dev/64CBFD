# Game Text Measurer Switch And Register-Hint Provenance - 2026-10-12

## Scope

Continue `func_150428D4` from consumer `32a3c84d` / tools `54ded39c` and
[Note 1309](1309-game-text-measurer-explicit-assignment-and-predicate-boundaries-20261012.md).
Previous turn was verified progress, not a wait or an external blocker.
Retail remains 219 words / frame 0x80; production stays the 199-difference
placeholder. Preferred `flag-branches-captured` remains 222 / 0x80 / 146,
rejected. Latest actual match remains `func_15042C40`, Note 1292. No installed
source, guard, profile, matching credit, totals or main README change.

## Five-Field Statement Controls

The new generator removes the old captured sixth flag field and its explicit
stores/loads. It retains five real metric fields and the original statement
flag initialization. New controls switch the newline/glyph dispatch separately
and together, then test an explicit `register` flag and its lexical scope.
These are not repetitions of the earlier six-field captured glyph switches.
All use the owner profile and remain non-installable.

```sh
python3 -m tools.experiments.game_text_measurer_switch_flags
python3 -m unittest tools.tests.test_game_text_measurer_switch_flags -v
```

| Statement Form | Words | Frame | Differences |
| --- | ---: | --- | ---: |
| Five-field if reference | 216 | 0x80 | 204 |
| Newline switch | 216 | 0x80 | 203 |
| Glyph switch | 216 | 0x80 | 203 |
| Both switches | 216 | 0x80 | 204 |
| Unscoped register flag | 216 | 0x80 | 204 |
| Scoped register flag | 217 | 0x80 | 212 |

Six forms produce three distinct instruction bodies. Both-switches and
unscoped-register objects exactly equal the if reference's text/functions/
relocations. The two individual switches exactly equal each other. They differ
from the reference at fourteen word indices:
1,8,10,18,20,101,103,115,124,127,165,168,195,204. Function/relocation maps remain
equal. The scoped-register form is a third distinct body. Emitted pool families
are empty, including small/literal/BSS families; no absolute internal jump.
Equal frame or difference counts are not a match or a substitute for word checks.

Every form saves S0 through S7, eight data registers rather than seven.
All initialize the named flag in S4 in the normalizer-call delay slot at word
39. None emits the shared T0 zero or any T0 stack save/reload. The ordinary
text reread on `A` sees T0=50, versus retail zero; the space-width read sees
0x5A000008, versus zero. On `AB\n\xA8`, the metrics call sees T0=50 while S4
holds the real zero flag. These are fired observations in both phases for
all three distinct bodies, not inference from a missing probe or spill opcode.
The observer preserves the unobserved model's events/GPRs/FPRs/memory, and
public memory/calls equal the byte-addressed reference. No new full instruction-
fault qualification is claimed. The 216-word count is not license to pad the
missing words or promote the wrong saved-register lifetime.

## Literal Register-Hint Records

Fresh complete CFE/UOPT captures qualify the named register hint itself:

| Source | CFE Bytes / Records | UOPT Bytes / Records | Literal CFE VREG |
| --- | --- | --- | --- |
| Plain if reference | 18,592 / 853 | 18,216 / 828 | None |
| Unscoped register | 18,608 / 854 | 18,216 / 828 | Byte 216, M-44, raw level 0 / length 4 |
| Scoped register | 18,632 / 857 | 18,256 / 832 | Byte 1560, M-48, raw level 0 / length 4 |

Unlike the earlier merely printed UOPT variable-table suffix, these are actual
CFE VREG opcodes. The unscoped hint changes the complete CFE stream, but its
complete UOPT stream is byte-identical to the plain reference. All three UOPT
outputs have no VREG/rstr/rlod records. The hint therefore does not create an
R8 call-save in these measured statement forms. Neither scope nor the keyword
recovers the required lifetime.

The decoder's raw `level` field is 0 for both user-register declarations.
Earlier anonymous expression-temporary controls have raw level 1 and real R8
saves. Keep these record classes distinct; the field's full semantic role and
the precise eligibility/coloring pass are not established by this comparison.
Do not label it lexical nesting or turn the observed difference into a compiler
edit, stream-header patch or physical-register workaround.

All diagnostics use normal flags and newly owned compiler children only.
Driver/producers/consumers exit 0; actual argv, fired initialized-table probe,
complete nonempty streams, marker order/hashes and cleanup are checked.
Normal text/functions/relocations and the union of all pool families remain
identical per capture. All four prepared compiler fingerprints remain exact.
No compiler source/binary edit/rebuild, installation, existing debugger attach,
native memory write, diagnostic compiler flag or failed `-K` reuse.

## Qualification And Bank

Six new tests pass in 19.217 seconds, no skips, including 2,265 public
comparisons across the three distinct bodies with actual normalizer/metrics
helpers. All-byte/both-phase, null/empty/control/newline/extended, alias/scale,
font-pointer aliasing and finite fractional-factor cases pass. Wrong newline
and invalid CLI controls reject. Fresh isolated predicate-snapshot regression:
six tests in 28.330 seconds, 4,530 comparisons, no skips. All twelve tests pass;
6,795 combined comparisons. No new full private/fired-fault/native/owner/
neighbors/padder/link/rebase match qualification. Earlier full-20 receipts
apply only to their unchanged original bodies.

Tools `615bdc9183344468ed2b691a0b2594a92e1ba590` is committed first; this note,
five concise indexes, confirmed workflow command and exact consumer pin follow.
The CLI, WSL consumer/mounted/older tool checks and Windows py_compile pass.
Existing shared tools are not edited.

Older tools HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` remains unchanged.
All 93 prior task fingerprints are preserved; exactly two previously absent
task files are synchronized and hash-checked. Dirty370 becomes dirty372, with
95 task fingerprints recorded. No older commit/reset/stash/history duplication,
unrelated reversal, OGL/Release/ROM/save/config/editor change, additional Claude
call or push.

Nine frozen production inputs and protected 189,088 bytes / 720 owners remain
unchanged with effective corruption controls. Game stays 2,813 / 4,823 (58.32%),
total 3,486 / 5,496 (63.43%), drift zero; conversion totals/main README remain
unchanged. Final bank requires fresh post-documentation/post-commit immutable
checks, resolved links, clean active repos and the consumer hook's fresh terminal
Graphify Rebuilt receipt with advanced log bytes/UTC and zero workers. Preserve
existing graph/version/scan-size warnings; no force/purge/install.

All 4,542 relative links across eight checked documents resolve. Initial
post-documentation immutable/corruption tests 05/06 pass in 1.393 seconds;
repeat those controls after the final bank.

## Next

Keep the same target and full Game goal active. Do not repeat these six forms
or infer that all C is exhausted. A literal source-register VREG with raw level
0 is not interchangeable with the anonymous temporary's level-1 record; follow
the actual default-zero/anonymous predicate merge rather than applying another
named register hint. Preserve early zero before both ordinary text reread and
space-width read without extra saved flag/constant/font-address lifetimes.
Recover the complete 219/frame0x80/seven-role/SP+0x68 routine before all final
private/fired-fault/native/owner/seven-neighbor/pool/both-padder/independent-link/
rebase/literal whole-ELF/data/guard-prefix gates and installation/totals.
`func_150417AC` follows only after a real match here.
