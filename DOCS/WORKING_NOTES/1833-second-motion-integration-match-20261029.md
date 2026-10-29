# Second motion integration callback C match

Verified 2026-10-29. `func_150CBE88` replaces the zero-return placeholder in
`conker/src/game/generated_F8590.c`. The original symbol remains unchanged. The existing `variables.h` declaration
supplies the time global; no shared declaration or header edit is needed.
VA `150CBE88..150CBF5C`, ROM `F9338..F940C`: 53 words, 212 bytes, no stack
frame, and two HI16/LO16 bindings to `D_800BE9A4`. Normal O2/g3 profile.

## Recovered behavior

The one-argument `s32 func_150CBE88(u8 *record)` snapshots acceleration at
`record+0x5C` and vertical velocity at `record+0x48`. It then updates:

- Position at `+0x38`, `+0x3C`, `+0x40` using velocities at `+0x44`, `+0x48`, `+0x4C`.
- Vertical position includes `((acceleration * dt) * dt) * 0.5f` in that order.
- Vertical velocity at `+0x48` using the acceleration increment.
- Angles at `+0x20`, `+0x24`, `+0x28` using rates at `+0x50`, `+0x54`, `+0x58`.

It returns one. The time global reloads after record stores; it is not cached
across the whole routine. Aliases between the global and record fields are
qualified. Local names describe recovered roles without asserting a particular
actor or gameplay identity.

The named local `delta` preserves the original ordered floating addition in
the vertical-velocity update. The initial draft and simply reversed source
expression produced a different quiet-NaN payload when both inputs were
NaNs. Those drafts remain rejected. The selected C and an ordered symbolic
store graph preserve the retail operand order without commuting arithmetic.
That graph models a global read conditionally seeing each preceding record
store, so the alias cases are included rather than assumed absent.

## Checked normalization and build

The complete C emits 53 words. Thirty-three expected-word guards normalize
closed register allocation and independent straight-line scheduling. There
are no inserted/omitted instructions, branches, calls, changed arithmetic
operators or commuted floating operands. Each guard checks its compiler
preimage and binding metadata; the inherited CSV prefix remains identical.
Raw C agrees on full memory and the return value. Normalized code agrees on
full register/FPR state and access prefixes. Raw fault-order equivalence is
not claimed.

The full owner preserves all 9 compact neighbors and normalized data pools.
The actual Make recipe has three commands: direct IDO compile, generated
padding, and assembly. A fresh execution reproduces the qualified padded
object without compiler diagnostics. Existing Makefile duplicate-recipe plan warnings concern
`generated_12D630`, whose inputs and object remain unchanged.

The literal linked-image prediction changes 158 bytes: 157 target-code bytes
and one target-extent byte. There are no symbol permutations or metadata
exclusions. All named values/types/sections remain fixed except the target's
extent. All 6,056 disassembled function addresses and 6,055 other bodies stay
fixed; all 189,088 protected Game bytes across 720 owners remain exact.
The map and conversion CSV remain unchanged.

## Qualification evidence

Eight fresh canonical methods and project tools checks pass independently in
both tools copies. All checks are fresh for this owner and table entry.

- 1,296 guest cases / 3,888 executions compare original, normalized and raw C.
  All 53 words are visited, including global/record aliases, signed zero,
  subnormals, finite overflow, infinities and distinct quiet-NaN payloads.
- Native32 O0/O2/O3 with UBSan: 648 cases per profile and six rejected mutants.
  A native-only global-indirection adapter permits the same record aliases
  while preserving the arithmetic body. Non-NaN outputs are bit-exact; native
  NaN payloads are not claimed identical to MIPS. Exact ordered payload checks
  belong to the guest and symbolic gates.
- 81 interrupted memory-access prefixes compare normalized/full retail state;
  three GNU relocation layouts cover 108 cases / 324 executions, including
  signed-low-half carry boundaries. Hardware FCSR and signaling NaNs are not
  claimed.
- 214 raw-byte/binding controls and 33 incorrect expected-word preimages are
  rejected. The initial operand-order source is also an effective negative control.
- 232 literal image mutations cover every target byte, its symbol record and
  selected ELF/outside bytes. The predictor compares the complete image.

The original dispatcher `func_151321D0` reaches this function through
`D_800898B0[2]`: ROM `22E378`, VA `800898B8`, also present in retained data ASM
`conker/asm/data/22E370.rodata.s`. Its 13-word window at VA `15132244`, ROM
`15F6F4`, passes 96 cases / 288 executions. Tests cover index-zero skip,
entry-two call/return-one, and restoration of the saved gate byte. Earlier
flags/table-selection behavior is an explicit precondition; complete parent
behavior and gameplay are not claimed. The aligned ROM scan finds one full
address registration and no direct JAL, without excluding computed encodings.

## Adoption and measured progress

Tools were committed first at `e7024c7a12a32f0410ef8c875818d5c1c617c491`. Production reproduces the
qualified object and independent 158-byte image. Each tools copy then passes
two fresh installed checks; six unchanged semantic methods are reused only
through complete input/module/artifact fingerprints.

ELF SHA256: `c87acd173db00d4dab0aa26c42b4d5327ae436e94d716985c057ddebe3b0ef45`.
Object SHA256: `a58a609d3b13e44706c689ea8d8dad22fe94ec908b3c1cf3783531ea328984ed`.
Source SHA256: `b0f0461ad94fc6428eefa300983166f20d7d4c9a9e0a43339a593d6c9319baa8`.

Actual recount: **3,910/5,506 (71.01%)**, Game **3,237/4,833 (66.98%)**,
Init 492/492 and Debugger 181/181, zero drift. **220 more** to the 4,130-function
75% threshold. Root README changes only two aggregate rows. The older tools
mirror preserves 1,937 inherited dirty paths plus three new modules, without
a mirror commit. The Graphify update is scoped; historical nodes and valid
relationships remain, without a full-corpus or new global-analytics claim.

`func_15030310` remains private and uncredited: 25,200 guest cases, 39 neighbors,
and 384 complete-wrapper cases support its behavior, but its best saved-role
form emits 52 words; a 53-word alternative still differs in 24 words. No
instruction insertion or broad branch rewriting is used for matching credit.
Its evidence remains in `conker/build/game-node-filter-cleanup-match/`.

Current evidence: `conker/build/game-kinematic-twin-match/`.
Next screen: `func_1507B974`, still private until separately qualified.
Other parked candidates remain uncredited. Keep the 75% goal active.
No push is performed.
