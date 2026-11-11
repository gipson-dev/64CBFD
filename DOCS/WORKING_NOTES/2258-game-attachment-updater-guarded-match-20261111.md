# Attachment updater guarded byte match

Date: 2026-11-11. `func_1518A094` restores an attachment update callback in
`conker/src/game/generated_1B74A0.c`; the original assembly remains in
`conker/asm/1B74A0.s`. The 96-word routine occupies VA
`0x1518A094..0x1518A214` and ROM `0x1B7544..0x1B76C4`, with a 0x50 frame.
Its semantic C emits 96 words; **42 expected-word guards** normalize private
stack slots, temporary registers, the callback gate, and return scheduling.
This is a guarded match rather than a direct compiler match.

The routine resolves an absent actor reference by its byte identity, checks
that the reference remains active and has the same identity, and optionally
invokes a signed-index subtype callback. If enabled, it transforms two point
triples through the selected 64-byte matrix and updates object flags; it
clears the relevant flag if the matrix is absent. The original record
dispatcher `func_1513CFE4` invokes this routine via index 2 of `D_80089CB8`
and uses a zero result to mark the record for removal.

Validation covers 2,048 original/raw/normalized guest cases, including modeled
callback and helper mutations, and 1,536 defined SDK32 native cases per
O0/O2/O3 with UBSan and eight effective negative controls. Negative subtype
indices other than -1 are modeled in guest checks but excluded from defined
native C cases. The original bounded dispatcher window passes 1,024 cases.
All four original subtype handlers are connected for 768 cases; the original
actor lookup covers all 26 slots over 162 cases, and the original 40-word
matrix helper runs over 128 finite-float cases. These are bounded tests; full
parent behavior, hardware FCSR, raw private-stack equivalence, callback aliases
outside their intended byte, and portable fault behavior are not claimed.

Both object padders agree with independently assembled retail code. The
qualification rejects 394 corrupted byte/binding inputs and 42 individually
corrupted guards, and passes 16 rebased links and 132 access-cut quads. Actual
Make and the independent complete-image comparison account for **339 changed
bytes**, including two explicitly checked symbol-order groups, with zero
exclusions. Five other owner functions, all 6,050 function addresses, and
189,088 protected data bytes remain unchanged. The production ELF SHA-256
is `d1e3fc9d0ec67a186db9956e0a4610fbb21a17ccd14e8a635b2fa33bd9986af5`. The existing full-build checksum mismatch remains;
this function match does not imply a matching complete ROM.

Fresh actual ELF recount: **4,327 / 5,513 (78.49%)** overall and **3,654 /
4,840 (75.50%)** Game, zero drift and 1,186 different. The 80% target needs
84 more exact functions. The tools were committed first as
`d04e40ba3a05d74b6ea0fa7c67243e673c93e43b`; the consumer change is committed
separately. No push is implied.
