# 1996 - Effect-actor update callback recovered directly from C

Verified 2026-11-02. Production **4,063/5,509 (73.75%)**; Game
**3,390/4,836 (70.10%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,446 different; one newly converted and byte-exact function. The active
80% target is now **4,408/5,509**, requiring **345 more**. This is progress
toward that goal, not completion.

## Interface and recovered behavior

`s32 func_15154A88(u8 *actor)` replaces the assembly placeholder in
`conker/src/game/generated_17CAF0.c`. Original `17CAF0.s`:
VA15154A88..15154C90, ROM181F38, 520 bytes, 130 words and a 24-byte frame.
The routine is registered only through `D_800898B0[18]`, whose original
pointer literal is at ROM22E3B8 / VA800898F8. The bounded original dispatcher
window in `func_151321D0` is VA15132244..15132278. Its ABI is
`s32(u8 *actor)`: a nonzero result keeps the actor and zero requests expiration.
No aligned direct JAL or jump to the callback exists.

The callback evaluates `sinf` at payload phase `actor+0x17C`, scales both actor
size fields by payload amplitude, and derives the opacity byte from the low
payload byte and the same wave. It subtracts the live frame delta
`D_800BE9A4` from payload lifetime and returns zero immediately when that
lifetime is no longer positive. A live actor advances phase by its payload
rate and integrates all three position coordinates from velocity using the
same frame delta before returning one.

The recovered source preserves the unsigned conversion shape around the
opacity byte. Alternate-source code was consulted only as a semantic clue;
its types were unsuitable for byte matching. The installed declaration,
types, comments and behavior are independently established from the retail
routine, registration table, dispatcher and runtime controls.

## Direct compiler match

The semantic C emits all 130 retail words directly with no expected-word
guards. Its three relocation bindings are exact:

- `+0x0C R_MIPS_26 sinf`;
- `+0x1C R_MIPS_HI16 D_800BE9A4`;
- `+0x28 R_MIPS_LO16 D_800BE9A4`.

Three independently shifted GNU links agree with the original routine. Raw
unresolved object SHA256:
`91be33265a4774f1628ef1270a0b65f738e4cda19b54893d56ce2af3468daee5`.
Linked retail payload SHA256:
`d578acd5448e5f5d9ce53a5cc2a6326ae48702fb27acce539fc0889a516770e0`.

## Fresh qualification

- Guest execution covers 256 cases at each of three independent links, 768
  executions total. Positive, zero and negative lifetime branches, every one
  of the 256 opacity input bytes and live `sinf` mutations execute. Original
  and raw-C words produce equal checked state.
- The bounded defined-conversion domain reaches 90/130 words. The remaining
  compiler exception scaffolding concerns floating-to-unsigned conversion;
  hardware FCSR and out-of-range conversion behavior are not claimed.
- Native O0/O2/O3 runs 256 cases per profile, 768 total, with five effective
  negative controls per profile, complete 512-byte image comparison, canaries
  and stop-on-first-error UBSan. Every profile is clean.
- Registration qualification proves the sole original pointer literal, slot
  18, callback ABI and zero/nonzero dispatcher meaning. Complete parent
  gameplay execution is not claimed.

The permanent five-method suite reproduces raw/binding, guest, native,
registration, owner/padder/actual-Make and complete-image gates from retained
receipts. It passes after installation against the actual production object
and ELF. The bounded Graphify refresh is structural AST only, retains every
prior node and every prior edge occurrence, and uses zero LLM tokens. No
full-corpus extraction, global reclustering or gameplay acceptance is claimed.

## Owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified object. Protected Game data remains
exactly 189,088 bytes across 720 owners, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The strict complete-image predictor has zero exclusions: all 6,052 function
addresses, 6,051 other bodies and the complete named-definition multiset
remain fixed. Because the direct C reproduces the original target bytes, the
entire predicted linked image is byte-identical. The installed production
object equals the qualified five-command Make object, and the production ELF
equals the independent strict whole-image prediction exactly.

Installed object SHA256:
`486b0599b1480bcbe15d9fa114c62a563916857a4660d1bf07d53d9dff2b8a80`.
Linked ELF SHA256:
`752feb861f0a37a4ce3ee397f1a52952a048048aff9c3521ad2b3ff3d9b122da`.
Production linker-map SHA256:
`ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.

The public qualification tools were committed first at `046f385`. The retained
stage is `conker/build/game-effect-actor-update-15154A88-match/`; it contains
the source, guest, native, registration, owner, whole-image and installed
receipts. The root README changes only aggregate rows; detailed recovery stays
here and in the five concise indexes. No Claude call was needed.

## Next step

Privately audit `func_1515548C`, the next assembly placeholder after the
already recovered `func_15154C90` and `func_15154D80`. Keep it uncredited until
ABI/caller, semantic runtime, owner/actual-Make, strict-image, installed
recount, documentation and bounded Graphify-retention gates pass.
