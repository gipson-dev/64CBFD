# Game Actor Lookup Byte ABI Direct Match

Date: 2026-10-07. Baseline: `2a02562a`,
[Note 1090](1090-game-scaled-sphere-query-direct-match-20261007.md).

`func_15142444`, VA `0x15142444..0x151424F4`, ROM
`0x16F8F4..0x16F9A4`, now emits **all 44 words / 176 bytes directly from C**
under the existing **O2/g3** owner profile. Frame `0x18`, selector home,
helper-call relocation, branches, delay slots and the unreachable final zero
assignment all match. No target guards, instruction insertion/deletion,
profile/padder/shared-header changes or padding locals.

## Sampler Lifetime Screen

Resume `func_151432BC` from
[Note 1074](1074-game-area-sampler-qualified-recovery-20261006.md), retaining
the supplementary controls in
[Note 1075](1075-game-range-clamp-byte-match-20261007.md).
The new [scalar-lifetime driver](../../tools/experiments/game_area_sampler_lifetime_candidates.py)
keeps the original 48-byte `struct209` scratch and moves only real rectangle
width / circle distance declarations into their individual case scopes.
Eight scope masks across break/early-return forms give 16 measurements:
14 new scoped forms and two unscoped anchors. All emit the same **252 words,
frame `0x50`, 109 differences**, identical raw words and relocation ownership.
The new maintained sampler test pins this result. Lifetime controls do not
recover the two per-path RA loads or the circle RNG-byte store schedule.

The sampler remains a production placeholder, with no new target guards.
Do not install it or add two words to hide the mismatch. The retained compiler
families now comprise 152 original, 30 supplementary and 16 lifetime
measurements; these are measurements, not distinct emitted bodies.

## Actor Lookup Recovery

The existing semantic actor routine compiled to 46 words, overflowing its
44-word slot. Nest the final pointer/validity checks, with one final NULL
return, to retain the original 44-word exit structure. The original final
zero assignment at `0x151424E0` is unreachable but remains in the exact body.

The last three allocation/scheduling differences come from the callee ABI.
The shared header declares `func_15083E90(s32)`, while its actual retail entry
begins `AFA40000 / 308E00FF / 01C02025`: save the incoming word, mask it to a
byte, then use that byte. The generated callee source also has its byte
signature, although its body remains a placeholder. Correct the declaration
**only in this owner**, using its established header-name override pattern.
There is only one call to this helper in the owner. Do not broaden this change
to the shared header or claim the helper's C implementation is recovered.

The [actor driver](../../tools/experiments/game_actor_lookup_candidates.py)
retains 31 source shapes under both word and byte helper declarations:
**62 O2/g3 measurements, 17 direct matches**, all under the byte declaration.
Controls cover flat/nested exits, outer else blocks, result reuse/scopes,
selector-local widths/assignments and pointer return typing. Select the simple
nested final check without a selector local. Isolated diagnostics are empty.

Contract:

- Selector is the low incoming byte. `255` reads candidate `+0x1D4` directly;
  it does not guard a NULL candidate or read its active word/identity.
- Other selectors reuse a non-NULL candidate only when its first word is
  nonzero and its byte at `+0x3B` equals the selector. A matching candidate with
  zero `+0x1D4` returns NULL without falling back to lookup.
- Otherwise call `func_15083E90` once. Read a non-NULL returned actor's live
  `+0x1D4`, after the call; return it only when that word is nonzero.
- Output is a pointer or NULL. There are no routine-owned external stores.
  No speculative candidate/returned-actor fields may be read on skipped paths.

## Qualification

[Ten actor tests](../../tools/tests/test_game_actor_lookup_match.py) cover:

- **24,552 guest fixtures**: every byte selector with high incoming bits,
  NULL/inactive/matching/mismatching candidates, zero/nonzero validity,
  NULL/distinct/candidate-alias lookup results and both stack phases.
  An independent reference checks return, ordered external reads/calls and
  readonly records. Raw C and retail additionally agree on **complete memory,
  all GPR/FPR values, events, calls and visited instructions**. All 43 reachable
  target words execute; the retained final zero assignment does not.
- **Eight callback fixtures**: change returned validity after lookup,
  including a result that aliases the original candidate. The live read is
  observed and the reference matches the callback write/call ordering.
