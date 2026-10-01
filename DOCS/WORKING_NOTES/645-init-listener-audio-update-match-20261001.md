# Init listener/audio update match

Date: 2026-10-01

`func_10011BB8` occupies 180 words and 720 bytes at
`0x10011BB8..0x10011E88`. The active source previously returned zero and did
none of the retail frame-level listener or audio-record maintenance.

When both transition flags are clear, the recovered routine snapshots every
active player into the 0x1C-byte `D_80041F68` listener array. Player zero uses
its alternate `0x2A4` position when flag `0x80000` is clear; all other cases
use the `0x2F8` position. Each listener also receives the common `0x2F8`
position and the orientation value at player offset `0x380`.

The routine then runs `func_10011310` and `func_10011624` over the active
0x30-byte records in `D_80041FE0`. It compacts records in place, retaining only
entries without flag `0x80`, and writes the surviving count to `D_80042760`.

The final phase compares the current channel target and transition state with
their previous values. State one clears channels zero and one. Other states
submit the current channel values, then move `D_80041F54` toward
`D_80041FDC` by the truncated product of their difference and
`D_80041F58`; a zero-sized step snaps directly to the target. The current
transition byte is then saved for the next update.

The semantic body compiles four words larger than the retail slot because IDO
retains redundant pointer/register moves around the listener and record-copy
loops. One hundred twenty-seven stale-checked rows normalize the resulting
closed allocation and scheduling cycle while preserving every global and call
relocation. Four of those rows omit the verified redundant moves. The other
57 linked words emit unchanged from C, and the padded function retains the
retail 180-word extent without an overflow trampoline.

The authoritative linked matcher no longer lists `func_10011BB8`. The linked
and retail 720-byte spans share SHA-256
`46f06a5608ddf3ddaa80ec0b81444b7b4463fee22ab930ca536ccd71394fa0de`.
The repository-wide stale-check build and final link pass. Project tool
checks pass, all 10 focused tool tests pass, and `git diff --check` is clean.

The measured checkpoint is `3,144 / 5,457 (57.61%)` overall and
`461 / 488 (94.47%)` in Init, with zero address drift and 27 genuinely
different Init C rows. The next Init candidate is `func_1000FF90`, a 35-word
active-record lookup with 31 real linked-word differences.
