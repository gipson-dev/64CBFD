# Game owner-identity object spawn byte match

Date: 2026-09-29

## Scope and behavior

`func_151001B4` in `conker/src/game/generated_12D630.c` occupies 31 words and
124 bytes at `0x151001B4..0x15100230`. It builds an eight-byte payload from
the caller pointer, the caller's identity byte at offset `0x3B`, and a zero
state halfword. It creates a type-`0x12C`, subtype-`0x4E` object and copies
the payload to object offset `0x28` when creation succeeds.

## Source recovery

The previous body was a false zero-return placeholder. A narrow local payload
type preserves the pointer, identity byte, untouched padding byte, and state
halfword. The recovered nine-argument `func_15149130` declaration preserves
the allocator ABI and fixed callback/category arguments.

IDO reproduces retail's 64-byte frame, incoming argument spill, payload
stores, nine allocator arguments, delay-slot identity-byte store, null check,
eight-byte `memcpy`, and epilogue directly from semantic C. No expected-word
guards are used.

## Verification

- The focused `generated_12D630` object reproduces all 31 retail words.
- The linked ELF and outer non-matching build pass.
- The authoritative matcher reports `3,020 / 5,463 (55.28%)` overall and
  `2,442 / 4,789 (50.99%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 124 linked bytes.
- Both spans share SHA-256
  `560751d5b99b1ad36a492f2f4100f5d38e2f0ca2ca844e71cd9f1cee93161a04`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_15106E78` as the next ordinary 32-word Game candidate. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten-assembly queue.
