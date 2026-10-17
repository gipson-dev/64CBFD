# Sequence Record Setup Frame And Private Home Recovery

Date: 2026-10-16. Consumer predecessor **9c930609**, tools predecessor
**332b6ba**. Continue **func_1501D348**, not another easier stub, from
[Note 1465](1465-sequence-record-setup-recovery-and-frame-boundary-20261016.md).

## Measured Progress

Recover retail's **0x78 frame**, opening saves/argument roles and all eight
observed private homes. The complete routine is still **not byte-exact or
installed**. Production conker/src/game/generated_49D30.c retains its stub.
Retail is **473 words / 1,892 bytes**, VA **0x1501D348..0x1501DAAC**, ROM
**0x4A7F8..0x4AF5C**. Keep the recovered void five-word interface and the
existing **O2/g3/no-unroll** profile.

| Complete Body | Words | Frame | Length-Aware Word Differences |
| --- | --- | --- | --- |
| Note 1465 recovery | 471 | 0xA8 | 405 |
| New FITTED | 473 | 0x78 | 273 |
| New PREHEADER | 474 | 0x78 | 275 |

These are two useful fits, not two matches. PREHEADER has the narrower
remaining instruction-shape problem despite its slightly higher pointwise
score: its first descriptor preheader now has the retail shape; the second
still emits one extra scale word. It exceeds the retail slot by four bytes.
Do not install, truncate, pad or credit either candidate, and do not repair
the old frame/home mismatch with guards.

The experiment is tools/experiments/game_sequence_record_setup_frame.py;
FITTED and PREHEADER have named source bodies with the same correct API,
typed counts/descriptors/runtime records, full-word sizes, live allocator
cell reloads, descriptor-group skip and ordered providers. Keep address-based
symbols. The shared word is named **value**, with a comment describing its
disjoint status/size/allocation/flag uses, not an invented global meaning.
The original recovery module's SELECTED remains INITIAL and unchanged.

## Source And Home Recovery

The 58 bounded screens separate declaration/home pressure from loop shape:

- Register-qualified locals and scoping the allocation temporary do not
  improve the original output. Removing five explicit cell-address aliases
  reduces the frame to **0x90**; the compiler still recovers their shared
  addresses and live cell accesses.
- Indexed row/descriptor expressions, ordinary for-loop lifetimes, direct
  total-halfword publication and explicit unsigned low16 allocation recover
  the **0x78 frame**. Some intermediate forms have wrong homes or saved
  roles; a frame/length score alone does not select them.
- Reuse one full word across disjoint phases, retain the separate byte-size
  value, and keep pointer-cell loads after the explicit allocation result.
  This recovers the original private-home block, not just its size.
- Retain the descriptor cursor across providers. Reinitializing it just
  before the second group removes its original saved lifetime and is
  rejected. Pointer-view, declaration, explicit-offset and union/carrier
  alternatives are recorded, not silently promoted.
- PREHEADER uses an independent first prefill cursor, then resets it to one
  for the later publication group. This recovers the missing original
  preheader initialization without an inserted guard. All source forms
  remain complete bodies; no retail-slot truncation is used.

Both retained fits directly preserve frame **0x78**, **S0-S5/RA at
SP+0x1C..0x34**, the first twelve words including the hook argument home,
and the original incoming homes **0x78/0x7C/0x84/0x88**. At every outgoing
provider, check literal values in these homes against the original:

| SP Offset | Observed Role |
| --- | --- |
| 0x3C | Auxiliary pointer-cell address |
| 0x40 | Preferred pointer-cell address |
| 0x44 | Fallback pointer-cell address |
| 0x48 | Runtime-loop byte offset / later per-record allocation cursor |
| 0x54 | Runtime pointer-cell address |
| 0x58 | Slot-times-four |
| 0x5C | Status pointer |
| 0x70 | Cached original bundle |

Raw text / sorted relocation-map SHA-256, **89 bindings each**:

```text
FITTED text
7788dad5751c126602de6768351244a490c80821b78d6106939d836bcfef8087
FITTED bindings
a38503432609c98b268268bf4f62232923fee37d648c62cf1e9857c56b2680f4
PREHEADER text
7591a7e391b9c2d3a36cd1e86e8200e5794d8f5f1ef149f0ec1b20bc2708e2e8
PREHEADER bindings
19aeaceffebfc1008e6faa7023b1bacc129f134af966962ced320d537e6cd331
```

Both compile without diagnostics or private pools. All **56 raw owner
neighbors** remain identical. Independently assemble the complete original
473-word artifact and compare every byte with ROM.

## Remaining Instruction Boundary

The register-free routing diagnostic is **not a guard plan or proof of
register allocation equivalence**. It preserves opcode/width/immediate/call
identity and checks branch destinations through the explicit word routing:

- FITTED lacks original word **95 / +0x17C**, the repeated cursor-one
  initialization, and has extra C word **278 / +0x458**. Original word
  **281 / +0x464** still has a different address-operation form.
- PREHEADER has no missing original word. Extra C word **279 / +0x45C**
  is **sll t8,s3,3**. Original word **281 / +0x464**, **addiu v0,a3,8**,
  corresponds to C word **282 / +0x468**, **addu v0,a3,t8**.
