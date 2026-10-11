# Game Resource Extras Loader Direct Match

Date: 2026-10-11. Continue
[Note 1258](1258-game-resource-preparation-caller-direct-match-20261011.md)
under [the agent workflow](../AGENT_WORKFLOW.md). Single Codex writer, zero
Claude calls. Keep the full Game matching goal active. Authorized checkpoints
are committed tools-first, without pushing.

## Scope And Immutable Baseline

- Complete func_1503DC3C: VA 0x1503DC3C..0x1503DD1C,
  ROM 0x6B0EC..0x6B1CC, 56 words / 224 bytes, frame 0x38.
- Owner: conker/src/game/generated_6A3D0.c; retail asm/6A3D0.s lines 971..1031.
- Consumer entry HEAD e3d8038f2f96d87979bb85e1a2fa5f574859eb68, clean.
- Mounted tools entry HEAD 160bba0e5db1411e38a09897427e12a4a5f4bc49, clean.
- Older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a,
  285 dirty entries; preserve all existing work.
- Original C is a 12-byte zero-return stub. Recover the complete routine,
  not an easier neighbor or only the already tested caller's normal path.
- Baseline ELF SHA-256:
  4584dc279ac3519c983969e64559c443ae4c4668ef37ae3a5dc344bb2cfab4b2.
- Baseline owner SHA-256:
  9505579fd018dc9d8f3082fe2817bcc726b3b39048e9fd39eb1763a74a119f36.

Freeze before-source/ELF/guard/progress/rodata/symbol/layout/auto-assignment
bytes and hashes in ignored conker/build/game-resource-extras-test.
Never rewrite its original baseline manifest after installation.
Inspect the complete retail routine and both actual callers: the banked
func_1503DA9C at 0x1503DB90 and still-unrecovered func_1503CF20 at 0x1503D1C4.
Both forward the identity word. Refine the owner's forward declaration to
the recovered s32 identity interface; the actual caller bytes remain exact.

## Complete Semantic Recovery

Read unsigned D_800C5628[identity]. Zero count returns zero without reading
D_800C5338 or a descriptor. Nonzero count takes its current descriptor base.
Each 12-byte descriptor submits word +4 to func_1510D0EC(input,0,0x3E,1).

After the callback, reload the live pointer-table slot to choose the result
publication address at the current byte offset. After storing, reload that
slot again before reading the published word. These are separate observable
operations: the destination can alias the table slot and publication itself
can rebind the base. Do not test the raw helper return instead of the word
read through the newly reloaded base.

Only exact 0x80000000 accumulates error bit 0x10. Zero, other negative words,
and valid nonzero values do not. Continue loading despite a prior sentinel.
Increment the signed index, advance the byte offset by 12 and descriptor
cursor by three words, then compare against the live unsigned count. Preserve
the retail branch-delay cursor advance and all seven saved-register lifetimes.

## Direct Compiler Evidence

Use the unchanged owner profile -O2 -g3 -Wo,-loopunroll,0. No Makefile,
profile, shared helper, guard, assembly substitution or opaque ROM body edits.

All five screened complete forms emit 56 words, frame 0x38, zero raw
differences: selected, inline-result, count-last, inline-slot, inline-count.
Select the first complete semantic form, with explicit count/slot/cursor,
index/offset and loaded result. Isolated and copied-owner target fingerprints
are identical. Every linked production word equals retail directly.

## Fresh Qualification

Ten pre-install tests pass in 89.216s. Ten post-install tests pass in 31.832s.
No fixture failure occurred in these suites.

- 1,728 independent-reference cases / 3,456 original/raw runs; all 56 words
  reached. Compare full memory, access order, calls and error results.
- 115 mutation/word-ABI cases / 230 runs: wrapping guest identity indices,
  unsigned 0x7FFF/0x8000/0xFFFF counts, live growth/shrink, repeated base
  changes and modified following descriptor inputs.
- Sixteen publication/count-alias cases / 48 original/raw/padded runs:
  table slot at offsets 0/12/24, destination store rebinding the base,
  reloaded sentinel despite valid helper pointer, and count/result alias.
- Nine independent original/raw/padded links across three symbol sets,
  54 rebase cases, signed-LO carry and zero direct differences.
- 936 all-access fault pairs, every gate fired; complete partial memory,
  accesses and callback prefixes equal. Guest instruction faults are not
  a portable C fault-semantics guarantee.
- Eleven effective freshly compiled IDO controls: stride, exact sentinel,
  wrong negative/nonzero tests, helper return versus reloaded word, cached
  destination, missing second reload, cached count, ignored zero count,
  wrong resource word and wrong request flag.
- Native32 complete C at O2 and O0: 2,016 cases per profile / 4,032 total.
  Independent reference compares every modeled memory byte and call trace;
  live table/count aliasing, growth/shrink and input mutation covered.
  The helper-return negative is effective and fails.
- Copied before/after owner, actual no-unroll profile: all 14 neighbors
  preserve bytes/extents/relocations/pools, zero diagnostics. Both real
  layout/generated padders preserve every non-target byte/relocation.
- 6,144 connected cases / 12,288 runs through actual 104-word caller,
  complete 56-word extras and actual 194-word buffer callee: independent
  outer/extras/buffer references, full memory/access/call/error comparison.
  Reach all 104 caller words, all 56 extras words and 137 buffer words.
  Do not claim all 194 buffer words reached by this fixture.

