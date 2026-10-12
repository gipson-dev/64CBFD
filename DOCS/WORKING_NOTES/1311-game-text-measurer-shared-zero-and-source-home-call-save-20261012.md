# Game Text Measurer Shared Zero And Source-Home Call-Save - 2026-10-12

## Scope

Continue `func_150428D4` from consumer `e0cd6aba` / tools `615bdc91` and
[Note 1310](1310-game-text-measurer-switch-and-register-hint-provenance-20261012.md).
Previous turn was verified progress. Retail remains 219 words / frame 0x80;
production remains the 199-difference placeholder. Preferred matching seed
`flag-branches-captured` remains 222 / 0x80 / 146, rejected. The new split
source is a qualified lifetime foothold, not a promoted matching seed.
Latest actual match remains `func_15042C40`, Note 1292. No production source,
guard, profile, matching credit, totals or main README change.

## Default And Split Updates

The real font flag is initialized false before the ordinary/space/newline
predicate. Effects can return that existing false value; the final assignment
still computes the real 0/1 font decision. There is no fabricated metric field,
normalizer-derived computed zero or physical-register binding. Both operands'
effectful branches are disjoint, and the tracked source does not modify the
flag inside the unsequenced OR operands.

Returning literal false from the metrics side shortens the named-default
lifetime. Splitting the update into two sequenced statements stores the left
decision before evaluating metrics, rather than keeping only an anonymous
left operand live across the call. The source-home change is measured below,
not attributed to an unobserved exact coloring pass.

```sh
python3 -m tools.experiments.game_text_measurer_default_carrier
python3 -m unittest tools.tests.test_game_text_measurer_default_carrier -v
```

| Tracked Form | Words | Frame | Differences | Saved Data Registers | T0 Call Home |
| --- | ---: | --- | ---: | ---: | --- |
| Whole expression, shared default | 222 | 0x90 | 216 | 9 | SP+0x5C |
| Whole expression, metrics false | 219 | 0x88 | 210 | 8 | SP+0x54 |
| Split, direct font | 218 | 0x80 | 210 | 8 | SP+0x68 |
| Split, local font address | 216 | 0x88 | 182 | 7 | SP+0x6C |
| Split, inline font address | 218 | 0x80 | 210 | 8 | SP+0x68 |
| Split, address after record | 216 | 0x88 | 182 | 7 | SP+0x70 |
| Split, address in font-only block | 218 | 0x88 | 211 | 8 | SP+0x70 |

All seven instruction bodies are distinct; counts do not establish identity.
All fail the retail first-13-word/save-role or frame requirements. The two
0x80/SP+0x68 bodies still hoist the global font address in S5 and preserve
maximum width in S7, adding an eighth save. Seven-save address forms retain
the wrong frame and swapped baseline/maximum roles. Moving the address
declaration shifts homes without solving the complete layout. Emitted pool
families are empty; no absolute internal jump or new data symbol.

Additional ignored scope/scalar/comma/font-object controls are shape screens
only, not newly qualified native/private/owner evidence. Equal-count scalar/
record forms differ in eight stack-home instructions; comma initializer pairs
differ in eleven. Four-byte font-object declaration controls do not remove the
address hoist and are not recovered global types. Do not repeat this matrix or
prefer its smaller/lower-difference forms while discarding lifetime gates.

## Shared Early Zero

Every tracked split form emits the sole `or T0,zero,zero` exactly six words
after the normalizer JAL. Its return prefix contains only integer arithmetic,
then an ordinary non-likely BNE with that reset in its delay slot. Therefore
the slot executes on both branch outcomes before any caller RAM access for
every normalized glyph, not merely on the space path. The static test checks
that prefix and excludes intervening memory operations or calls.

Fired observers confirm T0 zero at the first ordinary text reread, first
space-width read and metrics call in both phases for all five split forms.
The two whole-expression controls still expose stale 50 / 0x5A000008 at the
first reads, while their metrics call sees zero. Observer events/GPRs/FPRs/
memory equal the unobserved model. Removing the split reset only in an ignored
in-memory negative control makes the first-read and public-behavior checks
fail. No padding/production NOP or guard is added. These observations do not
claim complete instruction-fault/GPR/FPR parity for the non-matching bodies.

