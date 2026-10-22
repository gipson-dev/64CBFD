# Selector Callback Factory Direct C Match

Date: 2026-10-22

## Result

Match the existing semantic `func_1515D088` in
`conker/src/game_1897A0.c` directly from complete C. All **42 words,
frame64 and two bindings** emit under the existing normal O2/g3 profile.
There are no new guards, raw emitters, dummy locals, initialized reserved
bytes, alignment filler or profile changes.

VA1515D088..1515D130 / ROM18A538..18A5E0, ends exclusive.
Unlinked C/GNU-original body SHA-256:
`46ca32cb598d709f37b3e4d629e873924a6c0606f82af53bb52cfb7b805727b3`.
Keep `conker/asm/nonmatchings/game_1897A0/func_1515D088.s`.

The prior C was semantic, not a zero-return placeholder. Its linked extent
was 41 words plus a separate slot-padding word, with 37 retail differences.
The new body restores the exact local layout, opening branch sequence and
allocation-result lifetime. It does not add another converted-C function.

## Recovered Contract

Use `void *func_1515D088(void *source)`. Read the full word at source+0x18,
capture its low byte in the payload, and promote that byte to a signed
32-bit selector. Preserve the original signed range check: selector <0 or
selector >=2 returns NULL. The negative comparison is redundant after the
unsigned byte capture, but retaining the range-check shape reproduces the
retail branch without guards.

Do not compare the original full word, convert a float numerically, or
reload the selector after the factory call. Poisoned upper bits do not
change whether selector zero or one is accepted.

Use the owner-local `SelectorCallbackPayload`:

| Offset | Field | Treatment |
| --- | --- | --- |
| +0 | Source pointer | Capture before the factory |
| +4 | Float parameter | Set to positive zero |
| +8 | Selector byte | Capture from the incoming word |
| +9..+11 | Reserved bytes | Leave untouched; still copy all three |

The real 12-byte local has source at current SP+0x30, value at +0x34,
selector at +0x38 and three reserved bytes at +0x39..+0x3B.
The allocated pointer survives memcpy in the adjacent +0x3C word.
Declare created pointer, payload, then scalar selector. Other declaration
orders produce two, four or six differences despite the same frame/length.
The old mask-only gate gives 41 words and the wrong private layout.
Several semantically equivalent explicit byte/range forms match; the
historical spelling is not uniquely established.

Call `func_151491F4(0x12C, -1, 0x11, 0, 0xD, 0xC, 0xFF, 1)`.
On success, copy the complete 12-byte payload to created+0x28 and return
the allocated base, not memcpy's destination or return word.
On failure, perform no copy and return NULL.

Bindings relative to the body:

| Offset | Kind | Symbol |
| --- | --- | --- |
| 0x6C | R_MIPS_26 | `func_151491F4` |
| 0x88 | R_MIPS_26 | `memcpy` |

All 42 instructions execute across the corpus. The negative branch's true
edge is impossible for the captured byte; do not claim a negative post-capture
selector was exercised.

## Caller And Helper Bounds

The known direct caller is complete, already-exact `func_1501374C`,
11 words/frame24 at ROM40BFC..40C28. It ORs source byte +0x16 with 4 in
the target call's delay slot, invokes the factory routine, ignores its
result and returns 1. Qualify the whole original/current caller for 160 phases.

Add `void *func_1515D088(void *);` locally to `src/game_40490.c`.
All 32 caller functions, pools, diagnostics and the complete padded caller
object remain byte-identical. Both old/new diagnostics are empty; do not
claim an observed warning was removed. No shared header change is needed.

Connect the original, already-exact 28-word `func_151491F4` wrapper
at ROM1766A4 and 11-word `memcpy` at ROM22EC0.
Execute every helper word across 320 connected phases, including forward
overlap and private payload aliases. The wrapper forwards nine arguments
to `func_15149130`, including its inserted -1:
`(300, -1, 17, -1, 0, 13, 12, 255, 1)`.

That lower constructor remains a bounded provider. No complete constructor,
allocator, hardware or natural gameplay acceptance is claimed. Its existing
source and object are pinned and unchanged.

## Qualification

Tools: `experiments/game_selector_callback_factory.py` and
`tests/test_game_selector_callback_factory.py`, identical in both copies.

| Final Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 139.074s | 8 tests, 156.718s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 7.145s | 2 tests, 10.206s | 0 / 0 / 0 |

Explicitly reuse the other six checks per copy only under strict source,
raw/padded object, helper, input and whole-image identity. They are not
fresh installed executions. Shared project-tool checks pass in both copies.

- 20,480 guest phases sweep all selector bytes, four upper-word patterns,
  both allocation outcomes, five helper-effect plans and two SP phases.
