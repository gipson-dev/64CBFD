# Game Root Neighbor Lookup Direct Match

Date: 2026-10-06. Starting checkpoint: `fe924210`.

Recover `func_15085DF8` in
[generated_B3020.c](../../conker/src/game/generated_B3020.c), replacing its typed
zero-return placeholder. **All 168 words / 672 bytes emit directly from C**,
with the retail **0x80 frame** and complete saved-register lifetimes.
Slot: 0x15085DF8..0x15086098, ROM 0xB32A8..0xB3548.

No guards, new compiler profile, assembly edit, overflow, insertion/omission,
padding or data ownership change. The existing slice profile remains unchanged.
The parent from [Note 1023](1023-game-zone-neighbor-selection-lifetime-screen-20261006.md)
remains non-matching at 282 differences; its linked bytes do not change here.

## Retail Contract

- Narrow mode and band to signed bytes. Record band +6 and mode +14 are
  unsigned bytes: negative filters do not equal unsigned 128..255. Signed -1
  is the wildcard for each filter. Only mode zero enables the geometric check.
- Load the initial squared-distance minimum from D_8009D9CC, whose retail
  float is 100000000.0, once before helper calls.
- If the one-shot cache byte D_8008729C is not 255, read that node's signed
  halfword XYZ at +0/+2/+4, subtract the query coordinates, and optionally call
  func_15086D94 with five floats: query XYZ and horizontal deltas X/Z.
  The cache path does not apply the mode/band record filters.
- Accept a geometric result only when strictly negative; zero, negative zero,
  positive infinity and NaN fail. Negative infinity satisfies this comparison.
  An accepted cached node sets the bound to its full XYZ squared distance
  **plus 10**, but is not itself recorded as the winner.
- Consume a valid cache by writing 255 even if the helper rejects it, mutates
  the cache byte, or makes the record count nonpositive. An already-255 cache
  is not written.
- Initialize winner to 255. Scan the fresh signed-halfword D_80087290 count,
  with 16-byte records and fresh node-global/count reads after helper calls.
  Apply the two filters before reading coordinates or calling geometry.
- A candidate must be strictly closer than the current squared minimum and,
  for mode zero, pass the geometric helper. Equal distances retain the first
  winner. Keep the computed distance across the opaque helper even when it
  changes the current/future records or global table allocation.
- Return the full integer index, not a narrowed byte; indices 255, 256 and 511
  are explicitly exercised. Store truncated sqrt(minimum) in D_800D2354 even
  when no candidate wins. No null/count/coordinate safety behavior is invented.

## Compiler Evidence

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_root_neighbor_lookup_candidates.py)
freezes the straightforward pointer-based semantic body and the preceding
typed placeholder. **35 source forms / 70 profile controls** complete with
empty diagnostics. The unsigned-index forms are negative controls for the
signed count, not proposed recoveries.

| Form | Words | Frame | Real Differences |
| --- | ---: | ---: | ---: |
| Typed placeholder | 7 | 0 | 164 |
| Signed-byte arguments / retained node pointer | 171 | 0x90 | 168 |
| Explicit shifted index / retained node pointer | 168 | 0x88 | 10 |
| Inlined node addresses / shifted index (installed) | 168 | 0x80 | 0 |
| Installed form / default unrolling | 168 | 0x80 | 0 |
| Inlined addresses / Boolean flag assignment | 166 | 0x88 | 158 |

Explicit `i << 4` avoids a separately retained stride cursor. Removing the
unused named node-pointer home then closes the ten remaining frame/argument/
float-spill-home differences. No divide-by-one expression is needed in the
installed source. Keep the recovered repeated `check` conditions: collapsing
them changes retail's control flow and scheduling.

## Related ABI Change

The five-float geometric callee **func_15086D94 is not recovered yet**.
Its definition now declares its actual argument and float-result ABI and
still returns 0.0f. This is not a geometric implementation or a byte match.

Its complete 207-word slot contains four argument-home stores, the F0 zero
result and return sequence, followed by ordinary padding. Compared with the
old integer-return/no-argument stub, exactly this related slot changes in
addition to the recovered lookup. Two stack-phase probes bind the four homes,
store order and F0 result. No claim is made about the unused integer result.

