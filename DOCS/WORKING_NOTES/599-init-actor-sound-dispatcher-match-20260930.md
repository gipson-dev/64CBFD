# Init actor sound dispatcher match

Date: 2026-09-30

`func_10010630` occupies 60 words and 240 bytes at
`0x10010630..0x10010720`. The former empty placeholder is replaced with the
recovered five-argument actor sound dispatcher. It returns immediately for an
inactive actor. A camera-owned actor uses `func_10010F30` with the low 16 bits
of the incoming value, fixed priority 64, and a mode derived from bits in
field `0x184`. Other actors submit their truncated position, sound parameters,
identity byte, actor pointer, and `func_1000EE70` refresh callback through
`func_1000FA64`.

The object remains on its established `-O2 -g3` profile. An isolated `-O1`
compile produces a 56-byte frame and no saved actor/value registers, while
`-O2` without `-g3` also fails to reproduce retail. Plain and `register`
actor/value aliases leave the same compiler allocation. The maintained body
therefore uses explicit ABI-width casts for the three coordinate truncations,
the low-half camera value, and callback address.

Retail retains the actor and shared value in `s0` and `s1`; the available IDO
profile retains only the actor and repeatedly reloads the value's argument
home. It also hoists the callback-address relocation pair ahead of the camera
branch. Fifty-four function- and offset-scoped entries in
`retail_word_patches.us.csv` normalize that closed allocation schedule. The
rows explicitly move both halves of `func_1000EE70` and the
`func_10010F30` call relocation, preserve the unchanged `func_1000FA64` call,
and fail if any expected compiler word or relocation drifts.

The focused object build, exhaustive stale-guard rebuild, authoritative
matcher, and direct section-span comparison pass. The linked Init section and
pristine image share SHA-256
`3bec2ba128af0a55c7bb606f06d3d3cca59c83994bae3efe841627a5854c2feb`
for the complete function.

The matcher advances to `3,098 / 5,457 (56.77%)` overall and
`415 / 488 (85.04%)` in Init, with zero address drift and 73 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
