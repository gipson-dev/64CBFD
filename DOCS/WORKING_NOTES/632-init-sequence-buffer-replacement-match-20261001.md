# Init sequence-buffer replacement match

Date: 2026-10-01

`func_10008CE8` occupies 126 words and 504 bytes at
`0x10008CE8..0x10008EE0`. The former implementation returned zero. Its
recovered signature accepts an unsigned sequence-player index and a signed
32-bit sequence ID, and returns `-1` only when replacement-buffer allocation
fails.

The routine stops the selected compact sequence player and polls its state for
up to 2,000,000 iterations. If the player has not stopped, it issues a second
stop and continues polling to a 4,000,000-iteration total limit. When the
requested sequence differs from the current one, it frees the previous
buffer, reads the source from an 8-byte metadata record, allocates the exact
sequence size, copies the source with the length aligned to 16 bytes, and
updates the current sequence ID. It then initializes the compact sequence,
attaches it to the selected player, and starts playback.

Recovering the metadata as an 8-byte record was required to reproduce retail's
single three-bit sequence-index shift. The compact `while` forms also preserve
the branch-likely counter updates in both polling loops. The resulting C emits
121 of 126 words directly. Five stale-checked rows normalize two independent
IDO stack-slot selections: the saved player-table index and cached
current-sequence pointer.

The complete ELF link passed after a full stale-check rebuild. The
authoritative matcher no longer lists `func_10008CE8`; direct comparison of all
126 linked words reports zero differences, and the linked span has SHA-256
`81fcae361887ea2de962c306ac07c2b55afbd4d8f4c3ee1fa34274c5afc81b14`.
Project tool checks and the focused unit suite pass.

The matcher advances to `3,131 / 5,457 (57.38%)` overall and
`448 / 488 (91.80%)` in Init, with zero address drift and 40 genuinely
different Init C rows.
