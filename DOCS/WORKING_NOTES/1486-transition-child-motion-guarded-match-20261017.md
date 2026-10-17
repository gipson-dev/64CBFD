# Transition Child Motion Guarded Match

Date: 2026-10-17

Continue consumer **1b1d3922**, tools **5a038ed**, from
[Note 1485](1485-transition-burst-frame-recovery-and-native-qualification-20261017.md).
Recover the adjacent **func_150CFC60**, preserving the unresolved completion
burst rather than installing its 91-word mismatch. This is a guard-assisted
48-word match, not a direct raw-compiler match or completion of the Game goal.

## Retail Contract

- VA **150CFC60..150CFD20**, ROM **FD110..FD1D0**, 192 bytes / 48 words.
- Leaf, no frame; proper interface **s32(u8 *record)**, success result 1.
- Kind-13 callback at table **8008ACFC**. The original eleven-word dispatch
  window is **15154CE8..15154D14**, using table byte offset 52.
- Position X/Y at +0x10/+0x14; velocity X/Y, acceleration and floor at
  +0x70/+0x74/+0x78/+0x7C. Cache incoming vertical velocity/acceleration.
- Advance X with the live **D_800BE9A4** clock. Reload it for the quadratic
  Y step, then reload after the Y store for the velocity update.
- If **floor < updated Y**, clamp Y, take the updated vertical velocity's
  absolute magnitude, and damp X/Y velocities with **D_800A0878/800A087C**.
  Equality and unordered comparisons do not bounce.

Preserve the address-based public name. The semantic comment and local names
describe measured behavior, not a guessed original source symbol. Use the
SDK's existing fabsf intrinsic pragma convention; no new compiler profile,
constant pool, volatile declaration, fake padding or helper call is added.

## Exact Normalization

The complete semantic C emits 48 words with six HI16/LO16 symbol bindings.
Raw target SHA-256:
`02992176864e66405f1fdf98b7bf9438dee515ff46395010ddc0e0c544b88691`.
All **24 raw and padded owner neighbors** and all constant sections agree.
There are ten raw word differences, represented by ten explicit expected-word
guards appended to the existing manifest without rewriting prior records:

1. A closed floating-register cycle, F0 -> F2 -> F12 -> F0, over words 5..29.
2. Exchange independent setup words 8 and 9 (constant transfer/acceleration load).
3. Preserve retail's vertical-velocity add operand order at word 29.

An independent structural normalizer must derive exactly these ten pairs.
No instruction insertion, omission or relocation suppression is permitted.
The add exchange is not justified by ordinary commutativity: an explicit
two-qNaN case has a raw payload difference. Original and guarded words and
complete modeled state agree in that case. No FCSR/CP0/hardware NaN claim.

## Qualification

The focused suite covers:

- **388** ordinary/edge three-way original/raw/guarded guest cases, including
  18 global-to-record aliases, both stack phases, signed zero, infinities,
  subnormals and quiet NaNs; all 48 original words are naturally visited.
- **288 paired access-fault prefixes / 576 positively fired instances**,
  comparing original/guarded modeled state and ordered memory events.
- **16 paired original kind-13 callback-window cases**. This is the actual
  eleven-word call/restore/success branch, not the entire dispatcher.
- **Nine independent links / three symbol sets / 48 three-way rebase cases**,
  with signed-low carries and shared global storage. All guarded words match.
- **48 raw-word / six binding / ten expected-guard corruption controls**.
- **193 protected entries / 177 distinct paths**, with **386** positively
  fired live/frozen corruption controls. Only exact predicted successors
  normalize to the immutable predecessor; unknown bytes remain rejected.
- Four approved checkpoint paths, with twelve successor/fixture corruption
  controls after installation, and an independent whole-image prediction.

Prepared native32 uses the full C and a separately compiled typed caller,
360 cases per passing executable, all 128 record bytes and outer canaries.
Normal **O2/O0 + UBSan** pass. Real GNU linker clock aliases to record X/Y
pass at **O0 only**. Both optimized alias fixtures positively exit 22: GCC
caches the global across record writes, including in a diagnostic no-strict-
aliasing trial. Do not claim portable alias behavior or change production C
to fit this host extension. The original/guarded MIPS checks establish the
target's three live reads. Wrong inclusive floor, missing absolute value,
missing half factor and cached-clock controls all positively exit 22.

## First Complete Image

