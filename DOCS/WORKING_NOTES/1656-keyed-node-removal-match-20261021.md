# Keyed Node Removal Direct C Match

Date: 2026-10-21

## Result

Restore `func_15188AD0` in `conker/src/game/generated_1B5CC0.c` as
complete, purpose-commented C. Normal O2/g3 emits all **41 body words,
frame48 and four bindings** directly. No guard, raw emitter, profile change,
shared-header edit or alignment filler is needed. Keep `conker/asm/1B5CC0.s`.

VA15188AD0..15188B74 / ROM1B5F80..1B6024, ends exclusive.
Unlinked C/GNU-original body SHA-256:
`921eb15610ac00e64b12396a6eb60c292f9a24a71185cca523a747e088f97ed2`.

## Recovered Contract

Use `void func_15188AD0(s32 key)`. Capture the first head at
`D_800DF7C8` and traverse +0x0C successor links. Compare full 32-bit keys
at +0x10. Cache the successor before either helper. For every matching node,
rewrite the global head or last unmatched predecessor's link first, then
load its +8 payload pointer, mark that block with flag 2 through
`func_100043B4`, and free the removed node through `func_10004074`.

Do not advance the predecessor when removing a node. This preserves leading,
adjacent, interior and final matches. Do not reload the head or successor
after helper effects. Preserve low 24 payload-header bits when flagging; the
first helper marks the payload block, it does not immediately free it.
The second helper frees the node itself.

The local `KeyedNode15188AD0` view has eight opaque prefix bytes, payload
pointer +8, next pointer +0x0C and key +0x10. The adjacent constructor
`func_1518894C` statically corroborates a 0x14-byte node allocation and
these offsets; it remains a placeholder and gains no matching credit.
Byte-pointer/typed and while/do-while forms all emit the same complete body.
Choose the ordinary typed while-loop; historical type spelling is not unique.

The original routine does not materialize a return word. Both direct callers
discard its incidental V0. Preserve that register in full machine comparisons
without inventing a semantic zero return. The key can carry an actor-address
word; do not narrow it to a byte, halfword or table index.

Bindings relative to the body:

| Offset | Kind | Symbol |
| --- | --- | --- |
| 0x08 / 0x14 | HI16 / LO16 | `D_800DF7C8` |
| 0x60 | R_MIPS_26 | `func_100043B4` |
| 0x68 | R_MIPS_26 | `func_10004074` |

Add owner-local declarations matching the actual Init helper definitions.
The typed marker declaration initially exposed two integer-word argument
warnings in `func_151895A4` and `func_151895CC`. Recover their +8 loads as
`s32 *` pointers. Both neighboring bodies and their bindings stay unchanged;
before/after owner diagnostics are identical and empty. This avoids adding
warnings, not removal of pre-existing compiler warnings.

## Caller And Helper Bounds

There are two direct original call sites:

- In `func_15029BB8`, execute the original 17-word window at
  1502A7B4..1502A7F8 and five-word epilogue at 1502A88C..1502A8A0.
  It loads the word key, skips NULL/disabled selections, and calls the target
  otherwise. Its result is replaced by 1. These are bounded paths of the
  826-word/frame208 parent, not full-parent coverage.
- In `func_15060F28`, execute the original 14-word tail at
  150611B0..150611E8, passing the actor-address key. Then reload actor+0x31C,
  conditionally free that pointer, call `func_1505F188(actor)` and return.
  This is a window of the 176-word/frame32 parent, not full-parent coverage.

Sixteen caller-window phases cover both sites, key/gate choices, optional
follow-up free and both SP phases. Use explicit outer-frame offsets while
retaining the reused oracle's supported 0/8 phases. Both current C parents
remain stubs. No complete current-parent execution is claimed.

Both Init helpers are already exact in the current linked image:
`func_100043B4`, 22 words at ROM43B4, and `func_10004074`, 119 words
at ROM4074. Connect those actual instructions for 12 controlled phases,
executing all 22 marker words and 50 free-routine words on the single-block,
empty-free-list path. Check payload tag 2, preserved low bits, node header,
free-list head/tail, largest-block pointer/size and restored interrupt mask.

Only `osSetIntMask` is an opaque provider in this connected chain. No CP0,
hardware interrupt, full 119-word allocator-path, natural registration or
gameplay acceptance is claimed. Hostile target-suite free providers poison
mapped node objects; those are bounded writes, not portable use-after-free
or actual native deallocation.

## Qualification

Tools: `experiments/game_keyed_node_removal.py` and
`tests/test_game_keyed_node_removal.py`, identical in both local copies.

| Final Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 99.213s | 8 tests, 104.985s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 8.035s | 2 tests, 6.740s | 0 / 0 / 0 |

