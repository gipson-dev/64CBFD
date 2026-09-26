# Game nullable field cleanup match - 2026-09-26

## Result

`func_150F631C` is byte-exact directly from C across all 19 words, or 76
bytes, at `0x150F631C..0x150F6368`. The fresh linked matcher reports
2,659 / 5,483 exact C functions overall and 2,091 / 4,794 in Game.

## Recovered behavior

The function reads pointer fields at object offsets `0x30` and `0x34`. Each
non-null pointer is passed independently to `func_1516972C`.

The former C allowed IDO to retain the first field value in `a1`, which moved
the object owner to `a2` and changed both control-flow schedules. An explicit
owner lifetime retains the object in retail's `a1`. Marking the condition and
call-argument reads of offset `0x30` volatile preserves retail's separate
loads: the null test uses `t6`, while the call argument is reloaded into `a0`.

That source shape directly recovers the first branch-likely preload of offset
`0x34`, the owner spill and reload around the first call, the second nullable
call, and the complete epilogue. No guarded rows were required. The shared
patch table remains at 1,059 rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x12379C` and pristine retail
span `conker.us.bin+0x1237CC` are both 76 bytes and compare equal. Both hash
to:

`3d01686575967f832331b203dee11e677b94a8f8dc7ef88d6a270e2d887e1cdc`

The focused object rebuild, relocation-aware disassembly, linked ELF, objcopy
binary, fresh matcher, and exact span comparison pass. The shared patch table
did not change, so no all-consumer rebuild was required. The outer nonmatching
build, `make tools-check`, all project-tool unit tests, and `git diff --check`
also pass.

## Sibling audit

`64CBFDOGL` contains `func_150F631C` only in generated recompilation and
configuration artifacts and symbol references; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known three-word live-C compiler
overflow. Skip `func_15125628` in this queue: its source notes identify the
retail routine as probable handwritten assembly whose repeated self-base
global accesses cannot be produced plausibly from IDO C. Raw-assembly
ownership remains a separate workstream.

Continue with 19-word `func_15131958`, the next ordinary Game C row with
sixteen real differences. Its current implementation is a zero-returning
placeholder, while several actor-update callers pass a state block at offset
`0x58` and a related value from offset `0xA8`; behavior recovery is required
before compiler matching.
