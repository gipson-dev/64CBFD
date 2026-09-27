# Game object-index wrapper match - 2026-09-26

## Result

`func_15083FB0` is byte-exact across all 20 words and 80 bytes at
`0x15083FB0..0x15084000`. Fresh totals are 2,718 / 5,469 exact C functions
overall and 2,147 / 4,791 in Game.

## Recovery

The existing high-level behavior was correct: look up an object by byte
identifier through `func_15083E90`, return minus one when no object is found,
or subtract the `D_800CC2D0` object-table base and divide by the `0x32C` record
size to return its index.

The mismatch came from the local callee contract. An unspecified integer
return and parameter let IDO postpone the byte normalization into the call
delay slot, moving every later instruction. Declaring `func_15083E90` as a
pointer-returning function with a `u8` identifier makes IDO home and normalize
`$a0` before saving `$ra`, leave the call delay slot empty, select retail's
`$t7` table-base register, and place the stack restoration in the return delay
slot. Explicit integer-address casts preserve the intended pointer difference.

## Evidence

Linked ELF offset `0xC3FB0` and decompressed retail offset `0xB1460` compare
equal for 80 bytes, both with SHA-256
`903332ebe2d5ba12e58c9139e884b7c32ffd83b60f3c6211225b7df5bea4368c`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,718 / 5,469 (49.70%) | 1 | 2,750 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,147 / 4,791 (44.81%) | 0 | 2,644 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue with 20-word `guMtxIdentF`, the other smallest unparked Game candidate
in the fresh 19-real-difference tier. Keep the measured compiler boundaries
for `func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
