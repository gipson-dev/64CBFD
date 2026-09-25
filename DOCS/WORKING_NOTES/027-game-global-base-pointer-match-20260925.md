# Game global-base pointer match - 2026-09-25

## Result

`func_15087DCC` is byte-exact across its complete 34-word linked extent
`0x15087DCC..0x15087E54`. The fresh C-only matcher reports
`2546 / 5493 (46.35%)` overall and `1978 / 4804 (41.17%)` game. One init
function remains blocked by address drift; 2,946 total and 2,826 game C
functions still differ.

## Mismatch and resolution

The function already matched 30 of 34 words. Current C kept the global record
base in `v1`, tested it there, and reused `v1` for the indexed record pointer.
Retail kept the base in `v0`, tested `v0`, then formed the indexed pointer in
`v1`. The four differences were the global HI16/LO16 pair, null branch, and
pointer addition.

Testing `D_800872A0` directly before assigning the computed `rec` pointer gives
IDO the retail lifetimes naturally. An explicit second pointer local was
rejected because it enlarged the frame and changed spill offsets. The accepted
source-only form preserves the 32-byte frame and moves both global relocations
with their instructions; no guarded word patch is needed.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_B3020.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The target is absent from the non-exact list. An independent comparison of the
complete 136-byte linked and retail spans produced SHA-256
`a20e6632dcbdedac7de85f27d6c9abb04f0261ca86d9a2a2b0ee42517e5561a2`
for both.

The `64CBFDOGL` sibling contains this function only as a generated recomp entry
sourced from the ROM instruction stream. This IDO source-lifetime fix does not
transfer to host source. Its worktree was left untouched, and its frozen
Release configuration was not built or launched.

## Next boundary

The next listed game target is 14-word `func_1509D054` with four real
differences. Re-establish its linked mismatch and relocation context before
editing. The following rows are 5-word `func_150A7A00`, 9-word
`func_150ADACC`, 13-word `func_150BDB3C`, and 18-word `func_150F33B0`, each
with four real differences.
