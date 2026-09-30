# Game linked-endpoint event handler byte match

Date: 2026-09-29

`func_151B70B4` occupies 36 words and 144 bytes at
`0x151B70B4..0x151B7144`. It obtains a linked endpoint record through object
offset `0x98`. Event zero clears object byte `0x30` and sets flag `0x0008` at
offset `0x1E` when the event's first endpoint is the currently linked one.
Event `0x2D` replaces a matching first endpoint with the second and copies
selector byte nine, or replaces a matching second endpoint with the first and
copies selector byte eight.

The recovered semantic C emits the complete control flow, pointer accesses,
branch-likely path, selector-byte stores, and frame-free ABI. IDO emits a
34-word schedule and leaves two padding words. Nineteen stale-checked expected-
word transformations normalize one closed compiler allocation/scheduling
cycle: two inserted preload words preserve retail's event/current lifetimes,
and the remaining guards preserve the zero-event return schedule plus the
corresponding `t0`/`a3`/`v1` and endpoint temporary lifetimes. No relocations,
calls, memory offsets, branch behavior, or recovered semantics are changed.

The exhaustive guarded-object rebuild and non-matching link succeed. The fresh
matcher reports `3,041 / 5,463 (55.67%)` overall and
`2,463 / 4,789 (51.43%)` in Game with no address drift. Linked Game offset
`0x1B70B4` and retail ROM offset `0x1E4564` share SHA-256
`044f8a0c25072ab7a3589f49051658a9275c5c05284eb5b41e406a31f4db30b1`.
The guard table contains 2,266 rows, including 19 for this function, with zero
duplicate `(filename, function, offset)` keys.
The replacement payload build, outer non-matching ROM build, project tool
checks, all 10 tool unit tests, and whitespace check also pass.

Keep Game `func_15015F40` and `func_150A76F0`, Init `func_1000FF90`, and Game
`func_15106E78` parked at their documented ownership/compiler boundaries.
Resume with Game `func_151E55A8`, the next ordinary 33-word matcher row.
