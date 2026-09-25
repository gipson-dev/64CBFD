# Small game assembly boundaries - 2026-09-25

## Result

The two smallest apparent two-difference game rows were false C targets and
are restored to their original assembly ownership:

| Symbol | Extent | Classification | Linked result |
| --- | ---: | --- | --- |
| `func_150A6354` | 3 words | shared assembly epilogue | 3 / 3 retail words exact |
| `func_150AD770` | 4 words | handwritten syscall extent | 4 / 4 retail words exact |

The fresh C-only matcher reports `2532 / 5495 (46.08%)` overall and
`1964 / 4806 (40.87%)` game, with 2,962 total and 2,842 game C rows still
different. The exact numerator is unchanged because this is a classification
correction, not a new C match.

## Classification evidence

`func_150A6354` is not independently called. Retail `func_150A6210` reaches
address `0x150A6354` twice with non-linking `j` instructions, using it as a
shared exit that loads `$f20` and `$f21` before returning through the caller's
existing `$ra`. Modeling that address as `s32 func_150A6354() { return 0; }`
was structurally incorrect.

`func_150AD770` is explicitly marked handwritten in the retail assembly. Its
extent is one `syscall 0` instruction followed by three padding words. IDO C
cannot express this routine, and the placeholder return had no semantic or
instruction-level relationship to retail.

Both symbols now use `GLOBAL_ASM` with focused files under
`asm/nonmatchings/`. The generated-slice object rules compiled and linked
both paths successfully. Direct linked-ELF comparisons produced:

```text
func_150A6354: 4489A000 03E00008 448AA800
func_150AD770: 0000000C 00000000 00000000 00000000
```

Each sequence exactly equals the corresponding retail ROM words.

The `64CBFDOGL` sibling already carries both symbols in generated recomp
output and symbol tables. This guest source-ownership correction does not
transfer to host code. Its unrelated dirty worktree was left untouched, and
the frozen Release configuration was not built or launched.

## Next boundary

The remaining two-difference game queue begins with genuine C candidates:
`func_15087FC4` (10 words), `func_1519C910` (14 words),
`func_15087FEC` (16 words), `func_15079F6C` (20 words),
`func_1516968C` (20 words), `func_151696DC` (20 words), and
`func_1517F448` (16 words). Start with `func_15087FC4`, but retain the older
finding that source-shape experiments did not alter its scratch-register
choice; audit the complete body before deciding whether a guarded
normalization is appropriate.
