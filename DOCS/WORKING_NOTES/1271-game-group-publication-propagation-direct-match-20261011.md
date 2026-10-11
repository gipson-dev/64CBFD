# Game Group Publication Propagation Direct Match

Date: 2026-10-11. Complete func_1503D510, VA 0x1503D510..0x1503D5F0,
ROM 0x6A9C0..0x6AAA0, 56 words / 224 bytes. Owner:
conker/src/game/generated_6A3D0.c. All 56 words emit directly from semantic
C under the existing owner and retail profiles. No new guards, frame,
profile, recipe or global-declaration changes. Wider Game goal active.

## Baseline And Contract

Consumer 59b856104bf4e487b3822c527455096d891d64be, mounted tools
9359eb3ff803b349390408607ea66af6bd22b61c. Both active checkouts were clean.
[Note 1270](1270-game-descriptor-resource-loader-direct-match-20261011.md)
banked the direct 69-word descriptor loader. Its finish helper was still a
zero-return placeholder and modeled in the connected chain. Native Graphify
query and the full retail leaf show the caller func_1503D660 uses this helper
on both success and failure and ignores its return register.

Recover void (s32 identity), not a promised zero status. Scan five groups
using byte counts D_80098888 and byte member lists D_80084410. Empty groups
do not load their pointer. Compare each member with the original full-word
identity, without narrowing the argument or introducing a bounds gate.
On the first match only, propagate D_800D1588[identity] and the low-halfword
D_800C5A90[identity] across that group's members, then return.

The emitted group count and list pointer are cached. Each propagation
iteration reads the member byte, reads the live original pointer, stores
the pointer, rereads the same member byte, reads the live original halfword,
then stores the halfword. Preserve those reads under aliases. There are
no helper calls or private stack accesses. The incidental V0 value is not
a C return contract; the caller's instructions remain unchanged.

## Direct C Shape

Natural table-count expressions in the search and copy loops produce the
retail count hoisting, guarded pointer load and signed loop tests. Replacing
them with explicit local count/list caches was not an equivalent compiler
shape: the first diagnostic read empty-group pointers early and shortened
loops to equality tests. Guarded do-loop, argument-reuse, declaration/type
and post-increment probes also failed to provide the direct retail body.

The table form emits 56 words with one difference under both profiles:
signed lh versus retail lhu. An explicit u16 view of the existing signed
halfword table closes that word while preserving stored bits and the
existing global declaration. Final canonical CLI measurements both give
56 words, frame zero, zero differences, zero diagnostics and zero pools.
The preceding focused six-form profile comparison measured signed-table
1 difference, unsigned-view 0, and outer-do 3 under each profile.
Abandoned diagnostic objects are ignored evidence, not qualified bodies.

The default experiment command now selects the verified unsigned-view body.
Keep the existing mixed-profile owner recipe and its D804 selector unchanged;
this leaf comes from the ordinary no-unroll object. Both actual padded routes
preserve all 14 neighbors, extents, relocations, pools and the 69-word caller.

## Qualification

New tools: experiments/game_group_publication_propagation_candidates.py and
tests/test_game_group_publication_propagation_match.py. Reuse existing
compiler, guest oracle, native32, owner/pool/relocation and padding helpers.
Receipts live under ignored conker/build/game-group-publication-propagation-match-test/.

- Twelve final pre-install tests pass in 55.057 seconds. Complete original,
  raw C and actual padded streams agree on all 56 words under both profiles.
- The empty/late/duplicate/max-count/halfword/key/phase matrix passes
  1,728 cases / three forms and reaches all 56 words. Counts reach 255.
  Invalid full-word identities use mapped guest fixtures, not portable
  out-of-range array acceptance.
- Fifteen alias/payload cases pass. Explicit independently linked global
  overlaps confirm that a pointer store can change the count byte to 0x80
  or change the group-pointer table while the original count/list stay cached.
  Other cases cover member lists within pointer/halfword/count storage,
  member rereads and live source values. Guest cross-global aliases do not
  prove a portable C object layout.
- Nine independently rebased links pass 108 cases, with all four globals'
  HI16/LO16 carries, full-word keys and unused incoming registers.
- All 61 original/raw/padded public-memory fault triples fire and preserve
  full partial memory, events, calls and registers. No leaf stack accesses.
  These are guest-model results, not hardware acceptance.
- Five freshly compiled semantic mutations fail effectively; two stale
  installations reject. Three source/body/signature/newline corruptions and
  two linked word/extent corruptions reject before historical projection.
  An unrelated ELF byte remains visible through that projection.
- Complete before/after no-unroll and unrolled owners compile without
  diagnostics. Both real padders preserve all 14 neighbors, metadata,
  relocations, pools, the original D804 selector and caller instructions.
- Native32 O2/O0 each pass 71,680 cases: all 65,536 halfword payloads plus
  6,144 byte-identity/first-group/scenario cases, including 255-member lists.
  Full pointer and halfword arrays agree with an independent reference;
  a four-group mutation fails. Existing no-strict-aliasing policy applies.
  No 64-bit portable-host, real table bounds or hardware acceptance.
- The actual 69/28/61/10/35/9/56-word descriptor/remapper/request/first-list/
  count/tagged-relocator/finish chain passes 864 cases / 1,728 executions,
  reaches all 56 finish words and uses actual group publications on success
  and failure. The coverage assertion now requires all 56 words.
