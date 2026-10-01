# Init channel attachment match

Date: 2026-09-30

`func_1000B3D4` occupies 93 words and 372 bytes at
`0x1000B3D4..0x1000B548`. The former zero-return placeholder is replaced with
the recovered channel attachment and replacement routine.

When a parent is supplied, the routine compares its current child with the
incoming record. A conflicting child with the same identifier rejects the
incoming record; a different child is retired before the parent receives the
new pointer. Without a parent, the routine scans the three entries in
`D_800417B0`. It allocates an empty or inactive slot through `func_1000B2F4`,
or retires and replaces an idle child after repairing references through
`func_1000B294`. Allocation failure retires the incoming record.

Making the second parameter binding volatile recovers retail's incoming
argument home at `sp+0x3C`, while an explicit retained parent value preserves
the opening load lifetime. The recovered success edge jumps directly to the
loop increment, reproducing retail's branch topology. IDO then emits the exact
93-word extent, 56-byte frame, saved-register lifetime, and all control-flow
updates. Sixty-five words remain direct compiler output. Twenty-eight
stale-checked replacement guards normalize three closed register-allocation
cycles; no insertion, omission, or relocation rewrite is required.

The exhaustive shared-guard rebuild compiles and links every padded object
without a stale-guard failure. The authoritative matcher and direct 372-byte
section-span comparison pass. The linked and retail spans share SHA-256
`94732e1b11f4b548bf993a41315257f5d00810379afd568f162a694c10ada44f`.

The matcher advances to `3,114 / 5,457 (57.06%)` overall and
`431 / 488 (88.32%)` in Init, with zero address drift and 57 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
