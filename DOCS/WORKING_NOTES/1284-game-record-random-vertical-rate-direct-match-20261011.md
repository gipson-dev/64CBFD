# Game Record Random Vertical Rate Direct Match

Date: 2026-10-11. Recover complete func_1503EFC4 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503EFC4..0x1503F078, ROM 0x6C474..0x6C528: 45 words / 180 bytes.
All 45 words emit directly from semantic C under existing O2/g3, including
the retail 0x30 frame, unsigned division, delay-slot output store and
unreachable break 7 check. No guards, padding, drops, insertions, new pools,
headers, declarations, caller bodies, compiler profiles or recipes change.
Matching +1 only; converted counts/bytes unchanged. Full Game goal active.

## Baseline And Contract

Consumer d8dcb4e4542bf31fc55368efb897e3f1186e781c and mounted tools
7730335a1e3971c90817a76380292bbbeb76f6eb were clean at entry.
[Note 1283](1283-game-record-ground-collision-guarded-match-20261011.md)
left this genuine 45-word / 43-difference target. Query Graphify, then inspect
the complete body, original callback tables, actual dispatcher and owner
profile. Reuse IDO, ELF/object/pool parsers, GLOBAL_ASM processing, both
padders, native32 fixtures, StateOracle, the retained RNG64 runner/next_seed
and TimerOracle DIVU/MFHI/BREAK behavior. Codex is the single writer;
zero Claude calls, no bridge, installs or account changes.

Recover void func_1503EFC4(s32 slot), consistent with the existing
void (*D_8008443C[])(s32) finish-callback interface. The original three
table entries are func_1503EFC4, func_1503F108, func_1503F16C. It is the
group-0 initialization callback, not the active-frame callback. The dispatcher
calls it after element setup, then writes state 1 and invokes the active row.
V0 has no separate status calculation and is ignored.

- Derive the 16-byte D_800C6660[slot] control and read its unsigned group
  +0xE. Store signed-halfword timer 120 at +0xC, even for count zero.
- Read unsigned D_80098914[group] count after the timer store and cache it.
  Zero count skips RNG and buffer accesses.
- For every record, call func_150ADA20 exactly once. Use its low 32 bits
  as an unsigned numerator, take remainder modulo 20, cast remainder to
  signed before subtracting five, then convert once to single precision.
  Rates are -5..14; unsigned subtraction would instead produce huge floats
  for remainders below five.
- Reload the live control buffer after each RNG call. Store the rate to
  record +0x4C, advancing by the existing 104-byte struct04 stride.
  There is no flag/type gate. Preserve every other record/control byte.
- Preserve S0..S4, RA, 0x30 frame and loop/delay-slot lifetimes.

The complete original 18-word handwritten func_150ADA20 is retained.
Its return can be sign-extended in a 64-bit guest register; the local test
adapter feeds only low words to the existing DIVU runner, restores untouched
wide inputs, and reuses MFHI/BREAK behavior. No new RNG or CPU engine is
invented. Native callbacks qualify compiled source behavior, not an ISO C
guarantee of arbitrary assignment-expression evaluation order.

## Compiler Shape

The explicit temporary-RNG source reaches 45 words/frame 0x30 but has six
scheduling differences around address formation, divisor checking and the
delay-slot store. Direct assignment produces all 45 original words.
Unsigned literal and divisor-local variants retain six differences; cached
group, offset cursor, do-loop and count-home variants do not improve them.
Selected compact no-unroll is identical. O1 emits 47 words/frame 0x28 and
46 differences, so leave the actual owner profile unchanged.

The divisor is always 20 in valid executions. IDO naturally retains the
nonzero branch and unreachable break 7 at +0x80. Do not remove that retail
artifact or claim a C division-by-zero contract. No guard manifest changes.

## Fresh Qualification

Twelve pre-install tests pass in 18.237 seconds. Twelve installed tests pass
in 18.830 seconds. Ignored receipts:
conker/build/game-record-vertical-rate-match-test/.
Final source/ELF integrity gates pass again: two tests in 4.309 seconds.

- 150 retail/raw/padded cases cover counts 0/1/3/4/5/27/45/128/255, both
  stack phases, groups, mapped invalid slot words and every remainder/offset
  boundary plus 0x7FFFFFFF/0x80000000/0xFFFFFFFE/0xFFFFFFFF. All 44 reachable
  words execute; the dead break never does. Timer 120 is written for empty
  records, unsigned high bits and negative rates remain correct.
- Eight effective callbacks rewrite buffer/count/group or the pending field.
  Count/group remain cached; each buffer lookup follows its RNG call and
  the later store overwrites the callback's pending value. Alternating
  buffers distinguish subsequent iterations.
- Four timer/count alias cases map control+0xC/+0xD onto count bytes.
  High byte becomes zero, low byte becomes 120; the read-after-store count
  determines zero versus 120 draws. These are rebased guest checks, not
  portable native aliases or real N64 allocation acceptance.