- The actual 14-body parent chain adds this leaf to Note 1270's 13 bodies.
  It passes 1,920 cases / 3,840 executions, with the finish hook removed,
  actual success/failure propagation and all 69 descriptor words still
  reached. Full 56-word finish coverage is established by the focused
  seven-body chain, not inferred from this inherited parent matrix.

Early qualification corrected a missing native forward declaration and a
reference comparison that included private stack bytes it does not model.
The connected reference now compares public memory/events; the stack-free
leaf's focused fault tests still compare complete memory/register prefixes.
A rebased-alias assertion initially assumed a pointer payload while the
fixture deliberately supplied A5 bytes; initialize that payload explicitly.
These were harness issues, not production defects. No frozen inputs refreshed.

The final installed/regression run passes all 85 tests in 312.816 seconds:
twelve propagation, twelve descriptor, twelve pair, eleven counter, eleven
command, fifteen guarded parent, ten earlier shape/audit checks and two
historical status-join checks. No skips, errors or failures. Older complete
candidate shapes are recompiled; their full old behavioral matrices are not
rerun. Unchanged prior semantic receipts remain prior evidence.

## Immutable Audits And Actual Delta

Only the exact complete qualified successor may reverse to the frozen
descriptor-stage source SHA-256:
491ba6e43604e7d8ce7dd9b0f60fd860eefa60bb8274e7b9c259448a2b50a526.
Require all current 56 linked words to equal retail and extent 224 before
reversing only that slot and extent onto the trusted historical ELF.
Keep every other current byte visible. Existing descriptor/pair/counter/
command projections then serve older audits. The descriptor-stage receipt
explicitly labels its propagation-projected ELF view. Frozen source/ELF/
guard inputs and negative controls are unchanged; the new suite audits
the literal current installation.

Installed source SHA-256:
0621f5de4f8c8b3f9c931d07bcf6838566b204eafbbae45869e54d572d82a3c.
Installed ELF SHA-256:
e00c6867c8189e07472107ef036ca016267b22fce90e0b32cba5bdc9f410e6e2.
Exactly 165 ELF bytes change: 164 target-slot bytes and one extent byte,
12 -> 224. All other bytes, symbol names/values/extents, data, guards,
recipe and conversion/assignment inputs are identical.

All 189,088 protected data bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Guard SHA-256 remains
92679ed3e2a6439969298cd769daf69d41e9619c81360046094cf34f1ec3faf4.
Makefile SHA-256 remains
8493bae49a7d02eac15064df9acd84044095a21ecdd877b11f12b04375943abc.
Conversion CSV SHA-256 remains
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.

Required ELF/progress rebuild and fresh match-progress NON_MATCHING=1
exit zero. Existing duplicate generated_12D630 recipe warning remains;
no new owner diagnostics.

| Section | Byte-Exact | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,468 / 5,495 (63.11%) | 0 | 2,027 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,795 / 4,822 (57.96%) | 0 | 2,027 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

One matching credit only. Conversion/converted-byte metrics stay fixed.
README changes only the two affected aggregate matching rows.

## Ownership And Next Work

Single Codex writer, zero Claude calls. Mounted tools
0e3d5204ceb3ad699e182eadc84e14ad6ba592a0 is committed first; the consumer pins
that checkpoint with source, note and concise indexes. No push.
Consumer/mounted/older WSL tools checks and native py_compile pass.
Only two finalized absent paths are copied to the older sibling.
Its HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 33 protected
existing fingerprints stay unchanged. Dirty entries 310 -> 312 are only
those copies; existing older audit paths/history are not overwritten,
committed or reset. Copies are not an older-checkout function-suite claim.

Native Graphify update exits one after refusing shrink 39,859 -> 18,078
nodes, retaining 19,398 nodes from 2,972 still-existing excluded files.
Known version/devcontainer warnings remain; no force, purge or install.
Check zero actual native workers and fresh post-commit log length/UTC/
authoritative completion before reporting the consumer checkpoint settled.

Next unrecovered connected routine: func_1503DD1C, same owner.
Body VA 0x1503DD1C..0x1503DDC8, ROM 0x6B1CC..0x6B278, 43 words.
The retail-layout slot extends to VA 0x1503DDD0 / ROM 0x6B280:
45 words / 180 bytes, including two trailing NOPs. Recover its live
halfword count and 12-byte record cursor, sentinel 0x80000000 and
current==source skips, func_1510D7AC(s32 resource identity) submissions,
count reload only after calls, original 0x30 frame/S0..S4/RA, ignored return
and parent cleanup branch. Its complete body remains a zero-return stub.

The third loader func_1503D774 is already linked-exact over all 36 words
and extent 144. It is guarded, not direct: six existing normalization rows
and one instruction-drop row remain. Do not award another matching credit
or mistake the bounded chain hook for an unrecovered source body.
Guard elimination and actual third-loader chain qualification are separate.

Deeper lookup/block loaders, remaining cleanup model, real allocation/
heap/hardware/renderer/gameplay and portable 64-bit host acceptance stay
open. No OGL/Release/save/editor/private-input changes; Release frozen.
The wider Game goal remains active.