- All other routed non-register instruction fields agree, including the
  adjusted branch destinations. The many remaining GPR-field differences
  are still real raw differences, not credited as a match.

Resume from **PREHEADER's second descriptor preheader**. Resolve its
constant/induction source shape while retaining the correct frame, homes,
saved roles and first preheader. Do not repeat the rejected 58-screen sweep
as new progress or assume that masking register fields proves a safe patch.

## Fresh Qualification

All **five final tests pass in 207.068s**, no skips:

- **242 fixtures x two stack phases = 484 three-way guest cases** execute
  retail, FITTED and PREHEADER. Visit every one of their **473/473/474
  words**. Compare with the independent ordered public reference and retain
  all eight positively fired diagnostic provider gates.
- Both C fits agree with retail on **the entire memory dictionary, including
  private stack bytes**, every ordered **R/W memory event**, complete call
  packets and the existing **31-lane provider snapshots**. At every call,
  compare literal **S0-S7/GP/SP/FP values and all eight homes above**. Final
  saved GPR/FPR/SP/RA ABI checks also pass. These are stronger observations
  than the previous public-only recovery, not full instruction-fault parity.
- **60 native32 cases per body per O2/O0 profile with UBSan**, no fwrapv or
  LTO. Compile each complete actual C body, actual restored reset and typed
  caller/providers as separate units. Check all **756 canonical fields**,
  bank padding/canaries, used arena bytes/gaps/guards, packets, snapshots and
  fired counters. Both normal profiles return zero for both bodies.
- All **sixteen native controls**, eight per body, compile and execute,
  failing functionally with **21/22**, never accepted signals or sanitizer
  traps: truncated descriptor size, missing group skip, wrong capacity,
  stale runtime cell, wrong process index, signed total, stale request
  status and wrong callback parameter.
- All **58 bounded source screens** compile without diagnostics/pools and
  pass two diagnostic witnesses each. Only the two retained fits receive
  the complete guest/native qualification; do not generalize that evidence
  to all alternatives.
- Oversized screens can shadow the next provider's retail address if run
  at the retail entry. Execute such research at private **0x16010000** in
  the same MIPS jump region, without changing any word. Two positive controls
  reject overlapping-provider and wrong-jump-region placements. FITTED's
  full guest runs use the real **0x1501D348** entry; PREHEADER's use the
  private entry. This is not an installed layout or independent-rebase proof.
- All **136 live production inputs** remain unchanged; independently
  corrupting every input fails closed. Production source, caller, guards,
  Makefile, image, progress CSVs and root README are untouched.

Keep the prior provider boundary: guest reset uses its ordered reference;
native reset executes the actual C with a bounded clear helper. Other
providers, bzero and allocations are bounded contracts, not complete retail
helpers or hardware. Native arrays cover valid slots zero/one and bounded
groups; large u16 capacities use the documented fired count-shrink diagnostic.
NULL allocation failure, arbitrary aliases, complete caller/helper chains,
scratch-register/PC/fault-prefix equality, independent rebases and full
gameplay/host acceptance remain unqualified.

## Bank And Resume

Tools **b9e0781** banks the two new experiment/test files before the consumer
pin. Both copies have identical pairs and **four ASCII/AST checks**. All
eleven WSL padder tests pass per copy: active **0.038s + 0.023s**, mirror
**0.028s + 0.018s**. Consumer tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **962 initial dirty-file
hashes** and its independent history; **964 final dirty paths**. No mirror
commit/reset, push, Claude call, REA setup, dependency/configuration change
or frozen host Release action.

No production rebuild or matching remeasurement is claimed for this
research-only bank. Last installed measurements remain **Note 1464**:
Game **2,939/4,828 (60.87%)**, total **3,612/5,501 (65.66%)**, different
**1,889**, zero drift, converted **5,501/6,044 / 86.04% bytes**. The frozen
ELF is still
**17e327a95fcf43c50ac2611a19461980ad1d44664a3c3a218d593f35e26cd4ab**.
Unchanged prior installed-function suites are historical, not fresh tests.

Reproduction in the prepared consumer checkout, sequentially:

```sh
python3 -m tools.experiments.game_sequence_record_setup_frame
python3 -m unittest tools.tests.test_game_sequence_record_setup_frame -v
make tools-check
```

Use --group with the experiment only for a deliberate bounded follow-up;
the recorded full sweep is --group all. Do not run producers/qualifiers
sharing this scratch directory concurrently.

- [x] Recover the real frame, private homes and opening saved/argument roles.
- [x] Qualify both complete fits against literal memory/events and every call cut.
- [x] Qualify both native bodies, effective controls, input preservation and bounded screens.
- [x] Bank tools first, preserve both copies, update concise indexes; no root README change or matching credit.
- [ ] Resolve PREHEADER's second descriptor preheader and remaining GPR/scheduling fields.
- [ ] Qualify the eventual match's caller/helper, private/fault/rebase and first complete-image prediction boundaries.
- [ ] Only then install, rebuild, audit and measure fresh matching progress.

The wider Game objective stays active. Timing's 141 differences and other
additional-source/Game recoveries remain separately open.
