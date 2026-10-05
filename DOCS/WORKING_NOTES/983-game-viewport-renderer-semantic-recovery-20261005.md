# Game Viewport Renderer Semantic Recovery

Date: 2026-10-05. Starting HEAD: `29fea6a0`.

## Decision

Continue [Note 982](982-game-viewport-command-helper-semantic-recovery-20261005.md)
with the complete caller, `func_1510B9D0`, replacing its zero-return placeholder
in `generated_138520.c`. The recovered interface is **`Gfx *(Gfx *, s16)`**.
Update its public declaration in `functions.h` and add explicit pointer/word
casts at the sole source caller, `func_15019464`, without changing that caller's
79-word linked slot. No remaining downstream placeholder is treated as recovered.

| Measurement | Final production result |
| --- | --- |
| Entry | `0x1510B9D0`, unchanged |
| Retail reference | ROM `0x138E80`, 356 words / 1424 bytes |
| C body | 347 words / 1388 bytes, nine trailing padding NOPs |
| Frame | `0xB8` C versus `0x98` retail |
| Raw aligned differences | 343 / 356; non-matching |
| Guards / profile override | None |

Full linked slot SHA-256:
`8ee7028e5868defa0388d7b4ec082af1bb41d711f9a0a6433b86c7a0afc7d01f`.
This is complete semantic control-flow recovery in a fitting slot, not an
original-frame match, general machine-state equivalence or runnable-ROM claim.

## Retail Contract

- Sign-extend the incoming slot to sixteen bits. Compute its 0x9A0 actor stride
  and retain the initial actor pointer across callbacks.
- Set `D_800BEBA0` to one. Capture suppression from mode one plus its enable
  byte, or the slot bit in `D_800D18A0`. Later callbacks cannot change this
  captured decision. The shift uses the retail low five index bits.
- Emit the actual initial helper, two page-dependent light packets, palette
  updater/color connection, identity helper and modelview matrix load.
- Dispatch category `0x14` to `150C8600`, `0x1A` to `15100464`, `0x13` to
  `150DFBD0`, `0x35` to `150CF5E8`, and `0x33` to `150D765C` unless suppressed.
- Call the context reset, optionally emit `DC280C0A` with its page/slot source,
  reload the actor base and truncate its three coordinates for all fourteen
  arguments of `1515D914`. Preserve the captured light/table addresses.
- Unless suppressed, select the primary display-list/parser path, optional
  second list and actor effect; then call `1515E544`, emit the optional third
  list, and preserve late page/table/byte/list-pointer reloads.
- Call `151742EC` on every completed path, append the final pipe sync and
  return the resulting display-list cursor.

The initial second light packet is **`DC08060A`**, obtained with
`gSPLight(..., 1)`, not `gSPLookAtY`'s `DC08030A`. The first paired run caught
the wrong draft macro; it was corrected before final qualification. The
`DC280C0A` block uses the SDK DMA macro with length 48, index `G_MV_LIGHT` and
offset 96; no unsupported viewport/structure interpretation is invented.

Retail's 35-entry category table is read from the SHA-1-verified ROM and checked
against the five cases. C uses explicit comparisons, avoiding a new generated
rodata owner. Existing Game data and exported retail label addresses stay
unchanged; the recovered C does not use the now-inactive retail jump table.

The original `150A50C0` branch at `0x1510BE60..0x1510BE94` is unreachable:
the captured draw byte is zero at `0x1510BE58`, with no intervening mutation,
and that branch immediately skips the fourteen-word body. Do not invent a
second byte reload to make that dead body reachable. The new C likewise has
four unreachable duplicated comparison constants at `1510BB48/64/80/9C`.

## Qualification

Fourteen new tests in `tools/tests/test_game_viewport_renderer.py` qualify:

- **5379 complete paired retail/C traces**: 4608 slot/page/category/optional-pass
  products, 259 category boundary cases, 336 suppression products, 24 callback
  mutations, 96 connected leaf traces, seven slot/truncation boundaries, 48
  independent effect-byte/flag products, and one slot/coverage trace.