- 144 cases execute all 18 actual RNG words with twelve 64-bit seeds,
  counts 0/1/5, phases and a rate/seed-high-word alias. Subsequent draws use
  the modified seed, and negative sign-extended V0 uses low-word DIVU.
- Two independent links rebase three symbols with HI/LO carries in eight
  cases. All 53 fired fault triplets preserve complete memory/events/GPR/FPR/
  HI/LO state. No portable C fault or hardware/FCSR claim.
- Four freshly compiled controls fail on public effects: lost timer, wrong
  modulus, unsigned subtraction and cached buffer. The wrong-modulus fixture
  uses discriminating 19/20/0xFFFFFFFF draws after an initial below-16 stream
  proved non-discriminating; production is not changed to pass the test.
- One private zero-divisor instruction mutation per form reaches and fires
  the existing break 7. It is a guest-machine corruption test, not defined C
  zero division, and does not execute in normal paths.
- Both copied full owners are diagnostic-free, pass GLOBAL_ASM processing and
  both real padders. All 21 neighbors/extents/relocations and normalized pools
  remain exact, including dispatcher171, collision134 and impulse74.
- Exact source/ELF/seven-input checks and effective stale/duplicate installs,
  source, four ELF and old-guard corruption controls pass without refreshing
  the frozen baseline or permitting metadata exceptions.
- 96 cases execute actual dispatcher171 -> predicate27 -> group-0 finish45
  -> RNG18 with original callback-table provenance, states 2/3, counts
  0/1/3/5, phases and six seeds. Other callbacks/active and motion/matrix
  tails remain boundary models, not full gameplay acceptance.
- Native32 O2/O0 each pass 12,288 cases across every count 0..255, three
  slots, eight unsigned draw patterns and buffer/count mutations. Check all
  words in two 256-record banks and all control words, including skipped and
  empty cases; draw count is exact. Four native controls independently fail,
  including signed remainder, unsigned subtraction and cached buffer.
  No private alias, hardware or FCSR acceptance claim.

~~~sh
python3 -m tools.experiments.game_record_vertical_rate_candidates --profiles
python3 -m unittest tools.tests.test_game_record_vertical_rate_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit

The source-only rebuild compiles the one changed owner and relinks; no guard
timestamp triggers a broad rebuild. Exit zero with the known duplicate
generated_12D630 recipe warning; target owner is diagnostic-free.

Literal full-ELF comparison changes exactly 135 bytes: 134 target bytes and
one size byte (12 -> 180). Every other byte, function body/address/extent,
metadata record/string, section/header, pool and data remain exact. No
projection, metadata permutation or generic exception. Seven other inputs
are identical: guards, progress CSV, rodata assembly, symbols, undefined
functions, retail layout and Makefile.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | b29637289176da1db3720c86e43270c377e81d3567bbf32e2ebfbb32cdabc4c9 |
| Source after | 5516cd7c1641d54e312dcc5e6bbf0496f6b6dead96e22390a015c7213c1dbf36 |
| ELF before | ced34e5fd81c32b7c4c62d437c33f43894c705559633292fbc567e904d221c75 |
| ELF after | 2eba14a881b78db16bee6505b484a7484720777acf4ba8599ae6ef1f085002d1 |
| Guards unchanged | 92f39fbf0bf509614ecff961e3a654e01d30c98666c3c65f224884f57102206e |

Fresh progress: Game 2,805/4,822 (58.17%), total 3,478/5,495 (63.29%),
Init 492/492 and Debugger 181/181. Zero drift / 2,017 still different.
Matching +1 only; README gets aggregate rows, not a recovery narrative.

## Checkpoint And Next Body

Consumer, mounted and older standalone shared checks and native py_compile
pass. Bank mounted tools 4cc2121 first, then source, this note, five current indexes,
aggregate README and exact consumer gitlink. No push. Older sibling HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 59 recorded hashes remain
unchanged. Only two absent paths are copied with identical hashes; dirty
count 336 -> 338. Do not commit/reset independent older history. Target
suites run in the mounted consumer, not the standalone mirror. Prior unchanged
collision/impulse/motion/matrix/setup suites are reused from Notes 1283/1282/
1281/1280/1279, not reported as fresh runs.

Native graphify update . exits one on protective shrink refusal: 18,196
candidate nodes versus 39,976 saved. Preserve 19,398 nodes from 2,972
excluded but still existing files; no force/purge/install. Version/empty-source
warnings are separate from compiler diagnostics. Require fresh terminal Rebuilt, advanced
log bytes/UTC and zero workers after consumer commit. Precommit log:
538,371 bytes. Launch alone is not completion.

Fresh recheck: func_1503EFC4 45 words / zero linked differences. Next genuine
placeholder is func_1503F16C, 81 words / 80 differences, VA
0x1503F16C..0x1503F2B0, ROM 0x6C61C..0x6C760, same owner. Inspect the
full group-2 finish callback and caller contract before recovery.

Existing guard removal, remaining finish/active callbacks and independent
SDK/hardware/FCSR/renderer/gameplay acceptance remain separate and open.
No OGL Release build/change, private input/save or active editor/debugger
mutation. Keep the full Game goal active.
