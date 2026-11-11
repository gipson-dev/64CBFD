# Oscillation callback direct byte match

Date: 2026-11-10. `func_150D317C` replaces its zero-return placeholder with a
typed record oscillation callback. The compiler emits all **96 retail words**
directly, with a **0x20** frame and no guards. The production recount is
**4,323 / 5,513 (78.41%)** overall and **3,650 / 4,840 (75.41%)** Game, with
zero address drift and 1,190 different functions. The 80% threshold needs 88
more matches.

Owner `conker/src/game/generated_FFBA0.c`; original retained in
`conker/asm/FFBA0.s`. Target VA `0x150D317C..0x150D32FC`, ROM
`0x10062C..0x1007AC`. It occupies index 38 of callback table `D_80089D60`
(table word at ROM `0x22E8B8`). The original `func_1513CFE4` dispatcher uses
record byte +0x71 as that index and incorporates the callback return value in
its removal decision. This is a bounded dispatch observation, not a claim that
the entire parent has been qualified.

The record's nested motion block at +0x110 contains two output values, bases,
amplitudes, phases and rates, followed by a timer and byte multiplier. Each
phase advances by its rate times `D_800BE9A4`, is normalized by
`func_15144B68`, and feeds `sinf` to update the corresponding output. The timer
is reduced by the current frame step, its product with the multiplier is
converted to unsigned and stored at record +0x5C, and the routine returns
whether the timer is positive. Names such as `opacity` and `opacityRate` are
inferred from use and are not established original-source identifiers.

Validation covers 480 guest cases with mutating helper models, 162 defined
SDK32 cases per O0/O2/O3 profile with UBSan and eight effective incorrect-source
controls, and 240 cases through the original 13-word indirect dispatch window.
Another 98 bounded finite-angle cases connect the original 24-word angle
normalizer and execute every one of its words; the sine helper remains a model.
The guest's FCSR restoration check is a bounded nontrapping model, not a
hardware proof. Native C tests restrict float-to-unsigned conversion to finite
values in range; the original instructions cover additional edge cases, but
portable C behavior for an invalid conversion is not claimed. Original word
77 is an unreachable duplicate retained in the exact body.

Both object padding paths agree with the original body and bindings; 16 rebased
GNU links and 165 access-boundary quads pass. Actual-Make shadow compilation
and the independent strict complete-image prediction account for **283 changed
bytes** with zero exclusions. The other five owner functions, all 6,050 function
addresses and all 189,088 protected data bytes remain unchanged. The actual ELF
SHA-256 is `e79c33578f1c68189acef7547f44ec977b0e9b2adabe428a765bce8f2c4ea95d`. The existing full-build checksum mismatch
remains; this function match does not imply a matching complete ROM.

The qualification tools were committed first as `17ffe90a8fada514e2cc08ab3fa565ffe64915eb`.
The consumer source and this note are committed separately. No push is implied.
