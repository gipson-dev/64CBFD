# Init pending note-end query match

Date: 2026-09-30

`func_1001ADA4` occupies 97 words and 388 bytes at
`0x1001ADA4..0x1001AF28`. The former zero-return placeholder is replaced with
the recovered SDK pending-note-end query, corresponding to
`__n_voiceNeedsNoteKill` behavior.

The routine walks the sequence player's allocated event queue while
accumulating delta times. When it finds an `AL_NOTE_END_EVT` for the requested
voice, an event after the caller's kill time is removed from the allocated
list and returned to the queue's free list. Its delta is transferred to the
following event before unlinking. An event at or before the kill time clears
the returned kill-needed flag; absence of a matching event leaves that flag
set.

Seventy-six of 97 retail words emit directly from the typed SDK logic and the
object's `-g` compiler profile. Twenty function- and offset-scoped replacement
guards normalize four branch displacements and the closed relink/return tail.
The final epilogue word is emitted through one stale-checked `insert_after`
entry because IDO otherwise moves the preceding store into an unconditional
branch delay slot and shortens the generated body by one word. No words are
omitted.

The exhaustive stale-guard rebuild compiles and links every padded object
without a guard failure. The expected whole-ROM SHA-1 check still fails
because the project contains unrelated non-matching functions. The
authoritative matcher and direct 388-byte section-span comparison pass. The
linked and retail spans share SHA-256
`a23783a71d1e0d4ee84491f53a75f82cde29c37c044fb29f0d21dd2745f0874e`.

The matcher advances to `3,109 / 5,457 (56.97%)` overall and
`426 / 488 (87.30%)` in Init, with zero address drift and 62 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
