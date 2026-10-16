# View Matrix Preparation Direct Match

Date: 2026-10-16. Consumer predecessor **e7ba0f89**, tools predecessor
**cc49cf5**. Previous goal turn: **progress**, restoring the slot provider.
Continue the wider Game matching goal, not just this owner.

## Recovered Routine

```text
func_15094EA0  VA 0x15094EA0..0x15094F40  ROM 0xC2350..0xC23F0
40 words / 160 bytes / frame 0x98
```

Replace the false zero-return placeholder with a void one-index routine.
Convert the selected fixed matrix from `D_800DC2A0[D_800BE9C0]` into a
private float matrix, then reread the live frame/base globals to convert
the view-record matrix at byte `0x100 + frame * 0x40`. Combine the first
matrix with the second, in that order, into `D_800D2CA8[index]`.

Use the existing `ProjectedViewFrame95760` view record (size `0x180`) for
indexed record addressing, the SDK's `Mtx` pointer type, and the recovered
three-matrix `func_150A7A48` prototype. Preserve the two 64-byte locals at
SP+0x58/SP+0x18, incoming index home at SP+0x98, saved RA and original
matrix-call order. Do not cache the frame or base across the first helper.

All **40 words emit directly from C**, with **zero new guards**, insertions,
omissions or profile changes. Revalidate all **17** complete-owner source
screens against physical objects, bindings and linked words. Flat byte
arithmetic initially has seven scratch-register differences; staging a view
pointer grows the frame to 0xA0. Existing typed record addressing recovers
the original arithmetic and allocation. Four typed variants are direct
matches; choose the existing record type, not a new layout abstraction.

```text
Raw C target SHA-256
f3b4ac2e90b166ef949183076ddd7856cd1d78d20136cae6faf0791dab589762
Linked 40-word target SHA-256
e75104f8192e2cc6efdb864042ff6d4a70d2fe911494ac2592cfcfe283849ca6
```

## Qualification

Seven pre-install tests pass in **130.246s**. They include:

- **2,432** complete-state original/raw/padded cases covering all 256 frame
  bytes, four view indices, two stack phases, fixed-point edge patterns,
  output/input aliases and mutations between helper returns. All 40 root
  instructions are covered and **1,536** mutation gates fire.
- **1,800** fault-prefix cases at every one of the ten root memory accesses.
  Compare complete modeled state at the access boundary, with actual helpers.
- Fresh SDK O3 `guMtxL2F` compilation/padding reproduces the complete 46-word
  retail slot. Fresh compilation of the existing assembly-processor owner
  reproduces the original 78-word product-kernel slot, including its padding.
  The kernel remains assembly; it is not silently counted as converted C.
- **480** bounded retail caller-loop cases, **744** target invocations,
  original 13-word loop and original join at `0x1501929C`. Include negative,
  zero, one and three maximum indices plus a helper-triggered live-count shrink.
- Separate native32 O2/O0 with UBSan, **128 cases each**, using the actual
  preparation C and actual SDK decoder C. The native product is an ordered
  contract fixture; real-kernel execution is qualified separately in the guest model.
  Five compiled controls (cached frame, cached base, reversed product, wrong
  fixed slot and wrong output) fail observably with exit 22.
- All 18 neighboring raw bodies and relative bindings remain fixed. Check
  all 40 object words, all 13 bindings, unexpected pools, **102** immutable
  inputs and independent HI16/LO16 carry/J26 rebases. The two extra inputs
  are the original caller assembly and SDK API header.

The fresh SDK compiler retains its known `-Xfullwarn not supported` warning;
the target and product-owner diagnostic streams are empty. No production
SDK source, product kernel, compiler profile or guard manifest is changed.
Native cases use valid disjoint C storage. Alias/fault receipts are compiled
flat-guest evidence, not portable C, all-caller, hardware FCSR or gameplay
acceptance. Native units use `-mstackrealign` and `-fno-strict-aliasing` for
harness/SDK compatibility; these are harness flags, not guest build flags.

## Corrected Harness Boundaries

The first standalone assembly attempt exposes an untyped label to the
object parser and runs zero tests. Use the established assembly-processor
owner to supply function metadata; do not bypass the full 78-word comparison.

