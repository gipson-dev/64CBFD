# 1733 - Menu Selection Reset Match - 2026-10-26

The adopted Native ELF measures **3,810/5,506 exact C functions (69.20%)**,
Game **3,137/4,833 (64.91%)**, zero address drift and 1,696 different.
Only `func_15007778` gains credit. Inventory and converted-byte totals are
unchanged; 320 more matches reach the present 4,130-function 75% threshold.

## Complete C and recovered declarations

`func_15007778`, owner `game_33990`, occupies VA
`0x15007778..0x15007830`, ROM `0x34C28..0x34CE0`: a 44-word body,
two alignment words and no frame. Replace its zero-return placeholder and
obsolete commented draft with `void func_15007778(void)`. The retail symbol
is retained; comments describe the observed resets.

The function writes -1 into the three word and three signed-byte sentinel
fields of the **inline** `struct162 D_800BE3F8`, then sets the signed
halfword `D_800BE3DC` to -1, clears `D_800BE3DE`, and sets
`D_80082BC0` to one. Clear 27 pointed-to bytes, reloading the real
`D_800D2E4C` pointer every iteration. Clear nine inline bytes starting at
`D_800D2E60`, then write -1 into the four adjacent signed sentinel bytes
`D_800BE3DB` down through `D_800BE3D8`.

Correct two shared declarations in variables.h: the inline struct was wrongly
exposed as a pointer, and the four-byte sentinel group was exposed as one byte.
Add `MenuResetSentinels` with four signed-byte fields after `struct162`
in structs.h. Existing named aliases for the other three bytes are retained.
The existing pointer declaration for `D_800D2E4C` is retained and viewed as
bytes locally. No other live C consumer used either corrected declaration.

## Twenty-three derived guards

The ordinary O2/g3/mips2/o32 compiler emits a complete 44-word routine.
Twenty-three relocation-aware expected-word rows normalize three closed regions:

- The first counter starts at zero and reaches 27 without overflow. Derive the
  retail SLTI/BNEZ test from the raw LI/BNE loop while preserving the pointer
  reload, byte-address capture, increment, store delay slot and all 27 visits.
- Swap the two pointer roles in the nine-byte loop and restore the separately
  named end alias `D_800D2E69 = D_800D2E60 + 9`.
- Forward the known -1 value through the three signed-byte reloads in the final
  nonvolatile assignment chain. Derive the rematerialized temporaries and
  retain all four stores in high-to-low address order through their named aliases.

All raw words and bindings are pinned. No instruction is inserted or omitted;
no compiler profile, layout, fallback, symbol annotation or caller is changed.
The normalized body matches all 176 original bytes and all 19 original bindings.
Preserve all 17 raw/padded neighbors; all 18 compact functions agree with actual
Make's normal three-command compiler/padder/assembler plan.

This is **guarded semantic C**, including bounded-loop and byte-value forwarding
transformations. It is not compiler-only matching or merely independent
scheduling. Raw ordinary-memory results and alias/fault memory prefixes are
checked; fitted/original complete states agree. Raw private-register and fault
states are not claimed identical, and guest fault behavior is not portable C.
Nine actual GNU links found no raw end-expression carry failure; the named end
alias restores retail binding form, not a demonstrated raw linker bug.

## Caller and behavioral qualification

Graphify's bounded query locates the stub and owner. The retail census supplies
the actual interface: one JAL at VA `0x151DE91C`, ROM `0x20BDCC`, in
`func_151DE8F0`, with no arguments, no consumed result and no literal
registration. The original caller window `0x151DE8F0..0x151DE944` and its
skip target `0x151DE97C` preserve the late `D_8008FDA4` mode-byte
reload and SP+0x20 saved value. Caller source and object stay unchanged.

Both tools copies pass **nine fresh canonical checks** and their shared tools
checks. Each installed copy then passes two fresh input/image checks and
reuses seven unchanged semantic checks only through exact module, 54-input,
16,099-file seal and eleven-artifact fingerprints. Original execution receipts
remain available.

- 512 guest state/canary cases cover all byte patterns and two stack phases;
  all 44 body words are visited. Each ordinary call makes 49 stores and 27
  pointer reloads, 76 memory accesses in total.
- 936 pointer-alias cases cover 117 layouts, two stack phases and pointer-cell
  mutation; 96 unmapped-pointer cases check the repeated reload faults.
- 304 fired original/fitted fault-prefix pairs compare complete states.
  The local signed-LB oracle is independently checked for all 256 byte values.
