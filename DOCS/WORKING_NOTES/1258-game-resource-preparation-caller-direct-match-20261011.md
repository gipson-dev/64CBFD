# Game Resource Preparation Caller Direct Match

Date: 2026-10-11. Continue
[Note 1257](1257-game-resource-buffer-preparation-guarded-match-20261011.md)
under [the agent workflow](../AGENT_WORKFLOW.md). The previous turn banked
verified progress. Single Codex writer, zero Claude calls. Keep the full
Game matching goal active, commit authorized checkpoints tools-first, no push.

## Scope And Baselines

- Complete func_1503DA9C: VA 0x1503DA9C..0x1503DC3C, ROM 0x6AF4C..0x6B0EC.
- Retail 104 words / 416 bytes, frame 0x48, owner generated_6A3D0.c.
- Consumer entry HEAD a1e73d029761a1e9f29ec08f0f69b56d5448b487, clean.
- Mounted tools entry HEAD 8e07c9e4e9a6fe305f31e26258fd3253639a8a8a, clean.
- Older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a,
  283 dirty entries; preserve all existing work.
- Original C is a 12-byte zero-return stub. Do not substitute its callee,
  only the earlier 60 reached caller words, or an easier neighboring routine.
- Baseline ELF SHA-256
  5b1d021e64d52f5aec54232e046d41b8024c7310729aa386ac2df5fe0dc49979.
- Freeze before-source/ELF/guard/progress/rodata/symbol/layout/auto-assignment
  bytes and their hashes in ignored game-resource-preparation-test output.
  The original baseline manifest is immutable; never refresh it after install.

Inspect complete retail assembly, full live C, actual no-unroll owner profile
and all four direct retail call sites at 0x1502CDC0, 0x15082FF4, 0x15186AC8
and 0x15189658. They confirm actor/identity/channel/extras word forwarding.
The already recovered generated_58F80.c caller also declares this four-word
interface and checks the returned failure. No caller ABI edit is needed.

## Complete Recovery

Recover the main resource table read and unconditional actor +0x144 config
load. Emitted C preserves retail's global-read-before-config branch delay.
An absent main resource invokes func_1503CF20(identity,0,config,extras,
actor[0xAC]); the byte is unsigned and promoted to a full fifth argument.
This path skips the auxiliary and extras gates.

On the already-present path, config +0x18 bit 0x4000 short-circuits the
fallback actor +0xAC bit one read. A missing D_800C5C08 cache then invokes
func_150028BC. Keep its return ignored and table-index lifetime intact.
Nonzero extras and unsigned D_800C5628 count gate the descriptor read.
Compare its first word unsigned against 0x10000000 before func_1503DC3C.

After the extras loader, even a nonzero failure result does not skip the
entry loop. Reload unsigned D_800C4778 count after each callback and the
live D_800C4488 list base before every next entry. Dispatch five arguments
(entry,0,0,0x3E,0) to func_1510CE60 and ignore its return. Call the now-matched
func_15084044 only if the loading result is zero, preserving actor/channel
and propagating its result unchanged.

## Direct Compiler Evidence

Use the existing retail owner profile: -O2 -g3 -Wo,-loopunroll,0.
No Makefile/profile edits, guards, assembly substitution or opaque ROM body.

| Complete Body | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Explicit count/list pointers and byte cursor | 104 | 0x50 | 52 |
| Indexed list under the explicit loop gate | 104 | 0x50 | 51 |
| Natural indexed loop, named main resource | 104 | 0x48 | 49 |
| Natural loop, inline main table | 104 | 0x40 | 12 |
| Natural loop, named descriptor pointer | 104 | 0x48 | 29 |
| Natural loop, named descriptor word | 104 | 0x48 | 26 |
| Natural loop, shared word-table byte offset | 104 | 0x48 | 9 |
| Shared offset, recovered local ordering | 104 | 0x48 | 0 |

All 24 four-local declaration permutations retain 104 words/frame 0x48;
six emit directly byte-exact. Select config/index/result/tableOffset order.
The shared four-byte table offset is genuinely used for main/auxiliary/
descriptor/list accesses; it is not inert stack padding. Retain its O32
layout, live index spill +0x34 and result +0x3C. There are no normalization
rows for this function and the complete guard file is unchanged.

## Fresh Qualification

Ten pre-install tests pass in 26.342s after fixture corrections; ten final
post-install tests pass in 35.842s.

- 4,608 independent-reference core cases / 9,216 original/raw runs; all
  104 retail words reached, complete public memory, access order and calls.
- 1,114 word-ABI/count/mutation cases / 2,228 runs: high word bits, unsigned
  halfword boundaries, live growth/shrink/list rebasing, auxiliary mutations.
- Unmapped short-circuit inputs and three actual cross-role aliases pass.
- Nine independent original/raw/padded links across three symbol sets;
  48 rebase cases preserve signed-LO carry and the complete direct match.
- 3,200 all-access fault pairs; every gate fired, full partial memory,
  accesses and helper-call prefixes equal. Guest faults do not define C faults.
- Ten effective freshly compiled IDO controls cover loader extras/unsigned
  byte, auxiliary mask, unsigned threshold, command/fifth arg, error/channel
  propagation, and stale count/list snapshots under callback mutations.
- Actual complete native32 C: 18,432 cases at each O2/O0, 36,864 total;
  independent callback/result trace and every modeled memory byte compared,
  not just a checksum. An effective wrong-command control fails.
