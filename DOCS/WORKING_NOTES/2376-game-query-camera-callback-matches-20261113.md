# Game script-query and camera-condition matches

Follow-up: one of the seven query callbacks is now restored; see [Note 2377](2377-game-script-list-query-callback-match-20261113.md).

Date: 2026-11-13. The former zero-return placeholders `func_1509BE40` and
`func_150BE850` now reproduce their respective 92-word and 87-word retail
bodies. Their executable spans are VA `0x1509BE40..0x1509BFB0` / ROM
`0xC92F0..0xC9460` and VA `0x150BE850..0x150BE9AC` /
ROM `0xEBD00..0xEBE5C`. Both retain the retail `0x30`-byte frame.

The first routine builds a script-query packet from a count followed by
variadic words. It saves the prior packet count, extracts the selector and
dispatch-table index from the flags, writes the key and extra words, calls the
selected provider, restores the count, and returns the provider's result. It
does not add checks for invalid selector indexes or null table entries.
The raw C emits 93 words; 16 checked guards remove one redundant high-address
setup word and restore retail's argument homes, register allocation,
instruction scheduling and relocation bindings. The second routine queries
three script conditions and updates or releases a camera state through its
helpers. Its C callback takes the integer address passed by the original
`func_15130230` dispatcher; six checked guards restore a closed floating-
register allocation cycle. Both object padders reproduce the original bodies
and relocation bindings. For the query owner the generated-padder cross-check
uses a synthetic layout; production uses the generic padder.

The query-table ABI required more than fixing the new caller. The 14 non-null
entries in `D_80088498` now have compatible `(s32, s32, s32 *)` definitions;
the null entry remains null. Eight existing caller owners also use the
consistent `s32 (s32, ...)` query declaration. Existing recovered callback
bodies compile to their previous bytes. Seven callbacks remain zero-return
placeholders and are **not newly counted**: their typed signatures initially
emitted three unused argument-home stores each. Twenty-one additional checked
omission guards preserve their previous linked bytes and all owner neighbors.
These guards do not restore the missing callback behavior.

Tools commit `85bff4d` provides reproducible qualification:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_camera_query_150be850_match -v
```

The complete ten-check suite passed with staged sibling dependencies; nine
checks plus a separate query-table ABI check passed in the mounted environment.
Both environments also verified the installed source/guard fingerprints and
both linked retail bodies. The suite compares 162 query-helper and 128 camera
cases per modeled stream, including count boundaries, stack arguments, camera
state paths and provider mutations. It connects the complete original camera
dispatcher for 32 cases per stream and connects the original and guarded query
helper to the camera for 128 cases per stream. The guest fault model compared
69 helper and 28 camera access prefixes. Native32 builds at O0/O2/O3 passed
162 query cases and 128 camera cases per profile, with four and five effective
negative controls respectively. Eighteen GNU links across three layouts check
relocations, and 172 individual corrupted guard preimages are rejected by both
padders. The project tools check passed. These are bounded, synthetic tests:
providers are modeled, arbitrary overlapping objects and C fault semantics are
not proven, and no hardware or live gameplay acceptance is claimed.

Actual Make compiled all 21 affected owners. Its production objects and linked
ELF equal the independently audited shadow. The strict full-image comparison
accounts for 660 changed bytes, including four explicitly reconciled symbol
metadata reorder groups, with zero exclusions. Only the two target functions
change among 6,051 functions; every function address and all 189,088 protected
Game-data bytes remain unchanged. The other 1,433 linked objects and the
conversion rows remain unchanged. The 43 added guard rows comprise 16 for the
query helper, six for the camera callback and 21 for the seven placeholders.
The older standalone tools checkout's pre-existing changes were preserved.

A fresh production recount reports Game **3,762 / 4,843 (77.68%)**, total
**4,435 / 5,516 (80.40%)**, zero drift, and **113** further Game matches
required for 80% at the current denominator. The host port was not changed or
runtime-tested as part of this decompilation match.

The scoped graph refresh retained or relocated all 60,014 prior nodes, with
60,025 afterward and no out-of-scope removals or changes after restoring four
historical annotations. Its fail-closed path retained 31,816 existing nodes;
it was not a full-corpus extraction.
