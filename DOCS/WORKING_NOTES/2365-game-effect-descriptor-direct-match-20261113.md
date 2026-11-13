# Game randomized effect descriptor direct match

Date: 2026-11-13. `func_150B9D8C` in `generated_E5E90.c` now matches
retail directly across its 78-word executable body at
VA `0x150B9D8C..0x150B9EC4` and ROM `0xE723C..0xE7374`. Its three trailing
alignment words are outside that body. Instructions and relocation bindings
match without new guards; both independent padders emit the retail body.

When the signed selector at actor offset `0x98` is -1, the routine prepares
a 40-byte descriptor, makes three random draws and submits it to
`func_1513C4EC` with actor-derived coordinates and identity bytes. The
descriptor includes unwritten bytes that the factory may copy. The corrected
work-area layout and local declaration order place both saved random values,
the descriptor, saved registers and return address at the retail stack
offsets. Earlier variants did not preserve that layout for deliberately
overlapping actor and stack storage; see [Note 2343](2343-game-effect-descriptor-alias-screen-20261112.md).

Tools commit `e524aed` provides the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_effect_descriptor_150b9d8c_direct -v
```

The six direct checks passed before and after installation with mounted tools,
and with staged files and the sibling tools dependencies. They cover 72
ordinary guest cases, the original 18-word RNG in 48 bounded cases, 712
deliberate actor/stack-overlap cases per instruction stream, access-boundary
prefixes for four cases, and 12 GNU links across three address layouts.
Native 32-bit checks passed 16 cases each at `-O0`, `-O2` and `-O3` with
UBSan and six effective negative controls. The earlier five-test screen also
passes after installation. The factory is modeled in these checks; the RNG is
connected to its original instructions. The reference census did not identify
an original caller. Computed or external dispatch and full gameplay behavior
remain unproven; finite native checks exclude deliberately overlapping objects.

The Make-planned shadow and actual production object and ELF agree exactly.
The independently predicted image accounts for 242 changed bytes with zero
exclusions; only this body differs among 6,051 functions, all addresses remain
fixed, and all 189,088 protected Game-data bytes remain unchanged. The other
seven owner functions, constant pools, compiler diagnostics and 1,453 other
linked object hashes are unchanged. Project tool checks passed.

The production recount is Game **3,754 / 4,843 (77.51%)**, total
**4,427 / 5,516 (80.26%)**, zero drift, with **121** more Game matches
required for 80%.
