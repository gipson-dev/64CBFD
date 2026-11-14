# Game ranged-effect callback direct match

Date: 2026-11-14. `func_151A9634` now emits all 128 retail words and
relocations directly from C, with no new guards. Its slot is
`0x151A9634..0x151A9834` (ROM `0x1D6AE4..0x1D6CE4`) in
`conker/src/game/generated_1D4E00.c`. The original 0x90-byte frame and
saved-register lifetime are preserved.

The callback reads randomized ranges from the record at actor offset 0x80.
It draws three floats, then three integers and an optional fourth integer.
The record flags select a fixed or randomized effect tag and a mode. Signed
halfword bounds feed unsigned remainders, followed by signed-halfword or
byte truncation for the helper arguments. A successful `func_1514B8E4`
result receives eight bytes at offset 0x160: a float, a signed halfword and
two retained stack bytes. The source intentionally leaves those last two
bytes uninitialized, as retail does. The typed `memcpy` declaration precedes
the owner's earlier calls; their compiled bodies remain unchanged.

`D_8008F970[1]` points to this callback. Sixteen cases execute the original
dispatch window in `func_151A8CEC`, including successful and failed modeled
allocations. Guest comparisons cover 800 bounded input cases per stream,
12 overlaps between the copy destination and actor fields or the source
packet, and 201 access prefixes. Retail, raw C and padded streams have
identical modeled machine state in the sampled cases. All 125 non-trap
instructions are visited; the three zero-divisor break instructions are
byte-exact but are not dynamically exercised.

Native 32-bit C passes 100 cases under six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. Seven altered
source controls are detected. Native inputs are typed, aligned and disjoint;
scripted random helpers update a separate seed, matching the real helpers'
write scope. Native checks inspect the six initialized packet bytes and
exclude the two indeterminate bytes. Guest-only helper mutations of record
fields and incoming argument homes do not establish portable C parity for
those mutations. The helpers are modeled, and `func_1514B8E4` remains a
production placeholder. These checks do not prove full caller/helper
execution, unrestricted aliases, zero-divisor behavior, hardware or gameplay.

Both padding implementations pass 12 GNU links across four independently
rebased symbol layouts. The other 22 owner functions and normalized constant
pools are unchanged, and the target compile has no diagnostics. Production
Make produces the independently predicted shadow ELF. The strict whole-image
audit accounts for 373 changed bytes with zero exclusions. All 6,051
function addresses and 189,088 protected Game-data bytes remain fixed.
Only the target owner changed among 698 frozen linked objects; the guard
and conversion manifests are unchanged.

Tools commit `c661112` retains the installed regression suite. It passes in
the mounted tools checkout and an
isolated sibling tools overlay. The sibling checkout's existing edits are
preserved, and `make tools-check` passes:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_ranged_effect_151a9634_installed -v
```

A scoped fail-closed Graphify refresh retained all 60,132 previous node IDs.
This was not a full-corpus re-extraction. The graph query located the source
placeholder; the caller and helper interfaces were established from retail
assembly and the linked artifact.

Fresh production recount: Game **3,796 / 4,843 (78.38%)**, total
**4,469 / 5,516 (81.02%)**, zero drift. At the current denominator,
**220** additional exact matches are needed to reach 85% total.
