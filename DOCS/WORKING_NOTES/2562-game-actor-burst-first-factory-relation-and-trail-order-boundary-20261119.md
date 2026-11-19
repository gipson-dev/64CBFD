# Actor burst first-factory relation and trail-order boundary

Date: 2026-11-19. Continue `func_150BBB5C` from Note2561. The private
candidate now agrees with retail's ordered instruction effects through the
first descriptor-factory submission. Full traces also locate the first
remaining ordered FP difference in the trail loop, after the first particle
loop. **Uninstalled, zero new matching credit.**

## Recovered first-factory ordering

The previous 590-word candidate passes the extended sprite boundary, but
fails the first descriptor boundary. Its first difference is FP event52:
the Y-coordinate addition has reversed operands. Swapping the source
addition fixes that event, then exposes event53, where an independent
velocity addition runs before the Y-coordinate's final addition of five.

The selected source swaps the Y addition and gives the existing
`descriptor.position[1]` store a volatile float view. Both changes are
necessary: removing either is an effective negative control. No algorithmic
operation, global qualifier, compiler profile or production guard is added.
These are measured reconstruction constraints, not proof of the original
C spelling.

The compiled full owner remains **590 words / frame624 / 58 relocation
sites**, versus587 retail words. There are569 unequal overlapping words,
three extra words and an extra saved S4. All eight owner neighbors and
normalized pools remain unchanged under the existing O2/g3 profile.
Raw SHA-256:
`808e01bf55d22a85740eb5fbd292740e764060d77e7fcc8a2769d945c7337f68`.

Across five symbolic paths, the positive relation covers312 raw and309
retail instruction positions through the first factory or earlier return.
Ordered FP operands/status transitions, helper arguments, quiet-epoch
public-read multisets, the168-byte sprite and the complete124-byte
descriptor agree. Untouched packet bytes retain symbolic initial values.
Early-return saved-register, stack and return-address restoration is checked.

Opaque helpers can change public memory and FCSR, clobber caller-saved
registers, and mutate every previously passed private packet/vector range
at a later call. The model excludes inspection of unpassed locals, caller
code and implementation return PCs. Private stack and immutable literals
are disjoint from public memory. It does not prove arbitrary faults,
interrupt-visible state, complete private-frame equality or gameplay.

## Full traces identify the next boundary

The two initial random results are used for counts only after masking with
three. Enumerating all16 low-bit pairs therefore covers particle counts6..9
and trail counts10..13 while later helper results remain symbolic. Five
control-flow paths per pair give80 symbolic paths. Each pair collectively
visits all590 raw and587 retail instruction positions and restores the
saved ABI on return. Active return values remain ignored as the real caller
does; the early type-rejection result is checked.

Every pair reports a remaining difference at the same trail instructions:

| Side | Relative byte offset | Instruction word | Observed operation |
| --- | --- | --- | --- |
| Raw C | `0x558` | `0x461AA102` | Multiply cached radial cosine and trail speed |
| Retail | `0x54C` | `0x46062280` | Add the sampled height contribution and actor Y |

The retail instruction is at VA`150BC0A8`. The first unequal event is319,
367,415 or463 according to the first particle count. All prior ordered
events and particle-factory observations agree in these symbolic traces.
This is an explicit **failed whole-function relation**, not a full match
inferred from complete instruction coverage. Reports retain both traces,
term definitions and instruction locations for the next source experiment.

The ordinary named-Y/Z and cached-sample forms do not fix the trail order.
Intermediate array stores and volatile Y-only views either retain the
first difference or increase the body to592/594/598 words. These remain
private rejected experiments. The first-factory candidate stays590 words.

The initial first-factory traversal explored impossible nonpositive count
paths and hit its bound. The corrected verifier derives signed intervals
only for actual masks and non-overflowing affine expressions. Overflowing
or sign-bit masks stay unknown. NEG.S remains an ordered opaque FP/status
event; it is not assumed to be a status-free bit flip. The first temporary
store-view generator also rejected a duplicate field occurrence before
compilation; the corrected generator scopes its first-loop replacement.

## Validation and checkpoint

The focused five-test suite checks the full owner and first-factory
relation,274 direct guest cases/all587 retail words and two early byte-read
fault checks,384 native SDK32 cases each at O0/O2/O3 with UBSan/strict
aliasing and12 semantic negatives, and3,072 cases through the original
caller's relevant dispatch paths with six caller negatives. Seven effective
first-factory controls include both new ordering constraints. Verifier
limitations cannot count as semantic rejection. The full-trace diagnostic
must retain its trail mismatch across all16 count pairs.

Native fixture:2,827,780 bytes, SHA-256
`423cca435e1405de3fa1a4660e5c34507e75a9c702726394fbe1a72a2eb7e43e`.
Caller scope remains42/252 original caller positions and584/587 target
positions; the direct guest suite covers the remaining target rejection.
No alternate-helper recovery or physical coexistence of the oversized raw
body and the following slot is claimed.

All1,871 committed baseline inputs are frozen and checked. Production
source/object/ELF, original ASM, guards, profiles, protected data and root
README aggregate tables remain unchanged. The real sibling tools HEAD,
dirty status and343 dependency hashes are preserved; matching dependency
copies and explicit primary fallbacks form the isolated second test setup.
Both final five-test suites pass with zero errors, failures or skips and339
imported tool hashes each. Runner times: 134.586s primary and142.062s
sibling. The889-file overlay uses339 matching sibling files,545 primary
fallbacks, four task files and one bootstrap. `make tools-check` passes.

The first commit check caught an extra EOF blank line in the new proof
file. Only trailing whitespace changed, its parsed AST stayed identical,
and both suites were freshly rerun at the new fingerprints. Earlier
receipts and the pre-fix file remain archived separately.

Final paired receipts and graph-retention results are retained in
`conker/build/game-next-150bbb5c-relation-private/`.

Total stays **4,558 / 5,514 (82.66%)**, Game **3,885 / 4,841 (80.25%)**,
zero drift; **129** additional matches reach85%. The goal remains active.
There is no production Make/recount, installation, guard/normalizer credit,
host/Release/save change or gameplay acceptance in this checkpoint.

Resume `tools/experiments/game_actor_burst_150bbb5c_factory_manifest.json`.
Recover the trail FP order, then finish S4/address lifetime and actual
private-home/layout qualification. Pass both padders, independent strict
whole-image prediction, actual Make, installed checks and a fresh recount
before adding matching credit. Keep the rejected constant-allocation
profile from Note2560 rejected. Commit tools before the consumer; no push
or automatic pause.
