# Mirrored Texture Candidate And Private Gap

Date: 2026-10-17

Continue [Note 1476](1476-clipped-rectangle-direct-match-20261017.md) from
consumer **b0ac1a85**, tools **d52744e**, both initially clean.
This checkpoint audits the complete next routine, **func_1517FB9C**.
The recovered SDK candidate is **not byte-exact, not installed and receives
no C matching credit**. Keep the same target and wider Game objective open.

## Full Retail Contract

- Owner: `conker/src/game/generated_1AC2F0.c`.
- Original: `conker/asm/1AC2F0.s`.
- VA **0x1517FB9C..0x15180580**, ROM **0x1AD04C..0x1ADA30**.
- **633 words / 2,532 bytes**, frame **0xD8**, no JAL.
- The live routine is still its original 12-byte C placeholder.

The candidate's recovered interface is:

```c
Gfx *func_1517FB9C(Gfx *commands, s32 size, s32 textureSize,
                 f32 offsetX, f32 offsetY, s32 view);
```

The pointer/integers precede the floats, so offsetX arrives as a raw word
in A3 and offsetY at incoming SP+0x10, not a leading-float F12 ABI.
All four original call sites are in the still-unrecovered
**func_15180580** parent. No live C caller or prototype is silently repaired.
The source archive's integer-typed viewport accesses and apparent
uninitialized unksp32/unksp36 locals are not adopted. Those retail halfword
loads alias the low halves of prior fullword step stores at +0x30/+0x34.

Read extentX/extentY from the live 0x180-byte viewport row, add the projected
offsets from D_800DDDE8, then emit **four** gSPScisTextureRectangle expansions.
The output is **24 command words / 96 bytes**, with the expected cursor
advance in regular storage:

| Quadrant | X Interval | Y Interval | Step X / Y |
| --- | --- | --- | --- |
| Positive / positive | centerX+offsetX through +size | centerY+offsetY through +size | negative / negative |
| Negative / negative | centerX-offsetX-size through centerX-offsetX | centerY-offsetY-size through centerY-offsetY | positive / positive |
| Positive / negative | positive interval | negative interval | negative / positive |
| Negative / positive | negative interval | positive interval | positive / negative |

The rate is the unsigned conversion of the float32 textureSize/size ratio
times 1024, narrowed to 16 bits before negation. Keep float32 operation
boundaries, quarter-pixel signed-halfword clipping and fractional origins.
Crucially, the SDK tests X negativity after s16 narrowing, but tests Y
negativity on its **full expression word**. The Y product still uses s16.
A native control that narrows the Y predicate demonstrably changes output.
Each rectangle emits E4, E1 and F1 commands through the actual SDK macro,
not a hand-written replacement of the domain logic.

## Candidate And Measured Gap

The first semantic form is **626 words / frame 0xD0 / 618 ordinal differences**.
An explicit viewport-record pointer recovers **frame 0xD8**, four correct
global bindings and all **27 unchanged raw/padded owner neighbors**, but
still has **626 words / 604 ordinal differences**. That count includes its
**seven-word length deficit**; it is not seven remaining scheduling differences.
The inherited pool, compiler profile and entire guard manifest are unchanged.
The normal padder does not change this candidate's 626 emitted words.

Pinned diagnostic raw text SHA-256:
`95fe7a5372fc506f0c5ccf7035f020cd419705cdf4ef250cfa601b104e8b6a8f`.
Bindings: D_800BE628 **+0x18/+0x1C**, D_800DDDE8 **+0x30/+0x34**.
All 626 word controls, five binding controls (four plus an unexpected entry)
and 16 inherited compact-pool byte controls fail closed.

Representative complete-function screens:

