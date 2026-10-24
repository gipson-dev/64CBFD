# Object Attachment Direct C Match

Date: 2026-10-24. Consumer predecessor `56e49115`; tools predecessor
`7ed14440`. Qualification tools committed first as
`aece19851965664026f1989b38c055d28e36100e`. No push requested/performed.

## Recovered Routine

`func_1514EC1C`, `conker/src/game/generated_179F30.c`:
VA `0x1514EC1C..0x1514ECE0`, ROM `0x17C0CC..0x17C190`, exclusive ends.
The complete 196-byte / 49-word body emits directly from semantic C,
frame 32, six bindings, no instruction guards or compiler-profile changes.
The predecessor was a six-word / 24-byte typed zero-return stub, not the
usual three-word unprototyped stub. Preserve that measured size in the
strict image prediction rather than assuming twelve bytes.

Raw C SHA-256:
`44e8dc830eff2e49626b5cf0705cf3cf9e300d84107b162b97602a4eb60c7d14`.
Resolved/retail SHA-256:
`f8927328deb97be62d275a35aec1002d08dfbddab30c523d3bf31a247c2b5951`.

Recover the interface as `s32(s32 object, s32 ownerAddress, s16 key)`.
Keep the existing word-valued object/owner/return ABI, but correct the key
to signed short in both owner and external caller declarations. A word key
with repeated explicit short casts cached an extra converted value across
the helper call, producing 50 words/frame 40. The actual short parameter
restores the retail halfword reloads and 49 words/frame 32 without guards.
No volatile qualifier, artificial scheduling barrier or assembly substitute.

The function returns zero for a NULL object without dereferencing the owner
or key table. Otherwise allocate a node with
`func_1514EBA4(object, key, 0)`. On success:

1. Store the current owner+0x2F4 head into node+0x14 (`next`).
2. Publish the node as the owner's new head.
3. Reload the following pointer, clear node+0x18 (`prev`) and, if non-NULL,
   set the following node's previous pointer to this node.
4. Return the allocated node as a word.

On allocation failure, read signed callback entry one from the descriptor
selected by the signed key in `D_8008ABE8`. Callback -1 invokes
`func_1516972C(object)`; other valid entries index `D_8008AB58` and receive
the object word. Return zero regardless of the provider's return value.
Preserve late object/owner/key homes and exact overlapping-store behavior;
do not silently turn the failure path into a leak or unconditional release.

Bindings: node allocator JAL +0x24; descriptor HI16/LO16 +0x64/+0x74;
callback table HI16/LO16 +0x7C/+0x8C; base-release JAL +0xA4.

## Caller And Helper Boundaries

The full aligned retail scan finds 32 direct JAL sites and no literal
callback-pointer references. Six calls are outside the first owner/external
C-source search: `0x1506CDC8`, `0x1506CE4C`, `0x15073404`, `0x1509D2E8`,
`0x1519D618` and `0x1519E534`. Their original assembly remains untouched.
Validate all sites using their original argument-setup instructions and
delay-slot key, not a synthetic call ABI inferred from the newly recovered C.

Most argument windows are four words; `0x1519E534` needs five to include its
earlier owner load and byte spill. Seed boundary registers/homes from each
actual decoded setup instruction and stop before a nonexecuted return marker.
Run every site with NULL/non-NULL objects, node-allocation success/failure,
destructor/base-release paths and both stack phases: 512 phases. This is
argument-window qualification, not a claim to execute all complete parents.

`conker/src/game_16EE20.c` changes only the external declaration from a word
key to signed short. All 89 raw functions, owner pools and the entire padded
object remain byte-identical. The target owner's 77 other raw/padded
functions also remain identical, including the four pairs from Note 1691.

Retained `func_1514EBA4` (30 words) and `func_15167A68` (28 words) already
match their full original bytes. Execute both actual guest bodies together,
and compile their actual semantic C bodies into the native fixture. The node
request uses kind 0x24 and 32 allocated bytes; the node constructor clears
its links and stores the object/key. Check allocation failure and publication
through bounded heap/registration providers.

Natively execute all four actual C pair callbacks through the recovered
attachment helper, plus `func_15141E38`'s empty-list allocation path. The
external caller's search/create/memcpy services remain bounded. Its request
has three unspecified padding bytes; verify defined packet fields without
claiming those bytes are initialized. Keep memcpy an external, non-inlined
fixture boundary; do not edit the production caller or disable diagnostics
to invent initialized padding.

Base release and the three destructor services remain explicit bounded
providers. `func_1518D1C0` and unrelated parent placeholders are unchanged
and uncredited. This helper match is not full factory, heap, gameplay or
hardware acceptance.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation,
zero errors/failures/skips, no reused checks. Primary/mirror pre-install:
59.597s / 58.904s; installed: 61.800s / 62.095s. Both project tools checks
exit zero. Reuse the established MIPS, frame/fault, native32, relocation,
source-span and object parsers. A read-only equal-width return-type adapter
lets the existing primitive-type brace scanner extract the actual named
pointer-returning node constructor without rewriting its production source.

