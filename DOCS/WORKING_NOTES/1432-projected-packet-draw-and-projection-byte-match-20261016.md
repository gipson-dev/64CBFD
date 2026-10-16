# Projected-Packet Draw And Projection Byte Match

Date: 2026-10-16. Resume from consumer **d567b2a0**, tools **eee5a08**,
both initially clean. Bank tools **51f51e1** before consumer source/guards/pin/docs.
Continue the full Game/additional-source matching goal, not just one helper.

## Steps

1. [x] Revisit the proposed func_1516D738 target against its existing source/assembly and earlier qualification; preserve the positive inherited-stack C deferral in Note 1395.
2. [x] Recover its still-stubbed func_15095760 projection/draw provider with the correct packet widths, live viewport data, SDK graphics commands and returned cursor.
3. [x] Recover float-ABI provider func_1509563C jointly; do not silently change a neighboring stub's emitted argument homing. Qualify its closed output-scheduling normalization.
4. [x] Pass ten pre-install checks, preserve 17 neighbors, predict the complete image before editing production and reproduce the predecessor link exactly.
5. [x] Install both C bodies and ten projector guards, finish the guard-dependent guest rebuild, then pass all 13 final checks and reproduce every predicted byte without exclusions.
6. [x] Refresh README aggregates and current indexes, preserve the older tools mirror, bank tools before consumer C/guards/pin/docs and allow the incremental graph refresh to finish. No push.
7. [ ] Recover func_150958B0, VA 0x150958B0 / ROM 0xC2D60, 102 words / 408 bytes, frame 0x48, ending at 0x15095A48. Audit its visible-output pointer, flag provider and unsigned-depth/FCSR behavior first.
8. [ ] Retain func_1516D738 and func_1516FE1C's C deferrals, lower rendering providers, all original callers and the wider additional-source/Game/raw-matching queue.

## Renderer Boundary

The previous handoff selected **func_1516D738**. Before adoption, locate
[Note 1395](1395-packed-fade-scale-callback-and-renderer-deferral-20261015.md)
and the existing `test_game_packed_record_scale` renderer-deferral test.
Its prior 24 original-code cases already establish that the texture chain
writes the attachment at SP+0x94, not the inherited mode word at SP+0x5C.
Those older cases are reviewed evidence, not newly rerun tests in this turn.

Keep that renderer unchanged and C-deferred. Do not initialize the word,
assume the cache-equal branch is unreachable, import an undefined C read or
reclassify an original-assembly preservation as a C match. Its final
projection/draw call occurs after the inherited word has already been read;
restoring these providers does not retroactively resolve that contract.

## Recovered Pair

Owner: [generated_C1D70.c](../../conker/src/game/generated_C1D70.c).
Retain the address-based function/global names and short semantic comments.

| Function | VA Span | ROM Span | Body / Frame | Linked Match |
| --- | --- | --- | --- | --- |
| func_1509563C | 0x1509563C..0x15095760 | 0xC2AEC..0xC2C10 | 73 words / 0x28 | Ten checked scheduling words |
| func_15095760 | 0x15095760..0x150958B0 | 0xC2C10..0xC2D60 | 84 words / 0x48 | Direct SDK-generated C |

The complete slots total **157 words / 628 bytes**; neither needs separate
padding. Function sizes grow **12 -> 292** and **12 -> 336** respectively.
The owner is not complete: all 17 other functions retain their prior words,
sizes and relative bindings, including any still-unfinished neighbors.

**func_1509563C** takes three floats, four float-output pointers and a float
maximum. Pass the selected 64-byte matrix and all eight arguments to
func_150A7A00. After that call, read the transformed W and reject
`maximum <= W || W <= D_800D9B20`. On success, compute the reciprocal,
reread the live frame index/base, apply both float scale-plus-five and
translation fields, then write X followed by Y. Explicitly capture both
input outputs before either store, including overlapping output/view cases.
Return 0 or 1. Do not replace the ordered comparisons with a positive
interval predicate that changes NaN control flow.

**func_15095760** takes a display-list cursor and signed-halfword packet.
Convert offsets **0, 2, 4** to floats and call the real projector with
maximum **4000.0f** and four distinct local outputs. Rejection returns the
incoming cursor without graphics commands. Success emits SDK
`gDPPipeSync` and `gDPSetPrimDepth`, using the live frame/view indices,
signed viewport Z scale/translation, float32 Z/W calculation and 32x signed
conversion. The SDK shift packs the high half as unsigned bits. Pass the
cursor advanced by two commands, original packet pointer, projected X/Y/W
and words **1, 0, 0, 0** to func_15095A90; return its resulting cursor.

The owner-local **0x180-byte** typed view binds the float fields and SDK
viewport data beginning at **+0x40**. It is a bounded layout view, not a
global-header migration or a claim about the original struct declaration.
The reference's wrong coordinate loads and shifted/incomplete final draw
arguments are not imported. Merely typing the old projector stub changes
it from 12 to 28 emitted bytes through float argument homing; that fails
the neighbor invariant, so the full projection provider is recovered jointly.

## Direct And Guarded Evidence

The initial complete draw emits 85 words / frame 0x50 with 46 differences.
Inlining the viewport address recovers frame 0x48. The typed layout leaves
11 differences; the SDK primitive-depth macro resolves all of them without
guards, profile changes, pools or hidden instruction insertion.

The initial staged projector emits 73 words / frame 0x28 with 35 differences.
Capturing both inputs and retaining each complete output expression recovers
the same length/frame with **ten** remaining words. Guards normalize only
the closed **+0xD0..+0x114** block's viewport loads, scratch FPRs and
independent scheduling. An exact symbolic expression-tree check preserves
each IEEE operation's within-output order, return value and X/Y store order.
No branch, frame, saved register, call, relocation or expression is replaced.
Raw projector code is not advertised as a direct compiler match.

