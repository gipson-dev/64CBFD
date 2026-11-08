# Actor Snapshot and Resource Refresh Match - 2026-11-08

`func_15063254` now matches all **76 body words / 304 bytes**, its original
**0x58-byte frame**, and its **three trailing padding words**. The complete
retail slot is **79 words / 316 bytes**. Its semantic C replaces the old
zero-return placeholder and corrects the generated declaration to:

```c
void func_15063254(struct127 *actor, u32 field4, u32 field3, f32 value);
```

This is a **guard-normalized C match**, not a direct compiler match.
The inherited O2/g3 MIPS2/O32 profile emits 78 words with frame 0x50.
**59 checked rows**, including **two omissions**, recover the original
register lifetimes, snapshot cells, frame and memory schedule. No Makefile
or shared-header changes are needed.

Production recount: Total **4,258 / 5,513 (77.24%)**, Game **3,585 / 4,840
(74.07%)**, Init **492 / 492**, Debugger **181 / 181**, zero address drift.
There are **1,255** different converted functions and **153** additional
exact functions needed to reach 4,411 / 5,513 and the active 80% goal.
Conversion rows and denominators remain unchanged.

## Semantic recovery and interface

Owner: `conker/src/game_83300.c`. Body VA 0x15063254..0x15063384;
ROM 0x90704..0x90834. The slot ends at VA 0x15063390 / ROM 0x90840.
The source census found only the generated declaration and placeholder;
there were no existing C call sites requiring a dependent-owner change.

Capture the actor's identifier byte and auxiliary pointer before modifying
the auxiliary record. Store the low bytes of the two full-word arguments
at auxiliary+4 and +3, copy the fourth argument's exact FP payload to +0x20
and +0x24, and clear +2. Capture the camera/owner pointer, six actor FP
words and facing halfword. Call `func_15060F28(actor, 0)`, then submit the
captured auxiliary, captured identifier, two zeros and a one-based actor
slot to `func_15082A44`.

The slot calculation uses the wrapped 32-bit actor-minus-array-base
difference, interpreted signed, divided by the 812-byte actor stride with
truncation toward zero. Sparse guest fixtures cover unusual offsets;
native C fixtures use actual valid elements of the SDK actor array.

Restore the captured coordinates, motion/state words, owner pointer and
both facing halfwords after both helpers. Previous-coordinate outputs
receive restored X/Y/Z. The +0x1CC and old-Z stores deliberately read live
actor Y/Z after their earlier restores. Finally, the saved camera's
`unk3D4` receives the fresh actor+0x31C link. The local cast reconciles
existing SDK pointer views without changing a shared structure definition.

## Compiler and normalization boundary

An actual Make plan verified the default O2/g3 profile before screening.
Alternative declaration, source-shape and optimization screens did not
produce the original full body. The selected source emits the same raw
words and four bindings both in isolation and in the complete owner.

Normalization removes only a redundant argument copy and unused compiler
argument-home spill. It derives each remaining word from the raw semantic
stream: a checked bijection preserves the operations while restoring the
retail memory schedule, FP/GPR lifetime mapping, private-cell offsets and
0x58 frame. It does not read/copy replacement words from the ROM.
All **78 raw words** and **four bindings** are fingerprinted; altered-word
and altered-binding controls reject unknown input. **72** byte-corruption
controls verify the exact complete-owner register-mask union.

All **88** raw and padded neighbors and owner pools remain unchanged.
The actual **five-command** Make recipe performs asm preprocessing, IDO
compilation, asm postprocessing, `pad_c_object` padding and assembly. Its
89-function object equals the independently qualified padded object.
The owner has **eight inherited C warnings and zero added warnings**;
the isolated target has zero diagnostics. Existing warnings are preserved.

## Execution and full-image evidence

Six focused checks pass before and after installation in both tools copies,
with four sequential runs and exact source/dependency fingerprints:

- **583 guest cases**, all **76 words** reached, **16 FP payload patterns**,
  seven alias layouts and hostile caller-saved FP/GPR clobbers. Original
  and normalized programs have identical literal states and access traces.
  The raw C stream also agrees on public effects in **391 disjoint cases**.
- **399 instruction-fault cuts** compare exact original/normalized prefixes.
  Synthetic incoming/private-home and structure aliases are guest-only;
  raw C's different private frame is not claimed to share those aliases.
