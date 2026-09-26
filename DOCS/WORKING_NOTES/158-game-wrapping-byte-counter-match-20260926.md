# Game wrapping byte-counter match - 2026-09-26

## Result

`func_1508CA88` is byte-exact across all 20 words, or 80 bytes, at
`0x1508CA88..0x1508CAD8`. The fresh linked matcher reports 2,670 / 5,483
exact C functions overall and 2,102 / 4,794 in Game.

## Recovered behavior

The function increments the signed byte at offset `0x1703` in the object
addressed by `D_800D23B0`. It compares that updated byte with the signed limit
`D_8008FD90`. Values below the limit are returned unchanged; values at or
above the limit reset the byte to zero, reload the global object pointer, and
return the reset byte.

The previous C used an unsigned-byte pointer for the increment and split the
two outcomes into separate returns. That emitted `lbu`, inverted the retail
control flow, duplicated the return, and kept the global-address base live
through the final reload. A signed pointer, explicit result lifetime, `>=`
reset path, and shared return recover the retail loads, comparison, branch
likely, stores, and epilogue.

## Compiler and tool boundary

The recovered source emits nineteen of the twenty retail words directly. IDO
still reuses the first `D_800D23B0` address base for the final pointer reload;
retail hoists an independent `%hi(D_800D23B0)` into `t9` and pairs it with a
later `%lo` load.

Two guarded rows preserve that schedule. The first verifies the threshold
high relocation and inserts the independent `t9` high word; the second
verifies the compiled tail load and replaces it with the corresponding
symbolic low relocation. `pad_generated_object.py` and `pad_c_object.py` now
support relocations on `insert_after` words, reject relocation-only insertions,
and have focused ELF-relocation tests. The patch table contains 1,111 unique
rows with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0xB9F08` and pristine retail
`conker.us.bin+0xB9F38` spans are both 80 bytes and compare equal. Both hash
to:

`5329f59db01e662472dbd6eb6a3f48747d1c3dfdd94fa66d5fbeada21b9403cf`

The focused object build, all-object non-matching ELF rebuild, objcopy binary,
fresh matcher, exact span comparison, replacement/outer non-matching build,
`make tools-check`, all six project-tool unit tests, and `git diff --check`
pass. No gameplay runtime test was required for this byte-matching change.

## Sibling audit

`64CBFDOGL` references `func_1508CA88` through generated recompilation and
configuration artifacts; no separate maintained hand implementation was
found. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 21-word `func_15116930`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
