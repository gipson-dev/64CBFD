# Parameter Defaults Initializer Direct Match - 2026-11-08

`func_151872B0` emits all **77 words / 308 bytes directly from C**, with
**no frame, no instruction guards, and no new compiler/table binding**.
Its existing O2/g3/no-unroll MIPS2/O32 profile remains unchanged. The guard
manifest and Makefile are byte-for-byte preserved. Four explicitly derived
linker metadata permutations preserve every named definition.

Production recount: Total **4,261 / 5,513 (77.29%)**, Game **3,588 / 4,840
(74.13%)**, Init **492 / 492**, Debugger **181 / 181**, zero address drift.
There are **1,252** different converted functions and **150** additional
exact functions needed to reach 4,411 / 5,513 and the active 80% goal.
Conversion rows and denominators remain unchanged.

## Source, widths and defaults

Owner: `conker/src/game/generated_1B1600.c`; original slice `asm/1B1600.s`.
VA 0x151872B0..0x151873E4; ROM 0x1B4760..0x1B4894. The recovered interface:

```c
void func_151872B0(s32 variant);
```

The current C census found only the placeholder and an old commented call
in the original caller's source. New declarations stay local to this owner:
six signed words, one f32 and two unsigned bytes, matching observed stores.
No speculative packed shared structure or header changes are introduced.

Every invocation first writes all nine defaults in the original order.
The selected full argument word then applies overrides:

| Symbol | Default | 0x21 | 0x22 | 0x29 |
| --- | ---: | ---: | ---: | ---: |
| D_800DE01C | 600 | 4800 | 2400 | 1200 |
| D_800DE020 | 180 | 4799 | 2399 | 600 |
| D_800DE024 | 90 | 4798 | 2398 | 300 |
| D_800DE030 | 1016 | 1010 | 1016 | 1016 |
| D_800DE034 | 0 | 1 | 0 | 0 |
| D_800DE038 | 1 | 4 | 4 | 1 |
| D_800DE03C | 1.0f | 1.0f | 1.0f | 1.0f |
| D_800DE040 | 1 | 0 | 0 | 1 |
| D_800DE041 | 1 | 1 | 1 | 1 |

Variant **0x14** changes only D_800DE041 to zero after the defaults. Other
full words retain all defaults. The float store is exactly **0x3F800000**;
there is no FP arithmetic. Retain repeated word/byte stores and untouched
gaps at the surrounding addresses.

## Compiler shape and case placement

Actual Make verified this owner's inherited no-unroll flag before the
first screen. The initial switch matched 77 words but differed in 33 word
positions. Literal override assignments differed in 44 positions, and an
if-chain shrank to 74 words with 42 differences.

The remaining difference was basic-block placement, not address-register
allocation: the initial 34 words already agreed. Ordering the source cases
as **0x21,0x22,0x14,0x29** gives all 77 original words and 18 bindings,
including the 4800 load in the branch delay slot, the late byte-clear case,
and the unreachable duplicate immediate at relative **+0x118**. The other
two tested block orders leave 13 and nine differences. This is a measured
matching source shape, not a claim to possess the original source text.

The accepted raw hash is pinned below and in the committed qualifier.
Rejected switch/literal/if-chain and alternate block-order artifacts remain
in the private stage. No register/scheduling or ROM-word patch is applied
to the accepted body.

Both padders agree on the full **32-function** owner; all **31** neighbors,
pools and exact register-mask union remain intact. The isolated target and
complete owner agree across all 77 words and 18 bindings. Actual Make's
three-command recipe produces the identical padded object. All C compiler
diagnostics are empty. A temporary assembler-option typo in the private
qualifier was corrected before these final checks; the compiler and actual
production profile were never changed.

## Original caller and execution evidence

The aligned pristine census finds one direct JAL at ROM **0x3BA2C** /
VA **0x1500E57C** in `func_1500E470`, with no aligned entry/interior pointer
literal or interior direct entry. The original six-word window through
**0x1500E594** loads the argument from caller SP+0x18 in the JAL delay slot,
then calls `func_15178EB0` and `func_15012FE0`. The target's return is not
consumed before these calls.

**64 connected cases** cover full-word variants, poisoned initial A0,
both stack phases, and a global alias with the caller's argument home.
An independent reference poisons the void target result. Bounded following
service models observe the initialized globals, mutate them between calls
and clobber caller-saved GPR/FP values. Final memory, observations and
registers agree with original and C bodies. These service models do not
qualify their formal arities or bodies, nor the complete larger parent.

Six focused checks pass before and after installation in both tools copies,
with four sequential final runs and exact source/dependency fingerprints:

- **2,144 guest cases** across three layouts, with full-word and negative
  variants. All **76 reachable words** execute; +0x118 remains preserved.
