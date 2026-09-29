# Init record-key updater byte match

Date: 2026-09-29

## Scope and behavior

`func_100100E0` in `conker/src/init_EB00.c` occupies 29 words and 116 bytes at
`0x100100E0..0x10010154`. Its recovered C body samples `D_80042760` once,
walks the active prefix of the 48-byte `D_80041FE0` record table, and compares
the three key words at offsets `0x14`, `0x18`, and `0x1C`. A complete match
replaces those words with the function's final three arguments.

The positive-count gate is behaviorally significant. The cursor advances once
per record, and the loop terminates when it reaches
`&D_80041FE0[count]`, reproducing retail's unsigned pointer comparison and
branch-likely prefetch of the next first key.

## Compiler shape

The former index loop repeatedly tested the global count and compiled to a
32-word body with a saved-register frame, so it overflowed the 29-word retail
slot. Expressing the routine as the original pointer-range scan removes that
frame and emits exactly 29 words with retail's branch structure, delay-slot
cursor updates, stack-argument loads, and field stores.

IDO assigns the initial count and record cursor to `$v0` and `$v1`; retail
uses `$v1` and `$v0`. Twenty stale-checked guards normalize that closed
allocation cycle. The three address-bearing guards retain and verify the
`D_80042760` and `D_80041FE0` relocations. No instruction is inserted or
omitted.

## Verification

- The focused `init_EB00` object rebuild passes every existing and new stale
  check.
- A complete guarded-object rebuild and ELF relink pass.
- The authoritative matcher omits `func_100100E0` from its non-exact list and
  reports `2,997 / 5,463 (54.86%)` overall and `396 / 493 (80.32%)` in Init,
  with zero address-drift rows.
- Direct linked comparison reports zero differences across all 116 bytes.
- Both spans share SHA-256
  `cec07d243965cab8d62e7af4a4a557e8ce5e1177ded4ea275655300ff1b1b678`.
- Project tool checks and all 10 tool unit tests pass.

## Resume boundary

Continue with the next ordinary small C candidate from the authoritative
matcher queue. Keep `func_15015F40` parked behind its unresolved indirect-table
ownership and keep handwritten `func_150A76F0` in the assembly lane.
