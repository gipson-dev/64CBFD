# Game height-gated action selector byte match

Date: 2026-09-29

## Scope and behavior

`func_1506DC10` in `conker/src/game_981E0.c` occupies 37 words and 148 bytes
at `0x1506DC10..0x1506DCA4`. It compares the current actor's vertical position
with a threshold 60 units below `unk118`, while also recognizing the
`D_80099D50` sentinel. Below the gate it selects action `9`. Otherwise it uses
the low two bits of `func_150ADA20()` to select `0x8F`, `0x90`, `0x614`, or
`0x615`, then forwards the result and current actor to `func_15060A9C`.

## Source recovery

The previous signature accepted `s32 arg0` and initialized `value` from it.
Every control-flow path overwrote `value`, but the named parameter caused the
`-g3` IDO build to emit an argument-home store at `24(sp)`. That extra word
overflowed the retail slot even though the argument value was never read.

The routine is referenced only through the callback table in
`conker/asm/data/22AC10.rodata.s`. Recovering its no-argument callback
signature removes the debug home store. Declaring `value` without the false
initializer then emits the retail frame, branches, random selection, action
constants, calls, and delay slots.

## Compiler normalization

One non-relocating, stale-checked guard changes only the commutative
`c.eq.s` operand order from `$f0, $f10` to retail's `$f10, $f0`. Both operands,
the condition result, and the following branch are unchanged. No instruction
is inserted or omitted.

## Verification

- The focused `game_981E0` object accepts the new stale check.
- A complete guarded-object rebuild and ELF relink pass.
- The authoritative matcher reports `3,002 / 5,463 (54.95%)` overall and
  `2,424 / 4,789 (50.62%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 148 bytes.
- Both spans share SHA-256
  `21f8135feae7f64d4abfb9c2139abe072e30532dbfacc08743be5cf824bf03a8`.

## Resume boundary

Re-triage the next 30-difference Game bodies from the authoritative matcher.
`func_15079790` is the next known semantic candidate, but its 60-word span
should be compared against retail before editing. Keep `func_15015F40` parked
behind unresolved indirect-table ownership, `func_15022640` parked at its
measured IDO scheduling boundary, and handwritten `func_150A76F0` in the
assembly lane.
