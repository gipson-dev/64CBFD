# Init actor event/audio dispatcher match

Date: 2026-10-01

`func_1000EFB4` occupies 125 words and 500 bytes at
`0x1000EFB4..0x1000F1A8`. The former implementation returned zero. Its
recovered seven-argument callback signature includes two unused scalar
arguments while retaining the actor record, active value, event context,
result output, and trailing event selector used by the retail body.

The routine first requires an actor at `arg0->unk18` and a nonzero value at
`arg2`. For an actor with a nonzero interaction state, it scans the terminated
`u16` ID list at `arg0->unk1C`. An ID match, or a clear low policy bit in
`arg0->unk10`, writes the packed actor state to `arg5`, truncates the actor's
three floating-point coordinates into the callback record, and returns zero.

If no actor is accepted, event `0xCA` submits sound `0xCB`. Events `0x2CF` and
`0x2D2` submit sounds `0x2D7` and `0x2DA` respectively, then submit one of
three sounds beginning at `0x2EB` using the retail unsigned remainder. These
fallback paths return one.

Separating the two opening failure gates into their shared return path and
comparing the actor ID directly recovered retail's branch-likely layout and
125-word size. Reading the event selector directly allowed IDO to reuse the
retail register across all three comparisons. The complete function emits
directly from semantic C with no retail word guards.

The complete ELF link passed. The authoritative matcher no longer lists
`func_1000EFB4`; direct comparison of all 500 bytes reports zero differences,
and the linked and retail spans share SHA-256
`0835e229b55c402d6fac8e84fe5249cf3549d000c72e31a961e5247a09a77c09`.
Project tool checks pass. The focused unit suite passes all 10 tests.

The matcher advances to `3,129 / 5,457 (57.34%)` overall and
`446 / 488 (91.39%)` in Init, with zero address drift and 42 genuinely
different Init C rows.
