# Init header-tag update match - 2026-09-26

## Result

`func_100043B4` is byte-exact across its complete 22-word, 88-byte span at
`0x100043B4..0x1000440C`. The fresh matcher reports 2,690 / 5,475 exact C
functions overall and 389 / 501 in Init.

## Behavior and compiler boundary

The existing C behavior was complete: save the interrupt mask, replace the
high byte of `arg0[-1]` with `arg1`, preserve the low 24 bits, then restore the
mask. The first 15 words already matched.

Retail stores the updated word before the second `osSetIntMask` call and puts
an otherwise dead `arg0 - 3` adjustment in the call delay slot. Current IDO
instead moves the store into that delay slot and starts the epilogue
immediately afterward. Adding `arg0 -= 3` to C was tested; IDO eliminated it
and reproduced the same six differences, matching the earlier historical
classification of this function as a dead-code retention case.

## Guarded normalization

Six guarded rows restore retail's store/call/delay-slot/epilogue schedule.
The call moves from offset `0x3C` to `0x40`, and its
`R_MIPS_26:osSetIntMask` relocation moves with it. The remaining rows retain
the dead pointer adjustment and shift the unchanged `ra` restore, frame
restore, and return. No behavior, frame size, live register lifetime, or
other relocation changes.

## Exact-byte evidence

The linked Init-code slice at offset `0x33B4` and pristine retail ROM slice at
offset `0x43B4` compare equal for all 88 bytes. Both have SHA-256
`96bbbe8d7fc2767413fc9f85d64896d95b633d867cc2b61023c410a9646d2616`.
The fresh matcher moved exactly this row from different to exact:

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,690 / 5,475 (49.13%) | 1 | 2,784 |
| Init | 389 / 501 (77.64%) | 1 | 111 |
| Game | 2,120 / 4,793 (44.23%) | 0 | 2,673 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

`64CBFDOGL` retains the prior generated instruction schedule for this symbol,
but it performs the same header store and mask-restore call; retail's added
pointer adjustment is dead. No host-visible semantic difference or native
source edit is required. The sibling's existing dirty work and frozen Release
remain untouched.

## Validation

- The focused `init_3C40.c.o` build accepts all six guarded rows and the
  relocation move.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and summary `match-progress` runs pass.
- The independent 88-byte linked-versus-retail comparison passes.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Continue ordinary Init matching with 47-word `func_1000FD38`, the first
non-blocked row in the latest list. It has six real differences. Keep
address-blocked `func_10012588` parked.
