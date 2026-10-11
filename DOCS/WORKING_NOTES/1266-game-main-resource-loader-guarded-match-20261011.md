# Game Main Resource Loader Guarded Match

Date: 2026-10-11. Complete func_1503CF20, VA 0x1503CF20..0x1503D368,
ROM 0x6A3D0..0x6A818, 274 words / 1,096 bytes. Owner:
conker/src/game/generated_6A3D0.c. Guarded matching, not a direct C match
or a new conversion. The wider Game goal remains active.

## Baseline And Decision

Consumer ae4ef7319b5109dc57c0c98f889ee33ccb14453c, mounted tools
b9eae4717cd9f9b38a2c1fde31f9903254723e9b. Both active checkouts were clean.
[Note 1265](1265-game-main-resource-loader-first-loop-delay-initialization-match-20261011.md)
banked the complete semantic body, original 0x78 frame, saved S0..S6,
early status S6 and continuous count S5, with 22 raw differences.
The C source stays byte-for-byte unchanged, SHA-256
f43fa661893aadea680107f8ebe446bdad763489b5558996c8a906802beca058.
No compiler-profile, prototype, helper ABI, forced-local or padding change.

The additional binding/declaration sweep measures 65 complete diagnostic
forms in two successful runs (33 binding forms and 32 layout forms).
All compile without diagnostics or pools; the minimum remains 22 raw
differences. Some forms have identical source bodies; 65 is not a unique-body
claim or full behavioral qualification of every variant. Explicit main or
cleanup bindings enlarge the frame to 0x80; the cursor record retains 0x78
but has 28 differences. Config reuse/declaration order do not improve 22.

Use the repo's bounded expected-word matching mechanism, as in the adjacent
[Note 1257](1257-game-resource-buffer-preparation-guarded-match-20261011.md),
only after complete-body qualification. This changes Note 1265's source-only
next-step strategy; it does not claim those raw source differences are solved.
The selected source still emits 252 directly exact words and 22 different
words. All 274 production words must match after the guards.

## Closed Guard Groups

Append 22 rows to conker/retail_word_patches.us.csv, retaining every
historical byte and mixed line ending in its original prefix. The immutable
prefix SHA-256 is
5eace9a1e712613397671e3d8d61acfcbd1ceaa4a7a73d4377b15d97ff7400c6.
The generator checks complete length/frame/remaining-difference partition,
original epilogue, closed unused spill destinations, exact register transfers
and empty relocation sets at every patched word. No inserted/omitted words.

| Group | Offsets | Effect |
| --- | --- | --- |
| Private spill pair | 98, 9C, B8, C8, D8, F0, 108, 384, 3AC, 3C4, 3D4, 3EC, 3FC, 414 | Fourteen word accesses move main +0x50/word +0x54 to original +0x58/+0x5C; opcode/base/register unchanged. |
| Request-error return | B0, B4 | Original direct epilogue branch and literal V0 = 1 replace the S6-to-V0 return join. Full saved-S6 restoration unchanged. |
| Optional cleanup values | 3BC, 3C0, 3CC, 3E4, 3E8, 3F4 | Closed A0 load/test/NOP sequences become original V0 load/test/A0 transfer in the call delay. No callee ABI change. |

Offsets above are hexadecimal. Request output +0x6C, boundary +0x68,
half-index +0x4C, live counts/table reloads/callback order, original return
epilogue and all other 252 words remain directly exact.

## Qualification

New authored paths: experiments/game_main_resource_loader_bindings.py,
experiments/game_main_resource_loader_guarded_match.py and
tests/test_game_main_resource_loader_guarded_match.py. Six older suites
retain their frozen inputs/raw candidates/models and recognize only the exact
qualified source plus original guard prefix plus these 22 generated rows.
They independently compile the complete successor before whole-ELF auditing.

- Fourteen pre-install tests pass in 46.774 seconds after final audit-helper
  edits (the initial full run also passes in 46.540 seconds).
- Complete public reference: 1,021 cases / 2,042 executions, all 273 reachable
  original/current words; only the original duplicate compare is unreachable.
- Thirty callback cases, 175 width/sign/unsigned-size/alias cases, nine
  independent links and 1,800 fired public-access fault pairs are covered.
- Ten freshly compiled effective semantic controls; native32 complete C
  passes 6,048 cases per O2/O0 profile, including effective missing-main-free.
- Both actual padders preserve all 14 owner neighbors, extents, relocations
  and pools; their full guarded owner outputs agree.
