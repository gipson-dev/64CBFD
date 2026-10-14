# Codec Input Refill Guarded Match - 2026-10-14

## Result

Continue [Note 1364](1364-commented-source-audit-and-object-notification-match-20261014.md)
from clean consumer531bc27e/tools5733a7d. Replace func_151F7F60's false
zero-return C placeholder with its complete codec input-refill routine.
VA0x151F7F60 / ROM0x225410 now matches all74 words (296 bytes), frame0x20.
One expected-word guard exchanges the source operands of a commutative addu.

The restored routine compacts the input window when necessary, calls the
decoder's reader, preserves the original short-read zero-fill address, updates
the byte counters and returns the pre-increment input cursor. It uses the
existing func_151F6FD0_ReadFunc typedef and32-bit input handle, descriptive
locals and a typed forward declaration outside the placeholder group.
No shared header or unrelated routine is changed.

This is a guarded recovery from the additional source's commented draft,
not another raw byte-exact import. All33 earlier raw imports remain banked.
The wider source-adoption and Game matching goal remains active.

## Steps

1. [x] Freeze the clean source/profile/guard/progress/image baseline, with all five input hashes pinned.
2. [x] Read the complete retail function, original commented draft, active callback typedef and codec initializer/caller.
3. [x] Screen seven address expressions under retail-g; retain the semantic pointer expression and one commutative-operand guard.
4. [x] Confirm the initializer stores a32-bit input handle and reuse the established reader interface without changing instruction emission.
5. [x] Qualify complete owners under both O2/g3 and g, preserving all12 neighbors, relative relocations, pools and warning counts.
6. [x] Verify both actual padders, the exact eight-function mixed profile and independent original/rebased retail links.
7. [x] Qualify1,680 MIPS cases,177 fired root-memory fault prefixes and1,680 native32 cases per O2/O0 profile, with effective negative controls.
8. [x] Install the body, select only this additional function from the existing g object, and append one checked guard.
9. [x] Close the production ELF change to239 slot bytes and the target's symbol extent; preserve every other ELF byte and all generated progress.
10. [x] Pass101 final regression checks, standalone mirror checks and project tool checks; preserve archive and independent mirror work.
11. [x] Bank tools before the consumer pin/source/docs, without a push or frozen-Release operation.
12. [x] Qualify the commented func_151F86B0 frame-decode/metadata routine: all112 slot words match with six guards. See [Note 1366](1366-codec-frame-dispatch-guarded-match-20261014.md).
13. [ ] Reconstruct remaining failed bodies/used interfaces and real pool bindings, alongside func_151F4F38 and the original Game backlog.

## Source And Matching Evidence

Retail stores ra at frame+0x14, bytesRead at+0x18, shiftBytes at+0x1C and the
argument home at+0x20. The g profile preserves its complete stack reload
sequence. The normal O2/g3 profile remains authoritative for the other owner
functions; only func_151F7F60 joins the previously qualified seven g selections.

Six address forms emit exactly74 words with only word35 different. The
negative-offset spelling disrupts the subsequent schedule and is rejected.
At offset0x8C, IDO emits0x018A2821 (addu a1,t4,t2); retail uses0x014C2821
(addu a1,t2,t4). The sole guard checks that exact source word and absence of
relocations, then exchanges only the two operands. No frame, saved lifetime,
branch, delay-slot update, helper, or cursor operation is supplied by a guard.

The active initializer func_151F85C4 stores its s32 argument at decoder+0;
func_151F6FD0 reads that field through the existing s32 reader interface.
Using that established interface also leaves only word35 different, with
zero owner compiler warnings. The callback pointer comes from decoder+4.
No new global function name or guessed semantic identifier replaces the
stable address-keyed public symbol.

Both complete-owner profiles retain the same12 neighbors, their raw words,
sizes, relative relocations and normalized pools. The production padder
selects exactly eight named g bodies while preserving the remaining O2
functions. The generated padder separately qualifies the extracted target.
Independently assembled original code agrees with both padded objects at
retail and rebased addresses, including independent helper call targets.

## Behavioral Qualification

The MIPS replay uses the existing bounded interpreter and helper-contract
hooks. Its1,680 cases cross seven input positions, five request sizes,
negative/zero/short/full read results, six helper mutation modes and two
stack phases. It compares calls, all context/window bytes, the returned word,
saved registers and complete instruction state against independent results.
It reaches72 executable words; words68/69 are the retail unreachable return
fallback. Both are still included in the strict74-word comparison.

Callback modes cover request/count changes, compaction-time cursor changes,
zero-helper changes and a reader/handle switch during compaction. Argument
registers and normal o32 argument homes are deliberately clobbered by helper
hooks. All177 fired root-memory prefixes agree on complete state and actual
PC/delay-slot identity. Helpers are atomic bounded contracts in these prefix
tests; this is not a claim about arbitrary helper faults or portable C faults.

