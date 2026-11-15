# Private radial effect recovery and open frame boundary

Date: 2026-11-15. Continue the 85% total exact-C goal from
[Note 2465](2465-game-randomized-effect-dispatcher-direct-match-20261115.md).
The target remains **`func_150C29F0`**, VA **0x150C29F0..0x150C2C00**, ROM
**0xEFEA0..0xF00B0**, **132 retail words**, original **0x88 frame**.

Its complete radial-effect behavior is recovered and qualified in a bounded
finite domain, but **the C is private, uninstalled and uncredited**. Production
`conker/src/game_EF410.c` still contains its original placeholder. All **842
frozen production inputs** remain byte-identical, including every production
object, ELF, header, conversion CSV and guard manifest. Root README is unchanged.

## Recovered behavior and packet ABI

The routine takes one owner pointer and returns void. Its ordered calls are
integer random, two byte-angle lookup calls, float random, integer random,
two float random calls, effect constructor and final integer random. The
initial random result is narrowed to a byte; the angle helper receives
`(angle - 64) & 255` followed by `angle`.

The radial magnitude is a float random result times owner float **0x30**.
The position is owner **0x28** plus that magnitude times the first direction,
owner **0x34** unchanged, and owner **0x2C** plus magnitude times the second
direction. Two further random factors `draw * 0.5f + 1.0f` scale the packet's
five size/delta values. The owner bytes at **0xC / 1** are read immediately
before `func_15149550(&packet, 10, 1, 0, mode, selector)`. Its return pointer
is ignored. A final unsigned random remainder updates owner halfword **0xE**
to **`random % 51U + 25`**.

The local `RadialEffectPacket150C29F0` has the original **72-byte** layout:

| Packet offsets | Recovered fields / values |
| --- | --- |
| 0x00, 0x04, 0x08 | Three computed position floats |
| 0x0C, 0x14 | `D_800A02AC`, `D_800A02B0` times the first scale |
| 0x10, 0x18, 0x1C | `D_800A02B4`, `D_800A02B8`, `D_800A02BC` times the second scale |
| 0x20, 0x22 | Signed halfword codes `0x6231`, `0x1A4D` |
| 0x24 | Halfword duration `random % 201U + 100` |
| 0x26..0x29 | First three bytes zero, following byte 255 |
| 0x2A | Halfword flags value 1 |
| 0x2C..0x2F | Bytes 255, 255, 0, 1 |
| 0x30 | Zero word |
| 0x34 | Byte value 15 |
| 0x35..0x37 | Uninitialized padding; no semantic-value credit |
| 0x38 | Zero float |
| 0x3C, 0x40, 0x44 | `D_800A02A8`, `D_800A02A0`, `D_800A02A4` |

Field labels for unresolved codes/flags remain local, neutral names. The
constructor's original body at `conker/asm/176A00.s` establishes its pointer
return and `u8 / u8 / s32 / u8 / s32` parameter widths after the packet
pointer. No shared declaration is changed.

## Private semantic evidence

Original and compiled MIPS execution pass **512 finite cases / two streams**.
The fixtures exercise every byte angle, high-bit random words, unsigned
modulus boundaries, two stack phases, negative/zero radial values and modeled
helper mutations of owner data and global coefficients. All **132 retail /
129 raw target words** are visited. The **27 original instructions** of
`func_151423D8` execute against its actual 65-float quarter-wave table at
`D_8009A220`, ROM **0x23ECE0**; every helper word is visited too. The random
generators and effect constructor remain modeled providers.

Checks cover the full external fixture memory, call order and arguments,
**69 initialized packet bytes**, owner timer, saved registers and restored SP.
Private stack regions and the packet pointer are normalized for this semantic
screen; that is **not** physical frame, access-prefix or byte-match evidence.
Three packet padding bytes are deliberately outside the defined C contract.
Four effective instruction controls reject wrong duration modulus, timer
modulus, constructor kind and owner byte.

SDK32 native O0/O2/O3 each compile and execute the actual private C across
**512 cases**, with undefined-behavior traps and **eight effective compiled C
controls**. The native harness checks all 69 initialized packet bytes, the
complete **128-byte owner backing**, eight global float words and the helper
side-effect marker. Endian normalization preserves field values while
checking all owner bytes outside the typed fields. The angle helper uses
the original table and its recovered integer/quadrant logic. Its packet and
owner ABI sizes/offsets have explicit static assertions.

