# Game second motion-threshold update byte match

Date: 2026-09-29

`func_151AFC08` occupies 32 words and 128 bytes at
`0x151AFC08..0x151AFC88`. When object flag bit zero is set, it may lower the
progress byte to eight times the signed stage. If the stage exceeds the nested
motion threshold, it adds the nested rate scaled by `D_800BE9A4` to both
accumulators. It always returns one.

The routine is instruction-identical to `func_150CC638`. It uses the same typed
semantic C shape and the same 13 stale-checked expected-word transformations,
including two inserted address words, to normalize IDO's closed register and
scheduling choice. The full rebuild and non-matching link succeed. The matcher
reports `3,040 / 5,463 (55.65%)` overall and `2,462 / 4,789 (51.41%)` in Game
with no drift. Linked Game offset `0x1AFC08` and retail ROM offset `0x1DD0B8`
share SHA-256
`f513b7f3c9bee8f04c2afe8007ea87e74d5ba3cd3a2c240639dcd9bc60eb3bfe`.
`make tools-check` and all 10 tool unit tests pass.

Resume with Game `func_151B70B4`, the next ordinary 36-word matcher row. Keep
the four documented special-case rows parked.
