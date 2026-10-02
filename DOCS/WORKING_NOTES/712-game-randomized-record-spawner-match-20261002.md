# Game randomized record spawner match

Date: 2026-10-02

`func_1500F378` replaces its zero-return placeholder with the 37-word retail
routine at `0x1500F378..0x1500F40C`. The function allocates and initializes a
small record using a randomized type and four caller-supplied values.

The function masks `func_150ADA20()` to seven bits, adds ten, and converts the
result to signed 16-bit form, producing the allocator's type argument in the
range `10..137`. It calls `func_151491F4` with the fixed remaining arguments
`1, -1, 1, 0, 10, 255, 0`.

When allocation succeeds, the returned storage is viewed through the existing
`struct04` contract. The four incoming 32-bit arguments are narrowed into the
signed halfword fields at offsets `0x28`, `0x2A`, `0x2C`, and `0x2E`, and byte
field `0x30` is set to one. This matches the established sibling pattern in
`func_15011B00`; the explicit `struct04 *` view cast also keeps IDO's allocator
return-type warning out of this translation unit.

The complete routine emits directly from semantic C with no expected-word
guards, checked insertions or omissions, relocations, or compiler-profile
override. The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with
zero address drift. The linked and retail 148-byte spans are identical, with
SHA-256:

```text
58ce88359e1cc127fddac7df5938a1831bd84945b6c3c364c972aae05a3489ce
```

Game advances to `2,552 / 4,788 (53.30%)`, with 2,236 different C rows;
overall byte-exact C progress is `3,220 / 5,456 (59.02%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Resume the ordinary small-Game queue with 37-word `func_1500F9D0`, currently
at 35 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
