# Game Owner Point Initializer Frame And Private Home Fit

Date: 2026-10-09

## Result And Boundary

Continue complete func_151B3A7C from
[Note 1185](1185-game-owner-point-initializer-recovery-20261009.md).
VA 0x151B3A7C..0x151B3CF0, ROM 0x1E0F2C..0x1E11A0.

The [fitting driver](../../tools/experiments/game_owner_points_initializer_fitting.py)
recovers the original 157-word /628-byte slot and 0x60 /96-byte frame directly
from complete semantic C. The live position is at SP+0x44 and saved F20/F21 at
SP+0x08, matching the original. Raw differences fall 143 to 137.

Still uninstalled/nonmatching. No guards, matching credit or conversion credit.
The production placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) is unchanged.
Do not confuse matching frame/private homes with all linked words agreeing.

Baseline parent ea9538ad, mounted tools b3a58e3e547051d49c4b909330d2e68b2fd8de7a;
both clean initially. Previous turn made committed full-body recovery progress.
Single Codex writer, zero Claude calls; no OGL/Release/save/editor work or push.
The wider Game matching goal remains active.

## Real Layout And Local Lifetimes

Use an explicit actor prefix with flags at0x10, start/end positions at0x14/0x20,
metadata through0x48 and ten24-byte point records beginning at0x48.
The actual native32 layout check confirms12-byte positions,24-byte records and
a0x138-byte prefix; original bytes beyond that view are not read or written.

Owner fields remove repeated byte casts without changing public addresses.
The owner pointer is a live local used by real coordinate, flag and record access,
not unused padding. Put the actual delta, position and step vectors in declaration
order delta/position/step. This places the live position at originalSP+0x44 while
retaining frame0x60. A real local point-record pointer reduces GPR address
differences further without changing frame, private home or the complete contract.

Keep all ten records, captured endpoint deltas, independent scale words loaded
after the first record, repeated binary32 coordinate additions, zero second
vectors and final flag-bit-2 clear/success return. Preserve all ten private
position advances, not just the nine that produce subsequent public records.
The second vector's velocity label remains a candidate name, not an established
original field meaning.

No frame-word patch, register-binding assembly, unused local padding, literal
retail lookup or compiler/build profile change is introduced.

## Fitting Measurements

Twenty-nine full source forms pass all eight ordinary contract fixtures each:
232 candidate and232 original executions, zero failures/diagnostics/pool bytes.
Ordinary fixture agreement does not establish every alias for every control.
Only the selected body gets the entire qualification suite.

| Complete source form | Words | Frame bytes | Differences |
| --- | ---: | ---: | ---: |
| Earlier untyped recovery | 157 | 88 | 143 |
| Typed owner, prior vector order | 157 | 96 | 145 |
| Typed owner, delta/position/step order | 157 | 96 | 141 |
| Selected live record pointer | 157 | 96 | 137 |
| Register-counter keyword control | 157 | 96 | 137 |
| Counter declaration first | 157 | 96 | 141 |
| Hybrid byte-access position | 158 | 96 | 120 |
| Hybrid byte-access second vector | 158 | 96 | 118 |
| Count-minus-index positive test | 155 | 96 | 149 |

Do not choose the hybrids' lower difference count despite their one-word overflow.
Narrow integer counters, nonzero difference termination, peeled-first loops and
separate-zero controls likewise fail the original full slot/workspace shape.
The selected record-pointer form retains the full157 words and correct homes.

Fresh selected-body profile screen:
O2/g3 157/frame96/137; O2 157/frame96/121;
O1/g3 and O1 302/frame56/302. None matches; production stays O2/g3.

Additional diagnostic controls were run on the earlier141-difference owner form
and two simple/peeled vector forms, not falsely reported as the final137-word-diff
selected body. O3/g3 is rejected by the strict existing compiler helper because
uld warns that -Xfullwarn is unsupported; O2/g2 warns that optimization is disabled.
Do not suppress those diagnostics or claim those profiles were qualified.
Unroll0/2/4 controls retain157/frame96/141 on the earlier grouped form.
They do not recover the simple/peeled loop's original full shape.

## Full Qualification

[Eleven-test fitting suite](../../tools/tests/test_game_owner_points_initializer_fitting.py)
passes in122.336s, zero skips, on the final137-difference selected body.
The earlier141-difference body passed eleven tests in72.527s; do not reuse that
timing as the final selected-body receipt.

- Full guest:2,048 cases /4,096 original/candidate executions, all256 flag bytes,
  four coordinate bit-pattern sets, two stack phases and all157 words reached.
  Saved GPR/FP registers are restored.
