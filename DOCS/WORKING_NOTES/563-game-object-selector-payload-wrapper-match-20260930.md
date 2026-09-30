# Game object-selector payload wrapper byte match

Date: 2026-09-30

`func_15192920` occupies 33 words and 132 bytes at
`0x15192920..0x151929A4`. A null owner is a no-op. For a non-null owner, the
function constructs a 12-byte local payload containing the owner pointer, the
byte at owner offset `0x3B`, and a zero float. It requests a command-`0x23`
record from `func_151491F4` with arguments
`(0x23, -1, 0x14, 1, 0x10, 0x0C, 0xFF, 1)`. If allocation succeeds, the local
payload is copied to record offset `0x28`.

Declaring the result pointer before the typed payload recovers retail's exact
`sp+0x28`, `sp+0x2C`, and `sp+0x30` local layout. Qualifying the incoming
pointer itself as volatile preserves retail's two independent argument-home
loads while retaining the original null-gated behavior.

Sixteen words emit directly from semantic C. Seventeen stale-checked,
non-relocating guards normalize one closed IDO schedule: retail performs the
second owner load before preparing call arguments, fills the local payload
before the overflow arguments, and stores the selector before the allocation
call with the zero float in its delay slot. The branches, call relocations,
argument values, local offsets, copy destination, and failure path are
unchanged.

The focused object, complete replacement link, outer `NON_MATCHING=1` ROM
build, and authoritative matcher pass. The linked ELF and pristine
decompressed retail spans share SHA-256
`22a75e9e7d0e3f7d317b63e54214725208a2fc9a4bdb938f04f0352aa72cda4a`.
The matcher advances exactly one row to `3,066 / 5,462 (56.13%)` overall and
`2,487 / 4,788 (51.94%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_151B1AB0`, the next ordinary matcher row.
