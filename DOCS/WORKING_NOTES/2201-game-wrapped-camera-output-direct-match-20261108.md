# Wrapped Camera Output Direct Match - 2026-11-08

`func_151794C8` emits all **78 words / 312 bytes directly from semantic C**,
with its original **0x40 frame** and **zero guards**. The isolated body,
complete owner, both padders and actual Make agree. The literal full-image
prediction changes **251 bytes**, with zero exclusions or metadata permutations.

Production: Total **4,270 / 5,513 (77.45%)**, Game **3,597 / 4,840 (74.32%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. **1,243**
converted functions remain different; **141** more exact functions reach
4,411 / 5,513 and the active80% goal. Conversion denominators and the
progress CSV are unchanged.

## Reused recovery and measured interface

Owner `conker/src/game/generated_1A6360.c`, original `asm/1A6360.s`.
VA **151794C8..15179600**, ROM **1A6978..1A6AB0**. Interface:

```c
void func_151794C8(void);
```

Reuse the qualified semantic body and model from **func_150E41C0 / Note2197**.
Only the function name, math entry bindings, output symbol and existing
global-pointer type differ. Keep D_800DBFF0 declared asu8* in this owner;
explicit struct108 views recover the measured camera fields without changing
neighbor interfaces. Math entries have f32(f32) ABI; output D_800DD438 is
three halfwords. The sole caller ignores V0; emitted code retains its final
output-address value without inventing a portable scalar return contract.

Snapshot/truncate float fields+0x2F8/+0x2FC/+0x300 to signed32 X/Y/Z before
any calls. Cache angle+0x398 in F20 across func_150AD78C and func_150AD780.
Compute vertical=500*first sine result and horizontal=-500*first cosine
result. Reload the live camera pointer and angle+0x3A0 after that pair, then
cache it across another pair. Preserve the first integer coordinate snapshots
even if controlled providers mutate or retarget the camera between calls.

```text
X = trunc(float(savedX) + (0.0f + horizontal * secondSine))
Z = trunc(float(savedZ) + (horizontal * secondCosine - 0.0f))
Y = trunc(float(savedY) + vertical)
```

Write low16 outputs at offsets0,4,2. The explicit zero and named integer
updates preserve original single-precision operations and compiler schedule.
Homes remain F20/F21+0x10, RA+0x1C, sine+0x24, horizontal+0x28,
vertical+0x2C and captured Z/Y/X+0x34/+0x38/+0x3C. No source/profile search
or normalization was needed after reusing the already qualified body.
Raw SHA256 is the same instruction template:
`651429e7a352566b8269954498365931f232d56dbbce7a3a72b900a6c0577cdc`.

## Math-owner boundary and actual caller window

The original `asm/DAC30.s` and generated_DAC30 source are frozen with their
coefficient owner `asm/data/2441D0.rodata.s`. func_150AD780 is a three-word
phase-add entry that **falls through into func_150AD78C**, a larger polynomial
routine with further labels. D_8009F710 has bits3FC90FDB, value1.570796371.
Do not execute the three-word entry alone or claim SDK sinf/cosf equivalence.
This target's tests use bounded ABI providers for those entries; they do not
newly validate the complete polynomial, hardware FCSR or math-leaf accuracy.

Pristine aligned census finds one direct call at ROM **1A6940 / VA15179490**,
in func_15179008, with no aligned entry/interior function pointers. The full
original parent is304 words. Its **19-word tail window** at VA1517947C..151794C8
loads D_800DD436 into S2, tests signedhalfword count!=0, calls this target,
reloads the current signedhalfword, divides by30 and calls func_15179B14.
Then it restores RA/S0/S1/S2 and the parent's0x40 frame. This target's return
register is ignored. The window is qualified; the whole304-word parent and
followup body are not newly executed or reconstructed here.

## Focused qualification

Six checks pass sequentially before and after installation against mounted
and sibling tools, with exact source/dependency fingerprints.

- **2,215 guest cases**, **72 output/home alias cases** and
  **112 interrupted-access cuts** compare independent complete
  memory and literal original/C states. Every target word executes. Preserve
  F20/F21 and all callee-saved FP payloads, cached arguments, live pointer
  reloads, output arithmetic/order and provider/home mutation boundaries.
- **1,344 original caller-window cases** cover the
  signed count gate, initial and post-helper counts, truncating signed divide,
  exact followup argument and saved-register/frame restoration. All
  **168 zero-count cases** leave the camera pointer unmapped,
  proving the gated path skips target/provider accesses. A later zero count
  still submits quotient0 after the initial nonzero gate.
- **1,490 native32 cases per O0/O2/O3 profile**, trapping UBSan,
  reuse typed camera/output objects and complete canaries. All
  **12 semantic controls** are effective: wrong gains/signs/factors,
  missing stores/truncation, stale camera/angle reads and late snapshots.
- Three independent GNU links and12 rebased executions qualify all10 binding
  sites and high/low carry layouts. All78 word,10 binding,72 register-metadata
  and four whole-image corruption controls reject changes.

Numeric tests keep float-to-integer inputs finite and within signed32 range.
Nonfinite/signaling angle payloads are controlled-provider ABI probes, not
actual math-leaf acceptance. Synthetic private aliases qualify guest address
behavior rather than portable C overlap/fault semantics. The direct instruction
match is separate from hardware, gameplay and complete-parent acceptance.

## Owner, literal image, production and preservation

Actual Make retains O2/g3/MIPS2/O32 and its three compile/pad/assemble commands.
Both padders preserve all **nine functions / eight neighbors**, existing pools,
the exact register-mask union and **five exported interior labels**. Compiler
diagnostics are zero. No guards, shared headers or profile changes are used.

Independent full-ELF prediction replaces only the312-byte target body and its
12-to312-byte extent: **251 changed bytes, zero exclusions**, no metadata
permutations. All **6,052** disassembled entries keep their addresses; every
other body, extent and metadata byte stays fixed. Protected data remains exact
across **720 owners / 189,088 bytes**, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production compiles only this owner and equals the complete prediction.
Makefile, entire guard manifest, protected data and progress CSV are unchanged.
The existing full-ROM checksum mismatch (make all exit2) and duplicate
generated_12D630 recipe warning remain separate from the successful target
build/link/recount. Fresh shared smoke checks pass in both tools copies;
three unchanged helper regressions per copy are reused by exact fingerprints.
All **2,434** inherited sibling dirty paths remain preserved. **105 frozen
inputs** pin owner/math context, headers, layout, manifests, ROM and IDO compiler.
Baseline consumer d0f564c22732f98cda9483e2d983d8942a51bc0f, tools
ffe2833ea65f2ecb63921ab054a68166e0381625. Claude calls: zero.

ELF SHA256: `af2b43c34c3e00cb4b680ebda93526e206f78019a5da7e7d0dd7f59abf1d01ee`.
Binary SHA256: `c453ec367d2f077d5dbdd89a284776182c414b881b3ae2ad99ec23cc4b14c826`.
Owner SHA256: `7f0d02bb9107bc36af29d95ad77abd7a345dfa62ae14e41279b0ee88f31549c1`.
Guards SHA256: `e114c4f489dbfd2fafbad000982b4f5ba4e21702070234f75e2013e80afc8cc4`.

## Resume boundary

Next: **func_151A24A8**, an uncredited78-word threshold-driven record updater
in `conker/src/game/generated_1CC440.c`, original1CC440.s. VA151A24A8..151A25E0 /
ROM1CF958..1CFA90, leaf/no frame. Audit its one-pointer ABI, signed state at+38,
embedded signed-halfword table at+50, callers and actual profile before C.
Preserve six independent ordered gates, low-byte/halfword products, live tick
D_800BE9E4, state reload, render/control stores and final -9999 table sentinel.
Use defined wrapping arithmetic for arbitrary32-bit tick products/additions.
Complete every qualification gate before installing or claiming credit.

Receipts: `conker/build/game-wrapped-camera-output-151794C8-match/`.
Tools commit before consumer pin. Scoped Graphify refresh retains existing
unscanned nodes with evidence; it is not full-corpus extraction. Host Release
stays frozen. The80% goal remains active.
