# Payload effect factory direct C match — 2026-10-28

`func_150F0198` is recovered as a seven-argument `struct225 *` factory in
`conker/src/game/generated_11C2B0.c`. All 50 instructions (200 bytes) emit
directly from C using the existing IDO O2/g3/mips2/o32 profile. The 88-byte
frame and two call relocations match. No new guards or alignment words are
needed. The other 43 functions in the complete owner are preserved.

The actual adopted ELF recount is **3,878/5,506 (70.43%)** total and
**3,205/4,833 (66.31%)** Game, with no address drift. Init remains 492/492
and Debugger 181/181. There are 1,628 different C functions and **252 more
exact matches** needed to reach 4,130/5,506, the 75% threshold.

## Recovered behavior and interface

- VA `0x150F0198..0x150F0260`; ROM `0x11D648..0x11D710`.
- Arguments 0–3 and 5 are unsigned bytes. Argument 4 is the owner pointer;
  argument 6 is a complete signed 32-bit word. Unproven argument meanings
  remain numbered rather than receiving speculative names.
- The routine snapshots the owner pointer, creates a header with flags 2,
  sentinel -1, duration 300 and type `0x21`, and supplies a zero position.
- It calls `func_151602C0` with the four byte arguments, `255, 0, 4`, the
  fifth byte and final word. On success it copies the four-byte owner
  payload to the returned object at offset `0x18`, then returns the object.
  Failure returns null without the payload copy.
- `Header` is six bytes, including an untouched padding byte. The guest
  tests preserve the original padding behavior; native tests do not read
  or assert an indeterminate C padding value.
- The existing `memcpy` prototype moves before the recovered routine,
  alongside the typed factory declaration. Shared headers do not change.

The source comment describes the type-0x21 effect and owner payload. The
original function name is retained for traceability. Call relocation offsets
are `0x8C` (`func_151602C0`) and `0xA8` (`memcpy`).

## Qualification

Eight fresh checks passed in each tools checkout before installation. Two
fresh installed checks passed afterward in each copy; six semantic checks
were reused only after complete input, module and artifact fingerprint
identity. Shared tools checks passed in both copies.

| Evidence | Measured result |
| --- | --- |
| Complete owner and actual Make | 44 functions; 43 unchanged neighbors; all three Make commands reproduced the qualified padded object; no target compiler diagnostics |
| Direct guest execution | 1,664 cases; all 50 words covered; all five byte lanes, word boundaries, owner snapshot, null gate and incoming-home mutations |
| Original factory and wrapper | 72 connected cases; all 79 words covered (47 + 32); body failure, wrapper failure with cleanup, and success |
| Original caller | 72 cases through the nine-word window at `0x150EF33C`; seven arguments and returned-pointer store verified |
| Native 32-bit SDK | 115,200 cases each at O0, O2 and O3 with trapping UBSan, valid pointer backing and nine effective controls |
| Fault prefixes | 258 direct/connected and 83 caller prefixes; complete guest state, PC and memory trace compared; 18 direct/connected delay-slot cuts |
| Independent GNU links | Three layouts, 72 cases; original assembly, actual-Make object and selected C agree |
| Rejection controls | 52 changed word/binding probes, nine compiled semantic controls and nine whole-image corruptions rejected |
| Whole image | Exactly 152 changed bytes: 151 code bytes and one extent byte; zero metadata changes or exclusions |
| Protected Game data | 189,088 bytes across 720 owners unchanged |

The original caller is `func_150EEF80`, whose current C remains a
placeholder. Its original JAL is at VA `0x150EF354` / ROM `0x11C804`.
The caller passes `70, 255, 130, 0`, the owner, a byte and a complete word,
then stores the result at its state offset `0x2C`. This is a bounded original
instruction window, not a recovered parent C call.

The connected helpers are `func_151602C0` and `func_1516037C` from
`conker/src/game_18D770.c`. The latter allocates 28 bytes, copies the six-byte
header and stores the body pointer; the factory adds its flag and handles
cleanup on wrapper failure. External services `func_1515D5F8`,
`func_15167A68`, `func_1515F10C` and `memcpy` remain bounded in this test.
No complete provider, parent, hardware or gameplay acceptance is claimed.

Two initial harness issues were corrected before acceptance: the native
loop index signedness and the oracle's missing signed-byte load needed by
the negative control. The production candidate did not change. Negative
semantic comparisons exclude incidental private stack addresses and the
unspecified header padding byte; positive guest comparisons remain complete.

## Image and provenance

The independent image predictor changes only the literal 200-byte retail
body and the symbol extent from 12 to 200 bytes. Production reproduces the
private first link exactly. All 6,056 canonical function addresses and the
other 6,055 bodies are preserved. The progress inventory and inherited
guard CSV are unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor ELF | `e85af7c47fd8491a2d2fb28b8f025e0e5ff48e8bd529756b0476451fdec694ae` |
| Adopted ELF | `9d72b10678221387976993a584fefa58b12a3686483a3d6adf7f3b5ec8e0a128` |
| Adopted owner C | `f56b55fd19c0526da60908a1e0d6f10784bf4a0cf4eac7e4cf10ce842eaf0fd8` |
| Qualified padded owner | `f7a4fe4996e1e43ba5d4a3abe71543a645a9c36166292f00f5091389e13eaaa3` |
| Raw relocatable body | `79543186a84e4093e137a210bd099acea312e832f1a2362924b39b3df61a528d` |
| Retail body | `e9471b777e5c9c1fb7040b83546913ea919a1d7a4c58e82fe1c4cb17c0cb7887` |

The tools are committed first as `7e435ccb46713e5e6514f3c99fa8ed1b6ffab76b`,
following `4a20d04bd4fd8bce5be413f8ce810fe87126367f`. The consumer predecessor
is `678693f6b2bea6dd95720675452a2c298ca0895d`. The older tools mirror's
1,841 inherited dirty paths are preserved; three qualified modules are
added there without committing that mirror. No push is performed.

The ignored receipt directory is `conker/build/game-payload-effect-factory-match/`.
It retains 439 focused inputs, the 16,498-path input seal, private and
canonical test receipts, the actual-Make proof, production audit, live ELF
recount and independent final audit. Graphify is refreshed for the changed
sources and documents with old-node and valid-edge retention checks;
historical clustering is retained, not recomputed.

## Review and continuation

Codex implemented and validated this routine. Claude budget/attempted/completed:
0/0/0; local literal, ABI, caller and whole-image evidence resolved the task.
The wider 75% goal remains active. Next inspect the 50-word
`func_151025F4` in `conker/src/game/generated_12DAB0.c`.
`func_1514E920` remains parked and uncredited. The remaining source shapes
are 1,499 placeholders, 120 semantic/other and nine unlocated functions;
queue ordering is a screen, not an ABI or matching qualification.
