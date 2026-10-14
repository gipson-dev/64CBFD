# Codec Frame Dispatcher Guarded Match - 2026-10-14

## Result

Continue [Note 1365](1365-codec-input-refill-guarded-match-20261014.md)
from consumer0329bd82/tools a1cd670. Replace func_151F86B0's false
zero-return C placeholder with the complete frame/metadata dispatcher.
VA0x151F86B0 / ROM0x225B60 now matches its full 112-word (448-byte) slot:
109 code words plus three original alignment NOPs. The frame is 0x130;
the public symbol's code extent is 436 bytes, not the alignment-inclusive448.

The routine advances the six-entry output ring, parses the header, invokes
the selected layer decoder, publishes an output buffer and buffer count,
then reads and optionally dispatches null-terminated metadata. It preserves
the address-keyed public name, uses descriptive locals, a typed declaration
outside the placeholder group and the existing32-bit reader interface.

This is a guarded recovery of the additional source's commented draft,
not another raw-exact import. The33 previously qualified raw imports remain
banked separately. The selected layer callback func_151F78B4 and its helper
func_151F63C4 still have zero-return placeholders. Matching this dispatcher
does not restore either dependency or establish working audio playback.

## Steps

1. [x] Pin the complete source/profile/guard/progress/image baseline.
2. [x] Compare the original draft and complete retail slot; verify output types against the streaming caller and the reader type against the initializer.
3. [x] Screen ten source variants under retail-g, retaining six real differences with the proper interfaces.
4. [x] Prove one commutative addition and one closed t0/t2 allocation exchange; append exactly six checked, relocation-free guards.
5. [x] Preserve all12 owner neighbors under O2/g3 and g, including sizes, relative relocations, normalized pools and compiler-warning counts.
6. [x] Qualify both actual padders, exactly nine mixed-profile selections and four independent original/rebased padded-to-retail comparisons.
7. [x] Pass1,800 MIPS cases,199 fired root-memory prefixes and1,500 native32 cases per O2/O0 profile, with effective compiled/corruption controls.
8. [x] Install only this body/profile selection/guard group; close the complete ELF change to332 target bytes and its12-to436-byte extent.
9. [x] Pass all113 regression checks in193.589s and project tools checks; preserve historical baseline pins through a strictly hash-gated inverse.
10. [x] Sync only six compatible task files to the older tools mirror; preserve all497 unrelated dirty fingerprints and its independent HEAD.
11. [x] Bank tools a337e52245af39564cf7197ef8f8ec501a4d17a4 before the consumer pin/source/docs, without a push or host/Release operation.
12. [ ] Qualify func_1513C350 next, then the layer decoder func_151F78B4 and its helper func_151F63C4; continue the remaining actual source/interface/binding queues.
13. [ ] Continue the original Game matching backlog, including func_151F4F38; correct the independent legacy Debugger label counter separately.

## Interface And Scheduling Evidence

The stream caller func_151F2E88 uses void *pbuf and s32 nbuf, then iterates
nbuf times while advancing pbuf by0x488. The dispatcher therefore accepts
void **outputBuffer and s32 *bufferCount, not a guessed sample count.
The reader remains func_151F6FD0_ReadFunc(s32,void *,s32,s32), with the
initializer's32-bit input handle. No shared header or public renaming changes.

Retail saves ra at frame+0x1C and s0 at+0x18. Argument homes are+0x130,
+0x134 and+0x138; context is+0x12C, decoded status+0x128, metadata[256]
starts at+0x28 and its index is+0x24. The g profile emits all109 code words,
including the original stack reloads and delay slots. Moving the index before
the array introduces13 differences and is rejected; the proper typed forms
all retain six differences with zero compiler warnings.

