# Game Graph Edge Crossing Recovery

Date: 2026-10-06. Starting checkpoint: `c7ecbce1`.

Recover `func_15086D94` in
[generated_B3020.c](../../conker/src/game/generated_B3020.c), replacing its
five-float zero-return placeholder with the complete horizontal edge-crossing
pass. This is **semantic recovery, not a byte match**: 206 emitted words plus
one ordinary padding nop in the 207-word / 828-byte slot, frame **0x78** rather
than retail 0x90, and **151 real word differences**.

Slot: 0x15086D94..0x150870D0, ROM 0xB4244..0xB4580. No new guards, compiler
profile, assembly edit, overflow, insertion/omission or data ownership change.
The already-matched 168-word root lookup and recovered 369-word parent remain
byte-for-byte unchanged; the parent still has 282 differences.

## Retail Contract

- Call `func_15085DA8(y)` once, preserving query X and the other float arguments
  across caller-register clobbers. Read the signed-halfword record count after
  this callback. Load the node allocation once, only for a positive count.
- Initialize the acceptance minimum to **100.0f**, retail constant 0x42C80000.
  The earlier temporary handoff's 200.0f was incorrect; the direct assembly
  check corrected the experiment before any production installation.
- Scan 16-byte owner records: unsigned mode +14 must be one and unsigned band
  +6 must equal the helper's **full s32** result. Do not narrow that result.
- Examine exactly five unsigned neighbor bytes at +9..+13. Skip 255 and every
  ID less than or equal to the owner index. There is no neighbor-count bound.
  The target's mode must be one; its band is deliberately not checked.
- Use signed-halfword X/Z at +0/+4. Subtract integer coordinates before float
  conversion. Node Y at +2 is irrelevant to this horizontal calculation.
- Form the edge normal, plane constant and start/end side values with retail's
  single-precision operation association. A crossing needs one strictly
  negative side and one nonnegative side. Parallel, coincident and both-zero
  sides do not cross. Preserve conditional sign changes, not an unconditional
  absolute-value replacement.
- Rotate the normal to the edge tangent, compute the crossing fraction, and
  check the finite edge bounds. The owner endpoint is excluded and the target
  endpoint is included. Update the minimum only for an accepted, smaller
  fraction.
- **Return uses the last computed crossing fraction, not the minimum.** The
  minimum only gates whether a hit exists (`minimum <= 1`). A later rejected
  finite-edge crossing or a nonwinning accepted crossing can change the final
  distance. Return sqrt(dx*dx + dz*dz) times that last fraction; otherwise -1.
  Do not fix this retail quirk or initialize a fraction that is never returned
  on the no-hit path. No null/count/geometry safety behavior is invented.

## Compiler Evidence

[Candidate driver](../../tools/experiments/game_graph_edge_crossing_candidates.py)
retains the straightforward semantic baseline, indexed/do-while/cursor forms,
side-copy lifetime controls and reused parameter-normal controls. It also
includes explicit wrong-minimum-result and narrowed-band negative controls.
The installed form reuses the side values after the crossing predicate.

| Form | Emitted Words | Frame | Real Differences |
| --- | ---: | ---: | ---: |
| Straightforward pointer baseline | 203 | 0x78 | 186 |
| Reused side values (installed) | 206 | 0x78 | 151 |
| Indexed do-while | 200 | 0x78 | 194 |
| Explicit edge cursor | 204 | 0x80 | 170 |
| Parameter-normal / side copies | 207 | 0x80 | 179 |
| Narrowed-band control (invalid) | 206 | 0x78 | 147 |

The invalid narrowed-band form is not installed despite its smaller diff.
Oversized 208/210-word forms are also rejected. A fitting source form alone is
not evidence of the retail frame, saved-register allocation or scheduling.
All 39 source forms / 78 profile controls complete with empty diagnostics.
The inventory writes an ignored `screen.json` under
`conker/build/game-graph-edge-crossing/`.

## Qualification

