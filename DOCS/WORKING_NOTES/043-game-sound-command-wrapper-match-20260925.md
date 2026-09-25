# Game sound-command wrapper match - 2026-09-25

## Result

`func_1509F6B0` is byte-exact across its complete 14-word linked extent
`0x1509F6B0..0x1509F6E8`. The fresh C-only matcher reports
`2560 / 5489 (46.64%)` overall and `1992 / 4800 (41.50%)` game. One init
function remains blocked by address drift; 2,928 total and 2,808 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained wrapper has the correct `s32`, `u16`, `s16`, and `u8`
incoming types and forwards them to `func_10010F30` in retail order. Its
frame, fifth stack argument, call relocation, and epilogue already matched.
Seven words differed only because IDO spilled `a2` and `a3`, reloaded signed
`a3`, then saved `ra` and spilled/reloaded `a1`; retail saves `ra`, spills all
three incoming arguments in order, then reloads `a1`, `a3`, and `a2` into the
callee's `a1`, `a2`, and `a3` positions.

Adding the exact five-argument `func_10010F30` prototype from `functions.h`
was tested. It changed scheduling but grew the compiled body from the retail
14 words to 15, so the generated-object padding gate correctly rejected it.
That experiment was reverted.

Seven expected-word-guarded, non-relocating normalizations preserve the
compact source and select retail's spill/reload schedule.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_CBDB0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all 14 retail words and the target is absent from
the non-exact list. The patch table has 526 rows and no duplicate
filename/function/offset keys. An independent comparison of the complete
56-byte linked ELF span at file offset `0xDF6B0` and retail ROM span at
`0xCCB60` produced SHA-256
`fb415b32c20c90d0dbde27e11417779ab59151fd495be7bb3609b0d1aa381ec1`
for both.

The `64CBFDOGL` sibling contains this symbol in generated recomp output,
symbol configuration, and a host-side script-sound test, but no hand-maintained
implementation. This IDO scheduling normalization therefore does not transfer
to host source. Its dirty worktree was left untouched, and its frozen Release
configuration was not built or launched.

## Next boundary

The next listed game target is 14-word `func_150C7930` with seven real
differences. Earlier investigation associates it with a retail computation
that the maintained C does not preserve; revalidate its ownership and exact
instruction shape before choosing source recovery or assembly restoration.
