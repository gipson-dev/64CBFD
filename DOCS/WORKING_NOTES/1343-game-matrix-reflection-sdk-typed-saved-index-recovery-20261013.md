# Matrix Reflection SDK-Typed Saved Index

Date: 2026-10-13. Continue
[Note 1342](1342-game-matrix-reflection-direct-home-dispatch-and-cache-removal-20261013.md)
on `func_15034F30`: VA `0x15034F30..0x150356C8`, ROM `0x623E0..0x62B78`,
486 words / 1,944 bytes, original frame `0x190`.

## Scope And Baseline

Consumer baseline: `b35a9dc3`. Tools baseline:
`af0ed5c607622da8157ce21d9cb04e0d821f1797`. Production remains the zero-return
placeholder in `conker/src/game/generated_61D10.c`; the complete candidate is
still uninstalled. No source, guard, profile, linked-image, progress or root
README edit, no matching/conversion credit, and no host-port work.

New experiment and qualification:

- `tools/experiments/game_matrix_reflection_saved_index.py`
- `tools/tests/test_game_matrix_reflection_saved_index.py`

The wider Game matching goal remains active. The prior turn made concrete
progress by banking the direct-home checkpoint and restart verification.

## Recovered Index And Register Roles

The banked331 body strength-reduces `input+i*64` into an advancing s2 input
pointer. Naming the byte index explicitly, moving its assignment among arms,
and changing signedness does not recover retail's cross-call shifted index.
Those shared-index bodies also grow the frame to `0x198` and are rejected.
An ordinary C `register` parameter hint emits exactly the baseline words.

The real matrix-bank type changes the compiler lowering. Indexing the input
as a 64-byte matrix array and the live output as an SDK `Mtx` array recovers
the shared scaled index. The float-array form has486/frame0x190/284 differences;
using `Mtx *input` restores two operand orders and reaches282. Reuse actual
pointer locals after their matrix lifetimes for the actor callback, and replace
the redundant destination alias with a real `u32 actorFlags` local:259 differences.
No unused padding, fixed-register bindings, masks or copied instruction body.

Selected `actor-flags-u32-owner-cursor`:

| Measurement | Result |
| --- | --- |
| Complete words / frame | 486 / 400 (`0x190`) |
| Literal differences | 259, versus banked331 |
| Emitted words changed from banked331 | 125 |
| Diagnostics / extra pools | Empty / 0 bytes |
| Installation / credit | No / none |

All four retail shift instructions now match exactly: words45,52,290,297 are
`0x00139180`, `sll s2,s3,6`. The scaled index survives the input and output
matrix-helper calls. The extra advancing s2 pointer initialization/update are
gone. Loop roles now match s0 output cursor, s1 matrix pointer, s2 scaled index,
s3 item counter, s6 input bank, s7 input flag and fp output flag.

The remaining s4/s5 roles are swapped: source conversion-buffer cache s4 versus
retail s5, and byte offset s5 versus retail s4. Actor restoration recovers the
old pointer in s0, but the gate/output-home/actor-reload temporary registers
remain different. The opening still saves RA first rather than s6; the input
argument move remains later in the prologue. This is not a matched routine.

## Source Screen And Compiler Evidence

Seventy-five named complete forms produce23 extent/frame-valid literal arrays.
Full arrays, not just equal scores, establish these equivalences:

- Ordinary register-hint baseline equals baseline331.
- Typed-array and shared-index array/shift variants emit the same284 body.
- Signed/unsigned actor-flag cursor-owner forms emit the same259 body.

Reject all wrong-length/frame forms; direct/separate translation-value forms
both have486 words but frame0x198. Local reuse that removes storage can instead
shift the private layout or produce488/493 words; those are not installed.
Reusing another live temporary for the second mode snapshot gives no improvement.

The owned, fingerprint-locked compiler capture fires and preserves the whole
normal/traced object and pools. Frame transitions stay88 ->104 ->400, with
physical locals296 / saved88 / outgoing16. Frontend M288/P76 and optimizer
M296/P76 definitions remain fixed, along with all four matrix offsets
`-268,-192,-128,-64` (SP+`0x84,0xD0,0x110,0x150`). Both streams still have five
direct P+16 output loads and three direct P+8 mode reads, with no output-address
materialization. Reflection's fp cache stays removed. Only the two conversion
buffer `rlda M-268/raw register20` records remain; that cache role is unresolved.

`--probe` retains the selected/banked word comparison, fixed-input private
witness and owned frame receipt under the ignored target build directory.
Raw metadata is evidence; no undocumented stream flag interpretation or
compiler timing/cost inference is needed.

## Qualification

The new subclass retains the existing semantic, alias, live-home, native32,
caller-window, full-owner/padder, rebase, fault and protected-data gates.
Five fresh shape/native/private/index checks pass in7.707 seconds.

