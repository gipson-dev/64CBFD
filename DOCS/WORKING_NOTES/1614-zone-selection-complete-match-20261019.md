# Zone Selection Complete Match

Date: 2026-10-19. Consumer predecessor: `e1fb85cb`; tools predecessor: `743f234`.

## Installed Result

Complete `func_1508B3F8` now matches **all 369 words/1,476 bytes**, including
its 320-byte frame, VA 1508B3F8..1508B9BC, ROM B88A8..B8E6C. This closes the
query/scalar-home and store-order boundary in [Note 1613](1613-zone-selection-query-and-scalar-homes-20261019.md),
following the earlier [recovery](1022-game-zone-neighbor-selection-recovery-20261006.md)
and [lifetime screen](1023-game-zone-neighbor-selection-lifetime-screen-20261006.md).

The installed C keeps the 23 real local declarations and recovered query,
selection, zone and counter homes. Access the threshold through the actual
query object instead of its retained pointer, removing two redundant count
reloads without removing any public access from the final layout recipe.
The body retains its original name, `void(void)` interface and a concise
purpose comment. No shared header, dummy storage, volatile, physical register
binding, instruction array or compiler-profile override is introduced.

**This is not a direct compiler-only match.** The complete semantic C emits
367 words/frame 320 with 340 aligned raw differences. Checked source-origin
guards produce the entire 369-word retail routine, with no ordinary slot
padding. The other owner functions keep their existing compiler selections.

## Closed Source Origins

[Layout recipe](../../tools/experiments/game_zone_neighbor_selection_layout.py)
retains **364 unique source origins**, derives **five forms** and omits
**three words**. Every one of the 58 public memory instructions keeps its
unique source origin and typed opcode. All source words and 30 raw relocation
bindings are fingerprinted before transformation; all 32 output bindings and
the complete unresolved result are checked afterwards.

The omitted words are two cached-symbol LO address additions and one
duplicated 255 sentinel definition. None is a public or private memory
instruction. The five derived forms are the visited-pointer argument copy,
remainder-count copy, existing no-op in the coalesced-sentinel branch delay,
private query-end base and fresh publication-time node-symbol HI definition.

The recipe explicitly restores query S7, visited pointer S6 and sentinel S8,
the early counter/later zone stores, byte-winner casts, temporary register
allocation, address rematerialization, branch kinds/targets and delay-slot
schedule. The saved GPR/FPR area and all four named homes remain retail-exact.
The 367 expected-word rows comprise 109 identity rows, 255 other retained rows
and three omissions, with five insert-after cells. Every preceding manifest
byte is preserved; all original assembly remains untouched.

## Qualification

[Acceptance tests](../../tools/tests/test_game_zone_neighbor_selection_layout.py)
pass all 14 pre-install tests in **88.359s primary / 83.833s mirror**. The
installed runs pass all **16 tests in 99.624s primary / 97.327s mirror**,
including the existing production-slot contract and source-extracted native
footprint test. Mirror module paths are verified before redirecting only the
prepared consumer input roots; it retains separate owner/Make/ELF receipts.

- 2,990 four-way guest cases compare retail, normalized output, the raw
  367-word C and the prior home-layout candidate against the independent
  reference. Retail/normalized pairs also compare complete GPR/FPR/private
  memory, reads, stores, calls, events, condition and visited instruction PCs.
- Dedicated fixtures visit every one of the 369 parent and 84 connected retail
  visitor words. Signed bounds, strict/unordered floating gates, all candidate
  counts, ties, helper mutations and replaced globals/captured cursors remain
  covered. No query repetition or broader initialization is substituted.
- All 702 requested instruction-access-cut pairs fire and preserve literal
  state in both stack phases. Observer reads and opaque-provider accesses are
  excluded from fault gates. This closes the earlier store-order boundary,
  not a claim that observer-generated faults emulate hardware exceptions.
- Sixteen completed guest alias runs agree at the real query/scalar addresses;
  the same eight aliases reject the original unrecovered homes. These remain
  guest frame probes, not portable C calling contracts.
- 1,424 native32 fixtures pass O0/O2/O3 with trap-mode UBSan. A signed-overflow
  control fires SIGILL (-4), and three compiled semantic negatives reject
  repeated queries, lost queue clearing and inclusive distance comparisons.
