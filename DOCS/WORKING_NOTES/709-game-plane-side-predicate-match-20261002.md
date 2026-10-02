# Game plane-side predicate match

Date: 2026-10-02

`func_150A2E4C` replaces its zero-return placeholder with the 38-word retail
routine at `0x150A2E4C..0x150A2EE4`. The function converts three signed
halfword origin coordinates to floats, evaluates a plane-side expression, and
returns one when the result is non-positive.

The recovered plane record has signed origin coordinates at offsets
`0x00..0x04`, coefficient fields at `0x24`, `0x2C`, and `0x30`, and a scale at
`0x28`. After subtracting the first two origins, retail deliberately overwrites
the incoming fourth argument with the adjusted second value minus origin 2.
The resulting test is:

```text
(((value2 * coefficient2 + value0 * coefficient1) * scale)
    - value1 * coefficient0) <= 0.0f
```

Here `value2` denotes that overwritten local value, not the incoming fourth
argument. Preserving this unusual data flow is required for both semantics and
the retail instruction stream.

A volatile signed-halfword origin view recovers retail's opening load order.
Named coefficient temporaries then retain the semantic expression while
exposing the compiler's allocation boundary. Twenty expected-word guards
normalize only IDO's floating-point register allocation and instruction
schedule. The slice needs no checked insertions, omissions, relocations, or
compiler-profile override.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked and retail 152-byte spans are identical, with
SHA-256:

```text
993862e5dcb7c11feb945620c0129eb0b5a3fc73899448a96e8284657e434cf7
```

Game advances to `2,549 / 4,788 (53.24%)`, with 2,239 different C rows;
overall byte-exact C progress is `3,217 / 5,456 (58.96%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Resume the ordinary small-Game queue with 39-word `func_150BA424`, currently
at 34 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
