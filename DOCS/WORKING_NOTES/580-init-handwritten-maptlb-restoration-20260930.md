# Init handwritten osMapTLB restoration

Date: 2026-09-30

`osMapTLB` occupies 48 words and 192 bytes at
`0x10026310..0x100263D0`. The previous source was an empty C placeholder even
though the retail routine is handwritten assembly. It saves EntryHi, installs
the requested TLB index and page mask, constructs both EntryLo values, writes
the entry with `tlbwi`, observes the original hazard nops, restores EntryHi,
and returns. Three trailing retail padding words complete the slot.

The authoritative body from `asm/libultra/os/maptlb.s` now lives behind the
dedicated `asm/nonmatchings/generated_maptlb/osMapTLB.s` boundary. The empty C
body remains disabled under `#if 0` only to document the removed placeholder.
CP0 access and `tlbwi` are intentional handwritten operations and are not
modeled through synthetic C or expected-word guards.

The focused generated-slice build, complete relink, refreshed progress
inventory, authoritative matcher, and direct span comparison pass. The built
Init section and pristine image share SHA-256
`df58b390004db1a7de5265449eafe8115ecaf81acad24b5471290157b28cc85e`
across all 192 bytes.

The row is now correctly classified as assembly. The matcher reports
`3,081 / 5,460 (56.43%)` exact C rows overall and
`398 / 491 (81.06%)` in Init, with zero address drift and 93 genuinely
different Init C rows.

Resume with the remaining low-level Init primitives, beginning with the
smallest unparked row after `func_1000FF90`.