The typed input changes only the native fixture's input argument cast to match
the real prototype. The actual C body is not rewritten for the fixture. Native
O2/O0 retain256 cases each and all four effective negatives. The restoration
negative now targets the actual callback-pointer store (`cursor+4`), rather than
a stale `saved` spelling that no longer occurs there.

A new compiled wrong-index control shifts the actual `guMtxL2F` input by64 bytes
and produces a public mismatch. The correct selected input packet equals retail.
This proves the bank stride is operational, not only a declaration/name change.

The complete sampled guest domain covers4,800 cases with equal RAM/helper
packets. Across192 fault domains, **10,260 common cuts fire** against the
current331 baseline. All192 prior full modeled agreements survive, with no new
agreement. Output-home counts match retail and own-access-count distance never
worsens. The fixed-input witness retains equal RAM/FPRs and the same unresolved
GPR9/14 differences as banked331. Opening cut1 remains different in both phases.

These are bounded guest/native/provider-interface results, not arbitrary-input,
actual SDK execution, full-parent, hardware PC/BD/full FCSR/HI or gameplay proof.
The mixed-format alias retains its original bounded provider rejection; its
final result is not claimed. Routine work uses zero additional Claude calls.

## Explicit Historical Control References

The first complete run reports25 checks / one failure /103.400 seconds. Its
inherited lower329 rejection test expects eight failures against the historical
333 body, while the new class correctly uses331 as its previous checkpoint.
That newer reference rejects the same bad329 body in48 domains.

Only the new subclass makes those references explicit. It independently
compiles333,331,329 and the old407 diagnostic, preserving the21 older forms,
the11/15-word distinctions and exact old indirect address/load words. All eight
historical rejections remain; their domain set is a subset of the48 current
rejections. The selected count-distance gate is checked over all192 domains,
not only failed controls. No banked test or assertion implementation is changed.
The focused explicit-reference check passes in15.851 seconds. The final complete
run passes **all25 checks in99.151 seconds**, including23 target checks and the
two protected text/data checks. Its output is retained under the ignored target
directory in `full-suite-fixed.log`.

## Banking And Next Work

Production inputs, protected text/data, guards, progress and root README remain
fixed. The unchanged counts are Game2,824/4,823, total3,497/5,496, different1,999,
drift0 and converted5,496/6,044. There is no production build or aggregate credit.

Both tools copies pass ROM-free wrapper and Windows syntax checks. Older tools
HEAD ddbdd16 and all438 initial dirty-path fingerprints remain fixed, with only
two previously absent, byte-identical files added. Tools
**4efe06f102df0369df332e166dc790afc88b40b3** banks those two files first; the
consumer records that exact pin and these docs. No push, mirror-history
duplication, dependency installation, real-save changes or frozen Release work.

Direct graph update refuses18,754 proposed versus40,534 existing nodes.
Keep19,398 retained nodes from2,972 excluded-but-existing files and the current
skill0.9.20/package0.9.26, zero-node devcontainer and oversized-HTML limitations.
Do not force a shrink; record the incremental hook separately.

Reproduction from the prepared consumer root under WSL:

```sh
python3 -m tools.experiments.game_matrix_reflection_saved_index --filter actor-flags-u32-owner-cursor
python3 -m tools.experiments.game_matrix_reflection_saved_index --probe
python3 -m unittest tools.tests.test_game_matrix_reflection_saved_index \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls -v
make tools-check
```

Stay on this routine. Recover the original early s6 save/argument move, the
s4/s5 conversion-cache/offset roles, and remaining floating/temporary-register
schedules while retaining the recovered four shifts and all strict gates.
Finish all259 differences and private/fault/linked-image qualification before
installing or claiming a byte-exact function.

## Post-Bank Verification

Consumer **481d38c3eab703e818818353f08c5f79f50a2801** records the exact tools
**4efe06f102df0369df332e166dc790afc88b40b3** pin and linked documentation.
Both active checkouts are clean. Older tools retains HEAD ddbdd16 and all438
initial fingerprints, with only the two absent additions (440 dirty paths).

Eight fresh post-bank checks pass **in6.292 seconds**: all seven frozen target
inputs, private RAM/return-register boundary, owned compiler capture, opening
fault boundary, four exact shifted-index words, effective wrong-index control
and both protected text/data checks. The original input/home/ABI contracts stay
qualified; opening cut1 and returnGPR9/14 remain different, not silently waived.

The incremental hook completes at **40,544 nodes / 81,031 edges**, with zero
live graph workers. Retained history and existing oversized-HTML limitations
are intact. This is separate from the direct command's protective shrink refusal.
The new working-note link resolves; root README SHA256 remains
`640d27f289d843d625eabd94f747b399fc31105726db2a78ab245962ac885e8c`.
No push, production rebuild, dependency install or host Release work occurs.
The wider Game goal stays active on this routine's remaining259 differences.
