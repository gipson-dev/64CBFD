# Game cache-expiry cleanup match

Date: 2026-11-13. `func_1517ABB0` replaces the placeholder in
`conker/src/game/generated_1A8060.c`. Its 84-word retail slot spans VA
`0x1517ABB0..0x1517AD00`, ROM `0x1A8060..0x1A81B0`.

The recovered routine walks two cache groups. A group descriptor supplies the
row-count index and slots per row. Occupied entries with a nonzero age have it
decremented; entries at zero age are released through `func_10004074`. After a
release, the group and row pointers are reloaded before clearing the entry.
Slot and row counts are also reloaded at the original points so helper effects
and aliases retain their retail behavior. The C source uses named cache-entry
and descriptor layouts and the caller-compatible `void` interface.

The compiler emits the retail 64-byte frame and complete 84-word body. Sixteen
expected-word guards restore a closed saved-register exchange, a count-register
choice and one independent initialization order; two retain the original
HI16/LO16 bindings. Neither padder inserts or omits words, and both reproduce
the retail body and bindings. The other owner function is unchanged. See
[Note 2382](2382-game-cache-expiry-private-screen-20261113.md) for the private
screen and its initially incomplete free-path fixture.

Tools commit `32d006c` supplies the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_cache_expiry_1517abb0_match -v
```

The suite covers 2,880 guest cases per retail/raw body and all 84 instructions,
including helper mutations of live group pointers and counts, plus six
descriptor or caller-stack aliases. The original frame caller
`func_15019414` runs 480 cases per retail/raw/padded body. Native 32-bit
O0/O2/O3 each pass 2,880 cases with trapping UBSan and six effective semantic
controls. Another 428 retail/padded guest access-fault prefixes include 21
delay-slot cuts. Both padders reject 64 individually corrupted guard
preimages, and 12 GNU links cover four symbol layouts. The release helper is a
bounded provider; these results do not establish live gameplay behavior.

All eight checks pass in the mounted tools checkout and an isolated sibling
overlay. The overlay uses mounted fallbacks, so it is a hybrid check; the
sibling's 2,434 pre-existing dirty paths remain unchanged. Shared project tool
checks pass as well.

The production build and independent full-image audit pass with 265 changed
bytes and zero exclusions. The audit explicitly accounts for a reorder of the
two symbol metadata entries `D_80041890` and `D_8009BB90`. Only the target
body changes among 6,051 functions, all addresses remain fixed, and all
189,088 protected Game-data bytes remain identical. Of 698 fingerprinted
linked source objects, only `generated_1A8060.c.o` changes; the debugger object
and conversion CSV remain identical. The scoped Graphify refresh retains all
60,044 prior node IDs and does not claim a full-corpus extraction.

Fresh production recount: Game **3,767 / 4,843 (77.78%)**, total
**4,440 / 5,516 (80.49%)**, zero address drift. **108** further Game matches
are required to reach 80% at the current denominator. Continue the Game goal.
