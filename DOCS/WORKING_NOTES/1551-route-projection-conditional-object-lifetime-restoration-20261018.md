# Route Projection Conditional Object Lifetime

Date: 2026-10-18. Consumer predecessor **5fc2c839**; tools predecessor
**bc4a6e8**, new tools checkpoint **fabe5a1** banked first. Continue
**func_150891E8**, VA **0x150891E8..0x150896EC**, ROM **0xB6698..0xB6B9C**,
owner `generated_B3020`, retail **321 words /frame0x78**. This is progress
on the same parent, **not a production conversion or byte match**.

## Recovered Lifetime

Note1550's307-word model unconditionally saved its entry object at entry-SP-4,
even on a null-object return. Explicit pointer copies, block scope and early
return alone do not prevent that compiler spill. Separating common-phase IDs
also fails to recover the desired saved roles. Moving declarations changes
the object home predictably but does not itself recover conditional storage.

`tools/experiments/game_route_projection_lifetime_fit.py` now recovers the
actual lifetime with ordinary C. A signed32-bit work/index value first loads
actor+318. After the nonzero check and preference choice, capture its pointer
bits as `(u8 *)(u32)i`; the index then serves the anchor scan and its captured
mode before the final count reload. These uses have disjoint required
lifetimes. No volatile declaration, dummy effect, physical-register binding,
frame patch or inline assembly is introduced.

Move the object declaration immediately before projectedZ. The compiler now
emits the object store at relative word23, **after** the null/preference gates,
to **SP+0x3C**, and reloads that same home after command7. The null return has
retail's conditional RA reload and touches only the original seven save homes.
Keep S5/S2/RA/S4/S3/S1/S0 at28/1C/2C/24/20/18/14. The nonnull helper calls
still use fresh actor+318; the final four30f stores retain the entry object.

The selected complete body emits **302 words /frame120 /301 differences**,
including19 missing words. Raw SHA-256:
`6c76a9f1bf9e0e0cdcf4818da5e0fc75b0278b5acad183e5d530d3bb29630970`.
All302 words and18 relocation sites are strictly checked against15 unchanged
inputs. This partial fit is not installable. The previous307-word fixture
keeps its historical fingerprints; the test compiles it afresh as a negative
control rather than depending on a pre-existing ignored object.

## Qualification

```sh
python3 -m unittest tools.tests.test_game_route_projection_lifetime_fit -v
```

The final six-test run passes in **20.926s**. Ignored compiler candidates and
JSON receipts live in `conker/build/game-route-projection-lifetime-fit/`.

- **575 paired raw/retail public cases** retain Note1550's states, finite
  coordinates, signed modes/counts, preference bits, nine aliases, queue wrap,
  absent/later roots and index258 anchor. Both actual helpers execute:91-word
  selector1508907C and41-word original enqueue1512D560, not provider hooks.
  Every nonnull case also checks captured object at adjusted-SP+3C. Preserve
  saved F20..F31 and the runner's ordinary integer ABI checks.
- **24 additional paired guest cases** exercise object pointers7FFF0000,
  80060000 andFFFF0000 over four states and both stack phases. The signed-word
  carrier and unsigned-pointer cast preserve all32 bits. This is a guest ABI
  result, not native64 pointer portability or mapped hardware execution.
- **16 null-object cases** compare complete memory, including private saves,
  calls, public traces and FPRs. **240 actually fired access-fault prefixes**
  compare those states plus saved GPRs, SP and RA. All15 accesses occur in the
  same order. Dead GPRs, instruction PCs/delays and full nonnull fault-state
  equality are explicitly outside this result.
- Two real old-model null executions still expose its extra zero at entry-SP-4.
  A separately compiled declaration-order control keeps public results equal
  but puts the object at SP+38 rather than3C; the storage check rejects it.
  This is a private-home control, not a claimed public semantic failure.
- **Nine compiled complete-C semantic controls** each yield wrong public
  memory: preference bit, root type, unsigned coordinates, premature clamp,
  cached payload inputs, fresh final object, fresh selected table, omitted
  command5 and wrong command7. No crash/timeout is used as a witness.