The first caller assertion incorrectly assumes the installed caller already
contains its retail loop. Live progress and `nm -S` prove otherwise:
**func_15019130 remains a 12-byte C stub**, versus its original **740-byte /
185-word** slot. Its loop window in the frozen ELF is zero padding. Qualify
the original ROM loop instead and explicitly assert the installed stub
boundary. This turn does not restore that caller or claim an installed
full gameplay pipeline. The scoped Graphify/source/assembly searches establish
this observed caller edge, not the absence of any other runtime callers.

An initial cached-frame native control segfaults in the freestanding harness,
not at its intended protocol check. GDB observes `movaps 0x30(%esp),%xmm3`
at `0x080495b8`, ESP `0xffffd294`, an unaligned SSE read. Add native-only
`-mstackrealign`; positive O2/O0 and all five effective controls then pass
their required exit gates. The focused caller/native rerun passes two tests
in **17.507s** before the successful full pre-install suite. Retain this as
intermediate harness evidence, not a production or current-binary fault.

## Complete First Prediction

Freeze the original link script and owner object before installation and
reproduce the complete predecessor. The first candidate prediction changes
**138 ELF bytes**: 137 code bytes inside the original 160-byte slot and one
function-size byte (**12 -> 160**). No metadata reorder, symbol additions,
exclusions or unexplained changes are accepted.

```text
ELF    c0f62994f2c5778483cbc1159b7972694b2bdc5431874ddaf8339e27c185a628
Owner  ee0b950eea15592bcbf9f9ecb7d4c449156d072959cbf3a807409bdf692b22ab
Guards 6d409b75d30f2d5d7db243a5220aaa97011ed8a59054445693761ed1f25df465
```

The normal guest build completes with exit 0 and exactly matches that first
ELF hash. The guard CSV stays byte-for-byte unchanged, so only this owner
recompiles before linking and regenerating progress. The existing duplicate
`generated_12D630` recipe warning remains unrelated and unchanged.

## Verified Checkpoint

**All ten final tests pass in 148.649s**, including the post-install whole-
image, data-layout, every-input/callee/caller/metadata corruption and exact-
successor checks. The complete 3,257,636-byte ELF equals the first prediction;
all **100** other tracked inputs, all 18 neighboring raw bodies/bindings,
the complete guard CSV and protected **189,088 bytes / 720 owners** are fixed.
The local successor adapter recognizes only the changed ELF/owner hashes
above and checks its saved before/after fixtures; unknown live files are
never normalized.

Fresh official measurements:

| Section | Converted | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,501 / 6,044 (91.02%) | 3,598 / 5,501 (65.41%) | 0 | 1,903 |
| Init | 492 / 539 (91.28%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,828 / 5,323 (90.70%) | 2,925 / 4,828 (60.58%) | 0 | 1,903 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts and bytes are unchanged: the replaced placeholder already
counted as C, and the entire progress CSV is unchanged. Root README changes
only its two aggregate match rows. Mark matrix preparation done in the prior
roadmap entry while keeping the rectangle and caller as separate open tasks.

Tools commit **d7a8bb17758276a3a24fa83a93e21958f45ebbf7** banks the four
experiment/checkpoint/test files before the consumer pin. Windows AST parsing
passes for all eight files across both tools copies; all four mirrored files
are byte-identical. Eleven shared padder tests pass in each copy (0.061s
consumer, 0.050s old mirror), and `make tools-check` passes. Preserve the old
mirror's HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **837** initial
dirty-file hashes and **841** final dirty paths, without committing/resetting
that independent checkout.

## Resume Boundary

Prioritize the observed unfinished **func_15019130** caller (185 retail
words) next, under its own source/ABI/whole-image qualification. The adjacent
250-word `func_15094AB8` remains a stub. Rectangle `func_15095D34` remains
346 words / frame 0x88 / 18 differences / literal 148/91-word spans; keep
its twelve flip-block words and six macro-home accesses open. The wider
Game/additional-source/caller queues remain active. No push, Claude/auth
retry or host-port/frozen Release edit, build or launch.