| Source Shape | Words | Frame | Ordinal Differences |
| --- | ---: | ---: | ---: |
| Explicit record pointer, u16 step | 626 | 216 | 604 |
| Explicit float span | 626 | 216 | 605 |
| Y-positive assignment first | 622 | 216 | 599 |
| Word-sized masked rate | 620 | 208 | 608 |
| Cached negative phases | 622 | 224 | 608 |
| Positive-X array storage | 659 | 208 | 647 |
| Four-coordinate array | 750 | 168 | 736 |
| Signed-halfword rate | 589 | 208 | 617 |

These are diagnostics, not installable alternatives. Do not infer correctness
from a closer word count, substitute signed rate semantics, add arbitrary
volatile/fake arithmetic or normalize hundreds of words without a certificate.

Actual execution identifies the first private difference after the two
matching incoming homes:

| Trace | First Private FP Store PC | Frame Offset | Value |
| --- | --- | --- | --- |
| Retail | entry+0x70 | +0x54 | positiveX = 148.5 |
| Candidate | entry+0xAC | +0x60 | positiveY = 93.25 |

The original keeps offsetY/positiveY in F16/F18 and spills positiveX;
the candidate instead keeps positiveX and spills positiveY. Retail also
retains masked positive and negated step homes at **+0x34/+0x30**.
The diagnostic execution performs **83 original versus 78 candidate memory
accesses** in this case. That five-access gap does not prove the seven-word
deficit has one cause. Private bytes, instruction order and fault prefixes
are not equal even though public command packets agree.

## Qualification And Limits

All **seven final audit tests pass in 150.349s**. They explicitly
require the candidate to remain uninstalled and unmatched:

- Independently assemble/link all **633 original words** at retail bindings
  and require complete equality with the ROM span.
- **15,576 paired guest cases**, both stack phases, all 24 output words,
  exact public store order, 96-byte return advance and no opaque helper calls.
  Cover signed/full-word indices, wrap, fractional/signed-zero/nonfinite
  inputs, zero/negative/large sizes, rate high-bit recovery and invalid paths,
  and live viewport/projection/global output aliases.
- Naturally execute **631/633 original words**. The two missing original
  MFC1 words at +0x1F4/+0x308 are dead after unconditional branches.
  Candidate coverage is **622/626**; its four missing offsets are recorded
  as observed coverage gaps, not all asserted statically unreachable.
- **948 native32 cases per O2/O0 profile**, separate full SDK candidate and
  typed caller, UBSan, all 24 words and complete viewport/projection/output
  canaries. Eight effective controls all exit **22**, not a signal/trap:
  baked view, omitted projection, wrong ratio, X/Y direction, wrong phase,
  quarter units and the narrowed Y sign predicate.
- Three independently linked original/C **rebase pairs / 36 public pairs**
  change both globals, including HI16/LO16 signed-low carries.
  They do not claim instruction or private-state identity.
- **192 paired caller cases**, all four original sites, **7/9/12/7-word**
  windows. Execute the actual 633-word retail and complete 626-word C bodies,
  signed half/quarter size division routes, mixed float words, delay-slot
  homes, F20/S2 and incoming stack state. These are bounded windows, not
  the full unrecovered 991-word parent or natural-gameplay acceptance.
- **322 positively fired faults**, across both images/stack phases, confirm
  the requested access gate fires. The measured private mismatch remains;
  these are **not a fault-equivalence or instruction-guard certificate**.
- All **156 input entries / 147 distinct paths** reject corruption and
  remain equal to their frozen baseline. Game data is exact across
  **189,088 bytes / 720 owners / zero differences**.

Native scope is valid indices, finite/in-range conversions and arithmetic,
aligned float-backed output aliases under the existing GNU native32/
fno-strict-aliasing union-storage convention. Invalid indices/conversions,
wrap and fault state are guest-only; private output aliases remain unqualified.
The software nontrapping FP/FCSR model tests conversion-control restoration for four
initial control words; it does not establish hardware sticky/inexact flags,
enabled traps, CP0, pixels or full gameplay. No universal ISO effective-type
or all-input defined-C claim is made.

