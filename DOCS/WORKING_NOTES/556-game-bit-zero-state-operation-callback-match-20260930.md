# Game bit-zero state-operation callback byte match

Date: 2026-09-30

`func_1514E89C` occupies 33 words and 132 bytes at
`0x1514E89C..0x1514E920`. Operation zero toggles bit zero of the word at object
offset `0x10`, operation one sets it, and operation two clears it. Each handled
operation returns one; any other operation returns zero without changing the
word. The third callback argument is byte-typed but otherwise unused.

An old-style declaration and K&R definition preserve the callback table's
unprototyped call contract while exposing the byte type to IDO inside the
routine. That reproduces retail's entry argument spill without adding
conversion instructions to neighboring wrappers. Listing the clear case
before the set case gives IDO retail's physical block order, register
lifetimes, branch-likely load, and retained unreachable instructions. All 33
words emit directly from semantic C; no expected-word guards are used.

The matcher advances by exactly one row to `3,059 / 5,462 (56.01%)` overall
and `2,480 / 4,788 (51.80%)` in Game with no address drift. The linked
132-byte Game span has SHA-256
`e3b31f4007d3288e78f7111a743bcdb9e6ae4ebd371d4c4db5ecdb1df6f61851`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
32-word Game `func_1514EDF0`, the next ordinary matcher row.
