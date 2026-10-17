# Fixed Transition Constructor Direct Match

Date: 2026-10-17

Continue consumer **d8e056ad**, tools **6737b65**, after the tile emitter in
[Note 1482](1482-paired-scrolling-tile-windows-direct-match-20261017.md).
Install **func_150CF680** as a complete **96-word direct C match**, without
instruction guards, a new compiler profile, pool changes or build-rule changes.

## Complete Recovered Routine

- Owner: `conker/src/game/generated_FC5F0.c`.
- Original: `conker/asm/FC5F0.s`.
- VA **0x150CF680..0x150CF800**, ROM **0xFCB30..0xFCCB0**.
- **96 words / 384 bytes / frame 0x98**, SP adjustment at word 3.
- Proper interface **void(s16 id, u8 slot, s32 context)**. Retain the address
  symbol and add a succinct fixed-descriptor/transition-payload comment.

The function builds a complete **88-byte descriptor at SP+0x40** and a
**16-byte payload at SP+0x30**. The descriptor has its measured position,
scale, tag, signed ID, flags, size, color/duration bytes, packed control
words and trailing float fields. A private word-aligned byte union expresses
the selector cell at offset 0x44 without reading its unused word member.
The selector is the low byte of the signed word D_80082FA0.

The payload contains state 0 and float words 0.0f, -300.0f, 0.0f. Call
func_1515548C with exactly **seven integer/pointer words**:
`descriptor, 12, NULL, 0, 16, slot, context`. On success copy the complete
payload to returned-record+0x70. On null allocation make neither copy.
Both local objects have their actual copied extent; no out-of-object copy.

F12=7.5f and F14=1.0f are constant temporaries here, not additional formal
floating arguments. The other source's nine-argument rendering of this call
is not adopted. The existing recovered descriptor callers also use the
seven-word interface. No shared factory header or assembly definition changes.

## Actual Factory And Padding

Connect the actual **54-word func_1515548C** and **11-word SDK memcpy**.
For this constructor's NULL pair and flags 0x31, the factory asks its lower
allocator for **(0x57, context, 128, 1, slot, 1)**. On success its first real
SDK copy transfers **88 descriptor bytes** to record+0x10, then publishes
kind 12 at record+0x68. The constructor's second SDK copy transfers the
**16 payload bytes** to record+0x70.

All 96 constructor words and all eleven SDK copy words are naturally visited.
The factory's used paths visit **39 of 54 words**. Its optional pair-culling
path and flag-clear 0x5D path are not qualified by this constructor. The
lower allocator remains one explicitly scripted boundary, not a real heap
or gameplay acceptance claim.

Nine object-representation bytes remain inherited: descriptor offsets
**0x11, 0x42, 0x43, 0x45..0x47** and payload offsets **1..3**. Preserve them
in the guest, including scripted padding changes before the copies. Do not
zero them or infer portable C padding guarantees from native field checks.
The byte union provides alignment; no artificial initialized padding word,
volatile field, fake operation or unprototyped call is used.

The original six-word caller packet at **0x15027A04** loads the ID with LH,
the slot with LBU, and sets context 1 in the JAL delay slot. Its later branch
delay sets V0=1; that is not a callee return-value contract. Recover void
rather than retaining the false zero-return placeholder.

## Source Recovery

The complete initial typed candidate already has 96 words and frame 0x98,
but differs at 31 words. Seven halfword signedness forms do not change it.
Initializing header fields in offset order recovers the original temporary
roles and leaves eleven differences: one independent 72.0f constant setup
is scheduled late. Initializing that position component before the header
produces all **96 words directly**. This is a matching recovered C form,
not a claim that the original source text has been reproduced verbatim.

Raw target SHA-256:
`85acd74b8db2e84d805a1d4a410d1c876f8a61e6e77544b753f08628b6db79ba`.
Four bindings are pinned: D_80082FA0 HI16/LO16 at +0x9C/+0xA4, factory
R_MIPS_26 at +0x154 and memcpy R_MIPS_26 at +0x168. The normal padder
preserves the entire match, all **24 raw/padded owner neighbors** and all pools.

## Qualification

All **eight final installed tests pass in 70.848s**:

- **3,888 three-way guest cases**, original/raw-C/padded-C, independent full
  memory/call reference, exact modeled state and access order, both stack
  phases, signed/byte truncation, null and byte-unaligned returns, all nine
  inherited bytes and three scripted allocator-effect modes. Initial volatile
  FP registers contain arbitrary NaN patterns; no implicit floating arguments
  are supplied. Actual factory and both SDK copy invocations execute.
