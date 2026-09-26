# Game active-player-mask predicate match - 2026-09-26

## Result

`func_151464B8` is byte-exact across its complete 20-word, 80-byte span at
`0x151464B8..0x15146508`. The fresh matcher reports 2,693 / 5,469 exact C
functions overall and 2,122 / 4,791 in Game.

## Behavior

The function constructs a signed 16-bit mask with bits zero through
`D_80082FA0` set. It ANDs that mask with the halfword at offset two in the
caller's object and returns a byte boolean indicating that no active-player
bit is present. A negative `D_80082FA0` skips the loop and therefore returns
true for every input.

## Source recovery

The previous C already represented the loop's behavior, but initialized the
16-bit mask before the loop index, returned `s32`, and kept the final mask test
as one expression. IDO consequently omitted retail's opening input-pointer
copy, reversed the two zero-initialization registers, and used a different
three-register return sequence.

The matching reconstruction declares the `u8` return, assigns `i` before
`mask`, and retains the masked halfword in a named `s32` local. An
optimized-away `^ 0` preserves that local's retail lifetime. An all-ones mask
on the boolean return is also optimized away but makes IDO select retail's
`sltiu t1` followed by `andi v0` sequence. The decomp permuter found this final
zero-score form after the hand reconstruction had matched the first 18 words.
All 20 words compile directly; there are no guarded retail-word rows.

## Exact-byte evidence

The linked ELF slice at offset `0x1864B8` and pristine decompressed retail
slice at offset `0x173968` compare equal for all 80 bytes. Both have SHA-256
`39b706408f76f7e1676a9c8d19fce2a64ed7d81da41e115e35b876a8ccf2e25e`.
The fresh matcher moved exactly this row from different to exact:

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,693 / 5,469 (49.24%) | 1 | 2,775 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,122 / 4,791 (44.29%) | 0 | 2,669 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

`64CBFDOGL/recomp_out/.c` still contains the prior 19-word generated body. It
begins at retail's second instruction, uses the old mask/index initialization
order, and ends with an extra padded `nop`; a future controlled recomp
regeneration must consume the corrected 20-word guest body. The sibling's
1,659 existing dirty entries were preserved, and frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` remains 13,712,896 bytes
with timestamp `2026-09-23 05:04:28`.

## Validation

- The focused `game_16EE20.c.o` production build emits all 20 retail words.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh sequential `progress` and LIST `match-progress` runs pass.
- The independent 80-byte linked-versus-retail comparison passes.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Continue ordinary Game reconstruction with 20-word `func_1514ED3C`, the next
nonblocked Game C row at 18 real differences. It is currently a zero-return
placeholder in `src/game/generated_179F30.c`; reconstruct it from
`asm/179F30.s`. The next ordinary Init C row is 20-word `func_10001000` at 14
real differences; keep address-blocked `func_10012588` parked.
