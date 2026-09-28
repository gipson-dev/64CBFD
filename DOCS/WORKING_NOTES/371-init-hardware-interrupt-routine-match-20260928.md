# Init hardware interrupt routine match - 2026-09-28

## Result

`__osSetHWIntrRoutine` is recovered from its empty C placeholder and is
byte-exact across the complete 20-word, 80-byte retail span at
`0x10026AC0..0x10026B10`.

The fresh linked matcher reports 2,869 / 5,466 (52.49%) exact C functions
overall and 392 / 495 (79.19%) in Init, with 2,596 genuinely different C rows
overall and 102 in Init.

## Recovery

The local SDK source at `tools/ultralib/src/os/sethwinterrupt.c` established
the routine's compiler-generated semantics: save the result of
`__osDisableInt`, install the supplied handler in `D_8002AC70[interrupt]`, and
pass the saved mask to `__osRestoreInt`.

The default generated-object `-O2 -g3` profile produced a different frame and
register lifetime. Assigning this object `-O1` reproduces retail's `0x28`
frame, saved `s0` lifetime, disable-call delay-slot store, table update, and
restore-call schedule. No expected-word guards are used.

## Verification

The focused generated-object build, complete link and fresh matcher pass
succeed. The refreshed rebuilt span at
`build/conker.us.init.code.bin+0x25AC0` and pristine retail span at
`conker.us.bin+0x26AC0` compare equal across all 80 bytes. Both have SHA-256:

`e1788dea9d015addff0a0749a852ba1292c4c437c3ed0dcfc714795e0675a9f7`

The replacement build, outer-ROM build, project-tool checks, all nine focused
Python tests and whitespace validation also pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified or launched.

## Next boundary

Audit 25-word Init `func_1000CBF0`, now the smallest unblocked Init row in the
fresh mismatch list at 24 real differences. The smaller 17-word
`func_10012588` remains blocked on address drift.
