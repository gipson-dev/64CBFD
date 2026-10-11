# Game Descriptor Resource Loader Direct Match

Date: 2026-10-11. Complete func_1503D660, VA 0x1503D660..0x1503D774,
ROM 0x6AB10..0x6AC24, 69 words / 276 bytes. Owner:
conker/src/game/generated_6A3D0.c. All 69 words emit directly from semantic
C under both existing profiles. No new guards, profile or Makefile changes.
The wider Game goal remains active.

## Baseline And Contract

Consumer 22ea2b740155bd626cb69c817461266cf80f6701, mounted tools
1310ff74cb9bfdda580c23e04cc0a29d4ebdf235. Both active checkouts were clean.
[Note 1269](1269-game-vertex-coordinate-copy-guarded-match-20261011.md)
banked the guarded vertex-coordinate copy. This descriptor loader remained
a zero-return placeholder and a bounded fourth-status hook in the parent
chain. Native Graphify query and the complete retail body identify the
direct caller func_1503CF20, which joins this routine's status.

Recover the s32 (s32 identity, s32 unused) interface. An existing non-NULL
D_800D1588[identity] publication returns zero without helper calls.
Otherwise cache the slot across func_1503D5F0(identity) and
func_1502B5C8(&size, 2, 15, remapped identity). The actual request helper has
a void * (s32 *optionalSize, u32 depth, ...) interface: its returned V0
pointer is the descriptor; the private size output is not used.

A NULL return publishes NULL, clears the original identity's halfword
D_800C5A90 entry, calls func_1503D510(identity), and returns four.
Success publishes the returned pointer before relocating the three header
words. Preserve the first word's double-read and the live slot reloads.
A nonzero first word becomes descriptor-relative, then calls
func_1503D45C(first word, descriptor + 0x10). Nonzero header words +4/+8
are each relocated against the current descriptor. Reload the public slot
after callbacks and stores rather than caching a stale descriptor view.

Publish current descriptor + 0x10 before func_1503D484(records, original
identity), then call func_1503D510(identity) and return zero. There is no
new identity bound, NULL-base gate, resource-size interpretation or helper
return-status check. The second incoming word is ignored; reusing that
argument variable for the returned 32-bit address recovers the original
compiler lifetimes without an extra local. The comment makes this explicit.
The 32-bit address casts are the guest ABI, not portable 64-bit host code.

## Direct Shape And Diagnostics

Original 0x38 frame, S0 spill +0x18, RA spill +0x1C, incoming A1 home
+0x3C, private size output +0x34 and cached slot spill +0x28 all match.
The qualified owner -O2 -g3 -Wo,-loopunroll,0 and alternate -O2 -g3
bodies match all 69 words, including branches and delay slots.

The full sweep measures 62 source/profile forms: the canonical body plus
30 diagnostics under two profiles. Eight measurements are directly exact:
canonical, incoming-word reuse, word-expression reuse and pointer reuse
under both profiles. Some bodies repeat; this is not 62 unique bodies or
a full behavioral qualification of every form. Zero diagnostics/data pools.
Initial separate-local shapes emit 70 words with 51/52 differences; live
slot shapes restore 69 words but retain seven/eight layout differences.
Incoming argument reuse closes the original private layout and scheduling.
Only the clean canonical word-reuse body is installed.

Keep the existing mixed-profile owner recipe and its func_1503D804 selector
unchanged. This new function uses the ordinary no-unroll object directly.
Both actual padders preserve all 14 neighbors, extents, relocations, pools
and the typed parent's instructions. No core padder changes or new guards.

## Qualification

New tools: experiments/game_descriptor_resource_loader_candidates.py and
tests/test_game_descriptor_resource_loader_match.py. Reuse the existing
compiler, MIPS oracle, native32, owner/pool/relocation and padding helpers.
Receipts live under ignored conker/build/game-descriptor-resource-loader-match-test/.

- Twelve final pre-install tests pass in 51.186 seconds. Complete original,
  raw C and actual padded streams are identical across all 69 words.
- The identity/present/failure/field/unused-word/stack-phase matrix passes
  1,408 cases / three forms and reaches all 69 words. Invalid identities
  and wrapped addresses use mapped guest fixtures, not portable C bounds.
- All 130 callback/alias cases pass, including remap/request/first/count/
  finish mutation, publication aliases with each header word, full-word
  wrap, and private size outputs 0/1/INT_MIN/FFFFFFFF. Deeper opaque-helper
  pointer validity is not claimed for these focused alias cases.
- Nine independent links pass 288 cases with two global HI16/LO16 carries,
  all five helper JAL rebases, original identity, unused A1 and stack phases.
- All 83 original/raw/padded memory-access fault triples fire and preserve
  full partial memory, events, calls and registers, including private stack.
  These are guest-model fault-prefix results, not hardware acceptance.
- Eight freshly compiled semantic mutations fail effectively; three stale
  install attempts reject. Source/prototype/two-declaration/newline changes
  and linked word/extent corruptions also reject before historical projection.
  An unrelated ELF byte remains visible through the projection.
- Complete before/after no-unroll and unrolled owners compile without
  diagnostics. Both real padders retain only the prior D804 selector and
  preserve every other function, relocation and pool.
- Native32 O2/O0 each pass 77,824 cases: all 65,536 low-halfword header
  payloads plus 12,288 valid fixture identity/presence/failure/callback/
  ignored-word cases. Full arrays, 256 slots, counts, callback traces,
  return status and size independence agree with an independent reference.
  A changed failure status fails effectively. Existing no-strict-aliasing
  policy applies; no real 187-entry bounds or portable 64-bit acceptance.
