# Game Secondary Timed Callback Record Match

Date: 2026-10-02

## Recovery

`func_15158224` at `0x15158224..0x151582C8` replaces its zero-return
placeholder with the complete 41-word / 164-byte record lifecycle body in
`conker/src/game/generated_185560.c`.

Record flag bit zero at offset `0x10` enables countdown. The signed halfword
at `0x14` is decremented by `D_800BE9E4`, stored back, and reloaded before
testing its sign. Negative results complete the record; zero remains active.
Otherwise the signed byte at `0x12` selects the callback from `D_8008AE00`.
The `-1` sentinel skips invocation. A zero callback result completes the
record, while every nonzero result leaves it active. Completed records are
released once through `func_1516972C` using the original record pointer.

This has the same recovered lifecycle shape as `func_1513B798` in Note 728,
but the selector is at `0x12`, not `0x11`, and the callback table differs.
The existing old-style callback declaration preserves the indirect-call
shape without inventing an argument signature from the table address alone.
No defensive index clamp or early timer check changes retail behavior.

## Matching

The existing IDO `-O2 -g3 -mips2 -o32` profile emits 39 of 41 words directly,
including the 32-byte frame, halfword store/reload, callback dispatch,
record-pointer home, branch delay slots, release path, and return.

A byte-typed completion local initially produces six differences: different
register lifetime plus its spill. The final `s32` completion local recovers
the full register and branch schedule, leaving only the two known spill-width
differences. Strict expected-word guards normalize those two words:

| Offset | IDO word | Retail word |
| --- | --- | --- |
| `0x64` | `AFA3001C` | `A3A3001B` |
| `0x74` | `8FA3001C` | `93A3001B` |

The completion value is zero or one; both guarded operations use the same
retail byte slot at `sp+0x1B`. No insertion, omission, relocation rewrite,
source inlining trick, or compiler override is required. This is the same
bounded normalization already used for the preceding lifecycle recovery.

## Source Behavior Tests

`tools/tests/test_game_timed_callback_record.py` extracts the actual source
body and compiles it as host C with mock callback and release functions.
Eight tests cover:

- Disabled countdown, other flag bits, preserved record bytes, and a negative
  nonzero callback result.
- The signed `-1` callback sentinel.
- Timer expiry suppressing callback dispatch and releasing exactly once.
- A stored timer of zero remaining active and visible to the callback.
- Callback failure releasing exactly once.
- Both signed-halfword wrap directions, checked after the narrow store.
- Callback mutation preserving the original release argument.
- Selector offset `0x12`, independently of the neighboring byte at `0x11`.

All 39 tool tests pass. Host mocks establish source behavior, not fresh guest
gameplay or callback-table runtime qualification. The host compiler's narrow
signed conversion agrees with these tested guest wrap cases; this does not
claim every possible signed 32-bit delta avoids C arithmetic overflow.

## Verification

`make -C conker NON_MATCHING=1 all match-progress -j4` passes. Independent
linked extraction matches all 164 bytes against pristine span
`0x1856D4..0x185778`. The following `func_151582C8` remains at `0x151582C8`.
The routine SHA-256 is:

```text
8eda5947615a80fb1476d098b0f7171c024dd117d5df6c43267d33fb7c8996f5
```

Both entire Init sections retain their exact baseline hashes: 164,048 code
bytes and 17,376 initialized-data bytes. Fresh matcher results are total
3,243 / 5,461 exact C (59.38%), Game 2,570 / 4,788 (53.68%), Init
492 / 492 exact, and Debugger 181 / 181 exact. Address drift is zero;
2,218 Game C rows remain different. C conversion counts and byte totals
do not increase because the previous placeholder was already counted as C.

The guard CSV has 10,390 rows and zero duplicate filename/function/offset keys.
Project tool and whitespace checks pass. Existing pointer-type warnings in
the generated source are outside this recovery.

The sibling host port, real saves, and frozen Release artifacts remain
untouched. No compressed-ROM build or gameplay run is claimed.

## Resume

The fresh matcher confirms the next ordinary Game candidate is
`func_1515FFEC` in generated slice `18D250`, 41 words with 35 real differences. Keep
`func_150F631C` in its near-match cleanup queue and `func_150A76F0` in its
handwritten/register-contract workstream. The two custom Init experiments
remain deferred, with all original assembly ownership preserved.
