# Overlay Projection Direct Match

Date: 2026-10-17

Predecessor: consumer **6bfc2372**, tools **381d541**. Follow
[Note 1474](1474-pulsed-overlay-private-lifetime-audit-20261017.md) without
adopting its undefined-local pulse candidate. This checkpoint instead recovers
the next same-owner **func_1517F814** as complete, directly linked C.

## Scope And Result

- Owner: `conker/src/game/generated_1AC2F0.c`.
- Original: `conker/asm/1AC2F0.s`.
- VA **0x1517F814..0x1517F9F4**, ROM **0x1ACCC4..0x1ACEA4**.
- **120 words / 480 bytes**, frame **0x40**, RA at **SP+0x24**.
- **Zero new instruction guards**, unchanged O2/g3 compiler profile.
- All **27 raw and padded owner neighbors** remain unchanged.

Recover the five-argument interface:

```c
void func_1517F814(s32 screenSpace, f32 x, f32 y, f32 z, s32 view);
```

The live func_151814FC remains a C placeholder. Its original assembly packet
ignores V0; no C calls or prototypes require a separate edit. Do not
replace stable address names with speculative names. The source adds a
concise semantic comment and typed matrix-helper declaration.

## Source And Literal Binding

For screenSpace zero, call the actual eight-argument handwritten matrix-tail
helper with the 64-byte matrix row and four distinct private outputs at
SP+0x3C/0x38/0x34/0x30. Substitute 1 only for positive/negative zero W.
Read the live 0x180-byte viewport record after the helper. Preserve separate
multiply/divide/add/subtract operations, including the original Y sign.
The nonzero mode accepts screen X/Y directly and does not call the helper.

Preserve ordered upper/lower comparisons, unordered NaNs, and the lower
limit selected by the X branch then reused by Y. Publish relative X before
reading live extentY for the second output store, including supported aliases.
The viewport layout exposes extentX/extentY at +0xC/+0x10 without changing
its 384-byte size. No read of an uninitialized local is introduced.

Twenty-one bounded complete-function screens (initial plus 20 forms) resolve
the source/frame/literal issue:

| Form | Words | Frame | Ordinal Word Differences |
| --- | ---: | ---: | ---: |
| Mutable external bounds, ordinary locals | 120 | 72 | 45 |
| External bounds, record/lower first | 120 | 72 | 19 |
| Literal bounds, record/lower first | 120 | 64 | 36 |
| Literal bounds, four outputs first | 120 | 64 | 6 |
| Selected body with original pool binding | 120 | 64 | 0 |

The six remaining words are literal-address bindings, not semantic or
scheduling differences. The compact object emits three original float words:
**10000 / -10000 / -10000**, at original **D_800A7280/+4/+8**.
Use the existing generated-object **RETAIL_RODATA_SYMBOL := D_800A7280**
mechanism for this owner. It preserves emitted instruction words and section
addends, reusing existing runtime data; it is not an instruction guard, new
compiler profile, pool insertion or semantic patch.

The compact pool is 16 bytes, but its final four bytes are unused alignment
padding and are **not installed**. Only the original first 12 bytes are bound.
Do not mistake the padding for runtime D_800A728C, whose original value is 0.01.
The three original constants rebase together as one contiguous block.
Full raw C and normal padded C both equal all 120 original words after that
same binding. Preserve the unreachable compare at **+0x190** as part of the
complete 120-word gate; the natural corpus reaches 119 target words.

## Qualification

All **36 final tests pass in 482.491s**, comprising eight target tests,
three new installed-image tests, seven prior pulse-audit tests and 18 prior
installed-image regressions. Earlier focused target runs also passed:
seven tests in 150.078s, then the supplemental reset/writer test in 4.672s.

- **2,328 three-way guest cases**, comparing independent reference,
  original/bound raw/padded execution, complete private memory/register/events
  and helper homes across both stack phases.
- **2,520 actual matrix-helper runs** across the three images; every word in
  its complete **58-word physical helper/tail image** executes.
- **558 native32 cases per O2/O0 profile**, UBSan enabled, separately compiled
  complete body, typed caller and semantic matrix adapter. Both pass.
- Eight native semantic controls all fail effectively with **exit 22**,
  not a signal/trap: mode, matrix stride, W fallback, divide, Y sign, upper
  clamp, unordered NaN handling and swapped outputs.
- Three independent original/C rebase pairs move the complete three-word
  literal block, global anchors and R26 helper, including HI/LO carry cases.
- **231 positively fired three-way fault prefixes**, covering actual helper
  private state, literal reads and partial output publication.
- **40 three-way original caller-packet cases**, all 11 packet words,
  actual 120-word callee and 58-word helper. Preserve its SP+0x74 word
  and SP+0xC0/+0xBC floats. This is not the entire unrecovered 499-word parent.
- All 120 instruction-word, 16 compact-pool-byte, 16 binding controls
  (15 actual bindings plus an unexpected entry), and 156 input-entry
  corruptions reject. Installed image/extent/symbol/fixture gates also reject.

Native evidence is bounded to valid views 0/1/3, original constant values,
float-backed viewport/output aliases and separate matrices. It follows the
existing GNU native32/fno-strict-aliasing union-storage test convention, not
a universal ISO effective-type proof. NaN-class tolerance applies only to
changed float output words. Invalid/full-word sparse indices, altered pool
values, private-home cases and fault prefixes remain guest-only evidence.
The native semantic matrix adapter is not a proof for arbitrary private
matrix/output aliases. The existing nontrapping FP model does not establish
hardware FCSR/inexact/exception-enable/CP0 behavior, pixels or full gameplay.