- The actual 69/28/61/10/35/9-word descriptor/remapper/request/first-list/
  counter/tagged-relocator chain passes 3,840 cases / three forms and reaches
  all 69 target words. The first-list helper is 10 words, not nine. Its
  emitted load-ahead order is retained; the tagged leaf uses mask 0x0F000000.
  Five byte-count groups, the depth-two variadic request and sentinel-999
  record count run as actual linked instructions.
- The actual 13-body 104/274/52/46/96/69/28/61/10/35/56/9/194-word outer/
  main/command/counter/pair/descriptor/remapper/request/first/count/extras/
  relocator/buffer chain passes 1,920 cases / 3,840 executions and reaches
  all 69 descriptor words. The former fourth flag now drives the actual
  resource-request NULL / return-four path. Nested legacy receipt counts
  are not reused for this extended matrix.

The first full pre-install run passed its behavior comparisons but reached
only 57 descriptor words in the inherited chain fixture. Extend that
fixture's exact failure axis with fourth, and vary descriptor cached/zero
headers; preserve/restore the scoped fields and use actual pair words when
reusing its chain test. The corrected fixture reaches all 69. This was a
coverage-fixture issue, not a production defect.

The final installed/regression run passes all 73 tests in 364.675 seconds:
twelve descriptor, twelve pair, eleven counter, eleven command, fifteen
guarded parent, ten earlier shape/audit checks and two historical status-join
checks. No skips, errors or failures. Historical complete candidate shapes
are recompiled, not their entire old behavioral matrices. Unchanged prior
semantic receipts remain prior evidence.

## Immutable Historical Audits

Only the exact canonical descriptor body, typed forward and two added
declarations may reverse to the frozen pair-stage source SHA-256
c5e63d79936dc66521f8cd1bc284c0f09c854e8a33889994d1876c076fb0450b.
Before ELF projection, require all 69 current linked words to equal retail
and extent 276. Reverse only that complete slot and extent onto the trusted
historical ELF, keeping every other current byte visible.

The existing pair/counter/command projections then serve older parent
audits. The pair-stage receipt explicitly labels its successor-projected
ELF view. Frozen source/ELF/guard inputs, historical candidates and negative
controls are not refreshed. The new suite audits the literal installation.
The parent still needs its prior 22 guards; the pair still needs four.
This direct child does not eliminate those separate guard gates.

## Actual Delta And Progress

Installed source SHA-256:
491ba6e43604e7d8ce7dd9b0f60fd860eefa60bb8274e7b9c259448a2b50a526.
Installed ELF SHA-256:
08eef58ac95303c6e5dd3169a2daad0725d654bc767a16e5538b8ea8d222a973.

Exactly 197 ELF bytes change: 195 target-slot bytes and two extent bytes,
12 -> 276. Every other ELF byte, metadata byte, symbol name/value/extent,
protected data byte and conversion/assignment input remains identical.
All 189,088 protected data bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Guards remain byte-identical, SHA-256
92679ed3e2a6439969298cd769daf69d41e9619c81360046094cf34f1ec3faf4.
Makefile remains byte-identical, SHA-256
8493bae49a7d02eac15064df9acd84044095a21ecdd877b11f12b04375943abc.
Conversion CSV remains byte-identical, SHA-256
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.

Required ELF/progress rebuild exits zero. The existing duplicate
generated_12D630 recipe warning remains; no new owner diagnostics.
Fresh make -C conker match-progress NON_MATCHING=1 exits zero:

| Section | Byte-Exact | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,467 / 5,495 (63.09%) | 0 | 2,028 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,794 / 4,822 (57.94%) | 0 | 2,028 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

One matching credit only. Conversion/converted-byte metrics stay fixed.
Root README changes only the two affected aggregate matching rows.

## Ownership And Next Work

Single Codex writer, zero Claude calls. Mounted tools
9359eb3ff803b349390408607ea66af6bd22b61c is committed first; the consumer pins
that checkpoint with the source, note and concise indexes. No push.
Consumer/mounted/older WSL tools checks and native py_compile pass.
Only the two finalized absent paths are copied to the older sibling.
Its HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 31 protected
existing fingerprints remain unchanged; dirty entries 308 -> 310 are only
those two new copies. Existing older audit paths are not overwritten,
committed or reset. These copies are not a new older-checkout function-suite
qualification claim.

Native Graphify update exits one after refusing shrink 39,849 -> 18,068
nodes and retaining 19,398 nodes from 2,972 still-existing excluded files.
Known skill/package-version and devcontainer zero-node warnings remain.
No force, purge or install. Refresh terminates with zero actual native
Python/Graphify workers. Before reporting the consumer commit settled,
verify fresh post-commit log length/UTC, an authoritative fresh completion
record and zero actual workers; launch receipts alone are insufficient.

Next complete connected recovery: func_1503D510, VA
0x1503D510..0x1503D5F0, ROM 0x6A9C0..0x6AAA0, 56 words / 224 bytes,
same owner, still a zero-return placeholder. The full retail leaf scans
five byte-count groups, finds the first group containing the original
identity, then propagates that identity's live descriptor pointer and
halfword count across each group member. Recover its ignored return
contract, byte-member re-reads, live pointer/count sources, original loops
and branch delays before replacing the remaining finish hook.

The third-loader helper, deeper lookup/block loader, unrecovered finish
helper, real allocation/heap/hardware/renderer/gameplay and portable
64-bit host acceptance remain open. No OGL/Release/save/editor/private
input changes; Release stays frozen. The wider Game goal remains active.
