# 2000 - Fixed-point translation matrix recovered as guarded C

Verified 2026-11-02. Production **4,067/5,511 (73.80%)**; Game
**3,394/4,838 (70.15%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,444 different; one existing non-matching C function is newly
byte-exact. The
active 80% target is **4,409/5,511**, requiring **342 more**. This is progress
toward that goal, not completion.

## Interface and recovered behavior

`void func_150A7D00(volatile s16 *matrix, f32 x, f32 y, f32 z)` replaces the
non-matching `bzero`-based implementation in `conker/src/game_D51B0.c` with an
explicit eight-store implementation. Original `D51B0.s`:
VA150A7D00..150A7DA0, ROMD51B0, 160 bytes, 40 words and no stack frame.

The routine is the game's local fixed-point translation-matrix constructor.
It converts X, Y and Z to signed 16.16 values, clears the complete 64-byte N64
matrix through eight 64-bit stores, writes the homogeneous diagonal one, and
publishes each translation's integer and fractional halves in the final row.
The recovered behavior agrees with the retained libultra `guTranslate` C and
handwritten assembly implementations without replacing retail's local symbol.

The complete retail image contains five aligned JALs at ROM offsets `0xC0F88`,
`0x13B614`, `0x15A1D4`, `0x15A4D4` and `0x21BE00`, with no aligned literal
function pointer. The function is a leaf and has no relocation bindings.

## Guarded compiler match

IDO's retail `-O2 -g3 -mips3` profile emits the required eight `sd` zero
stores and a complete 160-byte function. One word emits directly; 39 checked
expected-word guards normalize retail's handwritten register allocation and
scheduling. No word is inserted or omitted and every guard has empty
relocation metadata.

Raw compiler payload SHA256:
`64d82d1b5d5f3dd442ca6d724034018ac8a0be6de25f73507801e5d3db7fe566`.
Retail slot SHA256:
`39eb5fa689bd570e196daf99f4d7df5fa78711afad16195dbca92f1df5f026c1`.

## Fresh qualification

- Guest execution covers 21 independent X/Y/Z tuples at both aligned matrix
  phases against the raw compiler body and guarded retail body. All 40 raw
  words and all 37 reachable retail words execute, all 64 output bytes agree
  with an independent signed-16.16 model, and callee-saved registers remain
  intact.
- Native 32-bit O0/O2/O3 execution covers negative, signed-zero, fractional,
  ordinary and boundary values. Four source mutations are effective at every
  optimization profile: wrong scale factor, wrong X integer slot, wrong Z
  fractional slot and an uncleared tail.
- The permanent census proves the five JAL sites and zero aligned literal
  pointers. Retained libultra `guTranslate` C and assembly provide independent
  SDK provenance for the matrix layout and conversion.
- Guard-staleness controls reject changes at the entry, zero-store region,
  translation publication and final return.

All five permanent tests pass after installation under WSL.

## Owner, image and production result

The real generated-owner recipe uses `-mips3`, applies all 39 checked guards
and produces the exact 160-byte retail slot. Protected Game data remains
exactly 189,088 bytes across 720 owners with zero different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The strict complete-image predictor has zero exclusions. Installing the
canonical body removes the now-unreferenced 172-byte private overflow copy
`__retail_overflow_func_150A7D00` at `0x15F005E4`; the unreferenced private
`__retail_overflow_func_15125490` moves from `0x15F00690` to `0x15F005E4`.
No canonical body or trampoline is retargeted. `.game_overflow` shrinks from
`0x6F8` to `0x64C`, the ROM cursor moves from `0x25ACE0` to `0x25AC30`, and the
expected symbol count moves from 6,052 to 6,051.

The installed production artifacts reproduce the independent prediction:

- owner object SHA256:
  `e525703060cc9ae7550762a9f76d14b00a8d0480d1c42c0a868c9002a1012039`;
- linked ELF SHA256:
  `9073a15c16751d7488d87c18d53fa5971fcce573dcfaf26f805fb4890165ef5a`;
- linker-map SHA256:
  `4ceeb40962070eb01cdc286937fdd209862def2bee87dbe33b6f8b7bd6912b38`.

`make all -j2` recompiles every owner consuming the shared guard manifest and
links successfully. Its final retail-ROM SHA-1 target remains expectedly
unsatisfied because the wider decomp image is not yet byte-identical; the
qualified owner, linked ELF, complete closure and protected-data checks all
pass independently.

The qualification tools were committed first at `edc5320`. The retained stage
is `conker/build/game-fixed-translation-matrix-150A7D00-match/`; it contains
frozen inputs, compiler diagnostics, proposed source/profile/guards, the exact
padded owner, expected complete image, guest/native artifacts and permanent
test receipts. The root README changes only aggregate rows. No Claude call or
gameplay claim was needed.

Graphify's retained graph already contains `func_150A7D00` at
`conker/src/game_D51B0.c:L7`. The required incremental update saw only 24,056
nodes versus the retained 58,384 and failed closed without `--force`, preserving
31,816 nodes from 3,754 still-existing files outside the reduced scan corpus.
The retained graph remains 58,384 nodes and 120,179 links; the older exact-C
node `func_15007778` remains present. This is retention evidence, not a
full-corpus refresh claim.

## Next step

Continue the ordinary Game queue from the freshly recounted non-exact ranking.
Keep handwritten custom-ABI `func_150A76F0` in its separate assembly workstream
and keep every candidate private until the same ABI, semantic, owner,
actual-Make, whole-image, recount, documentation and graph-retention gates
pass.
