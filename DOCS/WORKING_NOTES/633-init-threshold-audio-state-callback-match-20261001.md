# Init threshold audio-state callback match

Date: 2026-10-01

`func_1000B638` occupies 126 words and 504 bytes at
`0x1000B638..0x1000B830`. The former implementation returned zero. Its
recovered four-argument callback contract carries a packed state value and an
unsigned player index; the final two arguments are part of the callback ABI
but are not used by this routine.

The low state bit tracks whether the selected player's threshold-controlled
audio is active. A missing player record, or a record whose `unk30` value is
below 500, clears the corresponding global request bit. Transitions into and
out of the requested state update mask `0x8000`, select the level-specific
`0x7000` or `0xCA` channel path, and update channel `0xF`.

The second packed bit tracks a separate level-`0x27` effect. Entering that
level submits mode 4 and starts effect 1 once; leaving the level stops effect
1 and clears the bit. The routine returns the two updated bits as one packed
value.

The recovered C reproduces the complete frame, branch graph, calls, constants,
and 126-word slot. It emits 114 words directly. Twelve stale-checked rows
normalize two independent IDO choices: a closed seven-word temporary-register
allocation cycle at entry and five references to the pending-bit stack slot.

The complete ELF link passed after a full stale-check rebuild. The
authoritative matcher no longer lists `func_1000B638`; direct comparison of all
126 linked words reports zero differences, and the linked span has SHA-256
`9606b7c262cfd3a32317eb6775ec0fa9b29db52b3d7f5974048b14a33140cb8d`.
Project tool checks and the focused unit suite pass.

The matcher advances to `3,132 / 5,457 (57.39%)` overall and
`449 / 488 (92.01%)` in Init, with zero address drift and 39 genuinely
different Init C rows.
