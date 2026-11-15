# Game state-24 motion callback: private recovery and matching boundary

Date: 2026-11-15. Continues the 85% total exact-C goal from
[Note 2469](2469-game-motion-effect-literal-recovery-and-guarded-match-20261115.md).

## Result and baseline

Recovered the complete ordinary C body of **`func_150C3574`** privately.
The selected candidate emits **264 words / 1,056 bytes / frame 0x38**, equal
to retail's length and frame, but has **81 differing words** after binding
its **40 relocations**. It is **uninstalled and uncredited**. No guard rows,
production source, compiler profile or shared declarations are changed.

Consumer baseline: `a0680e05737cebf18297f208066a3edae70abdc4`.
Starting mounted tools: `801108f29d429523171a8e8d7a215695e5e43df5`.
Recovery and tests are banked in tools commit
**`29fbb0b263ad1f235d39dff360c29f8496f44cb6`**, before the consumer docs/pin
commit. Local commits only; no push.

Fresh recount of the unchanged production ELF remains **4,503 / 5,514
(81.66%)** total, **3,830 / 4,841 (79.12%)** Game, Init **492 / 492**,
Debugger **181 / 181**, zero drift and **1,011** still different.
**184** additional qualified matches are needed for at least 85%.

## Retail behavior and caller interface

Owner: `conker/src/game_EF410.c`, eighteen functions.
Retail VA **0x150C3574..0x150C3994**, ROM **0xF0A24..0xF0E44**.
Original assembly remains in `conker/asm/nonmatchings/game_EF410/`.
The callback receives the actor pointer in A0; its caller ignores the return.
The private recovered signature is `void func_150C3574(u8 *actor)`.

The body initializes byte 0x80, applies the type-0x25 approach/deceleration
special case, selects the type-dependent animation scale, and submits the
existing movement helpers. It derives X/Z displacement rates at 0xBC/0x148,
computes their magnitude, limits the stored speed, handles byte-0x87 phase
four and doubles that byte. It updates heading when the speed/flag-0x13D
gate allows it, selects a forward or reversed halfword heading, submits the
turn and animation calls, and manages the looping sound. Sound selection
depends on actor type; volume is capped at 28,000 and halved for type 0x25.
The final low-speed stop test reloads state after preceding helper calls.
Unknown fields retain numeric offsets rather than speculative shared names.

The retained table at **D_80086014**, slot **24**, contains this callback at
ROM **0x22AB34**. The original fourteen-word dispatch window
**0x1504AB00..0x1504AB38** selects the table entry, observes actor flag
0x200 at 0x25C, and calls through **JALR 0x1504AB2C** with `S0 -> A0`.
The window is qualified through its declared end boundary. The surrounding
parent is not claimed as qualified. The other located table user,
`func_15022998`, restricts dispatch to states 4/27 and does not select slot 24.

## Fresh private qualification

The complete owner compiles under the existing **O2/g3/mips2/o32** profile,
without diagnostics. All **17 non-target neighbors** preserve code and
relative relocation identities. Normalized `.data`/`.rodata` are unchanged.
The new callback uses retained external coefficient labels from
`244DE0.rodata.s`; it adds no literal pool. The production checker for the
previously matched `func_150C2C00` accepts the new compact owner, preserving
that function's raw body, 58 bindings and exact **80-byte** literal pool.

- **1,536 finite cases, two instruction streams**: retail and reconstructed
  code agree with the separate reference on public memory and all helper
  arguments. All thirteen helper targets are exercised. Both streams visit
  263 distinct words; this is not a claim that every retail word executes.
  Cases cover actor types, phase flags, flag 0x13D, heading wrap, the 0.5
  speed boundary, the timer-30 boundary, sound presence and helper mutations.
  Providers clobber o32 caller-saved integer/FP registers and argument homes.
- **Native32 O0/O2/O3**: each passes all 1,536 vectors, checks the complete
  **640-byte** actor backing and global/call results, and rejects six compiled
  controls for phase shift, speed gate, reversed heading, volume cap,
  type-dependent volume and animation scale. Undefined-behavior traps are on.
- **576 original dispatch-window cases, two streams**: positive, blocked and
  null-entry paths pass. A corrupted actor-argument delay slot is rejected.
  A separate guest phase-shift mutation is also rejected.
- The four-test recovery suite passes freshly through the mounted tools in
  **23.402 seconds** and the sibling overlay in **27.553 seconds**.
  `make tools-check` passes.

This is finite-domain qualification with modeled callees. Exceptional floats,
NaN payload order, invalid float-to-integer conversion/FCSR behavior and
guest fault/access prefixes remain open. The current square-term allocation
reverses the order of the two add inputs relative to retail; finite agreement
does not settle exceptional payload behavior.

## Evidence preservation and compiler experiments

Ignored evidence is retained at
`conker/build/game-actor-motion-150c3574-private/`. It contains the immutable
**846-input production baseline**, complete generated C/objects and
diagnostics, disassembly, caller scan, fresh guest/native/caller receipts,
both suite receipts, recount, graph audit and sibling snapshots.

All **846 frozen production inputs remain byte-identical**, including the
actual ELF, owner object, source, guards, Makefile, conversion CSV and layout
inputs. Production ELF SHA-256 remains
`98936610b7d62b2ec3378dc8da56ac61f14e426bf0c76c9ef2154539a0afd573`.
The root README's aggregate rows are unchanged because no match is credited.

Selected raw target SHA-256:
`70dd14c2f17f6e24ed95e967bd815a49d49364c10d3dfafd5ce904114925a3a0`.
The first single-variable heading form emitted 263 words with 183 differing
positions. Making the current and selected headings explicit recovers the
264-word shape and reduces the count to 81. Small square-expression and
declaration-order experiments preserve all neighbors/pools but produce
263-word and/or frame-0x30 alternatives; none supersedes the selected form.
The ignored early `screen.py` describes the earlier source version; use the
committed recovery module to reproduce the selected fixture.

The sibling tools checkout remains at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, preserving all **2,434 dirty paths**
and Windows-Git status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Only the five new task files are copied into an ignored overlay; conflicting
sibling files are not overwritten. Scoped Graphify AST extraction of those
five files retains all **61,698 old IDs**, records **61,737 nodes / 115,741
links**, and loses zero IDs. This is not a full-corpus extraction. No host
port edit/build is made, and the Release checkpoint is untouched.

## Continue here

1. Use `python3 -m unittest tools.tests.test_game_actor_motion_150c3574_recovery
   -v` with the prepared consumer root to reproduce the private gates.
2. Resolve the magnitude calculation's FP allocation, extra scheduling NOP
   and branch-likely schedule, then the heading branch/delay-slot shape.
   Recover animation-scale/speed stack homes (retail SP+0x28 / SP+0x30;
   selected candidate SP+0x30 / SP+0x2C). Do not treat 81 differing words as
   two isolated scheduling changes or normalize them without proof.
3. Qualify any selected normalization with complete binding/word pins,
   liveness, exceptional behavior and fired guest-prefix controls; keep the
   previous emitter's pool guard intact. Extend the caller evidence only as
   required by measured changes.
4. Before adoption, pass both padders, actual Make, independent full-image
   prediction with zero exclusions, production audit, installed tests and
   actual recount. Then update aggregate rows and commit tools before the
   consumer pin/source/docs. Until those gates pass, credit remains zero.

The 85% goal stays active. Continue this function rather than beginning a
new broad conversion batch.
