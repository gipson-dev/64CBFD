# Game record-copy builder match - 2026-09-26

## Result

`func_15167D84` is byte-exact across all 34 words at
`0x15167D84..0x15167E0C`. The linked matcher reports 2,651 / 5,483 exact C
functions overall and 2,083 / 4,794 in Game.

## Recovered behavior

The existing C behavior is correct. The function selects record kind `5` when
`arg1` is zero and kind `0x42` otherwise, then calls `func_15167A68` with a
payload size of `arg2 + 0x50`. When allocation succeeds, it copies `0x38`
bytes from `arg0` into the record payload at offset `0x10` and stores signed
byte `arg3` at record offset `0x48`.

IDO merges the null and populated paths into one compact epilogue. Retail
branches positively into the populated path, retains the result in `v1`, and
uses a separate null-path branch with an early `ra` reload before both paths
join at the frame teardown.

Thirteen guarded rows restore that CFG and register schedule. The first two
rows insert the missing `v1 = v0` copy and null-path `ra` reload; later rows
move the `bcopy` relocation, preserve `v1` across the call, reload the result
into `v0`, and reproduce the signed-byte update and teardown. The guards
therefore affect all fifteen differing words. The patch table now contains
991 rows with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x195204` and retail span
`conker.us.bin+0x195234` are both 136 bytes and compare equal. Both hash to:

`7bcd11da7cda505394e2f8dac0e719bf4e7d17bf8a61eb6544310623116e321f`

Changing the shared patch table triggered an exhaustive rebuild of every
padded consumer. The linked ELF, objcopy binary, fresh matcher, and exact span
comparison pass. The outer nonmatching build, `make tools-check`, all six
project-tool unit tests, and `git diff --check` also pass.

## Sibling audit

`64CBFDOGL` contains `func_15167D84` in generated recompilation outputs,
symbol/configuration lists, and one historical working note. There is no
separate maintained host implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Skip handwritten `func_151F892C` and `func_151F8960`. Continue with 41-word
`func_151D2E5C`, the sole remaining ordinary-C row in the fresh 15-difference
queue. For selector `0`, it compares linked-record identifiers and may call
`func_1516972C`; for selector `0x2D`, it rewires the record pointer and its
associated byte depending on which endpoint matches. The linked matcher
reports fifteen real differences.
