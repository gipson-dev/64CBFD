# Packed Scalar Callback Match - 2026-11-08

`func_15115F68` is byte-exact across all **60 words / 240 bytes**, with no
stack frame. Total **4,250 / 5,513 (77.09%)**, Game **3,577 / 4,840 (73.90%)**,
Init **492 / 492**, Debugger **181 / 181**. Address drift remains zero;
1,263 converted functions remain different. Another **161** exact functions
reach 4,411 / 5,513 and the active 80% goal. Conversion totals are unchanged.

## Source and callback interface

Owner: `conker/src/game/generated_142560.c`. VA 0x15115F68..0x15116058;
ROM 0x143418..0x143508. The recovered interface is `void(u8 *state)`.
The original callback callers pass A0 as the state pointer and ignore both
integer and floating return values. The old zero-return C placeholder is
not used as ABI evidence. No provider or caller source is changed.

An aligned pristine-image census finds no direct J/JAL entries and one
pointer at ROM 0x22D78C / VA 0x80088CCC. It is the first word of row **5**
in the twelve-byte rows of `D_80088C90`, whose base is ROM 0x22D750 /
VA 0x80088C90. That row is `(func_15115F68, func_15115EDC, 0)`.

The original 22-word registration path in `func_1509E900`, from
0x1509EBBC through the branch delay at 0x1509EC10, computes the row from
script word +8, copies its callbacks to state +38/+78, and copies the low
third-word byte to +92. Connected execution exercises every original word.

The two original JALR sites are 0x15113EE8 and 0x15113FC0 in
`func_15113E54`. Windows of seven and nine words qualify the pointer load,
A0 transfer, call delay, return, loop update and subsequent command setup.
An additional fifteen-word window begins at 0x15113FA0 and qualifies the
callback-pointer load in the taken branch's delay slot. Thirty-six caller
cases run each of retail, normalized and raw bodies; poisoned V0 returns
are ignored. Full execution of either larger parent is not claimed.

## Recovered behavior

The packed word at state +3C supplies four **signed** byte values by numeric
bit position: low byte is divisor, bits 16..23 are increment, bits 8..15 are
upper limit and bits 24..31 are lower limit. Repeated typed word reads and
signed-byte locals recover IDO's original common load and extraction lifetimes.
Numeric casts preserve their meaning on both big-endian MIPS and native
little-endian C. The wider game meaning of this scalar remains unnamed.

- A nonzero divisor divides float field7C by the signed divisor, adds the
  signed increment, then adds the old float field0. These are separately
  rounded single-precision operations in that original order. This path
  executes the ticks-address LUI but never reads the ticks word.
- A zero divisor multiplies the signed increment by `D_800BE9E4` modulo
  32 bits, interprets the low word as signed, converts it to float and adds
  the old field0. Unsigned C multiplication preserves the low-word product
  without signed-overflow undefined behavior.
- Reload field0. If the upper limit is less than it, store float(upper).
  Otherwise, if it is less than the lower limit, store float(lower). This
  ordered if/else-if matters for reversed limits and NaNs.
- Clear float field80, then field7C, to **positive zero**.

## Four derived scheduling guards

The complete semantic C body emits **60 words**, its original zero-byte
frame, two original data relocations, and every original FP/memory/control
instruction. Four expected-word guards swap two independent pairs of integer
shifts at byte offsets 1C/20 and 24/28. They preserve both pairs' complete
input/output dependency sets. Neither pair traps or accesses memory. No FP
instruction, branch, relocation, operation, register role or function length
changes. Both raw and normalized bodies consequently have identical literal
states at every executed memory fault cut and identical FP instruction operands.

Raw C SHA256:
`abef16ac79e720429a87b317554d3bd063fc83cdd94040a085a60443c84731ad`.
All 60 individual raw-word corruptions, both altered bindings, each of four
stale guard words and four unexpected guard relocations fail qualification.
The inherited guard CSV is an exact prefix. All 24 register-metadata byte
corruptions are rejected as well.

## Complete owner, actual Make and literal image

