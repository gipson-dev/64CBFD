# Game indexed callback forwarding match - 2026-09-26

## Result

`func_15147D1C` is byte-exact directly from C across all 18 words, or 72
bytes, at `0x15147D1C..0x15147D64`. The fresh linked matcher reports
2,663 / 5,483 exact C functions overall and 2,095 / 4,794 in Game.

## Recovered behavior

The function reads a callback-table index from object offset `0x20`, loads the
corresponding entry from `D_8008A390`, and invokes it when non-null.

The former C called the callback with no arguments. Retail preserves the
incoming object and scalar in `a0` and `a1`, normalizes the third argument to
`u8` in `a2`, and forwards all three through the indirect call. Giving the
function pointer its `void (*)(u8 *, s32, u8)` type and passing those arguments
directly recovers all sixteen mismatched words, including the argument
normalization, table-index register colors, branch-likely, and `jalr`.

No guarded rows were required. The shared patch table remains at 1,060 rows
with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x17519C` and pristine retail
span `conker.us.bin+0x1751CC` are both 72 bytes and compare equal. Both hash
to:

`447aedea4176680dcea5ebbc7b72ab9d9d3242591a52ef5a1e3d7310fe91d57b`

The focused object rebuild, relocation-aware disassembly, linked ELF, objcopy
binary, fresh matcher, and exact span comparison pass. The shared patch table
did not change, so no all-consumer rebuild was required. The outer nonmatching
build, `make tools-check`, all project-tool unit tests, and `git diff --check`
also pass.

## Sibling audit

`64CBFDOGL` contains `func_15147D1C` only in generated recompilation,
configuration, and symbol artifacts; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known three-word live-C compiler
overflow. Keep probable handwritten `func_15125628` out of the ordinary C
matching queue; raw-assembly ownership remains a separate workstream.

Continue with 18-word `func_1515C158`, the next ordinary Game C row with
sixteen real differences. Establish its source, callers, and retail behavior
before changing compiler shape or adding guarded rows.
