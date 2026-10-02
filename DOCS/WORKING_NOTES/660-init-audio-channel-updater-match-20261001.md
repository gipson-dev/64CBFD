# Init audio channel updater match

Date: 2026-10-01

`func_1000D2F8` occupies 280 words and 1,120 bytes at
`0x1000D2F8..0x1000D758`. Its former C placeholder returned zero and omitted
the per-frame state maintenance for each of the three sequence channels.

The recovered routine applies deferred sequence changes once their event mask
is clear, refreshes the channel's effective volume, and clears completed
requests. It detects stopped channels, promotes queued child records when a
new sequence can be loaded, tears down failed or inactive children, resets the
three channel timing globals, and restores all sixteen deferred track values.

For an active record, the routine dispatches its stride-16 update callback,
advances three target/current/step parameter groups through `func_1000CD40`,
recomputes the effective channel value, and validates or repairs the linked
record. The recovered `struct151` field at offset `0x34` is the callback's
persistent state. The metadata at `D_8002B07C` is a stride-16 callback table,
while `D_8002B080` is the corresponding stride-16 startup-byte view.

The decisive source shape uses an unsigned channel index, retains the indexed
root slot as an expression, and places the inactive-child cleanup after the
successful promotion path. That reproduces retail's `0x40` frame, all 280
words, the unrolled control-flow order, every branch target, every call, and
every relocation. Of those words, 167 emit directly after linking. The 113
function-scoped expected-word guards contain no relocation replacements and
normalize only IDO register allocation, repeated slot reloads, byte-versus-word
argument reloads, and the independent `0x7FFF` schedule.

Correcting the first parameter to the recovered unsigned channel type changes
two caller-side mask instructions in `func_1000D758`. Two additional scoped
guards preserve that already matched 133-word caller without changing its
behavior. The fourth argument remains an integer bit container at the public
call boundary and is reinterpreted as `f32` only for the five-argument update
callback, preserving the original caller ABI and retail `lwc1` load.

The padded-object build accepts all 115 new rows with their expected generated
words. The linked matcher classifies both `func_1000D2F8` and
`func_1000D758` as byte-exact. Direct comparison of
`0x1000D2F8..0x1000D758` reports zero different bytes, and both 1,120-byte
spans share SHA-256
`4735e2a088809328cac08aa82b49cf965dbd98d84de66acffe2bee99c5ed0b92`.

The matcher advances to `3,158 / 5,456 (57.88%)` byte-exact C functions
overall and `475 / 487 (97.54%)` in Init, with zero address drift and 12
different Init rows. The next smallest measured Init candidate is the
296-word `func_10001550`, currently different in 286 words.
