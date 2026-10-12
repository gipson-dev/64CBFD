# Game Record Ground Collision Guarded Match

Date: 2026-10-11. Recover complete func_1503ECA0 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503ECA0..0x1503EEB8, ROM 0x6C150..0x6C368: 134 words / 536 bytes.
The semantic C body emits all 134 words with retail's 0x68 frame; 119 match
directly. Fifteen expected-word guards normalize closed constant initialization
and F22/F24 allocation. All 134 linked words are exact. This is guarded-exact,
not full direct C. No drops, insertions, padding, new pools, shared headers,
compiler profiles or recipes change. Matching +1 only; converted counts/bytes
unchanged. Full Game goal active.

## Baseline And Contract

Consumer e259a591aefb9d6cd5c84022fd8d5f0a7c0c0bbf and mounted tools
f6b3f2241740ee9221d5911d6314664c9061fd8d were clean at entry.
[Note 1282](1282-game-record-impulse-guarded-match-20261011.md)
left this genuine 134-word / 128-difference target. Query Graphify before
inspecting the complete routine, timer caller, context wrapper, existing
record/control declarations and actual owner profile. Reuse IDO, structured
ELF/object/pool/CSV parsers, the signed-byte StateOracle, native32 helpers,
GLOBAL_ASM processing and both real padders. Codex is the single writer;
zero Claude calls, no bridge, installs or account changes.

Recover void func_1503ECA0(s32 slot). The known timer caller ignores V0;
retail has no separate result calculation. No caller body/header changes.
Keep the existing 16-byte control and 104-byte struct04 with local float views.

- Call func_1510F800(0) before accessing the control or caching count/damping.
  Then derive D_800C6660[slot], read unsigned group +0xE and unsigned
  D_80098914[group] count. Zero count skips damping reads and the loop.
- For positive count cache D_80098928 (0x3ECCCCCD, angular factor 0.4f)
  and D_8009892C (0x3F4CCCCD, horizontal factor 0.8f) across query calls.
- Each iteration reloads the live control buffer, checks nonzero flag +0x64,
  then reads live group/type. Only signed type -1 proceeds; acceleration
  +0x60 equal to either signed zero skips the query.
- Cache this element pointer. Truncate +0x24/+0x28/+0x2C position values
  to full 32-bit integer arguments, call func_1510F8D8(x,y,z,0), add five
  to its integer result and convert once to single precision.
- Compare post-query live Y to that floor. Only strict Y < floor clamps
  +0x28. Read live vertical rate +0x4C after the query.
- For strict rate < -4.0f, multiply +0x48/+0x50 by cached 0.8f, +0x4C by
  -0.5f, +0x54/+0x5C by -1.0f, and +0x58 by cached 0.4f. Keep acceleration.
- Otherwise clear +0x5C/+0x58/+0x54/+0x60/+0x50/+0x4C/+0x48 in retail
  order. The first +0x5C store is in a branch-likely delay slot.
- Preserve cached count, live next buffer/group/type, paired F20..F31
  saves/restores, S0..S6, RA and frame lifetime.

The duplicate zero store at +0x1B0 is unreachable. Separate C stores cause
IDO to emit it naturally; no guard inserts/drops/replaces it. The full
35-word timer caller func_1503EEC0 and eight-word func_1510F800 wrapper
remain exact. The 215-word height-query helper remains a placeholder;
context delegate, height result and retirement callbacks are modeled here,
not recovered SDK bodies or complete terrain/gameplay acceptance.

## Compiler And Guards

The initial shape reaches retail's length/frame with 20 differences. Separate
zero stores reduce that to 13, but it loads damping globals on count-zero.
Correct that lifetime with the guarded do-loop before qualification; this
134-word candidate has 15 differences. Constant scopes/order, early return,
explicit offsets, named physical constants, local order and loop shapes
do not remove them. Compact no-unroll matches selected O2/g3; O1 emits a
different 155-word, 0x38-frame body.

Two guards exchange offset-zero initialization and angular HI16 preparation
at +0x6C/+0x70. Nine at +0x80..+0xA0 restore constant preparation order and
linear damping HI16/LO16 relocations. Four at +0x16C/+0x17C/+0x188/+0x19C
close the linear-factor versus -1.0f F22/F24 allocation swap. Relocations move
with instructions. No arithmetic, branches, call arguments, memory-access
order or saved layout changes. Original guard byte prefix plus 15 rows only;
earlier impulse, teardown and motion guards remain intact.

## Fresh Qualification

Twelve pre-install tests pass in 18.799 seconds. The installed suite passes
all twelve in 22.592 seconds with stronger native callback coverage and the
exact metadata audit below. Ignored receipts:
conker/build/game-record-ground-collision-match-test/.
Final literal-install/integrity gates pass again: two tests in 4.944 seconds.

- 424 retail/raw/guarded cases cover counts 0/1/3/4/27/45/128/255, signed
  types, flags, acceleration signed zeros, strict floor/bounce thresholds,
  negative coordinate truncation, result rounding near 2^24, phases, groups
  and mapped invalid slots. All 133 reachable words execute; +0x1B0 never
  does. Preserve all six paired FP saves and GPR lifetime.
- Eighteen effective callback cases distinguish post-context count/damping
  from cached count/damping/current element, live next buffer/group/type
  and post-query Y/rate. Acceleration is not rechecked after the query.
- Six effective self-alias cases rewrite damping, live buffer or group during
  stores. Mapped emitted-guest checks, not portable C or real N64 memory-layout
  acceptance.
