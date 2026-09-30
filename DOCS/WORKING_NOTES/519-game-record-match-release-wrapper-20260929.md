# Game record-match release wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_1518F49C` in `conker/src/game/generated_1BA1D0.c` occupies 32 words and
128 bytes at `0x1518F49C..0x1518F51C`. It forwards an incoming record and
selector to `func_15169850` together with owner fields at offsets `0x18` and
`0x1C`. For selector `0x49`, it releases the owner through `func_1516972C`
when either the record word or discriminator byte matches.

## Source recovery

The previous body was a false zero-return placeholder. The recovered function
uses the actual three-argument ABI. Its selector is a 32-bit incoming argument
whose low byte is read directly from the argument home slot at each use. This
reproduces retail's two `lbu` instructions without creating a separate narrowed
local and oversized frame.

Loading both comparison pairs into explicit locals before the equality gate
preserves retail's simultaneous `$v0`, `$v1`, `$a0`, and `$a1` lifetimes and
keeps the record base in `$a2`. IDO emits the complete 40-byte frame, both
branch-likely exits, calls, and delay slots directly from semantic C. No
expected-word guards are used.

## Verification

- The focused `generated_1BA1D0` object reproduces all 32 retail words.
- The linked ELF and non-matching build pass.
- The authoritative matcher reports `3,023 / 5,463 (55.34%)` overall and
  `2,445 / 4,789 (51.05%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 128 linked bytes at
  Game offset `0x18F49C` and retail ROM offset `0x1BC94C`.
- Both spans share SHA-256
  `60e99d1939859e1e9b6d3415de34212abe309135238fa1ba79be3c37d0077bbb`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_151E4E64`, the next ordinary 33-word Game candidate with 30 real
differences. Keep `func_15106E78` parked on its 30-versus-32-word caller-saved
allocation cycle, `func_15015F40` parked behind unresolved indirect-table
ownership, and `func_150A76F0` in the handwritten-assembly queue.
