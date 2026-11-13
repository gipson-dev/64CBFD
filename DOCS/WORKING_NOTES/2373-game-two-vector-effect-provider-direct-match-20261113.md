# Two-vector effect provider direct C match

Date: 2026-11-13. `func_15160CDC` in `game_18D770.c` replaces a zero-return
placeholder. All 85 words at VA `0x15160CDC..0x15160E30` / ROM
`0x18E18C..0x18E2E0` emit directly from C with the original frame and
relocations; no word guards were added. Both object padders reproduce the
assembled retail body. The other 77 functions in its owner, normalized
constant pools and compiler diagnostics are unchanged.

The provider returns null for a null owner. Otherwise it snapshots the
owner pointer and identity, two supplied three-float vectors, a scale and
two flag inputs into a 40-byte payload. It constructs the original header
and zeroed argument block, calls `func_151602C0`, and copies the payload into
the returned object only on allocation success. The payload's two unwritten
padding regions are preserved rather than initialized. The factory and copy
helper are bounded by the tests below; their complete behavior is not newly
qualified here.

The existing `func_151BC074` caller used a conflicting declaration for this
provider. Its declaration now uses the recovered pointer, byte, halfword and
return types; its two three-word data symbols are declared as vectors. All
57 functions in that caller owner, including `func_151BC074`, compile and
pad identically to the baseline. Its original non-null caller window was
tested connected to the retail and C provider bodies. The two existing
`generated_179F30.c` callers already use a compatible interface; their earlier
bounded original-provider evidence is in [Note 1787](1787-two-vector-effect-match-20261028.md).

Tools commits `01312ed` and `bb71a57` provide the reproducible checks and
track the final source comment:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_two_vector_provider_15160cdc_match -v
```

An independent guest model passed 576 cases per stream across retail, raw C
and both padded bodies, visiting every retail instruction. Cases cover null
owners, allocation success and failure, signed lifetime boundaries, flag
bytes, allocator mutation and output aliasing the owner. Vector/stack overlap
fixtures, access-fault prefixes, and the original caller window were checked
across the same streams. Native 32-bit execution passed 576 cases each at
`-O0`, `-O2` and `-O3`, with UBSan and six effective negative controls.
Twelve GNU links across three layouts verified the original helper bindings.
These checks do not establish complete allocator behavior, portable C fault
semantics, hardware behavior or live gameplay. The focused suite passed in the
mounted tools checkout and with staged sibling dependencies; the sibling's
pre-existing changes were preserved. The project tools check also passed.

The production Make owner objects and linked ELF equal the independently
audited shadow. The strict full-image comparison accounts for 243 changed
bytes with zero exclusions; only this body changes among 6,051 functions.
All function addresses and 189,088 protected Game-data bytes are unchanged,
as are the other 1,452 linked objects and conversion rows. No new guards or
layout rows were required.

A fresh production recount reports Game **3,758 / 4,843 (77.60%)**, total
**4,431 / 5,516 (80.33%)**, zero drift, and **117** further Game matches
required for 80% at the current denominator.

The scoped graph refresh retained or relocated all 60,004 prior nodes, with
60,010 afterward and no out-of-scope removals or changes. Its fail-closed
path retained 31,816 existing nodes; it was not a full-corpus extraction.
