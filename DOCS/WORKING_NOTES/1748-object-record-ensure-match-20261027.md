# 1748 - Object-record ensure callback direct C match

Verified: 2026-10-27. Target `func_15097910`, owner `generated_C4DC0`.
VA `15097910..150979CC`; retail ROM `C4DC0..C4E7C`.

## Result and recovered behavior

Replace the zero-return placeholder with the complete 47-word /188-byte routine.
Every word emits directly from ordinary O2/g3 C: zero new guards, frame 0x30,
four call relocations and one HI16/LO16 pair for `D_800D20FC`. All three owner
neighbors and pools remain fixed; the owner contains four compact functions.

The recovered API is `s32(s32 selector, u8 identity)`. The incoming second value
is overwritten by the first input's low byte. Keep the full first word as a
parameter, the byte identity carrier, then a separate local index before the
actor pointer declaration. This recovers the original incoming argument spills,
identity home at frame+0x24 and local index home at frame+0x2C. A first-argument
byte prototype emits 45 words/frame 0x20; treating the index as the second formal
recovers 47 words but spills the index in the wrong incoming home. The selected
carrier and local order recover every word without guards or fake padding.

Call `func_15083E0C` with the byte identity. A missing descriptor (-1) returns
-1 without further table/actor accesses. Otherwise call `func_15083E90`. If an
actor exists, use its unsigned byte at +0x13F. If none exists, clear byte+2 of
the selected 48-byte descriptor, reload the global table pointer and submit
`func_15082A44(record, index, 0, 0, 0)`. Constructor failure returns -1. Success
repeats the descriptor query using the retained byte identity. A nonzero final
index receives bit 0x2000; zero stays zero. Preserve the full signed/unsigned
32-bit result patterns and the -1 sentinel.

`SpawnLookupRecord` describes only this routine's measured 48-byte stride and
state byte+2. Shared SDK types, headers, flags and other routines are unchanged.
The existing shared `struct258` declaration is not substituted for this local
record view. The byte store can overlap the global pointer in guest cases, so
its reload before forming the constructor argument remains observable.

## Actual interpreter callback boundary

The aligned retail census finds one pointer literal at ROM `22CEE4` /VA `80088424`:
slot1 of the 15-entry `D_80088420` table. No direct JAL/J targets this routine.

The authentic 39-word window `150AE0F8..150AE194` in `func_150ADAF0` selects
this table, extracts the expression word's type nibble, subtracts one for the
table index, clears the nibble from A0 and passes the expression pointer in A1.
The target overwrites that second input before using its byte carrier. The
window returns the callback's V0. S7 is explicitly its handwritten return-address
carrier, rather than an ordinary preserved caller local. Zero type returns zero;
a null selected table entry attempts an invalid callback, without a null guard.

Seven hundred cases qualify this original window with the source callee and
bounded other callbacks. Twenty-five of its 39 words are reached through this
entry; the other table-selection entries remain in the literal window. The
containing interpreter C is still a placeholder. No full caller recovery or
Native interpreter acceptance is claimed.

## Focused qualification

Both tools copies pass eight fresh canonical methods, zero errors/failures/skips.
The primary takes 8.864s; exact mirror timing is retained in its receipt. Both
shared tools checks pass.

- 7,854 guest cases cover every selector/actor-index byte, three full input-word
  patterns, both stack phases, zero and -1, signed full-word re-query results,
  constructor success/failure, six overlap layouts and five provider modes.
  Every one of the 47 target words is visited; complete private state agrees.
- The identity and local-index homes are exercised explicitly, including provider
  changes to incoming homes, the private identity and index homes, and the global
  table. Sparse/wrapped indices and private-frame overlaps are guest-only cases.
- Native32 O0/O2/O3 each pass 15,872 positives with correctly typed indirect calls,
  every incoming identity/actor-index byte, valid record indices, global table
  mutations, trapping UBSan and eight effective functional negative controls.
  Native lookup/actor/constructor providers are bounded contracts.
- Seventy-eight access-fault prefixes fire. Missing descriptors need only the
  stack mapped, with no table/actor storage. Fault semantics are guest-only.