The frozen baseline contains **104 inputs**, including the exact compiler
tools, SDK headers, original caller/registration/table sources, linker inputs
and production predecessor. The normal O2/g3/MIPS2/O32 profile and Makefile
are unchanged. All **83** other raw and padded functions, all owner data
pools and register metadata, and all **42** original case labels are fixed.
Strict and production padders agree across the complete 84-function owner.

The actual five-command Make recipe reproduces the qualified complete owner.
Three independent GNU links test the two bindings at original and rebased
addresses, including signed LO16 carry boundaries. The literal full-ELF
predictor permits exactly **156 changed bytes**: the restored function body
and its symbol size, from 12 to 240 bytes. There are **zero exclusions** and
no symbol/string order permutations. All 6,053 function addresses, all other
function bodies, 720 protected data owners and 189,088 protected data bytes
remain fixed. Four corruption controls reject changed code, header, symbol
size or protected data.

## Execution qualification

Both tools configurations pass six focused checks before and after
installation, in four sequential runs with exact module/helper fingerprints.
The sibling configuration uses a scratch overlay for the three new modules;
any missing helper fallback is explicitly recorded and read-only. Its HEAD
and 2,434 inherited dirty paths are preserved. Both configurations also pass
a fresh shared smoke check. Three unchanged synthetic shared regressions per
configuration are explicitly reused by exact hashes, rather than called fresh.

- **2,843 guest cases** execute retail, normalized and raw bodies. All four
  signed byte positions exhaust 0..255. Cases include signed tick products,
  byte extremes, reversed/equal limits, signed zeros, infinities, bounded NaN
  behavior, five global-alias layouts and both stack phases.
- All **59 reachable words** execute. The duplicate lower-byte MTC1 at
  0x15116020 follows an unconditional branch and has no incoming branch
  target; the branch-likely delay slot supplies its reachable counterpart.
  The unreachable word is preserved and is not counted as executed.
- **38 executed memory fault cuts** compare complete literal states across
  all three bodies. The two shift permutations complete before any later
  memory or FP access. Saved GPR/FPR lifetimes and FP operands agree.
- **2,510 native cases per executable** pass at O0/O2/O3 with trapping UBSan.
  Every state byte and both canary regions are checked. Twelve effective
  controls reject the stub, unsigned interpretation of each byte, wrong
  pending field/division/tick mask, changed addition order, independent
  clamps, wrong clear address and negative-zero clears. A cancellation
  fixture specifically distinguishes the two addition orders.

Numerical guest checks use a bounded nontrapping IEEE-single round-to-nearest
model. They do not emulate hardware FCSR flags/traps or legacy N64 NaN
payload rules. The separate literal scheduling proof preserves the exact FP
instructions, operands and PCs; it does not depend on that model to justify
the four integer-only guards. Native NaN-producing cases are excluded from
bitwise host comparisons. Guest aliases are not claimed as native aliases.

Production compiles exactly one C owner with no C diagnostics. The installed
ELF equals the complete prediction. `make all` retains the expected checksum
exit 2 while other functions remain unmatched, separately from successful
compilation/linking and the fresh matching recount. `progress.csv` is unchanged.
The README changes contain aggregate status rows only.

Production ELF: `dcb555ac9ca55bad1eb96fa40b6aef6b6b8fd58b693a452a86050b0f56fcad28`.
Binary: `ab6a82cdd0abb85f6e0845a2ea51ac22e70038c52a2ec5c0c80d3eb9760e4f20`.
Owner: `d53ec6fb6196a81965b0733566677467c5b0505202b9551e2d7b7c4ec0ae84ef`.
Guard CSV: `06cc6c67e6b7af7ab0e60ecad7733faef8aefdc26aee4eb326c1a391b5d386c3`.

## Resume boundary

Next ordinary C candidate: `func_151AE2BC`, a 59-word leaf in
`generated_1D92F0.c`, pending complete interface and floating-point recovery.
It remains uncredited. The smaller handwritten/nonstandard-register routines
recorded in Note 2180 remain separate restoration work, without false C credit.

Scratch receipts: `conker/build/game-packed-scalar-15115F68-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
retains unscanned existing nodes and audits changed-path relocations; it is
not a full-corpus extraction. Frozen host Release artifacts are untouched.
