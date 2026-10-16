# Packet Visibility Provider Byte Match

Date: 2026-10-16. Consumer predecessor **906aef35**, tools predecessor
**23a25ff**. Continue the Game C-matching goal from Note 1433. Close the
visibility provider, not the lower renderer or wider matching queue.

## Recovered Contract

**func_15095B08**, owner `conker/src/game/generated_C1D70.c`, original
`conker/asm/C1D70.s`, spans VA **0x15095B08..0x15095D0C** / ROM
**0xC2FB8..0xC31BC**: **129 words / 516 bytes**, leaf frame **0x18**,
saved F20/F22. Its existing typed zero stub occupied **28**, not 12, bytes.
Recover its six-input interface with a **void** return: both current callers
ignore the scalar register result; visibility is an actual full-word output.
Retain the owner-local 32-bit packet-address boundary used by those callers.

- Clear the whole visible word **before** reading either signed packet extent at +6/+8. A zero extent returns without reading the descriptor or writing any of the seven global draw inputs. A zero descriptor dimension is different: it still reaches global publication.
- Capture live float globals **D_800380A0/A4**, multiply the signed extents, and select the frame's +0x1C/+0x20 or +0x14/+0x18 scales using the complete mode word. Recover the existing **0x180-byte** view layout's eight formerly opaque float fields without changing its size.
- Load the descriptor through packet +0x10 and its **unsigned halfword** dimensions at +4/+6. Preserve the explicit unsigned conversion, float reciprocal and left-associated multiply order; do not import the reference draft's erroneous word loads, integer viewport fields or signed dimensions.
- Center the rectangle by subtracting half-width/half-height. Preserve inclusive left/top overlap and strict right/bottom comparisons, without normalizing negative extents or adding a new divisor gate.
- Publish scale X/Y, left/top, divisor, width/height to **D_800D2C70..D_800D2C88** even when the nonempty rectangle is invisible. Keep the original store order and full-word visibility semantics.

The source writer `conker/src/init_39C0.c` initializes the two live scales
from screen dimensions. Freeze that input too; these are not ROM constants.
Native checks verify the packet's **20-byte** layout, descriptor pointer
at +0x10 and view bounds at their original offsets. Naming and comments
describe the recovered fields; no cross-project symbol renaming is needed.

## Compiler And Closed Guards

The first complete semantic body emits 129 words / frame 0x18 with **46**
differences. Cast staging, halfword locals, declaration order and alternate
view access do not recover the full register allocation; several alternatives
also change length or frame and are rejected. Capturing both live global
scales before extent arithmetic reduces the result to **seven words**:

| Offset | Raw Linked Word | Retail Word |
| --- | --- | --- |
| +0x3C | 44834000 | 44833000 |
| +0x44 | 468021A0 | 46802020 |
| +0x48 | C42080A0 | C42880A0 |
| +0x50 | C42280A4 | C42A80A4 |
| +0x58 | 468042A0 | 468030A0 |
| +0x5C | 46003002 | 46080002 |
| +0x68 | 46025082 | 460A1082 |

These rename temporary FPR roles only. An exact symbolic DAG over
**+0x38..+0x6C** preserves operation/operand order, memory-read order, GPRs
and all non-scratch live outputs, including final scales F0/F2. A conservative
downstream CFG walk, **108 abstract states**, proves old F6/F8/F10 values
are overwritten before use on every path, including unsigned-conversion
fallback branches. Independent swapped-operand and old-scratch-read controls
fire these checks without relying on the raw fingerprint.

Two guard sites retain their actual **R_MIPS_LO16** scale bindings; the
manifest uses zero-immediate expected/replacement words with both relocation
columns populated. Preserve the complete old guard manifest as a byte prefix.
No branch, mathematical operation, saved register, stack frame, call, compiler
profile, shared helper or literal pool changes. All **18** other compact
owner bodies and relative bindings remain fixed. This is a **guard-backed
linked match**, not a raw direct compiler match.

```text
raw body eef5e7c981574013d8192371d63534a1a3ea879664207c564e7b98b69c98f182
```

## Fresh Qualification

