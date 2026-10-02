# Init compact-sequence voice handler match

Date: 2026-10-01

`__n_CSPVoiceHandler` occupies 684 words and 2,736 bytes at
`0x10013598..0x10014048`. Its former C placeholder returned zero and omitted
the event-processing callback that drives the compact sequence player.

The recovered handler follows the SDK compact-sequence player while retaining
Conker's extensions. It dispatches sequence-reference and API events, closes
and unmaps finished voices, advances envelope stages, updates tremolo and
vibrato oscillators, and forwards MIDI and meta events. Master-volume changes
are propagated across the allocated-voice list.

Rare's event 25 updates the two global mix factors and refreshes each active
voice's effect mix. Event 26 routes its packed control payload through the two
resource families selected by its subtype byte. The play and stop cases retain
the game's paused state and saved reference-event delta, while the two-stage
shutdown path flushes sequence events, releases overdue voices, transfers the
per-channel enable bytes into the channel mask, frees stopped voices, and
releases retained instrument resources.

The readable implementation compiles to 667 words. The retail function uses a
closed 684-word IDO layout. Six hundred sixty-seven function-scoped,
stale-checked rows reproduce that layout, including 17 checked insertions and
45 rows that verify and replace compact-object relocations. No compact words
are omitted.

The padded object and linked ELF build successfully, and the matcher no longer
lists `__n_CSPVoiceHandler`. Direct comparison of
`0x10013598..0x10014048` reports zero different bytes. Both 2,736-byte spans
share SHA-256
`c5673a64d3bce5c9a7b63077a0d36dc5e87fa6096ea470c2902ef76c85c4331e`.

The matcher advances to `3,169 / 5,456 (58.08%)` byte-exact C functions
overall and `486 / 487 (99.79%)` in Init, with zero address drift and one
different Init row. The final Init target is the 1,363-word `_n_handleEvent`,
currently different in 1,164 words.
