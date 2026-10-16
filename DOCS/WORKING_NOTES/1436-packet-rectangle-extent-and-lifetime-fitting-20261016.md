# Packet Rectangle Extent And Lifetime Fitting

Date: 2026-10-16. Consumer predecessor **7aa57bc1**, tools predecessor
**552f48e**. The previous turn made verified progress by recovering the
renderer semantically. Continue **the same func_15095D34**, not another
conversion batch. This stage improves matching but does **not** finish it.

## Restored Compiler Structure

Original owner `conker/src/game/generated_C1D70.c`, VA
**0x15095D34..0x1509629C**, ROM **0xC31E4..0xC374C**. Preserve Note 1435's
typed packet/Gfx boundary, byte fields, real SDK macros and animation contract.

| Stage | Words | Frame | Pointwise Retail Differences |
| --- | ---: | --- | ---: |
| Prior semantic checkpoint | 345 | 0x88 | 331 |
| Direct inset divisor, later captured divisor | 346 | 0x88 | 134 |
| Shared named integer numerator before width floor | 346 | 0x88 | 92 |
| Direct packet descriptor at animation tail | 346 | 0x88 | **71** |

Use D_800D2C80 directly inside the inset block while retaining the captured
`divisor` for later arithmetic. This recovers retail's F18-to-F16 branch-delay
transfer and the missing instruction. Capture the shared shifted integer
numerator before the width floor; this restores the original GPR roles across
both divisions and the tint block. Replace only the target's named descriptor
cache with direct `packet->descriptor` expressions, restoring the animation
tail's register allocation without changing its actual reload sequence.

The resulting **346-word / 1,384-byte** body has a literal **104-word prefix**
and **91-word suffix** matching retail, including the three argument homes,
inset/division/tint opening and animation tail. All **71** remaining differences
are in the intervening **151-word** window, offsets **+0x1A0..+0x3FC**.
The padder emits the complete C body without the old trailing alignment NOP.
There are **28 relocations**, no pools or compiler diagnostics, no new guards
and no compiler-profile/shared-helper changes. All 18 owner neighbors retain
their complete compact words and relative bindings.

```text
raw body     ecb44344191b7e1034df986d516cad2e17810783fcddb537b0685a4e1b13288b
linked slot  7e43dc8602f4d50f636a85909c399025c80d1e7f7f55d6287a9890ab9434f1d4
```

## Bounded Screens

The experiment preserves **84** measured source forms, not generated word
patches. Declaration permutations and register hints do not recover the
remaining allocation. Removing/reusing more named temporaries can shorten the
body or shrink its frame to 0x80; those are rejected fits, not matching gains.
Re-reading the divisor after tint can lose the captured-global contract.

Mixed `32`/`32.0f` expressions and alternate float spellings produce the two
separate FP constant loads seen in retail, but emit **347 words** and regress
matching. That is an observed compiler-output sensitivity, not proof of the
original source spelling or which compiler phase caused it. Common fractional-T
expressions likewise do not improve the selected fit. Keep the current 71-word
boundary rather than installing these controls or manufacturing stack locals.

An initial screen accidentally used `baseline` as its label and overwrote only
the new output directory's manifest JSON. Archive it as
`baseline-screen-collision.json`, verify every one of the **100 immutable before
inputs** against the declared hashes, then restore the exact manifest. No ROM,
source, before-input file or prior stage's first prediction was overwritten.
The new experiment rejects that reserved label before writing, and a regression
test verifies the manifest remains unchanged. This does not weaken a fixture gate.

## Qualification

Twelve pre-install tests pass in **80.357s**, exit zero. Reuse the prior
geometry/alias/trap/rebase/connection implementations with the unchanged ABI,
but compile and execute the new body. Override the candidate-specific shape,
physical binding, source-control and whole-image gates explicitly. Adapt the
inset and modulo controls to the actual new expressions; require every control
to differ from the selected source and fail observably.

