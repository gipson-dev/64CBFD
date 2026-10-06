# Game Actor Position Queue Wrapper Direct Match

Date: 2026-10-06. Starting checkpoint: `bb6dcd65`.

**`func_1517D5FC` matches all 37 words / 148 bytes directly from C.**
VA 0x1517D5FC..0x1517D690, ROM 0x1AAAAC..0x1AAB40, frame 0x28.
Replace the zero-return stub in
[generated_1A89B0.c](../../conker/src/game/generated_1A89B0.c) with a typed,
six-argument void wrapper. Add only the owner-local `structs.h` include and
two accurately typed externs, matching existing shared declarations.
Existing O2/g3; no new guards/profile/header/metadata/symbol/data edit.

## Recovered Contract

The first three arguments are signed 16-bit coordinates. Retail stores their
incoming words in caller homes, sign-extends their low halves, and forwards
them to `func_1517D578`. The fourth argument indexes `struct108` actors from
`D_800DBFF0` at stride 0x9A0; float bits at actor+0x380 become the helper's
fourth argument. Two remaining integer arguments are forwarded unchanged;
the seventh helper argument is the byte at `D_800DDD1C` shifted right by three.
With the three leading integer arguments, the float travels through A3 as
bits, not as a leading F12 argument.

The wrapper reads the actor-base global, then the selector byte, then the
selected actor float before calling. It does not reread them after the helper
and does not gate the call when the queue is full. Retail's residual V0 is
the helper's residue, not evidence of a meaningful integer-return API;
the recovered source is void. Guest tests check that observed residue and
saved-register/RA restoration without inventing a new public return contract.

The existing 33-word `func_1517D578` is already linked retail-exact. Its C body
and **29 pre-existing guards** from [Note 560](560-game-three-entry-position-queue-writer-match-20260930.md)
are unchanged. It reads byte count `D_8008CEB0[0]`; counts below three select a
16-byte record in `D_800DDD28`. Ordered stores are XYZ halfwords, float at
+0xC, incremented count, trailing halfwords +8/+0xA, then selector byte +6.
For counts three or above it writes nothing. Wrapper recovery does not
replace or re-normalize the retained helper.

## Compiler Controls

[Driver](../../tools/experiments/game_actor_position_queue_wrapper_candidates.py)
uses actual SDK/actor headers and fixed retail anchors. Eight forms under
O2/g3, O2, O1/g3 and O1: **32 controls**, isolated diagnostics empty.
Five O2/g3 forms match directly: plain typed parameters, coordinate locals,
register parameters, volatile index and explicit byte stride. The first
plain typed form is installed; no volatility or alternative profile needed.

Wide parameters and volatile coordinates produce 34-word O2/g3 bodies with
35 differences; a precomputed actor pointer produces 37 words with 20
differences. Plain O2 produces 33..37 words and 28..36 differences. O1
coordinate-local forms overflow at 42 words/frame 0x40; most other O1 forms
produce 34 words/frame 0x28, while cached actor produces 35/frame 0x30.
All 32 exact lengths/frames/difference counts are bound by tests, not inferred
from body length alone. Ignored receipts:
`conker/build/game-actor-position-queue-wrapper/` and
`conker/build/game-actor-position-queue-wrapper-test/`.

## Qualification

[Seven tests](../../tools/tests/test_game_actor_position_queue_wrapper_match.py)
use unchanged shared guest instruction runners, an independent ordered-access
and queue reference, and the actual recovered C plus existing writer natively:

- **24576 opaque guest cases, two bodies**: eight index patterns, eight full
  coordinate-word triples, eight float-bit patterns, eight selector bytes,
  three callback-mutation modes and two stack phases. Compare captured seven
  arguments, complete non-stack read/write/call traces, every non-stack byte,
  callback return residue and saved GPR/FPR/SP/RA lifetimes.
