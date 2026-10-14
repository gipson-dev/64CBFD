# View FOV Transfer Reconstruction

## Scope And Baseline

Continue the full additional-source/Game matching goal from consumer44774314,
tools820566f and ELF b87dd5bc. Both active repositories are clean before task
edits. Preserve the original archive, independently dirty older tools mirror,
all private receipts and frozen host Release. No push or host operation.

func_1501B0A0: VA1501B0A0, ROM48550,99 code words/396-byte slot, frame0x50,
RA-only save. Current owner game_476D0.c has a false parameterless s32/zero
placeholder; the archive retains GLOBAL_ASM and provides no C body. Recover
the natural void/two-index command interface, not another zero-return stand-in.
No direct named incoming calls were found in the scoped source/assembly search;
this does not establish absence of indirect callers or full caller acceptance.

Four real trig calls derive the tangents of two base half-FOVs. Reference
signed32 viewport dimensions divided by twice those tangents provide focal
extents. Two func_150484A0 calls turn selected view extents into corrections,
with live/reloaded view bases and base FOVs around callbacks. Final
func_1510B128 receives(index,offsetX,offsetY,1.0f,0.0f) through five o32 words.
The private layout exposes offsets0xC/10/6C/70 and preserves size0x180;
shared struct259 still hides these fields and is not broadly rewritten.
The extent/base-FOV roles are inferred from these formulas and the retail
command's writes to effective FOV fields74/78; offsets and load order are facts.

func_150484A0 has an existing typed float/float source body in game_75950.c.
func_1510B128 remains a zero-return C placeholder. Preserve its current s32
return declaration while recovering the float argument protocol locally;
the parent ignores its opaque result. The command body/complete cross-file
interface remains unfinished, and no C-stub/gameplay acceptance is claimed.

## Steps

1. [x] Inspect complete retail body, archive status, layout, angle helper and five-word command protocol.
2. [x] Screen11 complete source/lifetime forms; retain the exact99-word/frame0x50 body with only13 opening schedule differences.
3. [x] Qualify thirteen expected-word/relocation guards as one closed prologue permutation, with no invented operations.
4. [x] Preserve10 owner neighbors/pools, both padders and independent original/rebased links.
5. [x] Check cached half-angles, live dimensions/scales/bases, helper ABI, aliases, faults, native32 behavior and effective controls.
6. [x] Run connected recovered trig cases; keep angle-helper/command models and gameplay acceptance explicit.
7. [x] Install only a qualified body, close the whole image and extend exact-hash history gates without recapturing old snapshots.
8. [x] Refresh aggregates/indexes/graph and bank tools before the consumer group.
9. [ ] Continue the actual command/helper/donor/binding/codec/Game queues and separate rectangle history reconciliation; no whole-goal completion.

## Initial Measurements

All11 candidate configurations compile without diagnostics. Selected/indexed
C emits99 words/frame0x50; exactly words1..13 differ. Every other emitted word,
all math operations, saved-register lifetime and seven calls already agree.
Splitting trig expressions emits97 words; early dimension caching emits102.
Explicit first coefficient temporaries emit99 words with32 differences.
Const-qualified declarations retain the13 differences; reusing the pending
half-Y local as the coefficient yields82. All alternatives stay private.

The proposed guards move the existing D_800968F4 HI/LO load pair from words
10/13 to1/2 and shift the independent argument/save/view setup around it.
Four relocation records move intact, including the view base HI/LO pair.
No arithmetic, branch, call, frame update, new word or omission is supplied.
Current tests must prove full instruction-plus-relocation multiset identity,
actual guard inputs and complete normalized retail identity before installation.

Immutable fixtures are in conker/build/game-view-fov-transfer. Existing
before files are never overwritten. The first capture is extended only with
the two newly identified dependency owners, after matching their already-read
hardcoded hashes and confirming the original image is still current. No old
source/image/header/guard/progress fixture is recaptured to accommodate a result.

## Qualification

All 65 selected target/affected-history tests pass in 115.601s. The transfer
suite has ten qualification/control gates plus two pure source/guard checks.
The raw complete owner emits 99 words with 13 differences, frame 0x50 and no
diagnostics; the other 86 words emit directly. The guards preserve the complete
instruction/relocation multiset and both full-owner padders yield all 99 retail
words. Ten neighbors retain bytes, extents, relative relocations and pools.
Independent original assembly and generated C links agree at normal and
0x9000-rebased code/helper/data symbols. No padding is inserted in this slot.

- 2,160 paired MIPS cases cover three selected indices, six reference indices,
  ten helper-result patterns, six callback mutation modes and two stack phases.
  Check all 99 instructions, all seven argument packets, cached half-angles,
  live coefficients/dimensions/base reloads, equal-index aliases, signed32
  dimension extrema and full modeled state.
- 528 actually fired root-memory prefixes preserve state and actual PC/delay
  identity. Helpers are atomic/bounded here, not native C fault semantics.
