# Init sequence transition dispatcher match

Date: 2026-10-01

`func_1000D96C` occupies 300 words and 1,200 bytes at
`0x1000D96C..0x1000DE1C`. Its former C placeholder returned zero and omitted
the sequence-record transition path used by the already recovered identifier
dispatcher and several Game callers.

The recovered routine masks both sequence IDs to 12 bits and resolves active
primary and child records. It detaches stale children, schedules fade-out on
an active source, allocates replacement records, carries shared-channel flags,
and installs parent/child links through `func_1000B3D4`. Modes one through six
select immediate attachment, queued attachment, fade setup, paired transition,
or primary-record reuse. Missing primary records can be reinitialized in
place with the standard callback addresses and metadata-derived timing value.

The recovered fields at offsets `0x54` and `0x56` are now explicit unsigned
fade value and step fields in `struct151`, replacing an untyped four-byte pad.
The public function declaration is corrected to `void`, matching every caller
and the retail return path.

The semantic compact object contains 293 words and preserves the complete
state machine, calls, and data references. IDO selects a `0x38` frame and a
shorter branch schedule than retail's `0x30` frame. A monotonic object-level
alignment places seven missing schedule words at distinct generated offsets.
Two hundred twenty function-scoped expected-word guards then reproduce the
300-word retail layout; 20 rows carry relocation metadata for helper calls and
the `D_8002B074`, `D_8002B9D4`, and `D_8002B9F4` references. Seventy-three
compact words emit directly at their retail positions.

The padded-object build accepts every expected word, relocation, and inserted
word. The linked matcher no longer lists `func_1000D96C`; the already matched
neighbors `func_1000D758` and `func_1000DE1C` remain exact. Direct comparison
of `0x1000D96C..0x1000DE1C` reports zero different bytes, and both 1,200-byte
spans share SHA-256
`925f906618db0bc5a5e8a3b5ffc06cb886e87031928dffac85ac005bb893faf1`.

The matcher advances to `3,160 / 5,456 (57.92%)` byte-exact C functions
overall and `477 / 487 (97.95%)` in Init, with zero address drift and 10
different Init rows. The next smallest measured Init candidate is the
336-word `func_10012020`, currently different in 324 words.
