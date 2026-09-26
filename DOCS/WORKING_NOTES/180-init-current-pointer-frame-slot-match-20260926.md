# Init current-pointer frame-slot match - 2026-09-26

## Result

`func_1000FE88` is byte-exact across its complete 26-word, 104-byte span at
`0x1000FE88..0x1000FEF0`. The fresh matcher reports 2,689 / 5,477 exact C
functions overall and 388 / 503 in Init.

## Recovered behavior

The existing C implementation was already behaviorally complete. It checks
the caller's index against the supplied count, locates the 48-byte record,
calls `func_100111C8` when the record's halfword at `+0x24` is nonzero, sets
bit `0x80` in the word at `+0x10`, and returns zero. An out-of-range index
returns one.

The frame size, branches, delay slots, record-stride arithmetic, register
lifetimes, and call relocation already matched 24 of 26 retail words. The only
differences were the live current pointer saved across `func_100111C8` at
`0x18(sp)` and reloaded from that slot. Retail uses the otherwise equivalent
top frame slot at `0x1C(sp)`.

## Guarded normalization

Two `retail_word_patches.us.csv` rows change only those non-relocating stack
accesses:

| Function offset | Compiler word | Retail word | Meaning |
| ---: | ---: | ---: | --- |
| `0x3C` | `0xAFA30018` | `0xAFA3001C` | spill current pointer at `0x1C(sp)` |
| `0x40` | `0x8FA30018` | `0x8FA3001C` | reload current pointer from `0x1C(sp)` |

The patch guards require the known compiler output before replacement. Prior
source-only experiments established that the function has only one real local;
adding an artificial local moved the slot but also enlarged the frame. The two
guarded words therefore preserve the recovered C and constrain only IDO's
independent frame-slot choice.

## Exact-byte evidence

The linked Init-code slice at offset `0xEE88` and pristine retail ROM slice at
offset `0xFE88` compare equal for all 104 bytes. Both have SHA-256
`2468ea4fa2e9ade3f4f573e236236195922ecb3b8673d3543c19095073a2243d`.
The fresh matcher moved exactly this row from different to exact:

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,689 / 5,477 (49.10%) | 1 | 2,787 |
| Init | 388 / 503 (77.14%) | 1 | 114 |
| Game | 2,120 / 4,793 (44.23%) | 0 | 2,673 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

`64CBFDOGL` represents `func_1000FE88` at the same 104-byte symbol extent. Its
generated translation still shows the old `0x18(sp)` scratch slot, but saves
and reloads the same guest pointer around the same call. The slot choice has no
host-visible semantic effect, so generated output and host source were left
untouched. The sibling's 1,659 existing dirty entries were preserved, and
frozen Release was not built, modified, or launched.
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

- Focused `build/src/init_EB00.c.o` compilation accepts both guarded rows.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and summary/list `match-progress` runs pass.
- The independent 104-byte linked-versus-retail comparison passes.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Audit `__osRestoreInt` and `__osDisableInt` together. The preserved
`asm/libultra/os/interrupt.s` marks both as handwritten CP0 routines, while
`src/game/generated_interrupt.c` currently supplies false no-op/zero-return C
placeholders. Keep address-blocked `func_10012588` parked.
