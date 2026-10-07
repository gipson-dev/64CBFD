# Game Scaled Sphere Query Direct Match

Date: 2026-10-07. Baseline: `b20f0f46`,
[Note 1089](1089-game-scaled-sphere-query-capture-lifetime-20261007.md).

The complete `func_15145AD8`, VA `0x15145AD8..0x15145C90`,
ROM `0x172F88..0x173140`, is now installed as semantic C and matches
**all 110 words directly**, under the existing **O2/g3** owner profile.
Frame `0x88`, every original private local, incoming homes, saved-register
lifetime, lazy gates, branches and helper-call delay stores are retained.
No target guards, profile/shared-header/padder changes, padding locals or
instruction insertion/deletion are needed.

## Scope Recovery

The [selected source](../../tools/experiments/game_scaled_sphere_query_address_view_candidates.py)
uses the corrected capture-first assignments from Note 1089. Put the two real
scale locals in a success scope after the dimension gates, then introduce the
real reciprocal local in a nested scope immediately before the normalizer.
All declarations are meaningful, used and in their original storage order.

That combination lets IDO place the normalizer's address setup around the
second comparison exactly as retail does. The extra inverse load and extra
comparison NOP disappear through compilation, not through patches. Actual
call relocations return to **`0x58/0xFC/0x168`**, with their original symbols.

The driver retains **51 new controls**, **191 measured controls** including
the prior 140. These counts are measurements, not distinct bodies or matches:

| Family | Controls | Measured Result |
| --- | ---: | --- |
| Incoming three-component array views | 7 | Bit-identical to capture-first C111 |
| Local member address views | 7 | Bit-identical to capture-first C111 |
| Individual floating multiply operand order | 7 | Bit-identical to capture-first C111 |
| Capture comma/result expressions | 4 | Three identical; inverse-first result is an effective negative |
| Real scalar register hints | 3 | Bit-identical to capture-first C111 |
| Normalizer argument address views | 4 | Bit-identical to capture-first C111 |
| Scale/inverse initializers in real scopes | 4 | C111/frame `0x88`/73 differences; both inverse-first forms fail the private-actor case |
| Reciprocal lifetime at six source boundaries | 6 | C111 or C112, original frame/locals; none exact alone |
| Capture scope plus nested reciprocal scope | 9 | Three direct C110 matches; six C111/71 differences |

All isolated diagnostics are empty. **33 controls are bit-identical** to the
prior corrected candidate. The three exact forms are
`nested3-reciprocal-normalizer`, `nested6-reciprocal-normalizer` and
`nested9-reciprocal-normalizer`. Select the first, which moves only scale,
inverse and reciprocal declarations; the six/nine-local forms are not needed.
The reformatted production body independently compiles to the same retail words.

The three effective negatives are `capture-scale-result`,
`scope3-initialize-inverse` and `scope9-initialize-inverse`. They spill inverse
before reading an aliased actor scale and retain success status one while
producing the old wrong output Y words `0x409A7C98/0xC014F92F` instead of
`0x41427C98/0xC009F25D`. A plausible word count or source capture expression
does not establish this lifetime.

Correction to the previous note: even the straight capture-first C111 body
reads **inverse then scale**, as retail does, and duplicates the inverse load,
not scale. Its important semantic improvement was reading scale before the
inverse spill. The direct C110 body now also retains the complete retail
instruction sequence, not merely that pair of captured values.

## Owner And Installation

The actual copied, production-preprocessed owner binds the exact standalone
target and all three target-relative call relocations. All **88 other
functions**, their relative relocation ownership, both normalized pools and
the same **two compiler warnings** remain unchanged. There are still 89 owner
functions.

The actual padder emits the full **110-word / 440-byte** target slot, with no
target overflow or trampoline. Assemble and link that slot, then independently
rebase each of the three helpers by `0x100000`: only its call word changes,
retaining the complete rest of the routine. No new production guard rows exist.

Install only the recovered body, its local eight-position prototype and the
dimension helper declaration in
[game_16EE20.c](../../conker/src/game_16EE20.c). Other helper signatures are
already visible and are not duplicated. The historical wrapper copied-owner
fixture now keeps its float ABI in a typed zero-return baseline body, so the
restored caller remains unchanged between baseline and selected wrapper copies.
Older caller candidates are still reproduced from an explicit placeholder
copy; they are not silently replaced by the new installed routine.

