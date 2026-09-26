# Game packed-byte writer match - 2026-09-25

## Result

All 17 words of `func_1502EA0C` now match retail across
`0x1502EA0C..0x1502EA50`. The linked matcher reports `2580 / 5484 (47.05%)`
overall and `2012 / 4795 (41.96%)` game, with one address-drift blocker and
2,903 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The existing C writes command bytes `4`, `0`, the sixth argument, and `0xFF`
at offsets `0xA4..0xA7`. It also packs arguments five through two into the
32-bit word at offset `0xA0`. The compiler-produced function already had the
correct 17-word extent, stack argument loads, stores, return, and behavior.

Retail interleaves the first two shifts between the initial byte stores and
the sixth-argument byte store, then uses a different temporary chain while
building the packed word. Explicit partial-value locals did not affect IDO's
output. Marking the destination volatile improved one store ordering but
increased the differing-word count and was rejected.

Ten function-specific expected-word guards restore the retail schedule and
temporary registers. This function has no relocations, inserted words, branch
changes, or source-level behavior substitutions.

The generated object and complete shared-CSV rebuild passed. The complete
68-byte ELF span at `0x6EA0C` and pristine retail span at
`conker/conker.us.bin+0x5BEBC` both have SHA-256
`99bafbd40986e990628a4a760a04fedeb2eabda80b5ecd0355427dd6a209a1aa`.
The patch table has 641 rows, zero duplicate keys, and ten target rows.

The `64CBFDOGL` sibling has no hand-maintained source or documentation
reference for this routine. Its generated recompilation artifacts do not need
a manual transplant. The dirty sibling tree was left untouched, and frozen
Release was not built or launched.

## Next boundary

Continue with 16-word `func_15033E84`, now the first game row with ten real
differences. Compare its linked-list search C, compact object, retail words,
and relocations before editing.
