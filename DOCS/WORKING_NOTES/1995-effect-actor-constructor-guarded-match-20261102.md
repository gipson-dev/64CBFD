# 1995 - Effect-actor constructor recovered as guarded C

Verified 2026-11-02. Production **4,062/5,508 (73.75%)**; Game
**3,389/4,835 (70.09%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,446 different; one newly converted and byte-exact function. The active
80% target is now **4,407/5,508**, requiring **345 more**. This is progress
toward that goal, not completion.

## Interface and recovered behavior

`void *func_15154884(EffectVector15154884 *position, f32 lifetime,
f32 amplitude, f32 height, u8 slot, s32 context)` replaces the assembly
placeholder in `conker/src/game/generated_17CAF0.c`. Original `17CAF0.s`:
VA15154884..15154A88, ROM181D34, 516 bytes, 129 words, 192-byte frame and
seventeen relocation bindings. The position input is exactly three floats.
The constructor uses a natural 120-byte actor descriptor and a complete
20-byte motion payload; 112 descriptor bytes are semantically required and
eight remain private.

Non-positive lifetime returns null without drawing random values or allocating.
A positive lifetime builds the payload from lifetime, amplitude and height,
sets phase to zero and computes its rate from `D_800A601C / lifetime`. The
descriptor receives three randomized rotations, the complete caller position,
zero velocity, two randomized scalar fields, fixed flags/resource/duration and
the recovered control bytes. `func_15132A4C` receives the descriptor, payload
size, all 256 possible slot bytes and the full context. Successful allocation
copies all 20 payload bytes to offset 0x170; failed allocation returns null
without that copy.

The complete linked-image census finds exactly one aligned JAL: ROM103980,
VA150D64D0 in `func_150D6434` (VA150D6434..150D64E8). Its original words prove
all six O32 arguments: the forwarded three-float position; positive randomized
lifetime; randomized amplitude and height; zero-extended low caller byte; and
full caller context. The delay slot is a nop and conservative return-value
taint reaches no later read. No aligned jump or literal function pointer exists.
Complete parent gameplay execution is not claimed.

## Closed compiler words

The semantic C emits the complete 129-word extent and preserves all seventeen
relocation bindings. Its natural compiler frame is 184 bytes. Ten checked
expected-word normalizations close only the independent compiler layout choices:

- the opening frame-size word;
- six argument-home and corresponding load offsets;
- two result-spill offsets around the successful allocation path;
- the closing frame-release word.

Three independently shifted GNU links agree after those ten closed words. Raw
semantic payload SHA256:
`2928aca1c9b3c1784c71bd02c9b4e109b82e8b4afdc376117c414482aea361cf`.
Normalized payload SHA256:
`c47339d343812ae28a46b1f71b195a21c40e23f28c0742244f0e030de1c0a96a`.

## Fresh qualification

- Guest execution covers 256 cases at each of three independent links and
  three images, for 2,304 executions. It reaches 128/129 words; the sole
  unreachable word is the duplicate one-constant load at VA151548BC. Positive,
  zero and negative lifetime, allocation success/failure and all five random
  calls execute.
- Original, normalized and raw C agree in complete public machine, call,
  descriptor and payload state. Every case snapshots all 12 position bytes,
  120 descriptor bytes and 20 payload bytes. Live position and constant
  mutations prove the recovered read timing.
- Native O0/O2/O3 runs 256 cases per profile, 768 total, with warnings treated
  as errors and UBSan stopping at the first error. Every profile is clean, all
  256 slot values execute, success/failure paths agree and complete input
  fences remain intact.
- The caller census proves the sole original JAL and all six O32 arguments.
  Alternate-source code is not used for ABI proof.

The permanent five-method suite reproduces raw/binding, guest, caller, native
and complete-image gates from retained receipts. It passes after installation
against the actual production object and ELF. The bounded Graphify refresh is
structural AST only, retains every prior node and every still-valid prior edge
occurrence and uses zero LLM tokens: 58,196 nodes and 119,866 links retain all
58,130 prior nodes and all 119,735 prior edge occurrences. No obsolete prior
edge requires retirement. No full-corpus extraction, global reclustering or
gameplay acceptance is claimed.

## Owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified object. Protected Game data remains
exactly 189,088 bytes across 720 owners, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The strict complete-image predictor has zero exclusions: all 6,052 function
addresses, 6,051 other bodies and the complete named-definition multiset remain
fixed. Because the guarded C reproduces the original target bytes, the entire
predicted linked image is byte-identical. The installed production object
equals the qualified five-command Make object, and the production ELF equals
the independent strict whole-image prediction exactly.

Installed object SHA256:
`486b0599b1480bcbe15d9fa114c62a563916857a4660d1bf07d53d9dff2b8a80`.
Linked ELF SHA256:
`752feb861f0a37a4ce3ee397f1a52952a048048aff9c3521ad2b3ff3d9b122da`.
Production linker-map SHA256:
`ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.
The retained private-link map SHA256 is
`4b149099ac4b1762a1a0abe62502fd3e127f017e1e9b9ff38c1ea1345392259f`.

The public qualification tools were committed first at `76c84de`; their source
cleanup was committed at `5a385bd`. The retained stage is
`conker/build/game-effect-actor-constructor-15154884-match/`; it contains the
layout, guest, native, caller, owner, whole-image and installed receipts. The
root README changes only aggregate rows; detailed recovery stays here and in
the five concise indexes. No Claude call was needed.

## Next step

Privately audit `func_15154A88`, the next assembly placeholder in this owner.
Keep it uncredited until ABI/caller, semantic runtime, owner/actual-Make,
strict-image, installed recount, documentation and bounded Graphify-retention
gates pass.
