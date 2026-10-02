# Game color-driver callback family match

Date: 2026-10-02

Game `func_150D149C` occupies the 37-word slot at
`0x150D149C..0x150D1530`; `func_150D1B40` occupies the 36-word slot at
`0x150D1B40..0x150D1BD0`. Both callbacks pass float fields at offsets `0x30`,
`0x2C`, and `0x28` through `func_151467A4` with scale `10.0f`. The first uses
the range `50.0f`, `100.0f`, and `123.0f` with `D_800A08C0`; the second uses
`86.0f`, `170.0f`, and `255.0f` with `D_800A08E0`.

After the driver call, each callback truncates the resulting float at `0x28`
and passes it to `func_1515D4D4` as the first color component. Bytes one and
two from `D_800DCD20` remain the second and third components, and the fourth
argument is zero.

The first semantic form used a direct `arg0 + 0x28` expression before and
after the driver call. It had the retail executable length but reloaded the
base pointer after the call. Naming the derived float pointer reproduces
retail's duplicate stores at stack offsets `0x1C` and `0x28` and its `v0`
reload. Declaring the color publisher locally with full-width integer channels
is also required: the narrower shared-header prototype makes IDO emit guarded
float-to-unsigned conversions, while retail uses one plain `trunc.w.s`.

All words in both retail slots emit directly from C without expected-word
guards or compiler profile overrides. This includes `func_150D149C`'s trailing
alignment word supplied by generated-slice padding. Both 48-byte frames,
constants, global relocations, derived-pointer lifetime, calls, conversion,
color loads, epilogues, and delay slots match in the focused objects and final
linked image.

The incremental generated-object builds, full link, and linked matcher
complete with zero address drift. Game advances to
`2,540 / 4,788 (53.05%)`, with 2,248 different C rows; overall byte-exact C
progress is `3,208 / 5,456 (58.80%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object comparison, full-link, and linked-word comparison evidence.

Resume the ordinary small-Game queue with 36-word `func_1518BCD0`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
