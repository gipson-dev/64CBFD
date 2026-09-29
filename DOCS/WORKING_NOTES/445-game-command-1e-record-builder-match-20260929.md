# Game command 0x1E record builder byte match

Date: 2026-09-29

## Scope

This pass completed `func_1518AB60` in
`conker/src/game/generated_1B7EC0.c`. The retail slot spans 28 words and 112
bytes at `0x1518AB60..0x1518ABD0`.

## Recovered behavior

The routine accepts a full-width owner value and a selector byte. It requests
a `0x20`-byte command `0x1E` record from `func_15167A68` with the fixed
arguments `(0x1E, 0, 0x20, 1, 0xFF, 1)`. Allocation failure returns `NULL`.
On success, it stores the owner at offset `0x10`, clears the words at offsets
`0x14` and `0x18`, stores the selector at offset `0x1C`, and returns the new
record.

A plain typed-record body produced the correct frame, call, branches, and
record contents, but IDO rotated five independent success-path scheduling
words. Making the destination record volatile restored the retail store and
return schedule, while making the selector parameter volatile and retaining
an explicit selector lifetime put its reload and store in the correct slots.
That semantic shape left only a linked two-word register-allocation cycle:
IDO selected `$a0` where retail selected `$t9`. Two expected-word guards
normalize that selector reload/store pair. The remaining 26 words, including
the call relocation and all control flow, emit directly from C.

## Verification

- The focused `generated_1B7EC0.c.o` build matches all 28 retail words after
  the two selector-register guards and retains one
  `R_MIPS_26:func_15167A68` relocation.
- The exhaustive `wsl make -C conker NON_MATCHING=1 -j1` rebuild validated the
  complete expected-word manifest and linked successfully.
- The linked ELF and retail 112-byte spans share SHA-256
  `efb71a2eeaa43131b257ca76adf61765cd193e36396339f8a3796fd61921b3d0`.
- Fresh matcher totals are `2,946 / 5,465 (53.91%)` overall and
  `2,372 / 4,789 (49.53%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_151C9AC0`, currently at
27 real differences. Its retail body builds a three-float vector from owner
offsets `0x14`, `0x180` plus `2.0f`, and `0x1C`, transforms it through
`func_1504715C`, then calls `func_151ABE40` with both stack vectors, mode `2`,
the selector byte, and the final word. Keep the documented lower-difference
compiler cases parked. Also keep `func_151F3D78` parked behind the existing
audio-object layout drift, keep the tied Init SDK cache routines in their
ownership lane, and keep address-drift row `func_10012588` parked.