The entry census finds no direct Game JAL and one aligned entry pointer at
ROM **0x22EF94**, **D_8008A4C0[5]**. The complete original **45-word**
`func_15149264` parent is connected for **32 cases / two streams**, with
`jalr` at **0x151492E8**. This expiry route visits **31 parent words**, skips
the unrelated update callback, submits the radial effect and observes the
new positive timer, preventing the following free call. Wrong table selection
and timer-store offset controls fail. The other lifecycle paths, literal stack
equivalence and full gameplay are not claimed.

## Open matching issues and source screens

The canonical private body is ordinary C with an unqualified owner pointer.
It emits **129 words / frame 0x98**, versus **132 / 0x88** retail, with
**126 positional word differences** after binding its 25 relocations. Its
owner lives in S0, saved at **SP+0x20**; RA is at **SP+0x24** and the packet
starts at **SP+0x50**. Retail instead reloads the owner argument home at
**SP+0x88**, saves only RA at **SP+0x1C**, and starts its packet at **SP+0x3C**.
All **17 compact-owner neighbors** and normalized pools remain unchanged.

Raw target SHA-256 before binding:
`b3d93be2073c71f70796fe8dd1b0d21babf4abfe1fd515fcd5a0a14e7e9629b0`.

Forty-eight private source/profile screens are retained, with hashes for
their **96 C/object artifacts**. They cover plain/volatile parameter views,
explicit helper-result locals, snapshots, typed owner views, packet arrays,
grouped direction/radius locals, grouped packet scales and O1/O2 profiles.
Examples that recover the original frame still do not match the function:

| Diagnostic shape | Words | Frame | Positional differences |
| --- | ---: | ---: | ---: |
| Canonical plain C | 129 | 0x98 | 126 |
| Volatile owner | 134 | 0x90 | 122 |
| Volatile typed owner, no named position | 133 | 0x88 | 105 |
| Volatile owner, grouped packet/scales | 135 | 0x88 | 121 |

Volatile shapes are diagnostics, not recovered retail qualifiers or accepted
production code. O1 is also only a diagnostic profile; it is not installed.
The exact historical bodies are retained independently from the evolving
recovery module so the recorded screens can be reproduced.

There is a separate ordered floating-point issue. Retail's radius multiply
is **`mul.s F2,F0,F4`** (`0x46040082`); the canonical raw form emits
**`mul.s F2,F4,F0`** (`0x46002082`). Finite commutativity does not qualify
NaN payload selection. A positive boundary probe supplies distinct quiet
NaNs to both operands. Under an explicitly modeled left-NaN selection rule,
retail packet X/Z are **`7FC00001`**, while raw X/Z are **`7FC30002`**.
This is evidence of an open operand-order boundary, not a claim about which
payload physical hardware chooses. Exceptional FP/FCSR matching is unproven.

No guards are added and no source is installed. Padding/rebases, literal
frame/access-prefix equality, independent actual Make, full-image prediction,
production audit and recount gates still precede adoption.

## Checks, preserved state and next action

Fresh complete private suites pass in **34.712 seconds** mounted and
**38.482 seconds** through the sibling overlay. Each run rebuilds and executes
all native profiles. `make tools-check` passes. Routine Claude calls: zero.
The five-file ignored overlay preserves sibling HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a` and all **2,434 Windows-Git dirty
paths**, status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Scoped Graphify AST extraction covers six Python/C files, retains all **61,535
old IDs**, and records **61,571 nodes / 115,508 links**, with zero lost nodes.
This is not a full-corpus extraction.

The production ELF remains
`a0e774febc6423647616daa564758748653bff201ebb1db7f9e44fd8d8097c79`.
Its prior fresh recount remains applicable because the entire ELF and
classification inputs are unchanged: total **4,501 / 5,514 (81.63%)**, Game
**3,828 / 4,841 (79.07%)**, zero drift, **186** more matches to 85%.
No fresh production build or recount is claimed for this private-only work.

Next, keep this target and inspect CFE/UOPT local reservations and owner
call-save lifetimes. Compare the canonical body with the frame-0x88 diagnostic
forms, using the bounded compiler-observation procedure in
[Note 1322](1322-game-actor-callback-dispatch-direct-match-and-frame-provenance-20261012.md).
Recover the original homes: position **SP+0x20**, radius **+0x24**, directions
**+0x28 / +0x2C**, byte angle **+0x33**, first scale **+0x38**, packet **+0x3C**,
RA **+0x1C**, owner home **+0x88**. Then resolve ordered arithmetic and
scheduling and complete all adoption gates. Do not credit a frame-only result.

Tools commit **`826bd1f351f1874c9dfa1c87d4ce1b20bec46f1d`** precedes the
consumer documentation/pin commit. Ignored evidence remains in
`conker/build/game-radial-effect-150c29f0-private/`. The host port and frozen
Release are untouched; no push is performed. The 85% goal remains active.
