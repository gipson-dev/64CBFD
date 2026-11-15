# Game state-19/20 effect-phase callback: qualified byte match

Date: 2026-11-15. Continues the 85% total exact-C goal after
[Note 2471](2471-game-state-24-motion-guarded-match-20261115.md).

## Result and source

**`func_150C3994` now matches all 237 retail words / 948 bytes**, with its
original **0x50 frame**, saved-register lifetime and helper-call schedule.
The complete callback replaces its zero-return placeholder in
`conker/src/game_EF410.c` as `void func_150C3994(u8 *actor)`.
**236 words emit unchanged from C**; one checked guard restores retail's
operand order for a multiplication by the fixed -20.0f constant.
No instruction is inserted or omitted. Original assembly is retained.

Fresh production recount: **4,505 / 5,514 total (81.70%)**, Game **3,832 /
4,841 (79.16%)**, Init **492 / 492**, Debugger **181 / 181**, zero address
drift and **1,009** still different. **182** additional qualified matches
reach 85% at the current denominator. Converted counts/bytes do not change.

Baseline consumer: `1027e050f3971470cf82262763f7c2523d7df061`.
Starting tools: `2bbf027a7a003e9d5182faf1a45620c6bb16934c`.
Retail VA **0x150C3994..0x150C3D48**, ROM **0xF0E44..0xF11F8**.
The same eighteen-function owner retains all seventeen neighbors.

The body handles the state-20 preliminary effect/buffer path, a gated sound
for downward movement, the phase-zero initialization effects and sound,
the wrapping byte counter and flag clear, heading-derived angle, motion
integration/damping, and the conditional exit-effect/sound/state sequence.
Unknown actor fields retain numeric offsets instead of speculative shared
names. Moving the 500.0f initialization before the two flag statements
reproduces the retail setup schedule, reducing eight initial differences to
the single constant-multiply word. The existing **O2/g3/mips2/o32** profile,
Makefile and shared headers are unchanged.

## Constructor ABI and guard proof

The two `func_151B9BF0` calls use its recovered **sixteen-argument** interface:
two words, eleven signed halfwords, a value word, a view byte and a context
word. The three coordinates explicitly truncate through `s32` before
narrowing to `s16`, preserving the original wide-conversion/low-half behavior
for finite coordinates outside the signed-halfword range. Register and stack
arguments agree with the original constructor's actual loads and stores.

Qualification connects all **48 original constructor instructions** from
retail and pins their known truth hash. Native qualification uses its matched
C implementation, independently checking the complete **44-byte record**.
Allocator success, failure and alternating outcomes are modeled; this does
not claim complete allocator or sound-system qualification.

The sole guard is word **77 / offset 0x134 / VA 0x150C3AC8**:
`0x46100482 -> 0x46008482`, `mul.s F18,F0,F16 -> mul.s F18,F16,F0`.
The dominating instructions set F16 to **-20.0f**. The operation is behind
the negative-velocity gate; there is no intervening helper or F16 definition.
Destination, operation, frame, control flow, memory and bindings stay fixed.
The explicit FP models also check the swap with representative special
values and 1,024 additional bit patterns under both NaN-selection rules.
The complete raw body and all **14 bindings** are pinned before normalization.
Raw target SHA-256:
`5a3da9a33d1df37c8c658b4e40a5d3f5bd4158aeab22703a83be4fe05449ac3f`.

## Fresh qualification

- **2,048 finite cases across retail/raw/normalized streams**, with the
  original constructor connected, exercise **all 237 target words**. Public
  actor/output memory and all helper arguments agree with the separate
  reference. Cases cover both states, signed coordinate narrowing, phase
  wrap, sound/exit boundaries, callback mutations and three allocation policies.
- **1,202 fired memory prefixes** compare complete memory, integer/FP state,
  calls, traces, PC and delay-slot state, including constructor memory stores
  and two-allocation paths. Normal completion is compared on the same routes.
