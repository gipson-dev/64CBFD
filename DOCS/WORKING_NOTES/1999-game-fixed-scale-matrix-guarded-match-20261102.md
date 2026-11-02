# 1999 - Fixed-point scale matrix recovered as guarded C

Verified 2026-11-02. Production **4,066/5,511 (73.78%)**; Game
**3,393/4,838 (70.13%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,445 different; one existing C placeholder is newly byte-exact. The
active 80% target is **4,409/5,511**, requiring **343 more**. This is progress
toward that goal, not completion.

## Interface and recovered behavior

`void func_150A7C10(volatile s16 *matrix, f32 x, f32 y, f32 z)` replaces the
zero-return placeholder in `conker/src/game/generated_D50C0.c`. Original
`D50C0.s`: VA150A7C10..150A7CB0, ROMD50C0, 160 bytes, 40 words and no stack
frame.

The routine is the game's local fixed-point scale-matrix constructor. It
converts X, Y and Z to signed 16.16 values, clears the complete 64-byte N64
matrix through eight 64-bit stores, writes the homogeneous diagonal one and
then writes each scale's integer and fractional halves to the corresponding
diagonal slots. The recovered behavior agrees with the retained libultra
`guScale` C and handwritten assembly implementations without adopting an SDK
symbol name that retail does not expose here.

The complete retail image contains no aligned JAL to this address and no
aligned literal function pointer. The function is a leaf and has no relocation
bindings. No parent gameplay execution or runtime call-route claim is made.

## Guarded compiler match

IDO's retail `-mips3` profile emits the required eight `sd` zero stores and a
complete 160-byte function. One word emits directly; 39 checked expected-word
guards normalize the handwritten retail register allocation and scheduling.
No word is inserted or omitted, every guard has empty relocation metadata, and
the final three alignment nops remain part of the exact slot.

Raw compiler payload SHA256:
`a084312c1c589353c2884a6bd6221d669320f53ba34c58007ab9a7a038e7d0cd`.
Retail slot SHA256:
`6d90a2cacb1541d0ae93057609ae5ebd2f8dbffef99097d84f913e89910b2ab4`.

## Fresh qualification

- Guest execution covers 21 independent X/Y/Z tuples at both aligned matrix
  phases against both the raw compiler body and guarded retail body. All 40 raw
  words and all 37 reachable retail words execute, all 64 output bytes agree
  with an independent 16.16 model, and callee-saved registers remain intact.
- Native 32-bit O0/O2/O3 execution covers negative, signed-zero, fractional,
  ordinary and boundary-scale values. Four source mutations are effective at
  every optimization profile: wrong scale factor, wrong X integer slot, wrong
  Z fractional slot and an uncleared tail.
- The permanent census proves zero aligned JAL callers and zero aligned literal
  pointers. Retained libultra `guScale` C and assembly provide independent SDK
  provenance for the matrix layout and conversion.
- Guard-staleness controls reject changes at the entry, the zero-store region,
  the scale publication and the final return/alignment region.

The five permanent tests pass after installation under WSL. A native-Windows
invocation is intentionally unsupported because the matching compiler is a
Linux executable; it failed before running a test and does not contradict the
successful WSL suite or production build.

## Owner, image and production result

The real generated-owner recipe uses `-mips3`, applies all 39 checked guards
and produces the exact 160-byte retail slot. Protected Game data remains
exactly 189,088 bytes across 720 owners with zero different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The strict complete-image predictor has zero exclusions. The installed full
rebuild recompiled every owner that consumes the shared guard table without a
stale-guard failure, linked successfully, and reproduced the frozen image and
unchanged map identities:

- owner object SHA256:
  `2ebe7dcc9068dbfd061016257a362e9954784a91b0455b5d7bf1be9ad929c7c7`;
- linked ELF SHA256:
  `9bd8b47f72c3aaf7cd478dd013d3505e361582e94800f9d90ae1646a98ea3166`;
- linker-map SHA256:
  `ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.

The qualification tools were committed first at `701a243`. The retained stage
is `conker/build/game-fixed-scale-matrix-150A7C10-match/`; it contains frozen
inputs, compiler diagnostics, proposed source/profile/guards, the exact padded
owner, expected complete image, guest/native artifacts and permanent test
receipts. The root README changes only aggregate rows. No Claude call or
gameplay claim was needed.

## Next step

Continue the ordinary Game queue from the freshly recounted non-exact ranking.
Keep handwritten custom-ABI `func_150A76F0` in its separate assembly workstream
and keep every new candidate private until the same ABI, runtime, owner,
actual-Make, whole-image, recount, documentation and graph-retention gates
pass.
