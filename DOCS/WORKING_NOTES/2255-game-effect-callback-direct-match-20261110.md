# Effect callback direct byte match

Date: 2026-11-10. `func_150DDFAC` replaces its zero-return placeholder with a
typed effect-submission callback. The compiler emits all **96 retail words**
directly, with a **0x90** frame and no guards. The production recount is
**4,324 / 5,513 (78.43%)** overall and **3,651 / 4,840 (75.43%)** Game, with
zero address drift and 1,189 different functions. The 80% threshold needs 87
more matches.

Owner `conker/src/game/generated_108E90.c`; original retained in
`conker/asm/108E90.s`. Target VA `0x150DDFAC..0x150DE12C`, ROM
`0x10B45C..0x10B5DC`. It occupies index 3 of callback table `D_8008A430`
(table word ROM `0x22EEFC`). A bounded original `func_15148BA4` dispatcher
window forwards the actor, three previous-position floats, a height and a
pointer; the callback's integer result controls the continuation.

The routine caches the actor's payload and position table, samples a float
random value to obtain a range, and writes 4 to payload offset +0x20. It uses
an integer random bit to choose descriptor kind 29 or 30, initializes the
defined descriptor fields, then takes three further random samples. It selects
a 20-byte position record using the signed actor index at +0x2D and submits the
descriptor through `func_1513C73C` with 14 arguments, including the caller's
height and pointer, the sampled range, random values and actor tags. The
callback returns 1. Descriptor field names are inferred from their use.

Validation covers 332 guest cases with mutating helper models, all initialized
descriptor fields and five ordered random calls; 216 defined SDK32 cases per
O0/O2/O3 profile with UBSan and eight effective incorrect-source controls; and
72 connected cases through the 19-word original dispatcher window with all six
callback arguments checked. Twelve seeds connect the original 43-word 64-bit
random helpers, visit every helper word and verify all five seed transitions.
The final effect-submission helper remains modeled; full parent behavior and
actual gameplay are not claimed. Caller-home mutations are guest-only, and
portable-C fault behavior is not claimed. Original words 29 and 30 are
unreachable under the one-bit selector and retained in the exact body.

Both object padding paths agree with the original body and bindings; 16 rebased
GNU links and 245 access-boundary quads pass. Actual-Make shadow compilation
and the independent strict complete-image prediction account for **297 changed
bytes** with zero exclusions. The other 11 owner functions, all 6,050 function
addresses and all 189,088 protected data bytes remain unchanged. The actual ELF
SHA-256 is `d3a81a68afc40ac396815c54c7df7ccd4408eaa381bd882b83585ad3cf0a7fdc`. The existing full-build checksum mismatch
remains; this function match does not imply a matching complete ROM.

The qualification tools were committed first as `ad0d220e43faaea3f1773c3b90cce02d615996b9`.
The consumer source and this note are committed separately. No push is implied.
