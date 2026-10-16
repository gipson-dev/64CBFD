# Six-Piece Debris Guarded Byte Match

Date: 2026-10-16. Resume from consumer **f7a4e826**, tools **6f03b11**,
both initially clean. Bank tools **c0bbd87** first. Replace the false
zero-return placeholder for **func_15170B90** with semantic C and match all
**205 retail words / 820 bytes**, frame **0x120**, using checked guards.
**This is not a raw compiler match.** Close the prerequisites from
[Note 1423](1423-six-piece-debris-semantic-recovery-20261015.md) and
[Note 1424](1424-randomized-ring-emitter-guarded-byte-match-20261016.md).

## Steps

1. [x] Resume the six-input debris contract with the genuinely restored void ring, preserving prior captures and the strict successor checkpoint.
2. [x] Recover 205 words / frame 0x120 and escaped packet SP+0xBC using real locals; qualify the closed scheduling/register/staging-home normalization.
3. [x] Pass all 16 final target/install checks, including all 96 packet bytes, native32, fault prefixes, retained-pointer probes, rebases, callers and the actual consumer/allocator chain.
4. [x] Install only this body and declarations, append 205 guards, rebuild and explicitly reject the first slot-only image prediction. Account for the additional 84 serialization bytes without exclusions, and reproduce the entire image with two independent full relinks.
5. [x] Refresh official counts and aggregate README rows, preserve the independent tools mirror, and bank tools before consumer source/guards/pin/docs. No push.
6. [x] Audit and recover next func_15170F4C's actor/byte-flags/word-context ABI and packet lifetimes in [Note 1426](1426-table-debris-semantic-recovery-20261016.md). Retail is 158 words / frame 0xE8; the selected 158 / 0xF8 candidate still needs frame/saved-lifetime matching and remains uninstalled.
7. [ ] Continue func_1516D400, inherited-stack func_1516FE1C and every broader Game/additional-source, unconverted-caller and raw compiler-matching queue.

## Recovered Contract

Keep the address name and genuine effect-only prototype:

```c
void func_15170B90(u8 *actor, s32 baseKind, s32 variant, s32 options,
                  u8 flags, s32 context);
```

The complete retail body is VA **0x15170B90**, ROM **0x19E040**, ending at
**0x15170EC4**, with no separate padding word. Its owner is
[generated_19E040.c](../../conker/src/game/generated_19E040.c).

Snapshot signed-halfword actor coordinates +0x10/+0x12/+0x14 and coefficient
D_800A6F94. Initialize the fixed packet fields once, then emit six pieces:

- `options & 2` takes priority and copies the live six-byte D_800A6F80 object each iteration, selecting an unsigned byte. Otherwise retain the full baseKind word, adding index with defined 32-bit wrap when `options & 1` is set.
- Call func_1518C900(kind), then load the live vector triple from D_800A6E90. Position adds the snapshotted origin; velocity is X/Z times 0.08 and abs(Y) times 0.08 plus 7.
- Make six zero-argument func_150ADA20 draws. Use the signed high half: three velocity increments times 2^-14, then three spin values times 5/65536. Preserve the late asset store, kind-byte store and func_15168BE4(packet, flags, context) submission.
- After all six, call the genuine void func_151718F0 with origin X, Y-80, Z, radius 70, integer 500, float bits 0x3B960000, integer 0, integer 10, byte flags and full-word context. Only afterward set one byte at actor +0x6E to 1.

The real 96-byte packet begins at **frame SP+0xBC** in both raw and guarded
output. Fields are position +00, rotation +0C, velocity +18, spin +24,
scale +30, lifetime +3C, asset +40, coefficients +48, and control bytes
+54..+5D. Its four bytes +44..+47 and two tail bytes +5E..+5F intentionally
retain residue. Do not memset them or repeatedly reset fixed fields.
The source names those holes explicitly without claiming portable initial
indeterminate values.

The additional source at
`Another Source/CBFD-Recompiled/conker/conker/src/game/game_19E040.c`
remains unchanged/reference-only. Do not import its incorrect widths,
shifted arguments or unrelated locals. No retail function name is invented.

