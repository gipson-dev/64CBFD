# Strip update amplitude lifetime and prefix/snapshot relation - 2026-11-17

`func_151AD174` now has a stronger private draft, **v43: 490 words / frame
0x308**, against retail's 494 words. Its early amplitude occupies retail's
**F20**, and both original gravity operations remain. The bounded symbolic
relation now covers entry through the snapshot-copy exit at retail word 175
(VA **151AD430**). This is an instruction/state relation, **not 175 words of
byte-exact matching**, and not a completed routine. The production stub,
guards and compiler profile are unchanged; **no matching credit** is awarded.

Totals remain **4,532 / 5,514 (82.19%)**, Game **3,859 / 4,841 (79.71%)**,
Init 492/492 and Debugger 181/181, zero drift. **155 further matches** are
needed for the active 85% goal. The root README stays unchanged. Previous
recovery and capture evidence is [Note 2514](2514-game-strip-update-private-recovery-native-fixture-repair-and-caller-qualification-20261117.md).

## Target and source-lifetime correction

Owner `conker/src/game/generated_1D92F0.c`, VA 151AD174..151AD92C,
ROM 1DA624..1DADDC, **494 words / 1,976 bytes**. The protected class table
registers the one-pointer void callback at descriptor+4 for classes2F/4E.
The original secondary-list walker remains the caller qualification target.
All 32 owner neighbors and constant pools stay unchanged.

Earlier v20 reused one C amplitude for the four owner trig calls and the
loop's vertical result. It preserved sampled early stack bytes but used
different saved floating registers. The scoped-gravity v38 retained9*9 and
NEG9, but allocated the early amplitude to caller-saved F14 and spilled it
at SP+F8. Native/public correctness did not establish those internal roles.

The new source gives the loop's vertical result a separate live range and
reuses the now-dead early magnitude for constant9. The later planar value
can be overwritten by the vertical result after its square is retained for
the predicate. These are actual semantic temporaries, not padding variables,
volatile declarations or fake stores. v43 also retains unconditional
`81-square` subtraction before the comparison branch; v42's optimizer had
made that subtraction conditional on the successful square comparison.

For the sampled first six provider boundaries, v43 now agrees in **all saved
GPRs and FPRs**, private bytes and the ordered FP sequence. In comparison,
v20 differed in F20/F22/F26 and v38 differed in F20 plus the F8 spill. These
concrete observations motivated the separate symbolic checks below.

## Strict symbolic prefix relation

The paired checker follows every instruction in the **142-word opening**,
ending at VA 151AD3AC. It explores **18 branch paths**, with30 visited call
boundaries in the shared-prefix exploration. Initial register/FP state and
synchronized load/provider results are symbolic. Loads are deliberately
unconstrained after identical ordered accesses, giving an overapproximation
of alias/mutation behavior rather than relying on finite coordinate fixtures.

Memory operation widths, addresses and store values must agree in order.
FP operations require the same precision, operation, ordered operands and
abstract FP-control input; floating commutativity is not assumed. Branch
predicates, targets and likely-delay execution are compared. Every trig
call requires the same argument and all FP registers, ABI-preserved GPRs,
return/frame registers, HI/LO, FP condition and abstract control state to
agree. Calls obey the declared opaque-provider contract and may clobber
caller temporaries. The snapshot join also checks the captured count.

The checker permits compiler renaming of dead caller GPR temporaries. It
does not claim literal equality of every temporary register at every PC or
a complete architectural fault-state proof. It makes no statement about
the unproved reverse-loop/audio suffix. Wrong private stack store, wrong
FP operand and wrong call argument each reject as effective negatives.

## Inductive snapshot-copy relation

Words 142..174 contain the setup, empty-count exit and snapshot-copy loop.
The checker starts a **generic outer row**, with only loop-live values
related and dead caller temporaries deliberately different. Both versions
execute exactly three components, checked against the actual bound12 and
four-byte increments. All18 ordered row memory effects agree, every FP
register and the ABI-preserved/special state agree at exit, and the row
index, count, position/velocity cursors reestablish the loop relation.

This checks an inductive row transition instead of unrolling only the
twenty concrete fixture rows. The setup links to the opening's proved live
state, and the ordinary empty-branch delay executes on both outcomes.
Wrong component load, wrong row stride and wrong component bound reject.
The composition reaches VA 151AD430; the gravity preheader and reverse-loop
state relation remain open.

## Qualified compiler allocation evidence

Normal complete-owner mode5 captures use the fingerprint-locked prepared
cc/uopt, existing GDB observer and original O2/g3 profile, with the diagnostic
mode enabled. Driver completion, fired buffer/suppressed-printer markers,
input/helper fingerprints and all 33 body/binding/pool identities are checked.
No debug real-number costs or timings are interpreted.

