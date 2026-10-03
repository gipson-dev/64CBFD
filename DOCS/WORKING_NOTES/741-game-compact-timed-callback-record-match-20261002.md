# Game Compact Timed Callback Record Match

Date: 2026-10-02

## Recovery

`func_1515FFEC` at `0x1515FFEC..0x15160090` replaces its zero-return
placeholder with the complete 41-word / 164-byte lifecycle body in
`conker/src/game/generated_18D250.c`.

This is another timed callback record, with a compact layout distinct from
the preceding recovery:

| Field | This record | Note 740 record |
| --- | --- | --- |
| Countdown flag byte | `0x0E` | `0x10` |
| Signed callback selector | `0x0F` | `0x12` |
| Signed-halfword timer | `0x12` | `0x14` |
| Callback table | `D_8008B0D0` | `D_8008AE00` |

Flag bit zero enables subtraction of `D_800BE9E4` from the timer. Retail
stores the halfword and reloads it before checking its sign; a negative
stored value completes the record, while zero remains active. Otherwise
the signed selector chooses the callback, except for the `-1` sentinel.
Zero callback results complete the record; nonzero results retain it.
Completed records are released once through `func_1516972C` with the original
record pointer.

The neighboring `D_8008B0E4` three-argument dispatcher is not repurposed as
this lifecycle table. Local declarations preserve the separate symbol and
existing old-style callback call shape without inventing a new argument ABI.
No defensive selector clamp or altered timer boundary changes retail behavior.

## Compiler Match

The existing IDO `-O2 -g3 -mips2 -o32` profile emits the entire frame,
timer store/reload, selector/table lookup, indirect call, argument lifetime,
branches, delay slots, release path, and return. The focused object's only
two non-relocation differences are the completion flag spill/reload words:

| Offset | IDO word | Retail word |
| --- | --- | --- |
| `0x64` | `AFA3001C` | `A3A3001B` |
| `0x74` | `8FA3001C` | `93A3001B` |

Two strict expected-word guards use retail's byte slot at `sp+0x1B` for the
zero/one completion flag. This is the same bounded normalization already
used in Notes 728 and 740. Thirty-nine words emit directly from C. No new
profile, insertion, omission, relocation replacement, or rodata anchor is
required. The CSV contains 10,392 rows and zero duplicate patch keys.

## Tests

The existing source-extraction lifecycle tests are parameterized by source
owner, function name, callback table, and record offsets. A second concrete
test class compiles this actual body rather than duplicating the preceding
fixture or rewriting its record offsets. Both variants run the same eight
behavior tests independently, preserving the earlier regression coverage.

The tests cover countdown gating by bit zero, preserved record bytes when
disabled, the signed sentinel, expiry suppressing dispatch, the zero boundary,
zero and negative/nonzero callback results, both signed-halfword wrap
directions, callback mutation, original release-pointer preservation, and
selector independence from a neighboring byte. All 47 tool tests pass.

Host callback mocks establish source behavior, not guest gameplay or physical
callback-table runtime qualification. Narrow signed conversion in these tested
cases agrees with retail; no claim is made for arbitrary deltas that overflow
signed 32-bit C subtraction.

## Verification

`make -C conker NON_MATCHING=1 all match-progress -j4` passes. Independent
linked extraction matches all 164 bytes against pristine span
`0x18D49C..0x18D540`. The following dispatcher `func_15160090` remains at
`0x15160090`. The routine SHA-256 is:

```text
bf6188404c64553ae58919c0e922108163d8e11fb087342be13d4e28ed7cef9e
```

Both complete Init sections retain their exact baseline hashes: 164,048 code
bytes and 17,376 initialized-data bytes. Fresh results are total
3,244 / 5,461 exact C (59.40%), Game 2,571 / 4,788 (53.70%), Init
492 / 492 exact, and Debugger 181 / 181 exact. Address drift is zero;
2,217 Game C rows remain different. C conversion counts and byte totals
remain unchanged because the former placeholder was already counted as C.

Project tool and whitespace checks pass. Only the scoped source, two guards,
tests, and progress documentation are changed. The sibling host port, real
saves, and frozen Release artifacts remain untouched; no compressed-ROM build
or gameplay run is claimed.

## Resume

The fresh matcher confirms the next ordinary Game candidate is
`func_15163504` in `game_18D770.c`, 41 words with 35 real differences.
Keep `func_150F631C` in its
near-match cleanup queue and `func_150A76F0` in its handwritten/register-contract
workstream. Init's custom MMIO and bitmap experiments remain deferred.
