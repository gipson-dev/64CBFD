# Game texture-tile display-list builder match

Date: 2026-11-13. `func_151ED29C` replaces the zero-return placeholder in
`conker/src/game/generated_215960.c`. The 101-word retail body occupies
`0x151ED29C..0x151ED430`, ROM `0x21A74C..0x21A8E0`.

The routine reads the texture descriptor's unsigned width, height, format and
size fields, writes the byte footprint through its third argument, and emits a
pipe sync, load-tile setup, render-tile setup and tile-size command. It returns
the display-list cursor after four commands. The arithmetic preserves the
retail 32-bit product wrap and variable shift behavior. The size lookup uses
the four adjacent retail byte tables; native C qualification covers the four
defined SDK size indices. The guest test also exercises all 256 byte indices
against the mapped retail data, without claiming portable C behavior beyond
the declared table objects.

An early candidate read the format after writing the sync command. When the
command buffer overlapped the descriptor at offset four, that write could
change the format first; the candidate differed from retail. The recovered C
snapshots the format at the retail semantic point before the write. Its GNU
may-alias annotation preserves this access relationship under the native
compiler; IDO sees the ordinary structure declaration.

The candidate emits 102 words versus retail's 101. Eighty-eight expected-word
and relocation guards normalize register allocation and instruction schedule;
one omits an explicit shift mask already applied by MIPS variable shifts. A
one-to-one structural alignment accounts for all 101 retained instructions;
1,620 bounded guest cases also compare their individual result values, memory
accesses and branch decisions, including overlapping input/output storage.
This is bounded evidence, not a formal proof of every possible execution.

Tools commit `756894b` supplies reproducible checks:

```sh
python3 -m unittest tools.tests.test_game_texture_tile_151ed29c_match -v
```

The independent guest model checks 7,200 ordinary cases and 10,240 cases
covering all 256 size-byte values. A separate 3,024-case guest sweep covers
overlapping output and descriptor storage. Native32 O0/O2/O3 tests each
cover 4,096 cases, with and without strict aliasing, trapping UBSan, and six
effective incorrect variants. Other checks cover 96 retail/guarded guest
memory-fault prefixes, eight GNU links across four address layouts, both
padders and 352 stale word/relocation guard rejections. Fault-prefix evidence
applies to the emitted guest stream; it does not establish native C fault order.

An aligned Game-ROM scan identifies the direct call at `0x151ED478` in
`func_151ED430`. Its original bounded call window passes 288 cases per stream,
including the stack output and delay-slot write; the complete drawing helper
remains a placeholder and is not qualified by this window. The mounted tools
suite and independent sibling overlay passed before and after installation;
`make tools-check` passed, and the sibling's pre-existing dirty work was preserved.

The production Make build and independent complete-image audit account for
416 changed bytes with zero exclusions, including four checked symbol-table
ordering groups. Only this function changes among 6,051; every function
address and all 189,088 protected Game-data bytes remain fixed. Only the
`generated_215960.c.o` owner changed among 698 fingerprinted linked objects;
the conversion CSV and all prior guards are unchanged. The scoped Graphify
refresh retained all 60,071 prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,778 / 4,843 (78.01%)**, total
**4,451 / 5,516 (80.69%)**, zero address drift. **97** more Game matches are
needed for 80% at the current denominator.