Large-count fixtures shrink the live count after the first callback; they
do not execute 65,535 descriptors. Contrived wrapping indices are emitted
O32 guest evidence, not valid portable C array or signed-overflow domains.
Native32 uses aligned modeled identities 0,8,128,186 and four-byte pointers;
256-entry model storage is not a claim about the retail table's legal range.
The main retail loader uses a signed identity < 0xBB gate.

The earlier caller/buffer whole-suite receipts are prior unchanged evidence,
not fresh whole-suite runs here. Fresh connected tests and complete ELF
audit verify their unchanged installed code. Main loading, auxiliary/event/
resource-request and allocation/copy/free internals remain bounded callbacks.
No full heap/hardware/renderer/gameplay or 64-bit host-port acceptance claim.

## Linked Audit And Progress

Target extent changes 12 -> 224 bytes; ELF length remains 3,261,160.
Exactly 170 ELF bytes change: 169 target-slot bytes and one target-size byte.
The one changed metadata byte is that same size byte, not an additional
change; no metadata reordering occurred. Verify headers/sections and
symbol/name counters, all values and the one target extent before allowing
metadata. Every other ELF byte is identical.

- New ELF SHA-256:
  8b43e9619177ab0f1a8065094300796e24d39d51ca4fc929d37124bbcd1c0dcb.
- New owner SHA-256:
  a0b5a3b085da38a972e866ad6b1d1fbaba284eca12389297b88ef324c86a8fdf.
- All 189,088 protected data bytes / 720 owners exact, SHA-256
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
- Entire guard manifest unchanged, SHA-256
  5eace9a1e712613397671e3d8d61acfcbd1ceaa4a7a73d4377b15d97ff7400c6.
- Conversion CSV unchanged, SHA-256
  32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
- Rodata source, tracked symbols/layout and ignored auto assignments exact.

Fresh matcher: Game 2,789/4,822 (57.84%), total 3,462/5,495 (63.00%),
Init 492/492 and Debugger 181/181. Zero address drift, 2,033 different.
Only +1 matching credit; this stub already counted as converted C.
Root README changes only its two aggregate matching rows.

Commands from 64CBFD:

```sh
wsl --exec python3 -m tools.experiments.game_resource_extras_candidates --variants
wsl --exec python3 -m unittest discover -s tools/tests -p test_game_resource_extras_match.py -v
wsl --exec make -C conker -j4 build/conker.us.elf progress.csv
wsl --exec make -C conker match-progress NON_MATCHING=1
wsl --exec make tools-check
```

Build succeeds with the existing duplicate generated_12D630 recipe warning.
Target copied-owner diagnostics are empty. Consumer/mounted/older WSL tools
checks pass, plus native py_compile of the two new older-mirror files.
Do not infer a native full-check pass from py_compile.

## Ownership And Graph Gate

Tools commit 563924a549deca698404ad5955cde2b6f1feabb0 banks only the new
candidate module and focused test before the consumer pin. Copy only those
two absent authored paths into the independently dirty older sibling.
Its HEAD and all eight protected existing hashes stay unchanged; dirty entries
285 -> 287. A relative-path copy initially targeted an existing nested
folder; remove only the two newly copied hash-verified files, preserve its
directories, and verify the corrected absolute sibling copies. No existing
tool file is overwritten, no older commit/reset or push.

Native graph query succeeds (19 nodes). After documentation edits, native
update re-extracts eight uncached files but refuses unsafe shrink from
39,740 to 17,969 nodes. Its fail-closed path retains 19,398 nodes from
2,972 existing excluded files. Preserve version/zero-node devcontainer
warnings; no force/purge/install.
Wait for the consumer commit's detached hook using fresh log bytes/UTC,
a fresh Rebuilt tail and zero actual Graphify/Python workers before close-out.
No OGL/Release/save/editor/private-input changes; Release stays frozen.

## Next Complete Main Loader

Live verified func_1503CF20: VA 0x1503CF20..0x1503D368,
ROM 0x6A3D0..0x6A818, 274 words / 1,096 bytes, original frame 0x78.
Its current C body remains a 12-byte zero-return stub. The complete assembly
is asm/6A3D0.s lines 11..308, including the final cleanup and return paths.

1. Recover identity 0xFF/retail signed 0xBB guards, cached-presence return,
   six-argument main request, allocation failure and data/header publication.
2. Recover all pointer/count tables and both descriptor relocation loops,
   distinguishing live unsigned-halfword count from cached word count.
3. Connect the now-matched complete extras loader and preserve every event,
   auxiliary/config/fifth-flag gate and error accumulation order.
4. Recover all failure cleanup: optional free, extras cleanup, auxiliary and
   secondary free/NULL stores, and main pointer-minus-0x38 free/NULL store.
5. Qualify the complete main routine, copied owner/neighbors, all caller ABI
   changes and actual parent/extras/buffer connections before installation.

Do not replace this scope with easier neighboring func_1503D368 or only
the normal successful path. Deeper helper implementations/hardware/gameplay
and removal of the earlier buffer's normalization guards remain separately
open. This checkpoint does not complete the wider Game matching goal.
