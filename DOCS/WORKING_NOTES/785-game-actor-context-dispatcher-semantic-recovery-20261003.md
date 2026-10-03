# Actor Context Dispatcher: Semantic Recovery

Date: 2026-10-03. Baseline: `bc70ec7`.

## Result

`func_15044380` replaces its zero-return placeholder with the complete
actor/context dispatcher. Its recovered interface takes three floats, an actor
pointer, a first-pass mode, and a second-pass flag, and returns the accumulated
first-pass result. Full retail assembly and call sites establish this interface;
the prior no-argument declaration was not a recovered signature.

The entire 107-word / 428-byte slot emits from semantic C with no padding and
no new guards/profiles. It remains non-matching at twenty word positions.
The frame is `0x60`, versus retail `0x68`; remaining differences include saved
context/argument offsets, register allocation, independent opening setup,
and commutative accumulation operand order. No broad instruction substitution
is justified or introduced. This is not a byte-exact or runtime acceptance claim.

## Recovered Contract

1. Publish `-32768.0f` to `D_800CBDF4` and `D_800CBDF8`, clear only actor byte
   `+0x275`, and call `func_15044660(actor, x, y, z)`. The focused actor layout
   also exposes the flags word at `+0xF8` without renaming other actor fields.
2. Capture byte `D_800CBDD3` after preparation, not on entry. It is held in a
   word-sized local, matching retail's word store/reload rather than inventing
   an early snapshot.
3. Visit contexts 3, 2, 1, 0. Read each `D_80089120` enable byte at its visit;
   require exactly 1. Only descending context 3 is excluded by actor flag
   `0x200`. Switch context, then read `D_800DBE62`; any nonzero byte permits
   `func_150AB1F0(x, y, z, actor, mode)`.
4. Accumulate every first-pass return with modulo-32-bit addition, preserving
   retail's `addu` behavior even when signed mathematical sums overflow.
   Explicit unsigned addition followed by target signed conversion avoids
   relying on host signed-overflow behavior.
5. For any nonzero second-pass flag, visit contexts 0, 1, 2 only. Use the same
   live enable/after-switch eligibility checks, then call
   `func_150AC3E4(x, y, z, actor, 0)`. Do not include those calls in the sum.
6. Always switch context to zero at the end, even with no enabled contexts.
   Only after that helper returns, restore the saved `D_800CBDD3` byte and
   return the first-pass sum. Resetting the context machinery and restoring
   this byte are distinct operations; do not replace them with one action.

Coordinate arguments remain by value across all helpers. Preparation's changes
to extents, flags, context byte, and later enable bytes are not discarded by an
extra reset or a cached-array snapshot.

## Compiler Boundary

Adding a file-wide void prototype for `func_1510F800` changed an already-matched
height wrapper's register allocation. The existing expected-word guard rejected
that build at `func_15045714+0x20`. A block-scoped void declaration then failed
IDO's compatibility check against the slice's later implicit declarations.
The final source preserves the existing implicit-declaration convention for
this helper and ignores its return; no existing guards were relaxed or changed.
The helper's own interface/recovery remains a separate task.

The initial byte-sized saved-context local also emitted twenty differences
with a byte store/reload. Word-sized storage restores those access widths but
does not by itself recover retail's larger frame or allocation. The final
body's twenty differences must not be reported as twenty independent scheduling
words or a complete closed register rename.

## Linked Measurement

| Item | Verified result |
| --- | --- |
| Guest interval | `0x15044380..0x1504452C` |
| Retail ROM interval | `0x71830..0x719DC` |
| Slot / body | 428 bytes / 107 words, no padding |
| Different word positions | 20 |
| Following symbol | `func_1504452C = 0x1504452C`, unchanged |
| SHA-256 | `043673bf0162cba94bc5f48bf0283957161914b3ec75225e8f8ca21154421de6` |

## Verification

Fourteen source-extracted freestanding 32-bit tests in
`tools/tests/test_game_actor_context_dispatch.py` verify exact event traces,
descending/ascending bounds, any-nonzero second-pass flag, exact enable-byte
checks, the context-3-only exclusion, after-switch eligibility, preparation-time
flag/context changes, future enable mutation, by-value arguments, unchanged
post-preparation extents, modulo-32-bit accumulation, and actor byte/layout
preservation. Preparation/context/dispatch helpers are instrumented mocks.
These tests qualify dispatcher orchestration, not the actual helpers or gameplay.

Completed successfully:

```sh
make -C conker NON_MATCHING=1 all match-progress -j4
python3 -m unittest tools.tests.test_game_actor_context_dispatch
python3 -m unittest discover -s tools/tests
make tools-check
```

All 405 repository tool tests pass. Twenty-two exact regression slots remain
retail-identical: restored actor preparation, nineteen earlier exact routines,
and both matrix wrappers. Eight earlier non-matching hashes remain unchanged.
The 5,712-byte collector, 504-byte producer, and 16-byte return closure remain
exact. Both entire Init sections remain exact with the lengths/hashes in
[Note 782](782-init-pause-resume-conversion-assessment-20261003.md).

## Progress And Next

Aggregate numbers and README tables are unchanged because the placeholder was
already counted as C: total 5,462 / 6,042 C rows and 3,268 / 5,462 exact;
Game 4,789 / 5,321 C rows and 2,595 / 4,789 exact; zero drift, 2,194 different
C rows. Detailed recovery updates remain in DOCS.

The then-pending `func_1504452C`, initially described here as a sibling
dispatcher, is actually a three-vertex transform; Note 786 recovers and matches
it. Current actor-preparation assembly is exact, but dimension helper
`func_1507C3E0` remains empty. Context wrapper `func_1510F800` already has a
no-argument forwarding body; its explicit context argument remains to recover,
not an empty-body implementation. Recover those interfaces/dependencies before
claiming this actor/context chain is usable.
Matching this dispatcher and the earlier matrix/actor/terrain/entity routines
remains open; Init's two small candidates remain deferred under Note 782.

No compressed-ROM build, guest execution, host-port build, or gameplay test
was performed. The sibling port and frozen Release artifacts were untouched.
