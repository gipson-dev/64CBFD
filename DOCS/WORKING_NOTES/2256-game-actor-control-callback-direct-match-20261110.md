# Actor-control callback direct byte match

Date: 2026-11-10. `func_150F43F0` replaces its zero-return placeholder with a
semantic actor-control callback. The compiler emits all **94 retail body
words** directly, with a **0x28** frame and no guards. The two following zero
alignment words remain in the 96-word slot. The production recount is
**4,325 / 5,513 (78.45%)** overall and **3,652 / 4,840 (75.45%)** Game, with
zero drift and 1,188 different functions. The 80% threshold needs 86 more.

Owner `conker/src/game/generated_11FF10.c`; original retained in
`conker/asm/11FF10.s`. Body VA `0x150F43F0..0x150F4568`, ROM
`0x1218A0..0x121A18`; the two padding words extend the slot to VA
`0x150F4570` / ROM `0x121A20`. The function is index 24 of `D_80089670`
(table word ROM `0x22E190`), called through `func_15130230` when the context
selector byte is nonzero. The bounded dispatcher continuation ignores the
callback's return register, so the recovered interface is `void`.

For actor byte +0x23E equal to 0x3B, the callback requests input state 0x405C,
then checks the actor state and held field. When appropriate it invokes the
actor gate and, if successful, adjusts flags and two halfwords before invoking
an actor helper. It then initializes four actor floats and a word, or clears
the float at +0x190 on the alternate path. A different actor mode may invoke
the exit helper and clear the requested input state. Finally, two short-circuited
input queries determine whether bit 31 of the actor flags is set or cleared.
The names and purposes of individual actor fields and helpers remain inferred.

Validation covers 672 guest cases reaching every body instruction, including
mutating helper models and input-query short circuiting, and 672 typed SDK32
cases per O0/O2/O3 profile with UBSan and eight effective incorrect-source
controls. The original 13-word indirect dispatcher window passes 192 connected
cases. Sparse guest-memory tests check four skipped and two required reads of
the held field; they do not establish portable-C fault behavior. The helper
implementations remain modeled, and full parent or hardware behavior is not
claimed.

Both object padding paths agree with the original body and bindings; 16 rebased
GNU links and 71 access-boundary quads pass. Actual-Make shadow compilation and
the strict independent complete-image prediction account for **300 changed
bytes** with zero exclusions. The other 11 owner functions, all 6,050 function
addresses, the two padding words, and all 189,088 protected data bytes remain
unchanged. The actual ELF SHA-256 is `4ceecb7bc1948eae3f89e5d2bc72695e4bb955820bffd6c1ef43f306b040bb8f`. The existing
full-build checksum mismatch remains; this function match does not imply a
matching complete ROM.

The qualification tools were committed first as `ff015054a3f0e9d3f86eb937025b848e21dbc332`.
The consumer source and this note are committed separately. No push is implied.