Native32 O2 and O0 each run1,680 cases, compare every allocated context/window
byte, return value and helper call, and require32-bit pointers. The fwrapv
profile models N64 non-trapping signed arithmetic; native host endianness is
not treated as guest-endian evidence. Compiled negative controls for command0
instead of-1 and adding the cursor to the zero-fill destination both fire.
Expected-word and expected-relocation corruptions are also rejected.

The zero-fill call deliberately remains decoder+0x1C+bytesRead, without the
current input cursor. Do not silently change this to an inferred buffer
append location. The original retail load/store/helper order is the authority.
No audio playback or whole-game runtime acceptance is claimed here.

## Closed Image And Fixtures

Only239 bytes in the complete296-byte target slot change, plus its public
symbol size from12 to296. Every other byte in the ELF is fixed, including
all data, overflow, retained functions, addresses and symbol serialization.
Protected data remains189,088 bytes /720 owners /zero differences. The
progress CSV is byte-for-byte unchanged because the old placeholder already
counted as converted C; one different C function becomes exact.

| Input | SHA-256 |
| --- | --- |
| Baseline ELF | bbc201571e311a6946d21093d697b0fd7c18134e861f0e162922d4952416792f |
| Final ELF | a89a94186b0a4d2c0eedf36f927980489aa4e13783a642baf221de4760d11f18 |
| Final owner | d4ff5335ad0b03f85a580edd24cd6ab0ab2d6f01220d14a16c3ea6c8438cfa45 |
| Final Makefile | e773e5d536287a688d5c265bc6e82f667cd2e1d24e0f1747ebc47bbdb4de449c |
| Final guards | 0154601eeb05171a8af1c2ce21e4d322b0ec338142d6c0a38ea7c4bd8dd8ca24 |
| Unchanged progress | b7d6d464014d793ad67a1b6e39e5c4e51a29dfe87e1f5c3e8c109201d3cb2c02 |

The first101-check run passes100 and rejects an intermediate after-owner
fixture captured before the final callback typing cleanup. That intermediate
4ca8e22a fixture is retained and separately checked. The final d4ff5335 owner
lives in after-final-owner; no old fixture is overwritten or recaptured.
The final full rerun passes all101 checks in161.042s. The pinned inverse
accepts only the final full-input hashes; unknown/corrupt inputs pass through
unchanged and fail the existing historical checks. Current text, raw words,
profile selection, baseline capture and metadata controls remain effective.

Receipts and immutable inputs remain in
`conker/build/game-codec-input-refill/`. The fresh additional-source audit is
`conker/build/alternative-source-byte-audit-20261014/codec-refill-after.json`.
It reports zero remaining applicable raw linked donors, without crediting
failed/commented/binding cases as completed.

```sh
python3 -m tools.experiments.game_codec_input_refill_candidates
python3 -m unittest tools.tests.test_game_codec_input_refill tools.tests.test_game_codec_input_refill_candidates -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Progress And Boundaries

Fresh matching: Game2,871/4,830 (59.44%), total3,544/5,503 (64.40%), different
1,959, drift0. Conversion remains5,503/6,044 (91.05%),86.08% bytes; Game4,830/
5,323 (90.74%),85.44% bytes. Init492/492 C remains exact. Legacy Debugger181/
181 includes140 data labels; executable-only total3,404/5,363 (63.47%),
Debugger41/41. Root README changes only matching aggregate rows.

All801 original archive fingerprints remain fixed. Mirror only seven task
tool files; all fingerprints and syntax checks agree, three standalone
candidate/capture tests pass0.003s, and all492 unrelated dirty fingerprints
remain unchanged. The older mirror's HEAD stays ddbdd16b and its dirty count
rises495 to499 because four task files are new. Preserve its independent
history. Toolsa1cd6708c10bd8d1e6f7d1fb2abcdf6a940d6dd7 is banked before the consumer
pin/source/doc group; no push is performed. Zero Claude calls.

The read-only host audit confirms CMakeLists.txt:535 still selects recomp_out/.c;
its func_151F7F60 at line1445017 already has generated implementation code.
No source transfer, host build, runtime parity or frozen-Release operation
is performed. User saves/configuration and unrelated work remain untouched.

The full graph refresh again refuses to replace the40,791-node curated graph
with a19,010-node partial scan, retaining19,398 nodes from2,972 excluded but
still-present files. Do not force it. Await the incremental consumer commit
worker separately before recording its completion.

## Post-Bank Verification

Consumerf9dcbae0 banks the source/profile/guard recovery, tools pin and docs.
All16 post-bank target/capture/history checks pass68.142s. The incremental
build reports ELF/progress up to date and retains the a89a9418 image and
unchanged b7d6d464 progress. Main and active tools are clean before this
verification-note commit; the independently dirty mirror is preserved.
No push, host build, source transfer or Release operation is performed.

The source commit's incremental graph worker completes at40,801 nodes /
80,987 edges. It retains the curated/excluded-file boundary and skips only
the oversized HTML visualization. No smaller forced refresh is accepted.
