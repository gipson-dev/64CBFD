# Game Mode Callback Dispatcher Direct Match - 2026-10-12

## Scope And Queue

Continue the full Game matching goal from consumer `13de019e` / tools
`4dbdcbef` and [Note 1313](1313-game-text-measurer-repeated-predicate-and-font-load-fault-boundary-20261012.md).
Both active repositories were clean. Additional ignored text union/join/type
controls did not solve the font-pointer boundary. The ordinary direct exit
loses the required reset/save; no fitting credit or production change follows.
Keep `func_150428D4` open at 218/0x80/114 and A access cut27, not marked done.

Rotate the remaining Game queue to bank actual matching work. Its first entry,
`func_150A76F0`, is explicitly handwritten: register-only inputs T4/T9/S6/S7,
F8 result and return through V0. Do not invent an ordinary C ABI or promote its
zero-return placeholder. The next translator `func_15142314` remains 49/34;
ignored explicit selected-pointer returns give no scheduling improvement and
are not installed. No historical matching boundary is silently called complete.

This checkpoint replaces the untouched callback placeholder in
[game_35D20.c](../../conker/src/game_35D20.c). Target `func_15008930`, VA
0x15008930..0x150089D0 / ROM 0x35DE0..0x35E80, is a 40-word / 160-byte
retail slot: 38 real instructions plus two existing zero alignment words.
The original function end is 0x150089C8. Source emits directly at unchanged
O2/g3 / MIPS2 with frame0x30, no diagnostics, pool, guards or profile change.
All 160 linked slot bytes now equal retail. The peer `func_15008870` stays put.

## Recovered Contract

- Input is the complete signed32 mode, not a narrowed byte. Exact mode1 selects
  the callback slot at D_80082BD0; exact mode2 selects D_80082BD4. Other modes
  do not read a callback slot or an uninitialized selected pointer.
- Preserve the guarded counted do/while and live four-byte callback-slot read.
  Valid modes perform one indirect callback with no explicit argument setup;
  do not cache a handler in production state or add a null-handler fallback.
- After the callback, or immediately on invalid modes, store -1 to
  D_800DD1B0. Callback changes to that latch are overwritten by the final store.
- Preserve S0/S1/S2 and RA, the original selected-pointer home at SP+0x2C,
  counter/cursor lifetime and all delay slots. The void/signed32 source ABI
  matches the routine's observed call setup; the sole archived direct caller
  in `func_15007B3C` passes A0 and does not consume a return value.

```sh
python3 -m tools.experiments.game_mode_callback_dispatch_candidates
python3 -m unittest tools.tests.test_game_mode_callback_dispatch_match -v
```

## Qualification

Seven pre-install tests pass in 9.495 seconds, plus the focused final image-gate
rerun in 1.361 seconds. Seven post-install tests pass in 9.779 seconds, no skips.

- 19,152 guest cases cover all byte modes plus ten full-word edge patterns,
  both stack phases, three live registry arrangements, four initial latch values
  and three callback mutation modes. Complete memory/events/GPRs/FPRs/calls
  agree with the original instructions; public output is independently checked.
  Opaque providers modify the latch/registry and clobber caller-saved GPRs.
- Missing selected-slot and latch bytes fail closed. Invalid modes complete
  with both callback slots unmapped. All 306 own-routine R/W cut pairs match,
  with fired gates and terminal no-fault controls. Provider memory accesses are
  excluded from those instruction counts; actual callback code, PC/EPC/FCSR,
  renderer/gameplay behavior and arbitrary invalid function pointers are not
  claimed by these bounded provider tests.
- Native32 O2/O0 passes 9,576 cases per profile, 19,152 comparisons, checking
  four-byte integers/object pointers/function pointers, callback choice/count,
  entry latch, final latch and fences. Two fresh compiled negatives expose a
  wrong latch and a skipped callback. Invalid mode with null registry values
  completes without calling them. The unguarded for-control is not qualified:
  evaluating its uninitialized selected pointer on invalid modes is not valid C.
- Production-preprocessed copied owner has two functions and no warnings.
  The one neighbor's body is unchanged; relative target relocations match the
  isolated object and all pool-family union remains unchanged/empty. Both
  actual padders emit identical objects, a 152-byte function and the original
  eight-byte alignment tail. No arbitrary padding instruction is inserted.
