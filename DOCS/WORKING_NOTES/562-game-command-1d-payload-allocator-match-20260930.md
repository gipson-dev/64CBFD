# Game command-0x1D payload allocator byte match

Date: 2026-09-30

`func_1518AADC` occupies 33 words and 132 bytes at
`0x1518AADC..0x1518AB60`. It requests a 40-byte command-`0x1D` record from
`func_15167A68`. Allocation failure returns null. Success clears words at
offsets `0x10`, `0x14`, and `0x1C`, stores the retained owner at `0x18`,
duplicates a signed halfword at `0x20` and `0x22`, stores a byte selector at
`0x24`, and returns the new record.

The recovered three-argument contract preserves the signed-halfword and byte
argument homes. Their post-call `lh sp+0x26` and `lbu sp+0x2B` reloads therefore
come from the ABI rather than casts or raw stack access. The typed payload also
exposes every initialized field and keeps the allocation size and command type
explicit.

Twenty-three words emit directly from semantic C. Ten stale-checked guards
normalize two independent schedules: retail reloads the signed halfword before
testing allocation success and retains the result pointer in the branch delay
slot; then it loads the owner immediately after the first clear and carries it
across the remaining stores. No call argument, branch target, field offset,
loaded value, store value, or return path is changed.

The focused object, complete relink, outer ROM build, and authoritative matcher
pass. The linked ELF and pristine decompressed retail spans share SHA-256
`7e6524e62e23ce9f04813a749375ae59fd2ce4fd0cb2a8b3ff2d56c313256671`.
The matcher advances exactly one row to `3,065 / 5,462 (56.11%)` overall and
`2,486 / 4,788 (51.92%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_15192920`, the next ordinary matcher row.
