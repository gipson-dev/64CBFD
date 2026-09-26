# Game retained local-record pointer match - 2026-09-26

## Result

All 17 words of `func_1507FF94` now match retail across
`0x1507FF94..0x1507FFD8`. The linked matcher reports `2614 / 5484 (47.67%)`
overall and `2046 / 4795 (42.67%)` game, with one address-drift blocker and
2,869 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine constructs a local record containing `arg0` and its byte at
offset `0x3B`, then passes that record to `func_15191B8C` and
`func_151494E0` with code `0xD`. The original C rematerialized `&rec` for both
calls. It used a 32-byte frame and only 16 body words, so the final padding
word entered the 17-word retail extent and thirteen words differed.

An ordinary retained pointer recovered the 40-byte frame but IDO still
rematerialized the address. Making both call arguments read a volatile pointer
forced two loads and grew the body to 18 words, so that probe was rejected.
The accepted asymmetric lifetime stores a volatile `rec_ptr` after filling
the record, passes `&rec` directly to the first call, and reloads `rec_ptr`
only for the second call. Separating declaration from assignment also places
the pointer spill after the record stores, as retail does.

That source form emits the exact frame, local offsets, pointer spill/reload,
both call relocations, both delay slots, epilogue, and 17-word extent. Five
expected-word guards restore only the independent prologue order: return
address save, incoming-pointer copy, record target store, code-byte load, and
local-record address formation. No relocation is moved or replaced.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0xAD414` and pristine
retail `conker/conker.us.bin+0xAD444` are byte-identical for 68 bytes and share
SHA-256
`e4200d3dee6cba3505c9510b8b1bf1aec92d126dead87a84c041535655634e4f`.
The patch table contains 808 rows, zero duplicate keys, and five rows for this
function.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 30-word `func_15085B70`, now the first game row with thirteen
real differences. Inspect its existing C, retail control flow, and current
object before deciding whether source lifetime changes can reduce the guarded
surface.