- **168 exceptional-float cases** agree across the three streams under
  explicit left/right NaN-selection rules. Invalid integer conversion uses
  modeled 0x80000000; hardware FCSR conformance and portable native exceptional
  C behavior are not claimed.
- **Native32 O0/O2/O3** each pass all 2,048 finite vectors, checking **832 actor
  bytes**, **192 output bytes**, complete calls and the matched C constructor.
  Undefined-behavior traps are enabled. All **eight** compiled mutation
  controls fail, covering state, phase, counter limit, sound threshold,
  heading offset, damping, constructor parameter and flag clear.
- **1,536 original fourteen-word dispatch-window cases across three streams**
  exercise table slots **19 and 20** independently, including normal, blocked
  and null-entry paths. JALR **0x1504AB2C** passes `S0 -> A0` and ignores the
  return. A wrong caller-argument delay slot and a wrong multiply operation
  are detected. The complete surrounding parent remains uncredited.
- All **237 corrupted body words and fourteen corrupted bindings** are
  rejected (**251** controls). Both padders reject a corrupted CSV expected
  word, preserve all seventeen neighbors, and agree with retail through
  **twelve GNU links / four code/data carry layouts**.

Complete suites pass freshly pre-install in **56.239 seconds**, through the
sibling overlay in **56.899 seconds**, and installed in **59.423 seconds**.
`make tools-check` passes. The native fixture initially compared a leading
comment as part of a function body; the final check compares parsed bodies
and retains the exact matched constructor implementation.

## Production and preservation

Actual Make executes all **six** owner build commands. The strict independent
full-image prediction accounts for **741 changed bytes / zero exclusions**:
the restored target slot and size, plus one closed serialization swap of
`D_800A0334` / `D_8009FF34`. Named definitions otherwise remain fixed. The
actual production ELF is byte-identical to the qualified image, and all
**6,051 function addresses** stay fixed.

Only **one of 698 production objects** changes, `game_EF410.c.o`; its differing
sections are precisely `.text`, `.rel.text`, `.symtab`, `.strtab`. Added object
names are exactly the target's newly referenced symbols. All **189,088
protected bytes / 720 owners** remain unchanged, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Of **849 frozen production inputs**, only the four planned source/guard/
owner-object/ELF hashes change; the other **845** remain fixed. All eighty
headers, eighty-two include inputs, Makefile, conversion CSV and layouts are
unchanged. One guard row appends to the complete prior CSV bytes. No new
literal pool is emitted; the existing production checker still accepts
`func_150C2C00`'s raw body, 58 bindings and **80-byte** pool, and the newly
matched `func_150C3574` remains unchanged. Production ELF SHA-256:
`7e13d5f4594abd2edb1bafc1e76f45e1eccc7475b83663a64bcedff7bd4e5bc1`.

Tools commit **`1d259161907b4d09f462f787c0e9f2e5e92a1325`** precedes the consumer
source/guard/docs/pin commit. The eight-file ignored overlay preserves sibling
HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, all **2,434 dirty paths** and
Windows-Git status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Evidence and immutable pre-install receipts remain under
`conker/build/game-impact-phase-150c3994-match/`.

Scoped Graphify AST refresh covers eight files, retains all **61,775 old IDs**,
and records **61,822 nodes / 115,863 links**, zero lost IDs; it is not a
full-corpus extraction. Root README receives only its two aggregate matching
rows. Existing duplicate-recipe and line-ending notices remain; no broad
cleanup is included. The host path contains scratch directories only; no host
import/build is applicable, frozen Release is untouched, and nothing is pushed.

Next target: **`func_150C3D5C`**, called by this routine's exit path: **240 body
words plus one alignment word / 241-word slot / frame 0x100** in the same owner.
Recover its complete payload/helper ABI and qualify dependent callers,
neighbors and pool interactions before adoption. The 85% goal stays active.
