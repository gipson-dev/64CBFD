# Game scaled angle components match - 2026-09-26

## Result

`func_15143874` is byte-exact directly from C across all 25 words, or 100
bytes, at `0x15143874..0x151438D8`. The fresh linked matcher reports
2,662 / 5,483 exact C functions overall and 2,094 / 4,794 in Game.

## Recovered behavior

The function looks up an angle value through `func_151423D8`, subtracts
`0x40` from the angle for a quarter-turn-offset second lookup, multiplies both
lookup results by the supplied scalar, and writes the two scaled components to
separate output pointers.

Retail receives a sign-extended angle. Correcting the first argument from
`u8` to `s16` restores the initial low-byte load used by the first table call
and the signed-halfword reload used to calculate the offset angle. An explicit
`u8 angle` local gives the narrowed second angle its retail `t6` lifetime and
recovers the `addiu`, `andi`, call, and delay-slot move sequence.

An explicit `f32 angleValue` local preserves the authored `arg1 * angleValue`
operand order for the first multiply. Together those source changes recover
all sixteen mismatched words directly. No guarded rows were required, and the
shared patch table remains at 1,060 rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x170CF4` and pristine retail
span `conker.us.bin+0x170D24` are both 100 bytes and compare equal. Both hash
to:

`8bab5dc83a5f1c990ffc6b98f5ea2635f4a7a8e6a997689f1d99fa3be6923cb7`

The focused object rebuild, relocation-aware disassembly, linked ELF, objcopy
binary, fresh matcher, and exact span comparison pass. The shared patch table
did not change, so no second all-consumer rebuild was required. The outer
nonmatching build, `make tools-check`, all project-tool unit tests, and
`git diff --check` also pass.

## Sibling audit

`64CBFDOGL` contains `func_15143874` only in generated recompilation,
configuration, and symbol artifacts; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known three-word live-C compiler
overflow. Keep probable handwritten `func_15125628` out of the ordinary C
matching queue; raw-assembly ownership remains a separate workstream.

Continue with 18-word `func_15147D1C`, the next ordinary Game C row with
sixteen real differences. Establish its source, callers, and retail behavior
before changing compiler shape or adding guarded rows.
