# Game Range Clamp Byte Match

Date: 2026-10-07; work began 2026-10-06. Baseline: `84af7d00`,
[Note 1074](1074-game-area-sampler-qualified-recovery-20261006.md).
Match only `func_15143D18`; keep the sampler and oriented-builder recoveries
uninstalled. No shared-header, compiler-profile or padder-algorithm changes.

## Recovered Shape

Retail: 36 words / 144 bytes, frame `0x10`, VA `15143D18..15143DA8`,
ROM `1711C8..171258`. Existing four-input void ABI: two signed-word output
pointers and two signed limits. No new interface or return-value invention.

First order the limits through the original integer XOR sequence. Then read
both output values and, when reversed, exchange them through the original
live XOR stores and rereads. Finally raise the first value to the lower limit
if needed and lower the second value to the upper limit if needed.
These are independent endpoint clamps, not `clamp` applied to both values.
An entirely excluded range can remain reversed after clipping; do not reorder
it again or invent an empty-range return code. Identical output pointers see
the sequential lower/upper updates. Caller-owned stack storage is valid.

Removing the unnecessary pointer-copy locals and using the argument pointers
directly recovers both saved pointers in s0/s1, the complete 36-word shape and
the original frame. The old body emits 29 words/no frame with seven padded
words; its values are correct, but its linked instructions do not match.

## Register Normalization

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_range_clamp_candidates.py) reproduces
baseline/selected forms under four SDK profiles: eight maintained controls.
Selected O2/g3: 36 words/frame16/13 raw differences. Other profiles do not
remove those differences. Disposable pointer, XOR-expression and lifetime
screens measured 68 further controls; none produced a direct exact function.
The production profile remains O2/g3.

The 13 differing words change only temporary GPR operand fields. Offsets:
`2C,30,34,3C,40,48,4C,54,58,5C,64,6C,70`.
Retail keeps the first value in v1 and the second in a1, with its XOR temporary
in v0 and the updated first value in a0. C allocates these short lifetimes
differently. The final upper-bound load/comparison uses t8 instead of retail
t9. Normalize those checked allocation choices, not a global register rename.

Every opcode, XOR/comparison operation, memory base/displacement, branch and
delay-slot location, saved-pointer slot, frame and return instruction already
agrees. No instructions are inserted/omitted; no arithmetic, ordering, frame,
constant, address or control-flow rewrite. The function has no relocations.
The actual padder emits all 36 retail words and rejects a stale expected word.

Append exactly 13 rows to the existing guard CSV: 10842 prior rows are immutable,
10855 total. Prior canonical SHA256:
`500b722e15c6ce30c740e6b55bc6feb0afe0a24e46df571c8aa94955b7b94639`.
New canonical SHA256:
`07904caf0a4b949a8e5b39f87e8aad4c0a1cc62cb92b3e999dd8d9c6b90211a4`.
[Guard-history helper](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/game_owner_pool.py) pins the prior
prefix and exactly the new rows. Point-transform checks now bind their exact
31-row block rather than assuming it remains the end of the shared CSV.
No historical guard check is weakened to accept an arbitrary suffix.

## Qualification

[Nine maintained tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_range_clamp_match.py)
include eight pre-install checks and a production source/slot/history gate.
The eight pre-install checks passed in 12.207 seconds:

- 3750 paired raw-C/retail guest cases cover all 36 words in both bodies:
  signed extrema, reversed/equal limits and values, two stack phases, distinct
  and identical output pointers, and caller-owned stack storage. Whole mapped
  memory, ordered output reads/writes and preserved GPR/FPR/SP/RA agree.
  An independent sorted-endpoint/one-sided-clipping reference also agrees.
- 1250 actual freestanding 32-bit native typed-caller cases cover signed
  extrema, reversed limits and identical output pointers. No signed arithmetic
  overflow or invalid native pointers are needed for these probes.
- Eight maintained baseline/profile controls retain the output/read/write
  contract under 32 bounded cases each, without claiming their slot shapes match.
- 250 seeded cases execute the original lookup caller's call/delay pair at
  `15143918/1C`, forwarding its caller argument-home addresses and signed limit.
  The delay instruction's zero save is checked. The remaining caller context
  and return are synthetic; this is not complete `func_151438D8` qualification.
- Four compiled semantic negatives change public outputs: missing value swap,
  reversed lower/upper gates and unsigned comparisons. Detection does not rely
  on different private stack frames or scratch registers.
- Copied original/selected owners retain all 89 typed function symbols, every
  one of the 88 neighbors' raw bytes and relative relocation identities,
  the 624-byte relocation-owned pool and the same two warnings. The selected
  target's raw bytes agree with the standalone compile and have no relocations.
- Actual owner assembly post-processing/padding reproduces the complete retail
  target and rejects stale metadata; production matches all 36 linked words.

These are bounded guest/native checks, not hardware, gameplay or host adoption.
No other whole caller is claimed. The clamp itself does not use the FPU.

## Production Audit

US ELF rebuild passes. Across 6059 linked slots, only `func_15143D18` changes;
all addresses/extents remain identical. Protected `.init`, `.init_data`,
`.debugger` and `.game_data` sections are unchanged. All 720 Game-data owners /
189088 bytes remain exact. All 10842 prior guard rows are unchanged.

Matching: total3347/5465 exact (61.24%), Game2674/4792 (55.80%),
2118 different, zero address drift. Conversion remains total5465/6042 (90.45%),
Game4792/5321 (90.06%); Init492/492 and Debugger181/181 C functions remain exact.
The root README updates only aggregate matching rows and their verification
date. Detailed recovery updates stay under DOCS.

Expanded post-link regression: all 111 tests pass in 368.274 seconds, with
zero skips/errors/failures. The nine clamp tests and ten sampler checks run
alongside the previous 92-test neighboring suite. Tool/syntax/diff checks pass;
57 documents / 3646 relative links / zero broken links.

## Sampler Exit Controls And Resume

[Supplementary exit/storage driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_area_sampler_exit_candidates.py)
adds 30 reproducible O2/g3 controls to Note 1074's 152 measurements:
all output-volatility subsets, scalar versus aggregate scratch storage,
function-wide versus per-case locals, byte/word angle storage, declaration
order and descriptor-field volatility. No exact sampler candidate.
New scalar forms are screening evidence, not behavior-qualified replacements.

All 16 output-volatility forms retain252 words/frame0x50/109 differences.
Per-case byte-scalar forms keep frame0x50 but have117 differences; function-wide
scalars shrink the frame to0x48. Neither recovers the two missing retail exits.
Do not add volatility, insert words or change profiles to hide that discrepancy.

Next: recover `func_151432BC`'s per-path RA reloads and circle-byte scheduling,
or reconstruct the next 272-word record-query placeholder `func_151438D8` using
the now-matched range helper. Preserve the original query's field masks, live
table reads, range clipping and last-match selection. Oriented builder
`func_15142600` still has its 27 private-layout differences.

Ignored receipts: `conker/build/game-range-clamp/`,
`conker/build/game-range-clamp-test/` and `conker/build/game-area-sampler-exits/`.
No sibling project, frozen Release, saves/runtime or push. Goal remains active.
