# Ground-motion callback direct byte match

Date: 2026-11-11. `func_150EAE24` replaces a zero-return placeholder in
`conker/src/game/generated_117490.c`; the original is in
`conker/asm/117490.s`. Its 74-word body occupies VA
`0x150EAE24..0x150EAF4C`, followed by one zero alignment word, within ROM
`0x1182D4..0x118400`. The body emits directly from C, with a 0x38-byte frame
and no new guards. Ten neighboring function bodies remain unchanged.

The callback advances two horizontal coordinates, writes truncated coordinates
to the attached position record, queries ground height, chooses the queried or
fallback height, and decreases a remaining-time value. A typed motion layout
and existing `struct225`/`struct226` fields describe the observed accesses.
The scratch/native model uses a matching extended-record layout; a complete
project-wide object-layout audit and exceptional floating-point behavior are
not claimed.

The original dispatcher `func_151603FC` reads entry 19 of `D_8008B0F0`
(address `0x8008B13C`, ROM `0x22FBFC`) and passes the record pointer in
`a0`. The C dispatcher now explicitly passes that pointer through a function
pointer conversion; its prior zero-argument call did not express the original
ABI. All 78 compiled functions in its owner retain their bodies, with only
`.mdebug` differing in the independent raw-object audit and all 36 existing
compiler diagnostics unchanged. The shared table declaration and other table
entry types remain a separate, unqualified audit; no claim is made that all
other callback C signatures are compatible.

Thirty-two bounded guest cases visit all 74 retail body words, including
helper-driven frame-delta and output-pointer changes. SDK32 native O0/O2/O3
pass 16 finite cases and nine negative controls per profile; the native layout
is modeled. Sixteen bounded cases execute the complete original dispatcher,
verified table entry and callback, with ground and cleanup helpers modeled.
The corrected dispatcher separately passes 16 native cases and three negative
controls per profile. Sixteen cases execute 29 of 32 original ground-helper
words while modeling its precheck and fallback. NaNs, out-of-range float to
integer conversions, arbitrary helper side effects, hardware faults and
concurrency are not qualified.

Both object padders and independently assembled retail code agree; 16 rebased
GNU links and 64 bounded access-cut quads pass. Actual Make and an independent
strict image comparison account for **212 changed bytes** with zero
exclusions. All 6,050 function addresses and 189,088 protected data bytes
remain unchanged. The actual ELF SHA-256 is `0870afaf1e9ac585b5c7e52796c6689e3024e0b0be8e2f18cad3a20e36a46d8f`. The
existing complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,338 / 5,513 (78.69%)** overall and **3,665 /
4,840 (75.72%)** Game, zero drift and 1,175 different. The 80% target needs
73 more exact functions. Tools were committed first as
`c2c2f6cdce13c1e09de4a8bca0db9b9b2bec785c`; the consumer change is separate.
