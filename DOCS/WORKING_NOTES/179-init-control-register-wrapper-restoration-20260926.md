# Init control-register wrapper restoration - 2026-09-26

## Result

`__osSetSR` and `__osSetFpcCsr` are restored from false C placeholders to
their original assembly ownership. Both complete four-word, 16-byte spans
match retail. The fresh matcher reports 2,688 / 5,477 exact C functions
overall and 387 / 503 in Init.

## Ownership evidence

`__osSetSR` is explicitly marked handwritten in the preserved libultra source.
It writes CP0 Status with `mtc0 a0,$12`, waits through a hazard `nop`, and
returns. The no-op C placeholder instead compiled to a stack home followed by
an earlier return, leaving three real word differences.

`__osSetFpcCsr` is a low-level SDK assembly wrapper rather than an ordinary C
routine. It reads the old FPU control/status register with `cfc1 v0,$31`, writes
the new value with `ctc1 a0,$31`, and returns the old value. Its zero-return C
placeholder missed both control-register operations. IDO C cannot express
either wrapper's required instructions, so guarded retail-word replacement
would be the wrong ownership model.

## Build integration

Both generated slices now use minimal extracted `GLOBAL_ASM` bodies. Their
preserved `asm/libultra/os/*.s` files remain the retail-layout authorities for
`pad_generated_object.py`. Fresh `progress.csv` classifies both rows as
assembly, and neither filename has a guarded word-patch entry.

## Exact-byte evidence

| Function | Address | Bytes | SHA-256 |
| --- | ---: | --- | --- |
| `__osSetSR` | `0x10022A30` | `408460000000000003e0000800000000` | `8c9798aafb630c54a679991a2a686c3379687a94f8b3c8c14e5eafe1cd8cb961` |
| `__osSetFpcCsr` | `0x10022A50` | `4442f80044c4f80003e0000800000000` | `1b1c2a5e117a433a988d960120310c5634987537358a5b13b49fddcee5d2dac4` |

The linked Init spans and pristine `conker.us.bin` spans compare equal. The
corrected conversion inventory is 5,477 / 6,038 functions and
1,932,328 / 2,256,728 bytes overall. Init is 503 / 538 functions and
148,856 / 164,048 bytes. Exact C numerators remain unchanged because two
non-exact C rows correctly left the denominator.

## Sibling audit

`64CBFDOGL` already provides native tracked-status implementations for
`__osGetSR_recomp` and `__osSetSR_recomp`; `__osSetFpcCsr` remains represented
in the recomp symbol/stub configuration. No generated or host source change is
required for this guest classification checkpoint. The sibling's 1,659 dirty
entries were preserved, and frozen Release was not built, modified, or
launched. `build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

- Focused generated-slice object builds pass and disassemble to the four
  expected words for each wrapper.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and summary/list `match-progress` runs pass.
- Both independent 16-byte linked-versus-retail comparisons pass.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Continue ordinary Init C matching with 26-word `func_1000FE88`, the first
non-blocked Init row in the fresh difference list. It has two real word
differences. Keep address-blocked `func_10012588` parked until its linked call
target can be corrected without disturbing surrounding layout.