[Edge tests](../../tools/tests/test_game_graph_edge_crossing_match.py) compare
retail instructions, installed source and the frozen semantic baseline with
an independent float32 reference. They bind the float result, ordered height
calls, ordered external writes, full non-stack footprints and saved GPR/FPR
state at both stack phases. Native tests extract the installed source and
check 288 results plus all 8192 record bytes and globals.
There are **2177 three-way guest cases**. All **58 combined tests pass in
239.840 seconds**, no skips: 13 edge, 15 root lookup, 14 parent, three lifetime
and 13 visitor tests. The preceding 55-test run also passed before the three
additional endpoint/instruction/inventory checks were added.

Coverage includes orientations, zero movement, degenerate edges, signed-zero
and unordered coordinates, signed-halfword coordinate extremes, full band
returns, signed counts, target flags, all five edge positions, IDs 254/255,
self/lower-ID suppression, and neighbors outside the active count. Height
callback mutations exercise the post-call count/table snapshot and filtering.
Explicit two-crossing cases reject a minimum-result rewrite and preserve the
last fraction even when its finite-edge bounds fail. A narrowed-height control
also fails. Endpoint assertions distinguish excluded owner from included target.

**198/207 retail words are exercised.** The nine unvisited words at
0x15087004..0x15087024 belong to the negative-extent branch. They remain an
explicit bounded-coverage gap, not a claim of full executed-word coverage.
Local sign-bit negation and finite sqrt probes do not change shared oracles.

The native fixture suppresses GCC's maybe-uninitialized warning only around
the extracted body: every accepted crossing assigns fraction before reducing
the initially-100 minimum. No production initialization or test-runner warning
policy is changed. There is no FCSR/exception-mode/NaN-payload acceptance claim.
The root and parent behavioral fixtures still use opaque geometry/lookup
callbacks; these tests do **not** qualify the full production helper chain or
gameplay. Root ABI probes now execute the recovered geometric helper rather
than asserting the obsolete zero-return stub.

## Linked Audit

Before installation, all 6059 current slots exactly equaled the previous
checkpoint receipt. After rebuilding, every name, address and length survives;
**only func_15086D94 changes**, with the other 6058 slots unchanged.

Installed slot SHA-256:
`3bc4ecb9798225dd2b6f8cf921ec1bcd68467b62c38920374c373baf7087d1ad`.
Before/after slot, audit and behavior receipts are ignored under
`conker/build/game-graph-edge-crossing-test/`.

Init **164048 bytes**, Init data **17376 bytes**, Debugger **19800 bytes** and
Game data **189088 bytes / 720 owners** remain retail-exact. All **10643** CSV
guard rows are unchanged. No emitter/padding rule is relaxed.
Fresh ELF/progress/match-progress, `make tools-check`, whitespace checks and
**3036 relative links across nine documents** pass, zero broken links. The
existing duplicate generated_12D630 recipe warning is unchanged and unrelated.
The final comment-only rebuild preserves every audited slot and section hash.

Progress remains **3309/5462 total exact (60.58%)**, Game **2636/4789 (55.04%)**,
Init **492/492**, Debugger **181/181**, zero drift and **2153 different Game C**.
Conversion counts stay unchanged because the former stub already counted as C.
README aggregates/date remain correct and unchanged; detailed updates live here.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_graph_edge_crossing_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_graph_edge_crossing_match tools.tests.test_game_root_neighbor_lookup_match tools.tests.test_game_zone_neighbor_selection_match tools.tests.test_game_zone_neighbor_selection_lifetimes tools.tests.test_game_record_neighbor_visit_match -q -f
wsl make tools-check
git diff --check
```

Wait for relinking to finish before linked-image tests. Next continue matching
this helper's **0x90 frame, 0x50/0x54 private minimum/fraction homes, indexed
outer cursor, retained query X, and F12/F14 normal lifetimes**. The installed
form remains at 151 differences; do not cover them with a broad patch batch.
Then revisit the parent private homes/address lifetimes and connected helper
qualification. No sibling source/build/save/frozen Release change or push.
The full Game matching goal stays active.
