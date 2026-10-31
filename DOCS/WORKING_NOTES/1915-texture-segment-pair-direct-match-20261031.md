# 1915 - Texture segment pair restored from direct C

Date: 2026-10-31. Function `func_15133EEC`, generated owner `15F680`.
VA `0x15133EEC..0x15133FD8`, ROM `0x16139C..0x161488`.
Tools checkpoint: `60092733ae87ca657baeb5a6c621d5514fcd179d`.

The zero-return placeholder is replaced with the semantic resource loader
and segment command builder. All 59 words emit directly from C under the
retail O2/g3 profile, including the 64-byte frame, saved S0/RA lifetime,
three relocations, width-specific argument homes and branch delay slots.
There are no word guards, inserted or omitted words, or alignment padding.

## Recovered source and interface

The signature is `Gfx *(Gfx *cursor, u16 index, u8 segment, s32 priority)`.
The unsigned 16-bit index selects a 12-byte record in `D_80090B60`. Its
first word points to the signed resource ID. The metadata bytes at offsets
10 and 11 are captured before `func_1510D0EC(resource, &extent, priority, 0)`.
The first command binds the returned address to the selected segment.
Metadata value two adds a second binding at the next segment, using the
returned address plus extent minus 512 for layout one, or minus 32 otherwise.
The arithmetic wraps as unsigned 32-bit address arithmetic. The returned
cursor advances by one or two eight-byte commands.

The SDK `gSPSegment` macro emits both commands. Reading the resource ID
before the metadata and preserving the original scalar declaration order
recovers the retail allocation and instruction schedule without guards.
The alternative source was only a hypothesis: its wide index and metadata
loads were corrected from retail `lhu`/`lbu` instructions.

The local forward declaration now uses the typed interface. Callers
`func_15133E84`, `func_15133EB8` and `func_15133FD8` gain explicit SDK32
cursor casts. These casts preserve all emitted caller instructions. Their
other source is unchanged. The loader's recovered definition independently
confirms its `u32 (s32, s32 *, s32, s32)` interface. No shared header changes.

## Qualification and boundaries

- Eight fresh target checks pass independently in both tools copies, plus
  both shared tool checks. Each installed copy runs two fresh source/image
  checks and reuses six unchanged checks only by complete input, module and
  qualified artifact fingerprints.
- All 59 instructions are exercised in 864 guest cases / 2,592 executions
  across original, raw C and padded images. Metadata/resource mutation,
  unsigned narrowing, one/two-command cases, unsigned wrap, guest incoming
  home mutation, output aliases, eight cases under two independent rebases,
  and 65 access cuts including three delay cuts agree in full machine state
  and trace. Guest alias/home/fault claims concern emitted instructions.
- All five retail JAL sites execute: ROM `0x161350`, `0x161384`, `0x1614D0`,
  `0x204628` and `0x20463C`. Two complete 13-word wrappers pass 64 cases;
  the complete 35-word list caller passes 40 cases, including zero and 255
  entries. The remaining parent's seven-word two-call window passes another
  40 cases. Cursor chaining and helper argument forwarding are checked.
  No complete gameplay or full remaining-parent claim is made.
- The original 162-word loader is connected in 160 cases / 480 executions,
  reaching 77 of its words across cache-hit, zero-sized and invalid-ID paths.
  Tests verify min/max ID tracking, extent, signed priority update, retained
  count preservation and address output. Allocation/decompression paths are
  outside this bounded check. On an early invalid-ID return, the loader does
  not write extent; consumption of the existing stack word is compared only
  in the guest model. Native tests use an always-written extent contract.
- Native SDK32 O0/O2/O3 with UBSan trapping pass 131,072 cases per profile,
  covering all 65,536 indices, all byte selectors/layouts, helper metadata
  mutations, both command counts, address wrap and output canaries.
  Thirteen separately compiled IDO and native semantic controls fail by
  explicit mismatch; compiler/interpreter/sanitizer failures are rejected.
- Whole owner raw/padded compilation preserves all 30 neighbors and pools.
  The two inherited pointer/integer diagnostics in the unrelated resource
  release routine are unchanged; no new diagnostics are accepted. Actual
  Make performs five commands, including GLOBAL_ASM pre/post processing,
  and produces exactly the qualified object.
- The independent full-image prediction equals the first link and
  production ELF: 182 changed bytes = 181 target code bytes + one target
  symbol extent byte. There are no metadata permutations or excluded ranges.
  All 6,055 other bodies and all 6,056 addresses remain fixed. Protected
  Game data remains exact across 189,088 bytes and 720 owners.

Production ELF SHA-256:
`62a0323d8390580412174769d2b02b39a99834e672f7f1e92ae6c48971025452`.
The map, C inventory CSV and complete guard manifest remain unchanged.
Receipts: `conker/build/game-texture-segment-pair-15133EEC-match/`.

## Progress and continuation

The actual adopted ELF recount is **3,992 / 5,506 (72.50%)** exact C,
Game **3,319 / 4,833 (68.67%)**, Init 492/492, Debugger 181/181, with zero
address drift. The 75% threshold remains 4,130; **138** more verified
functions are required. Conversion inventory totals do not change.

Next screen: `func_15166118`. Tools are committed before consumer source/pin/docs.
The eleven-file graph refresh retains prior nodes and valid directed
relationships, retiring the two obsolete signed placeholder return edges.
Caller cast changes receive explicit source validation. No full-corpus
extraction, global clustering, push, host-port or Release work is claimed.
