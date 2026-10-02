# Init path-projection query match

Date: 2026-10-01

`func_1000A750` occupies 580 words and 2,320 bytes at
`0x1000A750..0x1000B060`. Its former C placeholder returned zero and omitted
the path-relative spatial query used by the audio record updater.

The recovered routine reads the selected path's point count and 8-byte signed
coordinate records. It scans for the point nearest the source position while
retaining the distances on either side of the current best point. Empty paths
return zero without invoking the downstream spatial calculator.

When the nearest point remains at least `0x6D61` squared units away and the
path has another point, the routine selects the better adjacent segment. It
builds the segment and source-offset vectors, computes their dot product and
segment length, retries on the opposite adjacent segment when the projection
falls outside the first, and clamps the projected point to the segment. The
resulting authored-path coordinate is then converted into listener and source
deltas and passed to the already matched `func_1000A420` attenuation/pan
calculator using the recovered 13-argument ABI.

The readable semantic implementation compiles to 404 words. Retail expresses
the nearest-point scan as a five-block remainder-plus-four-way unroll and uses
a closed stack/register schedule. Four hundred one function-scoped,
stale-checked rows reproduce that layout, including 176 checked insertions and
19 relocation-aware rows. No compact words are omitted. The neighboring
`func_1000A420` remains byte-exact.

The padded object and linked ELF build successfully, and the matcher no longer
lists `func_1000A750`. Direct comparison of
`0x1000A750..0x1000B060` reports zero different bytes. Both 2,320-byte spans
share SHA-256
`29dd260425d94890348301d23f84c2bafbc69119f06e2044f6c003c8aaabb8c1`.

The matcher advances to `3,168 / 5,456 (58.06%)` byte-exact C functions
overall and `485 / 487 (99.59%)` in Init, with zero address drift and two
different Init rows. The next smallest remaining Init target is the 684-word
`__n_CSPVoiceHandler`, currently different in 626 words.
