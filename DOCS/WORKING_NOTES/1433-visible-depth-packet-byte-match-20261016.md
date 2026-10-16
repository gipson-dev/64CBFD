# Visible-Depth Packet Byte Match

Date: 2026-10-16. Consumer predecessor **04e6726e**, tools predecessor
**51f51e1**. Continue the Game C-matching goal from Note 1432; this closes
one routine, not the additional-source or whole-Game queue.

## Recovered Contract

**func_150958B0**, owner `conker/src/game/generated_C1D70.c`, original
`conker/asm/C1D70.s`, spans VA **0x150958B0..0x15095A48** / ROM
**0xC2D60..0xC2EF8**: **102 words / 408 bytes**, frame **0x48**, saved S0/RA.
Replace the zero-return placeholder with:

```c
Gfx *func_150958B0(Gfx *output, s16 *packet, s32 *visible);
```

Read three signed coordinate halfwords and invoke the restored eight-input
projector func_1509563C with maximum 4000.0f. Rejection clears the **whole
visible word**, returns the unchanged cursor and never calls the visibility
provider. Success invokes the existing typed func_15095B08 with packet,
projected X/Y, divisor, integer flag **1** and the actual output pointer.
Its scalar return is ignored. Only a nonzero **whole visible word** emits
pipe-sync / primitive-depth commands and advances the cursor by 16 bytes.

The live scale **D_8009DEC0 = 16352.0f**, bits **0x467F8000**, is loaded
after the provider. Preserve the float operation order
`(depth / divisor) * scale + scale`, its **unsigned** conversion and low-16
depth packing. Do not substitute the signed conversion used by func_15095760.
All FP arithmetic and the retail FCSR save/restore/conversion sequence emit
directly and already match; no instruction in that sequence is patched.

## Compiler And Guards

Initial SDK-macro form emits 102 words / frame 0x48 with 18 differences.
Capturing the scale before the commands fixes order but moves the frame to
0x50; reject it. Reusing X storage or a union adds actual private accesses.
The selected complete semantic C reuses one command pointer and captures
the scale, recovering frame 0x48 with only **four scratch-GPR words** left:

| Offset | Expected | Replacement | Closed Role |
| --- | --- | --- | --- |
| +0xD4 | 02001025 | 02001825 | Second-command cursor V0 -> V1 |
| +0xD8 | AC580000 | AC780000 | Matching command-store base |
| +0x178 | 00084C00 | 00085400 | Shifted result T1 -> T2 |
| +0x17C | AC490004 | AC6A0004 | Matching result/base use |

Decode the intervening **+0xDC..+0x178** block and prove it does not touch
V0/V1/T1/T2; +0x180 overwrites V0 with the final cursor. A forbidden-register
control directly fires this proof, independently of the raw fingerprint.
Append exactly four expected-word guards; preserve the entire old manifest
as an immutable byte prefix. No branch, call, frame, saved-register lifetime,
FP/FCSR operation, relocation, compiler profile or shared helper changes.
This is a **guard-backed linked match**, not a raw direct compiler match.

```text
raw body a4914ad4ab2c1752165bb720e937dd2ceed8b5d95a078d9d12e977f0dc993554
```

## Fresh Qualification