- All 22 stale expected-word and relocation mutations are rejected by both
  actual padders: 88 fired rejections, not merely attempted negative tests.
- Forty-eight scenarios fire 4,180 original-versus-actual-padded fault pairs,
  including every private-stack/public access ordinal. Full partial memory,
  access/call traces and registers agree. Raw-C private faults are not claimed.
- The actual parent/main/extras/relocator/buffer chain passes 768 cases per
  raw/padded pass. Its deeper helpers and reachable-word coverage remain
  bounded; no complete gameplay chain claim.
- Ninety-six ignored incoming-word/identity/presence/extras cases compare
  original, raw and actual-padded forms.

The first generator run exposed tuple-versus-list epilogue equality in the
fixture, corrected before generation/qualification. No production defect.
The required manifest rebuild retains known duplicate generated_12D630 recipe
and legacy pointer/long-double compiler warnings; not a warning-free build.

The fifteen installed target tests pass, including eight fired manifest
mutation rejections: altered history, extra bytes, truncation and changed
guard operands cannot qualify as the accepted successor. All 61 older loader/
historical status-join tests also pass freshly: 76 combined tests in 372.351
seconds. Frozen inputs, raw candidates and negative controls remain intact.
Consumer/mounted/older WSL project-tools checks and native py_compile for
all nine changed tools plus three identical new-file copies pass.

## Whole-ELF Delta

Installed ELF SHA-256:
81f7a53fc8dd01e18813f618d7dde988220e76f457a719949052b718be7d501d.
Installed guard manifest SHA-256:
aa80c31e9eef9326b6a64100be34df67037a4d3dff3dfb76f89a15d054e0f6eb.

Exactly 26 target ELF bytes change from the Note 1265 raw checkpoint.
Every other ELF byte, symbol name/value/extent and metadata byte is identical.
All 189,088 protected data bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
The C source, rodata source, symbol/auto-assignment inputs and layout retain
their immutable hashes. The guard manifest preserves its exact original
byte prefix and appends only the 22 qualified rows. Conversion CSV stays
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
No other production routine changes. Required ELF/progress rebuild exits 0.

Fresh `make -C conker match-progress NON_MATCHING=1` exits 0:
Game 2,790/4,822 (57.86%), total 3,463/5,495 (63.02%), Init 492/492 and
Debugger 181/181. Zero address drift / 2,032 different. One matching credit
only, no conversion or converted-byte change. Root README edits only its
two affected aggregate matching rows; all detailed updates stay in DOCS.

## Ownership And Next Work

Single Codex writer, zero Claude calls: complete compiler output, closed
guards and independent references settle this bounded decision locally.
Commit mounted tools first, consumer guards/docs/aggregate rows/pin second.
Mounted tools f54c9fbff92e7d7e6c5d81e1ea60bdd968488f37 banks the three
new authored paths and six exact-successor audit extensions; its checkout is
clean before staging the consumer pin.
No push. Preserve the older sibling HEAD and all 22 protected existing paths;
copy only the three absent new authored paths, never overwrite its conflicting
older audits or commit/reset its independent history.
Older HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 22 protected
existing fingerprints remain unchanged; dirty entries 299 -> 302 reflect
only the three absent-file copies, identical to their mounted counterparts.
Native Graphify refresh after code changes refuses unsafe shrink
39,812 -> 18,037, retaining 19,398 nodes from 2,972 still-existing excluded
files. Protective exit 1, devcontainer zero-node and skill/package-version
warnings are preserved; no force, purge or install. Require fresh consumer
hook-log growth/UTC, a fresh Rebuilt record and zero actual Graphify/Python
workers before calling the checkpoint settled.
No OGL, Release, save, editor or private-input changes; Release remains frozen.
Guest fault models do not prove hardware/runtime/heap/rendering/gameplay or
64-bit portable C behavior.

Next connected semantic recovery: complete func_1503D368, VA
0x1503D368..0x1503D438, ROM 0x6A818..0x6A8E8, 52 words / 208 bytes,
same owner. Its current zero-return placeholder does not perform the retail
signed-byte command scan. Recover the NULL/-0x21 terminator gates, eight-byte
record cursor, opcode 1 or -0x24/subtype 0x0E conditional pointer relocation,
actual func_1503D438 call contract and callback-sensitive reload behavior.
The banked loader chain uses an explicit bounded model for this helper;
replace that boundary with the actual qualified body before broadening claims.
Removing the full loader's 22 guards remains a separate direct-C fitting task.
