# Init handwritten CP0 wrapper restoration - 2026-09-26

## Result

`__osGetSR`, `osGetCount`, and `__osSetCompare` are restored from false C
placeholders to their original handwritten assembly ownership. Each complete
four-word, 16-byte padded slot matches retail. The fresh matcher reports
2,688 / 5,479 exact C functions overall and 387 / 505 in Init.

## Ownership evidence

The three generated C files contained explicit zero/no-op placeholders. Their
retail counterparts are marked handwritten in the preserved libultra assembly
and differ at the privileged instruction that ordinary IDO C cannot emit:

- `__osGetSR` reads CP0 Status with `mfc0 v0,$12`.
- `osGetCount` reads CP0 Count with `mfc0 v0,$9`.
- `__osSetCompare` writes CP0 Compare with `mtc0 a0,$11`.

The matching `jr ra`, delay-slot `nop`, and trailing padding `nop` in the old
objects were compiler/padding coincidences, not valid C implementations.
Guarded replacement words would hide the ownership error, so none were added.

## Build integration

Each generated slice now uses `GLOBAL_ASM` with a minimal extracted body under
`asm/nonmatchings/generated_*`. The existing `asm/libultra/os/*.s` source stays
the layout authority for `pad_generated_object.py`, which preserves the final
padding word and exact 16-byte slot. Fresh `progress.csv` therefore classifies
all three rows as assembly.

## Exact-byte evidence

The linked Init code and pristine `conker.us.bin` spans compare equal:

| Function | Address | Bytes | SHA-256 |
| --- | ---: | --- | --- |
| `__osGetSR` | `0x10022A40` | `4002600003e000080000000000000000` | `98eb78e5220bcc1e31ff049202bde4471c76ac15ebbc22d818771f741671fe0a` |
| `osGetCount` | `0x10024770` | `4002480003e000080000000000000000` | `49439260d2ea325fd9d1049a302274c512c90775bbc3751b54513b65152f01ae` |
| `__osSetCompare` | `0x10027490` | `4084580003e000080000000000000000` | `424b05c5a5a48f29b4669731a97ea63a5ee362e2b47fa58afc9317487695229c` |

The corrected conversion inventory is 5,479 / 6,038 functions and
1,932,360 / 2,256,728 bytes overall. Init is 505 / 538 functions and
148,888 / 164,048 bytes. The exact C numerator remains unchanged because the
three non-exact C rows correctly left the C denominator.

## Sibling audit

`64CBFDOGL` already supplies a native `__osGetSR_recomp` override backed by
the tracked status register. `osGetCount` and `__osSetCompare` remain named in
the recomp symbol/stub configuration. This guest ownership correction does not
justify a generated-output or host-source edit, so the sibling's 1,659 existing
dirty entries were preserved. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

- Focused generated-slice object builds pass.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and both summary/list `match-progress` runs pass.
- All three independent 16-byte linked-versus-retail comparisons pass.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Continue the Init low-level ownership queue with `__osSetSR` and
`__osSetFpcCsr`. Determine whether each is original handwritten or SDK
assembly before attempting C. The ordinary Game queue remains available at
19-word `func_151444DC` with eighteen real differences.
