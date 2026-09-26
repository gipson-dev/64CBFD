# Game vector scale loop match - 2026-09-26

## Result

`func_15131958` is byte-exact directly from C across all 19 words, or 76
bytes, at `0x15131958..0x151319A4`. The fresh linked matcher reports
2,660 / 5,483 exact C functions overall and 2,092 / 4,794 in Game.

## Recovered behavior

The former implementation was a zero-returning placeholder. The retail
routine accepts a three-component `f32` vector and a scalar, loads the signed
loop count from `D_800BE9E4`, and repeatedly multiplies all three components
in place while the count remains positive.

Giving the routine its `void func_15131958(f32 *, f32)` signature and using
the same types at its two local call sites preserves the scalar's raw float
bits in incoming register `a1`. The straightforward loop directly recovers
retail's unrolled three-load, three-multiply, three-store schedule, count
decrement, and final component store in the loop branch delay slot. No guarded
rows were required. The shared patch table remains at 1,059 rows with zero
duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x15EDD8` and pristine retail
span `conker.us.bin+0x15EE08` are both 76 bytes and compare equal. Both hash
to:

`071b713780f4c96bc385a05aae4a1c1ec20fc1f2d62dd15ac19f9760f6e15877`

The focused object rebuild, relocation-aware disassembly, linked ELF, objcopy
binary, fresh matcher, and exact span comparison pass. The shared patch table
did not change, so no all-consumer rebuild was required. The outer nonmatching
build, `make tools-check`, all project-tool unit tests, and `git diff --check`
also pass.

## Sibling audit

`64CBFDOGL` contains `func_15131958` only in generated recompilation,
configuration, and symbol artifacts; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known three-word live-C compiler
overflow. Keep probable handwritten `func_15125628` out of the ordinary C
matching queue; raw-assembly ownership remains a separate workstream.

Continue with 43-word `func_151419D0`, the next ordinary Game C row with
sixteen real differences. Establish its current source and retail behavior
before changing compiler shape or adding guarded rows.
