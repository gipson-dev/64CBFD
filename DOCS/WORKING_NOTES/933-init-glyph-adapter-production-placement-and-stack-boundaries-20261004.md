# Init Glyph Adapter Production Placement And Stack Boundaries

Date: 2026-10-04. Starting HEAD: `5a0e86d3`.

## Production Adoption Decision

Note 932's adapter is a qualified experimental interface, not an adoptable
production conversion. New boundary tests pin two concrete restrictions:
the independently linked C address is occupied retail code, and diagnostic
formatter callers execute under two different stack regimes. Do not promote
based on the later overlay stack's containment alone.

## Code Placement

The current structured Init inventory assigns experimental address range
`0x10009000..0x10009080` to C `func_10008F90`, whose complete slot is
`0x10008F90..0x100093CC` (1,084 bytes). Local retail bytes in the experimental
range are nonzero. It is not vacant executable space, and installing the
candidate there would overwrite the recovered audio bootstrap.

The original glyph slot `0x10007D28..0x10007DA0` is exactly 120 bytes. It is
immediately followed by twelve-byte syscall wrapper `func_10007DA0` and then
`func_10007DAC` at `0x10007DAC`. There is no adjacent free extension into
which the additional 128 allocated C bytes can be placed without moving or
replacing existing code. These are live inventory/retail placement checks,
not a newly linked whole-section match or a survey of every possible slot.

## Two Diagnostic Stack Regimes

All fifteen direct formatter calls inside `func_10007DAC` are pinned to
their original instruction words. Nine occur before the overlay SP setup:

```text
0x10007E18 0x10007E3C 0x10007E4C 0x10007E5C 0x10007E6C
0x10007E7C 0x10007E8C 0x10007EA0 0x10007EC0
```

The preceding body saves the incoming SP globally but does not change it.
These formatter calls inherit the diagnostic entry stack. No complete
reservation for the proposed 56-byte adapter frame on that stack is proved.
The early high-position return path also renders before selecting an overlay
stack, so qualification cannot be restricted to the main overlay path.

The instruction at `0x10007F00` sets SP to the selected overlay base plus
`0x5958`. Six direct formatter calls occur afterward:

```text
0x10007F0C 0x10007F60 0x10007FAC
0x10008048 0x1000805C 0x100080E8
```

The body later reserves/releases 24 bytes for `osMapTLB`, and finally
restores the saved original SP. The added glyph frame is a separate lifetime;
those existing argument stores do not prove all required new frame ownership.

## Overlay Containment Measurement

Executing the existing retail placement slice for eight 0x2000-aligned pool
residues confirms overlay SP `base + 0x5958`. The adapter's frame would start
at `base + 0x5920`. Debugger DMA ends at `base + 0x4960`, leaving **0xFC0 /
4,032 bytes** between that payload endpoint and the added frame's low bound.
For all direct positive pool counts 107..362, the full hypothetical frame
is inside the modeled successfully allocated page pool.

This is containment relative to pool and DMA boundaries, not a private stack
allocation or lifetime proof. It does not cover arbitrary failed/corrupt
allocations, other live debugger storage, earlier inherited SP, hardware
effects or arbitrary stack/framebuffer aliasing. Placement fixtures perform
arithmetic only and make no pool writes.

## Fresh Verification

`tools/tests/test_init_glyph_adoption_boundaries.py` adds four tests for the
fifteen call sites/stack split, conditional overlay containment, occupied
experimental C address and adjacent slot ownership.

```sh
python3 -m unittest tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter tools.tests.test_init_diagnostic_storage tools.tests.test_init_syscall_fault_route -q -f
```

All twenty tests pass in 8.779 seconds, no skips. Adapter execution is still
independently linked in fixtures; no production adoption, guest hardware run,
full ROM build or whole-section byte comparison is claimed.

## Next Action

Keep the adapter experimental. Any adoption path must account for all fifteen
diagnostic formatter sites and real stack lifetimes, not just the six after
overlay setup. For text fitting, pursue a justified whole-connected layout
or a demonstrably owned location; do not overwrite the occupied experimental
address, consume neighboring syscall/diagnostic code, or assume zero bytes
elsewhere are unowned space. Current tests make those adoption boundaries
reproducible while preserving the recovered semantic C and ABI experiments.

Production Init remains 492 C / 47 assembly routines. Production source,
profiles, word guards and README aggregates are unchanged. No sibling build,
Release change or push.
