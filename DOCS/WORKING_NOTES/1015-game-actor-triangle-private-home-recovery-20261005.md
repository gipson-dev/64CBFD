# Game Actor Triangle Private Home Recovery

Date: 2026-10-05. Starting checkpoint: `e621196a`.

Follow [Note 1014](1014-game-actor-triangle-lifetime-and-overlapping-range-audit-20261005.md)
on `func_1502F490`. A mixed scalar/array declaration order recovers the
original homes of **all seven private arrays**, without changing their sizes
or the recovered operations. The installed default IDO form improves from
**275 to 273 differing words**. It remains **non-matching**: 298 body / 302
slot words, frame 0x160 versus retail 0x138. Four ordinary trailing slot NOPs
remain supplied by the existing padding tool; no artificial body padding,
instruction guards, compiler profile or assembly restoration is added.

## Production Change

[generated_58F80.c](../../conker/src/game/generated_58F80.c) changes only the
function's declarations. The ID cache, unsigned interval/first-match scan,
ordered buffer/source gates, six matrix calls, fresh second-source load,
float evaluation order and aliased coordinate updates are unchanged.

| Private Array | Retail And Installed Home | Size |
| --- | ---: | ---: |
| Vertices | SP+0xF4 | 12 bytes |
| Matrix indexes | SP+0x114 | 12 bytes |
| Six XYZ points | SP+0xAC | 72 bytes |
| Two first edges | SP+0x94 | 24 bytes |
| Two second edges | SP+0x7C | 24 bytes |
| New blend | SP+0x120 | 12 bytes |
| Old relative coordinates | SP+0x12C | 12 bytes |

The six SDK output triples start at +0xAC/+0xB8/+0xC4/+0xD0/+0xDC/+0xE8.
Their private addresses are recorded at real seven-argument call sites,
not guessed from frame size. A separate write-history comparison identifies
relative Y at +0x130 (5.5f then 1.25f) and blend Y at +0x124 (1.25f once)
in both retail and installed traces. Their equal final vectors alone would
not distinguish the arrays.

The earlier capacity-eight hypothesis is unnecessary: vertices remain
capacity **three**. Pass/axis and three weight locals account for the
20-byte inter-array declaration gap; this is a current compiler-placement
control, **not a claim of original variable names or declarations**.
Ten other scalar/pointer declarations precede the arrays. Their reserved
homes leave the frame 40 bytes too large. All seven array homes now agree;
the frame, several register lifetimes and instruction schedule still do not.

## Reproducible Controls

[Home driver](../../tools/experiments/game_actor_triangle_home_candidates.py)
contains **25 declaration controls** and **11 loop controls** (`--loops`).
Both five-scalar gap groups and six declaration cuts are measured against
retail homes, with a frozen original recovery as the baseline.

All 25 declaration forms compile without diagnostics and each passes 66
bounded guest cases: **1650 comparisons**. Three fitting loop forms pass
another **198**, **1848 total**. Eight explicit XYZ-cursor loop forms exceed
the slot at 306/308 words and are not installed or claimed fully qualified.
They receive only an accepted-path home measurement. Correct homes alone
do not qualify their body lengths or schedules.

| Form | Body Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Frozen original recovery | 298 | 0x160 | 275 |
| Selected retail homes | 298 | 0x160 | 273 |
| Selected homes, range-do loop | 296 | 0x160 | 277 |
| Selected homes, less-than inner range bound | 298 | 0x160 | 273 |
| XYZ cursors, for-range, correct homes | 308 | 0x170 | 282 |
| XYZ cursors, do-range, correct homes | 306 | 0x170 | 281 |

[Recovery driver](../../tools/experiments/game_actor_triangle_transform_candidates.py)
now distinguishes frozen `RECOVERY` from installed `SELECTED`; a fail-closed
home rewriter binds the selected declarations. The historical layout/lifetime
drivers explicitly retain `RECOVERY`, so changing production does not silently
change their measured controls. The standard recovery screen also includes
the installed home form.

