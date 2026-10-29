# Paired sine update direct C match — 2026-10-28

`func_151025F4` is recovered in `conker/src/game/generated_12DAB0.c` as
`s32 func_151025F4(PairedSineOwner *volatile owner, void *context)`.
All 50 instructions (200 bytes), the 48-byte frame and six symbol bindings
match directly from C using the existing IDO O2/g3/mips2/o32 profile.
There are no new guards or alignment words. All 22 other functions in the
complete owner remain unchanged.

The adopted ELF recount is **3,879/5,506 (70.45%)** total and
**3,206/4,833 (66.34%)** Game, with zero address drift. Init remains
492/492 and Debugger 181/181. There are 1,627 different C functions and
**251 more exact matches** needed to reach 4,130/5,506, the 75% threshold.

## Recovered behavior and interface

- VA `0x151025F4..0x151026BC`; ROM `0x12FAA4..0x12FB6C`.
- The owner's state starts at offset `0xA8`. Each output is its base plus
  its amplitude multiplied by the sine of its phase.
- Both outputs are evaluated before their stores. Each phase then advances
  by its own rate multiplied by `D_800BE9A4`. The routine normalizes the
  phases with `func_15144B68` and returns 1.
- The second parameter is an unused context pointer supplied by the
  original callback dispatcher. Native tests cover null, buffer-start and
  valid one-past pointers without dereferencing or changing the context.
- The owner is reloaded after the first sine call. Loading the second phase
  before advancing the state pointer resolves the last two scheduling words.
- The source comment explains the operation. The local structure reserves
  the retail frame and first-sine stack slot; its declaration and the
  volatile spelling are matching choices, not proof of the original C.

Call relocations are at `0x18` and `0x2C` for `sinf`, and `0x98` and `0xA4`
for `func_15144B68`. `D_800BE9A4` has HI16/LO16 bindings at `0x4C`/`0x50`.
The original function name remains for traceability; shared headers do not
change.

## Qualification

Eight fresh checks passed in each tools copy before installation. Two fresh
installed checks passed in each copy afterward; six unchanged semantic
checks were reused only after complete input, module and qualified-artifact
fingerprint identity. Shared tools checks also passed in both copies.

| Evidence | Measured result |
| --- | --- |
| Complete owner and actual Make | 23 functions; 22 unchanged raw and padded neighbors; all three Make commands reproduced the qualified padded object; no compiler diagnostics |
| Direct guest execution | 632 cases, all 50 words covered; 160 clock-alias cases; late owner, phase and global reads; caller-saved clobbers |
| Original math helpers | 84 connected cases; complete 104-word sine and 24-word phase-normalization bodies; 103 + 24 reachable words covered |
| Original callback | 64 cases through a 17-word slot-11 dispatcher window; signed selector, gate, owner/context arguments and return gate verified |
| Native 32-bit SDK | 648 cases each at O0, O2 and O3 with trapping UBSan; 216 input patterns and three context pointers; valid owner backing, fences and context preserved |
| Fault prefixes | 136 direct/connected and 36 caller prefix pairs; full guest state, PC and trace compared; 14 direct/connected delay-slot cuts |
| Independent GNU links | Three layouts, 96 cases; original assembly, actual-Make object and selected C agree, including signed-low address layouts |
| Rejection controls | 56 changed word/binding probes; seven effective native and nine compiled guest semantic controls; nine whole-image corruptions rejected |
| Whole image | Exactly 155 changed bytes: 154 code bytes and one extent byte; zero metadata changes or exclusions |
| Protected Game data | 189,088 bytes across 720 owners unchanged |

An aligned whole-ROM scan found no direct JAL and one function pointer at
ROM `0x22E24C` / VA `0x8008978C`: slot 11 of the 40-entry `D_80089760`
table in `conker/asm/data/22E220.rodata.s`.
The original `func_151303EC` dispatcher window is
`0x15130A0C..0x15130A50` (ROM `0x15DEBC..0x15DF00`). It reads the signed
selector at owner offset `0x72`, skips selector -1 or an active gate,
passes the owner and `SP+0x48`, and calls through JALR at `0x15130A38`.
The recovered return value 1 leaves its gate clear. The parent's current C
in `generated_15D730.c` remains a placeholder; this is a bounded original
instruction window, not a current C caller edge or full-parent acceptance.

The connected helpers are `sinf` in `conker/src/libultra/gu/sinf.c` and
`func_15144B68` in `conker/src/game_16EE20.c`. The sine's unvisited word at
offset `0xCC` is the already-qualified dead duplicate; the complete literal
body remains intact. All 24 normalization words are covered. The bound
`D_800A56A4` is the original float value `0x40C90FDB`.
Native math hooks are scripted; real math is supplied by the separate
connected original-instruction checks. Unbounded huge/infinite phase-wrap
completion, FCSR parity, hardware execution and gameplay are not claimed.

The early-owner and cached-clock negative controls use guest-only memory
mutations and aliases. They are not portable C aliasing claims. Every
compiled semantic control terminates without an incidental fault. Positive
guest comparisons retain full state; negative semantic decisions exclude
incidental private stack addresses.

## Image and provenance

The independent image prediction changes only the literal 200-byte retail
body and the symbol extent from 12 to 200 bytes. Production reproduces the
qualified private link exactly. All 6,056 canonical function addresses and
the other 6,055 bodies remain fixed. The progress inventory and inherited
guard CSV are unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor ELF | `9d72b10678221387976993a584fefa58b12a3686483a3d6adf7f3b5ec8e0a128` |
| Adopted ELF | `d58ca358aebe9cfdc02775b59e8fb8c705be28ed99b204ad673680e9cd5e5c16` |
| Adopted owner C | `5df65684c00323dfb14685a6bdf599d02ed4fc18e336b86dd3e333cf2330d98f` |
| Qualified padded owner | `5e5117df750e93ad8d091fc53dd5685689986e2ba9ac72e0ae490386d6edbcd9` |
| Raw relocatable body | `4dfd1772218ae56b8139216160c372003502ad0ecb9b9a0f5397c0ce7eb46550` |
| Retail body | `e2f53fa325ebccad5ee8bd7ee9be0db1c6a64e53f62bee8d2c1e93b96c7f0ddc` |

Tools were committed first as `4e83f09976b576d0befab468b3a490d05f9f98d3`,
following `7e435ccb46713e5e6514f3c99fa8ed1b6ffab76b`. The consumer predecessor
is `f00c56cb1a6249e84dd42af001c4ea99ebc610ee`. The older tools mirror's
1,844 inherited dirty paths are preserved; three qualified modules are added
without committing that mirror. No push is performed.

The ignored receipt directory is `conker/build/game-paired-sine-update-match/`.
It retains 449 focused inputs, the 16,505-path input seal, private/canonical
checks, actual-Make proof, production audit, live recount and independent
final audit. Graphify is refreshed for the changed sources and documents,
with old-node and valid-edge retention checks; historical clustering and
centrality are retained rather than recomputed.

## Review and continuation

Codex implemented and validated this routine. Claude budget/attempted/completed:
0/0/0. Local literal, ABI, callback and whole-image evidence resolved it.
The 75% goal remains active. Next inspect the 50-word `func_1510A344` in
`conker/src/game/generated_1368C0.c`. `func_1514E920` remains parked and
uncredited. The remaining shapes are 1,498 placeholders, 120 semantic/other
and nine unlocated functions; queue ordering is a screen, not qualification.
