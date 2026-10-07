# Game Sphere Wrapper Direct Match

Date: 2026-10-07. Baseline: `3c1c988c`,
[Note 1082](1082-game-projection-wrapper-match-20261007.md).

Recover `func_151451F0` from its zero-return C placeholder. Its complete
53-word slot, VA `151451F0..151452C4`, ROM `1726A0..172774`, now emits directly
from C with the original `0x28` frame. No instruction guards, new constants,
shared-header changes, compiler-profile changes or padder changes.

## Original Contract

The nine incoming arguments are origin, direction, center, float radius,
float threshold, two point outputs and two distance outputs. The call to
`func_151452C4` forwards eight arguments, skipping the fifth threshold argument.
The fourth argument's float bits pass through MTC1/MFC1 unchanged. The only
relocation is `R_MIPS_26:func_151452C4` at offset `0x2C`.

After a true callee result, reject two negative distances; accept a nonnegative
first distance with a negative second; otherwise accept only first < threshold.
Preserve the original unordered comparison behavior, lazy second-distance
reads, and post-call threshold/output-pointer home reloads. A false callee
result does not imply that outputs are unchanged.

Live source verification corrected an earlier handoff assumption: the callee
is already restored through `GLOBAL_ASM`, not an active zero-return body.
Its complete 126 original words and the 13-word dot helper `func_15144A74`
remain byte-exact and unchanged. The callee copies the direction/origin before
writing two points/distances, then computes a final sign check using the live
origin and direction. That check can reject after all eight output stores.

## Compiler Controls

[Driver](../../tools/experiments/game_sphere_wrapper_candidates.py) reproduces
24 measurements: five wrapper source shapes and one callee trial under four
profiles. The selected nested-return body and explicit cached-first form both
match all 53 words with retail O2/g3. O2 without g3 differs five words. Early-
false reshaping emits 52 words but differs 38, while volatile threshold and
pointer-home forms emit 54 and 58 words. O1 controls are not installed.

The callee C trial emits 128 words/frame `0x68`, with 106 differences versus
retail 126 words/frame `0x70`; O2 differs 120, O1/g3 and O1 emit 164 words/frame
`0x60` with 159 differences. The trial is not installed or claimed byte-exact.

## Qualification

[Tests](../../tools/tests/test_game_sphere_wrapper_match.py) distinguish natural
connected execution from seeded boundary probes and the uninstalled callee trial.

- 8,424 finite connected cases exercise nine center patterns, six signed/zero
  radii, six thresholds, thirteen output/input aliases and two stack phases.
  Complete external memory, ordered writes, return values, forwarded arguments,
  raw/retail memory and complete read/write traces agree with an independent
  single-precision reference. All 126 callee and 13 dot-helper words execute.
- Six natural scalar-home cases overwrite the incoming threshold or either
  output-pointer home through the real callee's stores. Bounded mapped targets
  prove that the wrapper reloads those homes, rather than caching their values.
- 5,832 seeded helper-boundary cases cover negative/positive infinity, negative
  values, signed zero, finite positive values and quiet NaN comparisons. They
  separately prove all 51 reachable wrapper words, preserve its two dead
  duplicated comparisons, and clobber caller-saved registers. They are not
  natural geometry or FCSR/exception acceptance.
- 26,244 actual freestanding 32-bit C calls check nine-position staging, all
  eight forwarded words, radius float bits, output aliases and return paths.
  The native helper is a controlled boundary model, not the original geometry
  implementation; native parameter-home aliasing is not claimed.
- 324 connected caller cases execute both original setup fragments: 14 words
  at `151C893C`/ROM `1F5DEC`, and 18 at `15145C00`/ROM `1730B0`. Both actual JAL
  delay stores and eight caller-owned output values agree. Earlier transform
  context and return scaffolding are seeded, not complete-caller acceptance.
- Three compiled negatives change actual results: stale threshold, stale
  output pointers and incorrect sign combination. Oversized negative wrappers
  run at a separate bounded address so they cannot overlap the fixed callee.
- Seventeen missing-required-field cases fail the maintained mapped-memory
  gate on the intended read/store. A natural miss leaves output storage
  unmapped and still returns cleanly; a post-write rejection retains all stores.
- Copied owner preserves all 89 symbols, 88 neighbors' raw bytes/relative
  relocations, normalized pools and both original warnings. Raw target bytes
  match standalone C. Actual padder/link matches all 53 words and retains the
  sole call relocation under normal and alternate helper addresses.
- 1,404 additional finite external-alias cases qualify the callee C trial's
  bounded outputs against the independent reference. Its private layout,
  frame-sensitive aliases, native behavior and byte fit remain unqualified.

All 13 pre-install tests pass in 40.702 seconds, zero skips/errors/failures.
The final post-link suite adds production source/slot/no-guard checks and
retains the projection, original helper and owner-pool regressions: all 49
focused tests pass in 193.212 seconds, zero skips/errors/failures. This is a
focused post-link run, not a rerun of Note 1082's broader 206-test checkpoint.
The final post-regression linked audit again changes only the wrapper across
all 6,059 slots. Project-tool, Python syntax and whitespace checks pass;
65 documents/3,738 relative links/zero broken links.

## Installation And Audit

Install only the wrapper body and typed wrapper/callee declarations. Retain
the original callee assembly; the stale placeholder comment is corrected.
The CSV is unchanged: all 10,953 historical guards, zero new guards.
US ELF rebuild passes with only the same two owner warnings and existing
Makefile recipe warnings. Complete linked audit changes only the target across
6,059 slots. All addresses/extents, protected sections and 720 Game-data owners
covering 189,088 bytes remain unchanged. Both dependency slots remain exact.

Matching: total 3,354/5,465 (61.37%); Game 2,681/4,792 (55.95%); 2,111 different,
zero address drift. Conversion remains 5,465/6,042 and Game 4,792/5,321.
README updates aggregate matching rows only; recovery details stay in DOCS.

No FCSR/exception, NaN arithmetic/payload, hardware execution, complete-caller,
gameplay or host-adoption claim. No sibling/frozen Release/save/runtime or push
work. The broader Game matching goal remains active.

## Resume

Next dependency conversion: `func_151452C4`, currently exact original assembly.
Recover its original local ordering, `0x70` frame, 126-word fit, projection/root
lifetimes and final live origin/direction reads before replacing that assembly.
The maintained 128-word C trial and 1,404 bounded cases provide a starting point,
not permission to normalize frame/private-slot differences with word patches.
Keep the volatile perpendicular-square store/reload and actual dot helper.
Sampler `func_151432BC` and oriented `func_15142600` work remain open.

Ignored receipts: `conker/build/game-sphere-wrapper/` and
`conker/build/game-sphere-wrapper-test/`.
