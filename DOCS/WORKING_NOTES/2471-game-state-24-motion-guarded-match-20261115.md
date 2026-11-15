# Game state-24 actor motion callback: qualified byte match

Date: 2026-11-15. Completes the private recovery in
[Note 2470](2470-game-state-24-motion-private-recovery-and-schedule-boundary-20261115.md).

## Result

**`func_150C3574` now matches all 264 retail words / 1,056 bytes**, with its
original **0x38 frame**, saved-register lifetime, arithmetic, control flow,
helper-call order and delay slots. The full movement, heading, animation and
loop-sound callback replaces its zero-return placeholder in
`conker/src/game_EF410.c` as `void func_150C3574(u8 *actor)`.

**253 words emit unchanged from ordinary C**. Eleven checked guards move two
private floating-point locals to their retail frame locations. No instruction
is inserted or omitted; no FP operation, branch, register, relocation or
caller argument is changed by these guards. Original assembly is retained.

Fresh production recount: **4,504 / 5,514 total (81.68%)**, Game **3,831 /
4,841 (79.14%)**, Init **492 / 492**, Debugger **181 / 181**. Address drift
is zero; **1,010** still differ. **183** more qualified matches reach 85%
at the current denominator. Converted counts/bytes do not change.

## Source recovery and private-local proof

Baseline consumer: `2379535830b8b08e876d2785a9068518085f6556`.
Starting tools: `29fbb0b263ad1f235d39dff360c29f8496f44cb6`.
Retail VA **0x150C3574..0x150C3994**, ROM **0xF0A24..0xF0E44**.
Owner `game_EF410` still contains eighteen functions.

Recovering `currentHeading` as the unsigned halfword loaded by retail and
recovering the square-expression order reduces the previous 81 differing
positions to eleven. This reproduces the complete retail magnitude/heading
instruction schedule under the existing **O2/g3/mips2/o32** profile. Compiler
flags, Makefile and shared headers are unchanged.

The only remaining raw differences are these private stack accesses:

| Value | Raw C home | Retail home | Changed words |
| --- | --- | --- | --- |
| Animation scale | SP+0x30 | SP+0x28 | 5 |
| Saved speed across calls | SP+0x2C | SP+0x30 | 6 |

The proof uses the bijection **0x30 -> 0x28, 0x2C -> 0x30, 0x28 -> 0x2C**
over three four-byte private cells. Raw SP+0x28 and retail SP+0x2C are unused.
All eleven words remain the same `lwc1`/`swc1` opcode, FP register and SP base;
only their displacement changes. The cells lie inside the allocated frame,
outside saved S0/RA and outgoing argument homes, and their addresses do not
escape. All other 253 instruction words and all **40 bindings** are fixed.
The qualifier pins the complete raw body and relocation set before applying
the transformation. Raw target SHA-256:
`5c57ed69838918c71545ea64fd3f5df1d771b1a56ff7ee29a37f654cae2891f3`.

The callback uses retained external coefficients D_800A0320..D_800A0330.
It adds no compiler pool. The existing production checker still accepts
`func_150C2C00`'s complete raw body, 58 bindings and exact **80-byte** literal
pool. All seventeen non-target owner functions retain code/binding identity.

## Fresh qualification

- **1,536 finite cases across retail/raw/normalized streams** agree with the
  independent public-state/call reference, including all thirteen modeled
  helper targets, boundary values, type/phase/flag combinations and mutations.
  Providers clobber o32 caller-saved registers, FP registers and argument homes.
- **597 fired memory prefixes** compare complete guest memory, registers,
  FP state, calls, access traces, PC and delay-slot state under the local-cell
  bijection. The same routes also compare normal completion. A deliberately
  wrong private home is detected.
- **120 exceptional-float cases**, including signed zeros, subnormals,
  infinities and distinct quiet/signaling NaN payloads, agree across all three
  streams under explicit left/right NaN selection models. Invalid integer
  conversion uses the declared modeled 0x80000000 result. Hardware FCSR
  conformance and portable native exceptional-C behavior are not claimed.
