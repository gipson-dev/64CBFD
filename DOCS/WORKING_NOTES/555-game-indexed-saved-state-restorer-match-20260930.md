# Game indexed saved-state restorer byte match

Date: 2026-09-30

`func_151239CC` occupies 34 words and 136 bytes at
`0x151239CC..0x15123A54`. It checks the selected entry in the 21-element
active-slot array at object offset `0x20C`. For an active entry, it restores
the saved identifier at offset `0x00`, four word values at offsets `0x2C`,
`0xDC`, `0x84`, and `0x134`, and two halfword values at offsets `0x1B4` and
`0x1E0`. It then calls `func_15124B18`, clears the selected active flag, and
returns one. An inactive slot returns zero without changing the object.

A typed 16-bit slot cursor plus repeated 32-bit indexed expressions reproduce
retail's two index scales, pointer lifetimes, load/store order, branches, call,
and success/failure values. Thirty-two words emit directly from semantic C.
Two stale-checked guards move the live slot pointer's call-delay spill and
reload from IDO's `sp+0x18` choice to retail's equivalent `sp+0x1C` slot. No
instruction position, relocation, branch target, or behavior changes.

The matcher advances by exactly one row to `3,058 / 5,462 (55.99%)` overall
and `2,479 / 4,788 (51.78%)` in Game with no address drift. The linked
136-byte Game span has SHA-256
`ec56b71f610b4610715e4fcf2392dfb3a9a19190390075a9053f0466bb6ad33a`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_1514E89C`, the next ordinary matcher row.