- **102 alias layouts / 510 cases** cover full/partial mixed word-byte-FP
  overlap and caller-home aliases. Independent complete memory, store
  values, widths and order agree. The routine performs no memory reads.
- **244 exact fault-prefix cuts** compare literal original/C states. F4
  always receives the exact one payload and every other FPR is preserved.
- **2,120 native32 cases at each of O0/O2/O3**, trapping UBSan, width
  assertions, all nine field values/FP bits and canaries. All **13** semantic
  controls are effective. Synthetic overlapping globals belong to guest
  fixtures; native C globals are distinct objects.
- Three independent GNU links and **18 rebased executions** qualify both
  halves of all nine global bindings, including low-half carries. Raw-word,
  binding and register-metadata controls reject 77,18 and72 corruptions.

## Closed metadata and whole-image proof

New external references change GNU ld hash-bucket order in four groups:

| Frozen order | Required order |
| --- | --- |
| D_800DE01C, D_800C3674 | D_800C3674, D_800DE01C |
| D_800DE030, func_15095A90 | func_15095A90, D_800DE030 |
| D_800DE034, D_80089570, D_80089120 | D_80089570, D_80089120, D_800DE034 |
| D_800DE03C, D_8008A284 | D_8008A284, D_800DE03C |

The predictor checks each original contiguous symbol/string group and
absence of additional references into its string block, then derives the
nine reordered entries and variable-length string offsets from the frozen
named definitions. Addresses, sizes, types and section identities of all
nine definitions remain unchanged, including `func_15095A90` and its body.
No symbol or string table is excluded or copied wholesale from the result.

The literal full-ELF prediction permits **323 changed bytes**: 232 body
bytes, two target-extent bytes (12 to 308), and 89 bytes in the four closed
metadata permutations. Actual production equals this prediction exactly,
with **zero exclusions**. All **6,052** disassembled entries retain their
addresses and every other body/extent is preserved. Protected data is
exact across **720 owners / 189,088 bytes**. All **17 image corruption
controls** reject changes in the header, body, extent, protected data,
each metadata definition and each affected string region.

Make compiles only this owner, links the predicted image, regenerates an
identical progress CSV and passes a fresh recount. The existing full-ROM
checksum failure (make all exit2) and duplicate generated_12D630 recipe
warning remain. Both shared tools smoke checks are fresh; three prior
helper regressions per copy are explicitly reused with identical hashes.
The sibling's **2,434** existing dirty paths are fingerprinted and preserved.

Baseline consumer `b2a3b36bc3bd8f27cf4a2620388b727316dbb62f`, tools
`c468a24e8109bdda273c4228b56204bc4297c79a`; **103 frozen inputs**.
Claude calls: **0**, since local compiler, instruction, caller and literal
image evidence resolve this routine without an advisory call.

Accepted raw SHA-256: `e0f4d4acd39253d1b990ef962522984888889bc2e5835d628919cfc186be5300`.
ELF SHA-256: `dee0e9366ad767c1bebcc74e3e27cfe6f2bd549327bfad500dd38cea5fd5244c`.
Binary SHA-256: `5dac22e3894dbd29175fa093e4166de7f77758f3f7e2060ea56a1342198c4bf7`.
Owner SHA-256: `129a84ddeb68450cc6c30743bba3fdbdbcf94f76e3f64aefc5abb38daa5f7d98`.
Guard CSV SHA-256: `f67f8d18908dc6db9ba58dfa2db4b4204a7202104e67173c35213711333f4dd9`.

## Resume boundary

Next: **`func_151BD2F8`**, an uncredited mirrored effect-pair constructor
in `conker/src/game/generated_1E73B0.c`. Body **77 words / 308 bytes**,
VA 0x151BD2F8..0x151BD42C / ROM 0x1EA7A8..0x1EA8DC; frame 0x60. Audit
callers, ignored argument homes and actual owner profile first. Null owner
skips construction. Otherwise capture owner+0x3B and its pointer into the
stack packet, preserve its mixed byte/half/FP widths and untouched padding,
and submit `func_15134DAC(packet,2)` twice. Each nonnull result receives
two zero bytes at+0x80 through the original memcpy call.

Before the second submission, reload and negate the packet floats at
SP+0x30 and SP+0x3C after the first helper/copy. Do not replace these live
reloads with cached initial constants. Preserve the global FP payload
D_800AA850, helper-clobber behavior, two independent failure paths and
padding/private-home boundaries. Existing SDK/factory oracles can assist;
complete all normal qualification/adoption gates before matching credit.
Graphify currently exposes placeholder/owner relationships, no accepted
recovery for this target.

Current receipts: `conker/build/game-parameter-defaults-151872B0-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
includes old-node retention evidence, preserving existing unscanned nodes
without claiming a new full-corpus extraction. Host Release remains frozen.
The 80% goal remains active.
