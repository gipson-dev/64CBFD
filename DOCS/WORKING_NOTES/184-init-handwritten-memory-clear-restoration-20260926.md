# Init handwritten memory-clear restoration - 2026-09-26

## Result

`func_10001420` is restored from a false C conversion to its original
handwritten nine-word assembly body. Its complete 36-byte span at
`0x10001420..0x10001444` matches pristine retail independently.

## Ownership evidence

The function clears `0xFE0` bytes beginning at `D_80043B40`. Retail loads the
moving pointer into argument register `a1`, derives the end pointer in `a0`,
increments `a1`, compares it with `a0`, and performs each store in the `bne`
delay slot. A no-argument C function has no natural reason to choose those
argument registers.

The repository's initial revision owned this function through `GLOBAL_ASM`
and documented the register mismatch. The later equivalent C uses return-value
registers and requires ten words. Since the retail allocation is nine words,
the layout tool had to replace that body with a jump to
`__retail_overflow_func_10001420`. This is an ownership mismatch, not an
ordinary compiler-scheduling problem.

## Restoration

`conker/src/init_1420.c` again references the extracted original body through
`GLOBAL_ASM`, and the assembly is now tracked explicitly. No guarded retail
word patches are involved.

The conversion denominator drops by one while the exact-C numerator remains
unchanged:

| Section | C functions | Raw assembly | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,474 / 6,038 (90.66%) | 564 | 2,691 / 5,474 (49.16%) | 1 | 2,782 |
| Init | 500 / 538 (92.94%) | 38 | 390 / 500 (78.00%) | 1 | 109 |
| Game | 4,793 / 5,318 (90.13%) | 525 | 2,120 / 4,793 (44.23%) | 0 | 2,673 |
| Debugger | 181 / 182 (99.45%) | 1 | 181 / 181 (100.00%) | 0 | 0 |

## Exact-byte evidence

The linked Init-code slice at offset `0x420` and pristine retail slice at
offset `0x1420` compare equal for all 36 bytes. Both have SHA-256
`a4726841f3477fedc98f9ff44c74f6cb613b2950e7d1c9434a0f61dbda17bdbf`.

## Sibling audit

`64CBFDOGL/recomp_out/.c` already contains the complete generated loop with
the correct pointer setup, comparison, and delay-slot store on both branch
paths. No host source, generated source, or frozen Release change is needed.

## Validation

- The focused `init_1420.c.o` assembly-processor build passes.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and LIST `match-progress` runs pass; `func_10001420` is no
  longer a C-classified mismatch.
- The independent 36-byte linked-versus-retail comparison passes.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Continue ordinary Init matching with 11-word `func_100038E0`, now the first
nonblocked row at nine real differences. Keep address-blocked
`func_10012588` parked.
