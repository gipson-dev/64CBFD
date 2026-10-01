# Init actor secondary-audio creator match

Date: 2026-10-01

`func_10010344` occupies 133 words and 532 bytes at
`0x10010344..0x10010558`. The former implementation returned zero and exposed
an incorrect unsigned 16-bit return type. The recovered contract returns the
signed handle produced by either audio-allocation path.

The routine rejects actors whose interaction state is zero or five. A
negative range is made positive while seeding flag `0x100`. Actors with a
camera use the direct allocator, including the packed `unk184` mode bits and
the special attached-record priority override that forces range `0x7FFF`.

The positional path applies actor-specific policy before replacing the
actor-owned handle. Actor `0x16` doubles the falloff and clamps it relative to
the outer range; actor `0x8A` can add flag `0x100`; actors `0x4F` and `0x83`
add flag 4. The old callback is retired with key `unique_id | 0x20000`, then
the replacement is allocated from the actor's truncated coordinates and
stored in `unk8C`.

The recovered C reproduces the complete frame, branch graph, calls, constants,
and 133-word slot. It emits 115 words directly. Eighteen stale-checked rows
normalize IDO's temporary-register allocation and independent store schedule;
two of those rows move the `D_80041FD9` low-half relocation between the
retail instruction positions without changing its target.

The complete ELF link passed after a full stale-check rebuild. The
authoritative matcher no longer lists `func_10010344`; the linked and retail
532-byte spans share SHA-256
`e4ab5af56af48c42b725a3aef809a80675e61953528b74452ed71ff35c59c03b`.
Project tool checks and all 10 tool unit tests pass.

The matcher advances to `3,133 / 5,457 (57.41%)` overall and
`450 / 488 (92.21%)` in Init, with zero address drift and 38 genuinely
different Init C rows.
