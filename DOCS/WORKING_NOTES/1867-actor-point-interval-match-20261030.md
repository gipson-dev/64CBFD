# 1867: Actor point vertical interval restored from C

Verified 2026-10-30. `func_150EAF50` replaces its zero-return placeholder in
[`generated_118400.c`](../../conker/src/game/generated_118400.c).
All 56 body/slot words and three JAL relocations emit directly from C on the
first typed source screen. No guards, inserted/omitted words, frame adjustments,
alignment words, compiler-profile changes, shared-header edits or guard-manifest
changes are needed. The function retains its original 56-byte frame, S0 at SP24,
RA at SP28, local three-float array at SP44 and homes at SP60/64/68.

Actual linked recount: **3,944/5,506 (71.63%)** total,
**3,271/4,833 (67.68%)** Game, Init 492/492, Debugger 181/181, zero drift.
The 75% goal stays active: **186** more to 4,130/5,506. C inventory and progress
CSV remain unchanged.

## Recovered behavior

The four-argument interface is `s32(f32 *position, u8 *actor,
HeightResult71820 *result, u8 mode)`. Modes other than one/two return zero before
pointer dereferences. Mode one selects matrix point 0x21; mode two selects 0x1D.
The matrix pointer at actor+0x1D4 and selected point go to `func_15142314`, which
fills the position. A null result then returns one.

Otherwise the routine captures `(x, y + 10.0f, z)` in its local array, initializes
the result with `func_1504715C`, then returns
`func_15046C80(start, 0, position[1] - 50.0f, result)`. The last Y read occurs
after initialization. Overlapping output/result/actor buffers therefore matter.
The declarations reuse the actual named height-result/actor tags, the resolver's
three-argument interface and the query's u16 selector and float ABI.

The existing qualified `func_150BA930` height-position routine supplied reusable
typed interfaces, alias effects and the original helper contracts. The alternate
source's integer coordinate reads and incorrect pointer types are not adopted.
No volatile parameters or artificial frame padding are introduced.

## Qualification

Ignored artifacts are in `conker/build/game-position-action-150EAF50-match/`.

- Raw body SHA-256:
  `3e31e93eba547cc540a3ec5a65296d850bb4970292ba4e5e38da60b41e6c2acd`.
  All 56 words, bindings, two raw/padded neighbors and normalized owner pools
  are fixed. Actual Make's three commands reproduce the qualified padded object.
  Selected, owner and actual-Make diagnostics are empty.
- Guest: 3,136 cases / 9,408 executions, all 256 low-byte mode values, six
  position layouts, four result layouts, helper mutations and float-word
  boundaries. Independent public/visible-output references agree with all
  calls, packets and results. Original/raw/padded programs agree on complete
  state and traces. There are 93 fired access prefixes, including 13 delay-slot
  cuts, 192 rebased cases in three layouts and 35 private-home/alias cases.
- Reachability: 55 of 56 body words execute. The retail duplicate `lwc1` at
  VA0x150EAFC8 / offset0x78 is unreachable behind the branch-likely/null-result
  paths, but remains byte-exact. It is not padding. The null-result path annuls
  its conditional position load. Raw corruption controls include this dead word.
- Original caller: the complete aligned ROM scan finds exactly one direct JAL,
  at ROM0x118570, and no function-pointer words. The sixteen-word window at
  VA0x150EB090 / ROM0x118540 runs 192 cases per program. Both matrix-disabled
  and enabled paths, the low-byte mode, parent-stack position/result objects,
  and the return-dependent continuation/skip routes are checked. This is a
  bounded caller window, not a complete-parent claim.
- Original helpers: 864 cases execute 121 literal retail words from the
  initializer and height query, with 88/89 and 29/32 words covered respectively.
  Entity-check, resolver and lower-query services remain bounded models; query
  status branches cover 0/1/2. The current ELF's initializer is still non-matching,
  while the query is byte-exact. Neither helper changes or gains credit here.
  The integration run executes their original ROM bodies; it is not proof that
  the current non-matching initializer is identical to retail.
- Native32: 15,360 finite-value/alias cases per O0/O2/O3 profile pass trapping
  UBSan and eleven effective controls for mode gates, both point indices,
  matrix offset, null result, margins, initializer, selector, stale height and
  returned result. Four position layouts and three result layouts use fresh
  untyped backing. Private argument-home mutations, fault ordering, FCSR and
  hardware NaN payload behavior are not portable C claims.
- Full image: production ELF equals the independent complete-file prediction,
  SHA-256 `65119a26d8b7044f738c5a52044c0c8e2529ebcba9e3fc749086aa76b6e04d7a`.
  Exactly 163 bytes change: 162 target-code bytes and one symbol-size byte.
  Metadata reorderings 0, exclusions 0. All 6,055 other bodies, every function
  address and 189,088 protected Game bytes across 720 owners are fixed.
- Both tools copies pass eight fresh canonical checks and their project-tools
  check. After production, two fresh installed checks run per copy, with six
  unchanged semantic checks explicitly reused through identical module/input/
  artifact fingerprints. The complete 16,961-file seal preserves other inputs.

Complete parent execution, all helper paths, hardware behavior and host-port
gameplay acceptance are not established by these checks.

## Banking and continuation

Tools are committed first at **c6c863a046314bf4985a9f97b1a2af95b864cd0a**, then the consumer pins that exact commit.
No push is performed. The independently dirty older tools mirror is preserved.
Root README edits are limited to its two aggregate exactness rows; detailed
updates stay in this note and documentation indexes. Graphify gets a scoped AST
refresh with explicit old-node/relationship retention, not a full extraction.

Next private screen: **func_15146890**. Deferred candidates stay uncredited until the
complete source, ABI, caller, owner, semantic, production and documentation gates.