- **37936 connected guest cases, two bodies**: 36864 cross-product cases,
  1024 full-byte sweeps and 48 source/queue-alias cases. All 256 count and
  selector bytes are exercised; the callback's trailing byte home, truncation
  of trailing integer arguments, three-entry gate and ordered stores agree
  with the reference. Queue aliases verify actor float capture before writes.
- **All 37 wrapper and 33 helper words execute** across these cases. No
  unreachable-word or padding coverage exception is needed here.
- **8192 opaque / 49152 connected native cases** use the actual complete
  `struct108` definition, actual queue-record definition and writer body,
  selected wrapper C, and explicit size/offset checks: actor 0x9A0, float
  +0x380, queue record 16 bytes. All actor and queue bytes, argument bits,
  count/selector/base globals and callback mutations are checked.
- Float words include signed zero, finite values, Inf, quiet NaN and a
  signaling-NaN pattern. This qualifies **bit transport**, not FP arithmetic,
  exceptions or complete FCSR behavior. No float arithmetic is introduced.
- Negative controls detect the zero stub, stride 0x980, actor field +0x37C,
  selector shift by two and incrementing the first coordinate.

Initial native fixture compilation caught its own scalar declaration for
`D_8008CEB0`, conflicting with the actual writer's array accesses. Corrected
the fixture to a one-byte array; both native tests pass in 1.056 seconds.
No production helper change was made to accommodate the fixture.

Guest negative/wrapped indexes are sparse mapped diagnostics, not evidence
that those indexes are valid gameplay actors or portable out-of-bounds C.
Native indexes are bounded 0..3. Evidence excludes arbitrary invalid pointers,
MMIO/concurrent memory, all caller domains, hardware execution and gameplay.

The complete post-link suite passes **all 59 tests in 255.215 seconds**,
no skips: actor queue wrapper, both actor queries, projection compiler/identity
audit, descriptor measure, pair clamp, indexed state-save, random timer and
effect-packet regressions. All seven new wrapper tests pass in that suite.

## Whole Linked Audit

NON_MATCHING ELF/progress/match-progress rebuild passes. Across **6059 linked
slots**, only `func_1517D5FC` changes; every address and slot size is preserved.
Init, Init data, Debugger and Game data remain byte-for-byte identical.
All **720 Game data owners / 189088 bytes** remain retail-exact; all **10646
guard rows** retain content/order, including the helper's old guards.
Target SHA-256:
`8b1838c4aa3febdb7ed38b129dfe4a035a32d7b237b93c51295afad046fa0e9c`.

Committed baseline and current complete owners compile independently after
the normal assembly processor: both have empty diagnostics. Shared headers
are unchanged. The build retains the existing duplicate generated-recipe
warning; no project-wide warning-free claim. README changes only aggregates:

| Section | Byte-Exact Converted Functions | Drift | Different |
| --- | --- | --- | --- |
| Total | 3317 / 5462 (60.73%) | 0 | 2145 |
| Game | 2644 / 4789 (55.21%) | 0 | 2145 |
| Init | 492 / 492 (100%) | 0 | 0 |
| Debugger | 181 / 181 (100%) | 0 | 0 |

Converted counts/bytes remain unchanged because the stub already counted as C.
No sibling host source/build/save/frozen Release change or push.
Root `make tools-check` and `git diff --check` pass. Documentation check:
3209 relative links across 22 documents, zero broken.

## Next Work

Inspect `func_1518E5D8`, still a zero-return placeholder in
`game/generated_1BA1D0.c`: 37 retail words, ROM 0x1BBA88, frame 0x18.
Retail calls the RNG twice, conditionally sets one flag bit, writes byte 0x16,
chooses selector three/four for `func_151429E0`, then writes byte 0xC8 and
halfword 0x401. Recover its seven-argument pointer ABI, post-callback reads
and output aliases before installation. This is static inspection, not a
new recovery or connected acceptance claim. Projection/pair-clamp frame work
remains open; the Game matching goal stays active.