- Another 320 phases cover source/destination/private-stack aliases.
  Check full final GPR/FPR/HI/LO/memory/event state, volatile clobbers and
  argument homes. The payload's reserved bytes have five observed patterns.
- 6,144 native32 cases per optimization at O0/O2/O3 use trap UBSan.
  Check the nine defined payload bytes, allocation gates, captured selector,
  returned base and all destination fences. Do not assert portable values
  for native uninitialized reserved bytes; guest tests qualify their exact
  physical contents, including deliberate alias mutations.
- All eight compiled wrong-C controls fail effectively. Six independent
  GNU links / 240 phases exercise both call relocations.
- Verify 1,512 fired root-access fault prefixes, excluding provider accesses,
  plus eight strict-image corruption controls. These are not C-fault/MMU
  guarantees.
- Pin 28 historical/current inputs and the predecessor target object.
  Preserve all seven owner neighbors, pools, diagnostics and all caller
  bytes. The actual Make shadow uses eight productive commands: three
  for the plain owner and five for the asm-processor caller.

Initial fixture failures are not passing receipts. The first padding seed
produced only two patterns; vary the upper-word seed to exercise five.
GDB identified the native O2 crash as an unaligned MOVAPS in freestanding
_start; use the existing native-fixture stack-realignment flag. Keep the
native byte-copy spy out of line, matching the real call boundary, so O3
does not inline and diagnose the intentionally untouched tail bytes.
No guest source change, warning suppression or reserved-byte initialization
was used to resolve those native-fixture issues. Rerun both complete suites;
the table records the final successful runs.

## Production And Preservation

Rebase the previously committed runtime factory's source, guard manifest,
object and ELF using its strict adoption proof. Add four new task-file
copies and verify all 15,802 live/cache files, including every one of the
1,454 linker objects. Reuse the already-verified Linux cache; no installation
or provider reconfiguration is needed.

Actual production Make exits zero in 1.968s and exactly reproduces the
independent full-image prediction: **123 changed bytes = 122 instruction
bytes + one symbol-size byte**, zero exclusions or metadata permutations.
The target extent changes from 164 to 168 bytes inside its existing slot.
The inherited duplicate generated_12D630 Make recipe warning remains.

Installed ELF SHA-256:
`beaa3ec7b8fe3915458d40e2b3f5a6850e6d03328b32412bdc930d1882dc7dc9`.
Installed target-owner object SHA-256:
`840296b21469a5045553902eedb4161fbdfc4b54176e8fe73555d3ff1cbd115e`.

All other 6,055 bodies and all 6,056 addresses remain fixed.
The entire guard manifest and caller object are unchanged.
Protected Game data remains exact: 189,088 bytes / 720 owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Recheck sealed live inputs before/after adopting only the target object,
ELF, generated linker script and progress CSV.

Tools commit `3bb6ee8ff0d5f49a72feab6afdeabdf05edc53f4` precedes the
consumer source/docs/pin commit. Preserve all 1,528 pre-existing older-mirror
dirty statuses and hashes; add only two task files, totaling 1,530 paths.
Do not commit/reset/clean/stash that mirror. No push or Claude call.
Host Release stays frozen. Root README changes only two aggregate rows.
Refresh Graphify and audit retention/unique relocation of prior nodes and
all excluded-existing nodes at the committed checkpoint.

## Measured Progress And Resume

The literal standard matcher exits zero against the adopted live ELF:

| Section | Byte-Exact Converted C | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,726 / 5,505 (67.68%) | 0 | 1,779 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,053 / 4,832 (63.18%) | 0 | 1,779 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The threshold remains 4,129; **403 more exact functions** are required.
The 75% goal remains unfinished. The refreshed ELF-pinned queue has 1,647
placeholders, 123 semantic/other definitions and nine unlocated entries.

Next: `func_1505E7CC`, 42 static words/frame0, existing semantic C with
39 differences. Source `conker/src/game_83300.c`, original
`conker/asm/nonmatchings/game_83300/func_1505E7CC.s`.
VA1505E7CC..1505E874 / ROM8BC7C..8BD24, ends exclusive.
Screen the byte actor-ID gate, pointer-table lookup, null/zero-length gates,
unsigned byte-length division by 24, header pointers at -4/-8 and first-match
search with a full-word key. Preserve branch-likely delay updates and the
two statically unreachable duplicate loads/increments at 1505E804/1505E858.
Establish all callers, aliases and physical schedules before fitting.
Screen only: no edit or credit. Keep the 862-word `func_1508CAD8` owner stub
queued separately.

Private snapshots, probes, fixtures, images, queues and audits live under
`conker/build/game-selector-callback-factory/qualified/`; do not commit them.