All **15 final post-install tests pass in 125.719s**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_packet_rectangle_fitting tools.tests.test_game_packet_rectangle_fitting_installed -v
```

The complete installed-image assertion passes again in **0.962s** after
clarifying only its metadata-serialization receipt key. The declared target
extent remains explicitly counted. Both tools copies pass Windows syntax and
all eleven shared WSL padder tests; `make tools-check` passes.

- **2,880 guest geometry cases**, both stack phases; native32 O2/O0 with real SDK macros, separate units, selected-C UBSan and **1,048,576 animation cases each**.
- **672 original/raw-C animation pairs**, 80 guest alias pairs, 16 BREAK 6/7 arithmetic pairs, five bounded special-float pairs and all eight compiled guest/native negative controls. Preserve the prior explicit invalid-C-cast, alias, exceptional DIV-register and hardware-FCSR limits.
- Three independently assembled original rebase sets / **48 paired runs**, **32 real caller/visibility/renderer sequences**, all **346 raw-word / 28 binding** corruption controls, extra pools and all **100 frozen-input** controls.
- **64 full modeled-state boundary pairs** stop before +0x1A0 and compare complete memory, GPRs/FPRs, HI/LO, events, access counts and modeled FP condition/state. A deliberately wrong private argument-home store still has identical public memory but fails full state. This is a real effective private-home control, not a raw-fingerprint failure. It does not prove later private/fault state or complete hardware behavior.
- Whole installed image/input/caller/metadata and strict predecessor/successor fixture gates remain mandatory. Prior unchanged unrelated neighbor-suite receipts remain prior evidence, not fresh broad tests.

## First Image Prediction

Freeze a new **100-input** semantic baseline in
`conker/build/game-packet-rectangle-fitting/`, without replacing Note 1435's
snapshots. Capture the old padded object/link script before installation and
require their baseline full link to reproduce the predecessor ELF. Predict
the target from independently padded C, not copied retail instructions.

The complete first prediction changes **1,152 bytes**, all in the target's
original 1,384-byte slot and its declared symbol extent **1,380 -> 1,384**.
There are **zero additional metadata serialization changes or exclusions**;
do not infer zero symbol-size changes from that statement. Guard bytes and
98 other input keys are expected to remain fixed. The normal guest build
exits zero with the pre-existing duplicate generated_12D630 recipe warnings.
The actual rebuilt ELF equals this first prediction byte for byte. Prior guard
bytes, all 98 other input keys and every other ELF byte remain fixed. Protected
data is exact across **189,088 bytes / 720 owners**. No dependency bypass is used.

```text
before ELF  05c247fb22b1ef93a931bf8dc4068a334c19ab6b4b1ea1fc64f6ea3befde655c
after ELF   cfa4611d4151c21bc820ea5a16ec2bfcf91d0daf897259469a8a314a0e80791f
after C     b145ca1b2ddd80f63ae8ea7113cf738e0758d7cf0fbc69a399622d39ed6ef90b
guards      197a60801a08f0db3ed2afa2461b3d692bd215cf21f78870609589fb06df9c41
```

## Next Matching Work

Keep **func_15095D34** open. Focus on the 151-word middle window, VA
**0x15095ED4..0x15096130**, while retaining the 104/91 literal spans. Resolve
the two constant roles, fractional-T versus flip-flag lifetime, flip branch
schedule and macro homes. Current macro words/halfword use SP+8/+4/+6 where
retail uses SP+0xC/+8/+0xA; equal frame size does not close these six accesses.

Use the existing IDO compiler observation helpers to compare the selected and
mixed-constant forms if source evidence cannot settle the allocation. Require
fired probes, unchanged compiler hashes, completed owned children and normal
object/relocation/pool identity. Do not add unused locals, physical-register
bindings or bulk guards to conceal this boundary. Start from a new immutable
baseline for the next accepted stage, retaining all semantic/private/image gates.

The wider Game matching goal, original callers and inherited-stack C deferrals
remain open. Routine Claude calls for this fitting stage: **zero**. No push or
host-port/frozen Release build, modification or launch occurs.

## Progress And Banking

Fresh official matching totals remain **Game 2,922/4,828 (60.52%)**, **total
3,595/5,501 (65.35%)**, different **1,906**, drift **0**. Init 492/492 and
Debugger 181/181 converted C routines remain exact. Conversions remain
5,501/6,044 (91.02%), converted bytes 86.04%. Root README already contains
these same verified figures/date and is not given a matching narrative.

Tools **aff42ac** banks the four experiment/checkpoint/test files before the
consumer source/pin/docs commit. Preserve older mirror HEAD **ddbdd16** and
all **811** initial dirty-file hashes, adding only four absent files for
**815** dirty paths. Copies are byte-identical; do not commit/reset the mirror.
Wait for the consumer's incremental graph hook without a full scan or purging
retained excluded nodes. No push or host/frozen Release action occurs.
