# Game actor extent callback direct match

Date: 2026-11-13. `func_15149A94` in `generated_176A00.c` replaces a
zero-return placeholder. Its 88-word body at VA `0x15149A94..0x15149BF4` /
ROM `0x176F44..0x1770A4` emits directly from C with its original six
relocations and no word guards. Both object padders reproduce the assembled
retail body; the other 35 owner functions, normalized constant pools and
compiler diagnostics are unchanged.

The callback moves the two float fields at `+0x2C` and `+0x30` toward
targets at `+0x118` and `+0x130`, using the scale at `+0x154`, unless their
corresponding flag bits are already set. It sets each flag once the updated
field exceeds its target multiplied by the relevant retail constant. Once
both transitions are complete, it calls `func_1513F680` with effect state 13.
Independently, a signed timer below 5 causes another helper call, a timer
reset to 100 and a clear of bit 0 at `+0x58`. The helper writes the four
bytes at `+0x70..+0x73`; the callback reloads fields after the first call.
The description identifies observed fields, not a fully established gameplay
meaning.

The pointer is entry 14 in `D_80089D60`, and the original
`func_1513CFE4` dispatcher window at `0x1513D070..0x1513D0A8` passes the
record and checks the integer return. The complete dispatcher and any other
computed or external callers are not newly qualified by this window test.

Tools commit `ab35dd5` provides the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_extent_15149a94_match -v
```

An independent guest model passed 864 cases per stream across retail, raw C
and both padded streams, including all flag combinations, signed timer
boundaries, both transition branches and modeled helper mutations. The
original table-dispatch window passed 128 cases per stream. Stack-overlap
fixtures and injected memory-access prefixes agreed across the four emitted
streams. Native 32-bit execution passed the same 864 defined-domain cases at
each of `-O0`, `-O2` and `-O3`, with UBSan and five effective negative
controls. Twelve GNU links across three symbol layouts verified the original
bindings. Helpers are modeled in these checks; exceptional float behavior,
complete callers, hardware faults and live gameplay are not established.
The focused suite passed in the mounted tools checkout and with staged sibling
dependencies; the sibling's pre-existing changes were preserved. Eleven
padder checks and the project tools check also passed.

The production Make owner and linked ELF equal the independently audited
shadow. The strict image comparison accounts for 303 changed bytes with zero
exclusions, including closed symbol-metadata reorderings. Only this body
changes among 6,051 functions, all function addresses remain fixed, and all
189,088 protected Game-data bytes are unchanged. The other 1,453 linked
objects are unchanged. No guard or conversion-layout rows were added.

A fresh production recount reports Game **3,757 / 4,843 (77.58%)**, total
**4,430 / 5,516 (80.31%)**, zero drift, and **118** further Game matches
required for 80% at the current denominator.

The scoped graph refresh retained or relocated all 60,002 prior nodes, with
60,004 afterward and no out-of-scope removals or changes. Its fail-closed
path retained 31,816 existing nodes; it was not a full-corpus extraction.
