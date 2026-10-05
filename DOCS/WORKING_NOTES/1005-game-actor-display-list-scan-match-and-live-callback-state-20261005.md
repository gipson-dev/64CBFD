# Game Actor Display-List Scan And Live Callback State

Date: 2026-10-05. Starting HEAD: `1e254b76`, the direct size query in
[Note 1004](1004-game-resource-size-query-direct-match-and-aligned-header-20261005.md).

Followup: [Note 1006](1006-game-actor-update-dispatch-direct-match-and-carried-slot-abi-20261005.md)
recovers the next dispatcher directly. Counts and next-target statements below
remain the historical scan checkpoint.

## Recovery

`func_1502BAD0` in `conker/src/game/generated_58F80.c` is recovered from its
zero-return placeholder. It scans **25 actors at stride 0x32C**, brackets
the output with SDK `gSPDisplayList` references, applies mode-specific actor
filters, chains returned display-list cursors and clears diagnostic state.

```c
Gfx *func_1502BAD0(Gfx *commands, s32 mode, s16 view);
```

The complete **173-word / 692-byte slot**, ROM **0x58F80**, address
**0x1502BAD0..0x1502BD84**, matches retail with the original **0x48-byte frame**.
Default IDO 5.3 O2/g3 is retained; no compiler-profile override is introduced.
Slot SHA-256:
`8a278075c83a3a64eeb495537f79a15a7fb32672d7f8881766e26a0f639b1060`.

The scoped actor layout contains the active word at +0, id byte at +4,
state byte at +5 and flags word at +0x184. The global retains 26 entries;
only the first 25 are visited. No null fallback or new selection rule is added.

## Selection And Callbacks

- An inactive word, state 3 or state 5 excludes the actor.
- State 2 is accepted only in mode 2, bypassing the ordinary id-255 exclusion.
- Mode 6 accepts only state 7. Mode 0 requires flags bit 9.
- Mode 1 excludes states 1 and 7. A state-zero actor passes only when
  `func_1506196C` returns a signed value **at least 255**.
- Mode 2 accepts states 0, 1 and 2. A state-zero actor is rejected only
  when that helper returns **exactly 255**; negative and greater values pass.
- Other modes retain common gates but add no mode-specific filter.
- State is reread after the filter callback. Callback-created state 2
  selects `func_1502C408`; active/id/flags are not checked a second time.
- `func_1502C974` receives five arguments, the fifth zero. Slot-zero generic
  rendering retains `func_150368C4` even if that renderer changes actor state.
- Final `func_15030E08` rendering maps modes 1, 2 and 6 to submodes 0, 1 and 2.
  Every returned cursor feeds the following call or packet.
- `D_8003C8E0` receives `0x01000000 | slot` before each visit, `0x01FFFFFF`
  before final rendering, then zero after the closing display-list packet.
- View is sign-extended from 16 bits once; downstream callbacks receive that
  full signed 32-bit word, not repeatedly narrowed argument homes.

## Matching Evidence

The driver `tools/experiments/game_actor_display_scan_candidates.py` provides
28 C-shape controls. The selected shape shares a signed word local between
the initial active read and state byte, recovering the temporary lifetime.

| Candidate | Body Words | Frame | Different Words |
| --- | ---: | ---: | ---: |
| Zero-return placeholder | 3 | 0 | 169 |
| Byte-state baseline with wide helper arguments | 174 | 0x48 | 136 |
| Signed-state local | 173 | 0x48 | 35 |
| Selected active/state local | 173 | 0x48 | 11 |
| Reversed comparisons / explicit constants | 173 | 0x48 | 11 |
| Reordered mode-six filter control | 172 | 0x48 | 160 |
| Selected with expected-word guards | 173 | 0x48 | 0 |

Eleven guards account only for the closed allocation of constants 1 and 7
between s6 and s7, including both definitions and every use, and commutative
equality/inequality operand order. Offsets: `0x070`, `0x074`, `0x0BC`, `0x0E8`,
`0x11C`, `0x124`, `0x12C`, `0x160`, `0x168`, `0x178`, `0x204`.
There are no insertions, omissions, changed branch/call targets, memory accesses
or argument values. Tests mechanically verify the cycle and unchanged branch
opcode/displacement. Raw and guarded C both pass the behavior corpus. Stale
expected words are rejected; omitted guards are not exact, and partial register
cycles have behavior-changing witnesses.

