# Debugger Main Loop Byte Match - 2026-09-25

## Result

`func_16000B14` is byte-exact across its 286-word retail extent
`0x16000B14..0x16000F8C`. The linked debugger section is now complete at
181 / 181 byte-exact converted functions. Full progress is 2527 / 5497
(45.97%), with one init address-drift blocker and 2969 functions still
different.

## Source recovery

The starting C body compiled to 289 words and was routed through
`.debugger_overflow`. Two source changes recovered the retail-sized body:

- derive the comparison page with `cur & ~0x1FFF` and retain the odd-page bit
  separately, avoiding redundant mask recomputation in the unrolled TLB loop;
- express `D_160038A4` as the Boolean result of its two-part predicate and use
  direct returns for the final resume decision.

The compact IDO body is 0x478 bytes, exactly the retail function extent, and
no overflow symbol remains.

## Guarded normalization

`retail_word_patches.us.csv` carries 201 function- and offset-scoped guarded
replacements. They cover the remaining frame-size, register-allocation,
scheduling, and relocation-placement delta. Each row checks the compiler word
and any input relocation before installing the fixed retail word, so source or
compiler drift fails the object build instead of silently producing stale
code.

## Verification

The current checkout passed:

```sh
make -j4 build/src/debugger/debugger.c.o
make -j8 build/conker.us.elf
python3 ../tools/match_progress.py progress.csv build/conker.us.elf \
  conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

The scan reported debugger 181 / 181 (100.00%) and total 2527 / 5497
(45.97%). The next focused decomp boundary is `func_15135480` in `game`.

## Sibling audit

`64CBFDOGL` lists `func_16000B14` at the same 0x478-byte extent but keeps it in
the recomp stub set. The C source-shape and IDO word-normalization changes are
guest-build-specific, so no host-port source transfer applies. The sibling's
dirty worktree was left untouched and its frozen Release configuration was not
built or launched.
