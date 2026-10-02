# Game angular motion-update family match

Date: 2026-10-02

`func_1511515C` and `func_151151FC` each occupy 40 words at
`0x1511515C..0x151151FC` and `0x151151FC..0x1511529C`. Their former
zero-return placeholders omitted two variants of the same angular integrator.
Each extracts the signed upper half of packed field `0x3C`, scales it through
`D_800BE9E4` and `0.00390625f`, stores the resulting component delta, applies
it to an angle, and wraps that angle into the 0-to-360-degree interval.

Both integrators emit directly from semantic C across their complete retail
slots. The established volatile store/reload shape preserves IDO's original
floating-point schedule. No expected-word guards or profile overrides are
required.

`func_15115EDC` occupies 35 words at `0x15115EDC..0x15115F68`. It snapshots
position fields `0x7C` and `0x80`, calls `func_15115E0C`, and, when the record
type at offset `0x84` is `0x4B`, extends each resulting displacement by a
factor of four. Its compiler-facing declaration places the snapshots in
`$f12` and `$f14`, matching retail's saved-register lifetime and arithmetic
schedule. The generated ownership slice combines a declaration contract that
does not describe the callee's eventual semantic pointer inputs; one
stale-checked word at offset `0x18` restores retail's record pointer in `$a1`
instead of typed C's `$a2`. All other 34 words emit directly from C.

The full linked matcher reports zero address drift and advances Game to
`2,512 / 4,788 (52.46%)`, with 2,276 different C rows. Overall byte-exact C
progress is `3,180 / 5,456 (58.28%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

Resume the ordinary small-Game queue with 33-word `func_151325C8`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.

Superseded resume note: `func_151325C8` and the following ordinary target
`func_151436B4` are complete in Working Note 679. Resume at 33-word
`func_1514795C`.