- **1,664 connected-search fixtures** execute the complete original 72-word
  `func_15083E90` routine, with 26 selectors,
  active/inactive tables, eight early/unrolled/final/no-hit positions, both
  validity results and stack phases. All **68 reachable helper words** execute.
  Four retained loads at `15083F08/2C/50/74` follow JR/delay returns and have
  no incoming branch target; they are explicitly excluded from coverage.
  Independently check the scan result; complete guest effects also agree.
- **12,276 freestanding native 32-bit typed-caller cases**: every byte slot,
  lazy gates, result aliases and complete readonly records. The native lookup
  is an explicit bounded C model, not the callee's placeholder source.
- Six compiled semantic negatives change results or external read/call traces:
  full selector, wrong sentinel, ignored active word, wrong identity offset,
  wrong validity offset and ignored returned validity. Required unmapped bytes
  fail closed; sentinel NULL remains an invalid retail input, not a new guard.
- Production-preprocessed/postprocessed copied owners retain **89 functions**,
  all **88 neighbors**, relative relocations, normalized pools and the same
  **two warnings**. The raw target agrees with the isolated object. The real
  padder emits the complete 44-word slot without overflow; its original
  `R_MIPS_26` at `+0x78` independently rebases the helper by `0x100000`.

These are bounded guest/native checks, not hardware/gameplay/MMIO acceptance,
all-caller coverage, host adoption or a recovered C body for `func_15083E90`.

Final combined regression: **44 tests pass in 156.500 seconds**, zero skips,
errors or failures. Includes ten actor tests, eleven sampler tests, three pool
ownership tests, nine range-clamp tests and eleven point-transform tests.
An earlier 43-test run passed in 161.368 seconds before the final overflow
regression was added; do not add repeated runs as unique behavioral cases.
Tool smoke checks, changed Python syntax and whitespace gates pass.
Documentation gate: **73 documents / 3,843 relative links / zero broken**.

```sh
python3 -m unittest tools.tests.test_game_actor_lookup_match \
  tools.tests.test_game_area_sampler_recovery tools.tests.test_game_owner_pool \
  tools.tests.test_game_range_clamp_match tools.tests.test_game_point_transform_match -v
```

## Build And Audit

`make -C conker build/conker.us.elf -j2` succeeds with the two existing owner
warnings. No new guard rows; all **11,006 guards** remain unchanged. Protected
Init/Init-data/Debugger/Game-data sections and all **720 Game-data owners /
189,088 bytes** remain unchanged and exact. Conversion counts/bytes are
unchanged because the target already had semantic C.

The audit distinguishes **6,042 retail slots** from compiler overflow symbols.
Every retail address/extent stays fixed; **6,040 other retail slots** remain
byte-identical. The only changed retail slots are the restored target and the
one-word trampoline rebase below:

- Remove `__retail_overflow_func_15142444`, the old 46-word out-of-slot copy.
- The following `__retail_overflow_func_151F2E88` moves from `0x15F00E4C`
  to `0x15F00D94`, exactly **184 bytes earlier**. Its full **739-word body**
  has the same SHA-256; its instructions are not changed.
- `func_151F2E88` keeps its 727-word retail extent. Only its initial jump target
  rebases to that moved overflow. Replacing that one target reproduces the
  baseline slot hash. A maintained test pins both body and trampoline evidence.
- There are now **6,058 linked function symbols**, down from 6,059 solely
  because the target overflow symbol disappeared. All other symbols remain
  unchanged. Do not describe this as an unrelated Game routine being matched.

Exact converted matching advances by one: **3,357 / 5,466 (61.42%) total**,
**2,684 / 4,793 (56.00%) Game**, **2,109 different**, zero address drift.
Init492/492 and Debugger181/181 C functions remain exact. Root README changes
only its two aggregate matching rows; detailed recovery stays under DOCS.

## Resume

Bank this direct lookup match and its sampler screen. Resume the still-open
sampler's two legitimate exit/RNG-byte scheduling gaps, or the original-frame
oriented matrix builder `func_15142600` from
[Note 1070](1070-game-oriented-matrix-original-frame-recovery-20261006.md).
Do not repeat these scalar-scope controls as new evidence or reopen the
completed scaled-sphere caller. No sibling/frozen Release, save/runtime or push.

Ignored receipts: `conker/build/game-actor-lookup/`,
`conker/build/game-actor-lookup-test/`,
`conker/build/game-area-sampler-lifetimes/` and
`conker/build/game-area-sampler-test/`.