- Reject302 raw-word corruptions,18 missing bindings and30 live/snapshot input
  mutations. Normal-profile comparison preserves all72 raw owner neighbors,
  their relative bindings and normalized pools. Production's owner still uses
  no-unroll; this does not authorize a whole-owner normal-profile replacement.

Base ordered traces remain **240/480 raw versus480/480 retail/reference**.
Across575 cases, visit282/302 raw root words and272/321 retail root words;
neither full CFG nor arbitrary float/FCSR behavior is qualified. Shared
LB/sqrt/guest runners are unchanged; their local extension controls are the
unchanged Note1550 receipts, not fresh tests here. Native32, independent parent
rebases, complete caller execution and full private/fault proof remain undone.

## Remaining Fit

Twenty-four bounded source forms measure phase-local IDs, entry-copy shapes,
declaration placement, word/byte candidate carriers, address capture, explicit
first-slot peeling and meaningful distance/node reuse. Only the selected
302-word form receives the complete tests above. No other shape screen is
promoted on its length or public-equivalence assumption. Individual compiler
objects/diagnostic/measurement files are retained; do not repeat this matrix.
An independent receipt audit confirms all24 reconstructed complete sources,
object hashes and recorded lengths against the unchanged frozen inputs.

The original five-slot scan is fully unrolled after its first slot; the
selected model still has a two-slot residual loop. The wider word-candidate
forms fully unroll but remain338/339 words with an incorrect private layout.
Splitting phase IDs gives293/frame128; distance/node reuse does not close the
extent or all saved roles. None is installation evidence.

The selected preference home is **SP+5F versus retail44**, minimum-distance
home **40 versus50**, and common current-distance home **44 versus5C**.
The current-node pointer must also recover retail's call-live48 home rather
than merely preserving the same public pointer value in another register.
The first10 opening words and the seven save homes agree, but the entry object
is held in A2 rather than retail V0. Keep conditional memory improvement
separate from a full physical-register or instruction match.

Next fit the five-slot unrolling and remaining real declaration/expression
lifetimes under the same strict302-word checkpoint. Then qualify any proposed
closed normalization, independent links and whole-ELF prediction/install audit.
Do not insert19 words, rewrite the frame or weaken guards to claim matching.
Enqueue1512D560's production C stub, vector15088F30's two-save fit, other
parent150896EC and wider Game queues remain open.

## Preserved Baseline

No production C, Makefile/profile, guard, ELF, progress or root README change.
Fresh hashes equal Note1550's baseline: ELF4b8ab8ed, ownerf7db991f,
guardsc40fe51b and Makefile840897f1 (full hashes remain in that note).
No build/recount is claimed. Note1549's unchanged official totals remain
**Game2,985/4,828 (61.83%)**, **total3,658/5,501 (66.50%)**, Init492/492,
Debugger181/181, **1,843 different /zero drift**. This checkpoint adds zero
matching credit; the overall Game goal stays active.

Shared padder/PC16 checks pass eleven per tools copy, both smoke checks and
consumer tools-check pass. Both new files pass ASCII/AST checks and are
byte-identical across copies. Standalone mirror HEADddbdd16 and all1,228
prior dirty hashes are preserved, adding only two absent task paths for1,230.
Zero Claude calls; this is a bounded compiler/source lifetime investigation.
No mirror commit/reset, push, host-port or frozen Release action.

Scoped Graphify refresh: **42,581 nodes /82,650 links /3,992 communities**.
Preserve all42,570 unaffected old IDs; three duplicate UPDATE_LOG headings
relocate by eleven lines with their labels/files retained. This note adds six
nodes. All19,398 excluded-but-existing nodes from2,972 files remain. Tools
stay outside the configured corpus; no fresh graph Python AST coverage is
claimed. Original graph/ID audit remain ignored; no full-scan purge, committed
graph output or history rewrite.
