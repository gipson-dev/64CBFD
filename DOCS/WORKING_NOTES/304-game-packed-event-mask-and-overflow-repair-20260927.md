# Game packed event-mask and overflow repair - 2026-09-27

## Result

`func_1507488C` is byte-exact across all 26 words and 104 bytes at
`0x1507488C..0x150748F4`. The required full rebuild exposed stale overflow
output for `func_1506EE60`; that 19-word / 76-byte function is also restored
exactly at `0x1506EE60..0x1506EEAC`. Fresh totals are 2,808 / 5,469 (51.34%)
exact C functions overall and 2,236 / 4,791 (46.67%) in Game.

## Packed event-mask recovery

The packed word at `D_800D1580` supplies four fields. Bits `16..23` select a
word from the active actor's table at offset `0x2E4`, bits `8..15` provide the
mask tested against that word, bit zero is the initial gate, and the signed top
byte is an increment. A nonzero table/mask intersection inverts the gate; a
final active gate adds the signed increment to actor byte `0x138`.

Explicit byte temporaries and a retained actor pointer recover the 26-word
control-flow extent. IDO still assigns equivalent registers differently, so 22
guarded rows restore retail's register schedule and branch-delay lifetime. The
four global-address words carry explicit expected and replacement relocations.

## Full-rebuild overflow repair

Changing the shared guard table correctly forced a broad object rebuild. That
revealed that the previously linked exact `func_1506EE60` came from a stale
object: current source emitted 20 words for a 19-word slot, leaving an overflow
trampoline in a clean rebuild. The source now retains `D_800D1580` once and
forwards its full low 16 bits. IDO still repeats one low-half normalization, so
the established guarded-overflow pattern replaces the verified trampoline and
zero padding with all 19 retail words, including explicit global and callback
relocations.

## Evidence

The rebuilt `func_1507488C` span at `build/conker.us.bin+0xA1D0C` equals the
pristine retail span at `conker.us.bin+0xA1D3C`; both have SHA-256
`9d7e011a25b9d1c74c33c0fbfd7b61ec7a2250fbbfdeb7a657dda5a69d7a7176`.
The rebuilt `func_1506EE60` span at `build/conker.us.bin+0x9C2E0` equals retail
at `conker.us.bin+0x9C310`; both have SHA-256
`3bafca9eac8e0ba631d319f1ce8a96fe5562a95bfe3c6fc6bceb8990346ba13c`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,808 / 5,469 (51.34%) | 1 | 2,660 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,236 / 4,791 (46.67%) | 0 | 2,555 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

Focused object builds, a complete guard-table-triggered object rebuild, the
full nonmatching link, fresh progress/matcher scan, and both direct binary
comparisons pass. The replacement build, outer ROM build, project tool checks,
all seven padding/relocation unit tests, guarded-table validation, and
whitespace check also pass. The guard table now has 1,395 rows with zero
duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word Game `func_1507EE58`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