The independent prelink predictor reproduces the entire normal predecessor
ELF before accepting the candidate. It predicts **142 changed ELF bytes**:
141 code bytes within this callback and one symbol-size byte (12 -> 192).
There are **zero metadata exclusions or serialization permutations**.
Expected normal ELF SHA-256:
`c8b6937388a52c546239100bfbef8ef676ba5d8cdf9f08e9cf8c94638d1d00f5`.
Owner-source SHA-256:
`83826e31bf955ea31ecbd0f61f8ef25236c896fe136902b0d62beab8656e6e2f`.
Guard-manifest SHA-256:
`1d3539f53bcdea24a4ccdb2f0b3ccb5e09052e330aca62c4e5dc92d5be0a112d`.

The complete prediction and source/guard/helper hashes are banked before
production edits. The older burst screen gains only an exact approved-
successor adapter; none of its immutable predecessor hashes are weakened.
Keep its raw and frame-recovered drafts reproducible from those frozen inputs.

- [x] Qualify the full C, original caller, aliases, rebases and corruption gates.
- [x] Freeze the independently declared first complete image before edits.
- [x] Verify the rebuilt normal image, all data and installed suite.
- [x] Bank tools first, then consumer source/guards/docs/pin; remeasure progress.
- [ ] Keep func_150CF800 and wider Game matching open.

## Bounded Advisory Disposition

One attempted/completed read-only Claude call considered func_150CF800's
remaining object/register lifetimes, not this routine. Existing Claude Code
2.1.218 / claude.ai / firstParty / Pro route, one turn, default model, effective
tools=[] and mcp_servers=[]; no tool use or account/provider/model switch.
Packet SHA-256:
`928fb8efe2da087ac17c65f72859f40f4420494f86a341991fa417335baaf7ad`.
Ignored packet/answer/receipt/disposition live under
`conker/build/game-transition-burst-advisory-20261017/`.

The suggested tail fragment already exists in the candidate. Reject the
missing-pointer-home explanation: the generated code already stores/reloads
the transition pointer at SP+0x84, and its CFE home exists. There is no new
supported edit and no exhaustive impossibility proof for other lifetime
levers. Codex's byte-access diagnostics worsen 91 to 98 differences and are
also rejected. Keep **251 words / frame 0x108 / 91 differences**, uninstalled.
No retry, filler object or production burst conversion follows this review.

An initial Windows import-depth failure preceded any model launch; preparation
moved to WSL and the launcher reads the verified packet. This was not an auth
repair. The user confirmed the overwritten truncated-path scratch was disposable;
no recovery is needed.

No host-port or frozen Release action, dependency/provider change, push or
gameplay/hardware acceptance is part of this checkpoint.

## Installed Validation

The normal rebuild completes with the existing duplicate generated_12D630
recipe warnings and pre-existing warnings in unchanged compilation units.
All four live source/guard/helper/ELF artifacts equal their first predicted
bytes before banking the approved after fixtures. All **ten installed tests
pass in 29.536s**, with no skips. The full data audit passes: **189,088 bytes,
720 owners, zero differing bytes/owners**. Nominal C conversion rows do not
change because this replaces an existing C placeholder.

Fresh official matching: Game **2,951/4,828 (61.12%)**, total **3,624/5,501
(65.88%)**, **1,877** different, zero address drift. Init **492/492** and
Debugger **181/181** remain exact. The root README changes aggregate rows
only; historical measurements in earlier notes remain dated observations.

Eleven shared padder tests pass in the active checkout (0.060s) and standalone
mirror (six in 0.031s, five in 0.019s); consumer tools-check passes. All seven
task files match across both tools copies; fourteen ASCII/AST parses pass.
Preserve mirror HEAD **ddbdd16b**, **1,058 unrelated initial dirty hashes**,
and all other work. The one exact predecessor update plus six new files yield
**1,065 dirty paths**. No mirror commit, reset or push.

Fresh predecessor regression runs **eleven behavior/compiler checks in
80.770s**, covering both archived burst candidates, real compiler captures,
native endian limits and actual caller windows. Their two historical
literal-live-baseline mutation methods are not rerun against a known newer
source/image; the current suite's 386 live/frozen controls and twelve exact
checkpoint controls test that boundary instead. No baseline hash is rewritten
to accept arbitrary successors. A final unmocked freeze rechecks all 193 live
entries after documentation edits.

Tools commit **36eccea** banks the six new tools and exact predecessor adapter
first. The consumer commit contains only this callback, ten manifest records,
the tools pin, this note, concise indexes and two README aggregate rows.
No publish/push is requested. The broader Game goal remains active.

Prepared-checkout commands:

```sh
python3 -m tools.experiments.game_transition_child_motion
python3 -m unittest tools.tests.test_game_transition_child_motion -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
