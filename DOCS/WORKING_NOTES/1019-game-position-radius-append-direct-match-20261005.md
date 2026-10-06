# Game Position Radius Append Direct Match

Date: 2026-10-05. Starting checkpoint: `33d1b26f`.

`func_1508B20C` replaces its false three-word zero-return placeholder with
semantic C matching all **39 words / 156 bytes** directly. Interval
0x1508B20C..0x1508B2A8, ROM 0xB86BC..0xB8758. No guards, padding,
assembly edit, header edit or compiler override.

## Recovered Contract

[generated_B3020.c](../../conker/src/game/generated_B3020.c) retains the
existing signed-word declaration of D_800D23B0 and the existing slice's
IDO O2/g3/mips2/o32, `-Wo,-loopunroll,0` profile. The existing four-float
void prototype in [functions.h](../../conker/include/functions.h) is correct.
X/Y arrive in F12/F14, Z/radius in A2/A3 and are homed at SP+8/+0xC.
The leaf does not adjust SP or acquire a saved-register lifetime.

A null global base returns without reading the count or converting XYZ.
Otherwise the **signed byte** at +0x1745 is tested against eight. Retail
has no lower-bound check: negative signed counts also take the append path.
The old count indexes a 12-byte record, then the count byte is incremented.
The record holds radius squared at +0x1748, truncated XYZ halfwords at
+0x174C/+0x174E/+0x1750, and untouched padding at +0x1752.
Payload stores occur in **X, Y, Z, square** order, after the count update.
Retail reloads the global before every payload store: five base reads on
the append path, one on the rejected/null path.

The direct match comes from checking the count inline and capturing its
old value with post-increment. This recovers the opening register schedule
and count lifetime without inserting instruction normalization. Explicit
`(s16)(s32)` coordinate casts preserve truncation to signed word followed
by low-halfword storage for representable values outside the s16 range.

## Compiler Screen

[Candidate driver](../../tools/experiments/game_position_radius_append_candidates.py)
freezes the initial recovery and placeholder separately from production.
All **34 controls** complete with empty compiler diagnostics. The selected
body is 39 / zero differences under both the isolated default profile and
the unchanged production no-unroll profile.

| Shape | Words | Raw Differences |
| --- | --- | --- |
| Old placeholder | 3 | 36 |
| Cached index, ordinary fresh bases | 39 | 15 |
| Literal count-byte increment | 39 | 5 |
| Post-increment with redundant cached count guard | 39 | 5 |
| Inline count guard and post-increment capture | 39 | 0 |
| Cached payload base | 31 | 36 |
| Byte-sized index plus literal increment | 41 | 35 |
| Unsigned count load, negative control | 39 | 16 |
| Added lower-bound gate, negative control | 40 | 37 |
| Wrong stride, negative control | 37 | 30 |
| Unsquared radius, negative control | 38 | 21 |

The full inventory includes declaration order, integer/unretained bases,
cached byte offset, volatile accesses, direct-halfword casts, early return
and pre-increment shapes. Compiler controls are not all semantic approvals.
In particular an unsigned word index has only five differences but rejects
retail's negative-count appends; cached bases fail alias-sensitive ordering.

## Qualification

[Matching tests](../../tools/tests/test_game_position_radius_append_match.py)
pass **nine tests in 22.789 seconds**, no skips. Source identity, the
existing prototype/profile, no target guards, frozen controls and all
39 production words are bound independently to retail.

- **8192 three-way guest cases** compare retail, isolated C and production:
  every count byte, eight coordinate/radius patterns, stack phases 0/8,
  and base phases 0/4. All **39/39 words** are visited. Ordered reads/writes,
  complete memory and preserved saved registers/FPRs agree.
- **16 null-base cases** use invalid XYZ conversion inputs only on the path
  that cannot convert them. No count dereference or external write occurs.
- **Six physical alias cases** prove the fresh payload bases and store order
  when X, Z or square overlaps the global word. These are guest instruction
  fixtures, not a native strict-C alias/concurrency acceptance claim.
- Six deliberate negative controls reject unsigned counts/indexes, a new
  lower-bound check, cached bases, wrong stride and missing radius square.
  The old zero-return placeholder also fails the recovered write contract.
- **252 bounded actual-caller cases** execute the 14 real setup/return words
  at 0x150C3494 and 0x150C3564 around the complete leaf. A nonzero enable
  byte passes actor XYZ and 900.0f radius; zero skips the call. The seeded
  caller frame is restored. This does not qualify all of func_150C3230.
- **65536 native source-extracted cases** cross every count byte, eight
  coordinate patterns, eight radii, aligned base phases and null/non-null
  state. Independent expected halfwords/square bits bind the whole storage
  footprint and untouched padding. A second native test fills eight records
  and proves four further calls leave them unchanged.

Coordinates executed on the conversion path are finite and representable
as signed 32-bit integers. Radii include signed zero, fractional values,
negative values and finite multiplication overflowing to infinity. No
out-of-domain conversion, NaN payload, FCSR/hardware exception, concurrent
load timing, full caller or PC gameplay acceptance is claimed.

The fresh focused regression run passes **57 additional tests in 52.685
seconds**, no skips: context matching/native semantics, actor preparation,
three-vertex transform, entity-scan assembly and optional-size loader
matching. The historical full shared-slice/triangle corpus is not rerun
wholesale for this isolated leaf change.

## Linked Audit

Fresh DECOMP build, progress and match-progress targets succeed. Comparing
the prior context checkpoint receipt across **6060 slots**, only
func_1508B20C changes; all addresses and lengths remain intact. Linked SHA:
`b1b87c9bd92c5b2d793671b8bb02c5c31421a517fd93d9d38c2555a57c9ca092`.
Local receipts are under `conker/build/game-position-radius-append-test/`;
the complete screen is `conker/build/game-position-radius-append/screen.json`.

Complete Init **164048 bytes**, Init data/rodata **17376 bytes**, Debugger
**19800 bytes**, and Game data **189088 bytes / 720 owners** remain
retail-exact. All **10637 CSV guard rows** are unchanged; none belongs to
this target. No neighboring routine, data ownership or guard is relaxed.

Exact totals become **3306/5462 (60.53%)**, Game **2633/4789 (54.98%)**,
Init **492/492**, Debugger **181/181**, zero drift, **2156 different Game C**.
Conversion counts and retained Init assembly inventory are unchanged.
README updates only aggregate tables; detailed matching updates stay in DOCS.

`make tools-check`, whitespace checks and **2983 relative links** across
eight current/working documents pass; zero broken links.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_position_radius_append_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_position_radius_append_match -q -f
wsl python3 -m unittest tools.tests.test_game_actor_context_dispatch_match tools.tests.test_game_actor_context_dispatch tools.tests.test_game_actor_preparation_assembly tools.tests.test_game_three_vertex_transform tools.tests.test_game_entity_scan_assembly tools.tests.test_game_optional_size_loader_match -q -f
wsl make tools-check
git diff --check
```

Continue Game matching. `func_15040CC8` is a semantic 39-word overflow in a
38-word retail slot, not a placeholder; its previous 52 controls did not
recover retail's three-saved-register loop shape. A genuinely new lifetime
shape is needed before installing it. Triangle func_1502F490 remains
302 words / frame 0x140 / 242 differences, with the read/frame boundary in
[Note 1017](1017-game-actor-triangle-cached-iterator-audit-20261005.md).
func_150E6FAC's duplicated RA load and handwritten func_150A76F0's separate
register-contract/assembly lane also remain open.

No sibling source/build/save/frozen Release change, host transplant or push.
The broad Game matching goal remains active.
