# Init audio-environment controller match

Date: 2026-10-01

`func_10012020` occupies 336 words and 1,344 bytes at
`0x10012020..0x10012560`. Its former C placeholder returned zero while a
substantial historical draft remained commented out below it.

The recovered routine starts from the two default pitch and volume pairs at
`D_8002BA18` and `D_8002BA10`. It resolves the requested environment from the
one-shot, override, and fallback mode globals, then dispatches five modes.
Those modes select fixed or oscillator-driven pitch and volume targets,
smooth active values toward new targets, and manage the state-four transition
that raises the secondary pitch until its completion threshold.

After mode processing, the routine advances the oscillator phase, updates the
three master-gain channels when the normalized level changes, and sends any
changed pitch or volume value to both environment channels. The consumed
one-shot mode is cleared before return. The existing read-only addresses are
declared as their real default arrays and floating constants, while byte
`0x2A` in `struct104` now names the runtime gate used by the mode override.

The semantic compact body contains 335 words. Its real `switch` emits a
five-entry `.rodata` table, and the `init_11FA0` object now retargets that
table to retail's `jtbl_8002C410_init`. One hundred eleven compact words emit
directly at their retail positions. The 225 function-scoped expected-word
guards normalize the remaining compiler allocation and schedule; one row
inserts the retail padding `nop` after the return delay slot, and 103 rows
carry relocation metadata for the switch table, constants, globals, and
helper calls.

The padded-object build accepts every expected word and relocation. The
linked matcher no longer lists `func_10012020`, and the four neighboring mode
setter/reset routines remain exact. Direct comparison of
`0x10012020..0x10012560` reports zero different bytes, and both 1,344-byte
spans share SHA-256
`983583d5193a47ee8b1140807b1a8dbdda67951e3d8b31bb21c2cc89a14ed8fb`.

The matcher advances to `3,161 / 5,456 (57.94%)` byte-exact C functions
overall and `478 / 487 (98.15%)` in Init, with zero address drift and nine
different Init rows. The next smallest measured Init candidate is the
345-word `func_1001B7D0`, currently different in 334 words.
