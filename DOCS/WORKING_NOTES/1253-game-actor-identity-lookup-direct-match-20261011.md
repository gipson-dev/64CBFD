# Actor Identity Lookup Direct Match

Verified 2026-10-11. Consumer baseline
f0b122aa0fe0a32acb7c6908a82c078ba2889b75; mounted tools baseline
630eaf9708a09de4dcdb2f4729e227228b48ba47. New tools
69e37a6b9be51a78ef688bce2571c439beba59bc committed first. No push.
Single Codex writer, zero Claude calls; DOCS/AGENT_WORKFLOW.md applies.
Previous goal turn banked the record-index query and census correction.
This finishes another complete routine; the wider Game goal remains open.

## Recovery And Direct Match

Recover func_15083E90, VA 0x15083E90..0x15083FB0,
ROM 0xB1340..0xB1460, in conker/src/game/generated_AEB40.c.
Replace the 16-byte byte-argument zero-return placeholder with the complete
u8 *(u8 selector) lookup. All 72 words / 288 bytes emit directly from C,
no frame, eight relocations, no new guards, pools or compiler profiles.

The preceding handoff mistakenly described 25 actors, slots 0..24. The
complete loop actually covers 26, slots 0..25: slot zero and slot one are
peeled, then the counter starts at 2 and advances by four to exclusive end
26. The first 25-slot candidate emits 62 words/52 differences and omits
the valid last slot. Correcting the full source bound to 26 gives a direct
72-word match. Explicit slot-25 and outside-slot-26 negatives qualify that
correction; the earlier note's next-target bound is corrected with a link.
An indexed-address expression instead of the pointer cursor emits 72 words/
36 differences; a word selector emits 68 words/71 differences.

- Store the complete incoming argument word at SP+0 before narrowing its
  low unsigned byte. Zero selector returns NULL without reading the pool.
- Scan the D_800CC2D0 array, 26 records with 812-byte stride. A nonzero
  32-bit presence word at +0 enables the identity byte read at +0x3B.
  The presence gate is not a byte check and does not require positive sign.
- Return the first active matching actor pointer. Inactive matching IDs are
  ignored, duplicates preserve first-match selection, no match returns NULL.
- Preserve all branch-likely next-presence accesses and the final cursor
  update. Slot 26 may be the final unused cursor but is never dereferenced.
  The pointer/count state does not call out or reload an external limit.

Inspect complete retail caller interfaces in AEB40.s, C4DC0.s, F4D20.s,
142560.s and 1E26F0.s, plus current C wrappers/callers generated_AEB40.c,
done/game_35EC0.c, generated_F4D20.c and generated_142560.c. Return use
includes NULL gates, actor-byte/float access, index conversion and global
pointer publication. Existing s32 caller declarations use the same O32 GP
argument route; the callee performs the retail low-byte narrowing. No caller
prototype sweep or unrelated consumer edits.

## Fresh Qualification

Ten final tests pass after installation and rebuild, 22.610 seconds.
Immutable snapshots and fresh independent receipts are in
conker/build/game-actor-identity-lookup-test/. Consumer make tools-check
and mounted standalone check_project_tools.py both pass under WSL.

- 15,802 independent-reference cases / 31,604 original/C guest runs: every
  selector byte and slot, absent/slot zero/one/25/outside 26, two stack phases,
  full upper GP words, nonzero presence 1/2/0x80000000/0xFFFFFFFF, inactive
  IDs, empty pools, holes and first duplicates. Complete memory, ordered
  accesses, return, GP/FPR and zero calls agree.
- Reach all 68 executable retail words. Four redundant unroll words at
  offsets 0x78, 0x9C, 0xC0 and 0xE4 follow unconditional returns and are
  bypassed by both branch paths. They match statically; do not claim dynamic
  coverage of those unreachable duplicate updates/loads.
- 28 alias/short-circuit cases / 56 runs and 402 fired full-access fault
  pairs: selector zero accepts unmapped pool; inactive slots accept unmapped
  identity bytes; first match skips unmapped later records; slot 26 storage
  is wholly unmapped and skipped. Rebased private pools put presence or
  identity fields under SP+0 so the full argument-home store changes later
  reads. Every fault gate fires; full partial memory/accesses/calls/GP/FPR
  agree. Private alias/fault order is guest-only, not portable C behavior.
- Three independently located pools / nine original/C/production-padded
  links, 18 cases / 54 runs. Rebase code and global HI16/LO16 sites across
  signed low-half carries. Original D_800CC30B and D_800CC5FC labels remain
  physically consistent with base+59 and base+812, not independent globals.
- Actual copied-owner preprocessing, IDO compilation and asm post-processing
  preserve all 30 neighbors' full fingerprints, extents, relocations and
  normalized pools with zero owner diagnostics. Both layout/generated-owner
  production padding routes preserve all non-target text/relocations and
  every existing guard fingerprint. All previously completed helpers remain
  unchanged; historical suites are not represented as freshly rerun tests.
