# Record Parameter Updater Guarded Match - 2026-11-07

`func_150A2940` replaces its zero-return placeholder with the complete
record-parameter updater. Its **34 words match retail after two guards**
exchange independent address/register instructions. The semantic C already
has the original frame-free ABI, six bindings, both optional stores, live
pointer reloads and conditional final clear. Raw C matches 32 of 34 words;
this is a guarded match, not a claim of direct compiler word identity.

Fresh production count: **4243/5513 = 76.96%**, Game **3570/4840 = 73.76%**,
Init 492/492, Debugger 181/181, zero drift. **168 more** exact functions reach
4411/5513 and 80%. The corrected census includes one previously omitted C placeholder.

## Source, ABI and ordered behavior

Entry 150A2940..150A29C8; ROM CFDF0..CFE78; 136 bytes; frame zero.
Owner `conker/src/game/generated_CDE80.c`; normal IDO 5.3 O2/g3, MIPS2/O32.
Interface: `void func_150A2940(u32 identity, s32 value, s32 kind)`.

The low twelve identity bits select a 0x34-byte record, provided the index
is strictly below the unsigned interpretation of D_800D3094. A full-word
value other than -1 writes field18; a full-word kind other than -1 stores its
low byte in field17. The function then clears field1C. Rejected indices do
not write anything. Values with a low byte of FF remain valid updates unless
the complete input word equals FFFFFFFF. The descriptor pointer D_800D3098
is reloaded after each potentially aliasing store. Field names/comments
record measured offsets and effects without assigning an unproven role.

The original caller at JAL ROM CD8C8 / VA 150A0418 loads two full words from
packet offsets 8 and C, calls the updater, then overwrites V0 with its own
success value 1. No target return value is consumed; the old s32/no-argument
placeholder was a false interface. The six-word original call window is
connected to the actual updater in five guest cases. The caller's complete
switch remains an unrelated production placeholder. Whole original-image
census finds one direct JAL and no entry/interior pointers.

## Scheduling and complete-owner/image gates

Raw SHA-256: `823a558b4f10d9d5ecd9c2aa4a60f86717d73c2f2c0377d7cfd26167f0db9e7d`.
The only differences are offsets 2C and 30: the compiler emits the T9 subu
before the A3 address addiu. Retail emits these independent instructions in
the opposite order, still before the descriptor-pointer load. Two expected-
word/expected-relocation guards exchange precisely this pair and move its
LO16 binding from 30 to 2C. The full raw-body SHA and all six named bindings
fail closed before normalization; the complete prior CSV byte prefix is
preserved. The signed-ID source screen still has two differences; the wide-
kind and split-ID variants fail full layout and remain private.

Predecessor consumer 7df94e8d432a037db1f848a8a546ee1d5951dfa7; tools
a825e158a57d00d3b95d57fb35e6217b7e2ba754. Qualification freezes 101
source/header/compiler/input files and compiles the complete GLOBAL_ASM
owner. All 27 raw/padded neighbors and their bindings, all allocatable pools,
and raw/padded register metadata remain fixed. Production and strict padders
agree across 28 functions/pools; all 31 preserved original case-label
symbols are separately accounted for. No Makefile or shared header changes.

The copied actual five-command Make recipe reproduces the qualified object.
The independent complete-image prediction equals production after **114
changed bytes, zero exclusions**: 111 bytes inside the target, one target-size
byte (12 -> 136), and two bytes changing the existing neighbor symbol from
absolute to section 5. Its address, 12-byte stub size, type and name stay fixed.
All 6052 existing addresses remain fixed; the disassembly now exposes the
neighbor boundary, yielding 6053 function entries. The complete-image and
named-definition predictors account for these exact changes without exclusions. All 189088 protected data bytes across
720 owners remain exact. The source installation compiles only this owner using O2/g3 without C
warnings. The metadata repair explicitly relinks the existing owner with Make
`-W build/src/game/generated_CDE80.c.o`, without another compilation: the auto
definition file is not itself a Make prerequisite. Existing duplicate
generated_12D630 recipe warnings and
the expected development-image checksum rejection are recorded separately.

## Focused qualification