- 23,040 guest phases visit all 49 words, cover signed/full-word incoming
  keys, callback -1/0/1/2, NULL objects, helper mutations and four node/owner
  layouts. Include next/prev fields overlapping the head slot and late
  incoming-home changes. Independent expected stores/calls/return agree;
  original and raw C preserve complete state and events.
- Native32 O0/O2/O3 with trap UBSan: 528,768 selected cases per optimization
  and eleven effective defined wrong-C controls. Cover every short key on
  success/NULL paths, NULL ignored owners, valid physical key ranges on
  failure, all destructor entries, opaque bytes and trailing storage.
  Use allocated owner storage and complete node objects, not undersized
  declared headers. Keep native callers/helpers and lower-provider limits
  explicit. No portable native claim for negative array indices, malformed
  descriptors, guest-only overlaps or private argument-home aliases.
- All 32 original caller argument windows pass 512 phases; preserve the
  external caller's complete object and all owner neighbors.
- 288 connected node/allocator phases visit all 58 retained helper words,
  including allocation failure, late owner heads and descriptor changes.
- Nine independent GNU links cover original, qualified padded and actual
  Make objects at three placements, including relocation carry boundaries.
  192 rebase phases and 448 fired literal root-access prefixes preserve
  complete state, PC and delay origin. Nine strict-image corruption controls
  are rejected. No portable C fault-order guarantee is inferred.

The first broad test run exposed omitted assembly callers and the scanner's
named-return limitation; both were corrected before fresh passing suites.
The native external-copy fixture initially inlined its provider and diagnosed
unspecified padding. Restoring that real external boundary kept the actual
C body, strict warnings and UBSan intact. No source relaxation or historical
input rewrite bypassed qualification.

## Production And Preservation

Seal 15,934 initial native files, adding the two owned tools files in both
copies for 15,938 files / 30 focused inputs. Cover all 1,454 linker objects.
Verify all cache/native static inputs and non-target objects. Only the two
source files, target object and ELF receive audited manifest overrides; the
rebuilt external-caller object must equal its old bytes and needs no override.
Use checked native streams, not DrvFS project reads.

Actual shadow Make executes three target commands and five caller commands
with ordinary IDO `-O2 -g3`. Both complete padded objects match independent
qualification. Inherited compiler diagnostics remain unchanged; the isolated
helper has none. Production Make exits zero in 0.620s and reproduces both
the independently predicted whole image and qualified target object.

Exactly 147 ELF bytes change: 146 target-code bytes and one symbol-size byte
updating 24 to 196. No metadata reordering, exclusions, guard rows, inserted
instructions, folded words or compiler-profile changes. Preserve all other
6,054 bodies, all 6,055 addresses and protected Game data: 720 owners /
189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The entire historical guard CSV remains byte-identical.

After both fresh installed suites, verify all 15,938 native entries before
and after adopting the exact generated artifacts. Recapture the actual live
ELF and independently recount that stream, not a candidate or inferred +1.

Installed ELF SHA-256:
`c8a75e2be5524189c7301bfac58c08162a4b7bd46413c8aa0a5e60ee4133557f`.
Installed target object SHA-256:
`8507cfd0f985a5105dc106163af4c8dd5e27065e9888c0488e7ef1702e6c340c`.

Preserve all 1,596 pre-existing older-mirror dirty paths, statuses, hashes
and HEAD. Add only the two owned tools files there, leaving 1,598 dirty paths;
do not reset or commit that independent mirror. Host Release, saves,
configuration, private ROM, providers and dependencies are untouched.

## Measured Progress And Resume

| Section | Byte-exact C functions | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,768 / 5,505 (68.45%) | 0 | 1,737 |
| Game | 3,095 / 4,832 (64.05%) | 0 | 1,737 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove only `func_1514EC1C` from the live-ELF-pinned queue. It was classified
as semantic/other because its old placeholder already had typed parameters;
do not falsely decrement the simple no-argument placeholder count. Remaining
source screens: 1,607 placeholders, 121 semantic/other, nine unlocated.
These are source-shape screens, not qualification. `func_1510D8C0` is existing
`Gfx *` C missed by the simple parser; its private screen and
`func_1518C850` remain unmatched/uncredited. Keep `func_1508CAD8` separate.

The 75% target is still 4,129 exact C functions: 361 more, goal not complete.
Root README changes only its two aggregate matching rows. Retain normal
post-commit Graphify receipts and audit all changed-file hashes/membership
and old-node retention, without a reduced-corpus extraction or forged stamp.

Ignored evidence: `conker/build/game-object-attachment/qualified/`.
Tools: `tools/experiments/game_object_attachment.py` and
`tools/tests/test_game_object_attachment.py`.