An initial focused run passed guest/native checks but hit a local test
namespace error in the private-state assertion. Correct it to inspect literal
memory and retain the exact first-spill assertions; the corrected five-check
run passes in 108.018s. The final seven-test run includes that correction.
No production or shared-helper fix is hidden in this harness correction.

## Advisory Reconciliation

One attempted/completed tool-free Claude analysis uses the existing
claude.ai / firstParty / Pro route and default Opus 4.8, with fresh help/auth
checks. Effective tools=[] / mcp_servers=[], one turn, zero tool-use events,
CLI exit0; no account/provider/model change, extra agent or retry.
Packet SHA-256:
`61e9014605b16ac3152c34922dc0b21e70ece83d2127439957551add45e3d3cb`.

Retain its response as advisory, not matching evidence. The claimed
word-count-neutral Y reorder is contradicted by the measured 622-word result,
including its size-left variant. The proposed seven-word spill explanation
is unproven, and its single-u16-rate suggestion already describes the current
candidate. No suggestion is blindly adopted. The wrapper's terminal exit1
was a Windows cp1252 error printing a Unicode arrow **after** the successful
CLI/receipt; recover the retained UTF-8 JSON result without rerunning the call.

## Unchanged Production And Bank

All production C source, normal ELF, CSV, guards, Makefile, archive and build
inputs stay unchanged. The normal ELF remains
`90fba53a4f9927a2528e5d77aee1076e1e5b05a2ab71b184f2425ec487fcaa3e`.
No normal rebuild is needed or claimed for this tools-only audit. Fresh
official matching remains Game **2,947/4,828 (61.04%)**, total
**3,620/5,501 (65.81%)**, different **1,881**, no drift. Init **492/492**
and Debugger **181/181** remain exact. Root README stays untouched.
Existing duplicate recipe warnings remain.

Tools **5deb8e2** banks four new files first. Both copies have four exact
task pairs / **eight ASCII/AST checks**. Eleven shared padder tests pass per
copy: active **0.032s + 0.021s**, standalone mirror **0.029s + 0.019s**;
consumer tools-check passes. All four mirror task paths were absent before
copying. Preserve mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**
and **all 1,025 initial dirty-file hashes**, producing **1,029 final paths**.
No mirror commit/reset, push, external dependency/tool configuration change,
host build/launch or frozen Release action.

Prepared-checkout reproduction, sequentially:

```sh
python3 -m tools.experiments.game_mirrored_texture_rectangles --candidate
python3 -m unittest tools.tests.test_game_mirrored_texture_rectangles -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover the entire SDK candidate and prove bounded public packet semantics.
- [x] Qualify actual retail words, native controls, callers, rebases and input gates.
- [x] Measure and preserve the private/fault gap instead of assigning false C credit.
- [x] Bank tools and the detailed handoff with production/README unchanged.
- [ ] Close the complete 633-word, private-home and fault-order requirements.
- [ ] Install only a fully qualified match, then continue the wider Game queue.

**Next: remain on func_1517FB9C.** Move from broad shape screens to a bounded
compiler-origin investigation of the first positive-X spill and positive/
negative rate homes. Reuse the read-only CFE/UOPT/UGEN capture approach with
this function's exact fingerprints and fully observed owned-child lifecycle;
the older text-measurer harness is target-specific and must not be run
unmodified as evidence for this routine. Establish which source lifetimes
actually select +0x54 and +0x30/+0x34, preserve full-word Y sign behavior,
then close all 633 words and private/fault gates. Do not treat public agreement
or a seven-word length gap as permission for a blanket patch batch. Wider
Game/additional-source matching, deferred pulse lifetime, query/sequence
engines, timing's 141 differences and full gameplay remain open.

Follow-through: [Note 1478](1478-mirrored-texture-upstream-home-provenance-20261017.md)
qualifies four target-specific compiler captures. The candidate's positiveY
and rate homes already exist in UOPT output. Five new tests pass; no source
installation, private/fault certificate or matching credit is added.