- Copied before/after owner uses the real no-unroll compiler profile: all
  14 neighbors preserve bytes/extents/relocations/pools, no diagnostics.
  Isolated and complete-owner target fingerprints are identical. Both actual
  layout/generated padders preserve every non-target owner byte/relocation.
- 4,608 connected cases / 9,216 runs through the actual matched 194-word
  func_15084044. Reach all 104 caller words and 140 callee words; qualify
  loader/extras failures, threshold/count gates and first/second allocation
  failures against independent outer and buffer references. Do not claim all
  194 callee words dynamically covered by this caller fixture.

Early fixture failures were resolved before production install: add the
zero-extra-count delay to the coverage product, route signed-byte negative
instructions through the existing LB implementation, and use the actual
layout padder CLI. Larger negative bodies can overlap the adjacent retail
helper address; rebase every negative to 0x15400000 before interpreting it.
All ten controls then execute and show a real observable difference.

The earlier 14-test callee qualification is prior evidence, not a fresh
whole-suite run here. Its source/guard/helper tools fingerprints and all
776 installed callee bytes are unchanged. Fresh connected testing and the
new complete-ELF audit cover the current caller change. Deeper loader,
auxiliary, entry-dispatch and allocation/copy/free internals remain bounded
callbacks; no complete hardware/gameplay acceptance is claimed.

Native32 uses valid modeled table identities 0,7,128,186. Contrived wrapping
indices/high bits are emitted-O32 guest evidence, not portable C array-domain
or signed-overflow guarantees, and not a 64-bit host-port implementation.

## Linked Audit And Totals

All 104 production linked words equal retail directly; the target extent
changes 12 -> 416 bytes. ELF length remains 3,261,160. Exactly 364 bytes
change: 324 in target slot, two target-size bytes and 38 existing metadata-
ordering bytes. The receipt's 40 changed metadata bytes include the two
size bytes; do not count them twice. Verify headers/sections, symbol/name
counters and all values rather than accepting arbitrary metadata changes.
Every other ELF byte, including the full buffer callee, is exact.

- ELF SHA-256: 4584dc279ac3519c983969e64559c443ae4c4668ef37ae3a5dc344bb2cfab4b2.
- Owner SHA-256: 9505579fd018dc9d8f3082fe2817bcc726b3b39048e9fd39eb1763a74a119f36.
- All 189,088 protected data bytes / 720 owners exact, SHA-256
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
- Guard SHA-256 unchanged:
  5eace9a1e712613397671e3d8d61acfcbd1ceaa4a7a73d4377b15d97ff7400c6.
- Conversion CSV unchanged:
  32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
- Rodata source, tracked symbols/layout and ignored auto assignments exact.

Fresh matcher: Game 2,788/4,822 (57.82%), total 3,461/5,495 (62.98%),
Init 492/492 and Debugger 181/181. Zero drift, 2,034 different.
Only +1 matching credit; the function already counted as converted C.
Root README changes only aggregate matching rows. Check off the completed
full caller in the roadmap, not the open deeper-resource/runtime work.

Commands from 64CBFD:

```sh
wsl --exec python3 -m tools.experiments.game_resource_preparation_candidates
wsl --exec python3 -m tools.experiments.game_resource_preparation_candidates --declarations
wsl --exec python3 -m unittest tools.tests.test_game_resource_preparation_match -v
wsl --exec make -C conker -j4 build/conker.us.elf progress.csv
wsl --exec make -C conker match-progress NON_MATCHING=1
wsl --exec make tools-check
```

Build succeeds with the existing duplicate generated_12D630 recipe warning;
target has no compiler diagnostics. Consumer/mounted/older WSL tools checks
pass, plus native py_compile of the two new older-mirror files. Do not infer
a native full-check pass from py_compile.

## Ownership And Graph

Tools commit 160bba0e5db1411e38a09897427e12a4a5f4bc49 banks only the new
candidate module and focused test before the consumer pin. Copy only these
two absent authored files into the older standalone checkout. Its HEAD and
all six protected existing hashes remain unchanged, dirty entries 283 -> 285.
No older reset/overwrite/commit or push.

Native graph query succeeds. Native update extracts two files but refuses
unsafe shrink 39,729 -> 17,947, preserving 19,398 nodes from 2,972 existing
excluded files. Keep version/zero-node warnings; no force/purge/install.
Wait for the consumer commit's detached hook: fresh log bytes/UTC, fresh
Rebuilt tail and zero actual Graphify/Python workers before closing out.
No OGL/Release/save/editor/private-input changes; Release remains frozen.

## Next Full Extras Loader

Continue func_1503DC3C: VA 0x1503DC3C..0x1503DD1C, ROM
0x6B0EC..0x6B1CC, full 56 words / 224 bytes, frame 0x38, same owner.
Its current C is still a zero-return stub. Preserve the complete routine:

1. Unsigned live D_800C5628 count and 12-byte descriptor stride; reload
   D_800C5338 base around helper calls, not a cached immutable table.
2. Invoke func_1510D0EC with (descriptor+4 word,0,0x3E,1), publish its
   result through the live descriptor base, then reload that result.
3. Accumulate result bit 0x10 only for exact 0x80000000 failure sentinel,
   not every nonzero or negative pointer word.
4. Keep live count reloads/descriptor cursor update, full O32 saved-register
   lifetime and all zero/boundary/mutation/failure paths.
5. Reuse the current caller to qualify actual extras loading and failure
   propagation beyond today's bounded callback. Main func_1503CF20 loading,
   deeper callbacks/heap/hardware/renderer/gameplay remain separate and open.

Do not mark the full Game matching goal complete for this direct match.