- **Native32 O0/O2/O3** each pass all 1,536 finite vectors and reject six
  compiled controls, with undefined-behavior traps enabled. Complete 640-byte
  actor backing, globals and call arguments are checked. The native harness
  itself grants no adoption credit; the installed source/image gate does.
- **576 original fourteen-word caller-window cases across three streams**
  pass normal, blocked and null-entry dispatch. Slot 24 of D_80086014 selects
  the callback; JALR **0x1504AB2C** passes `S0 -> A0` and ignores the return.
  This does not qualify the complete surrounding parent.
- All **264 corrupted body words and 40 corrupted binding sets** are rejected
  by the full pins. Both owner padders reject all **eleven** corrupted CSV
  expected words (**22** failures), preserve all seventeen neighbors, and
  agree with retail in **twelve GNU links / four code/data carry layouts**.
- The native runner's optional source-module argument preserves its default
  behavior: a fresh default run reproduces the earlier private C source and
  all three executable hashes exactly. The old fixtures remain usable.

Complete fresh suites pass pre-install in **54.571 seconds**, through the
sibling overlay in **96.720 seconds**, and installed in **55.405 seconds**.
`make tools-check` passes. Earlier individual screens remain diagnostics;
these final suites use the selected source and eleven guards.

## Production build and whole-image audit

Actual Make executes all **six** owner compile/postprocess/check/pad/assemble
commands. An independent link and strict predictor account for the complete
ELF with **989 changed bytes / zero exclusions**: the restored target slot,
its symbol size, and six closed metadata serialization permutations. The
permutations are recorded explicitly in `image.json`; named definitions stay
fixed except this target's size. The real production build is byte-identical
to that qualified image.

All **6,051 function addresses** stay fixed. Exactly **one of 698 production
objects** changes: `game_EF410.c.o`; its differing sections are precisely
`.text`, `.rel.text`, `.symtab`, `.strtab`. Added object names are exactly the
target's newly referenced symbols. No pool, loaded data or unrelated function
is excluded from the audit. Protected data remains **189,088 bytes / 720
owners**, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Of **846 frozen production inputs**, four planned hashes change (source,
append-only guard CSV, owner object and ELF); the other **842** remain fixed.
All eighty headers, eighty-two include inputs, Makefile, conversion CSV and
layout inputs are unchanged. Eleven rows append to the complete old guard
bytes; no historical row is edited. Production ELF SHA-256:
`ce22b9c6c2dc6ced4c635534cdb55087384ff55ade312b77268cd5c655a38d76`.

The existing duplicate `generated_12D630` recipe and CRLF-to-LF notices remain.
No broad warning, compiler-profile or line-ending cleanup is included.

## Banking and next target

Tools commit **`2bbf027a7a003e9d5182faf1a45620c6bb16934c`** precedes the consumer
source/guards/docs/pin commit. Evidence, the frozen baseline and immutable
pre-install receipts remain in `conker/build/game-actor-motion-150c3574-match/`.
The root README receives only its two aggregate matching rows; detailed
function updates stay here and in concise DOCS index entries. No push.

The six-file ignored overlay preserves sibling HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, all **2,434 dirty paths** and
Windows-Git status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Scoped Graphify AST refresh covers six files, retains all **61,744 old IDs**,
and records **61,768 nodes / 115,782 links**, zero lost IDs. It is not a
full-corpus extraction. The host path still contains scratch directories only;
no host import/build is applicable, and frozen Release is untouched.

Next target: **`func_150C3994`**, **237 words / frame 0x50**, in the same owner.
Recover its complete state-19/20 callback and caller ABI, preserve both newly
matched callbacks and the existing pool guard, and pass the full adoption
gates before assigning another match. The 85% goal stays active.
