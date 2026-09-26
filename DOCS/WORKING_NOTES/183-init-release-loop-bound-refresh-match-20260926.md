# Init release-loop bound refresh match - 2026-09-26

## Result

`func_1000FD38` is byte-exact across its complete 47-word, 188-byte span at
`0x1000FD38..0x1000FDF4`. The fresh matcher reports 2,691 / 5,475 exact C
functions overall and 390 / 501 in Init.

## Behavior and compiler boundary

The existing C behavior was complete. It scans `D_80041FE0`, selects records
whose three identifiers match the arguments, releases a non-null owned object
through `func_100111C8`, and sets bit `0x80` in the record flags.

The first 41 words already matched. Current IDO reloads `D_80042760` after
every matching record, whether or not the release call runs. Retail retains
the cached bound across the no-call path and reloads it immediately after the
call, before loading and updating the record flags. This is observable if the
callee changes the bound, so it is more than a temporary-register choice.

A source-level cached `count` local, both plain and explicitly `register`, was
tested. IDO hoisted the global address into saved register `s5`, expanded the
body to 49 words, and overflowed into `__retail_overflow_func_1000FD38`.
Those experiments were reverted.

## Guarded normalization

Six guarded rows restore retail's branch and post-call schedule. The no-call
branch skips the reload; the call path moves the `D_80042760` LUI/LW pair and
its `R_MIPS_HI16`/`R_MIPS_LO16` relocations ahead of the record flag load,
update, and store. The frame, saved-register lifetimes, loop induction, calls,
and all other instructions remain unchanged.

## Exact-byte evidence

The linked Init-code slice at offset `0xED38` and pristine retail ROM slice at
offset `0xFD38` compare equal for all 188 bytes. Both have SHA-256
`d6c4a2d813bb07d09cda2a9aee5f4cb54f9e0ac388a66f9f0265775945c171e6`.
The fresh matcher moved exactly this row from different to exact:

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,691 / 5,475 (49.15%) | 1 | 2,783 |
| Init | 390 / 501 (77.84%) | 1 | 110 |
| Game | 2,120 / 4,793 (44.23%) | 0 | 2,673 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

`64CBFDOGL/recomp_out/.c` still contains the pre-normalization generated
schedule, which reloads `D_80042760` on both the call and no-call paths. A
future controlled recomp regeneration should consume the corrected retail
bytes because the sampling timing differs. No generated host source was
edited manually, and the sibling's 1,659-entry dirty tree and frozen Release
executable remain untouched.

## Validation

- The focused `init_EB00.c.o` build accepts all six guarded rows and both
  relocation moves.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and LIST `match-progress` runs pass.
- The independent 188-byte linked-versus-retail comparison passes.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Audit nine-word `func_10001420` before attempting another C rewrite. Its
retail `bnezl` loop, tiny extent, and prior C overflow are strong evidence of
handwritten SDK ownership. Keep address-blocked `func_10012588` parked.
