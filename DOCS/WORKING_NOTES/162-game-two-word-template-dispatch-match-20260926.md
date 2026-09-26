# Game two-word template dispatch match - 2026-09-26

## Result

`func_1515572C` is converted from a zero-return placeholder and byte-exact
across its complete 21-word, 84-byte padded retail span at
`0x1515572C..0x15155780`. The fresh linked matcher reports 2,674 / 5,483
exact C functions overall and 2,106 / 4,794 in Game.

## Recovered behavior

The function copies the two-word template at `D_800A6038` into an eight-byte
stack record and passes that record to `func_15169260` with kind `2`, the
caller's data pointer, and the caller's byte selector. This is the two-word
structural sibling of the already matched three-word template wrapper
`func_15131D4C`.

The restored signature records the data pointer and `u8` selector explicitly.
That byte type recovers retail's incoming `a1` spill and zero extension before
the template copy and dispatch call.

## Compiler boundary

The typed two-word assignment emits retail's paired `lw`/`sw` template copy,
including the exact address relocation, register allocation, call delay slot,
frame, and epilogue. Every instruction matches directly from C. No guarded
word rows were needed, and the patch table remains at 1,111 unique rows with
zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x182BAC` and pristine retail
`conker.us.bin+0x182BDC` spans are both 84 bytes and compare equal. Both hash
to:

`944cf9c1d5c4ad797dfd79c5dc99f879a68303faccdd6a7f279fb7077bbc0413`

The focused object build, non-matching relink and objcopy binary, fresh
matcher, exact span comparison, replacement/outer non-matching build,
`make tools-check`, all six project-tool unit tests, and `git diff --check`
pass. No gameplay runtime test was required for this byte-matching change.

## Sibling audit

`64CBFDOGL` references this function through generated recompilation and
configuration artifacts; no separately maintained hand implementation needs
a paired change. Its 1,659 existing dirty entries were left untouched. Frozen
Release was not built, modified, or launched; `build/Release/conker_pc.exe`
retains timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 19-word `func_15178B98`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
