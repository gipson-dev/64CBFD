# Packet Scissored Rectangle Semantic Recovery

Date: 2026-10-16. Consumer predecessor **bbaab6ee**, tools predecessor
**3a933e0**. Continue Note 1434's renderer audit. This is a **semantic
recovery, not a retail byte match**. Keep func_15095D34 as the next matching
target; do not count this checkpoint as closing the wider Game queue.

## Recovered Contract

**func_15095D34**, owner `conker/src/game/generated_C1D70.c`, original
`conker/asm/C1D70.s`, spans VA **0x15095D34..0x1509629C** / ROM
**0xC31E4..0xC374C**: **346 retail words / 1,384 bytes**, leaf frame **0x88**,
no JALs. Its prior typed zero-return stub occupied **28 bytes**, not 12.

Replace that stub with semantic C using the real SDK `gDPSetPrimColor` and
`gSPScisTextureRectangle` macros. Keep the address-based function symbol and
32-bit returned-cursor ABI; recover typed Gfx/packet input pointers and the
three signed offset arguments. Both existing caller casts leave their emitted
instructions unchanged. Name the packet's recovered bytes without changing
its 20-byte size or descriptor pointer at +0x10:

| Offset | Field | Actual Access |
| --- | --- | --- |
| +0xA | alpha | unsigned byte |
| +0xB | animationStep | unsigned byte |
| +0xC | animationFrame | unsigned byte, high direction bit |
| +0xD | flipFlags | unsigned byte, X/Y bits 1/2 |
| +0x10 | descriptor | pointer, dimensions unsigned halfwords +4/+6 |

- Capture the seven draw-global inputs from D_800D2C70..D_800D2C88 at their actual phases. Truncate the two scales to signed integer divisors. A nonzero fourth argument both shrinks/insets the rectangle and contributes to the initial T origin. Publish width then height; floor only the local width to 2, not the height or stored global width.
- Preserve word-sized shifted numerators, signed divisions and the emitted real MIPS BREAK 7/6 checks. No invented zero-divisor fallback or broad instruction guards are added.
- When tint is unlocked, emit FA000100 and the three live RGB bytes plus packet alpha. Preserve the first command-word store before those byte reads. Always emit three rectangle commands; return the cursor advanced by 24 or 32 bytes.
- Retain float32 fractional S/T arithmetic and unsigned word shifts. X flip replaces S with `(descriptorWidth + 255) << 5`. Y flip subtracts the raw fractional T, not the completed offset T. Both negate the integer texture step through an unsigned halfword.
- Reload the descriptor after command emission. The animation gate, speed and timestep are byte loads; D_800BE9A0 is not a word-valued clock. Looping subtracts the frame limit once, not full modulo. Ping-pong keeps the original byte wrapping and direction restoration, including the descriptor flag reload after the packet-byte store.

The actual SDK macro at `conker/include/2.0L/PR/gbi.h` explains the retail
clipping region. Its X correction checks a signed halfword, whereas its Y
correction checks the full signed word before using the low halfword in the
product. Preserve that asymmetry. Retail `lh sp+0xA` reads the initialized
low half of a word at sp+8; it is **not** an uninitialized C local. Do not
import the reference draft's uninitialized `unkspA` or erroneous word-width
descriptor loads. The reference source remains a frozen input, not authority
over the actual instructions or SDK.

## Compiler Boundary

The selected `phased-typed-pointers` body emits **345 words / 1,380 bytes**,
frame **0x88**, with **331 pointwise retail differences**, including the
one-word length difference. There are **28 relocations**, no literal/data
pools and no compiler diagnostics. All **18** other compact owner bodies
and relative relocation bindings remain unchanged.

The first complete form was 355 words / frame 0xB0 / 346 differences.
Bounded declaration, capture/reload, step-reuse, numerator and pointer forms
recover the smaller frame but not a byte match. Some reload forms have fewer
pointwise differences without qualifying the selected global snapshots;
do not choose by count alone. A late flip-byte load worsens the selected
result to 332 differences. A register hint has no effect.

**No new guards** are installed. The padder retains the complete emitted
345-word body and adds one zero alignment word inside the original slot.
That NOP is not represented as a recovered retail instruction or match credit.

```text
raw body     01940fff7f9e3bf97261e6972d885ce3d2eacfe47969e8ff326e10c4662ec106
padded slot  9dbf7b6afd6bfaa3c0e6d995c2d187446dbbed6b4540869a79ae661aba4a49da
```

## Qualification

```sh
python3 -m unittest tools.tests.test_game_packet_rectangle_recovery tools.tests.test_game_packet_rectangle_installed -v
```

All **14 final tests pass in 148.459s**, exit zero, after the normal guest
rebuild. Both tools copies pass Windows syntax and all eleven shared WSL
padder tests; `make tools-check` passes.

