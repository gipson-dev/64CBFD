# Display sprite update guarded match - 2026-11-26

`func_151797B0` replaces its zero-return placeholder in
`conker/src/game/generated_1A6360.c`. All **194 words / 776 bytes match retail
after nine expected-word guards**: 185 words emit directly from semantic C,
six normalize equivalent byte-argument preparation registers and three swap
commutative integer ADDU operands. Every FP word, operand order, instruction
position, memory access, call, branch and all 18 binding positions stay fixed.
The natural frame is **56 bytes**. VA `0x151797B0..0x15179AB8`, ROM
`0x1A6C60..0x1A6F68`; no tail, insertion, omission, frame patch, new binding,
compiler-profile change or Makefile change. Both complete owner padders agree;
all eight neighbors, pools and five exported retail labels are retained.

Production: **4,703 / 5,528 (85.08%) total**, **4,030 / 4,855 (83.01%) Game**,
Init 492/492, Debugger 181/181, zero drift, 825 still different. One matching
credit; conversion rows and denominator unchanged. No caller/helper credit.
The active **90% goal requires 4,976 matches: 273 more**.

The entry is `void func_151797B0(SpriteFrameState *record)`. Its partial
184-byte view is copied from the existing typed sprite-frame owner, whose
callback table is `void (*)(SpriteFrameState *)`. Repeated byte views preserve
the recovered access layout without inventing a larger complete record type.
The camera uses canonical `struct108` offsets. Display/sprite/heading/opacity
names describe measured roles; the original effect name and visual identity
are unknown. No shared descriptor rename is folded into this change.

The routine derives an opacity byte from the planar X/Z camera distance:
`max(0, trunc(80 - 80 * sqrt(dz*dz + dx*dx) / 1000))`. Z is converted before
X, the Z subtraction precedes the X subtraction, and Z is squared before X.
The old halfword heading is captured before the RNG callback. After that call,
the routine reads the live wind byte and damping coefficient (retail bits
`0x3F638E4C`, approximately 0.888890028), adds the masked unsigned random
increment, multiplies and truncates, then clamps only the upper limit to 12800.
The halfword store retains retail narrowing; no lower clamp is added.

The speed captures the float conversion of the signed interpretation of the
low 32 bits of `motionSpeed * ticks`. Each table-wave argument is the current
heading's high byte. The real helpers take **u8**, not s32. The first wave
updates signed X and the second updates signed Y, with speed-times-wave before
coordinate conversion in the emitted FP stream. All three signed origins are
captured before any wrap store. A coordinate outside center +/-500 shifts by
1000 and sets the wrapped flag. With flags bit 2 and wrapping, the routine
decrements the count, clears the indexed slot and releases the record. With
flags bit 1, wrapping clears that bit; otherwise it hides the record by
clearing opacity. Callback-visible fields are reloaded at the retail points.

The private source initially had 194 words/frame 56 with 99 differences.
Capturing origins before stores repairs alias-visible ordering. Meaningful
distance/speed lifetimes restore the SP+0x18 speed home. A three-difference
screen used incorrect wide wave prototypes and was rejected. Correct u8
prototypes plus a signed heading-byte intermediate reduce the result to nine
derived words. Center-relative wrap expressions retain the original integer
operations. No dummy local, padding object, physical-register variable,
floating arithmetic rewrite or broad instruction replacement is used.

Guard derivation:

- Offsets `0x120,0x128,0x130` and `0x144,0x14C,0x150` cover two LHU/SRA8/ANDI255
  argument preparations. The derivation decodes and executes each raw/retail
  triple for all 65,536 possible phase halfwords, checking identical
  zero-extended byte arguments and corresponding temporary values. The first
  ANDI is in the unchanged JAL delay slot. Argument/temp register allocation
  differs, so full raw private GPR identity is explicitly not claimed.
- Offsets `0x1E4,0x22C,0x274` swap only RS/RT on integer ADDU. Every other
  register field, opcode, immediate, relocation and instruction remains fixed.
  No guarded position has a relocation; no FP word is rewritten. The old
  complete CSV remains an exact prefix with nine derived rows appended.

Validation:

- Both complete original-ASM owner padders emit identical whole objects. The
  actual three-command Make recipe agrees under normal O2/g3/mips2/o32,
  with zero target diagnostics. The full build retains existing duplicate
  recipe warnings for generated_12D630, generated_F44D0 and generated_F5800.
