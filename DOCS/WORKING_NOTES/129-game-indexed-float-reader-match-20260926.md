# Game indexed-float reader match - 2026-09-26

## Result

`func_15088270` is byte-exact across all sixteen words at
`0x15088270..0x150882B0`. The linked matcher reports
`2641 / 5483 (48.17%)` overall and `2073 / 4794 (43.24%)` game, with one
address-drift blocker and 2,841 total differing C functions. Debugger remains
complete at `181 / 181`.

## Index and pointer lifetime

The function reads an entry from the optional `D_800872A0` table. Each record
is `0x84` bytes, and the float at offset `0x14` is converted to an integer.
The previous source used `arg0` directly for the stride and retained a separate
pointer, producing the wrong index register and final record base.

Keeping `s32 idx = arg0` and then reusing `arg0` for the computed record
address recovers the source-level lifetimes. Ten guarded scheduling rows
restore retail's `a1` index copy, `v1` table-base load, completed stride in the
null-check delay slot, zero-return delay slot, and final `a0` record pointer.
No words are inserted. The patch table contains 923 unique rows with no
duplicate keys.

## Evidence

The final linked and pristine 64-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0xB56F0`
- retail `conker/conker.us.bin+0xB5720`
- SHA-256 `459eccfdf1e672fe1f29e94dcb9a782ad401863d80c893a74a9ceeaba3f27d2f`

The exhaustive nonmatching build, fresh direct matcher, outer build, and
project tool checks passed. The first guard attempt intentionally failed
against stale expected words; correcting those guards from the authoritative
compact object produced the exact span above.

The `64CBFDOGL` sibling contains only generated recompilation translations,
calls, declarations, and a stub for this symbol, with no separately maintained
host implementation to update. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Continue with 17-word `func_15188A58`. Retail clears `arg0 + 0x0C`, appends
the node to the list rooted at `*arg1`, and walks each existing node through
its offset-`0x0C` link. The current zero-return placeholder has no recovered
behavior or argument contract. Recover the smallest suitable node view and a
void append signature before considering guarded scheduling.
