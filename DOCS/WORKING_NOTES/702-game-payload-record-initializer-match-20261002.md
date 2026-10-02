# Game payload-record initializer match

Date: 2026-10-02

Game `func_1518BCD0` occupies the 36-word slot at
`0x1518BCD0..0x1518BD60`. It calls
`func_15167A68(0x1F, owner, 0x44, 1, selector, 1)` and returns null when the
allocator fails. A successful record receives the caller's 0x1C-byte payload
at offset `0x10`, followed by two independent `func_150ADA20() & 0x1F` values
at offsets `0x2C` and `0x30`. The record pointer is returned.

The recovered `void *func(void *, u8, s32)` contract explains retail's full
incoming argument spills and low-byte reload from the stored `a1` word. The
record local also reproduces the `s0` lifetime: it first carries the incoming
owner through the allocator call, then receives the returned record in the
call-result branch delay slot.

All 36 words emit directly from C without expected-word guards or a compiler
profile override. The 40-byte frame, saved-register lifetime, six allocator
arguments, null-return branch, `memcpy`, both random calls, delay-slot first
random store, masks, return value, relocations, and epilogue match in the
focused object and final linked image.

The incremental generated-object build, full link, and linked matcher complete
with zero address drift. Game advances to `2,541 / 4,788 (53.07%)`, with
2,247 different C rows; overall byte-exact C progress is
`3,209 / 5,456 (58.82%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object comparison, full-link, and linked-word comparison evidence.

Continue from [Working Note 703](703-game-scaled-indexed-global-updater-match-20261002.md),
then resume the ordinary small-Game queue with 37-word `func_150FCF1C`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
