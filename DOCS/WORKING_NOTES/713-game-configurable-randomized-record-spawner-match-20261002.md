# Game configurable randomized record spawner match

Date: 2026-10-02

`func_1500F9D0` replaces its zero-return placeholder with the 37-word retail
routine at `0x1500F9D0..0x1500FA64`. It is the five-argument variant of the
randomized record spawner recovered in `func_1500F378`.

The function masks `func_150ADA20()` to seven bits, adds ten, converts the
result to signed 16-bit form, and calls `func_151491F4` with fixed remaining
arguments `1, -1, 1, 0, 10, 255, 0`. On successful allocation, the first four
incoming values are narrowed into signed halfword fields `0x28..0x2E`.

Unlike `func_1500F378`, which forces byte field `0x30` to one, this variant
loads its fifth stack argument and stores that value to field `0x30`. The body
matches the established `func_1500EB30` family contract and uses an explicit
`struct04 *` view of the allocator result.

The complete routine emits directly from semantic C with no expected-word
guards, checked insertions or omissions, relocations, or compiler-profile
override. The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with
zero address drift. The linked and retail 148-byte spans are identical, with
SHA-256:

```text
b63c5d3871e70fcec46244df5a31f699652cb964e5ded12277c112e7fd8678d5
```

Game advances to `2,553 / 4,788 (53.32%)`, with 2,235 different C rows;
overall byte-exact C progress is `3,221 / 5,456 (59.04%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Resume the ordinary small-Game queue with 40-word `func_1502FD70`, currently
at 35 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
