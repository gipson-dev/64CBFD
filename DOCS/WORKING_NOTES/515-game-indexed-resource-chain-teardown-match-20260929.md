# Game indexed resource-chain teardown byte match

Date: 2026-09-29

## Scope and behavior

`func_150C0A48` in `conker/src/game/generated_EDE60.c` occupies 30 words and
120 bytes at `0x150C0A48..0x150C0AC0`. It follows a signed-index chain through
an eight-byte entry table owned at offset `0x40`. Each entry supplies a
resource pointer to `func_1516972C` and the next signed index at offset `4`;
`-1` terminates the chain.

## Source recovery

The previous body was a false zero-return placeholder. The recovered loop
retains the current index across the release call and reloads the owner's
table pointer before reading the next index, matching retail's observable
memory-access order.

An explicit integer-base address expression preserves retail's `$s1 + $s2`
operand order for both entry lookups. IDO reproduces the complete 48-byte
frame, five saved-register lifetimes, branch-likely loop, release-call delay
slot, table reload, and epilogue directly from semantic C. No expected-word
guards are used.

## Verification

- The focused `generated_EDE60` object reproduces all 30 retail words.
- The linked ELF and outer non-matching build pass.
- The authoritative matcher reports `3,019 / 5,463 (55.26%)` overall and
  `2,441 / 4,789 (50.97%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 120 linked bytes.
- Both spans share SHA-256
  `f4396ce3f3be8f1c133a1b70e34bd11fe5c83a539813888e6a90f801573fbddc`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_151001B4` as the next ordinary 31-word Game candidate. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten-assembly queue.