```text
raw draw      f2976934160d9d249e48dabc657e75f68665b1e8b563b435b26f075d48ddbf06
raw projector e52a1aa70930b4178660143d7bec06b0c020de5e661362546406916e2704ad25
```

All **19 relative bindings** and both complete raw bodies are checked
before normalization. Existing guard bytes remain an immutable prefix;
exactly ten rows are appended for func_1509563C, none for func_15095760.
No shared helper, Makefile/profile, layout or conversion row changes.

## Fresh Qualification

All **ten pre-install tests pass in 58.176s**. The final **13 tests pass
in 123.196s**, exit zero:

```sh
python3 -m unittest tools.tests.test_game_projected_packet_draw tools.tests.test_game_projected_packet_draw_installed -v
```

- **576 three-way whole sequences** compare retail, normalized runtime and raw C public outputs. Cover signed coordinate boundaries, clipping equalities, live frame/view changes made by the bounded matrix provider, both stack phases and guest packet/output overlap. All 84 draw words execute; no claim is made that every projector instruction is publicly reachable.
- **80 direct projector pairs** qualify overlapping output pointers and view fields, both input reads preceding output stores and rejection/success paths. Raw private scratch/fault states are not equated to normalized runtime states.
- **Native32 O2/O0**, actual SDK headers/macros, separate translation units and selected-C UBSan, each pass **144 joint cases** exercising both functions. Check 32-bit pointers, SDK viewport size, +0x40 offset and 0x180-byte view stride. Native arithmetic is bounded to finite, nonzero divisors and valid signed conversions; this is not out-of-range conversion or full FP-environment qualification.
- All **eight compiled guest and native negatives** reject observably: unsigned coordinate, wrong coordinate stride, wrong depth scale/component, wrong draw flag, ignored rejection and upper/near equality errors. Oversized guest negatives are relocated away from the caller, so overlapping code is not mistaken for an effective control.
- **380 fired fault-prefix pairs** compare complete literal normalized runtime state. Three independently assembled original rebase sets / **48 pairs** change all nine function/data bindings, exercise low-half carries and execute both restored routines. These are guest instruction-order proofs, not portable C fault or full hardware FCSR claims.
- All **157 raw-word / 19 binding corruptions** and ten guarded output-block controls reject. All **96 frozen/live inputs**, physical code/callee/data/symbol/string controls and both strict successor-fixture stages pass. Every other ELF byte and **93 unaffected input keys** remain fixed.
- **16 original caller-window captures** establish the two-input display-list/halfword-packet interface. All four current call windows remain zero-filled; these callers are not restored by this change. Matrix transformation and the final draw provider are bounded opaque models here, not full rendering/gameplay acceptance.

Negative-control review caught a test-only output buffer overlapping the
oracle's private-stack filter. Move it to a distinct mapped buffer and add
an explicit non-overlap assertion; rerun all guest controls and full suites.
Also recompute the physical draw fingerprint directly from the object,
rather than trusting a cached measurement row in corruption tests. These
are fixture/verifier corrections made before production acceptance.

Both tools copies pass Windows syntax and all **eleven** shared WSL padder
tests; `make tools-check` passes. No shared tool is edited. Prior unchanged
neighbor-suite receipts are prior evidence, not fresh reruns. Claude calls: zero.

## Image And Progress

Capture the old padded owner object and link script before production edits.
The baseline full link reproduces the predecessor exactly. The qualified
link equals the independently declared two-slot/two-extent prediction.
After source/guard installation, the manifest dependency triggers a broad
guest rebuild. It exits zero despite repeated pre-existing warnings;
the complete rebuilt ELF still equals the original prediction byte for byte:
**490 changed code/extent bytes**, zero extra metadata changes/exclusions.
Protected data remains exact across **189,088 bytes / 720 owners**.

```text
before ELF 1186370e78964af1417bcdf165ab7d24a41f9d8e02fd3fffcbda1e1c63c412de
after ELF  69c218a15ca4353aecda5233b8258f1f36da39a56b788a82375a0d7ffdb4e333
after C    8228375aead0d0dafd047760f476ec09f4c6ef375af7b95bf0ac128e3ffa02ff
guards     420648a53d79abb7b62309f862d41a7fc28aa531f36663b545cefd4a55af2c60
```

Fresh official totals: **Game 2,920/4,828 (60.48%)**, **total 3,593/5,501
(65.32%)**, different **1,908**, drift **0**. Init 492/492 and Debugger
181/181 remain exact. Conversion totals stay 5,501/6,044 (91.02%), converted
bytes 86.04%. Root README changes only the two aggregate matching rows.

Tools **51f51e1** banks the five experiment/oracle/checkpoint/test files first.
The older mirror keeps HEAD **ddbdd16** and all **791** initial dirty-file
hashes. Copy only five new absent files for **796** final dirty paths;
do not commit/reset the mirror. Bank consumer C, ten guard rows, tools pin
and docs separately. Let the normal incremental graph hook finish without
forcing a full scan or dropping retained excluded nodes. No push or
host-port/frozen Release build, modification or launch occurs.

## Next Audit

**func_150958B0** spans ROM **0xC2D60..0xC2EF8**, VA
**0x150958B0..0x15095A48**, 102 words / frame 0x48. Its third argument is
an actual visible-output pointer, unlike an unused homed argument. It uses
the restored projector, calls func_15095B08 to update visibility, then
conditionally emits depth commands. Audit **D_8009DEC0**, its unsigned
float-to-integer depth conversion and full **FCSR save/restore** sequence;
do not reuse the signed conversion from func_15095760 without qualification.
Keep the renderer deferrals, original callers and wider Game goal open.
