# Game delta-intensity limiter match

Date: 2026-10-02

`func_150BA424` replaces its zero-return placeholder with the 39-word retail
routine at `0x150BA424..0x150BA4C0`. It derives a byte intensity from a float
delta and a signed actor parameter, then publishes the smaller candidate.

The function subtracts float field `0x124` from field `0x38` and returns zero
when the result is negative. Otherwise it truncates the delta to an integer and
shifts it left by two. Independently, it reads signed halfword field `0x1C` and
shifts it left by four. Each candidate is capped at `0xFF` when it reaches or
exceeds `0x100`; negative values retain retail's signed comparison behavior.
The smaller candidate is stored to byte field `0x5C`.

Retail reloads that field as an unsigned byte, initializes the result to one,
and conditionally returns zero when the unsigned value is negative. Although
that check cannot fail, preserving its original result-local and early-return
shape is necessary for IDO to emit the final eight retail words. The complete
routine emits directly from semantic C with no expected-word guards, checked
insertions or omissions, relocations, or compiler-profile override.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked and retail 156-byte spans are identical, with
SHA-256:

```text
be3d8333e92bac19b5d23f1fb8dc50a3ea996b915e4dbc5516ded1aae9286aff
```

Game advances to `2,550 / 4,788 (53.26%)`, with 2,238 different C rows;
overall byte-exact C progress is `3,218 / 5,456 (58.98%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Resume the ordinary small-Game queue with 40-word `func_150CF0A0`, currently
at 34 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
