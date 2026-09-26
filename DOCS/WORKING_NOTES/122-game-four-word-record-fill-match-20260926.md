# Game four-word record fill match - 2026-09-26

## Result

`func_1519F3B8` is byte-exact across all eighteen words at
`0x1519F3B8..0x1519F400`. The linked matcher reports
`2634 / 5483 (48.04%)` overall and `2066 / 4794 (43.10%)` game, with one
address-drift blocker and 2,848 total differing C functions. Debugger remains
complete at `181 / 181`.

## Source and schedule

The function calls `func_1519F1C8(arg0, 6)` and
`func_1519F1C8(arg0, 7)`, storing those results in the first and third words
of a four-word record at object offset `0x58`; the second and fourth words are
cleared. A `FourWord1CC440` view records that layout in maintained C.

IDO preserves the operation but emits a compact 24-byte frame, direct
object-relative stores for the first pair, and reconstructs the record base
after the second call. Nine guarded rows plus one inserted `v1` reload restore
retail's 32-byte frame, retained record-base lifetime, interleaved stores, and
call-delay spill. Both call relocations remain explicit and guarded.

The patch table now has 888 unique rows. Exactly nine belong to this function,
and there are no duplicate `(filename, function, offset)` keys.

## Evidence

The final linked and pristine 72-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x1CC838`
- retail `conker/conker.us.bin+0x1CC868`
- SHA-256 `255c72317f442f9f907d25041cfeb2102a94d201814a062babd2b30298f1a432`

The focused object build, exhaustive nonmatching rebuild, fresh direct
matcher, outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only its generated recompilation translation
and declaration, with no separately maintained host implementation to update.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 19-word `func_15160274`, now the smallest ordinary-C game row
among the fourteen-difference candidates. It copies the word at `D_800A6670`
into a stack record and calls `func_15169260(record, 1, arg0, arg1)`. Compare
its current scalar-array expression with the one-word aggregate-forwarder
shape already proven by `func_1518F45C`, `func_151A561C`, and
`func_151D343C`; verify its distinct argument ordering and three padding words
before changing source.