- Independently assemble/link the complete original and C at three code/data
  layouts, including positive/negative LO16 and signed-low carry boundaries.
  Every rebased body matches its independently linked original, including the
  original tails. The production profile and six data relocations are retained.

Initial qualification failures were test setup errors: the selected base oracle
did not support JALR, raw owner relocations were compared with linked words,
the data report was unpacked as a tuple, and the function size was confused
with its alignment-inclusive slot. Reuse the existing TriangleOracle JALR
engine, compare raw objects/relocations, consume the report dictionary and
verify function152 plus tail8. No shared oracle or production defect is claimed.

## Build And Literal Image Audit

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds with only the
known duplicate generated_12D630 recipe warning; the owner adds no warning.
The current ELF equals the saved complete before-image byte for byte except
the declared 160-byte target slot and its exact symbol-size field, 12 -> 152.
All other code, addresses, names, metadata, sections and bytes are unchanged;
retail slot extent remains160. All 189,088 Game-data bytes / 720 owners are
exact. Guard history, progress.csv, retail layout and Makefile stay byte-identical.

ELF SHA-256 is now `c3ca8a2463fdb0fb891124f82274d6287504743a1f20ebef47fdf0fb84b896d6`;
source SHA-256 is `e280716f2b287c82df0182745a687784b88ed8720b619c9af84be3c466d1c65d`.
Fresh matching: Game 2,814 / 4,823 (58.35%), total 3,487 / 5,496 (63.45%),
2,009 different and zero drift. Converted functions/bytes are unchanged.
Root README receives only the two matching aggregate rows, no recovery narrative.

## Retained Text Fixture And Bank

The text-measurer tests pin the whole ELF to a known checkpoint. Advance only
their expected ELF hash after the dispatcher literal-image gate passes. Archive
the prior manifest/image in ignored `game-mode-callback-dispatch-test/
text-fixture-before-dispatcher/`; update the generated before-image/manifest,
leaving the other eight input hashes and all semantic/corruption checks intact.
The text source remains SHA802b4d27 and its linked slot remains the same
199-difference placeholder. No old snapshot is deleted or old evidence relabeled.

Fresh combined dispatcher/text-predicate regression: all fourteen tests pass
in 65.506 seconds, no skips, including the retained 53-word literal metrics
region and 710/768 named text access-cut states. Fresh immutable/corruption
tests05/06 pass in 2.560 seconds against the independently verified new image.
The shared test change is one known ELF hash, not a reduced comparison scope.

Tools `d3426e642f774aa5ea84d6e00b9d749a07551777` is committed first;
source, this note, five indexes, workflow, README aggregates and gitlink follow.
WSL consumer/mounted/older tools checks, Windows py_compile and whitespace
checks pass. Older HEAD `ddbdd16b` is preserved: two absent task files and one
fingerprint-checked shared fixture are synchronized/hash-checked. The other
100 fingerprints are unchanged; dirty378 becomes dirty380 / 103 task hashes.
No older commit/reset/stash/history duplication, unrelated reversal, extra
Claude call, OGL/Release/ROM/save/config/editor change or push. No host source
import is proposed for a byte-identical retail C match; host behavior was not
exercised or qualified by this decomp checkpoint.

Final bank requires fresh linked/immutable controls, resolved links, clean active
repositories and the fresh terminal Graphify Rebuilt receipt with advanced log
bytes/UTC and zero workers. Preserve existing graph/version/scan-size warnings.

Fresh post-documentation literal-image and text immutable/corruption controls
pass as three tests in 3.128 seconds. All 4,567 relative links across eight
checked documents resolve; repeat those controls after the final bank.

## Next

Keep the full Game goal active. Inspect `func_15015104` in `game_40490.c`,
52 words / frame0x58 / 37 current differences, next in the ordinary queue.
Its current semantic record construction still needs the original input-home
lifetime and helper/packet qualification. Retain the open text-measurer
218/114/cut27 checkpoint and translator scheduling boundary; neither is done.
Changing queue order is not a completion claim or a narrower Game objective.
