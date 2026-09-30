# Game owner-payload object spawn byte match

Date: 2026-09-29

## Scope and behavior

`func_150BDE90` in `conker/src/game/generated_EB340.c` occupies 31 words and
124 bytes at `0x150BDE90..0x150BDF0C`. It builds an eight-byte payload from
the caller's owner pointer and a zero state halfword, creates a type-`0x12C`
object with subtype `0x4F`, and copies the payload to object offset `0x28`
when creation succeeds.

## Source recovery

The previous body was a false zero-return placeholder. A narrow local payload
type preserves the owner pointer, zero halfword, and retail's untouched two
padding bytes. The correct nine-argument `func_15149130` prototype also
preserves the byte narrowing of the second caller argument and the full-width
final argument.

IDO reproduces retail's 64-byte frame, incoming argument spills, local
payload stores, allocator-call schedule, null check, eight-byte `memcpy`, and
epilogue directly from semantic C. No expected-word guards are used.

## Verification

- The focused `generated_EB340` object reproduces all 31 retail words.
- The linked ELF and outer non-matching build pass.
- The authoritative matcher reports `3,018 / 5,463 (55.24%)` overall and
  `2,440 / 4,789 (50.95%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 124 linked bytes.
- Both spans share SHA-256
  `c1210a8e98cd676608cb4aa49a6c41cf1d50889ec535d5174e64d22d10e21275`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_150C0A48` as the next ordinary 30-word Game candidate. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten-assembly queue.
