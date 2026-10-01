# Init audio-task submission match

Date: 2026-10-01

`func_100095A0` occupies 139 words and 556 bytes at
`0x100095A0..0x100097CC`. The former implementation returned zero; an older
commented draft identified some fields but called the wrong AI helper, omitted
the synthesis call, and confused command pointers with array indices.

The recovered routine converts the output buffer to a physical address,
services completed audio DMA state, advances synthesis state, and reads the
current AI byte count as samples. When a previous buffer exists it submits
that buffer through `osAiSetNextBuffer`. It then chooses the normal or reduced
sample count from the AI backlog and two-frame recovery counter.

If the selected physical span ends on an `0x2000` boundary, the output pointer
and physical address both advance by 16 bytes. `n_alAudioFrame` writes the
command count and returns the end of the command list. A zero command count
returns immediately; otherwise the routine builds the complete scheduler task,
writes back the cache, sends it to `D_8003B200`, toggles the command-buffer
index, and returns success.

The source restores the retail 64-byte frame and exact 139-word extent. A
three-word local record preserves the command-count stack placement. A
linker-address alias for `D_100291A0` preserves retail's two independent
address-materialization lifetimes while resolving both to the same address.

Sixty-eight words emit directly from semantic C. Seventy-one stale-checked
rows normalize IDO's remaining stack-slot, temporary-register, address-register,
and independent-store scheduling choices. Relocation-bearing rows retain the
original targets, including both retail `D_100291A0` materializations.

The complete ELF link passed after a repository-wide stale-check rebuild. The
authoritative matcher no longer lists `func_100095A0`; the linked and retail
556-byte spans share SHA-256
`0ccabf4750562b5e4fcd9ed0470bc6e10bb5aab211258c1ed3b4c2ceaeaeb360`.
Project tool checks and all 10 tool unit tests pass.

The matcher advances to `3,135 / 5,457 (57.45%)` overall and
`452 / 488 (92.62%)` in Init, with zero address drift and 36 genuinely
different Init C rows.
