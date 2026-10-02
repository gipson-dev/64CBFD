# Init instrument channel loader match

Date: 2026-10-01

`func_1001B7D0` occupies 345 words and 1,380 bytes at
`0x1001B7D0..0x1001BD34`. Its former C placeholder returned zero and omitted
the sequence player's program-to-channel setup path.

The recovered routine resolves the requested instrument through the audio
driver's resource callback, releases the channel's previous program resource,
and relocates each unresolved sound entry. It then copies the first sound's
envelope times and gains together with the instrument's volume, pan, priority,
bend range, tremolo, and vibrato defaults into Rare's 60-byte channel record.
Missing instruments set the channel's missing-resource flag and return one;
valid instruments clear transient fields, retain the selected program, and
return zero. Retail's unusual zero-sound early return is preserved.

A local `ConkerALChanState` overlay names the existing 32-byte Rare extension
to `ALChanState` without changing the public SDK layout. Repeating each
channel-index expression reproduces retail's unoptimized `-g` address
calculation. Ordering the three locals as sound, instrument, and loop index
also reproduces retail's stack slots. The resulting compact function contains
exactly 345 words and every word, branch, and relocation emits directly from
C; no expected-word guards are used.

The padded-object build accepts the source unchanged, and the linked matcher
no longer lists `func_1001B7D0`. Direct comparison of
`0x1001B7D0..0x1001BD34` reports zero different bytes. Both 1,380-byte spans
share SHA-256
`9fe00cc8721b345585d353b756b7131239bcfc9f104f87f4f6c0d9dcb9e41f1f`.

The matcher advances to `3,162 / 5,456 (57.95%)` byte-exact C functions
overall and `479 / 487 (98.36%)` in Init, with zero address drift and eight
different Init rows. The next smallest measured Init candidate is the
357-word `func_10011624`, currently different in 350 words.
