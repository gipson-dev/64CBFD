# Game Owner Fixed-Span Point Initializer Byte Match

Date: 2026-10-10

## Baseline And Result

Continue after consumer 8c6e2a434635988cf42c9696622dabea7463b106 and mounted
tools d9f391de8b05357a66910c14c1cb3153f570c183, both active checkouts clean.
[Note 1204](1204-game-owner-x-axis-point-interpolation-byte-match-20261010.md)
banked the neighboring X-axis updater. The independently dirty older tools
checkout remains at ddbdd16b53ce60b054fb6e11bf0649a41f48375a. Its164 existing
dirty entries and two tracked-dirty fingerprints are recorded before changes.
Mirror only the two absent newly authored files, never overwrite conflicts.

func_151B4B78: VA0x151B4B78..0x151B4C1C, ROM0x1E2028..0x1E20CC,
41 words /164 bytes, leaf with frame0 and no calls or stack accesses. Replace
the false zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) with the complete
typed ten-point fixed-span initializer. All41 linked words match retail through
a closed compiler-normalization recipe. This is semantic C plus41 dependency
guards, not a plain-C match. No omissions, inserted instructions, pools or padding.

Use the existing workflow, scoped Graphify queries, compiler/parser/MIPS/native32/
padder/ELF/data helpers. Single Codex writer, zero Claude calls; no shared helper,
profile, OGL, Release, saves or editor changes. No push. Keep the wider Game goal
active. Root README receives aggregate rows only.

## Recovered Contract

Reuse OwnerPoints3A7C, ten24-byte point records at owner+0x48. Initial X is
-1000.0f, raw bits0xC47A0000. Read D_800AA3C8 before any output store:
address0x800AA3C8, ROM0x24EE88, bits0x435E38E4 /222.222229f. The read can
alias an output component or an otherwise unused input/velocity field.

Store all ten positions with repeated rounded single-precision addition, not
-1000+i*step. Every position Y/Z is positive zero; all velocity bytes stay
untouched. Start/end coordinates are unused. Clear owner+0x10 flag0x2 after
all position stores and return1. No input/velocity mapping or private stack
access is needed by the emitted routine.

Retail peels two points, stores their X values before the first four Y/Z zeros,
then processes the remaining eight points through two four-record iterations.
The final addition is in the branch delay slot and executes on the final
iteration too. Its result is unused; no hardware exception/FCSR equivalence
is inferred from that fact.

Registration is D_8008FAF8[5] /0x8008FB0C, ROM0x2345CC. The complete original
81-word func_151B3184 dispatches through owner+0x34 selector5 when flags0xC
are absent. Return1 retains the owner; skipped dispatch sets flag0x2. The
dispatcher and table stay unchanged.

## Compiler And Closed Recipe

[Candidate driver](../../tools/experiments/game_owner_points_span_candidates.py)
screens nine complete forms with the existing O2/g3 profile. The selected typed
loop emits41 words, frame0, no diagnostics/pools and27 raw word differences.
The explicit local count emits20 words and38 differences; a zero local emits
the same41/27 shape. No shared compiler-profile change is necessary.

The recipe validates the entire41-word compiler body, allowing only relocated
immediate fields at+0x8/+0xC. It constructs no replacement from retail bytes:

- Rename the closed three-register floating-role cycle: literal-start f12 to
  f2, captured-step f2 to f14, positive-zero f14 to f12.
- Move the first loop point's Y/Z stores before the cursor increment; fold their
  offsets from -0x14/-0x10 to+0x4C/+0x50, preserving physical destinations.
- Move the independent final X addition into the loop branch delay slot.
- Preserve every instruction exactly once through a closed41-offset permutation.

All41 manifest rows guard the actual object:27 changed words and14 unchanged
dependencies. HI16/LO16 relocations stay attached to the producing instructions.
The actual padder and independently assembled original agree under four symbol
sets including signed-low carry boundaries. No stale-layout bypasses.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_owner_points_span_match.py): all nine
tests pass before installation in17.087s and after installation in16.048s.
The first negative-control run exposed an unmapped literal pool in the fixture,
not production. Map the actual compiled control's pools and compare public
memory so a private stack spill alone cannot count as a rejected control.

- 7,680 guest cases /23,040 executions cover all256 flag bytes, fifteen finite/
  signed-zero/subnormal/overflow/infinity/NaN step patterns and both stack phases.
  All41 original/raw/normalized words execute. Complete memory, return and
  saved GP/FP/SP agree with an independent rounded reference.
- Raw ordered reads and write multisets equal retail. Normalized full ordered
  read/write events equal retail. Raw reordered-store fault prefixes are not
  claimed equivalent.
