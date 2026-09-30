# Game auxiliary-state allocator byte match

Date: 2026-09-29

`func_1503B7C0` occupies 32 words and 128 bytes at
`0x1503B7C0..0x1503B840`. It allocates and clears an 0x50-byte auxiliary
record, stores the pointer through the object's state at offset `0x11C`, sets
record float offset `0x44` to `30.0f`, and initializes halfword offset `0x4C`
from `func_150ADA20() % 30U`.

The state pointer formerly occupied five bytes of anonymous padding in
`struct126`. Splitting that region into one padding byte and a pointer exposes
the retail field while preserving the structure's size and every following
offset. The recovered function deliberately reloads the object/state/pointer
chain after calls, reproducing retail's 24-byte frame, allocation and `bzero`
calls, float-store delay slot, PRNG division, and final halfword store. No
expected-word guards are needed.

The shared-header edit triggered a broad dependent-object rebuild. The fresh
matcher advanced by exactly this one row and reports
`3,046 / 5,463 (55.76%)` overall and `2,467 / 4,789 (51.51%)` in Game with no
address drift. Linked Game offset `0x3B7C0` and retail ROM offset `0x68C70`
share SHA-256
`8994679685f5b6fc094da283e915dd0eee9b0eb5c37aeb33bb08ec1b739d0c00`.
The replacement payload build, outer non-matching ROM build, project tool
checks, and all 10 tool unit tests also pass.

Keep Game `func_15015F40` and `func_150A76F0`, Game `func_15106E78`, and Init
`func_1000FF90` parked at their documented ownership/compiler boundaries.
Resume with 33-word Game `func_150413FC`, the next ordinary matcher row.
