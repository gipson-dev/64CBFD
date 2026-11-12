# Game position interpolation guarded match

Date: 2026-11-12. `func_150BE2E8` replaces its placeholder in
`conker/src/game/generated_EB340.c`. Its 84-word slot spans VA
`0x150BE2E8..0x150BE438`, ROM `0xEB798..0xEB8E8`.

The callback reads two signed three-component positions and signed fixed-point
step and progress values. It updates the step using `D_800A0068`, advances
progress by `D_800BE9E4`, writes three interpolated halfword coordinates,
then clamps progress above one and writes both scaled halfword values. The
clamp occurs after coordinate calculation. `func_1509E900` installs entry
56 of `D_80088C90` into the actor callback field; two original indirect-call
windows in `func_15113E54` pass that actor to the callback.

The target-only `-Wo,-no_const_in_reg` profile preserves seven ordinary
owner neighbors. Ten expected-word guards normalize floating-point operand
order and a closed register-allocation cycle; the final linked function is
byte-exact, including the four global relocations. The guards retain retail
instruction ordering rather than asserting that C NaN payloads or FPU
exception behavior are portable.

Both tools environments passed seven preinstall and seven installed checks.
The bounded finite guest screens cover 400 cases and a further 1,863
cross-product cases, including overlapping actor/global layouts; 337
out-of-range float-to-integer cases were excluded. Two original four-word
call windows each cover 100 cases, and the bounded access-cut model covers
240 prefixes including completed executions. The native 32-bit defined-domain
screen covers 200 cases at O0/O2/O3 and a trapping UBSan build at O2; three
incorrect controls fail. These do not prove full parent execution, native
fault behavior, or behavior of C conversions for NaN, infinity and out-of-range
values. The byte-exact guest instructions retain retail behavior for those
inputs subject to the execution environment.

Both padding paths and 12 independently rebased GNU links agree with retail.
Actual Make reproduces the independent strict ELF prediction: 285 changed
bytes, zero exclusions, all function addresses fixed, and all 189,088
protected data bytes unchanged. The rebuilt ELF SHA-256 is
`29fa52d17d549bda4c89f100a025d2cd7c369bd3d3da6a630bfa92c16001836b`. The existing whole-ROM checksum mismatch remains.

Fresh ELF recount: **3,704 / 4,840 (76.53%)** Game and **4,377 / 5,513
(79.39%)** overall, zero address drift. The Game 80% target needs **168**
more matches. Tools commit `e8ed75ff935b135a1e31a10e66af99f2b23fd150` precedes the consumer change. See
[Note 2307](2307-game-position-interpolation-candidate-screen-20261112.md)
for the private candidate history and limits.
