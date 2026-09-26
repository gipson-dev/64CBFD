# Game stack-record pointer match - 2026-09-26

## Result

`func_1519072C` is byte-exact across all seventeen words at
`0x1519072C..0x15190770`. The linked matcher reports
`2621 / 5483 (47.80%)` overall and `2053 / 4794 (42.82%)` game, with one
address-drift blocker and 2,861 total differing C functions. Debugger remains
complete at `181 / 181`.

## Evidence

The function builds a stack record containing the incoming object pointer and
the byte at object offset `0x3B`, then passes that record to `func_151D343C`
with code `0x2A` and to `func_1518F45C` with code `0x49`.

The generated C originally passed `&rec` directly to both helpers. IDO used a
32-byte frame and rematerialized the address before the second call, leaving
one padded word. A named pointer recovered retail's 40-byte frame and record
offsets, but IDO still rematerialized the address. Typing the live address as
`s32` recovered retail's single spill/reload but selected `sp + 0x18` rather
than `sp + 0x1C`. A separate volatile placeholder moved that spill but expanded
the frame to 48 bytes and was rejected.

The accepted source uses one local aggregate containing an unused word, the
integer-valued record pointer, and the record itself. That reproduces retail's
contiguous local layout: placeholder at `sp + 0x18`, saved record pointer at
`sp + 0x1C`, and record at `sp + 0x20`. The compiler then retains the input in
`a2`, spills the record pointer across the first call, and emits the exact call
and delay-slot schedule without guarded word patches.

The object build, full non-matching link, fresh matcher, outer build, and
project tool checks passed. Linked `conker/build/conker.us.bin+0x1BDBAC` and
pristine retail `conker/conker.us.bin+0x1BDBDC` are byte-identical for 68 bytes
and share SHA-256
`6f21df87663fadb3301142c9299fc72547fe44885afb7ae7fbb12668b4ea1939`.
The patch table remains at 823 rows with zero duplicate keys and no rows for
this function.

The `64CBFDOGL` sibling contains recompilation metadata and a stub declaration
for this address, but no maintained host implementation to update. Its 1,659
existing dirty entries were left untouched. Frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 15-word `func_1519582C`, now the first game row with thirteen
real differences. Its generated C writes the correct zero and `-2` values to
five globals, while retail first materializes pointers to `D_800E08E4` and
`D_800E08EC` and interleaves the remaining direct stores. Compare source-level
pointer locals and statement order before considering guarded scheduling.