- Independent scales/first-record constant aliases:44 cases /88 executions.
  Six effective compiled negatives reject changed flags/return/count/increment,
  collapsed scale and nonzero second vector.
- Actual complete native32 C:8,192 finite binary32 cases, every actor/canary byte,
  all flags and independent scales. Public outputs and success return agree.
- Actual complete original81-word registered update:32 cases /64 executions;
  preserves real D_8008FAF8[0] pointer and one-argument callback ABI.
- Four independent symbol sets/eight original/candidate links:32 cases /64
  executions, all six original relocation uses retained; semantics, not a
  byte-exact claim for the nonmatching candidate.
- Four missing-byte faults/eight executions compare public prefixes; two missing
  unused bytes/four executions still return normally. No portable-C or hardware
  exception/read-order equivalence claim.
- Actual owner:16 neighbors/pools/relative relocations preserved, zero existing/
  new warnings. Raw target equals isolated body. Actual padder emits the raw
  628-byte slot unchanged, without padding or guards, then assembles successfully.
- Exact private frame qualification:16 cases /32 executions over two stack phases
  and independent scales. Entire final memory, including private bytes, agrees.
  Both routines write only SP+0x08..0x10 saved-FP bytes and SP+0x44..0x50 position
  bytes within the private frame. No extra private writes.
- Actual native32 static sizes/offsets confirm the actor-prefix and point layout.
- Production source/ELF/guards/progress hashes and189,088 protected Game bytes/
  720 owners remain unchanged and exact.

This is bounded instruction/native qualification, not an unbounded floating-point
or FCSR/hardware proof. Private final-byte agreement is stronger than the earlier
public-only comparison, but instruction/public access ordering is still different.
Full caller cleanup/walker, SDK/hardware/emulator/live rendering/gameplay remains
outside this checkpoint.

During suite composition, patching the older RECOVERED body initially caused
the source-form generator to apply the owner conversion twice. Freeze the
original recovery seed before patching the qualified test body; rerun all tests.
No production bug or relaxed acceptance gate is inferred from that fixture error.
The fitting suite records its own uninstalled baseline and also verifies equality
with the older recovery baseline when present, without overwriting older receipts.

## Preservation And Checkpoint

Project make tools-check passes. No linked production rebuild is rerun because
source/profile/guards/data are unchanged; the prior successful Note1184 build is
reused explicitly. Fresh matching report remains total3,416/5,489 and
Game2,743/4,816 exact, zero drift/2,073 different. README aggregate rows unchanged.

Unchanged SHA-256:
source2cd9fbac1a68ad325b9e644abdedb867f42f777fdb4cff4cb058856cb82ad50c;
ELF4867fdd672d1e50e18345bcdc0f8a2d50c8774e443863e7d13cbffa0554a14b9;
guards431d3bb33607126440e2a13829f599c27bdf25851767e25d05097911a49c7913;
progress5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.
Protected data0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Mounted tools977010c57db940f57678fec65a1d541fb8fe01b7 commits the fitting driver
and suite before consumer documentation/tools pin. No push performed.
Older standalone HEADddbdd16b53ce60b054fb6e11bf0649a41f48375a, both tracked
dirty-file hashes and all124 previous dirty entries are verified unchanged.
Mirror only two absent authored files, yielding126; no older commit/reset/push.

Fresh documentation validation checks172 documents and4,551 relative links:
zero broken links. All91 authored tooling files parse and match their exact
mounted/older mirrors, including the two new fitting files.

Ignored receipts:conker/build/game-owner-points-initializer-fitting/ and
conker/build/game-owner-points-initializer-fitting-test/.
Explicit graphify update . exits1, refusing39,074-to-17,293 node shrink and
preserving the graph. Retain version/zero-node/scan-corpus warnings; no force,
purge or install. Consumer incremental post-commit hook has a separate receipt.

## Continue The Remaining Match

Original setup ends at offset0x11C; selected loop begins at0x118.
Both restore tails begin at0x258 and all seven tail words agree.
Original loop has79 words; selected loop has80. The selected control uses
SLT/index-less-than-count plus BNE-on-AT, whereas retail branches directly on
counter/end equality. A second-vector zero-chain store also reloads zero from
public memory into F0; retail retains the zero FP value without that load.

Recover this real integer induction/control and zero-store shape first, retaining
full157 words/frame0x60/SP+0x44 home and the complete late-scale/alias contract.
Then fit independent initial FP/setup schedule and closed register allocation.
Do not patch only the frame or synthesize retail words to force agreement.
Any residual normalization needs closed lifetime/memory/control proof, effective
negatives and complete independent linked qualification before guards.
Installation still requires every word plus whole owner/ELF/data/guard history.
