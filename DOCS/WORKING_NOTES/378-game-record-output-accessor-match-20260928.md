# Game record-output accessor match - 2026-09-28

## Result

`func_150A3330` is byte-exact across its complete 26-word, 104-byte retail
span at `0x150A3330..0x150A3398`.

The fresh linked matcher reports 2,876 / 5,466 (52.62%) exact C functions
overall and 2,302 / 4,790 (48.06%) in Game, with one address-drift blocker and
2,589 genuinely different C rows overall.

## Recovery

The function accepts a record index followed by four output pointers. It
indexes the table reached through `D_800D3098` using a `0x34`-byte stride, then
copies the unsigned byte at offset `0x17` and the signed words at offsets
`0x18`, `0x1C`, and `0x20` to those outputs.

The local record view includes explicit trailing padding so its C size matches
the retail stride. Repeating the global table expression for each output also
reproduces retail's four pointer reloads, which are required because the output
stores may alias global state. IDO naturally emits the exact strength-reduced
index calculation, register allocation, fifth stack-argument load, and store
schedule. No expected-word guards or compiler-profile override are used.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0xE3330` and the
pristine retail span at `conker/conker.us.bin` offset `0xD07E0` compare equal
across all 104 bytes. Both have SHA-256:

`eef8ecd23dcde0ee8054b8e53ed4bcb098a241dd3a748a52f173d0f0f8c8fc62`

## Validation

The focused object build, linked matcher, replacement build, outer ROM build,
project tool checks, all nine focused Python tests, direct byte comparison,
and whitespace validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 31-word Game `func_150E36BC`, currently at 25
real differences. Keep the smaller documented near-matches, `func_10003BD0`,
the Init SDK cache routines, address-drift-blocked `func_10012588`, and the
larger parked HUD renderers in their existing lanes.
