# Game menu-settings loader match

Date: 2026-11-13. `func_151E22BC` replaces the zero-return placeholder in
`conker/src/game/generated_20AE20.c`. Its 82-word retail body occupies
`0x151E22BC..0x151E2404`, ROM `0x20F76C..0x20F8B4`.

The function selects a ten-byte record through the current menu index, clamps
its fourth byte, corrects a nonpositive signed value in its second byte, and
copies settings into `D_800E0BE0`. The selected record index controls several
additional byte copies and settings changes. The routine finally calls
`func_151DD9E4` and returns with its result register unchanged. That callee
remains a separate placeholder; the checks here model it and do not establish
its real behavior or semantic return type.
The bounded caller window is in `func_151E0424`, from `0x151E04E0` to
`0x151E09C0`.

An initial C shape failed when the record overlapped the destination: for
indices 8 and 9 retail reads record byte 6 before two settings writes. The
recovered source snapshots that byte at the same semantic point. Its otherwise
redundant signed comparison also retains the retail clamp control flow.

IDO emits an 82-word body. Fifty-five expected-word and relocation guards
normalize register roles, two moved case blocks, two distinct settings writes,
branch offsets, and eleven byte-load sign extensions whose results are used
only by byte stores. The guards also preserve a constant-equivalent
instruction; no words are inserted or omitted. Static checks verify the 11
load/store pairs in both streams and that their temporary registers have no
intervening use or write. The resulting instructions match all 82 retail
words; the unguarded C does not directly emit that stream.

Adding this switch places its ten-entry compiler table immediately before the
neighbor's table. The existing retail tables are likewise adjacent at
`0x800AB994` and `0x800AB9BC`. The owner Makefile profile now names the earlier
table as its `.rodata` base. The neighbor's compiler addend moves by 40 bytes,
so its resolved table address and linked instructions stay unchanged. The
original retail data is retained; no compiled table replaces it.

Tools commit `ba437f5` supplies the reproducible checks:

```sh
python3 -m unittest tools.tests.test_game_menu_load_151e22bc_match -v
```

The bounded guest screen exercises 576 signed-index, clamp and settings cases.
A separate 1,036-case overlap sweep checks nearby record/settings aliases; the
selected and guarded streams agree with retail and the independent model. A
deliberately broken version that delays the record-byte snapshot fails 16 of
those cases. The native32 test checks 1,810 cases at each of O0, O2 and O3
with trapping UBSan and rejects three intentionally incorrect variants. Its
shared-backing alias fixture uses a linker alias. The suite also covers the
36-case caller window, 83 retail/guarded guest memory-access fault prefixes,
eight links across four address layouts, and 220 stale word/relocation guard
rejections across both padders. The caller and fault checks are bounded guest
models, not complete runtime or portable C fault-order qualification.

The focused suite passed in mounted tools before and after installation. An
isolated sibling overlay uses that checkout with mounted fallback modules; it
also passed before and after installation. `make tools-check` passed, and the
sibling's 2,434 pre-existing dirty paths were preserved. A first installed run
exposed a test fixture applying new guards to the frozen old object; the
fixture now uses the corresponding old and new guard sets, and the corrected
suite passed.

A private readability-only source layout changes the order of two independent
stores in IDO's output. It is not installed: adopting that layout would require
updating the guard preimages and repeating the relevant qualification.

The production Make build and independent whole-image audit account for 272
changed bytes with zero exclusions, including an accounted-for symbol-table
ordering change. Only this function changes among 6,051; every function
address and all 189,088 protected Game-data bytes remain fixed. Only
`generated_20AE20.c.o` changed among 698 fingerprinted linked objects. The
conversion CSV and prior guards are unchanged; the Makefile difference is the
single table-base selection. The scoped Graphify refresh retained all 60,064
prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,775 / 4,843 (77.95%)**, total
**4,448 / 5,516 (80.64%)**, zero address drift. **100** more Game matches are
needed for 80% at the current denominator.