- **384 native32 cases per profile** at O0/O2/O3 with trapping UBSan,
  actual SDK layout assertions, bit-exact floating payload checks, full
  actor-array/auxiliary/camera canaries, and **15 effective controls**.
  The byte-swap control uses distinct low-byte arguments.
- Three independent GNU links and **18 rebased executions** cover helper
  bindings and both halves of the actor-array address, including signed
  low-half carries. Five image-corruption controls cover headers, body,
  symbol extent, protected data and the trailing padding.

The original aligned census finds one direct JAL at ROM **0xC6E10** /
VA **0x15099960**, in `func_15097A8C`, and no aligned entry/interior
pointer literals or interior direct entries. **384 connected cases** execute
its original five-word window: `MFC1 A3,F0`, JAL, delay NOP, branch and
result-one delay update. This establishes the four-word O32 packet and
ignored target return. Upstream integer-to-float multiplication and the
larger parent are not emulated. Both child bodies remain opaque modeled
providers; this evidence does not qualify their current placeholders or
claim gameplay/hardware acceptance.

The literal full-ELF predictor replaces only the target's 316-byte slot
and updates its symbol extent from 12 to 304 bytes. Actual and predicted
files are identical: **238 changed bytes, zero exclusions**. All **6,052**
disassembled entries keep their addresses. Every other function body and
extent is unchanged. Protected data stays exact across **720 owners /
189,088 bytes**. The three slot padding words remain zero.

Production Make compiles only this owner under its inherited profile,
links the predicted ELF, regenerates an identical progress CSV, and passes
a fresh recount. `make all` retains the existing whole-ROM checksum
failure (exit 2); the full ROM is not yet byte-exact. The existing duplicate
recipe warning for generated_12D630 remains unchanged.

Both fresh shared tools smoke checks pass. Three prior shared regression
checks per copy are explicitly reused with identical helper/test hashes.
The sibling's **2,434 pre-existing dirty paths** are fingerprinted and
preserved, with a private three-file validation overlay.

ELF SHA-256: `5bef769822f533a2b3abd6aff915b80ae0f134078f3414d6035a1c0edb24a0f4`.
Binary SHA-256: `78d30120a6734f458ac14e46488c92225333ce9dbd738640eee877feb430bb21`.
Owner SHA-256: `59550a10be55de9c1a648a617a687f6e2bc91fa2b66bc384edbbd72e017f06f9`.
Guard CSV SHA-256: `7b76c76b62b7c36f9a538ce31c3f5d48712e111f2c9f2367e70d8548166168d4`.

## Resume boundary

Next candidate: **`func_1506B3B8`** in `game_981E0.c`, still an uncredited
zero-return placeholder, with an old commented-out attempt below it.
Graphify surfaced its prior private recovery in [Note 1949](1949-relative-direction-private-semantics-and-codegen-boundary-20261101.md)
and [Note 1950](1950-relative-direction-cfe-stack-home-recovery-20261101.md).
Resume those retained artifacts instead of repeating the source screens.
Their selected 77-word/frame0x20 candidate recovered the choice byte at
SP+0x19 and retained **34 different words**, principally table-address
materialization and register/scheduling consequences. That is historical
private evidence; requalify it against this committed production baseline.
Its complete body is **77 words / 308 bytes**, VA 0x1506B3B8..0x1506B4EC /
ROM 0x98868..0x9899C, frame 0x20. Reconcile its generated declaration,
audit original callers and actual owner profile before compiling.

Recover the two FP difference arguments and third zero word sent to
`func_1505A630`. Reload the current actor after that helper; calculate the
signed 16-bit angular difference using facing and the shifted byte, reduce
the magnitude to an eight-bit lookup category, preserve ordered strict
threshold tests, then clear +0x138 and write +0x244 and +0x21C through live
actor-pointer reloads. The original uses byte table reads at D_80099A3C /
D_80099A3E despite older halfword declarations. Qualify byte views and all
dependent owners before changing any shared declaration. Do not copy the
old commented call signature or halfword-indexed table access.

The historical census also found the original eight-word wrapper and an
action pointer at D_8008630C[31], installed by `func_1505E0C4`. Its downstream
indirect invocation still needs qualification. Existing scratch remains
`conker/build/game-relative-direction-1506B3B8-match/`; the new resume audit
is confined to `resume-2189/`, preserving all older candidate artifacts.

Current receipts: `conker/build/game-actor-snapshot-15063254-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
includes changed-path and old-node-retention evidence; it retains existing
unscanned nodes and is not a new full-corpus extraction. The host Release
checkpoint remains frozen. The 80% goal remains active.