| Offset | Expected compiled word | Retail replacement | Scope |
| --- | --- | --- | --- |
| 0xDC | 0x01485821 | 0x010A5821 | Exchange operands of commutative addu |
| 0x10C | 0x8FAA012C | 0x8FA8012C | Closed t0/t2 allocation exchange |
| 0x110 | 0x8FA80024 | 0x8FAA0024 | Closed t0/t2 allocation exchange |
| 0x118 | 0x8D590004 | 0x8D190004 | Closed t0/t2 allocation exchange |
| 0x124 | 0x8D440000 | 0x8D040000 | Closed t0/t2 allocation exchange |
| 0x12C | 0x010B2821 | 0x014B2821 | Closed t0/t2 allocation exchange |

The static proof exchanges register8/10 only in the relevant rs/rt/rd fields
across the complete metadata-read call region, words67 through75; every word
then equals retail. All other code words already match. Each guard requires
the exact old word and no relocations. Guards supply no loop, branch, stack
frame, helper protocol, output store or missing semantic operation.

Both real padders preserve the three trailing alignment NOPs, giving a
strict112-word slot match rather than an omitted-padding comparison.
Independent links compare primary/generated padded code with separately
assembled original retail at the original address and rebased code/helper/
global addresses. The other owner bodies still come from O2/g3; only this
routine joins the eight previously qualified g selections.

## Behavioral Qualification

The1,800 MIPS cases cross five ring values (including negative and signed
overflow), two header results, three full32-bit decoder statuses, six helper
mutation modes, five public output-alias layouts and two stack phases.
Metadata lengths are1,2,4 and256 bytes, including high-bit bytes. Compare
helper calls, payloads, return status, full public memory and complete
architectural state, including saved registers and live callback lookups.
The replay reaches107 code words; words102/103 are the unreachable retail
fallback. All109 code words and three alignment NOPs remain byte-checked.

All199 actually fired root-memory prefixes compare complete state and
PC/delay-slot identity. Helpers are atomic bounded contracts for this test;
no arbitrary helper-fault or portable C-fault equivalence is asserted.
Compiled wrong-ring-wrap and reader-command controls fail as intended.
Changed expected words and expected relocation metadata are rejected.

Native32 O2 and O0 each pass1,500 cases with five public alias layouts,
complete context/output memory, callback arguments and metadata bytes.
The fwrapv profile models N64 non-trapping signed arithmetic; native
endianness is not claimed to reproduce guest byte layout.

The deliberate notifier-pointer mutation during strlen remains a MIPS
scheduling probe. Native O2 selects the function designator before strlen,
while retail reloads it afterward; C does not promise this evaluation order.
The native contract cases therefore use ordinary read-only strlen, retaining
the adversarial mutation in MIPS tests, not weakening the linked-word gate or
changing production C. Real reader-driven callback updates remain native-tested.

EOF fixtures explicitly write zero before returning a zero read count so
the subsequent strlen is defined. Production adds no terminator, bounds
check or array initialization. Overlong metadata and arbitrary unwritten EOF
bytes retain retail's unsafe behavior; they are not runtime acceptance claims.

## Closed Image And Immutable History

Exactly332 bytes change within the448-byte dispatcher slot, plus its public
symbol extent from12 to436. Every other ELF byte is fixed, including data,
overflow, retained code, addresses and symbol serialization. Protected data
remains189,088 bytes across720 owners, with zero differences. The progress
CSV stays byte-identical because the old placeholder already counted as C.

| Input | SHA-256 |
| --- | --- |
| Baseline ELF | a89a94186b0a4d2c0eedf36f927980489aa4e13783a642baf221de4760d11f18 |
| Final ELF | c9ff4e7ec28882546f87fb159a96b0c0e1c2b8fac6de4eb58725d91eef78a3bd |
| Final owner | 868215866a175a9fc063e0003eb825822e0805530149981d35791a82b366c243 |
| Final Makefile | 838070597f76ea2f7182c158dfb6710946cfcabcb5435e994f93cdb99340e313 |
| Final guards | 25d0c541e1bd0ea1d537439e8ba4234ad629ee9c5405025cc0408d99f28e5b9a |
| Unchanged progress | b7d6d464014d793ad67a1b6e39e5c4e51a29dfe87e1f5c3e8c109201d3cb2c02 |

