# Game Cached Lookup Frame And Guarded Miss-Path Match

Date: 2026-10-05. Starting HEAD: `8f705752`.

## Source Recovery

Target: `func_1502AC88`, `conker/src/game_57FA0.c`. Entry/end:
`0x1502AC88..0x1502AF04`; ROM `0x58138..0x583B4`; 159 words / 636 bytes.

The earlier source emitted 158 body words into the 159-word slot, with a
matching 0xA0 frame but 156 raw word differences. Updating the address
parameter in place recovers retail's missing prologue move into s0 and the
full body length. Declaration order then recovers the saved cache record at
sp+0x3C, aligned DMA-pointer spill at sp+0x34 and captured offset at sp+0x58.
The selected source emits its first 128 words exactly, including all cache-hit
rotation instructions. It has twelve raw differences confined to the miss path.

The 71-form default IDO O2/g3 screen reproduces these measurements without
diagnostics; no trial is directly exact. The immutable baseline remains in
[the screen driver](../../tools/experiments/game_cached_lookup_candidates.py).
Reports are ignored artifacts under `conker/build/game-cached-lookup/`.
Integer buffer and aligned-pointer-update trials can exceed the slot and are
not adopted. Signed-shift trials are compiler experiments only, not qualified
source for negative indices. The chosen source retains unsigned multiplication.
No profile override, instruction insertion/omission, ABI or data-layout change
is introduced.

Unguarded full-slot SHA-256:
`741808c2f0dd29cfa36ed21f352da41403212510d5803172ed14cdbbba767a35`.
Guarded/retail full-slot SHA-256:
`78b570cec704115f1ab2f832a78373a1e6e0038b65735e868197083d96e37b05`.

## Guard Classification

This is a **guarded match, not a direct compiler match**: 147 / 159 words
already agree; twelve expected-word guards normalize the remainder. The
[patch table](../../conker/retail_word_patches.us.csv) and independent
[match tests](../../tools/tests/test_game_cached_lookup_match.py) pin each
unlinked expected/replacement word. None of the guarded offsets has a
relocation. All existing calls and branch/delay-slot control words are intact.

| Group | Offsets | Effect |
| --- | --- | --- |
| Before DMA | 0x200, 0x204, 0x208, 0x20C, 0x224 | Closed buffer/length temporary allocation and ABI-equivalent buffer roundup |
| After DMA | 0x230, 0x238, 0x23C, 0x240, 0x24C, 0x250, 0x258 | Closed pointer/offset/descriptor temporary allocation and commutative pair-pointer sum |

Source retains the ordinary `(storage + 15) & ~15` roundup. At offset 0x200,
retail uses `sp+0x68` whereas raw C uses `sp+0x6F` before masking. For an
8-byte-aligned N64 stack, `(sp+0x68)&~15 == (sp+0x6F)&~15` for both phases
0 and 8 modulo 16. This equality is not claimed for arbitrary alignment;
the test also pins a deliberately unaligned counterexample. It would be
incorrect to replace the generic C byte-array roundup with +8 solely for
this machine-word spelling.

The second group keeps the offset capture before output, descriptor output
before cache install, the live clock load in the install call's delay slot,
and the captured return after install. Raw and guarded ordered memory events
agree, rather than merely their final values. On hits, the return offset is
still loaded after the output store, so output aliasing the last cache offset
intentionally changes the returned value. On misses, the local offset capture
prevents that alias from changing the return.

## Qualification

The new module executes complete retail, freshly compiled raw and guarded
lookup bodies, each connected to freshly compiled/checked cache-installer
instructions from [Note 995](995-game-cache-installer-alias-preserving-word-copy-and-guarded-match-20261005.md).
Only SDK DMA and byte copy are bounded hooks. DMA writes deterministic words,
can mutate the live clock or introduce a new cache hit, and clobbers all
caller-saved integer temporaries. The install call is not an opaque callback.
This low-word runner is not hardware/emulator or real SDK DMA acceptance.