- Ten effective fresh IDO negatives: argument width, too-short/too-long
  bounds, presence inversion/byte width, identity offset/sign/comparison,
  stride and missing zero gate. The signed-byte negative uses existing local
  CopyOracle support; no shared helper edits. Add one effective native
  last-slot negative. Qualified C includes all retail slots, not a smaller
  compatible-looking scan chosen to make a test pass.
- Native32 O2/O0 each pass 21,504 cases, 43,008 total: every selector and
  match position, inactive/duplicate/full presence patterns, last valid slot
  and first invalid slot. Verify 32-bit pointer/integer widths and every pool
  byte unchanged. No host gameplay or hardware acceptance claim.
- Connect actual complete current byte-exact 20-word func_15083FB0 and
  20-word func_15008A10 with original/C lookups: 160 cases / 320 runs,
  240 helper calls per form. No callback models. Independently verify the
  wrapper's signed index/-1 result and the two-call caller's two pointer
  publications and three floating zero stores. Both complete caller bodies
  are verified against the retail ROM and remain unchanged in the final ELF.
- Connect complete 47-word retail func_15097910 with the banked, linked
  byte-exact 33-word func_15083E0C record query and original/C actor lookup:
  864 cases / 1,728 runs, 384 lookup calls per form. Neither query is a
  callback model. Independently verify -1, zero index, actor state-byte flags/
  0x2000 and requery after modeled initialization. Only func_15082A44 remains
  a bounded callback. The retail caller's current C is still unrecovered;
  this does not qualify its current installed body or deeper initialization.

One post-install fixture assumption failed: the saved byte-argument stub
has ST_SIZE 16, not the no-argument placeholder's 12. Verify its exact
four instructions (full argument store, zero result, return, nop), assert
16 explicitly, then require only 16 -> 288 ST_SIZE change. Do not loosen
the whole-ELF audit or overwrite the baseline. All ten final tests are fresh.

## Linked Audit And Progress

Only 226 ELF bytes change, inside the target's 288-byte slot and its
16 -> 288 ST_SIZE field. Every other ELF byte and metadata field is exact.
ELF 3,261,160 bytes, SHA-256
28e9c9a3fc995b13e0e44e87f47fccc92852a3a15f64f8f0dbf9d0f547d1a03a.
Protected data: 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
New owner: 13,053 bytes, SHA-256
5ab9d17221d86fd508faa1848e6f728236cab4d2fcc95d4bf575c7e22380651d.

Guards stay byte-identical at 1,940,850 bytes, SHA-256
5e50f8952c0e5d4ba39b7e9054b7ac5727517d021ba8e92d3b10c8a2f07b2f19.
Conversion CSV stays byte-identical at 317,252 bytes, SHA-256
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
Rodata, layout, symbol addresses and ignored auto assignments remain exact.
Linked rebuild succeeds with existing duplicate generated_12D630 recipe
warnings; no warning-free full-build claim. README changes two matching rows
only; function-by-function updates remain in DOCS.

Fresh matching: Game 2,785/4,822 (57.76%), total 3,458/5,495 (62.93%),
zero drift / 2,037 different. +1 matching only, no converted credit.
Converted stays 5,495/6,044 (90.92%), Game 4,822/5,323 (90.59%), converted
bytes total 86.01% / Game 85.37%. Init 492/492 and Debugger 181/181
already-converted functions remain exact.

```sh
python3 -m tools.experiments.game_actor_identity_lookup_candidates
python3 -m unittest tools.tests.test_game_actor_identity_lookup -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
cd tools && python3 check_project_tools.py
```

Older standalone tools HEAD ddbdd16 stays unchanged: 275 existing dirty
entries plus two absent-only byte-identical new mirrors = 277. Protected
older helpers remain exact; no existing paths overwritten or committed.
Native Graphify query found 63 nodes, showed 24 and truncated 39. Both native
updates exit 1, refusing unsafe shrink from 39,683 to 17,901 after source
edits and 17,909 after the final test/docs edits. Retain 19,398 nodes from
2,972 excluded-but-existing files. Preserve version and
devcontainer.json zero-node warnings; no force, purge or install. Require
fresh post-commit log growth/Rebuilt tail and zero actual workers before
reporting clean. No OGL/Release, saves, editor or private inputs changed.

## Next

Recover complete 27-word func_15083DA0 in the same owner,
VA 0x15083DA0..0x15083E0C, ROM 0xB1250..0xB12BC.
Current no-argument stub returns zero. Original starts candidate identity 1,
caches unsigned count D_800D2100 and positive-count D_800D20FC record base,
uses 48-byte indexing and compares identity +0x28. A matching identity
increments the candidate and resets cursor to zero, but the common loop
increment means restart continues at index one, not index zero. Preserve that
retail quirk and final candidate >= 0x100 cap to 0xFF; do not replace with a
different idealized unused-ID algorithm. Qualify empty/max counts, duplicates,
restart/access order, widths, aliases and caller use before installing.
Broader timeline matching and real initializer/child/allocator/hardware/
renderer/gameplay acceptance remain open; keep the wider Game goal active.
