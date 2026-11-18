# Actor bound burst parent recovery screen - 2026-11-18

`func_150B7B40` now has two complete semantic C drafts in the tools repository.
They are **uninstalled and uncredited**. The preferred captured-model draft
has the complete **484-word retail length**; the other has485 words.
Both use a **0x258/600-byte frame**, versus retail's **0x268/616**. Positional
differences, register scheduling and private layout remain unresolved.

| Draft | Words | Frame | Positional differences including length |
| --- | ---: | ---: | ---: |
| Explicit samples, direct model expression (`portable-11`) | 485 | 0x258 | 386 |
| Captured second model lookup (`captured-model`) | 484 | 0x258 | 444 |
| Retail | 484 | 0x268 | 0 |

The production source remains its zero-return stub. Accepted matching stays
**4,546 / 5,514 (82.44%)** total, Game **3,873 / 4,841 (80.00%)**,
Init492/492 and Debugger181/181. There is zero address drift and968 converted
functions still differ. **141 more exact matches** reach85%; the goal stays
active. The root README is byte-for-byte unchanged because its aggregate
figures did not change. Detailed recovery belongs here, not in that overview.

## Scope and recovered behavior

Owner `conker/src/game/generated_E4070.c`, retail `conker/asm/E4070.s:1110`.
VA `0x150B7B40..0x150B82D0`, ROM `0xE4FF0..0xE5780`.
Baseline consumer `16aaec94ed1835ec1c5c8b9977881dcf40e1409c`, tools
`ca59f78d45880af90caa212dabd4fa64c879a6ed`.
The recovered interface is
`void func_150B7B40(ActorBurstE4070 *actor, u8 slot, s32 context)`.
A null actor returns immediately. Local actor/descriptor types preserve the
recovered field offsets without changing shared headers or neighboring bodies.

1. With a model, query points4,5 and0 into two endpoint vectors and an origin.
   Without one, copy the actor position and form endpoints at X+20/X-20,
   Y+130 and the original Z. Reload the actor's current heading for each of
   two sine-table calls; multiply their results by its current radial offset.
2. Reload the model after those providers. Transform the three bound vectors
   at `D_8009FD30/3C/48`, or invoke the no-model bounds provider. Derive height
   as absolute Y distance and radius as the square root of squared X/Z deltas.
   The height/radius ratio falls back to1 when radius equals zero.
3. Submit the now-qualified `func_150B82D0` and `func_150B85C0` interfaces with
   the current center, dimensions, slot and context. Their bodies stay frozen;
   both are modeled as opaque providers in this parent screen.
4. Form a ground probe at centerY+100, initialize its36-byte query result and
   query down to centerY-2000. On a hit, use the returned floor height and an
   explicitly sequenced unsigned RNG duration `%11+30` for the twelve-argument
   floor effect. Its first two floats are observed from F12/F14; later arguments
   come from A2/A3 and the outgoing homes. This checks the actual o32 interface.
5. Initialize the first descriptor's fixed fields and actor parameters. Clamp
   both factors to0.5..1.0 using retail's ordered comparisons. Derive average
   scale and component scales. For each endpoint, capture a float sample,
   choose two integer angles, call the sine provider four times, and compute
   the velocity plus actor radial offsets. Two further samples choose rotations.
   Submit the descriptor through `func_15132A4C`.
6. Reload the actor factors, derive the second descriptor's scales from their
   mean and `D_8009FD5C`, write its fixed fields and owner word, and call
   `func_15151A38` with slot/context. Repeat for the second endpoint.

The first descriptor consumer, `func_15132A4C` through `func_1513264C`, copies
**0x7C bytes**, including unspecified reserved bytes. This parent fixture
observes all124 bytes, rather than the prior helper fixture's120-byte modeled
window. The second descriptor's complete136 bytes are observed too. C/native
qualification must compare only initialized bytes; it has not yet been run.
Twelve first-descriptor and four second-descriptor bytes remain unwritten by
the recovered routine. Their guest entry coupling uses uniform0xA5 solely
for this finite screen; it is not an arbitrary-private-state proof.

