# Game global mode-state updater byte match

Date: 2026-09-30

`func_151D66F0` occupies 34 words and 136 bytes at
`0x151D66F0..0x151D6778`. When global state `D_800BE9F0` is six and the
availability byte `D_80038080` is clear, it returns without changing state.
Otherwise a zero mode argument forces the selector to zero, and the resulting
selector/mode pair is written to `D_800BE574` and `D_800BE575`.

Disabling the selector also checks the retained resource in `D_800BE570`. A
non-null resource is released through `func_100043B4(resource, 3)` and the
global is cleared. Keeping that cleanup as a second condition after the paired
byte stores recovers retail's shared control-flow join and delay-slot layout.
Using full-width arguments preserves the incoming `a0` and `a1` lifetimes;
the byte globals provide the intended narrowing at their stores.

All 34 words emit directly from semantic C. The exact output includes the
mode-6 early branch, branch-likely return, selector normalization, both byte
stores, retained-resource call and clear, all five global relocation pairs,
and the shared epilogue. No expected-word guards are required.

The focused object, complete replacement link, outer `NON_MATCHING=1` ROM
build, project tool checks, whitespace check, and authoritative matcher pass.
The linked ELF and pristine decompressed retail spans share SHA-256
`891d28f56a54c034702efd5cd9fae345a6402c9b469fc259ab59040be46ca8a7`.
The matcher advances exactly one row to `3,069 / 5,462 (56.19%)` overall and
`2,490 / 4,788 (52.01%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Review
48-word Init `__osProbeTLB`, the next matcher row, for original handwritten
CP0/TLB ownership. If it remains assembly-owned, resume with 44-word Game
`func_15013D38`, the next ordinary C row.
