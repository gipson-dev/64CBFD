# Game mode-gated object cleanup wrapper byte match

Date: 2026-09-30

`func_1511A738` occupies 34 words and 136 bytes at
`0x1511A738..0x1511A7C0`. When `D_800C35EA` is one, it derives the object's
index from the `D_800DBEF4` table base and calls `func_15022B08(index, 0)`.
A successful lookup clears the state word at offset `0x7C` and the float at
offset `0x18`. The routine then always calls `func_151162D4` and forwards the
object plus its offset-`0x80` and offset-`0x84` fields to `func_1511A494`.

Recovering the byte-pointer table base, byte-sized mode flag, 160-byte record
stride, and `void` return type reproduces retail's frame, saved object-pointer
lifetime, branch-likely delay slot, conditional stores, and both final calls.
All 34 words emit directly from semantic C; no expected-word guards are used.

The matcher advances by exactly one row to `3,057 / 5,462 (55.97%)` overall
and `2,478 / 4,788 (51.75%)` in Game with no address drift. The linked
136-byte Game span has SHA-256
`a1053a069258527eb633d4a5874bdd5c7cdac0c558ad4075cc3587436922a264`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
34-word Game `func_151239CC`, the next ordinary matcher row.