## Fresh screens and limitations

The four maintained task files have the `game_actor_bound_burst_150b7b40` stem.
Both tools configurations pass **three fresh tests**, with no skips/errors:
**82.417s primary / 91.351s private sibling overlay**.
Each run fingerprints **312 imported tool files**.

- Both complete owners compile under existing O2/g3/no-unroll/MIPS2/o32.
  All20 compact neighbors and normalized pools remain unchanged. The preferred
  draft's raw SHA-256 is
  `f6ae7b3b5be62c55a8afbfc2189a8bc6737a7c81a3c045edc5eb340904d8d9e6`.
- The complete original function is independently GNU-assembled, bound and
  compared to all1936 ROM bytes. No retail words are used as replacement code.
- Retail and both drafts each pass129 cases, with4,160 provider calls per
  stream. Cases cover null/model/no-model paths, zero dimensions, floor hit/miss,
  clamp ranges, slot/context propagation and mutable providers. Providers can
  mutate actor fields and retain escaped vectors/scalars/descriptors. Ordered
  observations, full descriptors, public effects, emitted final V0 and saved
  GPR/FPR values agree. The C interface remains void.
- All483 reachable retail words execute. The duplicate LUI at0x150B7D60 is
  preserved and unreachable. The485-word draft executes484 words; the484-word
  draft executes483. Raw screens use a synthetic code base so an overlong draft
  cannot collide with the real child entry at0x150B82D0. No raw object is installed.
- Eight compiled source negatives are rejected by semantic observations:
  heading, pitch, ground depth, child duration, spray kind, damping, upper clamp
  and loop count. They preserve all neighbors/pools. An initial floor-depth
  negative introduced a compiler literal and shifted the neighboring helper's
  raw pool offsets; the owner audit rejected that fixture. Both failed producers
  were terminal before correction. Failed fingerprints, receipts and objects
  are retained; final suites use separate v2 output directories.
- All **1696 frozen source/build/tool inputs remain exact**,
  including all698 production objects and the ELF. Required tools checks and
  current actual-ELF match-progress pass. No build, guard, shared header or
  production C change is installed. There is no new whole-image/adoption claim.

Production ELF remains
`46cfd670adb3a01257e59f77734a12a6ce785c3b2807ce7ceb7b154044ad2ed2`.
The sibling tools checkout's HEAD,2,434 dirty paths and343 dependencies remain
fixed. Its private overlay contains339 sibling files,398 pinned primary fallbacks
and four task files. Host Release and saves are untouched. Host applicability,
hardware behavior and live gameplay are unverified. No Claude call or push.

## Next work toward adoption

1. Add native32 O0/O2/O3 execution with strict aliasing/UBSan and effective
   source negatives, comparing112 initialized first-descriptor bytes and132
   initialized second-descriptor bytes. Preserve the explicit RNG sequencing.
2. Recover the616-byte retail frame and closed private-home/register roles
   from the484-word draft. Establish the complete instruction-driven relation,
   including arbitrary private bytes, provider effects and ordered FP/FCSR.
   The opcode histogram still differs by one float load, two address setups,
   one NOP, two integer moves and two MTC1s; equal length alone is not a match.
3. Connect the genuine caller `func_1507D754` at0x1507DA90 (slot255/context1,
   ignored return), then connect the two already-qualified child bodies. Their
   current opaque models do not establish complete live caller behavior.
4. Only after that qualification derive guards if needed, exercise both actual
   padders, independent rebases and corruption controls, predict the full image,
   run real production Make, audit/recount, document and commit tools first.

Graphify's native/scoped receipts retain old IDs and link the screen module
to the production stub. This is scoped extraction, not a full-corpus rebuild.
Continue this parent; Notes2531/2532 retain other uninstalled drafts separately.
