# Init handwritten MMIO setup restoration - 2026-09-26

## Result

`func_100038E0` is restored from an equivalent C conversion to its original
handwritten 11-word assembly body. Its complete 44-byte span at
`0x100038E0..0x1000390C` matches pristine retail independently.

## Ownership evidence

The routine stores MMIO address `0xBC000C02` in `D_80038070`, stores `0x4040`
in `D_80038074`, writes the same halfword to the MMIO address, and returns the
address.

Retail constructs the address directly in return register `v0`, reuses it for
the MMIO store, and leaves it live as the return value. It independently loads
`0x4040` into `t6` and `t7` for the two halfword stores. Equivalent C instead
hoists the constant into `v1`, constructs the address through `t6`, and loads
the MMIO base again in `t7`. Nine of eleven words differ despite identical
observable stores and return value. This low-level register choreography and
the initial revision's `GLOBAL_ASM` ownership identify a handwritten routine,
not an ordinary C scheduling mismatch.

## Restoration

`conker/src/init_38E0.c` again references the extracted original body through
`GLOBAL_ASM`, and the assembly is now tracked explicitly. No guarded retail
word patches are involved.

The conversion denominator drops by one while the exact-C numerator remains
unchanged:

| Section | C functions | Raw assembly | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,473 / 6,038 (90.64%) | 565 | 2,691 / 5,473 (49.17%) | 1 | 2,781 |
| Init | 499 / 538 (92.75%) | 39 | 390 / 499 (78.16%) | 1 | 108 |
| Game | 4,793 / 5,318 (90.13%) | 525 | 2,120 / 4,793 (44.23%) | 0 | 2,673 |
| Debugger | 181 / 182 (99.45%) | 1 | 181 / 181 (100.00%) | 0 | 0 |

## Exact-byte evidence

The linked Init-code slice at offset `0x28E0` and pristine retail slice at
offset `0x38E0` compare equal for all 44 bytes. Both have SHA-256
`2afa60e885db40dd282ff0cf18ffe43a5716521c18c5c235975bcf8cb84d97f4`.

## Sibling audit

`64CBFDOGL/recomp_out/.c` retains the old equivalent compiled schedule. It
performs the same two global stores, MMIO halfword write, and `v0` return, so
no host behavior fix is required. A future controlled regeneration should
consume the corrected retail bytes for instruction parity. No host source,
generated source, or frozen Release artifact was changed here.

## Validation

- The focused `init_38E0.c.o` assembly-processor build passes.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and LIST `match-progress` runs pass; `func_100038E0` is no
  longer a C-classified mismatch.
- The independent 44-byte linked-versus-retail comparison passes.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Audit 12-word `osWritebackDCacheAll`, now the first nonblocked Init row at
nine real differences. Keep address-blocked `func_10012588` parked.
