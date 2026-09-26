# Game buffer-advance match - 2026-09-26

## Result

`func_150CFE98` is byte-exact across its complete 30-word, 120-byte extent
`0x150CFE98..0x150CFF0C`. The fresh matcher reports 2,685 / 5,482 exact
functions overall and 2,117 / 4,793 in Game.

## Recovered behavior

When the byte reached through the owner pointer at `arg0+0x38` is nonzero, the
routine advances the active buffer pointer stored at state offset `+0x10`,
copies that advanced value to `+0x0C`, and passes both to `func_150CFD84`. It
stores the returned segment length as a byte at `+0x14`, toggles the buffer
selector at `+0x15`, invokes `func_150CFE3C` to copy the selected state, and
sets the ready bit in the byte at `+0x08`. The state block begins at
`arg0+0x28`, so those fields correspond to owner offsets `+0x38`, `+0x34`,
`+0x3C`, `+0x3D`, and `+0x30` respectively.

## Source recovery

The previous C held the dereferenced owner pointer, current buffer pointer,
and returned length in named locals. IDO kept those lifetimes alive, producing
a 48-byte frame and eighteen real word differences. Removing the one-use
pointer and result locals and assigning the advanced pointer within the
`func_150CFD84` argument recovers retail's control flow, registers, calls,
relocations, and delay-slot schedules directly from C.

The resulting compiler body differs only in a coherent debug-frame choice:
IDO selects a 40-byte frame rather than retail's 32-byte frame and shifts the
owner and state-pointer spill slots with it. Seven guarded patch rows restore
the prologue/epilogue and those spill/reload offsets. They do not alter a
branch, call target, relocation, data access, or algorithmic instruction.

## Exact-byte evidence

The linked ELF `.game+0xCFE98` span at ELF file offset `0x10FE98` and pristine
retail `conker.us.bin+0xFD348` span are both 120 bytes and compare equal. Both
hash to:

`2324732635eb02dc1675a8a8928f4d551e8d425e0751a1a08beb25ef70d755cd`

The retail patch table contains 1,132 rows with no duplicate
`filename,function,offset` keys; seven rows belong to this function. The
focused object build, complete replacement link, fresh matcher, exact-span
comparison, outer build, tool checks, six pad-tool unit tests, and whitespace
audit pass.

## Sibling audit

`64CBFDOGL` contains the generated recomp declaration and overlay entry for
`func_150CFE98`; no separately maintained host source implementation needs a
paired change. Its 1,659 existing scoped dirty entries were left untouched.
Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership,
keep 17-word `func_150721A4` parked as the known live-C compiler overflow, and
keep probable handwritten `func_15125628` outside the ordinary C queue.

Continue with 21-word `func_150F34A0`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior, relocations, and current object shape before editing source.
