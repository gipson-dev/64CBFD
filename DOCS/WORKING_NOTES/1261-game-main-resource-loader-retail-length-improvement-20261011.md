# Game Main Resource Loader Retail-Length Improvement

Date: 2026-10-11. Continue the same complete func_1503CF20 from
[Note 1260](1260-game-main-resource-loader-recovery-20261011.md) under
[the agent workflow](../AGENT_WORKFLOW.md). The previous goal turn made
verified progress by banking the semantic recovery. Single Codex writer,
zero Claude calls. Full Game matching remains active. Commit authorized
checkpoints tools-first; no push.

## Scope And Immutable Checkpoints

- Full VA 0x1503CF20..0x1503D368, ROM 0x6A3D0..0x6A818:
  274 retail words / 1,096 bytes, original frame 0x78.
- Owner conker/src/game/generated_6A3D0.c, complete asm/6A3D0.s routine.
- Consumer entry HEAD 36f275ea57cfbe0fdd93a43b31d3fe28800abcb2, clean.
- Mounted tools entry HEAD b50347469279bab389e3f67a56f2260b3e99b548, clean.
- Older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a,
  289 independently dirty entries. Preserve its existing work and history.
- Banked source SHA-256:
  be9b10d5893d895bd5c70ec40e7fdad8b92d43bd9fd5988cfa122b39cc2ff863.
- Banked ELF SHA-256:
  61eb09430a85aed3fc5fa0229ba87c9bbf749876c396e7f1cd0fe4b277f3be39.

Freeze that complete recovery in ignored
conker/build/game-main-resource-loader-lifetimes-test/checkpoint.json and
checkpoint-* files before installation. Also hash-check and retain the
original Note 1260 stub-era baseline without refreshing it. The older suite
now accepts this specific qualified successor and audits its whole ELF
against that original baseline; it does not silently accept arbitrary C.

## Installed Full-Body Improvement

Recover distinct cursors in both relocation loops: the relocation call
receives &(*table)[index], while the child call uses the separately advanced
byte offset. Retail likewise emits an indexed shift in each loop plus its
four-byte cursor. Preserve the post-callback live primary count and the
cached unsigned secondary count, including every base reload.

Remove the short-lived first-table pointer and use the correctly typed
D_800C4020 accesses directly. Reuse the ignored second parameter as the
status value only after explicitly resetting it to zero where status becomes
live. This does not accept an incoming error/status: early-return paths
ignore that word, and both extras gates start from the same zero status.
The five-word O32 interface and all existing caller bodies remain unchanged.
Keep the u8 **cleanupSlot accesses; no pointer-table type punning is installed.

| Full C Body | Emitted Words | Frame | Raw Word Differences |
| --- | ---: | ---: | ---: |
| Note 1260 recovery | 272 | 0x88 | 273 |
| Mixed cursors only, late status | 274 | 0x88 | 271 |
| Selected direct first-table accesses and ignored-word scratch reuse | 274 | 0x80 | 271 |
| Retail | 274 | 0x78 | 0 |

All 274 words now come from complete semantic C, with no padding tail, word
guards, opaque instruction body, compiler-profile, layout or symbol edits.
The frame shrinks eight bytes, but remains eight bytes larger than retail.
This is not a byte match and earns no matching or conversion credit.

The candidate module records early/late status, cursor, initial-count,
declaration/storage, loop-gate, header representation and cleanup-lifetime
experiments. These other forms are uninstalled measurements, not semantic
qualification claims. Early status plus mixed cursors still spills status
and emits 287 words. Reusing cleanup pointer storage could shrink a frame,
but that cast form is rejected for installation. Explicit initial-count
temporaries and header types do not solve retail allocation. Nine locally
evidenced allocator controls were tried on both early/late complete bodies;
none recovered the required layout. O2/no-debug and O1 probes likewise do
not justify changing the existing O2/g3/no-unroll owner profile.

One shape assertion caught that removing only the first-table pointer was
still frame 0x88; it was not installed as a claimed frame-0x80 result. The
selected ignored-word lifetime was compiled and fully requalified instead.
A first linked test started while the linker was still writing its ELF;
that incomplete artifact failed its metadata assertion. Wait for the build
to finish, then rerun qualification serially. No gate or immutable baseline
was weakened to make either failure pass.

## Fresh Qualification

Ten pre-install tests pass in 33.674s. After adding explicit current-word
coverage, incoming-word cases and a compiled status-initialization control,
the final eleven-test installed suite passes in 23.466s. The original ten-test
recovery suite also passes fresh in 25.281s against the installed successor.
These are fresh runs, not reused unchanged whole-suite receipts.

- 1,021 cases / 2,042 original/current guest executions compare every public
  memory byte, access event, helper call and error against an independent
  reference. Reach all 273 reachable retail words and all 273 reachable
  current words. Each body has one statically unreachable duplicated SLTI:
  retail VA 0x1503CF68, current VA 0x1503CF64. Do not claim all 274 dynamically
  reached. Both unreachable words remain present in their complete bodies.
- Thirty mutation cases preserve live primary growth/shrink, primary and
  secondary base rebindings, cached secondary counts, event-count changes
  and callback-driven optional cleanup/main-pointer replacement.
