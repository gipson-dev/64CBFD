# Game path-count pointer contract match

Date: 2026-10-02

The shared declaration of `D_800D2108` incorrectly described its storage as
an inline byte array. Retail code loads a pointer from `D_800D2108` before
indexing the path-count table. Correcting the declaration to `u8 *` restores
that ownership contract and makes two existing Game routines byte-exact
directly from semantic C.

`func_150778F0` occupies the 46-word slot at
`0x150778F0..0x150779A8`. It reads the selected path count minus one, permits
object field `0x21F` to override that count, advances byte field `0x21E` by
signed step field `0x221`, wraps the result with the path count, and clamps it
to minimum field `0x220`.

`func_1507A528` occupies the 62-word slot at
`0x1507A528..0x1507A620`. Command mode zero assigns byte field `0x221`; mode
one negates it. Mode two selects either the explicit limit or the selected
path count minus one, reverses the signed step, applies command byte
`D_800D1893` according to the new direction, wraps field `0x21E` into range,
and stores the resulting byte.

Before the declaration correction, IDO treated the symbol address itself as
the table base. In `func_1507A528` that omitted retail's pointer load and
shifted the remaining register allocation, producing 34 real differences.
The pointer declaration naturally restores the missing load and the complete
downstream schedule in both routines. No expected-word guards or compiler
profile overrides are used.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked and retail spans are identical:

- `func_150778F0`, 184 bytes: SHA-256
  `5997b1de50ef57c77eb8f9661c572193e4b237de0d9e9cf0a10888c60501956a`
- `func_1507A528`, 248 bytes: SHA-256
  `008563b157539d36a3d872cb78a0ca356d22c5eb303d2deace35574a1e012a41`

Game advances to `2,548 / 4,788 (53.22%)`, with 2,240 different C rows;
overall byte-exact C progress is `3,216 / 5,456 (58.94%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

The same corrected declaration is used by `func_15075650`, but that larger
routine remains non-matching for independent control-flow and scheduling
reasons. No fresh gameplay run was performed.

Resume the ordinary small-Game queue with 38-word `func_150A2E4C`, currently
at 34 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
