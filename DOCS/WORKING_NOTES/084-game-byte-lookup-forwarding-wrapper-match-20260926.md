# Game byte lookup forwarding wrapper match - 2026-09-26

## Result

All 15 words of `func_15178E14` now match retail across
`0x15178E14..0x15178E50`. The linked matcher reports `2597 / 5484 (47.36%)`
overall and `2029 / 4795 (42.31%)` game, with one address-drift blocker and
2,886 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The wrapper narrows its incoming value to `u8`, passes that identifier to
`func_15178B98`, and forwards the returned record pointer to `func_15178DA4`.
The former K&R wrapper and unspecified-parameter placeholder definitions let
IDO keep the narrowed value in `a1` and move it into `a0` in the first call's
delay slot.

Giving the wrapper an ANSI `u8` parameter and giving its two local placeholder
definitions their real `u8` and word-sized argument contracts recovers retail
directly from C. IDO now spills the incoming `a0`, narrows through `t6`, moves
the byte back to `a0`, saves `ra`, leaves the first call delay slot empty, and
forwards `v0` in the second call delay slot. The frame, both call relocations,
epilogue, and three trailing extent nops all match without guarded rows.

The complete non-matching link and project tool checks passed. The linked span
at `conker/build/conker.us.bin+0x1A6294` and pristine retail span at
`conker/conker.us.bin+0x1A62C4` both have SHA-256
`a019d616adcd1685df8d90af91eb0c6da92463538aeeb540adf85fd4e9ccbbfd`.
The patch table remains at 711 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling exposes this function only through generated symbol
metadata. It has no hand-maintained host body requiring a transplant. Its
1,659 existing dirty entries were left untouched, and frozen Release was not
built, modified, or launched.

## Next boundary

Continue with 16-word `func_151ACA20`, the final game row with eleven real
differences. Compare its signed-halfword threshold, four-bit scaling and
sign-extension sequence, branch-likely byte load, conditional minimum store,
and return scheduling before editing.