- **2,880 geometry cases**, both stack phases, compare original and raw C public memory/cursor: scale signs, fractional positions, large/narrowed coordinates, all flip combinations, inset/tint gates, width floor, untouched height and large unsigned descriptor dimensions. This geometry sweep executes **310/346 original words**; do not count raw-C visits as original instruction coverage.
- **672 original/raw-C animation pairs** exercise zero flags, single wrapping, both ping-pong directions, byte boundaries and speed/time limits, with an independent byte formula.
- **Native32 O2/O0**, separate translation units, real SDK macros and selected-C UBSan: 2,880 geometry cases and **1,048,576 animation cases per selected optimization level**. All eight compiled native and eight guest controls reject observably; compiler or unsupported-instruction failures are not counted as rejection.
- **80 guest alias pairs** qualify live descriptor/color reloads and cached-global phases. **16 arithmetic pairs** qualify real BREAK 6/7 classification and prior public writes; five nonfinite/zero-divisor guest cases retain their bounded conversion scope. These are not portable C alias/invalid-cast guarantees, exceptional DIV LO/HI values, complete private state, hardware FCSR or fault-prefix equivalence.
- Three independently assembled original rebase sets change entry and **12 externals**, with **48 paired public-memory/cursor runs**. All **345 raw-word / 28 binding** corruptions and extra pools reject. All **100 frozen-input** corruption controls fire.
- **32 connected sequences** execute the real 30-word caller func_15095A90, 129-word visibility provider and original/new renderer together. No opaque rendering hook substitutes for the new body. This is bounded guest-model evidence, not natural gameplay, GPU pixels or host-port acceptance.
- Full-image/input/caller/metadata corruptions and both strict predecessor/successor fixture stages are checked separately. Retain prior unchanged neighbor-suite receipts as prior evidence rather than claiming fresh broad reruns.

## Independent Image Prediction

Before production edits, capture the old owner object and link script and
require their full link to reproduce the predecessor ELF. Freeze **100**
inputs, including the two actual SDK headers. Predict the replacement from
the independently padded **C output**, not copied retail words.

Preserve the rejected slot/extent-only prediction:
**e2e7aeb39263ac4d5eddff1c6e4c0035205932a6ff1b8415aada541df96d443a**.
Two exact adjacent symbol/string swaps account for **18** further bytes:

```text
D_800D237C <-> D_8008997C
D_800D2DA8 <-> D_8008ADA8
```

Canonical symbol definitions remain identical. No metadata sections or other
bytes are excluded. The normal guest rebuild exits zero, with the pre-existing
duplicate generated_12D630 recipe warnings, and reproduces the complete first
prediction: **1,035 bytes = 1,017 code/extent + 18 metadata**, target extent
**28 -> 1,380**. Every other ELF byte and **98 unaffected input keys** remain
fixed. Prior guards are byte-identical. Protected data is exact across
**189,088 bytes / 720 owners**. No dependency/cache bypass is used.

```text
before ELF  a7e8634c178f315ca4b42dabb3c4d348b84101cfa7d338e7c6de44ac6e4bdc51
after ELF   05c247fb22b1ef93a931bf8dc4068a334c19ab6b4b1ea1fc64f6ea3befde655c
after C     d80e8a78be87de9517c88eef652832e843c37d0dd5091f0b43a0be25bf24b357
guards      197a60801a08f0db3ed2afa2461b3d692bd215cf21f78870609589fb06df9c41
```

## Advisory Review

One justified packet-only Claude analysis, no tools/MCP, safe mode and no
session persistence. Complete target assembly, selected C and relevant SDK
macro were supplied; packet SHA
**e0dc7e9f1bcf3afa1180b192099d6f854a1f2cf25759152c5802c4a249808b8a**.
The CLI returned success; a wrapper's CP1252 display error did not discard
the saved JSON or justify another call. The three homed arguments/frame
observation is confirmed. The width clamp was already in the suggested place.
The independently tested late flip load regresses matching. Descriptor
hoisting would ignore actual reload points, and manual macro expansion has
no demonstrated value. No suggestion is accepted as proof of semantics or
byte matching. Ignored packet/answer receipts remain in the target build dir.

## Next Matching Work

Keep **func_15095D34** open. Recover the missing instruction and remaining
FPR/GPR lifetimes and scheduling through the real macro before claiming
346-word/frame-0x88 identity. In particular, compare the retail divisor's
F18-to-F16 transfer with the current direct F16 capture; equal frame/home
counts are not complete register or private-state identity. Preserve all
semantic, alias, relocation, owner and image gates. Start that stage from a
new immutable semantic baseline rather than overwriting this first prediction.
Do not use 331 blanket word replacements to call the function matched.

Keep the original caller backlog, inherited-stack func_1516D738/func_1516FE1C
C deferrals and broader Game/additional-source/raw-matching queues open.
No push or host-port/frozen Release build, modification or launch is authorized
by this retail decomp checkpoint.

## Progress And Banking

Fresh official totals remain **Game 2,922/4,828 (60.52%)**, **total
3,595/5,501 (65.35%)**, different **1,906**, drift **0**. Init 492/492 and
Debugger 181/181 remain exact. Conversions stay 5,501/6,044 (91.02%),
converted bytes 86.04%; the predecessor already represented this stub in C.
Root README already has these same verified aggregate figures and date,
so it needs no edit or recovery narrative.

Tools **552f48e** banks the five experiment/oracle/checkpoint/test files
before the consumer source/pin/docs commit. The older standalone mirror
retains HEAD **ddbdd16** and all **806** original dirty-file hashes; add only
five absent files for **811** dirty paths, with byte identity to the committed
tools copies. Do not commit/reset that mirror. Let the consumer's incremental
graph hook finish; do not force a full scan or delete retained excluded nodes.
No push or host-port/frozen Release action occurs.
