# Game cache-expiry private screen

Date: 2026-11-13. `func_1517ABB0` is the next unconverted candidate in
`conker/src/game/generated_1A8060.c`. Its retail body spans VA
`0x1517ABB0..0x1517AD00`, ROM `0x1A8060..0x1A81B0`, or 84 words.

Retail iterates two cache groups. Each group's eight-byte descriptor selects
a halfword row count and a byte slot count. For non-null group tables it walks
rows and eight-byte entries: an occupied entry with a nonzero age decrements
that byte; an occupied entry with zero age calls `func_10004074`, reloads the
group and row pointers, and clears the allocation pointer. The original also
reloads the slot count after occupied entries and the row count after a
nonempty inner scan. Those access points must be preserved when qualifying
aliases and provider mutations.

An initial private semantic C screen emits 83 words, has the retail 64-byte
frame, and leaves the sole other owner function and the owner pools unchanged.
It differs at 64 same-position words. An explicit byte-offset variant also
emits 83 words and reduces that measure to 61 differences; the counts include
the extent mismatch and are not a claim of equivalent scheduling. Sources,
objects and diagnostics are retained under the ignored directory
`conker/build/game-cache-expiry-1517abb0-screen/`.

The alternative-source draft is non-matching and includes incompatible
field-width and pointer-stride assumptions; it was not adopted. Next, inspect
the register and delay-slot differences, preserve all live pointer/count
reloads, and qualify the full caller, aliases, provider effects, owner, padder
and linked image before installing or crediting a match. No production source
or match total changes in this screen. Game remains **3,766 / 4,843 (77.76%)**;
**109** more matches are needed for 80% at the current denominator.
