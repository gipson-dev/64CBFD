# Clipped Rectangle Direct Match

Date: 2026-10-17

Continue [Note 1475](1475-overlay-projection-direct-match-20261017.md) from
consumer **b4c6f01b**, tools **9d0f799**, both initially clean. Replace
func_1517F9F4's zero-return placeholder with its complete signed viewport
clipping and SDK fill-rectangle body. Keep the broader Game matching goal
open; this is one measured recovery, not completion of the queue.

## Recovered Interface

- Owner: `conker/src/game/generated_1AC2F0.c`.
- Original: `conker/asm/1AC2F0.s`.
- VA **0x1517F9F4..0x1517FB9C**, ROM **0x1ACEA4..0x1AD04C**.
- **106 words / 424 bytes**, frame-free, **directly exact from C**.
- **No new guards, compiler profile, pool, runtime data or Makefile changes**.
- All **27 raw/padded owner neighbors** remain unchanged.

```c
Gfx *func_1517F9F4(Gfx *commands, s32 left, s32 top,
                 s32 right, s32 bottom, s32 view);
```

Preserve the stable address name and add a concise semantic comment. Both
live caller parents remain C placeholders; only their original assembly
packets are qualified here. There are no C calls or prototypes to alter.
The reference archive's matching broad control shape is useful,
but its integer-typed viewport loads are not the original floating conversions
and are not copied into production.

Sort each endpoint pair using signed comparisons. Read the live 0x180-byte
viewport row using the full-word index. Convert left/top/right/bottom from
float to signed integer using the original TRUNC.W.S order. Preserve strict
overlap tests and all four ordered clamps. Touching a viewport boundary can
reject, but **zero-area endpoints inside the viewport can still emit**;
do not add a blanket zero-area rejection.

Emit the SDK F6 fill command with ten-bit coordinate packing and an eight-byte
cursor advance. Preserve the incoming SP+0 cursor home, its update before
command stores, **W1 then W0** publication and the final live home reload.
Guest-only cursor/home aliases can therefore change the returned value.
Do not replace that reload with an assumed register cursor in a guarded body.

## Source Recovery

The first complete semantic form has **105 words / 63 ordinal differences**.
Recovering the original float-load order improves the ordinary form to
105/50. A shared clamp result restores 106 words; assigning results back to
the endpoint parameters leaves 30 register-role differences. Reusing the
sorting scratch as the left clip bound closes all of them: **106/0**.
The final source names this variable scratch and comments its later role.
No instruction normalization or changed optimization flags are used.

Raw target SHA-256:
`ed394c8a4cb392c4df81808c9ed0b032a8c877efacae38bcd922ea6762b21b0b`.
Lock both D_800BE628 bindings, **+0x34 HI16 / +0x38 LO16**, and the full
16-byte inherited compact pool. The prior projection's existing pool binding
stays unchanged; this recovery emits no new literals.

Ten compiler words are unreachable from this routine's entry after sorting
and the strict overlap gates: duplicate comparisons at **+0xA8/+0xBC**,
and impossible clamp arms at **+0xC8/+0xCC, +0xF4/+0xF8,
+0x10C/+0x110, +0x138/+0x13C**. Keep all ten in the complete 106-word
comparison and corruption gates. The natural corpus executes **96 words**;
do not claim that the retained dead arms were naturally executed.

## Qualification

All seven pre-install tests pass in **95.206s**. All **13 final tests pass
in 199.893s**: the seven target checks, three new installed-image checks
and three affected predecessor projection checkpoint regressions.

- **1,536 three-way guest cases**, independent reference versus original,
  raw C and padded C. Cover signed sorting, reversed bounds, strict/touching/
  degenerate boundaries, fractional/signed-zero/extreme bounds, sparse full-word
  indices, wrap, live viewport/output aliases and both stack phases.
- **900 emitted / 636 rejected cases**. All private/public memory, registers,
  events, return bits and no-call behavior agree across the three images.
- **588 native32 cases per O2/O0 profile**, UBSan, separate complete SDK body
  and typed caller, complete viewport/output canaries. All eight effective
  controls fail with **exit 22**, not a trap/signal: X/Y sorting, inclusive
  edges, baked view, wrong lower X, missing Y clamp, swapped X and changed edge.
- Three independently assembled original/C global-rebase pairs, including
  signed-low HI16/LO16 carries, preserve all 106 words.
- **126 positively fired three-way fault prefixes**, including initial cursor
  homing, argument/bound reads, live home updates and partial command stores.
- **96 three-way real caller cases** across all **16 original call sites**,
  six original packet words each, both stack phases and views 0/1/3. Execute
  the real 106-word callee, delay-slot argument stores/updates and private
  SP+0xDC/+0xEC/+0xE8/+0x40/+0x3C writes.
- All 106 word, 16 inherited-pool-byte, three binding controls (two plus
  an unexpected entry), and **156 input-entry corruptions** reject.
  Installed extent/symbol/dead-word/fixture gates also fail closed.