- Independently assembled original parent/visitor code matches the normalized
  object and runs with raw C on three GNU maps, including HI/LO carry
  boundaries: 27 completed rebased runs. All 32 output bindings are exercised.
- 397 raw-word/binding stale controls, two corrupted recipes, two actual-padder
  stale controls and four complete-image corruptions are rejected.

The initial alias negative mistakenly used the already recovered homes; it
now uses the actual earlier SP+0xE8 source. Original-assembly fixtures add
function type/size metadata without changing instructions, order their link
sections so orphan metadata does not overlap code, and rebase the independent
visitor reference's globals too. Final tests use these corrected fixtures;
no acceptance gate is removed to accommodate those harness errors.

Height/root lookup and bzero remain bounded opaque providers in the behavioral
fixtures; the visitor is real connected retail code. Native tests exclude
negative guest-only indices and deliberate frame aliases. Full production
caller/helper/hardware/FCSR/gameplay acceptance is separate from byte identity.

## Production Proof

[Integration](../../tools/experiments/game_zone_neighbor_selection_integration.py)
compiles both complete owner profiles and preserves 72 other functions and
their pools. Actual padding retains all 73 owner addresses/extents and every
non-target byte. Primary and mirror independently reproduce the seven-command
Make shadow, unchanged normal overrides and the same first linked image.

The actual N64 production build succeeds and exactly reproduces the strict
prediction: **897 changed bytes, all within the target code; zero metadata
bytes or other serialization allowances**. All 6,056 other bodies, all 6,057
addresses and 189,088 protected Game-data bytes across 720 owners remain
fixed. Makefile and progress CSV stay byte-identical. The shared guard CSV
causes a broad object rebuild, not a broad source conversion. Existing
duplicate generated_12D630 recipes and unrelated pointer warnings remain;
this is not a warning-free build.

Tools `4a805fc` is committed before the consumer source/guards/docs/pin. Three
absent task files are copied into the independent mirror. Its previously clean,
identical production-contract test receives the same narrow migration as the
primary copy; all 1,430 older dirty leaf hashes and HEAD `ddbdd16b` are retained.
No mirror commit/reset/stash/clean, push, host/frozen Release, save, dependency
or advisory-agent operation is requested or performed.

Fresh totals: **Game 3,017/4,832 (62.44%)**, **overall 3,690/5,505 (67.03%)**,
1,815 different and zero address drift. Init 492/492 and Debugger 181/181 stay
exact. The owner is **69/73 exact**. Conversion remains 5,505/6,044 (91.08%),
86.08% bytes. Root README changes only its two matching aggregate rows.

```text
Source:     5f5f14255a3c9ec9892795be08f96460e00f5b7d440ab055643dc674adc5cfba
Manifest:   6ab62890a80f47ef85a9dc72c3da36c9a89f5b48844be9ba59613674dbca01cb
ELF:        cb2982f5a28805eb99f092abc2577a6c16a0b0789de32e436f9a9bf69108abe8
Raw C:      a9dec5c02b267241ecae64bac15157893d9c320a498f8fd5d654d5a208ab477c
Normalized: 9b20e1a7ccc254a4858aed8a140c6fb819f0cfa82624c3651ca05f4b0552c9c6
```

Receipts are ignored under `conker/build/game-zone-neighbor-homes/match/`:
pre-install/installed primary and mirror tests, separate owner/Make/first-link
outputs, the production log/audit, fingerprints, remaining-owner report and
Graphify baseline/audit. Refresh and audit the graph when banking this change.

## Next Function

Continue with **func_1508A6FC**, 678 words/2,712 bytes, frame 288,
VA 1508A6FC..1508B194, ROM B7BAC..B8644. It is a 12-byte zero-return C stub,
still 665 classified word differences, and calls the now-matched zone pass.
Read its entire retail body and caller/helper interfaces before deciding its
real signature and typed state views; the opening captures many state arrays.
The other remaining owner nonmatches are `func_15086364` (539 words),
`func_1508CAD8` (862) and `func_1508DC24` (681). Keep the wider Game goal open.
