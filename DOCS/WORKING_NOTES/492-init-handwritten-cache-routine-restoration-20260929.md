# Init handwritten cache routine restoration

Date: 2026-09-29

## Scope and ownership

Two libultra cache-maintenance routines were represented by empty C
placeholders even though preserved retail assembly listings already identified
them as handwritten:

- `osInvalICache` at `0x10022C90..0x10022D10`, 32 words / 128 bytes.
- `osWritebackDCache` at `0x10023D20..0x10023DA0`, 32 words / 128 bytes.

Both are restored through body-only `GLOBAL_ASM` sources under their generated
slice directories. The complete reference listings remain under
`conker/asm/libultra/os/`.

## Behavior

Both routines return immediately for nonpositive lengths, reject wrapped
address ranges, align the start and end to the appropriate cache-line size,
and walk the requested range with explicit branch-delay updates. Requests at
least as large as the corresponding cache instead walk the full KSEG0 cache:

- `osInvalICache` uses 32-byte lines, a 16 KiB threshold, hit invalidate
  opcode `0x10`, and index invalidate opcode `0x00`.
- `osWritebackDCache` uses 16-byte lines, an 8 KiB threshold, hit writeback
  opcode `0x19`, and index writeback-invalidate opcode `0x01`.

These primary-cache instructions and scheduling contracts are handwritten
assembly concerns, not ordinary compiler-generated C.

## Verification

- Both focused objects reproduce all 32 retail words, including three trailing
  extent-padding words each.
- The complete ELF relinks and the matcher reclassifies both rows as assembly
  with zero address drift.
- Direct linked comparison reports zero differences across both 128-byte
  spans.
- `osInvalICache` shares SHA-256
  `cf9ac7a3378e8d2013f33517eebd339955e401c76380ec29ca56152a34f0040d`.
- `osWritebackDCache` shares SHA-256
  `21514538b715f668861f169883c91749feb94cb501d5dfd9a24b67f782fa1b69`.
- The authoritative matcher reports `2,996 / 5,463 (54.84%)` overall and
  `395 / 493 (80.12%)` in Init, with zero address-drift rows.

## Resume boundary

The paired cache routines and `osWritebackDCacheAll` now consistently retain
handwritten assembly ownership. Continue with an ordinary small Game or Init
candidate; do not convert primary-cache or control-register instruction
routines into synthetic C placeholders.
