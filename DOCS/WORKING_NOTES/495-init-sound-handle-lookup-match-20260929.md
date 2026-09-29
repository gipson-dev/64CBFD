# Init sound-handle lookup byte match

Date: 2026-09-29

## Scope and behavior

`func_1000F4D8` in `conker/src/init_EB00.c` occupies 36 words and 144 bytes at
`0x1000F4D8..0x1000F568`. It normalizes the incoming 16-bit identifier to its
low fifteen bits, scans all sixteen twelve-byte records in `D_800425E0`, and
skips records without a live handle. For a matching masked record identifier,
it calls `func_100173C4` on the handle field and returns one on the first
successful validation; otherwise it returns zero after the full scan.

## Source recovery

The previous source initialized a separate `value` local from
`arg0 & 0x7FFF`. IDO then retained the narrowed argument and repeated its mask
inside the loop, displacing the complete retail schedule. Retail instead
narrows the incoming argument, copies that value, and applies the `0x7FFF`
mask once before loading the first record.

Updating `arg0` in place expresses that lifetime directly. IDO emits the
retail frame, saved registers, one-time mask, initial record load,
branch-likely pointer advances, loop-end comparison, call, and return paths
without expected-word guards. The object represents the end pointer as
`D_800425E0 + 0xC0`; it resolves to the retail `D_800426A0` address.

## Verification

- The focused `init_EB00` object rebuild passes.
- A complete ELF relink passes.
- The authoritative matcher reports `2,999 / 5,463 (54.90%)` overall and
  `397 / 493 (80.53%)` in Init, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 144 bytes.
- Both spans share SHA-256
  `e1997a581a20e13ffd2f3b88fb29e08ec757f0e79095e9bb50492b56928926ce`.
- Project tool checks and all 10 tool unit tests pass.

## Resume boundary

Continue with the next ordinary small C candidate from the authoritative
matcher queue. Keep `func_15015F40` parked behind its unresolved indirect-table
ownership and keep handwritten `func_150A76F0` in the assembly lane.