The listing parser must first delimit this routine's unique local-optimization
and reemission markers. Expression identities recur in other functions: an
initial identity-only private selector included four foreign rows. The
maintained parser is function-scoped. It also distinguishes M/P procedure870
records from valid hard-register R/procedure0 records at offsets 2 and32.
An initial maintained assertion rejected those R records; that failed output
and snapshot are retained, and both tools configurations were rerun freshly
after the parser correction.

For amplitude **M-528 / expression52**, v20's final color was33, v38's27,
and v43's **30 (emitted F20)**. v43's final forbidden set is only24, compared
with v38's much larger set. These are final allocation facts, not a captured
causal selection/cost history. Do not infer one pressure or birth-order cause
from the final color table alone.

## Fresh qualification in both tools configurations

All **five tests pass freshly**, primary **110.852s** and sibling
overlay **112.212s**, with identical four-file task hashes and actual
import origins retained. The source/header/compiler/padder primitives are
reused; the target executions and checks below are fresh.

- Full owner compile:490 words/frame 0x308, exact relocations, all32 neighbors
  and pools unchanged; retail input independently pinned.
- **544 cases per retail/raw stream** compare every declared public byte,
  complete provider calls and saved registers. Coverage489/494retail and
  485/490raw; this remains incomplete path coverage.
- The symbolic prefix and inductive snapshot checks pass all six effective
  instruction mutations described above.
- Native32 **O0/O2/O3** pass544 cases each; four compiled wrong-score/decay/
  signed-countdown/smoothing variants each reject. All public arena bytes
  and calls are compared, with the qualified complete-pointer replay fix.
- The full74-word original registered-list caller passes **64 cases per
  stream**, both classes, rows0/1 and byte depths0/3, with73/74words visited.
  A changed callback pointer rejects; complete public RAM/calls agree.
- A fresh complete-owner allocation capture in each configuration reproduces
  all 33 functions and verifies the scoped amplitude color/constraints.

Fixtures use fresh disjoint mapped objects, count0..20, in-range indices,
finite coordinate/provider values and SSE single/double RNE on native32.
Native/public checks do not establish N64 FCSR or private-frame parity for
the suffix. The symbolic opening checks have their separate scope above.

## Bounded advisory review and rejected hypotheses

One Claude Code request used the complete packet only, with tools/MCP,
customizations, hooks and session persistence disabled. Packet SHA256:
`352770fb486cd29aad9d40ecfd87c12abc02e5af101361afbbcdf3afbef76120`. Codex independently checked its claims.
The complete retail assembly has no literal SP+80 reference, and AC/B0
stores/loads occur around the **first force-input norm**, before151AD584.
The review's description of those as second-phase deltas is incorrect, and
the measured v38 optimized M slots are not known original retail CFE slots.

Its two suggestions were tested separately against v43. A narrow downward
local (v46) emits491 words/frame 0x310; a named squared-gravity invariant (v47)
emits490/frame 0x310. Both fail the required frame and are rejected. The proposed
single pressure/birth-order explanation remains unproved. No second review
was requested. Packet, response, receipts and reconciliation remain private.

## Remaining matching work and preservation

The sampled full reverse path still differs at **SP+7C,80,84,AC,B0**, with
1,671 FP operations in each stream but different order/operands. Retail's
9*9 precedes NEG9 and stores81 at84, minus9 at7C. v43 reverses their order
and stores81 at7C, minus9 at80. The first displacement's Y/Z values remain
promoted instead of the original B0/AC spills. These differences are not
discarded or normalized into a passing claim. Continue at the gravity
preheader, establish the complete reverse-loop relation, then qualify
normalization, both padders/rebases, full state, actual Make and strict
whole-image adoption before any installation or matching credit.

The final snapshot contains **1,513 verified inputs**:1,509 links to immutable
prior snapshots and four copies, with zero live-worktree hardlinks. Fresh
audit leaves all **698 production objects**, source/headers/profiles/guards
and root README unchanged; **189,088 protected bytes /720 owners** stay exact.
Fresh actual ELF recount and shared tools checks pass. Production ELF:
`7c1c2f7ef67741c05a3d512530e777e9e4e4de6f29df28ebc8a22e9b95e4af90`.

The sibling's 2,434 dirty paths/339 scoped dependencies are unchanged. The
host sibling exposes diagnostics only, with no source checkout; no host,
Release or save work is included. Graph refresh retains previous IDs using
scoped AST evidence after the native CLI refuses corpus shrink. Bank tools
before consumer notes/pin, with no push or automatic pause. The 85% goal stays
active.

New maintained files use prefix `game_strip_update_151ad174_lifetime`.
Run with a fresh owned `CBFD_STRIP_UPDATE_LIFETIME_WORK` path:
`python3 -m unittest tools.tests.test_game_strip_update_151ad174_lifetime -v`.
Receipts: `conker/build/game-next-151ad174-private/lifetime-final/`.
Raw v43 SHA256: `4ac5cf912862042698d8a7d51e11874547bf3a6dc3cf84594e906d172e42d800`.
