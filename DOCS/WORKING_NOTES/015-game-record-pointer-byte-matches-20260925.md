# Game record-pointer byte matches - 2026-09-25

## Result

`func_15087FC4` and `func_15087FEC` are byte-exact across their complete
linked extents:

| Symbol | Extent | Linked result |
| --- | ---: | ---: |
| `func_15087FC4` | 10 words | 10 / 10 retail words exact |
| `func_15087FEC` | 16 words | 16 / 16 retail words exact |

The fresh C-only matcher reports `2534 / 5495 (46.11%)` overall and
`1966 / 4806 (40.91%)` game. One init function remains blocked by address
drift; 2,960 total and 2,840 game C functions still differ.

## Mismatch and resolution

Both maintained C bodies already had the retail control flow, arithmetic,
record stride, field offset, and function length. IDO selected `$t7` for the
final record pointer, while retail selected `$v1`; each dependent store then
carried the same register difference. Source-shape experiments documented in
the older working notes did not change this allocation choice.

`retail_word_patches.us.csv` now contains four function- and offset-scoped
expected-word guards:

```text
func_15087FC4 +0x18: 01C27821 -> 01C21821
func_15087FC4 +0x1C: A1E50031 -> A0650031
func_15087FEC +0x2C: 01C27821 -> 01C21821
func_15087FEC +0x34: E5EA0004 -> E46A0004
```

The first word in each pair assigns the final record address to retail's
`$v1`; the second uses `$v1` for the byte or float store. The guarded patcher
aborts if IDO stops emitting any expected input word, keeping the
normalization local and drift-detecting.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_B3020.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

Neither target appears in the non-exact list. An independent disassembly and
ROM read compared linked addresses `0x15087FC4..0x1508802C` with
`conker.us.bin+0xB5474`; all 26 words match. The debugger remains complete at
181 / 181 C rows, plus its independently exact handwritten assembly row.

The `64CBFDOGL` sibling consumes these guest routines from generated recomp
output, so this IDO-only register normalization does not transfer to host
source. Its unrelated dirty worktree was left untouched, and its frozen
Release configuration was not built or launched.

## Next boundary

The remaining two-difference game queue contains `func_1519C910` (14 words),
`func_1517F448` (16 words), `func_15079F6C` (20 words),
`func_1516968C` (20 words), and `func_151696DC` (20 words). Continue with
`func_1519C910`, auditing its complete linked body before choosing a source
change or guarded normalization.