- 288 integrations execute both original and retained 33-word descriptor and
  72-word actor lookup copies. They cover zero identity, descriptor misses,
  indices 0/3, actor misses and slots 0/25, constructor failure and table changes
  before re-query. The visited helper subsets are 32/33 and 46/72 words; this is
  bounded integration, not complete helper-path or constructor acceptance.
- A separately compiled cached-table mutant fails under a real provider mutation,
  making the stale global read observable. Three raw/binding negatives fail
  closed. Six GNU links across three layouts preserve all six bindings, another
  JAL region and signed-low carry; eighteen rebased guest cases pass.
- Seven full-image corruptions and three wrong inputs are rejected.

The first canonical run exposed two harness issues: parallel copies linked the
same immutable fixture path to a shared output, and an overly broad missing-index
mutant could dereference index -1 before returning a normal mismatch. Each copy
now links its own byte-identical object in its PID directory. The negative now
rejects the valid zero index while retaining the -1 gate, producing an ordinary
wrong-result/call sequence. Candidate C and prepared artifacts are unchanged.
Failed v1 receipts remain in `failed-canonical-v1/`; accepted suites are v2.

## Production and measured progress

The actual three-command owner Make recipe reproduces all four compact functions
and the padded object. Production passes with the inherited duplicate
`generated_12D630` recipe warning. Each tools copy runs two fresh installed
owner/image methods and reuses six semantic methods only after module, snapshot,
prepared-artifact and sealed-input fingerprints agree. Broad unchanged suites
are retained evidence, not freshly rerun checks.

The whole production ELF equals the independent prediction: 140 target code bytes
and one symbol-size byte change, 141 total, zero exclusions or serialization
allowance. All 6,056 function addresses and 6,055 other bodies remain fixed.
Protected Game data stays exact across 720 owners /189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

All 125 focused inputs and 16,167 sealed Native/cache files are checked with four
declared source/object/ELF/map adoption paths. Conversion inventory and guard
manifest bytes remain unchanged. No emulator, R4300 hardware, FCSR, rendering
or gameplay acceptance is claimed.

The captured adopted Native ELF recount is 3,826/5,506 exact (69.49%):
Game 3,153/4,833 (65.24%), Init 492/492 and Debugger 181/181; zero address drift,
1,680 still different. The 75% threshold remains 4,130 exact, requiring 304 more.
Remaining triage is 1,551 placeholders, 120 semantic/other and nine unlocated
entries; source-shape screening alone earns no matching credit.

## Checkpoint and continuation

Baseline consumer `54a122bf1d4c27ee9bdeb97936d6b767f53b9415` and tools
`7a27c64df6ea03dc507fdd6ef7931a45969d1698`. Tools are banked first in
`f77d4b4af6358f81480ecf638ddc53490bed53ad` and pinned by the consumer.
Preserve the old mirror's 1,706 inherited dirty paths plus two new files. No push.

- Snapshot SHA: `79e686dc8180bf7045c19216e875cae1b2c31e3206fd290e322c008e6e65afb8`.
- Raw body SHA: `73b13145e722b2bc5704cc6220bb52a3eab89173b0175d1eda5437d96566166c`.
- Padded object SHA: `f5dec4123dbc0fffd5dba966b53360860d861dc747d71198f00e6a7568109018`.
- Adopted ELF SHA: `5795da319763009c6e5c780cf08f6d1d8089ae1d94a98d12b9d8dc9b83cef63d`.
- Reproduce: `python3 -m unittest tools.tests.test_game_object_record_ensure_match -v`
  in the prepared consumer/cache. Ignored artifacts remain in
  `conker/build/game-object-record-ensure-match/` with fresh PID directories.

Codex owns implementation/validation; routine Claude calls zero. Refresh the
changed-source Graphify graph with node/relationship retention checks, without
a full-corpus or new global-community claim. Keep the 75% goal active.
The private `func_1514E920` screen stays parked and uncredited. Next screened
placeholder: `func_15110544` in `generated_13D350`, 47 words, requiring full gates.
