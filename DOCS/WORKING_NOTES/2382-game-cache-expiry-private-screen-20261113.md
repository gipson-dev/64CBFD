# Game cache-expiry private screen

This screen was subsequently promoted in [Note 2383](2383-game-cache-expiry-cleanup-match-20261113.md).

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

A later split of the two slot-count reload paths emits the full 84-word retail
extent and reduces the remaining same-position differences to 16. These are
a saved-register exchange, count-register allocation and one independent
initialization order. A private generated-padder screen restores all retail
words and bindings with 16 proposed guards and preserves the padded neighbor.
A private guest screen passes 2,880 cases for both retail and raw C, reaching
all 84 words and including free-provider changes to group pointers and live
counts. The test initially missed the free path; its fixture was corrected
before the reported run. Native 32-bit O0/O2/O3 each pass 2,880 cases and six
incorrect implementations are rejected. The complete original frame caller
`func_15019414` passes 480 cases per retail, raw and padded body. These remain
private bounded screens pending durable tests and production qualification.

The subsequent private qualification adds six descriptor or caller-stack
aliases, 428 guest fault prefixes (21 in delay slots), 64 stale guard
rejections across both padders, and 12 links over four symbol layouts. The
actual three-command Make shadow changes only this body among 6,051 functions
and leaves all protected Game data identical. Its strict 265-byte difference
includes a predicted reorder of two symbol metadata entries, with zero
excluded ranges. The mounted durable eight-test suite passes; production has
not yet been rebuilt or recounted for this candidate.

The alternative-source draft is non-matching and includes incompatible
field-width and pointer-stride assumptions; it was not adopted. Next, make the
guest, native, caller and guard checks durable; extend alias and fault-prefix
coverage; and qualify the actual Make output and linked image before installing
or crediting a match. No production source
or match total changes in this screen. Game remains **3,766 / 4,843 (77.76%)**;
**109** more matches are needed for 80% at the current denominator.