Both mounted and sibling configurations pass seven fresh tests before and
after installation. Only the three new modules are staged in an ignored
sibling overlay, with its missing-pool-helper fallback recorded. The actual
sibling checkout's 2434 dirty paths are fingerprinted and preserved. The
initial WSL status listed five extra status entries; the native Git snapshot
has the same HEAD and identical hashes for all 2434 files. Both snapshots
are retained; later checks use the native inventory. Both shared smoke
checks are fresh; three unchanged shared regressions per copy are reused
with exact helper/test fingerprints.

| Check | Evidence |
| --- | --- |
| Ordered guest model | 244 cases; all 34 instructions reached; exact complete memory and literal modeled state for retail, raw and normalized words |
| Width/bounds | Low12 identity mask, flagged IDs, equality rejection, unsigned high-bit counts, full-word sentinels and low-byte conversion |
| Aliases | First word store redirects the descriptor pointer; byte store changes its low byte; subsequent stores follow reloaded pointers |
| Preserved roles | Saved integer/floating roles, GP/SP/FP/RA; no calls and no semantic V0 result |
| Native32 | 225 cases at each of O0/O2/O3; real SDK types, descriptor52/pointer32 layouts, valid arrays, trapping UBSan |
| Effective negatives | Stub, wrong mask, inclusive bound, byte sentinel, truncated word, lost clear and wrong destination field |
| Caller | One original six-word packet/call/result window; five connected cases; one JAL and zero entry/interior pointers |
| Fault prefixes | 23 executed-access cuts; identical literal low-word machine states for retail/raw/normalized words |
| Fail-closed controls | All 34 raw word corruptions, all six binding corruptions, guard-prefix corruption and five complete-image corruptions rejected |
| Independent relocation links | Two GNU links covering all bindings, including signed LO16 carry rebases |

The first production recount correctly withheld credit: the stale absolute
`func_150A29C8 = 0x150A29C8` rule hid that existing C stub from the map, while
the retail layout merged its 292-byte span into the updater's 428-byte row.
The tracked symbol file now declares the neighbor `type:func defined:true`,
and the tracked layout has separate 136/292-byte rows. Only that stale rule
is removed from the generated, ignored auto file; no full extraction occurs.
The real Splat parser/writer suppresses the defined entry, preserves an
unresolved canary, and restores the target rule when `defined` is removed.
The progress gate permits only shortening the updater row and adding the
neighbor row; counts rise by one matched function and one existing converted
placeholder. The unmatched total remains 1270, and 80% now requires 4411.

The image-corruption fixture initially tried to locate the BSS count label
in file-backed ELF bytes. It now corrupts a real protected-data byte; no
production source change was needed. The guard emitter also uses explicit
minus signs for empty relocation lists, as required by the existing loader.
The final tests use these corrected fixtures.

Guest alias/fault probes establish the emitted O32 contract. They do not
claim portable C semantics for arbitrary addresses, full upper-register or
hardware state, the caller's whole switch, collision behavior or gameplay.
Routine task: zero Claude calls. The host port and frozen Release are untouched.

## Bank and next action

Production ELF SHA-256: `a493762c70c8084a6237b210df7caa8b9f5e0470dab737655bd4a08c31835d8d`.
Binary: `f3365bcecd085f1079b04dd6f410381b1a6497e4607dead5e11a6d1182a89ebe`.
Owner: `be2c55ffbd97177efce5d2c96e5e89c783cb7421561f303404d84b877f858351`.
Guard CSV: `6792fe9767ba771d5a3c0a92abe798df38a6b4970cda689f4d93b84a7ad26b95`.

Reproduce in prepared WSL from the consumer root:
`python3 -m unittest tools.tests.test_game_record_parameter_150a2940_match -v`.
Canonical receipts: `conker/build/game-record-parameter-150A2940-match/`.
Tools first, then source/two guards/layout/symbol declaration/docs/README rows/pin are
committed locally. No push. Graphify uses the scoped refresh/retention audit,
not a full-corpus extraction; existing legacy nodes remain part of the graph.

Next inspect `func_150A29C8`, the adjacent 73-word single-record occupancy
query. Preserve its unusual inclusive bound (identity equal to count is
accepted), enabled-actor mask path and original collision fallback. Keep the
80% goal active. The `func_1513FAB4` layout study remains uninstalled/uncredited.