Nine focused pre-install tests pass in **52.738s**. All **12 final tests
pass in 117.051s**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_packet_visibility tools.tests.test_game_packet_visibility_installed -v
```

- **1,296 complete guest cases**, both stack phases, compare original and raw C public memory. Include signed extent limits, unsigned dimension limits, zero dimensions, modes 0/1/0x100/negative, both frames, live scale values, negative divisors and all four overlap equalities. **123/129** words execute; six unsigned-conversion fallback words cannot be reached from these unsigned-halfword loads and are not advertised as covered.
- **32 guest alias pairs** cover output overlap with packet extents, descriptor dimensions, scale/output globals, view bounds and frame index. Null-descriptor tests confirm both zero-extent lazy exits. Void return registers and raw private scratch state are not equated to portable C outputs.
- **Native32 O2/O0**, separate translation units, real SDK types and selected-C UBSan each pass **1,296 cases** against independently generated float32 results. Use finite inputs and nonzero divisors; no native private-stack/alias or floating-environment claim.
- All **nine compiled guest and nine native controls** reject observably: signed dimension, unsigned extent, byte clear/mode, wrong view stride, either X-bound equality, missing width output and wrong reciprocal. Unsupported instructions or compile failures do not count as rejection.
- **Ten nonfinite/divide-zero guest cases** and **90 fired fault-prefix pairs** retain their explicit bounded-oracle scope. Fault pairs execute the actual independently padded normalized object against original words, not a second copy of a constant truth list. No complete hardware FCSR flags, traps, NaN-payload or raw C fault-state claim.
- Three independently assembled original rebase sets change entry and all **eleven external symbols**, including relocation low-half carries; **48 paired runs** preserve full normalized guest state. All **129 raw-word / 26 binding / seven guard** corruptions, extra-pool, DAG/liveness and metadata controls reject.
- **48 connected sequences** execute the real projector, previous 102-word depth routine and new visibility provider together. Matrix transformation remains bounded/opaque; this is not host-renderer or natural gameplay acceptance. The lower draw routine is still a placeholder.
- Check all **98 frozen/live inputs**, physical caller/callee/code/symbol/string controls and both strict successor-fixture stages. Every other ELF byte and **95** unaffected input keys remain fixed. Protected data is exact across **189,088 bytes / 720 owners**.

Both tools copies pass Windows syntax and all eleven shared WSL padder
tests; `make tools-check` passes. Prior unchanged neighbor-suite receipts
remain prior evidence, not fresh reruns. Routine Claude calls: zero.

## Image And Progress

Capture the old owner object and link script before production edits; the
baseline full link exactly reproduces the predecessor. Preserve the rejected
slot/extent-only prediction, SHA **dbdd63f0ade4c09b9b7f790f4e52d762f48564b84ad37706dd4a8c477c63db99**.
Account explicitly for seven symbol/string swaps and **157** serialization
bytes, with canonical definitions unchanged:

```text
D_800D2C80 <-> func_151A8584
D_800D2C7C <-> .L1514EAE8_game_data
D_80099444 <-> D_800A3C94
D_800994A4 <-> D_800A3CF4
D_800D23A4 <-> D_800899A4
D_800D2C74 <-> D_8009DD3C
D_800D2C70 <-> D_8008AC70
```

The normal guard-dependent guest rebuild exits zero with pre-existing
warnings. Its entire ELF equals the first pre-install prediction:
**551 changed bytes = 394 code/extent + 157 metadata**, extent **28 -> 516**,
no metadata or other exclusions. No cache-dependency bypass is used.

```text
before ELF 0896a6bb14a5780fe6c88d04cd7ece72fa460336afa8d4dbd3f739af0d079f66
after ELF  a7e8634c178f315ca4b42dabb3c4d348b84101cfa7d338e7c6de44ac6e4bdc51
after C    6e9a02f95eabb630214749833ad581a47a7a823ba0259362abd56fe6abf866f8
guards     197a60801a08f0db3ed2afa2461b3d692bd215cf21f78870609589fb06df9c41
```

Fresh official totals: **Game 2,922/4,828 (60.52%)**, **total 3,595/5,501
(65.35%)**, different **1,906**, drift **0**. Init 492/492 and Debugger
181/181 remain exact. Conversions remain 5,501/6,044 (91.02%), converted
bytes 86.04%. Root README changes only its two aggregate matching rows.

Tools **3a933e0** banks the five experiment/oracle/checkpoint/test files first.
Preserve older mirror HEAD **ddbdd16** and all **801** original dirty-file
hashes, adding only five absent files for **806** dirty paths; do not
commit/reset that mirror. Bank consumer C, seven guard rows, tools pin and
docs separately, then let the incremental graph hook finish without forcing
a full scan or dropping retained excluded nodes. No push or host-port/frozen
Release build, modification or launch occurs.

## Next Audit

**func_15095D34** is the next unfinished renderer in this owner: VA
**0x15095D34..0x1509629C**, ROM **0xC31E4..0xC374C**, **346 words /
1,384 bytes**, leaf frame **0x88**, no JALs. It reads all seven recovered
draw globals. Audit its five-input cursor/packet contract, signed conversion
and flag-driven clipping/texture commands, descriptor fields and animated
packet byte +0xC before replacing its zero stub. Use the real SDK graphics
macros and preserve the existing callers' returned-cursor behavior.
Keep original callers, inherited-stack func_1516D738/func_1516FE1C deferrals,
and the wider Game/additional-source/raw-matching queue open.