[Home tests](../../tools/tests/test_game_actor_triangle_home_candidates.py)
assert both inventories, unchanged operation text for the declaration forms,
source/candidate identity, fail-closed rewriter anchors and the live/retail
private-home map. The initial source-binding gate caught pass/axis ordering
ahead of the float declarations in the generator; the copied header was
corrected and rebuilt before acceptance. Its two binding checks then passed
in 0.001 seconds. No assertion was weakened to accept that mismatch.

## Linked Audit

Across **6060 slots**, only `func_1502F490` changes. No function, address or
slot length is added, removed or moved. The exact coordinate phase, buffer
copy, dispatcher, display scan and selector remain unchanged. The update
pass remains independently non-matching at 109 words; matrix leaf/tail
assembly is unchanged.

Installed linked-slot SHA-256:
`faf4457b18eb43de8f30215bd4f94d12a125f4f5df98088ee8e8ca0d5948de79`.

Complete Init **164048 bytes**, Init data/rodata **17376 bytes**, Debugger
**19800 bytes**, and Game data **189088 bytes / 720 owners** remain retail-exact.
The patch CSV remains 10622 rows, SHA-256
`b805f4aada0d4273b2af4ba67424da07de5bfc41e766449f29893b4b63bf011b`.

The complete transform qualification still covers 1719 three-way guest cases,
64512 native reference cases plus 33 aliases, 300 / 302 executed retail
words and 53 / 53 matrix/continuation words. These are bounded finite/address/
ABI checks, not R4300 FCSR, traps, subnormal/legacy-NaN or PC gameplay acceptance.

Final qualification receipts, all exit zero and no test skips:

- Focused suite: **60 tests in 269.380 seconds** (272.233 seconds wall time).
- Selected regression corpus: **362 tests in 818.122 seconds** (819.764 seconds wall time).
- `make tools-check`: passed in 1.185 seconds wall time.
- Whitespace: staged `git diff --cached --check` passes.
- Relative links: **2983** checked across thirteen current/working documents; zero broken.

A fresh live-ELF comparison agrees with every one of the 6060 accepted slot
receipts. Protected sections/data and the CSV checksum are rechecked against
retail/the starting checkpoint, not inferred from the unchanged totals.

Exact C counts stay **3304 / 5462 total**, **2631 / 4789 Game**, zero drift,
**2158 different**. Conversion and the 47 retained Init ASM routines remain
unchanged. README aggregate measurements are still accurate and unchanged;
function details stay in these working docs. No sibling source/build/save/
frozen Release change, host transplant or push.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_actor_triangle_home_candidates
wsl python3 -m tools.experiments.game_actor_triangle_home_candidates --loops
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_triangle_home_candidates tools.tests.test_game_actor_triangle_lifetime_candidates tools.tests.test_game_actor_triangle_transform_match tools.tests.test_game_actor_buffer_copy_match tools.tests.test_game_actor_attachment_phase_match tools.tests.test_game_actor_update_pass_match tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

Next: recover the **0x138 frame** and original SDK-loop lifetimes while
preserving these seven array homes. The 40-byte excess is now above the
relative array rather than below the arrays. Investigate compiler-reserved
scalar homes and dead phase temporaries without forcing early pointers/IDs
into saved registers or changing the argument-spill schedule. Explicit XYZ
cursors alone still exceed the slot, even with correct homes. Preserve the
qualified first-match, fresh second-source and coordinate-alias gates.
The opening saved-register area already matches retail at SP+0x28..0x4C;
argument homes remain at +0x160/+0x164/+0x168/+0x16C instead of retail's
+0x138/+0x13C/+0x140/+0x144. Frame allocation, not that saved-register area,
is the next layout target; other register lifetimes still differ.
Do not normalize the remaining 273 words with a broad guard batch.

The full Game matching goal remains active; this is layout progress, not a
new byte-exact function.