- 11088 three-way cases cover three cache/clock patterns, both N64 stack
  phases, all sixteen hit positions, duplicate first-match selection, all
  64 cache-word output aliases, clock output alias and an external output.
- Misses additionally cover low address offsets 0/4/8/12, DMA lengths 16/32,
  clock wrap, live callback clock mutations, and a callback-created hit that
  must not restart the already-missed scan.
- Complete mapped memory including stack/fences, ordered read/write/call
  events, call arguments, return values and saved-register restoration agree.
- Each form visits 158 / 159 lookup words. The unreachable redundant scan
  increment at offset 0x1E0 is covered by static full-slot identity. The
  connected count-two installer path visits 53 / 97 words; the independent
  installer suite retains all-97-word coverage across counts 0..16.
- Omitting each of the twelve guards fails a bounded access/control check
  or the complete event/memory/return comparison. Both alignment phases and
  selected external/clock/cache-offset outputs are used as witnesses.
- Seven address/component vectors additionally qualify 32-bit wrap and the
  signed component extremes, with both stack phases and DMA clock mutation.
- A native 1056-case selected-source hit/output-alias matrix checks actual C
  against independent cache rotation/output/return expectations. Existing
  native miss, clock mutation, partial-overlap and connected lookup/block/
  variadic/relocator fixtures remain intact.

The new module also checks production source/table/full-slot identity and
unlinked guard inputs with no guarded relocations. The existing fresh-IDO
three-function fixture now applies only the twelve independently checked
lookup guards, retaining the cache installer's 41 guards and guard-free block
loader comparison. Patch table: 10591 rows, zero duplicate numeric
owner/function/offset keys.

The shared patch-table consumer rebuild succeeds and freshly reports:

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3292 / 5463 (60.26%) | 0 | 2171 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2619 / 4790 (54.68%) | 0 | 2171 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This adds one guarded byte match, not a new C conversion. The 47 retained
Init ASM functions are unchanged. README edits contain aggregate totals only;
recovery narration stays in the dedicated documentation. Existing generated-
slice recipe and unrelated source warnings remain; no isolated candidate
diagnostics are introduced. `make tools-check` passes.

**All 183 final combined checks pass in 107.148 seconds, no skips.** Complete
Init code (164048 bytes), Init data (17376 bytes), Debugger code and Game data
(189088 bytes / 720 owners) remain retail-exact. `git diff --check` passes.
The combined command extends Note 995's 176-check suite with the seven new
cached-lookup checks, without removing earlier gates.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m tools.experiments.game_cached_lookup_candidates
python3 -m unittest tools.tests.test_game_cached_lookup_match tools.tests.test_game_cache_installer_match tools.tests.test_game_cache_installer_candidates tools.tests.test_game_block_loader_direct_match tools.tests.test_game_offset_relocator_match tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

## Host Boundary And Next

Read-only sibling inspection finds translated retail `func_1502AC88` in
`64CBFDOGL/recomp_out/.c:202256`: frame 0xA0, original sp+0x68 masked buffer,
sp+0x34 pointer spill, sp+0x58 return capture and live-generation install call
are already present. Existing diagnostic probes and the old heap commentary
remain separate. No host synchronization is needed for this matching change.
No sibling source, build, save or frozen Release artifact is modified; real
SDK DMA/copy, PC runtime and rendering acceptance remain separate and open.
Unaligned/invalid pointers, unsupported memory extents and arbitrary stack
alignment remain outside this bounded qualification.

Next connected recovery: `func_1502AF04`, still a zero-return placeholder.
Retail occupies 71 words with frame 0x40: derive table address from base and
component, round caller buffer/address/length for DMA, add the original base
to the offset word of each eight-byte pair, and return the adjusted pair
pointer. Begin with count-zero, peeled/bulk counts, buffer alignment and
in-place offset-wrap fixtures before source-shape matching. Do not infer the
caller buffer contract from this lookup's private byte-array allocation.
