# Game Text Measurer Address Work Lifetime And Retail Save Roles - 2026-10-12

## Scope

Resume `func_150428D4` from consumer `c55d0099` / tools `54c48088` and
[Note 1311](1311-game-text-measurer-shared-zero-and-source-home-call-save-20261012.md).
Both active repositories were clean; no owned compiler jobs survived the
interruption. Retail is 219 words / frame 0x80, VA 0x150428D4..0x15042C40,
ROM 0x6FD84..0x700F0. Production remains the 199-difference placeholder.
Latest actual match remains `func_15042C40`, Note 1292. The historical
`flag-branches-captured` 222 / 0x80 / 146 seed remains rejected and oversized.
No production source, guard, compiler profile, totals or main README change.

## Disjoint Work Lifetimes

The existing real `extent` word temporarily holds the 32-bit address of the
global font-pointer object. Two pointer reads through that address still
surround the width write; afterward the same word holds the calculated font
height. This reuses an actual address/height lifetime rather than adding a
sixth metric field, computed-zero state or physical-register binding.
Pointer/integer conversions are explicitly qualified for the existing 32-bit
ABI, not claimed portable to arbitrary pointer widths.

```sh
python3 -m tools.experiments.game_text_measurer_work_lifetime
python3 -m unittest tools.tests.test_game_text_measurer_work_lifetime -v
```

| Tracked Form | Words | Frame | Differences | Saved Data Registers | Opening Roles |
| --- | ---: | --- | ---: | ---: | --- |
| Direct-font control | 218 | 0x80 | 210 | 8 | Extra font-address save |
| Integer address work | 216 | 0x80 | 181 | 7 | S5/S6 swapped |
| Forward ordinary work | 217 | 0x80 | 176 | 7 | S5/S6 swapped |
| Forward ternary work | 216 | 0x80 | 171 | 7 | Retail first 13 words exact |
| Excluded-join control | 217 | 0x80 | 120 | 7 | S5/S6 swapped |

All five bodies are distinct and non-installable. Every form retains the
common T0 zero six words after the normalizer JAL, before any caller RAM
access, plus the full-word save/reload at SP+0x68. The four work forms remove
the hoisted saved font address and preserve S0..S6 in retail stack homes.
Their font-address HI16/LO16 pair uses caller-saved V1 instead. Pools are
empty across the union of all pool families; no absolute internal jump.

The forward ternary form additionally recovers baseline S6, maximum width S5,
all first 13 opening words, and opening words 14..27 exactly. This is the
current qualified lifetime foothold: correct seven roles, frame, common zero
and named call home together. It is still three words short and differs in
171 real words. Its backward dispatch joins and one materialized font address
are not retail's full forward dispatch / independent global-address loads.
Do not pad it, normalize a broad block, or grant matching credit.

The 120-difference excluded form contains an identity assignment solely as a
compiler-shape control; it is not recovered source or a preferred matching
seed. Ignored union/qualifier, compact/direct-exit and nested dispatch screens
remain shape evidence only. Nested forms lose the required frame/lifetime;
do not repeat that matrix or use the lower difference count as acceptance.

## Completed Compiler Captures

| Source | CFE Bytes / Records | UOPT Bytes / Records | R8 Save / CUP / Reload Bytes | Home |
| --- | --- | --- | --- | --- |
| Integer address work | 18,816 / 854 | 18,304 / 817 | 3520 / 3536 / 3552 | M-24 |
| Forward ternary work | 18,824 / 861 | 18,264 / 821 | 2768 / 2784 / 2800 | M-24 |
| Excluded-join control | 19,032 / 877 | 18,424 / 834 | 2864 / 2880 / 2896 | M-24 |

Fresh complete captures verify the named false-flag store at CFE byte 1544,
five length-20 metric LDAs at M-44, and real UOPT R8 M-24 save/reload.
Frame 0x80 minus 24 is SP+0x68. Work-address reuse removes the extra save
without displacing that source home. No unobserved coloring-pass cause is
claimed for the ternary's recovered S5/S6 roles.

Normal flags and newly owned compiler children only: driver/producers/
consumers exit 0, actual argv/input paths, fired initialized-table probe,
nonempty complete streams, marker/hash order and cleanup pass. Each capture
preserves its normal text/functions/relocations and all pool-family union;
all four prepared compiler hashes remain exact. No compiler edit/rebuild/
install, existing debugger attach, native-memory write or failed -K reuse.

## Qualification And Bank

Six new tests pass in 41.183 seconds, no skips. They cover 3,775 public
guest comparisons across all five bodies, all bytes/both phases, null/empty/
control/newline/extended input, output/font/factor/scale/text aliases and
finite fractional-factor boundaries with actual normalizer/metrics helpers.
Fired first-read/call observers equal unobserved events/GPRs/FPRs/memory.
Removing the reset and caching the font pointer are effective negative controls.

Native32 passes all five bodies at O2 and O0: 733 cases per body/profile,
7,330 comparisons, four-byte integer/pointer/float checks, actual helpers and
buffer/table canaries. A fresh compiled empty-height mutation fails as
expected. Native runs retain the existing no-strict-aliasing and SSE FP
flags. Synthetic low-address font-pointer aliasing is guest-only; full
private-home/instruction-fault/FCSR/hardware/gameplay parity is not claimed.

Fresh isolated prior default-carrier regression: six tests in 41.285 seconds,
5,285 public comparisons, no skips. All twelve new/regression tests pass;
9,060 combined guest comparisons. One initial new-test assumption wrongly
rejected every first-13-word prefix; inspection proved the forward ternary
exact and the assertion was corrected before the complete passing rerun.

Tools `4cf5203311a072530f8897bc539d7877ff96cad8` is committed first. This
note, five concise indexes, confirmed workflow command and consumer gitlink
follow. CLI, WSL consumer/mounted/older tools checks and Windows py_compile
pass. The independent older checkout's HEAD `ddbdd16b` and all 97 prior task
fingerprints are preserved. Only two previously absent task files are
synchronized and hash-checked: dirty374 becomes dirty376 / 99 fingerprints.
No older commit/reset/stash/history duplication, unrelated reversal, extra
Claude call, OGL/Release/ROM/save/config/editor change or push.

Nine frozen production inputs and protected 189,088 bytes / 720 owners remain
unchanged with effective corruption controls. Game stays 2,813 / 4,823 (58.32%),
total 3,486 / 5,496 (63.43%), drift zero. Final bank requires fresh immutable
tests 05/06, resolved links, clean active repos and fresh terminal Graphify
Rebuilt with advanced log bytes/UTC and zero workers. Preserve existing graph/
version/scan-size warnings; no force/purge/install.

Fresh post-documentation immutable/corruption tests 05/06 pass in 1.429
seconds. All 4,554 relative links across eight checked documents resolve;
repeat immutable controls and verify the final hook after committing.

## Next

Keep the same target and full Game goal active. Start from the qualified
`forward-ternary-work` lifetime, not the rejected extra-save direct form or
lower-difference identity control. Recover retail's forward outer/inner range
dispatch without losing common zero/named M-24, then independent font-address
rematerialization and the complete 219-word body. All final private/fired-fault/
native/owner/seven-neighbor/pool/both-padder/independent-link/rebase/literal
whole-ELF/data/guard-prefix gates remain mandatory before installation/totals.
`func_150417AC` follows only after a real match here.
