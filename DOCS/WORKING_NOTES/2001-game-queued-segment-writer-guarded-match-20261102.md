# 2001 - Queued segment writer matched as guarded C

Verified 2026-11-02. Production **4,068/5,511 (73.82%)**; Game
**3,395/4,838 (70.17%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,443 different; one existing semantic C function is newly byte-exact.
The active 80% target is **4,409/5,511**, requiring **341 more**. This is
progress toward that goal, not completion.

## Existing source and interface

`Gfx *func_1510D8C0(Gfx *cursor, s32 key)` remains in
`conker/src/game/generated_139FC0.c`. This pass does not replace a stub or
change the already-qualified source from [Note 970](970-game-queued-segment-writer-and-big-endian-alias-qualification-20261004.md).
The source still scans the queued 16-byte segment records, emits one required
and one optional F3DEX2 `gSPSegment` command for each matching key, reloads the
live queue count after matching writes, preserves big-endian alias ordering,
and returns the advanced display-list cursor.

The retail slot is VA `0x1510D8C0`, ROM `0x13AD70`, 176 bytes/44 words and
frameless. Fresh IDO `-O2 -g3` emits a 40-word body in that slot; retail has a
41-word execution body. The complete image has one aligned JAL at ROM
`0x140F84` and no aligned literal function pointer.

## Guarded compiler match

The semantic source differs from retail at 38 word positions. Thirty-eight
checked expected-word guards restore retail's register roles, branch layout,
command-store schedule, queue-count reload and return schedule without changing
the source contract. They also preserve all six production relocation sites:

- `0x04`/`0x08`: HI16/LO16 for `D_800D9ED0`;
- `0x0C`/`0x10`: HI16/LO16 for `D_800D9ED8`;
- `0x84`/`0x88`: the late HI16/LO16 reload of `D_800D9ED0`.

No instruction is inserted outside the existing 44-word slot. The guarded
slot is exactly the retail slot, including its 41-word reachable body and three
trailing words.

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler object | `3986629e75f287d39f4c2a364a01d3bbe5af41932cb1ed8b8f9d52bfd0c29ccd` |
| Raw linked 44-word slot | `f3a227545fc8d35dd017430e12f6fd1da0512c5746e400423358eee3a9566feb` |
| Retail/guarded 44-word slot | `d4909fd2c5d0fa9df7bc1118c01ae806110cd3e919d69f1799daa6286337bd70` |
| Relocation-normalized retail template | `23e63d547626daa4d1112b89e5fe932f77a9d6579e16dd890c0c1a151c0ff4df` |

## Semantic and structural qualification

The retained bounded big-endian oracle and native SDK fixture were rerun in
both raw and installed states. The combined reset/append/writer/color module
completes 1,710 paired executions: 913 writer pairs, 787 palette-color emitter
pairs, nine append pairs and one reset pair. Coverage includes all 40 raw writer
words, all 41 retail writer words, every segment byte, signed/high-bit and
sparse keys, optional commands, live count reloads, empty queues, full cursor
values, and mapped queue/output aliases. Three invalid-index prefix cases and
262,144 native color-emitter cases also pass. This is a bounded low-word
big-endian and native command-model qualification, not hardware, RSP/RDP or
natural rendering acceptance.

The permanent guarded-match suite additionally proves:

- all 38 guards are present, exact, relocation-aware and stale-input checked;
- the existing semantic source and the sole retail caller remain intact;
- the padded owner is exact and all six relocation bindings survive;
- the complete 6,051-function image changes only `func_1510D8C0`, keeps every
  canonical address fixed and uses zero strict-image exclusions;
- protected Game data remains exactly 189,088 bytes across 720 owners with zero
  different bytes, SHA256
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

All 16 semantic tests and all three guarded-match/image tests pass after
installation under WSL.

## Production result

The actual generated-owner recipe produces SHA256
`f6479404609b3524685973edab6063d618fef0556866e3443ec1abdec13e522c`.
The independently predicted and production-linked ELFs are byte-identical at
SHA256
`f930a85c4640fb0f36cac1750284d15863164fd5d4140010a99dd94a9f6ceb04`.
The linker map remains unchanged at SHA256
`4ceeb40962070eb01cdc286937fdd209862def2bee87dbe33b6f8b7bd6912b38`.

`make all -j2` recompiles every owner consuming the shared guard manifest and
links successfully. Its final retail-ROM SHA-1 target remains expectedly
unsatisfied because the wider decomp image is not yet byte-identical; the
qualified owner, linked ELF, complete-image closure and protected-data checks
all pass independently.

The qualification tools were committed first at `316776a`. The retained stage
is `conker/build/game-queued-segment-writer-1510D8C0-match/`; it contains frozen
inputs, proposed guards, the exact owner, expected whole image and closure
receipt. The source was already counted as converted C, so converted totals do
not change. The root README changes only aggregate byte-exact rows. No Claude
call was needed.

Graphify already contains `func_1510D8C0` at
`conker/src/game/generated_139FC0.c:L428`. The required incremental update saw
24,063 nodes versus the retained 58,384 and failed closed without `--force`,
preserving 31,816 nodes from 3,754 still-existing files outside the reduced
scan corpus. The retained graph SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`;
`func_1510D8C0` and the older exact-C node `func_15007778` both remain present.
This is retention evidence, not a full-corpus refresh claim.

## Next step

Continue the ordinary Game queue from the fresh non-exact ranking. Keep
handwritten custom-ABI `func_150A76F0` in its separate assembly workstream and
keep every candidate private until the same ABI, semantic, owner, actual-Make,
whole-image, protected-data, recount, documentation and graph-retention gates
pass.
