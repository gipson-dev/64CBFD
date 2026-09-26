# Game indexed record deactivation match - 2026-09-26

## Result

`func_15088780` is byte-exact directly from C across its complete 30-word,
120-byte retail span at `0x15088780..0x150887F4`. The fresh linked matcher
reports 2,680 / 5,483 exact C functions overall and 2,112 / 4,794 in Game.

## Recovered behavior

The function first returns when the global record table `D_800872A0` is null.
Otherwise it resolves an index through `func_1508855C`, clears byte `0x31` in
that index's `0x84`-byte record, and clears the corresponding bit in
`D_800D2394` relative to signed-byte base index `D_800D2398`.

The original C already represented that behavior. Its named one-use `rec`
pointer made IDO assign the record-address chain and the following mask chain
to different registers from retail, producing 18 real instruction
differences despite identical control flow and length.

## Source correction

Removing the one-use `rec` local reduced the mismatch to five words and made
the entire mask-update half match. Writing the commutative address as table
base plus scaled index then assigned retail's `t7` table base, `t8` stride,
and `t9` final pointer. The complete 30-word body now matches directly from C.

No guarded word rows were added. The patch table remains at 1,116 unique rows
with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The linked ELF `.game+0x88780` span at ELF file offset `0xC8780` and pristine
retail `conker.us.bin+0xB5C30` span are both 120 bytes and compare equal. Both
hash to:

`c70d2601cd04ee0b936cb95e64238adc7d0e652f7e66e903f39f4cfe2ba79e33`

The focused generated-object build, full replacement relink, fresh matcher,
exact span comparison, patch-table duplicate audit, replacement/outer
non-matching build, `make tools-check`, all six project-tool unit tests, and
`git diff --check` pass. No gameplay runtime test was required for this
source-equivalent byte-matching change.

## Sibling audit

`64CBFDOGL` contains this function only in generated `recomp_out/.c`; no
separately maintained host implementation needs a paired change. Its 1,659
existing scoped dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 24-word `func_1509E8A0`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
