# Path-distance branch command recovered directly from C

Verified 2026-11-01. `func_150781F4` emits all **54 retail words directly from
C**, with its original **24-byte frame**, 13 bindings and **zero word guards**.
An explicit node-index local restores retail register allocation; integer
radius conversion removes the old eight-word excess. Its interface remains
`void(void)`, with the existing `PathNode8` view and notification declaration.

Production Make and an independent Windows actual-ELF recount report
**4,034/5,507 (73.25%)** total and **3,361/4,834 (69.53%)** Game, zero canonical
address drift and 1,473 different. Init remains492/492; Debugger181/181.
Converted inventory stays5,507/6,045, Game4,834/5,324. Threshold4,131 requires
**97 additional exact C functions**. The wider goal remains active.

## Source and recovered compiler shape

- Source/owner: `conker/src/game_A28B0.c`, `game_A28B0`.
- Original `conker/asm/nonmatchings/game_A28B0/func_150781F4.s` retained.
- VA `0x150781F4..0x150782CC`; ROM `0xA56A4..0xA577C`, 216 bytes.
- No shared headers, layouts, compiler profiles or guard CSV edits.

The command selects signed X/Z from
`D_800D2104[currentActor->unk13F][D_800D1891 + 1]`, subtracts the actor's
float positions, squares each single-precision delta, adds, then takes `sqrt.s`.
The unsigned radius byte is shifted left three **as an integer before** float
conversion. Mode zero branches strictly inside the radius; every nonzero mode
branches strictly outside. Equality never branches. A taken branch calls
`func_15075400` with the live first command byte, zero-extended to `s32`.

The old C emits62words/frame24. Integer radius conversion yields54words but17
GPR differences. Naming `nodeIndex = D_800D1891 + 1` restores all register roles
and produces the complete retail payload. Splitting the increment leaves12
differences; leaving the addition inside indexing leaves11. Named locals and
the semantic function comment preserve the direct match. The dead X-delta
temporary is reused for the radius after the square root; a separate radius
local introduces three FP-color differences, so the verified zero-guard form
retains that lifetime. No scheduling normalization, filler or inserted words.

Raw SHA-256:
`9c8c7a46715a56f276125f07c2ff18078e4afc78cf937803bafd815c8d7ba5f6`.

## Runtime, complete helper and both callers

- **12,292 guest cases / 49,168 executions**, three symbol rebases, four input
  aliases, both stack phases and all256 values of the command bytes. All54
  words execute. Original ASM, padded owner, actual Make and isolated C agree
  in complete modeled state and access traces. The corpus covers equality,
  either strict direction, signed coordinates and four nonfinite cases.
- **41 fault prefixes / 164 executions** agree across all four exact programs.
  This qualifies guest instruction order, not portable C fault semantics.
- Native O0/O2/O3 each pass **1,024 finite cases**, UBSan and complete actor/path
  canaries. `sqrtf` uses SSE `sqrtss`; intermediate operations remain float32.
  Eight controls are effective: unsigned X/Z, wrong node, wrong radius,
  inclusive inside/outside comparisons, mode-one-only and missing notification.
  Pointer aliases and nonfinite inputs are guest-only. Full FCSR/hardware and
  gameplay behavior are outside this qualification.
- **1,024 connected cases / 4,096 executions** run all38 words of original
  `func_15075400`, VA`0x15075400..0x15075498`, ROM`0xA28B0..0xA2948`, pinned
  against retail and the baseline ELF. No nested provider substitutes for it.
  Arguments below247 advance five-byte packets by the argument. Sentinel search
  handles normal records, nonmatching sentinels, a matching sentinel and the
  100-iteration limit. A match advances one byte then subtracts five, giving
  **net cursor minus four**; the independent reference preserves this behavior.
- Script table`D_80086730[161]` is the sole aligned root pointer at ROM`0x22B474`.
  **120 cases / 480 executions** run the original29-word dispatcher window,
  covering28 reachable words, opcodes161/247/255, four ignored-return poisons,
  payload copies and five-/one-byte advancement. The duplicate load at+0x20 is
  unreachable. The larger dispatcher is bounded, not fully emulated.
- Census also finds one direct JAL, ROM`0xA6DC0`, in`func_150798F8`.
  **64 cases / 256 executions** run its complete12-word wrapper, pinned to
  retail and ELF. It copies actor byte`unk21E` into`D_800D1891` in the call's
  delay slot. Distinct initial command bytes, both outcomes, stack phases,
  preserved registers and four return poisons verify that interface.
- **Eight cases / 16 executions** validate the retargeted two-word trampoline,
  preserving all registers, FP registers and memory at its new private boundary.

## Owner and exact overflow-removal closure

All **210 raw/padded neighbors** and normalized pools stay fixed. Existing
owner warnings remain **14->14** with the same kinds and source expressions.
The actual five-command Make recipe reproduces the qualified object.

The obsolete248-byte `__retail_overflow_func_150781F4` at`0x15F006F4` is removed.
Three private bodies move down248 bytes without changing any body bytes:

| Private body suffix | Before | After |
| --- | --- | --- |
| `150A7B80` | `0x15F007EC` | `0x15F006F4` |
| `150A7D00` | `0x15F00870` | `0x15F00778` |
| `15125490` | `0x15F0091C` | `0x15F00824` |

Only the live `func_150A7D00` trampoline retargets. Exhaustive executable-reference
checks and moved-body control-flow checks confirm local relative branches and
unchanged absolute call destinations. All **6,045 canonical addresses** stay
fixed and **6,052 other bodies** stay identical. Executable inventory falls
6,055->6,054 solely by deleting the obsolete private implementation. This is
not an all-function-addresses-unchanged claim.

Independent literal complete-ELF prediction accounts for the target slot,
trampoline, removed payload, private symbol moves, local-symbol deletion,
GNU shared-name string reconstruction, two absolute ROM symbols, program/section
headers and alignment. ROM cursor movement is256 bytes because the next region
is16-byte aligned. ELF length falls **284 bytes**, 3,256,900->3,256,616. Named
definition multisets are checked, including repeated absolute aliases.

The entire linker map also matches an independent prediction, including all25
changed lines. The private first-link comparison maps its ten shadow-object
path occurrences and one output filename to production paths; production then
passes the literal map check without path remapping. No image/map exclusions.
Corruption controls cover code, moved bodies, trampoline, symbols, strings,
unrelated image data and the map. All **189,088 protected Game bytes / 720 owners**
remain exact. Installed ELF SHA-256:
`cc5981e7788bf5d36abd8790fe86661ede5425c45086e450a283d22455b4c4f5`.

Production reviews17,628 predecessor sealed inputs: only source, owner object,
ELF and map change. Guard history and unrelated objects stay fixed. Six focused
tests per tools copy pass before/after installation, both shared checks pass,
and the Windows actual-ELF recount independently confirms the new total.

## Evidence and continuation

`conker/build/game-path-distance-branch-150781F4-match/` contains1,064 frozen
focused inputs and30 canonical artifacts, source screens, exact owner/Make/image/
map evidence, runtime/caller/helper checks and final bank receipts. BANKED_STATUS
supersedes historical private flags. Original assembly and older private
candidates remain preserved. Archived historical checkpoints need restoration
before their target tests. Tools are committed before the consumer; no push.

Next audit the56-word Game command`func_1507E1D0` in`game_A9D90`, using its
complete assembly and interface. The small translation routine`func_150A7D00`
needs separate SDK/handwritten-provenance review before entering the compiler-C
queue; its interleaved doubleword stores are not assumed compiler-generated.
Root README receives aggregate rows only; detailed recovery stays in these notes.