- 57 positive alias/independent-step cases include unused endpoints, initial
  X/Y/Z outputs, untouched velocity and later points. Six effective complete
  compiled negatives cover late constant read, wrong initial X, nine points,
  direct formula/repeated rounding, velocity clearing and wrong flag mask.
- 32 paired normalized fault prefixes agree; unused endpoint and velocity
  bytes can be unmapped. This qualifies guest instruction order, not portable
  C faults or real hardware traps.
- Actual native32 selected C passes8,192 finite full-memory cases,288 aliases
  and196 special-float cases. Size0x138, stride24 and existing layout offsets
  qualify. Initial X/Y/Z are bit-exact; arithmetic NaNs are classified, not a
  host/N64 payload or FCSR-equivalence claim.
- Twelve independent links/four entry-global symbol sets and32 guest rebase
  cases qualify relocations. Twelve complete original dispatcher cases retain
  registration, dispatch/skip flags and the no-removal contract.
- Actual copied owner preserves all16 neighbors, raw bodies, relative
  relocations and pools, with zero diagnostics. Actual padding preserves every
  other owner byte and the original func_151B4C1C address.
- Actual padder rejects each of41 individually stale words at its exact offset
  and independently rejects a stale HI16 relocation specification.

Prior unchanged neighbor receipts in Notes1203/1204 remain prior evidence, not
fresh reruns. The fresh copied-owner and whole-ELF audits prove their current
bodies unchanged. Historical curve suites retain their earlier owner/ELF
fingerprints; do not overwrite those receipts or treat an authorized neighbor
conversion as a curve regression. No live game/emulator/hardware qualification.

## Linked Installation And Bank

Fresh build/progress and make tools-check pass. The shared guard manifest
triggers the normal wider rebuild. Existing duplicate generated_12D630 recipes,
legacy pointer/long-double and old compiler fullwarn warnings remain; isolated
and copied target-owner compiles are clean, not the entire project build.

The complete rebuilt ELF equals the baseline after replacing only the164-byte
target slot and symbol extent. Symbol/string ordering is normalized; decoded
metadata agrees. Old guard bytes remain an exact prefix, with only41 qualified
target rows appended. Conversion CSV is byte-identical. Protected data remains
189,088 bytes /720 owners, all exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
The registered pointer and protected step constant remain unchanged.

Fresh matcher: Game2,749/4,816 (57.08%), total3,422/5,489 (62.34%),
Init492/492 and Debugger181/181 exact. Zero address drift /2,067 different.
Converted counts/bytes stay unchanged because the prior placeholder was C.
Bank tools1e345c1b87bf105eaeb0c0033fd98ac3fdad1be2 first, then consumer source,
guards, docs, aggregate rows and pin. The two new files are exact older mirrors;
its HEAD and tracked dirty fingerprints stay unchanged. No push.

Manual graphify update exits1, refusing a39,253 to17,472-node shrink. Retention
keeps19,398 nodes from2,972 excluded-but-present files. Existing0.9.20/0.9.26
and zero-node devcontainer.json warnings remain. No force/purge/install or policy
changes; qualify any fresh consumer post-commit hook separately.

## Next Target

func_151B4A14:89 words /356 bytes, frame0x68,
VA0x151B4A14..0x151B4B78, ROM0x1E1EC4..0x1E2028.
Registration D_8008FB10[1] /0x8008FB14, ROM0x2345D4. The recovered renderer
func_151B32C8 dispatches through owner+0x2E with eleven32-bit output pointers
and two byte outputs. The routine first captures owner+0x150, passes four local
output addresses to func_1502EC34, then reads the captured object's flag+0xA4.
Bit0 selects custom metadata; otherwise call the already recovered
func_151B498C with all original outputs and truncate its return to a byte.

Recover the complete14-argument signature, post-helper read/alias ordering,
custom writes, fallback call, byte return and actual0x68 frame/saved/local homes.
func_1502EC34 is itself a zero-return placeholder: inspect its complete original
body to establish the four-output contract; do not infer it from that C stub.
Qualify actual linked/connected behavior and preserve every newly matched
neighbor before installation. No next-target candidate is installed here.

The larger curve func_151B3FDC remains an uninstalled zero-return stub. Preserve
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md):
the186-word/frame0x120 diagnostic qualifies fourteen float homes but shifts saved
writes8 bytes downward and overflows32 bytes. One complete form must combine
frame0x118/saved homes, private float/access lifetimes and178-word extent, then
match all words. Create a fresh scoped owner/ELF baseline for future curve work.
