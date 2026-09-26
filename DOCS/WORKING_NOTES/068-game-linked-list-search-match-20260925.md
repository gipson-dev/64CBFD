# Game linked-list search match - 2026-09-25

## Result

All 16 words of `func_15033E84` now match retail across
`0x15033E84..0x15033EC4`. The linked matcher reports `2581 / 5484 (47.06%)`
overall and `2013 / 4795 (41.98%)` game, with one address-drift blocker and
2,902 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function searches the list rooted at `D_800C3EE0` for a node whose first
byte matches input byte `0x3B`, returning that node or zero. The prior C was
behaviorally correct but loaded `node->next` only after a failed comparison.
IDO consequently used likely loop branches and initialized the zero result at
entry, producing ten reported differences.

Loading the next pointer before the comparison recovers retail's `v0`
lifetime. Expressing the loop test as `(node = next) != 0` then produces the
ordinary `bne` comparison, `bnez v0` loop branch, and `move v1, v0` delay-slot
update. The exact 16-word extent and both `D_800C3EE0` relocations now come
directly from C. No guarded patch rows are used by this function.

The generated object and full linked build passed. The complete 64-byte ELF
span at `0x73E84` and pristine retail span at
`conker/conker.us.bin+0x61334` both have SHA-256
`944012697ea2666086f345f59f6c1cd8f750eb86b20835a40aa096bbae61d6c8`.
The patch table remains at 641 rows, has zero duplicate keys, and has zero rows
for this function.

The `64CBFDOGL` sibling has no hand-maintained source or documentation
reference for this routine. Its generated recompilation artifacts do not need
a manual transplant. The dirty sibling tree was left untouched, and frozen
Release was not built or launched.

## Next boundary

Continue with 12-word `func_15094F40`, now the first game row with ten real
differences. Compare its display-list cursor C, compact object, retail words,
and relocations before editing.