- SDK/native32 O0/O2/O3 each run 256 positive cases and eight effective compiled
  semantic negatives with trap UBSan, layout/ABI assertions and complete canaries.
- 3,072 original caller-window cases enter 24 actual target calls, across all
  initial mode bytes, two stack phases, ordinary/mode-byte-alias buffers and
  three bounded opaque provider patterns. Providers `func_151EDF4C`,
  `func_151E7DC0` and `func_151E81EC` remain opaque here; no complete
  parent, provider or gameplay acceptance follows from this window.
- 44 raw-word controls, 16 binding controls, extent/history controls, an actual
  stale-guard padder negative, nine GNU links across three carry-sensitive
  layouts, and seven whole-image corruption controls are effective.

Private failures are retained: an incomplete include overlay and draft rename,
an incorrect assumed Make command count, an unsupported test-local LB opcode,
and a caller-fixture attribute collision. The corrected canonical copies pass
freshly. Frozen raw compiler executions are not overwritten or rerun in place.

## Production and exact image accounting

Actual production Make exits zero in 5.987s and reproduces the
independent ELF `042fc7049cfdd62471d10bcc580b06ab0b55c41fb175e2e85514028c346628ba`. The exact difference is **238 bytes: 153 target
code bytes and 85 metadata bytes, zero exclusions**. The target symbol size
changes from 12 to 176. A closed five-symbol serialization rotation moves
`D_800D2E69` behind `D_80099DF0`, `D_800AB77C`,
`.L151901CC_game_data` and `.L15027038_game_data`; their named values
and types remain unchanged. The corresponding contiguous string block rotates
with them. All 6,056 function addresses and 6,055 other bodies remain fixed.
All 720 protected Game data owners / 189,088 bytes remain exact, SHA
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The first full static-input audit deliberately stopped on rebuilt
`debugger_258ED0.c.o`. A complete object derivation verifies exactly two
undefined extern-size changes, `D_800BE3D8` 1 -> 4 and `D_800BE3F8`
4 -> 48, the non-allocated .mdebug payload, and mandatory ELF geometry for its
1,380-byte shrink. Instructions, relocations, register information, loaded
sections and every other section payload are identical. Retain that rebuilt
object with its corrected declaration metadata; preserve the failed audit
receipt. This is an explicitly accounted intermediate-object change, not an
exclusion from the strict linked-image comparison. The completed production
build and installed checks are reused under identity; no redundant compilation.

Source SHA: `0875d2b24de0e6984da8a5ca5a39723f5804e73e1f084701111c3fbd6daf8342`.
Guard CSV SHA: `33390a4db6e1bd4accdcf8fd11a4c6d7f29cd0780342cf84166bd9fd41f517b7`.
Padded owner object SHA: `4529f1e3dbdb956fe335d4311ce8d2709fba67bde390f10a16f9cbdf63dcb775`.
Raw body SHA: `e18db73c61fa12000aa20d6b28ef6dfa2b688352e1e9165ca6aea5bb6d6bec85`.

Baseline consumer `e1a3f87d`, tools `4980b4b1`, ELF `40663e32`.
Tools `c22a5c33b3d366623d3927a0cefa2eab6999fc88` are committed first. Preserve all 1,676 pre-existing dirty
paths and the older tools mirror's history; only this pair is added there.
The final seal covers 16,099 Native files, 54 focused inputs and exactly eight
qualified adoption outputs, including the accounted debugger metadata object.
Progress CSV and all inventory/converted-byte totals remain fixed. Recount uses
the actual adopted Native ELF, rather than inferring a one-function gain.

The scoped graph closeout refreshes ten changed C/header/Markdown sources through
the native no-cluster update. Before adoption it must retain or uniquely relocate
all 44,288 previous nodes and preserve manifest freshness outside that scope.
Prior community labels remain historical; global clustering and centrality are
not recomputed. Tools AST extraction is separate because the parent ignores tools/.

## Continuation

The ELF-pinned queue contains 1,567 placeholders, 120 semantic/other definitions
and nine unlocated screens. Next screened placeholder is `func_150DDED0`
(`generated_108E90`), uncredited until all qualification gates pass. Preserve
the unresolved pointer/NULL factory classification. The 75% goal stays active.
Routine Claude calls: zero. No push or host-port work.

Prepared-checkout focused command:

```sh
python3 -m unittest tools.tests.test_game_menu_state_reset_match -v
```

Keep frozen raw objects intact; new compilation requires new fingerprints.
