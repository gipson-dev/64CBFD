# Game Random Edge Emitter Semantic Recovery

Date: 2026-10-04. Starting HEAD: `44e900ab`.

## Result

Replace `func_150E76D0`'s zero-return placeholder in
`conker/src/game/generated_113D60.c` with its semantic descriptor builder.
This completes the two emitter helpers used by the recovered probability
dispatcher `func_150E7290`. It is a behavior recovery, not a byte match.

The production linked body is 155 words in the original 177-word slot,
with the original 0xB0-byte stack frame. All function addresses remain fixed.
There are 171 different aligned word positions and no instruction guards.
The remaining 22 words are slot padding; the difference count is not a count
of semantic errors.

## Retail Contract

Reference: `conker/asm/113D60.s`, `0x150E76D0..0x150E7994`,
ROM `0x114B80..0x114E44` (708 bytes / 177 words).

The first integer RNG result selects a variant with `& 3`. Incoming byte
flags have bits 0x06 cleared. Both descriptor scale fields receive the input
scale; kind is 5. ID, sizes, duration and opacity retain retail narrowing.
The common initialized fields follow the positioned helper's layout, with
the recovered constants and caller values. Unknown byte +0x11 and tail
+0x42..+0x57 remain unwritten, as in retail; tests do not read those bytes.
The submission callee copies the full 0x58-byte descriptor.

| Variant | Tag table | X | Y | Added flag |
| --- | --- | --- | --- | --- |
| 0 | Side | `145.0f - scale` | `sample * 160.0f - 80.0f` | 0x02 |
| 1 | Side | `scale - 145.0f` | `sample * 160.0f - 80.0f` | None |
| 2 | Top | `sample * 260.0f - 130.0f` | `110.0f - scale` | 0x04 |
| 3 | Top | `sample * 260.0f - 130.0f` | `scale - 110.0f` | None |

`D_80088A68` contains side tags 72, 73, 74; `D_80088A74` contains top
tags 69, 70, 71. Their retail words are in
`conker/asm/data/22D4E0.rodata.s`, ROM `0x22D528..0x22D540`.
The selected three-word table is snapshotted before the second integer RNG
call. Its unsigned result modulo three selects the tag, which is stored
before the float RNG call. Dynamically, every path uses two integer samples,
one float sample, then one submission. The range proof removes unreachable
default-branch scaffolding without introducing another input gate.

The helper forwards `pair`, mode, slot and context to
`func_1515548C(&descriptor, 0, pair, mode, 0, slot, context)` and returns its
complete result. It does not dereference `pair`; a null pair is forwarded.

## Verification

New suite: `tools/tests/test_game_random_edge_emitter.py` (five tests).

- 168 variant/unsigned-selector/float-sample cases check coordinates, tags,
  flags, initialized fields, argument forwarding and result propagation.
- Eight callback-mutation cases check table snapshots before the second
  integer sample and tag selection before the float sample.
- Thirty-two return/narrowing cases include null pairs and high-bit results.
- Connected dispatcher fixtures execute both actual production helper bodies,
  including all four alternate variants, sound/event/packet ordering and the
  positioned path. Alternate trace is `FFFIIIIFASEIIT`; positioned trace is
  `FFFFFIIIIPSEIIT` in the fixture's callback notation.
- An independent, warning-clean IDO O2 build fits the original slot and
  retains only the expected RNG/submission call targets. Its six static JAL
  sites include duplicated branch call sites, not six dynamic helper calls.

```sh
python3 -m unittest tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters -q -f
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
```

All 21 focused tests pass in 4.007 seconds, no skips. The production object
and final link succeed. Fresh linked measurements confirm entry
`0x150E76D0`, following entry `0x150E7994`, 155 body / 177 slot words,
176-byte frame, 171 differences and zero guard rows. `git diff --check` passes.

| Section | Byte-exact / C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,276 / 5,463 (59.97%) | 0 | 2,187 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,603 / 4,790 (54.34%) | 0 | 2,187 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The host fixtures and independent footprint check do not constitute guest,
hardware or visual acceptance. No full Init decoder corpus was rerun here.
Conversion and matching aggregates are unchanged because this was already
a non-matching C placeholder. README aggregate tables remain unchanged;
detailed updates stay in working docs. No sibling build, Release change or push.

## Handoff

- [x] Recover the alternate helper and preserve retail sampling/snapshot order.
- [x] Test both actual dispatcher/helper paths and verify production slot fit.
- [ ] Inspect and recover adjacent placeholder `func_150E7994` from its retail
  body and caller contract before changing its prototype or implementation.
- [ ] Pursue byte matching of `func_150E76D0` separately; broad compiler-flow
  differences are not candidates for a bulk instruction-guard replacement.

Init remains 492 C / 47 assembly functions. Its production adoption gates
and ordered candidates remain in Notes 926-936; this Game recovery does not
resolve or change those boundaries.
