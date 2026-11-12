# Game session reset private screen

`func_1500E5C0` is an 83-word Game routine at VA `0x1500E5C0` and ROM
`0x3BA70`. Its startup caller `func_1500E470` invokes it without using a
return value. Retail calls three initialization helpers, clears 20 bytes at
`D_800E0950`, clears paired 12-byte ranges and several other globals, and
calls `bzero` for five bytes.

An isolated semantic candidate compiled to 78 words with 70 positional word
differences across the unequal-length bodies. The other five functions in
the owner compiled unchanged and diagnostics did not change. The candidate
is not installed or counted.

The candidate uses `(&D_800E0950)[i]`, but `variables.h` declares that symbol
as one `u8`. Indexing beyond that object is not a valid final C declaration;
the existing `game_1FFF60.c` also uses the same expression. Retail's loop
establishes a 20-byte access range, but does not by itself establish every
consumer's intended bounds or the full object definition. Qualify the
symbol's ownership, all callers and accesses before choosing an array or
other representation. A shared-header correction also needs the dependency
and image audit described in [Note 2291](2291-game-secondary-walker-type-audit-20261112.md).

The private screen is retained under
`conker/build/game-next-15015FBC-private/` while that scratch directory exists.
It still needs a safe source representation, guest/native and caller checks,
padding and full production-image qualification before it can be counted.