Reuse the other six checks per copy only under unchanged source, raw/padded
object, helper, input and full-image identity. They are not fresh installed
executions. Shared project-tool checks also pass in both copies.

- 5,080 guest phases cover every match pattern through six nodes, four
  full-word key patterns, five helper-effect plans and two SP phases.
  Preserve cached successors, late payload reads, predecessor lifetime,
  unlink order, saved registers and volatile/argument-home clobbers.
- All 41 static words match; 39 execute. Duplicated words at 15188B2C and
  15188B48 are unreachable. Do not claim all-41-word dynamic coverage.
- Another 360 guest phases cover shared payloads and header aliases against
  the head/current link. These machine fixtures are not portable native C.
- 2,540 typed native32 cases per optimization at O0/O2/O3 use trap UBSan,
  real node/payload objects, normalized pointers, complete memory/fences and
  callback packets. All eight compiled wrong-C controls are effective.
- Six independent GNU links / 54 phases exercise all four bindings and
  signed-low carries. There are 364 fired root-access fault prefixes,
  excluding provider accesses, and eight strict-image corruption controls.
- Pin 27 historical/current inputs and the predecessor object. Preserve all
  14 owner neighbors, pools, diagnostics, guard bytes and addresses. The
  actual Make shadow executes three productive commands with normal O2/g3.

The first whole-owner gate rejected the two newly exposed marker argument
warnings; recover the pointer loads before qualifying. An initial fixture
also placed a payload header over the model's saved return address and
passed unsupported negative SP phases to the shared oracle. Separate the
payload region, assert its stack disjointness, and model outer frames
explicitly. The matching C body is unchanged. Rerun both complete suites;
the table records the final successful runs, not the failed attempts.

## Production And Preservation

Seal 15,794 live/copy files, including every one of the 1,454 linker objects.
Rebase only the previously committed six-byte routine's source/object/ELF
delta using its strict adoption proof, then add four new task-file copies.
The existing Linux cache remains valid; no dependency/provider changes.

Actual production Make exits zero in 3.553s. It reproduces the independent
whole-image prediction exactly: **122 changed bytes = 121 instruction bytes
+ one symbol-size byte**, zero metadata exclusions/permutations. The only
build warnings are the inherited duplicate Make recipe.

Installed ELF SHA-256:
`2389af8542638298d4a2e4e98adcc44939772f2c3a18ad2146b6b71e01b8b6de`.
Installed owner object SHA-256:
`ea5cb2e7d016c1bdde0d50af38e5a787d0ee4dc3229d7dc38c9167a44e252ae4`.

All other 6,055 bodies and all 6,056 addresses remain fixed. Protected Game
data is exact: 189,088 bytes / 720 owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Recheck all sealed live files before/after adopting only the owner object,
ELF, generated linker script and progress CSV.

Tools commit `d86b5c2de2d96134fb202823fc46cbbd72afd529` precedes the
consumer source/docs/pin commit. Preserve all 1,524 pre-existing older-mirror
dirty statuses and hashes; add only two task files, totaling 1,526 paths.
Do not commit/reset/stash/clean that mirror. No push, host build/launch/change,
shared-header/profile edit or Claude call. Host Release remains frozen.
Root README changes only two aggregate rows. Refresh Graphify and explicitly
audit retained/relocated old nodes and excluded-existing files at checkpoint.

## Measured Progress And Resume

The standard matcher exits zero against the adopted live consumer ELF:

| Section | Byte-Exact Converted C | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,724 / 5,505 (67.65%) | 0 | 1,781 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,051 / 4,832 (63.14%) | 0 | 1,781 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The threshold remains 4,129; **405 more exact functions** are required.
The wider 75% goal is unfinished. The refreshed ELF-pinned queue has 1,648
placeholders, 124 semantic/other definitions and nine unlocated entries.

Next: `func_15189FF0`, 41 body words/frame56 in
`conker/src/game/generated_1B74A0.c`, reference `conker/asm/1B74A0.s`.
VA15189FF0..1518A094 / ROM1B74A0..1B7544, ends exclusive. Static inspection
shows a source-record+0x58 byte store of 0x0B, a ten-argument factory call using
a 0x80-byte source-copy size and byte arguments, a NULL gate, then a 32-byte copy to the
returned object+0x170. Preserve the allocation result across memcpy and
determine the actual caller/return ABI, argument homes, widths and factory
contract before drafting/installing. No matching credit or source change
is claimed for it.

Private receipts, snapshots, probes, native/guest fixtures, Make shadows,
images, queue and preservation audits live under
`conker/build/game-keyed-node-removal/qualified/`. No ROM, generated
fixture or build artifact is committed.