The original six-word windows are bounded packet evidence, **not complete
execution of either unrecovered parent**. Native evidence is limited to
valid views, finite in-range signed conversions and aligned float-backed
viewport/output aliases under the existing GNU native32/fno-strict-aliasing
union-storage convention. It is not a universal ISO effective-type proof.
Sparse invalid indices, nonfinite/out-of-range conversion values, incoming
home aliases and wrap/fault state remain guest-only evidence.

The guest invalid-conversion result follows the existing bounded nontrapping
indefinite-word model. It is **not hardware FCSR, enabled-exception, inexact,
CP0, pixel or gameplay acceptance**. Initial focused harness failures were an
incorrect caller shift expectation (high signed half, not low half) and an
overstated natural-coverage expectation. Both were corrected against original
words without production edits or relaxed byte/fault gates. Native selected
bodies and all eight controls already passed that focused run.

## First Image And Normal Build

Before source installation, reproduce the entire predecessor ELF and freeze
the first whole-image/source prediction. The complete **3,257,636-byte ELF**
changes exactly **331 bytes: 329 target code bytes and two symbol-size bytes**.
The target extent grows from **12 to 424 bytes**. No symbol/string reordering,
metadata exclusions, unrelated image differences or pool changes.

Normal `make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1`
rebuilds the single owner, pads/links successfully and regenerates progress.
The entire result equals the first prediction. Existing duplicate recipe
warnings remain; this is not a warning-free or whole-ROM checksum claim.

```text
ELF                  90fba53a4f9927a2528e5d77aee1076e1e5b05a2ab71b184f2425ec487fcaa3e
generated_1AC2F0.c    9d7f84a8a678832a89a3ac29a92bcc01ba63ca7222757148ed8b799c077d91db
Makefile             4458ac99ecbe044a54930d5ec79f6a72d33b2ee06acc871d61dde60f32582ef3
guard manifest       5084330509403cb54c534e06be40b8417b97e95addf3dd362f843e4235b58b35
```

Protect **156 input entries / 147 paths**, **154 unchanged entries**, both
exact before/after fixture pairs, conversion CSV and all previous guard bytes.
Game data remains exact across **189,088 bytes / 720 owners / zero differences**.
The affected predecessor checkpoint recognizes only this exact source/image
successor before its original inverse. Unknown data, symbols, fixtures or
source edits are not silently accepted.

Fresh official matching: Game **2,947/4,828 (61.04%)**, total
**3,620/5,501 (65.81%)**, different **1,881**, no drift. Init stays
**492/492**, Debugger **181/181**. Nominal conversion stays **5,501/6,044
functions / 86.04% bytes**, because the prior stub already counted as C.
Root README changes only its two aggregate matching rows.

## Tools And Handoff

Bank tools **d52744e** first: seven new files and three affected predecessor
checkpoint files. Ten exact mirror task pairs / **20 ASCII/AST checks** pass.
All eleven shared padder tests pass in both copies: active **0.030s + 0.020s**,
mirror **0.030s + 0.018s**; consumer tools-check passes.

All three existing mirror task files match the committed active baseline and
their initial live hashes before copying; seven new paths are absent.
Preserve mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a** and all
**1,015 unrelated initial dirty-file hashes**, producing **1,025 final paths**.
No mirror commit/reset, push, Claude calls, external dependency/tool
configuration changes, host build/launch or frozen Release action.

Prior unchanged neighbor-suite receipts remain prior evidence, not fresh runs;
this direct conversion changes no other linked body, data, guards or compiler
profile. The target suite, exact image audit, affected predecessor checkpoint
and shared tools checks are fresh.

Prepared-checkout reproduction, sequentially; retain first frozen receipts:

```sh
python3 -m tools.experiments.game_clipped_rectangle_installation
make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1
python3 -m unittest tools.tests.test_game_clipped_rectangle \
  tools.tests.test_game_clipped_rectangle_installed \
  tools.tests.test_game_overlay_projection_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover the complete direct C interface, signed clamps and SDK command.
- [x] Preserve all 106 words, private cursor lifetime, pool, guards and 27 neighbors.
- [x] Qualify guest/native/control/rebase/fault/caller and corruption boundaries.
- [x] Freeze the first entire image, build, pass 13 final checks and measure progress.
- [x] Update aggregate rows/indexes/roadmap, preserve mirror and bank tools first.
- [ ] Recover the next textured rectangle routine and wider Game queue.

Next **func_1517FB9C**, same owner: **633 words / 2,532 bytes**, frame
**0xD8**, VA **0x1517FB9C..0x15180580**, ROM **0x1AD04C..0x1ADA30**.
Recover its complete size/step/offset/view interface from all original callers,
float and fixed-point conversions, clipping, original texture-rectangle packet
order, live viewport/projection offsets and private homes. Do not assume the
reference's types or arithmetic shifts are correct. The deferred 111-word
pulse wrapper's supported lifetime/precondition, query/sequence engines,
timing's 141 differences and full gameplay remain open.

Follow-through: [Note 1477](1477-mirrored-texture-candidate-and-private-gap-20261017.md)
recovers the next routine's complete four-rectangle SDK candidate and qualifies
its public packets, native behavior and original caller windows. It remains
uninstalled: 626/633 words and private spill homes still differ. No new credit.
