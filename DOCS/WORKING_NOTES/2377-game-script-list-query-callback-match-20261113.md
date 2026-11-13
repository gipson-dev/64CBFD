# Game script list-query callback match

Date: 2026-11-13. `func_1509DBBC` replaces the zero-return placeholder in
`generated_C9EC0.c`. Its 84-word body spans VA `0x1509DBBC..0x1509DD0C`
and ROM `0xCB06C..0xCB1BC`; one alignment word follows. The established
three-argument query-table ABI and retail `0x40`-byte frame are preserved.
The raw semantic C emits 88 words. Four checked omissions and 24 checked
word/relocation replacements restore retail's traversal and branch schedule;
both padders reproduce the body and its relocation bindings. The other 18
owner functions, constant pools and compiler diagnostics are unchanged.

For selector 25 and query 4 the routine scans three table-selected linked
lists in each of two rows, returning zero if any node has type byte 2 and one
if none does. The linked table currently contains column indexes 54, 76 and
91. Other selector/query combinations return four. Retail also contains a
coordinate-query block for selectors 4, 5 and 6, but its call is unreachable:
those exact values shifted right by six are zero. The recovered source retains
that control flow rather than crediting the coordinate helper as exercised.
The table's actual callers pass a packet pointer as the third argument; this
callback does not read it.

Tools commit `c18d742` provides reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_query_list_1509dbbc_match -v
```

The seven-check suite passed in both tools environments before and after
installation. A separate 720-case-per-stream guest model covers selector and
query boundaries, all six list slots, multi-node walks and no-match paths.
The complete original and linked `func_1509BE40` query dispatcher was connected
for 756 cases per callback stream with extra-argument counts 0, 1 and 3. The
guest fault model compared 109 access prefixes across retail and both padded
streams. Sixteen deliberately constructed stack/global alias outcomes agreed
across retail, raw C and padded streams; for invalid outcomes only the
exception identity is compared. Native32 builds at O0/O2/O3 passed 360 cases
per profile and rejected six semantic negative controls. Nine independent GNU
links checked three layouts; 112 individually corrupted guard preimages were
rejected by both padders. The project tools check passed. These are modeled,
bounded checks, not a claim about arbitrary invalid pointers, portable C fault
semantics, hardware or live gameplay.

The earlier camera/query regression packet reconstructs its fingerprinted
historical version of this owner and guard manifest in memory. Its ten-check
suite passed after installation with both mounted and staged sibling
dependencies. Those historical checks remain distinct from the new installed
callback checks; the previous source is not restored to the checkout.

Production Make and the independently audited shadow produce identical owner
objects and linked ELF. The strict full-image comparison accounts for 253
changed bytes with zero exclusions; only this function changes among 6,051
functions. All function addresses, 189,088 protected Game-data bytes, the
other 1,453 linked objects and the conversion rows remain unchanged. Three
old placeholder-only guard rows were replaced by the 28 target guards; all
other guard rows retain their prior content and order. The standalone tools
checkout's pre-existing changes were preserved.

A fresh production recount reports Game **3,763 / 4,843 (77.70%)**, total
**4,436 / 5,516 (80.42%)**, zero drift, and **112** further Game matches
required for 80% at the current denominator. The host port was not changed or
runtime-tested as part of this decompilation match.

The scoped graph refresh retained or relocated all 60,025 prior nodes, with
60,027 afterward and no out-of-scope removals or changes. Its fail-closed
path retained 31,816 existing nodes; it was not a full-corpus extraction.
