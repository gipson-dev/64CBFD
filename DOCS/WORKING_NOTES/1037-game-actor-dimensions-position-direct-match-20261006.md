# Game Actor Dimensions And Position Direct Match

Date: 2026-10-06. Starting checkpoint: `7a7ed06e`.

Continuation: [Note 1038](1038-game-alternate-actor-dimensions-direct-match-20261006.md)
completes the adjacent alternate-field query and its two retail padding words.

**`func_1515C1A0` matches all 41 words / 164 bytes directly from C.**
VA 0x1515C1A0..0x1515C244, ROM 0x189650..0x1896F4, no frame.
Replace the zero-return stub in
[generated_188F90.c](../../conker/src/game/generated_188F90.c) with a void,
four-pointer query using existing `struct127`/`struct17` layouts. Only this
owner gains a `structs.h` include; no shared header/prototype, data, symbol,
metadata, profile or guard change. The existing O2/g3 profile matches directly.

## Recovered Operation

Read actor ID byte +4 once. For IDs below 0xBB, write signed halfword +0xD2
as float to the first dimension output, then signed +0xD4 to the second.
Copy actor X (+0x14), add signed halfword +0xD6 to actor Y (+0x18), then copy
actor Z (+0x1C) to the point output. For IDs 0xBB..0xFF, write 1.0f to both
dimension outputs and copy XYZ with no vertical adjustment.
Dimension terminology describes the query shape; full caller/geometric
meaning is not established by this bounded recovery.

The retail `ID != 0xFF` test after `ID < 0xBB` is redundant but remains in
the source to preserve its branch and delay layout. Its taken branch is
impossible for the already-cached byte. No early output snapshot is used:
each dimension store precedes the next halfword load, X is stored before
the vertical-offset/Y loads, and Y is stored before the Z load. Output
pointers may overlap one another or actor fields, changing subsequent reads.
Do not cache all fields or substitute unsigned halfword loads.

## Compiler Controls

[Driver](../../tools/experiments/game_actor_dimensions_candidates.py) uses
the real SDK, actor and point headers. Four forms (direct fields, cached ID,
reversed floating-add operands and early return) under O2/g3, O2, O1/g3 and O1:
**16 controls**, empty isolated diagnostics. The first direct-fields O2/g3
form already matches; no experimental profile is installed.

- Direct fields, cached ID and early return each match all 41 words under
  both O2 profiles: six exact controls.
- Reversing the addition operands leaves 41 words but eight differences.
- O1 forms are oversized: 43 words, or 44 for cached ID, with 43 differences
  including overflow. They are not installed.

Ignored receipts: `conker/build/game-actor-dimensions/` and
`conker/build/game-actor-dimensions-test/`.

## Qualification

[Five tests](../../tools/tests/test_game_actor_dimensions_match.py) bind the
direct linked slot, no guards, real source and compiler inventory; compare
an independent ordered-access reference with retail and recovered guest C;
and run the actual C in native fixtures:

- **36864 guest cases, two bodies**: every ID byte, six signed-dimension/
  finite-coordinate sets, twelve output-alias layouts and two stack phases.
  Compare every non-stack memory byte and the complete ordered read/write
  trace, no helper calls, preserved saved GPR/FPR/SP/RA lifetimes.
- Aliases include shared dimension outputs, dimensions inside the point,
  point inside the actor, a first dimension store corrupting the next signed
  halfword, height corrupting the vertical offset/Y, and writing the ID after
  the initial gate. Later reads retain their retail timing.
- **40 reachable retail words execute**. The branch-likely delay word at
  0x1515C1B4 is structurally unreachable because its taken ID==0xFF branch
  follows ID<0xBB. Tests bind the five gate/branch/delay words; complete direct
  byte equality also covers the unreachable word. No 41-word execution claim.
- **18432 native cases** use the actual header's actor prefix through the
  signed fields, actual `struct17`, explicit offset checks and the selected C.
  Compare all 1088 storage bytes to a sequential independent reference.
  Native little-endian overlap effects are checked against native memory;
  this is not a claim that cross-halfword byte effects equal big-endian guest
  effects. Guest tests independently cover the retail big-endian footprints.
- Negative controls detect the zero stub, threshold 0xBC, unsigned dimension
  conversion and missing vertical offset. Shared guest runners are unchanged.

Four pre-install tests pass in **38.493 seconds**, no skips. Finite arithmetic
uses single-precision rounding, including signed zero and values around 2^24.
This is bounded aligned ordinary-memory evidence, not arbitrary invalid
pointers, full actor/caller domains, MMIO/concurrent inputs, all NaN/Inf/
subnormal/FCSR modes, hardware execution or gameplay acceptance.

The complete post-link suite passes **all 47 tests in 193.845 seconds**,
no skips: actor query, projection compiler/identity audit, descriptor measure,
pair clamp, indexed state-save, random timer and effect-packet regressions.

## Whole Linked Audit

NON_MATCHING ELF/progress/match-progress rebuild passes. All **6059 linked
slots** compared with the banked descriptor/projection checkpoint:
only `func_1515C1A0` changes; every address and slot size is unchanged.
Init, Init data, Debugger and Game data remain byte-for-byte identical.
All **720 Game data owners / 189088 bytes** remain retail-exact; all **10646
guard rows** retain their original content and order. No target guards.
Target SHA-256:
`d3b3a48ef8b6f98f80e1b59488c752dd391ac3b9d1089340178d62a66105902f`.

Independently compile the committed and current complete owner after the
normal assembly processor: both have empty compiler diagnostics. The build
retains the existing duplicate generated-recipe warning; no project-wide
warning-free claim. README changes only aggregate matching rows:

| Section | Byte-Exact Converted Functions | Drift | Different |
| --- | --- | --- | --- |
| Total | 3315 / 5462 (60.69%) | 0 | 2147 |
| Game | 2642 / 4789 (55.17%) | 0 | 2147 |
| Init | 492 / 492 (100%) | 0 | 0 |
| Debugger | 181 / 181 (100%) | 0 | 0 |

Converted counts/bytes remain unchanged because the old stub already counted
as C. No sibling host source/build/save/frozen Release change or push.
Root `make tools-check` and `git diff --check` pass. Documentation check:
3184 relative links across 20 documents, zero broken.

## Next Work

Inspect the adjacent `func_1515C244`, a 43-word slot still represented by a
zero-return stub. Retail shows the same ID gate and ordered XYZ query but
uses signed fields +0xE4/+0xE6/+0xE8, and ends with two padding words.
Existing `struct127.unkE8` is unsigned: use an explicit signed field view
without globally changing the actor layout. Qualify this twin independently
before installing it; no match is claimed yet. Projection frame/aliases
remain open in [Note 1036](1036-game-projection-wrapper-abi-and-frame-audit-20261006.md).
The Game matching goal remains active.
