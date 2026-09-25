# Working Note 003: Debugger Rectangle Fill Byte Match

Date: 2026-09-24

## Result

`func_16001390` is byte-exact in the linked US ELF. The restored C retains the
retail 88-word length, 32-byte frame, saved-`s0` lifetime, four-pixel unroll,
and pointer update in the loop branch delay slot.

The linked checkpoint is:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,520 / 5,497 (45.84%) | 1 | 2,976 |
| Init | 387 / 508 (76.18%) | 1 | 120 |
| Game | 1,959 / 4,808 (40.74%) | 0 | 2,849 |
| Debugger | 174 / 181 (96.13%) | 0 | 7 |

## Scheduling Boundary

IDO 5.3 consistently emits the final independent operations as stride `sll`
then row `sra`; retail emits row `sra` then stride `sll`. More than 40,000
permuter candidates from both source orderings did not improve the one-
reordering score. The debug ROM contains the same retail schedule, confirming
that the US target extraction is not the source of the difference.

`conker/retail_word_patches.us.csv` records the two replacements at function
offsets `0x13C` and `0x140`. `tools/pad_c_object.py` checks the compiled input
word before applying each replacement and fails on stale or unapplied entries.
The table is therefore an explicit compiler-scheduling exception, not evidence
that the unpatched C object is intrinsically byte-exact.

## Verification

The following checks passed:

```sh
python3 -m py_compile tools/pad_c_object.py
make -C conker build/src/debugger/debugger.c.o NON_MATCHING=1 -j4
make -C conker build/conker.us.elf NON_MATCHING=1 -j8
python3 tools/match_progress.py conker/progress.csv \
  conker/build/conker.us.elf conker/conker.us.bin --version us \
  --objdump mips-linux-gnu-objdump
```

The linked tail is `subu t1`, `sra a3`, `sll t2`, `bgtz a3`, with the pointer
`addu` in the delay slot. The matcher no longer lists `func_16001390`.

## Resume Boundary

Continue with debugger `func_16000F8C`, currently five real differences in
the `v1`/`v0`/`t0` coloring of the float word, exponent mask, and doubled-zero
test. Keep `func_15135480` as the separate game follow-up candidate.