## Actual Source Home

Fresh complete captures compare the controlled direct-font forms:

| Source | CFE Bytes / Records | UOPT Bytes / Records | R8 Save / CUP / Reload Bytes | Home |
| --- | --- | --- | --- | --- |
| Whole shared default | 18,552 / 838 | 18,216 / 812 | 3600 / 3616 / 3632 | M-52 |
| Whole metrics false | 18,568 / 838 | 18,168 / 809 | 3544 / 3560 / 3576 | M-52 |
| Split direct font | 18,544 / 837 | 18,240 / 814 | 3552 / 3568 / 3584 | M-24 |

The whole forms have four anonymous CFE VREG homes -48,-52,-56,-60, raw
level 1 / length 4. Split has only -48,-52. Its named flag M-24 stores occur
at CFE 1544,1968,2992,4440; the left result at 2992 precedes metrics CUP 3592.
Five metric LDAs are length 20 / base M-44, distinct from that flag home.
UOPT introduces the R8 M-24 save before UGEN; frame 0x80 minus 24 is SP+0x68.
Thus the early reset, frame and actual full-word call-save home are now
recovered together in this source form, but the complete routine is not.

Normal flags/newly owned children only: driver/producers/consumers exit 0;
actual argv, fired initialized-table probe, complete nonempty streams, marker
order/hashes and cleanup are checked. Every capture preserves its normal
text/functions/relocations and union of all pool families. All four prepared
compiler fingerprints remain exact. No compiler edit/rebuild/install, existing
debugger attach, native-memory write, diagnostic flag or failed `-K` reuse.

## Qualification And Bank

Six new tests pass in 31.085 seconds, no skips, including 5,285 public
comparisons across all seven bodies with actual normalizer/metrics helpers.
All-byte/both-phase, null/empty/control/newline/extended, alias/scale,
font-pointer aliasing and finite fractional-factor cases pass. Wrong default,
reset mutation and invalid CLI controls reject. The augmented source-store/
record-home capture test passes separately in 13.467 seconds. Fresh isolated
switch/register regression: six tests in 18.932 seconds, 2,265 comparisons,
no skips. All twelve distinct tests pass, with the focused capture rerun;
7,550 combined public comparisons. No new full private/fired-fault/native/
owner/neighbors/padder/link/rebase match qualification. Earlier full-20
receipts apply only to their unchanged original bodies.

Tools `54c480889266632ec0afe2b3092fe80877e6ec62` is committed first; this note,
five concise indexes, confirmed workflow command and exact consumer pin follow.
CLI, WSL consumer/mounted/older tool checks and Windows py_compile pass.
Existing shared tools are not edited. Older HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a` and all prior 95 task fingerprints
are preserved. Exactly two previously absent files are synchronized and
hash-checked: dirty372 becomes dirty374, with 97 task fingerprints. No older
commit/reset/stash/history duplication, unrelated reversal, OGL/Release/ROM/
save/config/editor change, additional Claude call or push.

Nine frozen production inputs and protected 189,088 bytes / 720 owners remain
unchanged with effective corruption controls. Game stays 2,813 / 4,823 (58.32%),
total 3,486 / 5,496 (63.43%), drift zero; conversion totals/main README remain
unchanged. Final bank requires fresh post-documentation/post-commit immutable
checks, resolved links, clean active repos and the consumer hook's fresh terminal
Graphify Rebuilt receipt with advanced log bytes/UTC and zero workers. Preserve
existing graph/version/scan-size warnings; no force/purge/install.

All 4,548 relative links across eight checked documents resolve. Initial
post-documentation immutable/corruption tests 05/06 pass in 3.111 seconds;
repeat those controls after the final bank.

## Next

Keep the same target and full Game goal active. Carry forward the verified
split early-zero and named M-24 lifetime; do not restart the named-register
hint or whole-expression screens. Recover font-address rematerialization without
another local stack slot or an eighth saved register, then the complete retail
control-flow/219-word layout. Do not pad the 218-word candidate or install it
on partial lifetime evidence. All final private/fired-fault/native/owner/seven-
neighbor/pool/both-padder/independent-link/rebase/literal whole-ELF/data/guard-
prefix gates must pass before installation/totals. `func_150417AC` follows only
after a real match here.