`make -C conker build/conker.us.elf -j2` succeeds with the two existing owner
warnings. Refresh `progress.csv`; conversion counts are unchanged because this
routine was already counted as a C placeholder.

## Qualification And Audit

[Nineteen fitting-caller tests](../../tools/tests/test_game_scaled_sphere_query_match.py)
bind the selected source into the real native fixture and reuse the complete
guest/reference bank: **37,808 bulk fixtures**, including **10,368 private-actor
cases**, and **126,720 actual 32-bit native finite calls** with all five real
C helpers. Do not add repeated historical/fitting executions as unique cases.

For the fitting caller, every reference-backed guest case additionally compares
**all guest memory**, including complete caller/helper frames, ordered read/write
events, all integer and floating registers, visited instructions, helper arguments
and snapshots to the original execution. Both code streams are also bound
word-for-word to retail. Source scope recovery does not depend on a scheduling
remap or a guard-input approximation. The independent reference still has its
documented bounded private-frame model; complete frame acceptance here comes
from the additional direct retail/emitted instruction execution comparison.

The final combined **112 tests pass in 688.694 seconds**, zero skips, errors
or failures. This includes all nineteen fitting-caller tests, both historical
caller suites, dimensions, sphere allocation/frame/recovery, wrapper,
projection schedule and owner pools. Initial fitting layout/owner/padder checks
pass: two tests in **6.668 seconds**. Corrected wrapper owner/padder checks pass:
two tests in **4.847 seconds**. Tool smoke checks, changed Python syntax and
whitespace checks pass. Documentation gate: **72 documents / 3,826 relative
links / zero broken**.

Full-run retail coverage remains caller 109/110, dimensions 40/41, normalizer
41/50, wrapper 49/53, sphere 126/126 and dot 13/13. The caller's unreachable
duplicate radius load remains present in the exact slot; it is not deleted.
Helper coverage is the actual connected domain, not an all-input claim.

```sh
PYTHONPATH=. python3 -m unittest \
  tools.tests.test_game_sphere_callee_allocation_match \
  tools.tests.test_game_sphere_callee_frame_recovery \
  tools.tests.test_game_sphere_callee_recovery \
  tools.tests.test_game_sphere_wrapper_match \
  tools.tests.test_game_projection_schedule_match \
  tools.tests.test_game_owner_pool \
  tools.tests.test_game_actor_dimensions_match \
  tools.tests.test_game_scaled_sphere_query_recovery \
  tools.tests.test_game_scaled_sphere_query_source_layout \
  tools.tests.test_game_scaled_sphere_query_match -v
```

The fresh whole-slot audit confirms **only `func_15145AD8` changes** among
6,059 functions. All 6,058 other slots, every address/extent, protected sections,
**720 data owners / 189,088 bytes** and **11,006 guard rows** remain unchanged.
Exact converted functions increase by one:

- Total: **3,356 / 5,466 (61.40%)**, previously 3,355.
- Game: **2,683 / 4,793 (55.98%)**, previously 2,682.
- Still different: **2,110**, zero address drift.
- Conversion counts/bytes, Init and Debugger are unchanged.

The main README changes only the two measured aggregate rows. Detailed recovery
belongs here and in the DOCS handoffs. No full-ROM checksum, gameplay, hardware,
MMIO, native private-stack aliases, all-float/FCSR/NaN-payload behavior, host
adoption, sibling/frozen Release, real save, runtime or push claim.

## Resume

Bank this direct caller recovery with its green regression/audit receipts.
The scaled-sphere caller is no longer the open one-word fit task. Continue Game
matching with the still-open sampler `func_151432BC`; oriented `func_15142600`
also remains open. Resume the sampler from
[Note 1074](1074-game-area-sampler-qualified-recovery-20261006.md): existing
C252 versus retail C254, frame `0x50`, 109 positional differences. Its next
source-lifetime/exit work is the two retail per-path RA reloads and circle RNG
byte-store schedule. The live source still has its placeholder. Preserve its
existing experimental and negative evidence instead of restarting the
completed sphere-helper chain.

Ignored receipts: `conker/build/game-scaled-sphere-query-address-view/` and
`conker/build/game-scaled-sphere-query-match-test/` (measurements, selected source,
copied owner/padder, coverage, before/after slot and data audits, progress).