- Guest: 960 cases across five streams exercise all 194 target words. Four
  literal retail/normalized/padded streams have equal full private state and
  159 fault-prefix quadruples. Raw C matches memory, access order, calls,
  FP/FCSR, HI/LO, PC/delay and all GPRs except the six declared volatile
  argument/temp roles. The same restricted relation holds at 159 faults;
  no full raw fault GPR identity claim. An independent reference compares
  complete public memory, ordered FP operations and FCSR.
- Guest coverage includes every wrap axis/boundary, all flag combinations,
  signed-halfword extremes, all four rounding modes, captured old headings,
  mutable wind/coefficient/ticks/coordinates/origins, aliased origin and
  coefficient memory, and incoming parameter-home redirects. Home/alias
  experiments qualify guest instructions only. Finite DIV and SQRT use exact
  rational bracketing for the modeled rounding modes. Bounded invalid integer
  conversions are software results, not hardware trap acceptance.
- Original 12-word/36-word wave helpers are connected, including nested calls
  and all table quadrants. All 260 bytes of quarter-wave data at `0x8009A220`
  are pinned to ROM and frozen ELF (SHA256
  `63d5e433f26fc064a7de67354337d256cd4b91ffcfa8cff53bcf92e1181adf46`).
  RNG/release slots are pinned but remain opaque contracts. No original
  allocator, release backend, gameplay or hardware acceptance claim.
- ROM/source context identifies callback table `0x8008C9C8`, 132 bytes,
  index 1 at ROM `0x23148C` / VA `0x8008C9CC`. The actual caller is the
  existing typed wrapper `func_15168870`, not a direct registry callback.
  Its complete original 111 words/frame 24 and table are pinned; its frozen
  ELF slot is already exact and receives no new credit. On zero frame-speed
  paths, 648 cases per original/normalized stream execute 27 parent words
  and 216 connected children. The independent whole-wrapper reference on
  those paths covers signed -1 callback disable, a null table cell, live
  phase reload and release cleanup. Three ignored-result poisons preserve
  effects through parent return. Nonzero frame-speed animation branches are
  not executed or claimed as covered.
- Native: actual selected C in three translation units, 4,096 cases at each
  O0/O2/O3, strict aliasing, UBSan traps and LTO type checks. Every byte-view
  access has a correctly typed native record member at the asserted offset.
  Complete initialized 184-byte records, camera/slot arenas, canaries,
  globals, callbacks and MXCSR agree across all four rounding modes. High-bit
  low-word products use small finite waves to keep conversions defined.
  Fifteen deliberate semantic negatives finish with comparison exit 42;
  no compile failure, signal or trap counts as a control. Native providers
  are noipa counterparts, not original guest helper execution. Native tests
  do not claim the guest-only home/alias experiments as portable C.
- Both padders reject 18 guarded-word corruptions and expose 370 unguarded
  word and 36 binding corruptions. Both reject oversize objects. Twenty GNU
  links / 100 guest rebases check address carry seams and jump regions.
  Rebase cases use opaque providers, without relocating the connected retail
  table helpers. No guard masks a changed binding.
- Independent frozen old-C plus original-ASM prediction equals the complete
  private and production ELF: **657 changed bytes, zero exclusions**. All
  189,088 protected data bytes across 720 owners stay fixed. ELF SHA256:
  `ef0f95c6f2f120a1680cfe81119406f30ccdccbdb14750c8ad8e49fd917ed509`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 167.395 s | 5 fresh / 0 reused |
| preinstall-sibling | 120.531 s | 5 fresh / 0 reused |
| installed-primary | 106.328 s | 5 fresh / 0 reused |
| installed-sibling | 126.481 s | 5 fresh / 0 reused |

All 20 target tests are fresh, with identical primary/isolated-sibling task,
import, data and artifact fingerprints. Shared tools-check passes; unchanged
broad suites are reused explicitly, not reported fresh. Frozen inputs:
4060; copies: 3000. The separately dirty
real tools sibling is preserved. Tools commit:
`52e2a9e8e6162062193cd5f7b8bc2de6577afec2`. Baseline consumer:
`9bb3a918b06ef6df6f0a1b7f7fce074a4a06f18e`. Receipts:
`conker/build/game-display-sprite-update-151797b0-private`.

Zero Claude calls or subagents: measured source screens and bounded derivation
settle this routine. The historical generated host target is still a stub;
the active host implementation is unqualified. No host source transfer,
build, launch, Release change or push. Scoped Graphify refresh audits all
nine owner definitions, preserves old IDs/qualification metadata and waits
for actual hook producers to terminate; no full-corpus extraction claim.
README receives aggregate rows/date only. Continue from sealed N69 toward 90%.