The new inverse accepts only these exact complete after-input hashes and
projects them onto the immutable previous pins. Unknown/corrupt inputs pass
through unchanged and existing history checks reject them. Keep text/byte
crosschecks before projection so text-read controls remain effective.
No earlier fixture is overwritten, recaptured or excluded.

Private receipts and frozen inputs:
`conker/build/game-codec-frame-dispatch/`.
Fresh additional-source audit:
`conker/build/alternative-source-byte-audit-20261014/frame-dispatch-after.json`.
The successful linked raw-donor queue is empty; this does not complete the
failed-file/commented/interface/pool-binding queues.

```sh
python3 -m tools.experiments.game_codec_frame_dispatch_candidates
python3 -m unittest tools.tests.test_game_codec_frame_dispatch tools.tests.test_game_codec_frame_dispatch_candidates -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Progress And Boundaries

Fresh Game2,872/4,830 (59.46%), total3,545/5,503 (64.42%), different1,958,
drift0. Conversion remains5,503/6,044 (91.05%),86.08% bytes; Game4,830/5,323
(90.74%),85.44% bytes. Init492/492 C remains exact. Legacy Debugger181/181
includes140 data labels; executable-only total3,405/5,363 (63.49%),
Debugger41/41. Root README changes only the two aggregate matching rows.

All801 original archive files remain unchanged. The six task mirror files
agree byte-for-byte, pass syntax checks and three standalone candidate tests
in0.002s. Preserve all497 unrelated dirty fingerprints; mirror HEAD remains
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and its dirty count grows499 to503
because four task files are new. Do not reset or duplicate its history.

Tools a337e52 banks the qualification before the consumer pin/source/docs.
No push, Claude call, host transfer/build or frozen-Release operation occurs.
User confirmed that the previously path-truncated Conkers output was disposable
compiler scratch; no recovery is needed. Preserve corrected space-safe output
handling, source archive, user saves/configuration and unrelated work.

Full graph refresh again refuses the19,021-node partial scan in place of the
40,802-node curated graph, retaining19,398 nodes from2,972 excluded but still
present files. Do not force it; await the incremental source commit worker.

## Post-Bank Verification

Consumer5e41123d banks the source/profile/guard recovery, tools pin and docs.
All16 correctly selected post-bank target/capture/history checks pass33.113s.
The first invocation had two nonexistent notification test-class selectors;
its14 substantive checks passed but the command failed. Correct the selectors
and rerun the complete16-check group, without changing tests or production.
The incremental build reports ELF/progress up to date and retains the c9ff4e7e
image and b7d6d464 progress. Main and active tools are clean before this
receipt commit; the independently dirty mirror remains preserved.

The source commit's incremental graph worker completes at40,812 nodes /
81,004 edges. It preserves the curated/excluded-file boundary and skips only
the oversized HTML visualization. No smaller forced refresh is accepted.

## Next Function Handoff

Use func_1513C350 at VA0x1513C350 / ROM0x169800 next. The prior commented-source
screen emits103 words under O2/g3 with four real differences; retail frame0x38.
Its active owner conker/src/game_169510.c still uses GLOBAL_ASM and carries
the full commented body. The stable public struct210-return interface is in
conker/include/functions.h:1123; the default D_800A4AA0 declaration remains
ambiguous and must be checked against retail access and helper interfaces.
Review its full owner/callers before changing any private type or declaration.

Keep the larger codec layer follow-up separate: the prior g screen of
func_151F78B4 emits427 words/frame0x958 with79 differences. Its helper
func_151F63C4 also remains unrecovered. Original survey objects are diagnostic
evidence, not qualified active-owner replacements. Neither draft is installed,
and neither receives matching credit in this checkpoint. A graph query finds
no func_1513C350 node; direct source/assembly evidence governs this handoff.
