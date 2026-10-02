# Game indexed resource lazy-loader match

Date: 2026-10-02

`func_1503D774` replaces its zero-return placeholder with the 36-word retail
routine at `0x1503D774..0x1503D804`. Its first argument selects an entry in
the 187-pointer resource table `D_800D1C90`; the second argument is retained in
the retail function signature and argument home but is otherwise unused.

An already populated slot returns zero immediately. For a missing slot, the
function calls `func_1502B6BC` with its output word, controls `2` and `0`,
resource mode `2`, fixed kind `0x11`, and the incoming table index. A null
loader result clears the slot and returns two. A successful result is first
published as the returned wrapper and then replaced by that wrapper's first
`struct124 *`, leaving the table pointed at the resource payload and returning
zero.

The semantic compile recovers the complete frame, call contract, status paths,
and table writes. Six expected-word replacements restore retail's saved slot
location, post-call branch-delay schedule, direct `v0` publication, and the
early-exit displacement after omission. One checked omission removes IDO's
redundant copy of the loader result from `v0` to `a0`. No relocation-aware
rows, checked insertions, or compiler-profile override are required.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked and retail 144-byte spans are identical, with
SHA-256:

```text
bfcfc1059accaaa23866d1a6053f997357809baec37e285c8617cdeaf900818b
```

The patch audit reports seven rows for `func_1503D774`, including exactly one
checked omission, with no duplicate patch keys. Game advances to
`2,556 / 4,788 (53.38%)`, with 2,232 different C rows; overall byte-exact C
progress is `3,224 / 5,456 (59.09%)`. Init remains `487 / 487 (100.00%)` and
Debugger remains `181 / 181 (100.00%)`. `make tools-check` also passes. No
fresh gameplay run was performed.

Continued in
[Working Note 717](717-game-trailing-marked-record-compactor-match-20261002.md),
which matches `func_1503DDD0`. Resume the ordinary small-Game queue with
36-word `func_15042E3C`, currently at 35 real differences. Keep
`func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
