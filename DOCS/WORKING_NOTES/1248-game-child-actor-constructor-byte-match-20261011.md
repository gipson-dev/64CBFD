# Child Actor Constructor Byte Match

Verified 2026-10-11. Consumer baseline
05a9b4d683c605d003736a6c031b6a4e799e851e; mounted tools baseline
03d8ec2b8febcaab87d10cdcfec59f687e1c2d01. New tools
a9694bd84dbfcb35be65ffe696e48ebb319a3fc3 committed first. No push.
Single Codex writer, zero Claude calls; follow DOCS/AGENT_WORKFLOW.md.
Complete semantic C plus checked normalization now matches the full retail slot.

## Complete Match

Finish func_15083AC8, VA 0x15083AC8..0x15083DA0,
ROM 0xB0F78..0xB1250, all 182 words / 728 bytes and original 0x38 frame.
Note 1247 recovered its complete nine-argument constructor. This checkpoint
does not change that C, its callers, adjacent placeholders or compiler profile.
Raw IDO O2/g3 still emits 182 words / frame 0x50 with 125 differences;
do not describe the result as a direct, unguarded compiler match.

The explicit closed recipe changes 125 words and keeps 57 as identity checks.
All 182 compiler words have expectation rows, including those identity checks.
Check the 728-byte extent and all 22 original relocation sites. Six rows change
relocation ownership: move the initialization call into its retail slot and
rematerialize the actor-base HI16/LO16 pairs. The fitted body has all ten JAL
sites and all three original actor-base address pairs. No manifest insertions
or omissions, different function object, source padding or retail-word array.

- Close the S2/S3 actor/attachment/limit register cycle, keeping the original
  save slots and restoration order rather than blindly swapping saved words.
- Reduce frame reservation/return by 24; move incoming homes down by 24 and
  private mode accesses from SP+0x40 to SP+0x2C. Preserve unwritten capacity
  and all original caller-home reloads.
- Remove the cached constant actor-base spill from the emitted schedule and
  rematerialize its immutable symbol address for parent and final slot division.
  Derive both new pairs from the compiler's original symbolic address producer;
  independently retain their HI16/LO16 carry behavior and all signed divisions.
- Restore the value store to its call delay slot, parent quotient/status store
  schedule, flag/byte-copy temporaries and inclusive live-limit loop temporaries.
- Close unsigned magnitude/scale FP lifetimes: F16/F18 conversion, delayed F6
  scale load, original multiply operand order and unchanged result/store.
  Normalize the one commutative actor/index sum and final constant temporary.

The recipe contains the compiler fingerprint, not a retail replacement array.
Its independently transformed output is then checked against the original
assembly, ROM, production padding and independently linked symbol sets.

## Qualification

Thirteen final tests pass after the broad generated-slice rebuild. New immutable
baseline snapshots and reproducible receipts are under
conker/build/game-child-actor-constructor-match-test/. Historical Note 1247
receipts retain their earlier whole-ELF baseline; do not overwrite them.

- 2,224 cases / 6,672 full retail/raw/fitted guest executions agree with the
  independent ordered public reference. All flag/identity/inherit bytes,
  signed/full-width arguments, mode/resource/count boundaries, stack phases,
  self/offset aliases and callback-mutated incoming homes/globals qualify.
  Dynamically reach 179 retail words; three unsigned-LHU negative-conversion
  path words are unreachable through those inputs. All 182 match statically.
- 390 fired public-access fault triples / 1,170 failed runs agree in public
  partial memory/events/calls. Three explicit NULL-result runs fault at the
  first actor write after three callbacks; no synthetic NULL guard appears.
- Nine independent links at three entry/five-global/nine-helper symbol sets;
  21 cases / 63 runs qualify all ten calls and rematerialized address pairs.
  Independently assembled retail and fitted bodies match at each rebase.
- Seven effective newly compiled IDO negatives fail both behavioral checks and
  normalization. Different-word/extent/relocation diagnostics are accepted as
  distinct rejection reasons; an initial test incorrectly required only the
  word-error wording for a changed-extent negative, and that assertion was fixed.
- Native32 O2/O0 each run 18,432 independent-reference cases, 36,864 total,
  including self/offset aliases, mutable allocation limits and forwarded float
  words including signaling-NaN bits without arithmetic. One native negative
  fails. Scale arithmetic is finite and strict aliasing is disabled as in the
  existing decomp harness; no hardware FCSR equivalence is inferred.