## Compiler And Guards

Run **42 named source/layout screens**: initial eight, stack fourteen,
lifetime nine and object eleven. Some screens compile identical bodies;
do not call them 42 independent implementations. A ternary kind choice
and branch-local six-byte staging object recover 205 words but retain
frame 0x128. Reusing one genuine float component across the three axes
recovers frame 0x120. Declaring the real packet after originX recovers
its escaped SP+0xBC home. No artificial padding locals, volatile,
fixed-register assignments or production profile/header changes.

Selected raw SHA-256:
`d91b415ed3e526a91af1f8336972e45b26c6d016050b168fb302f6e46dc20fb4`.
It emits **205 words**, has **44 real linked-word differences**, no
diagnostics and no data/rodata pool. All **eight owner neighbors** retain
their raw bytes, symbol sizes, relative relocations and normalized pools,
including the restored ring and dispatcher.

The [experiment](../../tools/experiments/game_six_piece_debris_match.py)
pins the complete raw stream and all 21 relocation sites. Retain each of
the 205 operations exactly once. Normalize two closed regions, indices
24..73 and 92..113: independent schedules, temporary/FP allocation, and
the single unescaped six-byte kind staging home **SP+0x94 -> SP+0x9C**.
The frame, escaped packet home, saved homes, branches and all nine static
call instruction boundaries stay fixed. Preserve ordered floating operands;
no floating commutation lemma is used.

The [expression checker](../../tools/experiments/game_six_piece_debris_proof.py)
compares saved roles, packet writes, read/operation multisets and ordered
FP expression trees for both regions. Canonicalize only the unescaped
kind staging object, not the escaped packet. Its boundary is ordinary,
disjoint actor/table/frame memory under the O32 provider contract, not
asynchronous/volatile, fault-order or FP-environment equivalence. Unpassed
volatile register values are not callback inputs. Nine effective dependency
negatives fail; the low-relocation addend is part of the expression, and
unsupported high/jump addends are rejected.

Append **205 expected-word guards: 158 identity and 47 transforming**.
The latter includes three binding-only changes, so it is not the raw
44-linked-word difference count. The actual production padder/assembler
emits every retail word with no insertion or omission. Preserve the old
CSV as a byte-identical prefix, including its CRLF-prefix/LF-append
working-copy behavior. Fresh-checkout newline normalization still requires
explicit fixture requalification; do not rewrite the whole manifest.

## Fresh Qualification