- The **96 connected traces execute the actual linked helper, palette updater,
  color emitter and identity helper on both sides**, not substitute versions.
  The angle callback supplies a bounded finite sample; other external renderer
  callbacks remain explicit models with checked arguments, snapshots and cursors.
- **4608 native cases** compile the actual renderer, helper, color emitter and
  SDK macros with strict 32-bit compiler warnings. Independently check expected
  callback order, all fourteen transform arguments, packet count, both light
  command words/pointers, returned cursor, fences and final state flag.
- **Four invalid-slot prefixes** stop on an unmapped read after agreeing on
  the original callback/global-write prefix. They are not full invalid-input,
  hardware-fault or safety acceptance.
- Mutations prove suppression remains captured in both directions; coordinate
  conversion uses a reloaded actor base with distinct values; the later actor
  effect retains the original actor pointer; and late category, page, table,
  byte and optional-list updates are observed.
- Output-fence controls reject unowned writes. An independent actual-source
  IDO O2/g3 compile reproduces all 347 body words with no compiler warnings.

Complete visible memory, callback arguments/order/snapshots, state-flag writes,
return cursor and preserved registers agree in the paired fixtures. Stack
scratch bytes differ by design and are excluded from visible-memory comparison;
saved-register restoration is checked separately. Ordered arbitrary reads,
FCSR, exception behavior, original call-frame identity and pixels are not proven.

Coverage reaches **342 / 356 retail words** and **343 / 347 C body words**;
the only exclusions are the proven dead bodies above. Nine C padding words
receive no credit. The ignored receipt is
`conker/build/game-viewport-renderer-qualification.json`; its complete flag
requires all fourteen successful methods and the exact corpus counts.

Final shared-header rebuild, padding, guards, link and progress pass:

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_viewport_renderer tools.tests.test_game_viewport_command_helper tools.tests.test_game_palette_updater tools.tests.test_game_queued_segment_writer tools.tests.test_game_dual_matrix_emitter tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_startup_thread_contract -q -f
```

All **95 final combined tests pass in 52.200 seconds, no skips**. The rebuild
reports unrelated existing pointer/integer warnings; no zero-warning full-tree
claim is made. Complete Init code/data, Debugger code and Game data remain
retail-exact. The caller, initial helper, guarded `1510B32C` and `1510B958`
linked slot hashes are unchanged and pinned by the tests. Matching totals remain
3283/5463, Init 492/492, Game 2610/4790 and Debugger 181/181, zero address drift.

## Next And Boundaries

Read-only sibling audit finds its existing renderer at `recomp_out/.c:816929`
through the original return at `0x1510BF58`, with title/scene admission logic
and gated diagnostics. No named override appears in the scoped host src/CMake
search. Do not overwrite those host changes or infer fresh runtime acceptance.
No sibling source, build, save or frozen Release changes.

Current dependency inventory still has zero-return C placeholders for
`1515D914` (601 words), `1515E544` (209), `151742EC` (193) and `1512E5F0` (188).
The 228-word `150A5378` retains assembly; context-reset `1510F800` already has
its eight-word semantic wrapper. Their actual algorithms and natural effects
are outside the callback-model evidence, not completed by recovering this caller.

- [x] Recover the full renderer body and public cursor/signed-slot interface.
- [x] Preserve captured state, late reloads, optional passes and all call arguments.
- [x] Qualify connected actual command/palette/color/identity leaves.
- [x] Rebuild shared-header users, retain caller bytes and pass all 95 checks.
- [ ] Recover full `func_1515D914` and qualify its fourteen-argument contract.
- [ ] Recover `func_1515E544`, `func_151742EC` and `func_1512E5F0` separately.
- [ ] Qualify actual submission, RSP/RDP pixels and natural effects.
- [ ] Recover original renderer frame/scheduling for a raw byte match.

Init still has 492 C / 47 ASM owners; no new Init adoption. README aggregate
rows remain unchanged because the renderer placeholder was already counted C
and this is not a new byte match. No push, ROM promotion or broad goal completion.