- 175 width/size/alias cases preserve signed/wrapping identity gates,
  config/flags/extras, unsigned division/shifts/u16 truncation and cross-table
  publication aliases. High counts shrink via callbacks, not 65,535 loops.
- Nine actual original/current/padded links, three symbol sets and 24 rebase
  cases include signed-LO carry. Both real owner padding routes pass.
- 1,800 fired public-access fault pairs compare complete public partial
  memory/access/call prefixes. Different private-frame faults remain outside
  this comparison; this is emitted guest order, not portable C fault behavior.
- Ten existing effective freshly compiled semantic controls plus a new
  missing-status-reset control. The latter must reject propagation of an
  incoming 0x80000000 second word when extras is zero. Three stale installation
  guards also fire. No missing-free or clear-before-free control is disabled.
- Actual complete native32 C: 6,048 cases at each O2/O0, 12,096 total, all
  modeled memory bytes and normalized call traces compared to an independent
  reference. Missing-main-free control still fails. Valid native identities
  only; wrapping guest indices are not portable C array-domain guarantees.
- All 14 owner neighbors, extents, relocation fingerprints and data pools
  remain exact; isolated/owner target fingerprints agree, zero diagnostics.
- 768 connected cases / 1,536 runs through actual parent/main/extras/
  relocator/buffer code. Mapped words 104/274/56/9/194; retail-path reached
  counts 41/256/56/9/140. All public memory/access/calls/failure results compare
  with independent references within the same deeper-helper bounds.
- 96 additional incoming-word/early-return/extras-gate cases / 192 runs
  explicitly qualify scratch reuse for negative, valid and rejected identities,
  existing entries and high-bit/all-ones ignored words.

Only the private request-output pointer is normalized between layouts.
Request/child/auxiliary/cleanup/allocator/copy/free internals remain bounded.
No full heap, hardware, rendering, live gameplay or 64-bit host acceptance.
Prior deeper caller/extras/buffer whole-suite receipts remain prior evidence;
their unchanged code/guards plus fresh connected tests qualify this change.

## Linked Audit And Progress

From the committed complete recovery, exactly 566 ELF bytes change: 565
inside this target slot and one symbol-size byte, extent 1,088 -> 1,096.
The metadata receipt's one byte is that same extent byte, not an extra change.
ELF length remains 3,261,160; every other ELF byte/name/value/header/section
and every other function/address/extent are exact.

- Installed ELF SHA-256:
  2129eb586ceac58a8201542a83a62601853a16d8589f49596fdeb137fb02fcaf.
- Installed source SHA-256:
  25fd41ff70c4fb4db5c7649c74c27fbd4d72ed10831f95ffcb1abdaf75f18a52.
- All 189,088 protected data bytes / 720 owners exact; SHA-256 unchanged:
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
- Guard SHA-256 remains
  5eace9a1e712613397671e3d8d61acfcbd1ceaa4a7a73d4377b15d97ff7400c6.
- Conversion CSV remains
  32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
- Rodata source, tracked symbols/layout and ignored auto assignments exact.

Fresh matcher: Game 2,789/4,822 (57.84%), total 3,462/5,495 (63.00%),
Init 492/492 and Debugger 181/181, zero drift / 2,033 different. No credit.
Root README aggregate rows remain correct and unchanged; detailed function
updates stay here. Build plus consumer/mounted/older WSL tools checks and
native new-file py_compile pass. Preserve the existing duplicate
generated_12D630 recipe warning; no warning-free build/native full-check claim.

## Ownership And Graph Gate

Tools e06635c banks the new experiment/qualification files and the specific
legacy audit update before the consumer pin. Copy only the two absent new
paths into the older standalone sibling. All twelve protected older hashes
and its HEAD remain unchanged; dirty entries 289 -> 291. Do not overwrite its
existing legacy test, commit/reset its independent history or push either repo.

Native Graphify query succeeds with 20 nodes. Native update re-extracts two
files but refuses unsafe shrink 39,762 -> 17,980, retaining 19,398 nodes from
2,972 existing excluded files. Preserve version/devcontainer warnings; no
force/purge/install. Before close-out, wait for the consumer commit's detached
hook using fresh log bytes/UTC, fresh Rebuilt tail and zero actual workers.
No OGL/Release/save/editor/private-input changes; Release stays frozen.

## Next, Same Complete Function

1. Recover the original 0x78 frame and S6 status lifetime. Current saves
   S0..S5 at +0x1C..+0x30, RA +0x34, and uses S4 for late status. Retail saves
   S0..S6 at +0x20..+0x38, RA +0x3C, and keeps zero status in S6 from the
   opening presence gate. Early initialization alone still spills; the
   compiler's cost decision is not yet causally explained.
2. Recover private request output +0x6C versus current +0x7C, main-slot/
   word-offset spills +0x58/+0x5C versus current +0x48/+0x4C, half-index spill
   +0x4C versus +0x3C, and boundary/cached-bound scratch +0x68 versus +0x5C.
3. Preserve the recovered mixed cursors, full live/cached count behavior,
   every publication/cleanup alias, ABI, delay joins and all failure paths
   while restoring retail scheduling. Do not switch to an easier neighbor
   or mask 271 broad layout/schedule differences with instruction rows.
4. Requalify the full current body, both padders, connected caller and whole
   linked ELF before claiming a match. Deeper helper/runtime work remains
   separate; this checkpoint does not complete the full Game objective.
