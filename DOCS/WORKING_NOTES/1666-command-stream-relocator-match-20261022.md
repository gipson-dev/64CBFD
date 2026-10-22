# SDK Command-Stream Relocator Guarded C Match

Date: 2026-10-22

## Result

Recover `func_150049A4` in `conker/src/game_30E90.c` from its zero-return
placeholder. Complete SDK-based C emits **42 words, an eight-byte frame and
no relocations**. Eleven checked fields keep one cursor lifetime in retail's
a1 instead of the compiler's v1, making the linked body byte-exact.
This is guarded C, not compiler-only matching. No inserted words, frame
patches, dummy locals or compiler-profile changes.

VA150049A4..15004A4C / ROM31E54..31EFC, ends exclusive.
Preserve the original `asm/nonmatchings/game_30E90/func_150049A4.s`.
Raw unlinked body SHA-256:
`96fd852b9c2b0f8ab38902b04579f9b8704ea989d71734f5727fe8642e22030d`.
The old body was 12 bytes in a 168-byte slot. One additional exact match;
the converted-C count and denominator do not change.

Keep the address-based name, descriptive parameters and purpose/quirk
comments. Recover `void func_150049A4(s8 *, u32 dataOffset, u32 matrixOffset)`
and its local prototype. Both retail caller sites ignore V0; the loop index
remaining there is verified machine behavior, not a new C count-return API.
No shared-header or caller-source changes.

## Recovered Contract

Walk eight-byte commands until signed opcode `(s8)G_ENDDL` (-33). Read the
first byte for the empty-list precheck and again for the first loop body.
Recompute the cursor from the original base and index; increment the index
for each processed command. Retail preserves matrixOffset in saved S0 across
the loop, with the original save/restore and eight-byte frame.

For G_VTX (1), add the complete dataOffset to the word at command+4 with
32-bit unsigned wrapping. For signed G_MOVEMEM (-36), first read byte3 as
unsigned and add matrixOffset only for G_MV_MATRIX (14). Do not dereference
the relocated payload addresses. Other commands leave payloads unchanged.

Preserve retail's positive G_DL comparison (222) after the signed byte load.
A real byte0xDE becomes -34 and cannot enter that case. The SDK-based source
and purpose comment make this deliberate matching boundary visible; changing
it to a signed G_DL test is an effective wrong-C control, not a matching fix.

Use a valid, backed, terminated stream for ordinary C/native qualification.
The loop has no length/error guard because retail has none. Do not claim
safe behavior for malformed streams, unaligned word accesses or arbitrary
ISO C pointer wrap/concurrency.

Several returning/nonreturning, declaration and loop forms fail the retail
extent, opening reads or saved roles. The indexed for-loop recovers the full
shape; removing redundant initializations and using SDK constants leaves the
same raw body. The attempted O1 screen was rejected by asm-processor setup
before compilation, so no O1 result is claimed. Production stays normal O2/g3.

## Cursor Guards

| Offset | Expected | Replacement | Field |
| --- | --- | --- | --- |
| 0x01C | 0x00801825 | 0x00802825 | OR cursor definition rd3 -> rd5 |
| 0x044 | 0x8C790004 | 0x8CB90004 | LW cursor base rs3 -> rs5 |
| 0x050 | 0x8C6F0004 | 0x8CAF0004 | LW cursor base rs3 -> rs5 |
| 0x05C | 0xAC780004 | 0xACB80004 | SW cursor base rs3 -> rs5 |
| 0x060 | 0x8C790004 | 0x8CB90004 | Original unreachable LW base |
| 0x06C | 0xAC6D0004 | 0xACAD0004 | SW cursor base rs3 -> rs5 |
| 0x070 | 0x906E0003 | 0x90AE0003 | LBU cursor base rs3 -> rs5 |
| 0x07C | 0x8C6F0004 | 0x8CAF0004 | LW cursor base rs3 -> rs5 |
| 0x084 | 0xAC780004 | 0xACB80004 | SW cursor base rs3 -> rs5 |
| 0x08C | 0x03241821 | 0x03242821 | ADDU cursor definition rd3 -> rd5 |
| 0x090 | 0x80660000 | 0x80A60000 | LB cursor base rs3 -> rs5 |

Before the first cursor definition, word3 captures the incoming a1 data
offset in a3. Prove that a1 is then vacant and that every later v1 field is
one of these two definitions/nine memory operands. Change only that field;
keep every opcode, data operand, immediate, branch, delay instruction and
frame operation. Pin the complete raw body/empty bindings and reject stale
words or any additional v1 use. Append exactly eleven rows with the old CSV
prefix intact, including all ten neighboring func_15004CE0 guards.

For raw C, qualify an explicit register relation: its v1 cursor equals
retail's a1 cursor, raw a1 retains the input offset, and retail v1 retains its
incoming value. All other modeled registers, memory accesses, effects and
state agree. Before the first cursor definition, require literal register
agreement too. Guarded C agrees literally with retail across full modeled
state and fired fault prefixes. Do not call the raw registers byte-exact.

