# Game transformed-position short writer byte match

Date: 2026-09-30

`func_1516441C` occupies 35 words and 140 bytes at
`0x1516441C..0x151644A8`. Its caller passes the event-specific inline payload
beginning at `struct225 + 0x18`. The payload's first three words are the source
position, while its word at offset `0x0C` points to the transform consumed by
`func_15145CD0`.

The recovered routine supplies one source and one stack-local destination to
that transform helper. It truncates the three resulting floats to signed
integers and stores their low halfwords at offsets `0x0E`, `0x10`, and `0x12`
of the render record referenced by `struct225 + 0x14`.

The shared `struct225` payload region remains intentionally unchanged because
other event classes interpret the same storage differently. A focused cast at
the caller and the handler's typed `struct227 *` contract make this event's
inline interpretation explicit. Pointer declarations followed by the output
vector recover retail's `sp+0x2C`, `sp+0x28`, and `sp+0x1C` local layout; source
then destination assignment recovers the complete `t6`/`t7` lifetime.

All 35 words emit directly from semantic C with no expected-word guards or
compiler-profile override. The focused object and complete linked build pass.
The linked ELF and pristine decompressed retail spans share SHA-256
`2b3e339b55f5ccfb744f48761aab23bb7e518571dc34d5aeef4826b8a7015d26`.
The authoritative matcher advances exactly one row to
`3,062 / 5,462 (56.06%)` overall and `2,483 / 4,788 (51.86%)` in Game, with
zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_1517D578`, the next ordinary matcher row.