Nine pre-install tests pass in **88.966s**. Final **12 tests pass in
133.716s**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_visible_depth_packet tools.tests.test_game_visible_depth_packet_installed -v
```

- **1,440 paired connected guest cases** compare original and raw C public memory, return cursor and full provider arguments. Exercise clipping, signed coordinates, visibility 0/1/0x100/negative/full-word values, ignored provider returns, stack phases, live scale/private-depth mutations and guest packet/output/status aliases. **101/102** target words execute; one repeated MFC1 is unreachable in this bounded path set, not claimed covered.
- **Native32 O2/O0**, separate translation units, real SDK headers and command-macro reference, selected-C UBSan: **128 cases each**. Restrict native casts to finite values with unsigned-representable integer parts; no native private-stack alias or out-of-range-cast acceptance claim.
- **84 conversion-fragment cases**, 31 retail words at +0xFC..+0x178, reach 30 words and cover negative fractions, negative integer sentinel, 2^31 carry, largest float below 2^32, 2^32, NaN/Inf and three saved control snapshots. This reuses the bounded truncation/restore oracle, not full hardware flags, rounding modes, traps or portable invalid-C-cast semantics.
- All **nine compiled guest / eight native negatives** reject observably. Map a wrong-scale negative's actual linked literal pool before executing it; an unmapped read, unsupported instruction or compile failure does not count as an effective control. Native fixture argument and conversion bounds, and fragment initial-FCSR bookkeeping, were corrected before acceptance.
- All **102 physical raw-word / four binding / four guard corruptions**, extra-pool and metadata controls reject. Preserve all **18** other compact owner bodies and relative relocations, including the previous projection/draw pair. Three independently assembled original rebase sets change entry and all three external bindings and match normalized output literally.
- Check all **97** frozen and live inputs, physical code/callee/symbol/string corruption controls and both strict successor-fixture stages. Every unaffected ELF byte and **94** other input keys remain fixed. Protected data is exact across **189,088 bytes / 720 owners**.

The aligned full-US-ROM word scan finds no direct JAL or absolute-pointer
word for this entry. This does not exclude computed references or prove dead
code. The real projector executes with a bounded opaque matrix provider;
func_15095B08 remains a typed zero stub, so this is not full natural
visibility/render/gameplay acceptance. Prior unchanged neighbor-suite receipts
are prior evidence, not fresh reruns. Routine Claude calls: zero.

## Complete Image And Progress

Capture the old owner object and link script before production edits. The
baseline full link reproduces the predecessor exactly. Preserve the rejected
slot/extent-only image, SHA **65158999162d23d8fe6329d5e3d257482181df623640085d0eb74d6a2b5e5eba**:
it misses two exact symbol/string swaps, **D_8009DEC0 <-> D_80090820** and
**D_800CC284 <-> D_800A3D14**. Model all **32** serialization bytes explicitly
and verify canonical definitions unchanged. Do not exclude metadata.

The standard guard-dependent guest rebuild exits zero with pre-existing
warnings, and a sequential repeat reports ELF/progress up to date. The
complete ELF equals its first pre-install prediction: **317 changed bytes =
285 code/extent + 32 metadata**, target extent **12 -> 408**, no exclusions.

```text
before ELF 69c218a15ca4353aecda5233b8258f1f36da39a56b788a82375a0d7ffdb4e333
after ELF  0896a6bb14a5780fe6c88d04cd7ece72fa460336afa8d4dbd3f739af0d079f66
after C    ea844704626b560ae270459e7bee5469474d0f50c3c9c09a67e3094f5a409aea
guards     e41413f066e143b17c98ae0254dbec2f1419d8e3479d332ec3d278a73603bc90
```

Fresh official totals: **Game 2,921/4,828 (60.50%)**, **total 3,594/5,501
(65.33%)**, different **1,907**, drift **0**. Init 492/492 and Debugger
181/181 remain exact. Conversions remain **5,501/6,044 (91.02%)** and
converted bytes **86.04%**. Root README changes only the two aggregate rows.

Tools **23a25ff** banks the five experiment/oracle/checkpoint/test files
first. Both tools copies pass Windows syntax and all eleven shared WSL
padder tests; `make tools-check` passes. The older mirror retains HEAD
**ddbdd16** and all **796** original dirty-file hashes, adding only five
previously absent files for **801** paths. Do not commit/reset that mirror.
Bank consumer C, four guard rows, tools pin and docs separately, and let
the normal incremental Graphify hook finish without a full scan or dropping
retained excluded nodes. No push or host-port/frozen Release action.

## Next Audit

**func_15095B08** is the next actual unfinished provider in this owner:
VA **0x15095B08..0x15095D0C**, ROM **0xC2FB8..0xC31BC**, **129 words /
516 bytes**, frame **0x18**, saved F20/F22. It clears the output word,
gates on signed packet extents +6/+8, scales through D_800380A0/A4 and
the current 0x180-byte frame, reads unsigned descriptor dimensions through
packet +0x10, performs rectangle/viewport overlap tests and writes seven
globals D_800D2C70..D_800D2C88. Audit early-exit writes, ignored scalar
return, float lifetimes, mode-dependent scales and all boundary equalities.
Do not treat the existing typed zero stub as a functioning flag writer.
Keep func_1516D738/func_1516FE1C's inherited-stack C deferrals, lower draw
providers, original callers and the wider Game goal open.
