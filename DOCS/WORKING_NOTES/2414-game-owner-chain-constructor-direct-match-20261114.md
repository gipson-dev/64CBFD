# Game owner-chain constructor direct match

Date: 2026-11-14. `func_150C0AC0` now emits all 94 retail instructions
directly from C at `0x150C0AC0..0x150C0C38` (ROM `0xEDF70..0xEE0E8`). The
recovered body replaces a zero-return placeholder in
`conker/src/game/generated_EDE60.c`; it requires no word guards.

The routine checks the descriptor's mode and, when required, its resource
pointer and first word. It requests a type-`0x25` allocation sized from the
descriptor's signed count, copies 28 descriptor bytes into the new record,
initializes two position components and the record's chain heads, and links
the free entries. Allocation or prerequisite failure returns null. The
original `func_1514F5CC` constructs a descriptor and calls it with slot
`0xFF` and context `1`.

A local struct keeps the allocation size and returned pointer in the retail
stack order. An earlier private candidate swapped those two slots: a descriptor
pointing into the callee's own frame made that candidate diverge from retail.
The final direct C emits the retail words and relocations, and the same
private-stack case now agrees through the modeled unmapped-read boundary.
Both padding paths and 12 GNU links over four symbol layouts match retail; all
six neighboring functions and normalized constant pools remain unchanged.

The retail, raw C and padded streams agreed with an independent model in 736
cases each, covering signed counts, both modes, missing resources, allocation
failure, byte-sized slots and descriptor changes made by the modeled
allocator. Another 96 cases overlap the descriptor and allocated record using
a forward-byte copy provider. In 192 cases the original 11-instruction
`memcpy` is connected instead, including overlaps; 493 modeled fault
prefixes compare complete machine state. Forty-two cases execute the original
26-instruction `func_1514F5CC` caller and original copy routine with the
allocator modeled.

The C passed 644 native 32-bit cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan; seven altered
source controls were rejected in both aliasing modes. Native cases use
non-overlapping copy buffers. Guest overlap results describe the original
byte-copy implementation, not a general claim that overlapping `memcpy` is
defined by C. The modeled allocator and bounded checks do not establish
complete allocator, hardware, renderer or gameplay behavior.

The actual production Make rebuild is byte-identical to the independently
predicted shadow ELF. The strict whole-image audit accounts for all 279 changed
bytes with zero exclusions; all 6,051 function addresses and 189,088 protected
Game-data bytes remain fixed. Only `generated_EDE60.c.o` changed among the 698
frozen linked objects. The guard manifest and conversion CSV are unchanged.
A scoped, fail-closed Graphify refresh retained all 60,115 existing node IDs;
it was not a full-corpus re-extraction.

Tools commit `46e223d` retains the fingerprinted pre-install screen and
installed regression tests. The pre-install screen is bound to its original
inputs and is not a test of the installed checkout. For the installed checkout:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_owner_chain_create_150c0ac0_installed -v
```

Both installed tests passed in the mounted tools checkout and an isolated
sibling overlay, with no skips; `make tools-check` passed. The sibling tools
checkout's prior dirty paths were preserved.

Fresh production recount: Game **3,791 / 4,843 (78.28%)**, total
**4,464 / 5,516 (80.93%)**, zero drift. **84** more Game matches are needed
for 80% at the current denominator.