- **864 native32 cases per O2/O0 profile**, separately compiled full body and
  typed caller, UBSan, all 95 initialized input bytes, factory kind and all
  external canaries. Ten effective controls exit 22, not a sanitizer signal.
- A zero-padding control passes the native fields-only checks but changes
  copied bytes in the actual guest chain and fails the exact-object guard.
  Exclude only the nine unspecified bytes from native comparisons; native
  agreement alone is not a byte-match or installation certificate.
- Three independent original/C constructor rebase pairs, three independent
  factory links, all 96 constructor words equal and **432 state cases**.
  Move the global across signed low carries and relocate every helper target,
  including the actual SDK copy body.
- **1,332 three-way positively fired access-fault prefixes**: **3,996 fired
  instances**, null/non-null paths, both stack phases and live-padding stress.
  Actual instruction accesses number 60 on null and 273 on non-null. Not
  portable C faults, CP0/FCSR or hardware timing acceptance.
- **288 three-way original caller cases**, actual six words through the real
  join, complete constructor/factory/copies, narrowed inputs, context delay
  and later V0=1. Not the complete unrecovered dispatcher or natural gameplay.
- All 96 word controls, five binding controls and **182 protected entries /
  167 distinct paths** reject corruption. Cache only the injected fixture;
  re-read every live input afterwards. Strict before/after fixture controls
  reject unknown successors rather than accepting arbitrary current hashes.

Twelve affected checks also pass freshly in **51.749s**: the complete tile
suite, two reset image/successor checks and one candidate/context check each
for the fade and mirrored renderer. Their exact-successor adapter validates
preserved predecessor fixtures; it does not assert the entire current owner
or ELF is unchanged. Other broad suites remain prior evidence, not fresh tests.

## First Whole Image

Freeze the source, normal owner object, link script and all inputs before the
production edit. Reproduce the entire baseline ELF, then prelink the qualified
candidate. Independently predict the original 384-byte slot and function-size
change from 12 to 384 bytes; freeze this first complete source/image prediction.

The normal rebuilt ELF equals that prediction exactly:

- **292 target instruction bytes**, **two size bytes**, **294 total bytes**.
- No symbol/string permutation, other body/address/extent change, data change
  or metadata exclusions. No guard, profile, Makefile or retail-layout change.
- Game data remains **189,088 bytes / 720 owners / zero differences**.
- The already matched tile emitter and all other functions remain unchanged.

ELF SHA-256:
`9ff7f89b5a621b216a65e6018c4df1485c18cb4c4e92485bb5c94c53eb3592b4`.
Owner SHA-256:
`645d71e6cf77a1f7f2940e27c983c0c79a53f0ca9d292a15d296b6bf56dcf328`.
Only these exact successors and their verified frozen fixtures are recognized.

## Progress And Bank

Fresh Game **2,950/4,828 (61.10%)**, total **3,623/5,501 (65.86%)**, still
different **1,878**, zero address drift. Init **492/492** and Debugger
**181/181** remain exact. Nominal conversion rows/bytes stay unchanged because
the placeholder was already counted as C. README gets two aggregate rows only.

Tools **791eb66** banks six new files and two narrow predecessor updates first.
Eight exact task pairs / **16 ASCII/AST checks** pass. Eleven shared padder
checks pass per copy: active **0.023s + 0.033s**, mirror **0.020s + 0.030s**.
Consumer tools-check passes. Preserve mirror HEAD **ddbdd16b** and all
**1,045 unrelated initial dirty-file hashes**; update only two exact task
predecessors and add six files, for **1,053 dirty paths**. No mirror commit,
reset, push, extra agent, dependency/provider or host/frozen Release action.
The existing duplicate Makefile recipe warnings remain.

Prepared-checkout checks, sequentially:

```sh
python3 -m tools.experiments.game_fixed_transition_installation
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_fixed_transition_constructor -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

- [x] Install the complete 96-word typed constructor directly from C.
- [x] Qualify the seven-word interface, actual factory/copies and live padding.
- [x] Verify first whole image, every protected input, data and affected checks.
- [x] Audit neighboring **func_150CF800**, **251 words / frame 0x108**,
  and recover its complete uninstalled typed candidate in
  [Note 1484](1484-transition-completion-burst-candidate-and-frame-gap-20261017.md).
- [ ] Match all 251 words/frame and close private/native/installation gates;
  the current 93 differences and larger frame are not matching credit.
- [ ] Keep the 54-word fade, 633-word renderer, deferred pulse lifetime,
  wider Game/additional-source queue and natural gameplay boundaries open.
