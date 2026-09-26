# Game unaligned bitstream helper restoration - 2026-09-26

## Result

`func_151F892C` and `func_151F8960` are restored from false zero-return C
placeholders to their original handwritten 13-word assembly bodies. Their
complete 52-byte spans at `0x151F892C..0x151F8960` and
`0x151F8960..0x151F8994` independently match pristine retail.

## Behavior and ownership

Both routines perform paired `lwl`/`lwr` loads and extract a variable-width
bit field from an unaligned byte stream. `func_151F8960` receives the bit
cursor by pointer, advances it, and writes it back in the return delay slot.

`func_151F892C` is explicitly non-ABI: it consumes the current bit cursor from
live register `t0` and the field width from live saved register `s1`, then
returns the extracted value in `v0` while advancing `t0` in its return delay
slot. A standalone C function cannot reproduce that calling convention. The
initial project layout correctly kept the complete `225D20` slice in assembly,
and the later generated C file replaced both helpers with false zero-return
bodies.

## Restoration

`conker/src/game/generated_225D20.c` now references tracked copies of only
these two original bodies through `GLOBAL_ASM`. Neighboring functions in the
large mixed slice are unchanged. No guarded retail-word patches are involved.

The conversion denominator drops by two while the exact-C numerator remains
unchanged:

| Section | C functions | Raw assembly | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,038 (90.58%) | 569 | 2,691 / 5,469 (49.20%) | 1 | 2,777 |
| Init | 497 / 538 (92.38%) | 41 | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,318 (90.09%) | 527 | 2,120 / 4,791 (44.25%) | 0 | 2,671 |
| Debugger | 181 / 182 (99.45%) | 1 | 181 / 181 (100.00%) | 0 | 0 |

## Exact-byte evidence

The linked ELF slices at offsets `0x23892C` and `0x238960` compare equal to
the pristine retail slices at offsets `0x225DDC` and `0x225E10` for all 52
bytes of each function. Their SHA-256 values are respectively
`e1bcfb7ac1912e9ca1986dacb6e16db8ea7c1b0b9c9a192ce35b789a44739cd6`
and `a5c0dbc044b26fe073f7e493a8977b0ed69b6ef729eab087d2b973d3b7ee6af7`.

## Sibling audit

`64CBFDOGL/recomp_out/.c` already contains complete generated implementations
for both helpers, including the unaligned loads, live-register state, cursor
updates, and delay-slot effects. Its symbol configuration records both correct
`0x34`-byte extents. No sibling source or frozen Release artifact was changed.

## Validation

- The focused `generated_225D20.c.o` assembly-processor build passes without
  changing neighboring mixed-slice functions.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and LIST `match-progress` runs pass; both helpers are absent
  from the C mismatch list.
- Both independent 52-byte linked-versus-retail comparisons pass.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow and
keep probable handwritten 26-word `func_15125628` outside the ordinary queue.
Continue ordinary Game matching with 19-word `func_151444DC`, which has 18
real differences. The next ordinary Init C row is 20-word `func_10001000` at
14 real differences.