## Frozen Image And Build

Before source edits, reproduce the entire predecessor ELF byte-for-byte and
freeze the first image/source/Makefile prediction. The complete prediction has
**371 changed ELF bytes = 369 target code bytes + two symbol-size bytes**.
The target symbol grows from **12 to 480 bytes**. ELF length remains
**3,257,636**. There are **zero metadata exclusions**, symbol/string
reordering or unrelated image changes.

The normal `make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1`
finishes successfully. The Makefile prerequisite causes a broad generated-slice
rebuild; allow it to complete normally, without a Makefile bypass. The
entire resulting ELF equals the first prediction, not merely the target slot.
Existing duplicate recipe warnings remain. This is not a warning-free
build, whole-ROM checksum or runtime/gameplay acceptance claim.

Installed SHA-256 values:

```text
ELF                  5dace9c4eedc9095056502b70a98d16ad615706dacc3ff2576d01fb6c05abcc7
generated_1AC2F0.c    1874f2f029edf42198bc24884d2aa69ffdbdc28041d00eb3c037b3585e38dea5
Makefile             4458ac99ecbe044a54930d5ec79f6a72d33b2ee06acc871d61dde60f32582ef3
guard manifest       5084330509403cb54c534e06be40b8417b97e95addf3dd362f843e4235b58b35
```

Protect **156 input entries / 147 distinct paths**, **153 unchanged entries**,
three exact before/after fixture pairs and **189,088 Game-data bytes /
720 owners / zero differences**. Conversion CSV and every instruction-guard
byte remain unchanged. Prior checkpoints recognize only this exact successor
before their prior inverse; no unknown source/image/fixture change is ignored.

Fresh official matching is Game **2,946/4,828 (61.02%)**, total
**3,619/5,501 (65.79%)**, different **1,882**, zero drift. Init stays
**492/492**, Debugger **181/181**. Nominal conversion remains **5,501/6,044
functions / 86.04% bytes**, because the prior stub already counted as C.
Root README changes only its two aggregate matching rows.

## Deferred Pulse Follow-Through

func_1517F564 remains unchanged and gets **no C matching credit**. Actual
func_15008A60 reset execution in **six 76-word cases** clears the timer
without clearing the pulse byte. Source-only cold/alternate boot ordering
inspection does not establish initialization on all program paths.

The neighboring func_1517F488 indexed alpha writer, executed in **two
20-word guest cases**, can hit D_800DDD8C with channel **-16** while the
timer remains active. The actual pulse/lookup/draw chain then publishes
RGB **60/65/100** from inherited **0.25**, independently preserving the
prior pulse-off concern. That invalid native index is **guest-only**;
it is not evidence of natural gameplay reachability or a valid native call.
Neither finding proves a supported C lifetime or all-program pulse-one
invariant. Do not adopt undefined C or substitute zero.

## Tools And Next Step

Tools **9d0f799** banks exactly ten files before the consumer pin.
Ten mirror task pairs are identical; **20 ASCII/AST checks** pass. Eleven
shared padder tests pass in each copy: active **0.029s + 0.020s**, mirror
**0.032s + 0.019s**; `make tools-check` passes.
Before copying, all three existing task files matched both the committed
active-tools baseline and their captured mirror hashes; seven new paths
were absent. Preserve mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**
and all **1,008 unrelated initial dirty-file hashes**. Three task files update
and seven are added, producing **1,018 final dirty paths**. No mirror
commit/reset, push, Claude call, external tool/dependency configuration change, host build/
launch or frozen Release action.

Prepared-checkout reproduction, sequentially (retain the first frozen receipts):

```sh
python3 -m tools.experiments.game_overlay_projection_installation
make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1
python3 -m unittest tools.tests.test_game_overlay_projection \
  tools.tests.test_game_overlay_projection_installed \
  tools.tests.test_game_pulsed_overlay_audit \
  tools.tests.test_game_color_overlay_draw_installed \
  tools.tests.test_game_color_channel_aggregate_installed \
  tools.tests.test_game_color_progress_installed \
  tools.tests.test_game_color_state_submit_installed \
  tools.tests.test_game_sequence_event_scan_installed \
  tools.tests.test_game_sequence_record_setup_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover complete direct C, original literals/frame/private ABI and all neighbors.
- [x] Qualify real helper/caller paths, native controls, rebases, faults and corruption gates.
- [x] Freeze the first whole-image prediction, complete the normal build and pass 36 tests.
- [x] Measure fresh matching, update aggregate rows/indexes/roadmap and bank tools first.
- [ ] Resolve the deferred pulse wrapper's supported lifetime/precondition without invented C.
- [x] Recover the adjacent clipped rectangle leaf in Note 1476.

Next **func_1517F9F4**, same owner: **106 words / 424 bytes**, frame-free,
VA **0x1517F9F4..0x1517FB9C**, ROM **0x1ACEA4..0x1AD04C**. Recover the
six-argument cursor/endpoints/view interface, signed endpoint normalization,
four signed TRUNC.W.S viewport conversions, strict overlap/ordered clipping
and one SDK F6 fill-rectangle / eight-byte cursor advance. Preserve incoming
cursor homes and their live alias/update order, full-word indices and actual
caller packets before accepting C. Wider Game/additional-source matching,
query/sequence engines, timing's 141 differences and full gameplay remain open.

Follow-through: [Note 1476](1476-clipped-rectangle-direct-match-20261017.md)
installs the complete 106-word clipped rectangle directly from C, without
new guards/profile/pool/build changes. The deferred pulse lifetime stays open.
