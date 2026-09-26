# Game gated byte-result chain match - 2026-09-26

## Result

`func_1519257C` is converted from a zero-return placeholder and byte-exact
across its complete 18-word, 72-byte retail span at
`0x1519257C..0x151925C4`. The fresh linked matcher reports 2,676 / 5,483
exact C functions overall and 2,108 / 4,794 in Game.

## Recovered behavior

The function calls `func_15192308(arg0, arg1)` and retains its low byte. A
zero full-width result returns that zero byte immediately. A nonzero result
authorizes a second call to `func_15192358(arg0, arg1)`, whose low byte becomes
the final result. The first call is therefore a gate, not a fallback result.

Separate full-width `call_result` and byte-sized `result` locals preserve the
retail distinction between testing the complete first return value and
returning only its low byte.

## Compiler boundary

The split locals emit retail's first-call `beqz` with the byte mask in its
delay slot, the conditional second call and second mask, and the shared
`v1`-to-`v0` return path. Every instruction matches directly from C. No
guarded word rows were needed, and the patch table remains at 1,111 unique
rows with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x1BF9FC` and pristine retail
`conker.us.bin+0x1BFA2C` spans are both 72 bytes and compare equal. Both hash
to:

`6fa2ab2ca7daf2cf8c3d1ced76a4176bcf5b66029fc45fa455b7964fd90a52a8`

The focused object build, non-matching relink and objcopy binary, fresh
matcher, exact span comparison, replacement/outer non-matching build,
`make tools-check`, all six project-tool unit tests, and `git diff --check`
pass. No gameplay runtime test was required for this byte-matching change.

## Sibling audit

`64CBFDOGL` uses generated recompilation artifacts for this guest function;
no separately maintained hand implementation needs a paired change. Its 1,659
existing dirty entries were left untouched. Frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 19-word `func_151B82CC`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
