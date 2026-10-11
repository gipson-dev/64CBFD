# Game Command Weight Counter Direct Match

Date: 2026-10-11. Complete func_1503D984, VA 0x1503D984..0x1503DA3C,
ROM 0x6AE34..0x6AEEC, 46 words / 184 bytes. Owner:
conker/src/game/generated_6A3D0.c. All 46 retail words emit directly from
semantic C, no new guards, padding substitutions or compiler-profile changes.
The wider Game matching goal remains active.

## Baseline And Contract

Consumer bc606ed28b88c5c086ceb4170c08bd4bdc192243, mounted tools
349aa214c1621a556de1d172f2086a51952034d9. Both active checkouts were clean.
[Note 1267](1267-game-command-stream-relocator-direct-match-20261011.md)
banked the complete 52-word command relocator. The next counter was still a
zero-return placeholder, and the loader chain modeled its helper boundary.
Local Graphify query and the complete assembly confirm the one direct caller
in func_1503CF20 passes identity and ignores the result.

Recover a void (s32 identity) interface and the missing extern s16
D_800C5918[] declaration. There is no identity validation or NULL gate in
this routine. It loads D_800C4488[identity], reads only its first command
pointer, then scans eight-byte records until signed opcode -0x21 / 0xDF.
Every opcode is extracted from a full 32-bit first-word load, not a byte read.

Opcode 5 contributes one, opcode 6 contributes two, and signed opcode >> 4
equal to one contributes four. Negative opcodes do not satisfy that last
test. The result is published with one halfword store to D_800C5918[identity].
The native boundary tests confirm low-16-bit publication through signed-half
wrap. Retail also leaves the full count in V0; tests verify that incidental
machine value without advertising a C return-value contract. A return-count
source variant is measured, but is not the selected source or an ABI finding.

The selected complete source retains the one-entry outer loop and explicit
commandIndex * 2 word indexing. Under the existing -O2 -g3 -Wo,-loopunroll,0
profile, IDO naturally strength-reduces the inner index to the original live
pointer, including its opening OR copy, opcode extraction, branch-likely
read and cursor update. No stack frame or saved-register spill is introduced.
The typed caller's instructions are unchanged.

The full diagnostic sweep succeeds for 77 complete forms, with zero compiler
diagnostics or data pools. Four indexed word/full-opcode/Gfx/byte-view forms
match all 46 words. Some source bodies repeat, so 77 is not a unique-body or
full behavioral qualification claim. Pointer-cursor forms emit 45 words and
do not match; returning-count variants also differ. Only the canonical
indexed-word body is installed and fully qualified.

## Qualification

New authored tools: experiments/game_command_weight_counter_candidates.py
and tests/test_game_command_weight_counter_match.py. Reuse the established
IDO, MIPS oracle, native32, owner, pool, rebase and padding helpers. Receipts
are under ignored conker/build/game-command-weight-counter-match-test/.

- Eleven final pre-install tests pass in 24.555 seconds. All 46 raw,
  original and actual-padded words agree, no new guards, frame zero.
- All 256 signed opcodes, four lower-word payload patterns and two stack
  phases pass 2,048 cases / three forms. Every one of the 46 words is
  exercised. Reads are exactly four bytes; publication is exactly two bytes.
- Sixty-one mixed-length/alias cases cover immediate DF, streams through
  511 records, all three weights, signed negative opcodes and destination
  aliases with table words, payloads and already-read commands. Full modeled
  memory/access order is preserved. The second table entry is never read.
- Nine independent links pass 108 identity/unused-register/stack-phase cases,
  including independent HI16/LO16 carries. Guest wrapped identity addresses
  are qualified only within mapped fixtures; this is not portable C or
  real-table out-of-bounds acceptance.
- Every word-read/halfword-store ordinal fires: 66 original/raw/padded fault
  triples agree on complete partial memory, access events, calls and registers.
  This leaf accesses no private stack. Faults are a guest-model result.
- Eight freshly compiled effective semantic mutations and three stale
  owner/interface install rejections pass.
- Complete before/after owner compilations have zero diagnostics. Both real
  padders preserve all 14 neighbors, bytes, extents, relocations and pools,
  including the typed parent and the exact command relocator. Routes agree.
- Native32 O2/O0 each pass 67,864 cases: all 65,536 opcode pairs, all 256
  valid native-fixture identities, 2,064 mixed-length/payload cases and eight
  long-stream halfword-wrap boundaries. All modeled output halves, pointer
  slots and stream words agree with an independent reference. An altered
  four-weight increment fails. No signed-32-bit counter overflow is claimed.
- The actual 104/274/52/46/56/9/194-word parent/main/command/counter/extras/
  relocator/buffer chain passes 768 cases and reaches all 46 counter words.
  The former prepare helper hook is replaced with this actual body, including
  the real three weighted opcode paths. Deeper helpers remain bounded.
