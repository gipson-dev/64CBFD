# Init sound-record updater match

Date: 2026-10-01

`func_10011624` occupies 357 words and 1,428 bytes at
`0x10011624..0x10011BB8`. Its former C placeholder returned zero and omitted
the central pass that maintains active positional-sound records.

The recovered routine traverses the caller-selected record range while
respecting both the live record count and an explicit upper bound. It clears
one-shot state, detects completed or stale voice handles, and either retires
the record or resets it for reuse. Active records derive volume, pan, distance,
and callback state through the existing listener-relative helpers. The global
mute gate, optional record callback, sound-ID replacement, zero-volume stop,
pan reflection, priority selection, and voice allocation paths are preserved.

For an existing voice, the routine sends only changed volume, pan, effect-mix,
and pitch parameters. Records with the distance-pitch flag derive a bounded
scale from the previous and current distances, clamp it to `0.5..2.0`, and
smooth the result with the retail constants at `D_8002C400` and `D_8002C404`.
The final handle, flags, distance, volume, packed pan/effect bytes, and pitch
are written back in retail order.

IDO emits a 356-word compact body from the semantic C. Sixty-four words already
match retail directly. The remaining closed frame, register-allocation, and
scheduling difference is represented by 293 function-scoped, stale-checked
rows: 292 substitutions and one insertion after compact offset `0x540`.
Twenty rows carry relocation metadata so calls and global references remain
validated rather than copied blindly.

The padded-object and full linked builds pass, and the matcher no longer lists
`func_10011624`. Direct comparison of `0x10011624..0x10011BB8` reports zero
different bytes. Both 1,428-byte spans share SHA-256
`670591f6d2289fc90f772638ae1d52533acd7ca2cc7d3b659fe6f3db194f7e2f`.

The matcher advances to `3,163 / 5,456 (57.97%)` byte-exact C functions
overall and `480 / 487 (98.56%)` in Init, with zero address drift and seven
different Init rows. The next smallest measured Init candidate is the
370-word `func_10001AA8`, currently different in 358 words.