- 648 native32 cases per O2/O0 profile compare all seven calls, entire backing
  view storage, dimensions and globals. Four effective negatives reject a
  reloaded pending half-angle, early dimensions, unsigned width and wrong scale.
  Native arithmetic uses finite/nonzero trig returns; no NaN payload/FCSR,
  arbitrary index wrapping or portable fault-equivalence claim.
- 36 connected paired cases freshly compile and execute the exact recovered
  104-word sine and 88-word cosine slots. The angle helper and final command
  still use identified bounded models; their actual callee bodies and full
  gameplay/camera behavior are not accepted by these cases.

The first expected-relocation corruption control did not mutate a differently
formatted offset string. Replace that fixture manipulation with CSV parsing;
both expected-word and expected-relocation corruptions now reject actual
changed inputs. A check observed the ELF while the linker was live and failed;
wait for build completion before accepting whole-image results. No failed or
partial producer output is used as a qualification receipt.

## Installed Image And History

The production build completes with inherited warnings, including the duplicate
generated_12D630 recipe; this is not a warning-free full-build claim. The target
owner compiles without diagnostics. The closed-image gate independently expects
the old ELF with only the 396-byte target slot replaced from retail, public
size 12 -> 396 and one adjacent four-symbol/string permutation. It measures
329 changed target bytes. The checked group rotates old order (0,1,2,3) to
(3,0,1,2): D_8009E530, D_8009E960, D_800A3300, D_80099000. Each named symbol's
value/size/type/binding/section tuple and string adjacency is asserted. No
other symbol definitions change and every remaining ELF byte is fixed.

Protected data is exact: 189,088 bytes, 720 owners, zero differing bytes/owners.
Headers, original assembly, both dependency owners, Makefile and progress CSV
retain their frozen hashes. The 13-row guard append preserves the entire old
prefix byte-for-byte; do not globally normalize its mixed line endings.

Pinned after hashes:

| Input | SHA-256 |
| --- | --- |
| ELF | f36703ce83adebb99de90c1bc8061eec68431f36f6a366b90b2a331d25574c1a |
| game_476D0.c | 831ac69eb405bc46db96cf7f76d032f9eb9b021c89192f60843b2cd6e615f2d8 |
| Guards | c0bf9a67de2d35e5acb65eb383e82d9b6cd78323866ed44cba6a26c5998baf94 |
| Progress | 005fd7682d37802a2b7591cfb023648b6a083c8df6b957bdfedd737222cad68e |

Exact-hash inverses advance transfer -> cosine -> sine -> frustum and the
existing donor/codec history. Existing fixtures remain immutable; unrecognized
or corrupted bytes pass through unchanged and fail the actual image/input
gates. Frozen-capture corruption is rejected. No generic metadata mask or
recaptured old snapshot. The separately stale rectangle image gate remains
open and is not included in a claim that every legacy test passes.

## Banking And Next

Tools 7b6f51a commits seven owned paths first. Shared tools checks, standalone
compilation of all seven mirror paths and its two namespace-bound pure tests
pass. Before the copy, the mirror's three existing owned baselines match active
HEAD exactly; four new paths do not exist. Only those seven paths are copied.
Its independent ddbdd16 history and 516 unrelated dirty fingerprints are fixed;
523 dirty paths after the four additions is expected. All 801 original archive
file hashes remain unchanged. No mirror commit, archive edit, push or host work.

Fresh match-progress: Game 2,877/4,831 (59.55%), total 3,550/5,504 (64.50%),
different 1,954, zero address drift. Executable-only total 3,410/5,364 (63.57%);
the README retains its 140 debugger data-label convention. Conversion totals
remain 5,504/6,044 (91.07%), 86.09% bytes; Game 4,831/5,323 (90.76%),85.46%.
The README changes only its two aggregate match rows.

Full graph update fails closed at 19,088 nodes versus the existing 40,862,
preserving 19,398 nodes from 2,972 still-present excluded files. Never force
the smaller graph; await the source commit's incremental worker.
Routine task: zero Claude calls. All semantic/matching decisions are qualified
locally; no review packet, external-source fetch or tool installation needed.

Next func_1510B128: VA1510B128, ROM1385D8, 129 words, frame0x50. Qualify its
actual argument/return and direct-caller protocol before replacing the current
parameterless s32/zero placeholder or changing shared interfaces. Then continue
the failed donor/binding/codec/original Game queues and rectangle reconciliation.
The wider goal remains active; no full caller, command, hardware or gameplay
acceptance follows from this one matched parent routine.

## Post-Bank Verification

Consumer db0141f6 banks the source, guards, tools pin, aggregates and docs.
All 26 post-bank target/history checks pass in 56.618s. The incremental build
reports ELF/progress up to date and retains the four exact after hashes above.
The source commit's graph worker completes at 40,872 nodes/81,053 edges,
preserving curated/excluded nodes and skipping only oversized HTML visualization.
No forced full scan. Both active repositories are clean before this receipt-only
documentation edit; the older mirror remains independently dirty as recorded.
No push, host/Release operation or original-archive change. The wider goal is
still active with func_1510B128 and the recorded remaining queues next.