The lookup's signed-byte argument declaration was first compiled against the
parent in isolation. Its complete linked 369-word slot is byte-for-byte
unchanged. The parent candidate declaration and native mock now reflect the
recovered ABI, and the obsolete lookup-placeholder assertion is replaced by
an assertion of the new complete direct match.

## Qualification And Linked Audit

[Lookup tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_root_neighbor_lookup_match.py)
provide **3275 three-way guest cases** against an independent float32 reference:
retail, installed source and the frozen pointer-based semantic recovery.
They compare the full non-stack memory footprint, ordered external writes,
ordered helper calls and integer return. Saved GPR/FPR state and both stack
phases are checked. This is not universal external-read-trace equality.

Cases cover cached bounds/consumption, signed argument narrowing and count,
unsigned record fields, wildcard filters, strict ties and ray predicates,
wide indices/counts through 512, empty-table gates, finite squared minima,
signed-halfword extremes, unordered coordinates and helper responses.
Helper mutations exercise fresh count/table globals, retained computed
distances/minima, cache writes, future filters/coordinates and final output.

**166/168 retail words are executed.** The two exceptions, 0x15085EC4 and
0x15085FEC, are branch-likely delay slots that cannot execute after the
preceding nonzero check. They are still included in the complete 168-word
byte comparison. Do not describe this as 168 executed words.

**1536 source-extracted 32-bit native cases** bind ordered call digests,
return/distance/cache values, all 8192 record bytes and the globals. Compiled
missing-cache-clear, inclusive-distance and byte-winner controls fail.
Twenty-four finite sqrt/truncate instruction probes and the two helper ABI
probes remain local to this fixture; no shared oracle is changed.

All **45 combined tests pass in 214.375 seconds**, no skips: 15 lookup tests,
14 parent tests, three lifetime tests and 13 visitor regression tests.
The parent retains 2990 four-way guest and 1424 native cases; its lookup is
opaque in those parent behavioral fixtures. This does not qualify the full
production height/geometry/lookup/visitor/gameplay chain. Native fixtures
and local FP probes use finite final sqrt/truncate values; full FCSR,
exception modes and invalid FP-to-integer behavior are not claimed.

Fresh ELF/progress/match-progress and `make tools-check` succeed. The existing
duplicate generated_12D630 recipe warning is unrelated and remains unchanged.
The complete **6059-slot audit** preserves every symbol, address and length:
only the lookup and geometric placeholder ABI change. All other 6057 slots,
including the parent, are byte-for-byte unchanged.

Lookup slot SHA-256:
`4f66c85e8e670ed6cadf9988aab2f86852f68870f5c3b0fd80c9a6d38aec000c`.
Geometric placeholder slot SHA-256:
`85079fb5dd1c845c89d3a052252e984c9e43fbb9c913ab5a830096f05b45b925`.
Ignored before/after/audit receipts live under
`conker/build/game-root-neighbor-lookup-test/`; the 70-control inventory is
`conker/build/game-root-neighbor-lookup/screen.json`.

Init **164048 bytes**, Init data **17376 bytes**, Debugger **19800 bytes** and
Game data **189088 bytes / 720 owners** remain retail-exact. All **10643 CSV
guard rows** are unchanged. No emitter/padding or ownership rule is relaxed.

Exact totals increase to **3309/5462 (60.58%)**, Game **2636/4789 (55.04%)**,
Init **492/492**, Debugger **181/181**, zero drift and **2153 different Game C**.
Conversion counts stay unchanged because both former stubs already counted
as C. README only updates the aggregate exact-match tables; detailed updates
remain in documentation.

Whitespace checks and **3030 relative links** across nine current/working
documents pass; zero broken links.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_root_neighbor_lookup_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_root_neighbor_lookup_match tools.tests.test_game_zone_neighbor_selection_match tools.tests.test_game_zone_neighbor_selection_lifetimes tools.tests.test_game_record_neighbor_visit_match -q -f
wsl make tools-check
git diff --check
```

Wait for the build to finish before linked-image tests. Next recover
**func_15086D94**, the 207-word geometric helper, so the lookup no longer
depends on a false float-return placeholder. The parent still needs its
private homes/address lifetimes matched. No sibling source/build/save,
frozen Release, host transplant or push. The full Game matching goal stays active.