- Four altered body/prototype/declaration/source inputs and two changed
  word/extent inputs are rejected by the historical projection. Unrelated
  ELF bytes survive projection for whole-ELF rejection; frozen inputs remain.

The first pre-install audit run caught a duplicated existing declaration in
the proposed insertion anchor. A unique existing declaration is now required;
the final suite passes before production installation. No production defect.
The candidate generator's final complete sweep and native py_compile pass.

After installation, 49 fresh tests pass in 145.149 seconds: eleven counter,
eleven command-relocator, fifteen complete guarded-parent, ten earlier loader
shape/whole-ELF checks and two historical status-join shape/audit tests. The
31 historical candidates are recompiled, but their complete semantic matrix
is not rerun here. Unchanged prior semantic receipts from Notes 1266/1267 are
reused explicitly, not counted as fresh tests.

## Immutable Historical Audits

The narrow successor helper accepts only the exact selected counter body,
typed prototype and one new declaration. Reversing these edits must reproduce
the frozen command-stage source SHA-256
0f8594be47c2082c073901586c8a3a7ee74b6a4b70588de92729e61d3ba0c52d.
Before projection it independently requires all 46 current linked counter
words to equal retail and its symbol extent to be 184 bytes. Only that slot
and its extent are reversed onto the trusted historical ELF. All other
current bytes remain subject to the original whole-ELF checks.

The existing command-stage helper then applies its separately qualified
52-word projection for older parent audits. Neither historical stage's
frozen inputs, references, candidates, controls or guard prefix is refreshed.
Historical receipts are explicitly projected views, not a claim that the
literal current owner source/ELF is unchanged. The new counter suite audits
the actual production delta. Parent func_1503CF20 still has 252 direct words
plus its existing 22 guards; this counter does not eliminate those guards.

## Actual Delta And Progress

Installed source SHA-256:
6456ebae21a9227a74bbd15b19dba47cba8319f01c1e02d2d517da09a8df6fa2.
Installed ELF SHA-256:
b714ed2f171bce3917539e59a91ae6ee1f1571f2e9665dc495f7ec579133a01b.

Exactly 126 ELF bytes change: 125 in the target slot and one symbol-length
byte as its extent changes 12 -> 184. Every other ELF byte, metadata byte,
symbol name/value/extent, data byte and assignment input remains identical.
All 189,088 protected data bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
The guard manifest is byte-identical, SHA-256
aa80c31e9eef9326b6a64100be34df67037a4d3dff3dfb76f89a15d054e0f6eb.
Conversion CSV is byte-identical, SHA-256
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
Required ELF/progress rebuild exits 0, retaining the known duplicate
generated_12D630 recipe warning. No new owner compiler diagnostics.

Fresh `make -C conker match-progress NON_MATCHING=1` exits 0:

| Section | Byte-Exact | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,465 / 5,495 (63.06%) | 0 | 2,030 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,792 / 4,822 (57.90%) | 0 | 2,030 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

One matching credit only. Conversion/converted-byte metrics stay fixed.
Root README changes only the two affected aggregate matching rows.

## Ownership And Next Work

Single Codex writer, zero Claude calls. Mounted tools
23570e99b9cc1fd3e0dc16f4ce909b02c48fca8e is committed first; the consumer
source/docs/aggregate rows pin that exact tools checkpoint. No push.
Consumer/mounted/older WSL project-tools checks and native py_compile for all
four changed tools plus two identical absent-path copies pass.
Older sibling HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 27
protected existing fingerprints remain unchanged. Its dirty entries 304 -> 306
reflect only the two new-file copies. Do not overwrite its older audits or
commit/reset its independent history.

Native Graphify refresh exits 1 after refusing shrink 39,830 -> 18,049 nodes,
retaining 19,398 nodes from 2,972 still-existing excluded files. Known
skill/package-version and devcontainer zero-node warnings remain; no force,
purge or install. Require fresh consumer hook-log length/UTC, a fresh Rebuilt
record and zero actual Graphify/Python workers before calling it settled.
No OGL/Release/save/editor/private-input changes; Release remains frozen.
Guest/native32 qualification does not prove real heap/hardware/renderer/
gameplay or portable 64-bit host behavior.

Next complete connected recovery: func_1503D804, VA
0x1503D804..0x1503D984, ROM 0x6ACB4..0x6AE34, 96 words / 384 bytes,
same owner, still a zero-return placeholder. Recover the identity-0x24
94-record gate, already-published early return, original base/record lookup,
allocate_memory(94 * 4, 1, 0, 2), result publication/failure status, signed
halfword pairs at source offsets +8/+10, 16-byte source/four-byte destination
strides, remainder/four-record unroll and original 0x38 frame/spill lifetimes.
Qualify the complete routine before replacing that secondary helper model.
Parent guard elimination and wider runtime acceptance remain separate work.
