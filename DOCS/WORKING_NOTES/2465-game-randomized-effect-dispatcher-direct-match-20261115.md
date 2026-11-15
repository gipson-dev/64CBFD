# Game randomized effect dispatcher direct C match

Date: 2026-11-15. `func_150C2898` replaces its zero-return placeholder in
`conker/src/game_EF410.c`. The complete **86-word / 344-byte** routine spans
VA **0x150C2898..0x150C29F0**, ROM **0xEFD48..0xEFEA0**, with no alignment
tail. All words emit directly from semantic C under the existing O2/g3
profile, with the original **0x78-byte frame** and **RA save at SP+0x44**.
There are **zero guards**, no inserted words and no profile, Makefile or
header changes. All **17 owner neighbors** and normalized pools are preserved.

This continues the next-target handoff in
[Note 2464](2464-game-quaternion-matrix-direct-match-20261115.md). The live
owner is the root-level `conker/src/game_EF410.c`, rather than a source under
`conker/src/game/`.

## Behavior and source recovery

The routine takes six `f32` values followed by an owner byte pointer and
returns void. The first three floats form the position. A float random draw
produces `(draw * 112.0f + 247.0f) * D_800A0288`; multiplying this by the
negated direction forms the velocity vector. The remaining helper sequence
is one float draw, two integer draws and one float draw. The complete order is
**float, float, integer, integer, float, effect constructor**.

The final sixteen-argument `func_151D9014` call carries position, velocity,
kind **6**, `first * D_800A028C + D_800A0290`, `(firstValue & 15U) + 25`,
`secondValue % 101U + 155`, `second * 119.0f + 129.0f`, the fixed flag/scale
arguments, and owner bytes **0xC / 1**. Its local prototype uses the recovered
SDK widths; integer random results are retained as `u32`. High-bit results
therefore use unsigned remainder, as in the original `divu` instruction.
The obsolete local placeholder declaration is removed.

The initial complete reconstruction already had the right 86 words, frame,
instructions and relocation targets. Four real word differences were stack
offsets: the retained random results occupied different local slots. Declaring
`speed, second`, then `secondValue, firstValue`, then `first` recovers the
original retained slots **SP+0x4C / 0x50 / 0x54**. No patching is needed.
Position remains at **SP+0x6C** and velocity at **SP+0x60**.

Raw body SHA-256, before linking its twelve ordinary relocation entries:
`cfd5c5854ac0d77932a5acf5217214bbaab71674a56baf1887c10a45c93a9e4d`.
Binding those entries to the retail addresses reproduces all 86 original
instruction words exactly.

## Guest, native and indirect caller qualification

Original and directly compiled streams pass **416 finite guest cases**, with
all 86 words visited. Fixtures cover signed zero, varied positions/directions,
integer mask and remainder boundaries, high-bit random words, byte identities,
both valid stack phases, and modeled helper mutations of the owner bytes and
three global float values. Complete public memory, the position/velocity and
all sixteen submitted arguments are checked. Helpers clobber volatile GPRs,
FPRs, HI/LO and their argument homes. Callee-saved registers and SP are retained.

Another **80 exceptional modeled cases** cover subnormals, largest finite
values, infinities and NaNs under explicit left/right NaN selection rules.
These remain bounded single-word floating models: hardware NaN selection,
FCSR flags/traps, full 64-bit floating state, arbitrary invalid owner pointers
and complete provider behavior are not claimed. **76 fired access-cut
prefixes** compare the complete modeled registers, HI/LO, memory, trace,
calls, packet observation and current instruction/delay context. Four
instruction controls reject wrong kind, mask, modulus and owner-byte offset.

SDK32 native builds execute the actual recovered C at **O0/O2/O3**, each with
**416 finite cases**, undefined-behavior traps and **seven effective compiled
C controls**. The checks include the complete position, velocity and submitted
arguments, all **128 owner-storage bytes**, three mutable global words and
the helper side-effect marker. The controls change direction sign, speed
bias, mask, modulus, scale, kind or owner byte. Exceptional floating inputs
are excluded from this portable native contract. Random generators and the
effect constructor remain modeled providers.

