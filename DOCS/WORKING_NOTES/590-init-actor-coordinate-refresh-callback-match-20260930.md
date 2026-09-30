# Init actor-coordinate refresh callback match

Date: 2026-09-30

`func_1000EE70` occupies 52 words and 208 bytes at
`0x1000EE70..0x1000EF40`. It validates the actor referenced by a 48-byte
event record and the caller's enable word, then compares the actor's unique
identifier with the record's masked low-byte key.

For a matching active actor, the recovered C writes the actor's orientation
class to the caller's output word and truncates the actor's X, Y, and Z
coordinates into record halfwords at offsets `0x2`, `0x4`, and `0x6`. A
nonmatching actor falls back to the record handle-liveness query through
`func_1000F44C`; null actors, disabled callers, and live unmatched handles
return the retail failure result.

Thirty-four of the 52 words emit directly from semantic C. Eighteen
stale-checked guards preserve one closed compiler temporary-register rotation
across the state/key comparison, orientation extraction, output pointer, and
three coordinate conversions. The frame, branches, delay slots, call
relocation, and complete behavior emit directly; no relocation guards or
omitted words are present.

The focused object build, exhaustive guarded relink, authoritative matcher,
and direct section-span comparison pass. The linked Init section and pristine
image share SHA-256
`529b4111534c32467e43c8889c4f475252494d74e82022ca94bbcae6090cc1ad`
across all 208 bytes.

The matcher advances to `3,088 / 5,457 (56.59%)` overall and
`405 / 488 (82.99%)` in Init, with zero address drift and 83 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
