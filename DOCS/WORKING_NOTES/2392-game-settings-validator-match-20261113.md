# Game settings validator match

Date: 2026-11-13. `func_151DD9E4` replaces a zero-return placeholder in
`conker/src/game/generated_20AE20.c`. Its 108-word retail body occupies
`0x151DD9E4..0x151DDB94`, ROM `0x20AE94..0x20B044`.

The validator checks 23 signed setting bytes against their signed minimum and
maximum tables. Values outside the inclusive range are replaced with the
corresponding default; values in range are retained. Retail leaves 23, the
completed loop index, in its return register, and the recovered C returns that
value. The first three bytes and the remaining five groups of four retain
retail's compiled access sequence.

The source emits 109 words. Two relocation guards bind the cursor to retail's
`D_800E0BE3` label; one omission guard removes an unnecessary load of 23 after
the loop has already placed 23 in the return register. The loop starts at 3,
increments by four, and exits only at 23. An initial single-guard screen
matched at retail addresses but failed when the settings base crossed a signed
low-half address boundary. The restored high/low relocation pair fixes that
layout and matches the original in four separately linked layouts. No other
instruction changes.

Tools commit `386158a` supplies the reproducible checks:

```sh
python3 -m unittest tools.tests.test_game_settings_validator_151dd9e4_match -v
```

The guest model checks 11,776 settings cases for each of retail, unguarded C
and both guarded padding streams. Each byte value is exercised at each setting
position with retail minimum/maximum bytes and a synthetic signed-bound set.
Native32 tests run 11,776 cases at each of O0, O2 and O3 with trapping UBSan;
five deliberately incorrect variants fail. Additional checks cover 389
retail/guarded guest memory-access fault prefixes, eight GNU links across four
address layouts and 12 stale word or relocation rejections across both
padders. The fault tests concern the emitted guest sequence; they are not a
claim about native C fault order.

An aligned scan of the Game ROM finds direct calls at `0x1500752C` and
`0x151E23EC`. The two original call windows pass 512 combined cases against
the original and guarded bodies, including the pre-call delay-slot setting
writes and the return value. These windows do not establish full parent or
gameplay execution. The mounted tools suite and a sibling checkout overlay
passed all nine checks before and after installation; `make tools-check`
passed, and the sibling's pre-existing dirty paths were preserved.

The production Make build and independent complete-image audit account for
404 changed bytes with zero exclusions, including a checked symbol-table
ordering change. Only this function changes among 6,051; every function
address and all 189,088 protected Game-data bytes remain fixed. Only the
`generated_20AE20.c.o` owner changed among 698 fingerprinted linked objects;
the conversion CSV and all prior guards are unchanged. The scoped Graphify
refresh retained all 60,069 prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,777 / 4,843 (77.99%)**, total
**4,450 / 5,516 (80.67%)**, zero address drift. **98** more Game matches are
needed for 80% at the current denominator.
