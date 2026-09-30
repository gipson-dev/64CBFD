# Init handwritten osInvalDCache restoration

Date: 2026-09-30

`osInvalDCache` occupies 44 words and 176 bytes at
`0x10022D10..0x10022DC0`. The previous source was an empty C placeholder even
though the retail routine is handwritten assembly. It rejects nonpositive
sizes, falls back to a complete 8 KiB cache invalidation for large ranges,
handles unaligned starting and ending cache lines with hit writeback/invalidate
operations, and invalidates each aligned interior line. One trailing retail
padding word completes the slot.

The authoritative body from `asm/libultra/os/invaldcache.s` now lives behind
the dedicated `asm/nonmatchings/generated_invaldcache/osInvalDCache.s`
boundary. The empty C body remains disabled under `#if 0` only to document the
removed placeholder. The original `cache 0x15`, `cache 0x11`, and `cache 0x01`
instructions are handwritten operations and are not modeled through synthetic
C or expected-word guards.

The focused generated-slice build, complete relink, refreshed progress
inventory, authoritative matcher, and direct span comparison pass. The built
Init section and pristine image share SHA-256
`7ea4c6bffed307fe915ab8ef0ae37d86482e17b132eb99598f82ad5cbca40a71`
across all 176 bytes.

The row is now correctly classified as assembly. The matcher reports
`3,081 / 5,459 (56.44%)` exact C rows overall and
`398 / 490 (81.22%)` in Init, with zero address drift and 92 genuinely
different Init C rows.

Resume with the remaining Init queue after the parked `func_1000FF90`.
