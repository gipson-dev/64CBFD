# Init actor positional-audio creator match

Date: 2026-10-01

`func_10010154` occupies 124 words and 496 bytes at
`0x10010154..0x10010344`. The former implementation returned zero. The
recovered return type is `s32`; the placeholder's `u16` declaration introduced
a false return-value normalization and did not match the retail caller ABI.

The routine rejects actors whose interaction state is zero or five. An actor
with a camera uses the direct audio allocator with pan `0x40`, the actor's
existing handle, packed state flags from `unk184`, and `D_80041FD9`, then
stores the returned handle at `unk8E`.

Without a camera, actor ID `0x16` doubles the signed range and, when the
caller-provided limit is smaller, replaces it with that limit minus 200. IDs
`5`, `0x4F`, and `0x83` select flag `4`; IDs `0x8A` and `0x23` select flag
`0x100` when `unk13C` is set. The routine retires the prior actor-owned sound,
then, if the actor remains active, creates a positional sound from the actor's
truncated coordinates and stores the new handle.

The recovered C reproduces the complete frame, branch graph, actor policy,
calls, and 124-word slot. Seventy-eight words emit directly from semantic C.
Forty-six stale-checked rows normalize the remaining camera-call scheduling,
temporary-register allocation, and stack-slot selection; three rows preserve
the relocation migration for `D_80041FD9`.

The complete ELF link passed after a full stale-check rebuild. The
authoritative matcher no longer lists `func_10010154`; direct comparison of
all 496 bytes reports zero differences, and the linked and retail spans share
SHA-256
`0c51638492ad873409e1f0207c4185ddbcb9288bcfc7b8384ba1e065d39fb915`.
Project tool checks pass. The focused unit suite passes all 10 tests.

The matcher advances to `3,130 / 5,457 (57.36%)` overall and
`447 / 488 (91.60%)` in Init, with zero address drift and 41 genuinely
different Init C rows.