The aligned Game-code JAL census finds **no direct calls**. The sole aligned
literal entry pointer is ROM **0x22E5D4**, **D_80089AFC[6]**. The original
`func_151349D0` callback window at **0x15134B78..0x15134BF4** loads that table
entry, constructs its mixed floating/stack arguments and calls through
`jalr $t9` at **0x15134BEC**. All **31 original words** execute with both
streams across **four cases** covering stack phase and helper mutation.
The window checks all six floats and the owner pointer at entry; public
memory and saved registers agree after return. Wrong table selection and
owner-argument storage controls fail. The following retail continuation does
not consume V0. The complete parent, its surrounding loop and gameplay are
outside this bounded caller qualification.

## Padding and complete production image

Both complete-owner padders agree across all **18 functions**, including the
17 unchanged neighbors. Twelve independent GNU links at four code regions
(`0x15000000`, `0x25000000`, `0x65000000`, `0x95000000`) reproduce the target
from both padders and independently assembled original target instructions.
The target has no alignment tail. The generated-padder owner map uses original
assembly where available and retail ROM/layout rows for already recovered
neighbors whose individual assembly files are absent.

The independent actual-Make shadow executes the existing **five-command**
ASM-processor/compiler/postprocessor/padder/assembler recipe. Its predicted
ELF equals the installed production Make result byte for byte:

- **283 changed ELF bytes**, zero exclusions and no metadata permutations.
- All **6,051 function addresses** remain fixed. Only the target body and
  expected symbol extent change, from the 12-byte stub to 344 bytes.
- Only `game_EF410.c.o` changes among **698 production objects**.
- Its changed sections are exactly `.text`, `.rel.text`, `.symtab` and
  `.strtab`. The string table adds exactly the newly referenced
  `D_800A0288`, `D_800A028C`, `D_800A0290`, `func_150ADA20` and
  `func_151D9014` names, with no removed names.
- All **189,088 protected data bytes / 720 owners**, all 80 headers and all
  82 include inputs remain unchanged.
- Of **839 frozen production inputs**, only the declared source, owner object
  and ELF change; **836 non-adoption inputs** remain fixed. Guard manifest
  and conversion CSV are byte-identical.

Production ELF SHA-256:
`a0e774febc6423647616daa564758748653bff201ebb1db7f9e44fd8d8097c79`.
Fresh full focused-suite times are **36.832 seconds** pre-install,
**35.844 seconds** through the sibling overlay and **33.181 seconds** installed.
Native executables are rebuilt and executed in each suite. `make tools-check`
passes. The existing duplicate `generated_12D630` Make warning remains.

The six-file ignored sibling overlay preserves actual sibling HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a` and its **2,434 Windows-Git dirty
paths** exactly. Before/after status SHA-256 is
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Scoped Graphify extraction covers seven Python/C files, retains all **61,492
old IDs**, and records **61,529 nodes / 115,441 links**, with zero lost nodes.
This is not a full-corpus re-extraction. Routine Claude calls: zero.

## Actual recount and resume boundary

The fresh production ELF recount is **4,501 / 5,514 (81.63%)** total exact C,
Game **3,828 / 4,841 (79.07%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and **1,013 still different**. Converted counts and byte
percentages are unchanged. **186 more exact C functions** reach 85% at the
current denominator; the wider goal remains active.

Next target: adjacent **`func_150C29F0`**, a 132-word routine with a **0x88
frame**. Recover its random angle/trigonometric calls, effect payload and
submission, and final unsigned-remainder halfword update before any
matching credit. It remains a placeholder in production.

`64CBFDOGL` has no active host Git/CMake checkout at the recorded path. No
host adoption is claimed and the frozen Release remains untouched. Ignored
evidence and immutable pre-adoption receipts are retained in
`conker/build/game-randomized-dispatch-150c2898-private/`.

Tools commit **`ac9147f601482af2e2f93c1b85c7194fd436a9a2`** precedes the
consumer source, documentation, two aggregate README rows and tools pin.
No push is performed.