Exploratory s16 helper-view declarations inserted redundant narrowing words;
the wide types remove them. Typed parameter lists on the two retained renderer
placeholders caused IDO argument-home stores and were not adopted. Their
original no-argument placeholder shapes remain, with corrected Gfx pointer
return types and unchanged entire slots. The unused scan declaration in
`game_45B80.c` is aligned. This does not restore those renderers or callers.

## Qualification

`tools/tests/test_game_actor_display_scan_match.py` passes **13 tests in
35.826 seconds, no skips** against the final rebuilt ELF:

- **4868 cases**, each executing the complete retail, raw-C and guarded-C
  bodies. The 4536-case gate matrix uses an independent predicate; additional
  cases cover sparse/mixed full tables, all modes, both stack phases, signed
  views, all slots, live callback mutations and redirected/zero/double advances.
- **193536 native C cases** cover all 256 state bytes, id/flags/activity gates
  and signed alpha boundaries using the actual SDK display-list macro.
- **587 additional native cases** cover full tables, signed views, mutations
  and returned cursors with 32-bit pointers and mapped storage.
- Ordered reads/writes, arguments, diagnostic receipts, fences, cursor returns,
  fifth stack argument and saved-register restoration agree three ways.
- All **172 reachable retail words** execute. The duplicate id load at
  `0x1502BBA4` has no control-flow predecessor: all preceding paths branch
  around it and no branch/jump targets it. That retained word is byte-exact.
- Full pre-edit slot lengths/hashes of caller placeholders `func_150195A0`
  and `func_15019CC8`, and renderer placeholders `func_1502C408` and
  `func_1502C974`, remain unchanged. They are not restored active C callers.

Callbacks are deterministic opaque fixtures, not actual full renderer bodies.
This qualifies the scan's contracts and instructions, not complete gameplay,
hardware rendering, final pixels or PC runtime acceptance.

## Measured Progress

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3301 / 5463 (60.42%) | 0 | 2162 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2628 / 4790 (54.86%) | 0 | 2162 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The final rebuild succeeds. A pre-edit address/length/SHA-256 snapshot of all
**6060 function slots** proves that only `func_1502BAD0` changes, with no
added/deleted slots. Complete protected sections remain retail-exact: Init
code **164048 bytes**, Init data/rodata **17376 bytes**, Debugger **19800 bytes**,
Game data **189088 bytes / 720 owners**. Conversion totals and **47 retained
Init ASM functions** remain unchanged.

The patch table has **10606 rows**, no duplicate keys, SHA-256:
`22f784b5c5dc38114c6d2ed9da81fb74ea9ac3eb5c97c4a3be57d129d1fa4099`.
`make tools-check` and `git diff --check` pass. README changes contain aggregate
counts only; function detail stays in DOCS.

The combined actor/viewport/SDK/resource/matching/tool regression passes
**302 tests in 265.481 seconds, no skips**, against the final rebuilt ELF.
All **2920 relative links** in the touched README/status/roadmap/working-note
documents resolve. Existing unrelated duplicate-recipe and pointer/integer
warnings remain; the isolated recovered candidate has no diagnostics.

## Reproduction

Run from the `64CBFD` root in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_actor_display_scan_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_display_scan_match -q -f
wsl make tools-check
git diff --check
```

For the combined regression prepend `tools.tests.test_game_actor_display_scan_match`,
`tools.tests.test_game_viewport_renderer` and `tools.tests.test_game_dual_matrix_emitter`
to [Note 1004's resource/matching/tool modules](1004-game-resource-size-query-direct-match-and-aligned-header-20261005.md).

## Host Boundary And Next

Read-only sibling inspection finds translated `func_1502BAD0` in
`64CBFDOGL/recomp_out/.c`, including its frame and signed-view extension.
No maintained `src/pc` reference/override is found. Preexisting translated
caller guards are not a new PC fix or rendering acceptance. No sibling source,
build, save or frozen Release artifact is changed.

Next bounded target: `func_1502BD84`, **88 words / frame 0x20**, ROM **0x59234**,
the adjacent per-actor update dispatcher. Its retail body clears actor +0x1D4,
handles state/id gates, sequences update callbacks and rereads callback-mutated
activity/flags before optional work. Preserve those reads, the original slot
home and callee lifetimes. Reference: `conker/asm/58F80.s`.