- 64 caller cases / 128 paired runs execute actual complete byte-exact 89-word
  descriptor caller and 70-word resource-transition helper around original/raw
  and original/fitted constructors. Eight linked descriptors exercise 28 real
  type-zero calls per pair form. Deep allocators/initializers and the alternative
  constructor are bounded callbacks, not completed resource/gameplay behavior.
- 96 private-layout cases / 192 runs check an independent original save/home/
  mode/restore contract, absolute 0x38 frame, live home reads and untouched
  capacity. GP/FPR lifetimes are preserved.
- 28 full-layout cases / 56 runs plus 2,214 fired full-access fault pairs /
  4,428 failed runs compare complete original/fitted memory, events, calls,
  GP and FPR state at both phases. Twelve parent/output private-alias cases
  qualify. These checks do not assert raw C's different-frame equivalence.
- Four cases / eight runs mutate the original SP+0x2C mode home during a
  callback; the last helper receives the changed full word, not a cached bool.
- Actual production padder rejects all 182 individually mutated compiler words
  and all 22 individually changed relocations, including identity rows.
- Actual copied-owner compile/preprocessing/padding preserves all 30 neighbors'
  bytes, extents and relocations. Source/compiler pools are unchanged because
  the same owner object is padded with old/new manifests. Adjacent helper
  placeholders remain unchanged; copied owner and isolated target diagnostics
  are zero. Historical broader unchanged-neighbor suites are reused, not
  described as fresh executions.
- Consumer make tools-check and mounted standalone python3
  check_project_tools.py both pass. Broad rebuild succeeds; existing duplicate
  generated_12D630 and SDK/generated warnings remain. Not a warning-free build.

Private qualification is normalized-versus-retail guest behavior, not portable
C equivalence for arbitrary aliases into its different raw compiler frame.
Actual allocation/resource lifetime, remaining helper bodies, FCSR hardware,
full renderer and live gameplay acceptance remain separate open gates.

## Linked Audit

Only the target slot changes: 237 ELF bytes; all other ELF bytes and complete
metadata are identical. ST_SIZE remains 728. ELF 3,261,160 bytes, SHA-256
d84699b9a24ebc64cf6c380ef0fba1ed97bb091cb0cc7078fefd6c5a0c93424f.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Unchanged owner 9,769 bytes, SHA-256
5cf9c0bc7ddb18b7d5e09538b53761e56d8df54c820f83642ebb1321a46c97f9.

Guard manifest appends exactly 182 rows / 28,260 bytes, with the entire old
prefix and 298 historic CRLF lines retained. New 1,940,850-byte SHA-256
5e50f8952c0e5d4ba39b7e9054b7ac5727517d021ba8e92d3b10c8a2f07b2f19.
Native Git's existing CRLF-to-LF checkout warning remains; the scoped diff
contains 182 additions and zero deletions, not an EOL rewrite.
Conversion CSV stays 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Rodata, symbols and ignored undefined assignments remain byte-identical.

Fresh matching: Game 2,780/4,821 (57.66%), total 3,453/5,494 (62.85%),
zero drift / 2,041 different. Add one matching credit, no converted credit.
Root README aggregate rows updated only. Converted total remains 5,494/6,043
(90.92%); already-converted Init 492/492 and Debugger 181/181 stay exact.

```sh
python3 -m unittest tools.tests.test_game_child_actor_constructor_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Older standalone tools HEAD ddbdd16 is untouched: 265 prior dirty entries plus
two absent-only byte-identical new mirrors = 267. Protected helper hashes and
older submit copies remain untouched; no older commit/reset/overwrite.
Native Graphify update refuses unsafe shrink 39,642 -> 17,860 nodes, exit 1;
retains 19,398 nodes from 2,972 existing excluded files. Preserve skill
0.9.20/package 0.9.26 and devcontainer.json zero-node warnings; no force,
purge or install. Require fresh consumer post-commit rebuild completion and
zero actual workers before reporting clean. No host/OGL source, Release,
saves, editor state or private inputs changed. Wider Game goal remains open.

## Next

Bank this match before another conversion. Recover complete 68-word
func_150839B8 in generated_AEB40.c, VA 0x150839B8..0x15083AC8,
ROM 0xB0E68..0xB0F78, original frame 0x18. Its current body still returns
zero. Inspect actual caller types, the identity-0xFF gate, optional configuration
and world-0x1D branch, ordered resource-field copies, repeated byte reloads and
optional func_15036C70 callback. Preserve this constructor's complete compiler
fingerprint; prove any necessary declaration changes before altering its guards.
The adjacent 51-word func_150838EC, timeline matching and actual deeper
resource/allocator/hardware/gameplay behavior remain separate open work.