All **16 final tests pass in 167.798 seconds**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_six_piece_debris_match tools.tests.test_game_six_piece_debris_installed -v
```

- **1,440 whole sequences / 4,320 raw-normalized-retail runs** compare all 96 packet bytes, calls and public state. Derive first residue bytes independently from initial stack at SP+0xBC. Every one of the 205 instructions executes. Normalized/retail literal state is equal; raw private-frame bytes need not be equal because the kind home differs.
- **844 fired fault-prefix pairs** compare normalized/retail state, plus **16 guest retained-pointer probes** for RNG velocity mutation and later lookup lifetime mutation. Native C is not claimed to support arbitrary retained RNG writes or initial indeterminate-byte observations.
- **Native32 O2/O0, 1,024 cases each**, separate translation units and selected-C UBSan, check the genuine void ring ABI, all 90 initialized packet bytes and the six holes only after the provider seeds them. Eleven compiled guest/native negatives fail: unsigned RNG, narrowed asset ID, option priority, missing absolute value, spin scale, wide actor store, ring integer, cached kinds, fixed-field reset, early vector load and reserved-byte reset.
- All **205 raw-word flips, 205 production-padder word flips, 205 padder binding flips and 21 external binding changes** reject; preserve the old guard prefix. Three independently assembled original rebase sets / 72 cases change all six data and four call bindings and compare every packet byte.
- **16 captures** execute the original and current dispatcher func_15170EC4 across states 2/16, low/high-word flags and both tested stack phases, checking all six physical argument words. The dispatcher remains byte-identical; no whole-game caller claim.
- **144 connected cases** execute the actual 26-word func_15168BE4 and 28-word allocator func_15167A68. The bounded real bcopy target is 0x10023A10, not memcpy. Copy all 96 bytes, including first residue, to the allocated record +0x90. Cover zero asset and every-third allocation failure. Heap, registration, RNG, lookup and ring remain bounded or opaque; this is not gameplay/hardware qualification.
- All **801 archive fingerprints**, **75 frozen/live inputs**, capture/manifest/successor corruption controls and physical code/data/callee/metadata corruptions fire as intended. Protected layout remains **189,088 bytes / 720 owners / zero differences**.
- Both tools copies pass Windows syntax and all **eleven shared WSL padder tests**; consumer `make tools-check` passes. New target suites run in the consumer layout. Routine Claude calls: zero.

## Whole Image Audit

Do not report the first prediction as successful. Preserve immutable
`initial-prediction.json`: its slot/extent-only ELF SHA is
`b0429fedef05f574cc9e06c7ab12621564ee7e6d37fda29fa2bce33a6895c682`.
It accounts for 675 changed bytes in the 820-byte target slot and symbol
size **12 -> 820**, but the rebuilt ELF has **84 additional metadata-byte
differences**. No code/data difference lies outside the target slot.

Trace and explicitly serialize exactly two contiguous symbol/string cycles:

1. `(func_150CBCE0, D_800A3E2C)` becomes `(D_800A3E2C, func_150CBCE0)`.
2. `(D_800A6E90, D_800A2460, osCreateThread)` becomes `(D_800A2460, osCreateThread, D_800A6E90)`.

All named definitions, section membership, extents and every other byte
remain fixed. The amendment SHA-gates the rejected prediction, checks
structured records and contiguous string spans, preserves canonical symbol
definitions and requires exactly 84 changed bytes. **Fifteen effective
symbol-record/name corruptions** reject. Two independent full GNU-ld
relinks reproduce the qualified ELF byte-for-byte. Keep the distinct
`qualified-prediction.json`; do not overwrite the failed initial capture.

The final 3,257,636-byte ELF has **759 changes = 675 + 84**, with every
other byte and all **72 unaffected inputs** fixed. No section, symbol or
metadata exclusion is used.

| Input | SHA-256 |
| --- | --- |
| ELF | 9110fcc52b4a87dbbc8aed553daf25789ab8810bff2b962cadee6f001fe96283 |
| Owner | 93485699f28006bd236fdde7e64a2a328b6f1b52144d86bee1742af9b4d2604f |
| Guards | a5f47cb991e377c7f9e80faa896b4db392a7999273a958520dcc61d9d1b22b62 |

The redirected broad guest-build wrapper reports exit 1 because PowerShell
classified inherited stderr warnings as NativeCommandError. Its log
contains the completed link and progress generation, with no compiler/link
error. A direct unredirected make rerun exits zero with ELF/progress up to
date; both independent full relinks and the official report also exit zero.
Keep that distinction rather than relabeling the first wrapper successful.

## Banking And Resume

Fresh `make -C conker match-progress NON_MATCHING=1` reports **Game
2,913/4,828 (60.34%)**, **total 3,586/5,501 (65.19%)**, different **1,915**,
drift **0**. Init 492/492 and Debugger 181/181 remain exact. Conversion
data stays 5,501/6,044 (91.02%), byte coverage 86.04%. README changes only
the two matching aggregate rows; detailed updates stay in DOCS.

Tools **c0bbd87** contains six new files. The independent older mirror
remains at HEAD **ddbdd16**, with all **757 initial dirty-file hashes**
preserved. Copy only the six current-turn additions hash-equal, yielding
**763 paths**; do not reset or commit that checkout. Commit the consumer
source/guards/tools pin/docs after the tools commit. No push.

Next is **func_15170F4C**, 158 words / frame 0xE8. Its opening preserves
A1's low byte in S5 and A2's context in S6. Audit the complete routine and
its shared packet contract in a new successor directory before changing
its remaining placeholder. Keep all broader queues active. Older fixed-live
tests are historical receipts, not current-image audits. No host-port
build/launch, gameplay acceptance or frozen Release operation.
