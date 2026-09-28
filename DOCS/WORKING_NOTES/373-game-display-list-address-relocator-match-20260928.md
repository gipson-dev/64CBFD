# Game display-list address relocator match - 2026-09-28

## Result

`func_15004CE0` is byte-exact across its complete 28-word, 112-byte retail
span at `0x15004CE0..0x15004D50`.

The fresh linked matcher reports 2,871 / 5,466 (52.52%) exact C functions
overall and 2,297 / 4,790 (47.95%) in Game, with one address-drift blocker and
2,594 genuinely different C rows overall.

## Recovery

The function scans eight-byte display-list commands until opcode `0xDF`. For
each `0xDC` command whose byte-3 index is `0x0E`, it adds the supplied delta to
the payload when that payload is a physical address below `0x80000000`.

The previous placeholder used an unsigned byte pointer and pointer induction.
Retail loads opcodes with `lb`, so the recovered source uses signed `s8`
opcodes (`-0x21` and `-0x24`), preserves the index byte as unsigned, and
recomputes each command pointer from the original base and an eight-byte
index. An explicit precheck and post-tested loop recover the retail branch
shape. The volatile second opening load is intentional: retail reads the
first opcode for the empty-list precheck and reads it again for the loop body.

This semantic source emits the exact extent, branches, memory operations, and
instruction schedule apart from ten compiler register-allocation words. Ten
expected-word-guarded normalizations select retail's constant/register
lifetimes and commute one equivalent pointer addition. They do not replace a
call, branch target, load/store address, arithmetic result, or side effect.

## Verification

The linked span at `build/conker.us.elf` file offset `0x44CE0` and pristine
retail span at `conker.us.bin` offset `0x32190` compare equal across all 112
bytes. Both have SHA-256:

`b01eb064b755a867c88664319e6b053c96eb045ebff7f26fdfc5d83eb4dd5274`

The replacement build, outer-ROM build, project tool checks, all nine focused
Python tests, matcher scan, guard-table duplicate check, and whitespace
validation pass. The guard table has 1,660 rows and zero duplicate keys.
Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Audit ordinary unparked 28-word Game `func_15033F70`, now the first unparked
row in the 25-real-difference tier. `func_10003BD0` remains open at 25 real
differences after a source-shape audit whose experiments were removed. Keep
the smaller documented special cases parked unless new evidence changes their
ownership or compiler boundary.
