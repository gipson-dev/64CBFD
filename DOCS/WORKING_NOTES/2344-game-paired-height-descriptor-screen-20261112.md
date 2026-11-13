# Paired Game height-descriptor screens

**Historical screen:** superseded by [Note 2345](2345-game-paired-height-descriptor-match-20261112.md). Its original ordinary-case fixture accidentally placed the context at the emulated stack pointer; the corrected non-overlapping cases and extended checks passed in the follow-up.

Date: 2026-11-12. `func_150C5F94` in `generated_F3270` and
`func_150C68C4` in `generated_F3BA0` each occupy 81 retail words. Their known
callers, `func_150C5F40` and `func_150C6870`, pass an owner and context and
store the result at context offsets `0x5C` and `0x70`, respectively. Both
production definitions remain zero-return placeholders; neither is credited.

The two retail bodies build a ground-query point from owner offsets `0x14`,
`0x18` and `0x1C`, query with a lower height bound of owner Y minus 100,
select either the query result or a fallback height, and submit a 48-byte
partially initialized descriptor to `func_1513418C`. When the factory returns
nonzero, they copy a 12-byte payload containing the context pointer, active
byte, untouched padding and height into the returned record at offset `0x58`.
The two variants use distinct global constants and descriptor fields.

Private typed C candidates have the same frame and 81-word length. A shared
local work area reproduces retail stack addresses for the query point and
payload. Each candidate matches 52 instruction positions directly; 29
relocation-aware expected-word guards normalize instruction and descriptor
store scheduling. Both independent padders reproduce all retail instructions
and relocation bindings. Nine other functions and the constant pools in each
owner are unchanged in these isolated compilations.

Tools commit `d50360d` retains the candidates and reproduces the screening:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_paired_height_descriptor_screen -v
```

The two tests pass with mounted tools and with four staged files against the
sibling tools dependencies. For each function, 96 modeled cases (with the fixture overlap described above)
compare raw, retail and both padded programs, including helper mutations, query
outcomes, allocation outcomes, all 48 descriptor bytes and 12 copied payload
bytes. In a separate sweep, 638 overlapping owner/context cases per function
complete with the same observations. Ten more per function encounter matching
modeled invalid return or memory states; only their exception identity is
compared, not their preceding accesses. These deliberately constructed aliases
are not proof about real callers. The factory, query and memcpy are modeled
hooks, not connected retail helper executions, and no independent semantic
model or fault-prefix proof is claimed.

Before installing either candidate, inspect the callers' storage contract;
qualify the interrupted alias cases, helpers, caller path, independent
semantic/native behavior, relocations and fault ordering as applicable; then
perform production Make, full-image and owner-section audits, and recount.
No production code, retail guards, linked image or progress row changed in
this screen. The previous linked recount remains Game **3,732 / 4,842
(77.08%)**, total **4,405 / 5,515 (79.87%)**, zero address drift, with
**142** additional Game matches needed to reach 80%.

The scoped Graphify refresh retained or relocated all 59,949 previous nodes,
with 59,951 afterward and no changes outside the selected files. It retained
31,816 nodes fail-closed; it was not a full-corpus extraction.
