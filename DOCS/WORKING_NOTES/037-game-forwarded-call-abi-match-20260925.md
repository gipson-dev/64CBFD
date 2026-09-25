# Game forwarded-call ABI match - 2026-09-25

## Result

`func_151B2FA0` is byte-exact across its complete 12-word linked extent
`0x151B2FA0..0x151B2FD0`. The fresh C-only matcher reports
`2553 / 5490 (46.50%)` overall and `1985 / 4801 (41.35%)` game. One init
function remains blocked by address drift; 2,936 total and 2,816 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained wrapper and its local `func_151B47D8` declaration typed the
forwarded third argument as `s16`. IDO therefore spilled the incoming `a1`,
reloaded it with `lh`, and scheduled the argument saves differently. Five of
the wrapper's 12 words differed even though its call target and behavior were
otherwise recognizable.

Widening only the wrapper argument to `s32` did not solve the mismatch. The
callee declaration still required conversion to `s16`, so the compiler kept
the `lh` and moved other setup instructions around it. Widening both the
wrapper argument and the callee declaration to `s32` removed that false
conversion and reproduced retail exactly: IDO spills `a2`, masks it into
`a3`, moves the incoming `a1` directly into `a2`, then saves `ra` and the
original `a1` before the call.

This is a source-level ABI/type correction. It adds no guarded word patches
and does not change the unprototyped generated definition of `func_151B47D8`.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_1DF510.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all 12 retail words and the target is absent from
the non-exact list. The patch table remains at 494 rows with no duplicate
filename/function/offset keys. An independent comparison of the complete
48-byte linked ELF span at file offset `0x1F2FA0` and retail ROM span at
`0x1E0450` produced SHA-256
`39d8f40d465f804aa8ae34e5a18beb2004aea57e6d7fad3fc509ebb97eff27da`
for both.

The `64CBFDOGL` sibling contains `func_151B2FA0` and `func_151B47D8` only in
generated recomp output and symbol configuration. This IDO-facing C type
correction does not transfer to hand-maintained host source. Its dirty
worktree was left untouched, and its frozen Release configuration was not
built or launched.

## Next boundary

The five-difference game queue is complete. The next listed game target is
36-word `func_150770E4` with six real differences. Other game rows at the same
tier include eight-word `func_150A7770` and 14-word `func_1515F008`; classify
ownership and source-shape risk before choosing between them.
