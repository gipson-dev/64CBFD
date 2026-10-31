# 1892 - Actor payload callback and retail return layout

`func_150D1F6C` replaces the zero-return placeholder in
`conker/src/game/generated_FF0E0.c` with a complete semantic handler. The
callback ABI is `void (struct260 *actor, s32 payloadAddress, u8 command)`.
The existing O2/g3 profile emits 56 words; eight checked guard rows restore
the complete 58-word retail slot, including two original RA reloads.

## Retail contract

- VA `0x150D1F6C..0x150D2054`, ROM `0xFF41C..0xFF504`: 232 bytes,
  58 slot words and no alignment words. Frame 24, saved RA at SP+20,
  incoming command home at SP+32. The full incoming third argument is saved
  before its low byte selects the command.
- Callback table `D_8008A8D8` has 74 entries; slot 41, VA `0x8008A97C`,
  ROM `0x22F43C`, registers this function. The original 23-word dispatcher
  `func_15149434` forwards actor, payload address and byte command and ignores
  a return value. Its existing typed table declaration establishes the ABI.
- A local state view begins at actor+`0x28`. Its position at local `0x18`
  maps actor `0x40..0x48`; value at local `0x3C` maps actor `0x64`;
  owner at local `0x40` maps actor `0x68`; flag byte at local `0x44`
  maps actor `0x6C`. The payload has a three-float vector and fourth float.
- Command `0x32` copies three payload words in retail load/store order and
  then copies the fourth float into the value field. Commands `0x30/0x31`
  require payload identity to match the owner field, then set/clear bit zero
  without changing other flag bits. Command `0x4E` copies `D_800A5480` into
  the actor position; command `0x4F` releases the actor through
  `func_1516972C`. Other commands do nothing. No invented NULL guard is added.

The shared headers, other signatures and compiler profile remain unchanged.
Local named state/payload types describe only the fields the original accesses.

## Return normalization

The raw 56-word body has identical semantic operations and register roles.
Retail duplicates two saved-RA reloads on separate exits. Eight guard rows
restore their two store/branch schedules and associated forward branch offsets;
two inserted `lw ra,20(sp)` words restore the original delay-slot reloads.
The original frame, saved-register lifetime and actor/payload operations remain
unchanged. Three relocation bindings retain their symbols and kinds while
moving to their original offsets. No instruction is omitted.

Raw payload SHA-256:
`223da744ea8e76639471ec8ee2afdc705f09465c16965b5860460ee2a5dabe04`.
Normalized payload SHA-256:
`60819ed76446ac1a877a23490e2a2a5c0665e5095b1f5fc17a53576da5ad5dd8`.

Each guard has an expected word and expected relocation preimage. Sixteen
deliberately invalid word/binding cases are rejected by the actual padder.
The complete inherited guard prefix remains byte-identical. This is a guarded
match; the raw compiler body is not described as byte-exact retail code.

## Qualification

Artifacts and receipts:
`conker/build/game-actor-command-payload-150D1F6C-match/`.

- The whole owner preserves all four neighboring functions and normalized
  pools. The target, before/after owner and actual Make emit no diagnostics.
  Three actual Make commands reproduce the qualified padded object.
- 2,576 guest cases / 7,728 executions cover every command and flag byte,
  high command homes, float bit patterns, identity gates, seven payload alias
  layouts and release side effects. All 57 reachable original instructions
  execute; the duplicate load at offset `0x84` is unreachable. Raw C agrees
  on public memory and calls; original and normalized streams agree on complete
  machine state, traces and fault context. Raw fault scheduling is not equated.
- Original and normalized code agree at 42 access-prefix cuts, including seven
  branch-delay cuts. Nine independently rebased original/raw/normalized cases
  preserve symbol bindings and public behavior.
- The original 28-word release helper executes all 28 words across type,
  destructor/fallback and pre-service type-mutation routes. Bookkeeping and
  lower release services remain bounded providers; their full internals are
  not claimed. The complete original dispatcher passes 96 cases including
  registered, NULL and out-of-range slots; all 23 dispatcher words execute.
- Native SDK32 checks pass 131,168 cases per profile at O0/O2/O3 with UBSan,
  typed callback invocation and complete envelope/canary comparison. Native
  identity commands include aliases. Partial overlapping structure copies are
  guest-machine extensions, not claimed portable C behavior. Copy-command
  native cases use a separate typed payload. Twelve float bit patterns include
  zeros, extremes, infinities and NaN payloads.
- Ten separately compiled semantic changes are effective in both IDO guest
  and native checks. Compiler/interpreter failures do not count as controls.
- Eight canonical checks and shared tools checks pass in each tools copy.
  After production, two installed checks rerun in each copy, with six unchanged
  semantic checks reused only under exact input/module/artifact fingerprints.
- The production ELF equals an independent literal prediction with zero
  exclusions: 169 changed bytes, comprising 168 target-code bytes and one
  function-extent byte; zero metadata changes. All 6,055 other disassembled
  function bodies and all addresses stay fixed. Protected Game data remains
  byte-exact across 189,088 bytes and 720 owners. Inventory CSV stays unchanged.

Production ELF SHA-256:
`fa76db5c79433c9fa27238794dfdcfd76a6fe3f3bc2031ed75107b78de90a76b`.

## Banking and continuation

The tools commit `025de7f54b8db9dce33a62b7fba0a903637ac7fc` precedes the consumer commit. Only the three new
canonical tool modules are committed in tools; the older mirror's inherited
changes remain preserved. No push or host/gameplay acceptance claim is made.

Actual adopted-ELF recount: **3,969 / 5,506 exact C (72.08%)**; Game
**3,296 / 4,833 (68.20%)**, Init 492/492 and Debugger 181/181. Address drift
is zero; 1,537 C functions remain different. The active 75% goal requires
4,130 exact functions, leaving **161** more. Root README changes only its
two aggregate rows; function details remain in this note.

Graphify receives an eleven-file structural refresh with prior-node and valid
relationship retention checks, retiring obsolete placeholder return edges.
Historical communities remain historical; no full-corpus extraction, global
clustering or centrality recomputation is claimed.

Next screening candidate: `func_151DCEF0`. Private candidates remain uncredited.
