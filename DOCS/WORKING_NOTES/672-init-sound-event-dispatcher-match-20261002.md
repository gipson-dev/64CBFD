# Init sound-event dispatcher match

Date: 2026-10-02

`_n_handleEvent` occupies 1,363 words and 5,452 bytes at
`0x10015944..0x10016E90`. Its former C placeholder returned zero, so the Init
sound player had no event dispatcher despite the surrounding allocation,
cleanup, and playback helpers already being represented in C.

The recovered routine walks linked sound states and handles the complete Rare
event set. It resolves deferred sound resources, allocates and starts voices,
computes envelope timing, volume, pan, pitch, effect mix, and effect bus state,
retries failed allocations, schedules decay and stop events, releases finished
voices, updates channel-volume state, and starts child sounds for parent states.

The typed implementation uses the existing `N_ALSndpSoundState`, `ALSound`,
`ALEnvelope`, and `ALKeyMap` contracts while retaining offset access only for
the event payload and fields that are not yet named in the shared headers. Its
compact IDO body is 1,241 words. One stale-checked row guards each compact
word; 122 checked insertions expand that body to retail's 1,363-word layout,
and 87 rows verify compact-object relocations before replacing the closed
compiler layout. No compact words are omitted.

The padded object and linked ELF build successfully, and the authoritative
matcher reports `_n_handleEvent` byte-exact. Direct comparison of
`0x10015944..0x10016E90` reports zero different bytes. Both 5,452-byte spans
share SHA-256
`583662222304bf87a3b24bc9495055b930b2076e36ecb37183fa5612a36b8525`.

The matcher advances to `3,170 / 5,456 (58.10%)` byte-exact C functions
overall. Init is now `487 / 487 (100.00%)`, with zero address drift and zero
different C rows. Game remains `2,502 / 4,788 (52.26%)`, with 2,286 different
C rows, and Debugger remains `181 / 181 (100.00%)`.

This completes the Init **code-function** matcher queue. It is not a claim that
the entire Init data section is byte-exact. In the current linked image,
`jtbl_8002C708_init` is still an absolute symbol over shifted Init rodata: the
64 bytes at `0x2C708` do not match the retail 16-entry dispatcher table. That
pre-existing Init-data layout issue must be repaired separately before this
dispatcher can be considered runtime-qualified from the rebuilt image.
