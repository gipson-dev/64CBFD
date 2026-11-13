# Game coordinate-table initializer match

Date: 2026-11-13. `func_1512ABF8` in `generated_157840.c` replaces a
zero-return placeholder. Its 87-word body occupies VA
`0x1512ABF8..0x1512AD54` / ROM `0x1580A8..0x158204`. Semantic C emits
81 retail words in the original positions; six relocation-aware guards
restore the remaining setup schedule and equivalent branch operand order.
Both object padders reproduce the complete assembled retail body. The other
14 owner functions, normalized constant pools and compiler diagnostics are
unchanged.

The function copies each of four eight-byte coordinate presets into each of
four output groups. When the player count is 1 through 3 it scales the first
two signed halfwords by one half; modes 27 and 30 apply a further three-quarter
scale. Each scaling step truncates before the next. The last two halfwords are
copied unchanged. Finally it clears the separate 304-byte state block through
`bzero`. Field names describe the observed coordinates rather than a complete
gameplay identification.

The original `func_15005290` call window at `0x15005440..0x15005448` invokes
this initializer with no arguments and ignores its return. The tests exercise
that bounded window; they do not qualify the complete parent or exclude other
computed callers.

Tools commit `86554bf` provides the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_coordinate_table_1512abf8_match -v
```

An independent guest model passed 56 cases per stream across retail, raw C and
both padded bodies, covering player-count boundaries, both special modes,
signed coordinate extremes and the modeled clear operation. The original call
window passed 40 cases per stream. Sampled access-fault prefixes agree across
retail and the two guarded streams. Raw C reads the two fixed globals in the
opposite order; the guards restore retail's order, so the raw access trace is
not claimed identical. Native 32-bit execution passed 56 defined-domain cases
each at `-O0`, `-O2` and `-O3`, with UBSan and six effective negative
controls. Twelve GNU links across three layouts verified the rebased words and
bindings. These checks do not establish complete `bzero` implementation,
portable C fault semantics, hardware behavior or live gameplay. The focused
suite passed in the mounted tools checkout and with staged sibling
dependencies; the sibling's pre-existing changes were preserved. The project
tools check passed.

The production Make owner and linked ELF equal the independently audited
shadow. The strict full-image comparison accounts for 265 changed bytes with
zero exclusions; only this body changes among 6,051 functions. All function
addresses and 189,088 protected Game-data bytes are unchanged, as are the
other 1,453 linked objects and conversion rows. Six checked guard rows were
appended to the existing manifest; no layout rows changed.

A fresh production recount reports Game **3,759 / 4,843 (77.62%)**, total
**4,432 / 5,516 (80.35%)**, zero drift, and **116** further Game matches
required for 80% at the current denominator.

The scoped graph refresh retained or relocated all 60,010 prior nodes, with
60,012 afterward and no out-of-scope removals or changes. Its fail-closed
path retained 31,816 existing nodes; it was not a full-corpus extraction.
