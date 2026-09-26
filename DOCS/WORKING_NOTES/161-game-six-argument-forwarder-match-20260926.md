# Game six-argument forwarder match - 2026-09-26

## Result

`func_15130374` is converted from a zero-return placeholder and byte-exact
across its complete 18-word, 72-byte retail span at
`0x15130374..0x151303BC`. The fresh linked matcher reports 2,673 / 5,483
exact C functions overall and 2,105 / 4,794 in Game.

## Recovered behavior

The function forwards six arguments to `func_15130280`. It preserves the
first argument, zero-extends the second byte argument, inserts zero as the
third argument, moves the original third argument to the fourth position,
then forwards the low byte of the original fourth argument and the original
fifth argument through the two stack argument slots. The return value from
`func_15130280` is returned unchanged.

The local declaration now records `func_15130280`'s six-argument and integer
return contract. Changing only `func_15130374`'s fourth parameter from `s32`
to `u8` makes IDO spill the incoming `a3` word and reload its low byte from
the big-endian argument-home slot, matching the retail ABI exactly.

## Compiler boundary

The direct forwarding expression emits retail's complete 32-byte frame,
incoming `a1`, `a2`, and `a3` spills, `a1` zero extension, argument register
shuffle, two stack-argument stores, call, and epilogue. All instructions match
directly from C. No guarded word rows were needed, and the patch table remains
at 1,111 unique rows with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x15D7F4` and pristine retail
`conker.us.bin+0x15D824` spans are both 72 bytes and compare equal. Both hash
to:

`184a83f8a6398738fccde102155bf4ddd03b35140388f4548245a78aaf418eb0`

The focused object build, non-matching relink and objcopy binary, fresh
matcher, exact span comparison, replacement/outer non-matching build,
`make tools-check`, all six project-tool unit tests, and `git diff --check`
pass. No gameplay runtime test was required for this byte-matching change.

## Sibling audit

`64CBFDOGL` has no separately maintained implementation requiring a paired
change. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 21-word `func_1515572C`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
