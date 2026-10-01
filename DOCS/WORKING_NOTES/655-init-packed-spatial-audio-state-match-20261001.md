# Init packed spatial-audio state match

Date: 2026-10-01

`func_1000BF60` occupies 252 words and 1,008 bytes at
`0x1000BF60..0x1000C350`. Its previous C body returned zero even though the
retail routine maintains a packed state word for sound `0x22`.

The recovered body starts the sound when needed, preserves its prior mode and
packed channel values, and exits through the existing audio cleanup path when
the active level is not `0x1D`. In the active level it performs three spatial
queries through `func_100114D0`, normalizes their returned values, and updates
the affected volume and position channels through `func_1000886C`,
`func_10008744`, and `func_100086FC`. The final mode transition either counts
down and fades mode 1 or starts mode 2, then returns the refreshed packed
state.

IDO emits the semantic body in 250 words with retail's `0x60` frame. One
hundred thirty-nine retail words emit directly. One hundred eleven
function-scoped, stale-checked rows normalize the remaining closed register,
stack-slot, and scheduling differences. Two of those rows insert retail's
redundant `move a2` scheduling words at `+0x20C` and `+0x2A4`; two rows carry
relocation differences explicitly. No resolved-address binary patch is used.

A targeted object rebuild accepts every expected word and relocation, and the
full linked ELF completes successfully. Direct comparison of
`0x1000BF60..0x1000C350` reports zero different bytes. Both 1,008-byte spans
share SHA-256
`e7a0f3fa7e4953b9c62c703ee6c206047cdf9ddc3dc3452c2217b800435b3e1d`.

The refreshed matcher reports `3,153 / 5,456 (57.79%)` byte-exact C functions
overall and `470 / 487 (96.51%)` in Init, with zero address drift and 17
different Init C rows. The next smallest measured Init candidate is the
258-word `func_10003C6C`, currently different in 254 words.
