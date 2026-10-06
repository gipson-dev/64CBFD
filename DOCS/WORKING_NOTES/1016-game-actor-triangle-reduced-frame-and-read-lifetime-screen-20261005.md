# Game Actor Triangle Reduced Frame And Read Lifetime Screen

Date: 2026-10-05. Starting checkpoint: `8bdb515c`.

Follow [Note 1015](1015-game-actor-triangle-private-home-recovery-20261005.md)
on `func_1502F490`. The installed typed reuse form preserves all seven retail
private-array homes while reducing the frame **0x160 to 0x140** and real
differences **273 to 242**. It emits **302 body / 302 slot words** directly
with default IDO 5.3 O2/g3/mips2/o32, without new guards, profile changes,
assembly changes, enlarged arrays, or body/slot padding.

It remains **non-matching**. Retail's frame is 0x138, and the opening
argument/register and ID/count read lifetimes still differ. This is partial
frame/instruction progress, not a new exact C function.

## Production And Private Homes

[generated_58F80.c](../../conker/src/game/generated_58F80.c) reuses the early
offset-table pointer for the SDK matrix cursor, the early vertex base for
the later buffer/source base, range counters for the later edge/blend loops,
and the determinant temporary for the later second weight. The ID and count
locals become direct nonvolatile table expressions. The SDK outer iterator
uses a less-than bound within the same six-element points array.

The selected form retains a typed range pointer. The experimental
range/point cast-reuse forms are **not installed**; neither removing that
pointer nor casting it into a different phase recovers retail allocation.

| Private Array | Retail And Installed Home | Size |
| --- | ---: | ---: |
| Vertices | SP+0xF4 | 12 bytes |
| Matrix indexes | SP+0x114 | 12 bytes |
| Six XYZ points | SP+0xAC | 72 bytes |
| Two first edges | SP+0x94 | 24 bytes |
| Two second edges | SP+0x7C | 24 bytes |
| New blend | SP+0x120 | 12 bytes |
| Old relative coordinates | SP+0x12C | 12 bytes |

The six real SDK output triples start at +0xAC/+0xB8/+0xC4/+0xD0/+0xDC/+0xE8.
A separate accepted-path trace distinguishes relative Y at +0x130 (5.5f,
then 1.25f) from blend Y at +0x124 (1.25f once) in both retail and installed
code. Equal final vectors alone do not establish their identities.

## Read Lifetime Boundary

On the three-range fixture, **before the first SDK call**:

| Reads | Retail | Installed |
| --- | ---: | ---: |
| Actor ID byte | 1 | 10 |
| Range count halfword | 1 | 3 |

The opening now saves the actor in s7 rather than spilling a0 as retail does.
The live compiler output therefore does **not** recover the original cached
ID/count loads or argument lifetime, even though this form has fewer real
word differences and passes the bounded external-effect/reference checks.
There are no intervening external calls in this early phase, but these
checks are not volatile/concurrent-read parity or hardware acceptance.
Do not describe those early reads as matched or normalize them with guards.

The offset-null return, unsigned interval/first-match behavior, ordered
buffer/source gates, fresh second-source load, signed vertex conversions,
six SDK calls, float evaluation order and aliased coordinate update order
retain their qualified external effects. No weight-sum gate is added.

## Compiler Controls

[Frame driver](../../tools/experiments/game_actor_triangle_frame_candidates.py)
freezes the previous private-home checkpoint independently of installed
`SELECTED`. It supplies **29 scope controls** and **48 reuse controls**
(`--reuse`), all compiling without diagnostics. Sixty-eight fitting forms
pass 66 bounded guest comparisons each: **4488 total**. Nine 303-word forms
exceed the slot and receive only the accepted-path home measurement, not
full qualification or installation.

All scope-only forms keep the 0x160 frame. Moving declarations into blocks
changes their homes without removing frame reservations. The reuse screen
can combine the exact 0x138 frame and all seven homes, but those forms have
295 body words and **299 differences**; correct frame size alone does not
recover the retail routine. The selected form is
`direct-id-count-for-less-cut-2`: 302 words / 0x140 frame / 242 differences.

