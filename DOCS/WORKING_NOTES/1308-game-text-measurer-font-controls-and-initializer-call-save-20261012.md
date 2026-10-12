# Game Text Measurer Font Controls And Initializer Call-Save - 2026-10-12

## Scope

Continue `func_150428D4` from consumer `e162b75d` / tools `b3d042d7` and
[Note 1307](1307-game-text-measurer-wire-operands-and-source-marker-provenance-20261012.md).
Retail remains 219 words / frame 0x80. Production remains the 199-difference
placeholder; preferred `flag-branches-captured` remains 222 / 0x80 / 146,
rejected. Latest actual match remains `func_15042C40`, Note 1292. No production
source, guard, compiler profile, matching-credit or root README change.

## Reproducible Font Controls

`game_text_measurer_font_controls.initializer()` reconstructs the earlier
ignored direct-font, scoped carrier initializer from the existing source
generator. It uses five metric fields and one real font predicate; no fabricated
sixth metric field or computed-zero state. The four new declarations are
diagnostic controls, not recovered types or evidence that the font is volatile.
All use the unchanged owner compiler profile and remain non-installable.

```sh
python3 -m tools.experiments.game_text_measurer_font_controls
python3 -m unittest tools.tests.test_game_text_measurer_font_controls -v
```

| Font Declaration Control | Words | Frame | Differences |
| --- | ---: | --- | ---: |
| Plain pointer / plain bytes | 219 | 0x80 | 208 |
| Volatile pointer / plain bytes | 223 | 0x80 | 216 |
| Plain pointer / volatile bytes | 219 | 0x80 | 208 |
| Volatile pointer / volatile bytes | 223 | 0x80 | 216 |

The generated controls reproduce the earlier ignored objects' complete text,
function maps and relocation maps. There are three distinct instruction bodies,
not two. Plain and volatile-bytes objects are exactly identical. The two
volatile-pointer forms have equal function/relocation maps but differ at eleven
word indices: 146,147,150,151,152,153,158,159,160,161,162. Fixed full-text hashes
and explicit comparisons guard this distinction instead of deduplicating counts.
The union of object pool families is empty, including small/literal/BSS families.

Every form still saves S0 through S7: eight registers, not retail's seven.
The opening 13 words differ. The global font address remains hoisted at words
32/33, using S5 in the plain form and S3 in the volatile-pointer forms. In the
ordinary-glyph fixture, the latter make four global pointer reads rather than
two. Volatile pointer qualification changes reads and roles, not the required
saved-register lifetime. Do not install these declarations to suppress a hoist.

## Actual Flag Boundary

All four emit T0 zero only at word 54 in the space path, save it at word 93
to SP+0x68 and reload it at word 99 before the metrics width write. On
`AB\n\xA8`, T0 at the metrics call is zero in both phases. Unlike the earlier
direct-font layout control, this is not the positive previous-line maximum.
However, on the isolated space fixture the first width read sees T0 0x5A000008,
where retail sees zero. The required shared post-normalizer early zero is still
missing. The observer fires in both phases and preserves the plain model's
events, registers, floating registers and memory in its noninterference checks.
This is a bounded register observation, not new full fired-fault qualification.

The complete plain-initializer CFE/UOPT capture qualifies the actual call-save:

| Stage | Bytes | Records | Relevant Records |
| --- | ---: | ---: | --- |
| CFE | 18,520 | 834 | VREG M-48 at byte 1520; M-52 at 1536, level 1 / length 4 |
| UOPT | 18,232 | 813 | R8 rstr M-24 at 3544; metrics CUP at 3560; rlod at 3576 |

With frame 0x80, M-24 maps to SP+0x68. The UOPT stream already contains the
save/reload before UGEN; this is not attributed to a new UGEN pressure-handler
event. It does not explain the exact source eligibility/coloring pass or solve
the shared-zero merge. No inference that all C forms are exhausted.

The diagnostic uses normal compiler flags and newly owned children only.
Driver/producers/consumers exit 0; initialized-table probe, actual argv,
nonempty complete streams, hash-bound marker order and cleanup are checked.
Text/functions/relocations and all pool families match its normal baseline;
that baseline also matches the independently compiled plain control. All four
prepared compiler fingerprints remain exact. No compiler edit/rebuild, existing
debugger attach, native memory write, package install or failed `-K` reuse.

## Qualification And Bank

Six new tests pass in 21.053 seconds, no skips, including 2,265 public
comparisons across the three distinct bodies with actual normalizer/metrics
helpers. Tests include null/empty/control/newline/extended bytes, aliases,
scales, font-pointer aliasing and a finite fractional factor. Effective wrong
space-width and invalid CLI controls reject. Fresh isolated frontend regression:
nine tests in 56.691 seconds, no skips, including its existing 3,020 public
comparisons and diagnostic corruption controls. All fifteen tests pass.
No new full private/native/owner/neighbors/rebase/padder or matching evidence;
earlier full-20 receipts apply only to their unchanged original bodies.

Tools `01a4cd8f4d65ecd84fa03c4547ffbe1e9bf36376` is committed first; this note,
five concise indexes, confirmed workflow command and exact consumer gitlink
follow. WSL consumer/mounted/older tool checks and Windows py_compile pass.
Direct native Windows tool checks fail with WinError 193 because mkrawobject
is a Linux binary; use the existing WSL recipe, not a helper replacement.

Older tools HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` stays unchanged.
All prior 89 task fingerprints are preserved. Exactly two previously absent
task files are synchronized and hash-checked; dirty366 becomes dirty368,
with 91 task fingerprints now recorded. No older commit/reset/stash/history
duplication, unrelated work reversal, OGL/Release/ROM/save/config/editor change,
additional Claude call or push.

Production source, ELF, guards and Makefile hashes remain exact. Nine frozen
inputs and protected 189,088 bytes / 720 owners remain unchanged with effective
corruption controls. Game stays 2,813 / 4,823 (58.32%), total 3,486 / 5,496
(63.43%), drift zero; conversion totals and root README stay unchanged.
Final bank requires fresh post-documentation immutable controls, checked links,
clean active repos and the consumer's fresh terminal Graphify Rebuilt receipt
with advanced log bytes/UTC and zero workers. Keep existing graph warnings;
no force/purge/install.

All 4,530 relative links across eight checked documents resolve. Initial
post-documentation immutable/corruption tests 05/06 pass in 1.544 seconds;
repeat them after the final bank as an independent close-out control.

## Next

Keep the same target and full Game matching goal active. Track the anonymous
predicate's shared default-zero merge separately from global-address hoisting:
the current initializer has the real SP+0x68 call-save but still lacks early
T0 zero and seven saved roles. Do not repeat these four qualifier screens or
promote 219/frame0x80 shape alone. Recover the complete retail lifetime before
all final private/fired-fault/native/owner/seven-neighbor/pool/both-padder/
independent-link/rebase/literal whole-ELF/data/guard-prefix gates and installation.
`func_150417AC` follows only after a real match here.
