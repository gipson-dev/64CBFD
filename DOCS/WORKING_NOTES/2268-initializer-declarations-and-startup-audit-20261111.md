# Initializer declaration and startup audit

Date: 2026-11-11. Follow-up to [Note 2267](2267-game-ten-entry-initializer-direct-match-20261111.md). The committed initializer remains a 91-word direct byte match; this audit does not change the match count.

`D_800BE4E0` is used as the address of a ten-entry table. The restored `generated_3D2E0.c` declares it as `Entry10 *`, while `include/variables.h` and `generated_F5800.c` declare it as `s32`. The initializer declares `func_150ADA20` as returning `u32`, whereas `include/functions.h` and the other source declare `s32`. These declarations have the same 32-bit o32 machine representation but are inconsistent across translation units; the byte comparison alone does not establish C type compatibility.

Private IDO screens found two possible directions. A localized version using the existing `s32` global declaration and an explicit unsigned conversion of the random result emitted all 91 retail words and left the two neighboring function bodies unchanged. A pointer-typed version in both affected source files kept all 3 and 19 compiled function bodies, respectively, unchanged; its only observed raw object section change was `.mdebug`. Neither version is installed or fully qualified. A shared-header edit could affect other compiled objects and must be audited at section level; it must not be credited based only on these screens. The pinned initializer tests and manifests would also need updating and independent revalidation.

The next unmatched startup routine `func_1500E470` has a commented source reconstruction in `conker/src/game_3B920.c`. A private screen compiles it without diagnostics, but emits 82 words against the 84-word retail slot and has scheduling and register differences. A volatile-access experiment emitted 84 words but differs in 20 positions; it is not evidence that the retail accesses were volatile. Neither candidate has been adopted or subjected to the full caller, helper, padders, guest/native, image, and production checks. Its original direct caller includes `func_15007B3C` at `0x15007FA4`.

The current production recount remains **4,336 / 5,513 (78.65%)**, with zero drift and **75** further exact functions needed for 80%. The existing complete-ROM checksum mismatch remains.

The startup routine was subsequently qualified and adopted in [Note 2269](2269-game-startup-initializer-match-20261111.md); the declaration inconsistency remains open.