[Recovery driver](../../tools/experiments/game_actor_triangle_transform_candidates.py)
now separates original `RECOVERY`, prior `HOME_RECOVERY`, and installed
`SELECTED`. A fail-closed reduced-frame helper binds the original recovery;
its output must equal the independently generated selected frame control.
Historical layout, lifetime and home controls keep their original bodies.

[Frame tests](../../tools/tests/test_game_actor_triangle_frame_candidates.py)
bind both inventories, scoped operation sequences, unchanged capacities,
fail-closed anchors, selected source identity, typed reuse, the live read
mismatch, and the separate relative/blend histories. Existing production
home and transform gates now require the 0x140 / 302 / 242 form; they do not
weaken the source/linked identity or semantic qualification checks.

## Linked And Test Audit

Across **6060 slots**, only `func_1502F490` changes. Every address and slot
length is intact. Matrix leaf/tail assembly, coordinate phase, buffer copy,
dispatcher, display scan and selector are unchanged. The actor update pass
remains separately non-matching at 109 differences.

Installed linked-slot SHA-256:
`8df5041be7cf2e4d7e923c4d338270f1d7158e5228b23fd68b47d8887c457afd`.

Complete Init **164048 bytes**, Init data/rodata **17376 bytes**, Debugger
**19800 bytes**, and Game data **189088 bytes / 720 owners** remain retail-exact.
The patch CSV remains 10622 rows, SHA-256
`b805f4aada0d4273b2af4ba67424da07de5bfc41e766449f29893b4b63bf011b`.

Focused qualification passes **64 tests in 170.165 seconds** (173.416 seconds
wall time), including 1719 three-way triangle cases, 64512 native reference
cases plus 33 aliases, 300 / 302 executed retail words and 53 / 53 connected
matrix/continuation words. The final five frame tests, including the added
read-history probe, pass separately in **0.748 seconds**, no skips.

Final qualification receipts, all exit zero:

- Selected regression corpus: **367 tests in 527.136 seconds** (529.528 seconds wall time), no skips; includes the final read-history probe.
- `make tools-check`: passes in 0.561 seconds wall time.
- Whitespace: staged `git diff --cached --check` passes.
- Relative links: **2993** checked across fourteen current/working documents; zero broken.

The focused run loaded the four initial frame checks before the read-history
probe was added. Its final five checks were rerun separately, and all five
are included in the fresh 367-test regression corpus. No test was skipped
or weakened to accept the remaining early-read mismatch.

Exact C totals stay **3304 / 5462**, **2631 / 4789 Game**, zero address drift,
**2158 different**. Conversion counts and retained Init ASM are unchanged.
README aggregates are accurate and untouched; details remain in working docs.
No sibling source/build/save/frozen Release change, host transplant or push.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_actor_triangle_frame_candidates
wsl python3 -m tools.experiments.game_actor_triangle_frame_candidates --reuse
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_triangle_frame_candidates tools.tests.test_game_actor_triangle_home_candidates tools.tests.test_game_actor_triangle_lifetime_candidates tools.tests.test_game_actor_triangle_transform_match tools.tests.test_game_actor_buffer_copy_match tools.tests.test_game_actor_attachment_phase_match tools.tests.test_game_actor_update_pass_match tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

Next: recover the **last eight frame bytes**, original actor argument and
single ID/count reads, and the retail SDK counter/output-pointer lifetimes,
while retaining all seven private homes and the qualified external effects.
Scope-only changes and an exact frame by themselves are disproven fixes;
direct table expressions are an intermediate non-matching form, not the
final retail read shape. No broad 242-word guard batch.

The full Game matching goal remains active.

Follow-up: [Note 1017](1017-game-actor-triangle-cached-iterator-audit-20261005.md)
banks cached metadata/SDK/mixed-bound controls without installing a frame regression.
