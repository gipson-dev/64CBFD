# 1845: Segment resource setup match

Date: 2026-10-29. Target `func_150DFBD0`, owner `generated_10CD70`.
VA `0x150DFBD0..0x150DFCA8`, ROM `0x10D080..0x10D158`: 216 bytes / 54 words.

The zero-return placeholder becomes a complete `Gfx *` routine matching its
existing caller declaration. Three iterations query `func_150DF8C0(index)`.
A nonzero answer selects resource table word `9 + D_800DD405`; zero selects
word 8 of `D_80090324`. The unsigned variant and resource word are read after
the query, preserving helper mutations. It loads each resource through
`func_1510D0EC(resource, &extent.value, 3, 0)`, emits `gSPSegment` for segments
2, 3 and 4, and returns the cursor advanced by three commands / 24 bytes.
Zero and high-bit resource addresses are emitted without an extra gate.

The SDK macro recovers the retail temporary command pointer and segment-offset
induction. Reusing the temporary for the activity result, variant and loaded
address recovers the retail register lifetimes. A union exposes the loader's
s32 output while preserving the retail aligned output cell at SP+72. The
returned extent is unused. This reconstructs a legal C storage shape and the
measured ABI; the original source spelling or union declaration is unknown.

All 54 words and six relocations emit directly from C with the existing O2/g3
profile. The original 88-byte frame saves S0..S7 at +20..+48 and RA at +52,
uses 16 outgoing argument bytes and no incoming homes. No guards, inserted
words, omissions, frame adjustments, shared-header or compiler-profile edits.
The inherited guard manifest and conversion inventory CSV bytes are unchanged.

- Eight fresh canonical methods pass in each tools copy, plus shared checks.
  Installed checks rerun two methods per copy; six semantic methods reuse
  only full input/module/artifact identity.
- Guest: 4,112 cases / 12,336 original/raw/padded executions agree in literal
  full state and cover all 54 words. Cases exercise all 256 variant values,
  all activity masks, high-bit query results, zero/high-bit loaded addresses,
  live variant/table mutations, two stack phases and commands aliasing the
  resource table, including the fallback word read by a later iteration.
- Native32 O0/O2/O3 each pass 2,056 cases with UBSan and reject eight controls:
  wrong query index, inverted activity, cached variant, wrong fallback word,
  wrong selected word, wrong segment, wrong payload and wrong return cursor.
- 114 access prefixes, six sparse executions and three layouts / 288 rebase
  cases pass. The original four-word caller window in `func_1510B9D0` at
  VA1510BB6C / ROM13901C passes 144 cases, forwarding the updated cursor to S0.
  Activity and loader are bounded providers, including permitted mutations.
  No complete provider, parent, hardware or gameplay execution is claimed.
- Complete owner compile/padding preserves all 12 neighbors and pools. Three
  actual Make commands reproduce the object with zero C diagnostics. The
  inherited duplicate-recipe Make warning remains. All 222 raw-byte/binding
  and 236 whole-image corruption controls reject.
- Strict independent image prediction equals production: 174 changed bytes
  = 173 target code + one symbol extent, zero metadata changes or exclusions.
  All 6,055 other linked bodies and all function addresses remain fixed.
  Protected Game data remains exact across 189,088 bytes / 720 owners.

Fresh actual adopted-ELF count: **3,922/5,506 (71.23%)**, Game **3,249/4,833
(67.23%)**, Init492/492 and Debugger181/181, zero drift. **208** more to 4,130.
Tools committed first: `f8dc2c4a5a1dc66c207bd0429a36281b1603e880`. No push. Root README gets aggregate rows only.

The scoped eleven-file AST refresh retains or uniquely relocates all 49,851
prior nodes and preserves 103,358 valid old directed relationships. Exactly
one obsolete s32 return edge retires for the recovered Gfx pointer interface.
Both helper calls and the existing caller are source/binding checked. Outside
manifest rows and analytics remain historical; no full-corpus extraction.

Artifacts: `conker/build/game-segment-resource-setup-match/`. Next screened
target `func_1518F384` still needs full qualification. Parked candidates uncredited.
The older tools mirror retains 1,973 inherited dirty paths plus three new files.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls. The 75% matching goal remains active.