All 42 static words match. Dynamic cases visit 37 words. Four words of the
positive G_DL body and the duplicate LW at15004A04 are unreachable from the
signed-byte interface; reproduce them statically, without claiming execution.

## Caller Bounds

The aligned retail scan finds exactly two JALs at ROM3088C/308B8, corresponding
to VA150033DC/15003408 in `func_150031EC`, and no literal target pointer.
These are static observations, not exhaustive runtime-target proof.

Execute the actual six-word window at 150033CC..150033E4 and three-word
window at 15003404..15003410 over 24 phases. The first reads the stream through
s1, reads the bank word through a7, adds 0xFF000000 in the call delay slot and
forwards s0 as matrixOffset. The second reads the stream from s0 and forwards
s0 as matrixOffset; its full a1 value is an explicit entry precondition.
Both reach their real return boundaries with the correct call packets.

Do not execute or synthesize continuations to claim a full caller. The parent
is 178 retail words and its current production body remains a 12-byte stub.
The windows do not restore the complete asset loader or establish gameplay.

## Qualification

Tools: `experiments/game_command_stream_relocator.py` and
`tests/test_game_command_stream_relocator.py`, identical in both copies.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests,92.388s | 8 tests,109.459s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests,1.779s | 2 tests,1.816s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks per copy only under strict
source, raw/padded object, input and complete-image identity. They are not
fresh installed executions. Both shared tools checks pass (0.123/0.117s).

- 12,298 guest phases cover all 256 opcodes, unsigned tag boundaries, full
  offsets, wrapping payloads, empty and multi-command streams, two SP phases
  and streams through 257 commands. Check exact accesses, all memory/fences,
  incidental V0 count, saved S0 and the raw cursor-register relation.
- Native32 O0/O2/O3 each pass 73,728 selected-body cases with trap UBSan,
  backed packet arrays and whole-arena fences. Eight effective defined wrong-C
  controls cover both offsets, vertex opcode, matrix index, signed MOVEMEM,
  signed G_DL, payload width and terminator. A backed alternate terminator
  keeps the wrong-terminator control finite. Use the established alias flag
  for generic memory views, not as a claim of ISO object-layout portability.
  Batch selected/controls into three native compiler invocations.
- Eighteen guest header-read interventions qualify the opening double-read.
  Compile an actual cached-opening wrong-C body and reject its wrong payload
  update after a first-read intervention. This is emitted-read evidence, not
  portable C concurrency. No external function providers are needed.
- Six independent GNU links and 72 rebase/wrap phases pass, including bounded
  guest32 address wrap. Check 196 fired root-data fault prefixes, 15 guard
  corruption controls and five whole-image corruptions. Do not infer hardware,
  MMU or portable C fault/wrap semantics.
- Pin 26 historical inputs plus the predecessor padded object. Preserve all
  eight raw/padded neighbors and pools. Isolated diagnostics remain empty;
  owner diagnostics are unchanged. Three productive normal Make commands use
  the ordinary layout-based pad_c_object route, with cleanup alone skipped.

## Production

Seal 15,834 live/cache files, including all 1,454 linker objects. Preserve all
1,544 old mirror dirty paths, statuses, hashes and HEAD; add only two task
files, leaving 1,546 dirty paths. Do not reset or commit that mirror.
Commit tools first: `c24126276ae5a23ef6788d3fb504a162ebdc55cc`. No push.
Routine Codex-only qualification uses zero Claude calls.

Normal Make rebuilds the owner, linked ELF and progress CSV in the verified
Linux copy (0.471s). Mark only the qualified target-only guard append old to
avoid unrelated rebuilds. Revalidate live inputs before adopting four
generated outputs. Linker-script and conversion-CSV bytes remain unchanged.
The existing duplicate generated_12D630 recipe warning remains; this is not
a warning-free build. No new compiler diagnostics.

The independent full-ELF prediction is reproduced with zero exclusions:
**126 changed bytes =125 code bytes +1 target-size metadata byte**.
All other 6,054 bodies, all 6,055 addresses and all 720 protected Game-data
owners /189,088 bytes remain fixed. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`dd23f700e3ae8219783c96e850b627d805f058cb00b19b7f494a091632434bda`.
Installed padded owner:
`82e69be28eb11d02f37e37f48713304b083233bfef70115bad36dcbb0950b7c5`.

## Handoff

The standard live-ELF matcher reports total **3,734/5,505 (67.83%)** and
Game **3,061/4,832 (63.35%)**. Init492/492 and Debugger181/181 remain exact.
Zero address drift; 1,771 different. The 75% threshold remains 4,129 exact:
**395 more matches are needed**. Queue shapes: 1,640 placeholders, 122
semantic/other and nine unlocated entries. Next `func_150BA37C` is screened
only, not edited or credited. Keep `func_1508CAD8`'s 862-word stub queued.

Root README changes only aggregate rows. Detailed progress stays here and in
concise indexes. Post-commit graph-worker and every-old-node retention audits
remain private receipts; retain the excluded-corpus/large-HTML caveats without
claiming full re-extraction. Frozen host Release remains untouched.
