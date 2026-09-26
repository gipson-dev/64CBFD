# Game argument-load schedule match - 2026-09-25

## Result

All 41 words of `func_150771F0` now match retail across
`0x150771F0..0x15077294`. The fresh linked matcher reports
`2571 / 5484 (46.88%)` overall and `2003 / 4795 (41.77%)` game. One init
function remains blocked by address drift; 2,912 total and 2,792 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Source and schedule evidence

The function dispatches one of three actor operations using four byte globals.
Its second branch already matched retail word-for-word. All nine differences
were in the first five-argument call to `func_1506160C`.

Moving the selector expression directly into the call made IDO prepare the
third and fourth arguments earlier. Explicit local assignment and equivalent
inverted-condition variants did not recover retail's two-arm selector shape.
Nine expected-word guards complete the schedule: retail hoists the
`D_800D1890` high half, prepares and loads `D_800D1891`, chooses `a1` with two
explicit assignments, and delays loading `D_800D154C` until immediately
before the call. Eight rows explicitly declare both expected and replacement
relocations, so compiler or symbol-lifetime drift fails the build.

## Verification

The current checkout passed:

```sh
make build/src/game_A28B0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 164-byte linked ELF span at file
offset `0xB71F0` and pristine extracted retail span at
`conker/conker.us.bin+0xA46A0` produced SHA-256
`735443235523748393545106b44ca5886db042803279aa7dc842704ff00d72f8`
for both. The retail-word patch table has 582 rows, no duplicate
filename/function/offset keys, and exactly nine rows for this function.

The `64CBFDOGL` sibling has no hand-maintained implementation of
`func_150771F0`; only generated or backup symbol references are present. This
IDO scheduling normalization does not transfer to host source. Its dirty tree
was left untouched, and frozen Release was not built or launched.

## Next boundary

Continue with 10-word `func_15080200`, now the first game row with nine real
differences. Compare its C body, compact object, retail words, and relocations
before editing.
