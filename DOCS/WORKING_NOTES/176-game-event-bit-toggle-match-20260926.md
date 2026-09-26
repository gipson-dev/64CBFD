# Game event-bit toggle match - 2026-09-26

## Result

`func_150FADC8` is converted from a zero-return placeholder and byte-exact
across its complete 20-word, 80-byte extent `0x150FADC8..0x150FAE14`. The
fresh matcher reports 2,687 / 5,482 exact functions overall and
2,119 / 4,793 in Game.

## Recovered behavior

This three-argument callback interprets its third byte argument as an event
code. Event `0x53` sets bit `0x2` in the 32-bit owner field at offset `0x58`
and returns immediately. Event `0x54` clears that bit. Other event values
leave the field unchanged. The second byte argument is part of the callback
ABI but is not used by this handler.

The function is referenced from the callback table at `D_8008A02C`, which
supports the shared `(owner, byte, event-byte)` signature already present on
the adjacent `func_150FACE4` callback.

## Source and ABI evidence

The old `s32 func_150FADC8(void)` declaration emitted only a three-word
zero-return placeholder. Retail homes `a2` at `8(sp)`, narrows it to eight
bits, homes `a1` at `4(sp)`, and then performs the two event tests. Declaring
both callback values as `u8` reproduces that entry sequence exactly.

The natural `if (arg2 == 0x53) ... else if (arg2 == 0x54)` form also emits
retail's early `jr ra` with the set-bit store in its delay slot, followed by
the clear-bit branch and terminal return. All 20 words compile directly from
C; no guarded patch rows are required.

## Exact-byte evidence

The linked ELF `.game+0xFADC8` span at ELF file offset `0x13ADC8` and pristine
retail `conker.us.bin+0x128278` span are both 80 bytes and compare equal. Both
hash to:

`d5ecec1757d0c3cb4b0029f249451874134a13c2e94381cf7c0408d6bd066a96`

The focused object build, complete replacement link, fresh matcher, exact-span
comparison, outer build, project-tool checks, six pad-tool unit tests, and
whitespace audit pass.

## Sibling audit

`64CBFDOGL` has no separately maintained host implementation. Its already
dirty generated `recomp_out/.c` currently reflects the old three-word
zero-return placeholder for this routine, so host parity is not yet implied by
the decomp match. That generated output was left untouched for a later
controlled regeneration from the corrected guest input. The sibling's 1,659
existing dirty entries were preserved. Frozen Release was not built, modified,
or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership,
keep 17-word `func_150721A4` parked as the known live-C compiler overflow, and
keep probable handwritten `func_15125628` outside the ordinary C queue.

Continue with 21-word `func_15133DE8`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior, relocations, and current object shape before editing source.