- Count-zero leaves both damping constants/type tables unmapped; flag/type/
  zero-acceleration gates leave coordinates unmapped. Twenty gate/payload
  cases include subnormal, infinity and NaN. No hardware NaN/FCSR proof.
- Two independent links rebase seven symbols with HI/LO carries in 16 cases.
  All 245 fired fault triplets preserve memory/events; guarded/retail GPR/FPR
  state is exact. Raw initialization changes intermediate FPR lifetime and
  may leave different scratch AT on no-query paths. Healthy raw paths match
  every other GPR and every FPR. No portable C fault-prefix claim.
- Six compiled controls fail on public effects: wrong type/flag, threshold,
  lost height offset, wrong damping and live damping. Stale guard rejected.
- Both complete owners are diagnostic-free, pass GLOBAL_ASM processing and
  both real padders. All 21 neighbors/extents/relocations/pools remain exact,
  including timer35, impulse74 and its typed callbacks.
- Strict source/ELF/guard successors and stale/duplicate installs, source,
  eight ELF and guard corruption controls fail effectively. Metadata controls
  corrupt moved values/sections/strings and adjacent text. No baseline refresh
  or arbitrary metadata acceptance.
- 108 cases execute actual timer35 -> collision134 -> context8 against the
  independent composed reference, including signed timer/step and retirement.
  Height query, delegate and stop remain boundary models.
- Native32 O2/O0 each pass 27,648 cases over every count 0..255, three slots,
  types, flags, thresholds and floor outcomes. Check all 26 words of all 256
  records including skipped/padding bytes and call counts. First-query rate/
  global mutations leave later records able to bounce, making cached damping
  independently sensitive. Four native controls fail with mismatch receipts.
  No private aliases, signed overflow or hardware/FCSR claim.

Fixture fixes select the existing signed-byte oracle, include the caller's
35th delay word, and collect no-collision boundary visits for coverage.
Keep guarded AT comparison exact while acknowledging raw initialization.
Correct a native reference indentation warning without weakening warnings.
These are fixture fixes, not production workarounds or acceptance reductions.

~~~sh
python3 -m tools.experiments.game_record_ground_collision_candidates --profiles
python3 -m unittest tools.tests.test_game_record_ground_collision_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit

The manifest timestamp triggers the existing wider dependency rebuild, not
a broad conversion batch. It exits zero with known source warnings and the
duplicate generated_12D630 recipe warning. The strict audit catches one
adjacent symbol/string swap: D_80098928 and func_150DEC90. Values, types,
bindings, sections and the function's 44-byte extent remain unchanged.
Construct the exact 25-byte string swap and two records from the frozen
baseline; never copy arbitrary current metadata.

Literal full-ELF comparison changes 443 bytes: 402 target bytes, two symbol
size bytes (12 -> 536) and 39 metadata bytes. Every other ELF byte, body,
address, extent, header, section and metadata entry remains exact.
Six other inputs remain identical: progress CSV, rodata assembly, symbols,
undefined functions, retail layout and Makefile.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | 9367a1516def9e328ede83dc1c82584a6c6ae6e485ac32ff45bf57e29a9b0fde |
| Source after | b29637289176da1db3720c86e43270c377e81d3567bbf32e2ebfbb32cdabc4c9 |
| ELF before | 9ae3dd99b1c097f66414e7a23f5ad8d847b39e09b7112437687f9f173046f355 |
| ELF after | ced34e5fd81c32b7c4c62d437c33f43894c705559633292fbc567e904d221c75 |
| Guards before | 2887c379208a8ddadbded3ee593396db2e7c7920261ee9f05443f0af412e7911 |
| Guards after | 92f39fbf0bf509614ecff961e3a654e01d30c98666c3c65f224884f57102206e |

Fresh progress: Game 2,804/4,822 (58.15%), total 3,477/5,495 (63.28%),
Init 492/492 and Debugger 181/181. Zero drift / 2,018 still different.
Matching +1 only; README gets aggregate rows, not function narratives.

## Checkpoint And Next Body

Consumer, mounted and older standalone shared tool checks and native
py_compile pass. Bank mounted tools 7730335 first, then source/guards, this note,
five current indexes, aggregate README and exact consumer gitlink. No push.
Older sibling HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 57
recorded fingerprints remain unchanged. Only two absent files are copied with
identical hashes; dirty count 334 -> 336. Do not commit/reset its independent
history. Target suites run in the mounted consumer, not the standalone mirror.
Prior impulse/motion/matrix/setup suite receipts are reused from Notes
1282/1281/1280/1279 on unchanged evidence, not called fresh runs.

Native graphify update . exits one on protective shrink refusal: 18,187
candidate nodes versus 39,967 saved. Preserve 19,398 nodes from 2,972
excluded but still existing files; no force/purge/install. Version/empty-source
warnings remain separate from compiler diagnostics. After consumer commit require fresh
terminal Rebuilt, advanced log bytes/UTC and zero workers. Precommit log:
537,716 bytes. Launch alone is not completion.

Fresh recheck: func_1503ECA0 134 words / zero linked differences. Next genuine
placeholder is func_1503EFC4, 45 words / 43 differences, VA
0x1503EFC4..0x1503F078, ROM 0x6C474..0x6C528, same owner. Inspect its
complete body and callback-table/caller contract before recovery.

The 15 initialization/register guards, earlier guard removal, remaining
height/context/retirement bodies and independent hardware/FCSR/renderer/
gameplay acceptance remain separate and open. No OGL Release build/change,
private input/save or active editor/debugger mutation. Keep the full Game
goal active.
