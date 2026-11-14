# Game actor coordinate packet match

Date: 2026-11-13. `func_150F1B48` replaces the zero-return placeholder in
`conker/src/game/generated_11C2B0.c`. The retail body occupies 90 words at
`0x150F1B48..0x150F1CB0`, ROM `0x11EFF8..0x11F160`.

The routine updates a shared signed coordinate using the game tick scaled by
546, clamps against the original floating limits, and emits six signed
halfword (x, y) pairs. It returns the output cursor advanced by 24 bytes.
The output can overlap the shared coordinate; the recovered C snapshots each
coordinate at the point needed to preserve the retail write sequence. Its
32-bit arithmetic wraps before the floating comparison. The slot index is
unchecked in the original and is not newly validated here.

The existing caller declaration has been corrected to return the output
pointer. The two linker symbols used as indexed storage now have consistent
array declarations; the existing actor consumer and its complete object were
checked to remain unchanged. The recovered compiler output occupies 87 words;
23 relocation-aware guards restore retail scheduling and three instructions
folded by the compiler, producing all 90 retail words. This is a guarded match.

Tools commit `69c0cf6` contains the reproducible qualification:

```sh
python3 -m unittest tools.tests.test_game_actor_coordinate_packet_150f1b48_match -v
```

The guest model and native32 O0/O2/O3 tests each cover 2,304 cases, including
overlap and boundary values. Seven deliberately incorrect native variants are
rejected. The original caller window has 216 bounded cases, and an aligned ROM
scan identifies its direct call at `0x15034114`. The checks also cover 92 guest
fault prefixes, eight GNU links across four address layouts, both padders and
92 rejected stale guard preimages. These tests are bounded evidence and do not
establish native C fault ordering or physical hardware behavior. Both mounted
and independent sibling suites passed before and after installation; project tools
checks passed, and the sibling's pre-existing dirty state was preserved.

The production Make build and independent complete-image audit account for
278 changed bytes with zero exclusions and no symbol-ordering groups. Only
this function changes among 6,051; every function address and all 189,088
protected Game-data bytes remain fixed. Of 698 linked objects, only the target
owner and debugger object changed. The debugger's symbol-table difference is
exactly the undefined `D_800CC298` symbol changing from size four to zero,
plus a changed debug section; its final linked image is unchanged. All 84
functions and all sections of the existing actor consumer, and all 10 caller
functions and caller sections, are unchanged. The conversion CSV and prior
guard entries are unchanged. The scoped Graphify refresh retained all 60,074
prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,779 / 4,843 (78.03%)**, total
**4,452 / 5,516 (80.71%)**, zero address drift. **96** more Game matches are
needed for 80% at the current denominator.
