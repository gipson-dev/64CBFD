# Game relative-offset tree walk match - 2026-09-26

## Result

All 39 words of `func_15002560` now match retail across
`0x15002560..0x150025FC`. The linked matcher reports `2610 / 5484 (47.59%)`
overall and `2042 / 4795 (42.59%)` game, with one address-drift blocker and
2,873 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine walks a tree encoded with signed relative halfword offsets. It
fills a missing sibling offset from `arg1`, follows the child offset at
`0x0C`, recursively repairs each sibling chain, and advances to the child
until a zero child offset ends the walk.

The previous ordinary `while (arg0 != NULL)` let IDO turn the loop-back edge
into a bottom `bnez`. Expressing the walk as an infinite loop with a top null
exit restores retail's unconditional branch back to the original branch-likely
null test. The direct conditional halfword assignment still emitted separate
stores. Assigning its ternary result to a scalar first makes IDO merge the
paths through `v0`; this also frees `t7`, shifting the recursive sibling chain
into retail's `t7`, `t8`, and `t9` registers. Array-index spelling for the two
pointer additions produced no change and was reverted.

Two expected-word guards remain at relative offsets `0x48` and `0x60`. They
select retail's base-first operand order for the commutative child and sibling
pointer additions. They alter no relocation or control-flow word. The recursive
`R_MIPS_26` call relocation, frame, early exit, branch-likely loop, and full
39-word extent are source-emitted and exact.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x2F9E0` and pristine
retail `conker/conker.us.bin+0x2FA10` are byte-identical for 156 bytes and
share SHA-256
`38e72a9437314876eb11b824d041a92158c88f2856a50f2a371ab8c5ec554f8f`.
The patch table contains 781 rows, zero duplicate keys, and two rows for this
function.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 19-word `func_150356C8`, now the first game row with thirteen
real differences. It rejects slot count fifteen, increments `D_800C3F00`, and
returns the previous 12-byte record in `D_800C3F08`. Its branch structure,
zero return, stride arithmetic, and extent are already aligned. Retail keeps
the cursor address in `a0`, increment in `t6`, narrowed index in `t7`, stride
in `t8`/`t9`, and table address in `t0`; current C uses `a1`, `a0`,
`t6`/`t7`/`t8`, and `t9`. Test cursor/local declaration and increment lifetime
ordering before adding guards.
