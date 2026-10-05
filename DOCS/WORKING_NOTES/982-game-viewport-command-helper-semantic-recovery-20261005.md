# Game Viewport Command Helper Semantic Recovery

Date: 2026-10-05. Starting HEAD: `a22cbf1b`.

Subsequent [Note 983](983-game-viewport-renderer-semantic-recovery-20261005.md)
recovers the complete `func_1510B9D0` caller. Its downstream placeholders,
original-frame matching, submission and natural pixels remain separate gates;
pending-caller statements below describe this note's historical checkpoint.

## Decision

Continue the connected Game recovery identified in
[Note 973](973-game-palette-updater-and-connected-color-qualification-20261004.md)
after the remaining Init fitting work. Replace `func_1510B7B4`'s zero-return
placeholder in `generated_138520.c` with the complete SDK graphics command
helper. Its interface is `Gfx *(Gfx *, s32)`; the slot is not narrowed to the
signed halfword used by the pending renderer.

The production C body is **103 words / 412 bytes** in the original **105-word /
420-byte** slot at `0x1510B7B4`, followed by two padding NOPs. It remains
non-matching at **104 raw aligned word positions**. No frame, calls, expected-word
guards, profile override, ownership change or address drift are introduced.
The complete linked slot SHA-256 is
`3f8226f75dae50f3e03d73ed53ac6f6bedabbe5b831946646c59856150c4247a`.

README aggregates do not change: the placeholder was already counted as C,
and this is not a new byte match. The complete 356-word renderer
`func_1510B9D0` remains a placeholder, not a completed renderer milestone.

## Command And Read Contract

The helper emits twelve eight-byte packets and returns the cursor advanced
by 96 bytes. The retail reference is ROM offset `0x138C64`, all 105 words.

| Packet | Command / payload |
| --- | --- |
| 1 | `E7000000 / 0`: pipe sync |
| 2 | `F9000000 / 1`: blend color |
| 3 | `DA380003 / D_80089470`: modelview load, no push |
| 4 | `DB0E0000 / u16`: normalize from `D_800BE628 + slot*0x180 + 0xB8` |
| 5..8 | Clip ratio 3: offsets `4/C/14/1C`, payloads `3/3/FFFD/FFFD` |
| 9 | `D9EFFFFF / 0`: clear `G_LOD`, not `G_FOG` |
| 10 | `DA380007 / base + slot*0x180 + page*0x40 + 0x100`: projection load |
| 11 | `DA380005 / D_800DC2A0[page] + slot*0x40`: projection multiply |
| 12 | `EF082C3F / 00552230`: other mode |

Retain the two separate base reads and the two separate page-byte reads.
Output alias fixtures demonstrate that intervening packet stores can change
the later base, page or matrix-table value. In the late-page case, the second
read observes 128 after the projection payload overwrites the initially zero
selector. A cached-page mutation produces a different packet and is rejected.
This artificial alias case is model-only, not ordinary native page-128 usage.
No new NULL, slot or page guards are invented.

## Qualification

New `tools/tests/test_game_viewport_command_helper.py` uses the actual production
helper, SDK macros and actual color emitter. An isolated IDO O2/g3 compile
reproduces the production body without compiler warnings; fixture `SUBALIGN(4)`
preserves the production entry placement. The bounded instruction oracle is a
local subclass of the existing queue oracle, not a general emulator change.

- **65,600 native cases**: every unsigned normalization value (65,536), four
  slots/two pages/seven normalization boundaries (56), and eight actual
  helper-to-color cursor connections.
- **97 complete paired traces**: 56 ordinary, eight low-word wrapping index
  cases, 32 output aliases, and one instruction-coverage trace.
- **Three invalid slot/page prefixes** stop at the mapped-read fence with the
  same prior stores and reads. They are not complete invalid-input acceptance.
- Complete mapped memory, ordered reads/stores and return cursors agree.
  All 103 C body words and 105 retail words execute; padding is not credited.
- Four output-fence controls reject unowned or wrong-width stores. A cached
  selector control rejects the changed late-read behavior.

The receipt `conker/build/game-viewport-command-helper-qualification.json` is an
ignored artifact. Its complete-module flag requires all twelve successful
test methods as well as the exact case counts; partial selections cannot
claim completion. The final combined run passes **81 tests in 19.953 seconds,
no skips**:

```sh
python3 -m unittest tools.tests.test_game_viewport_command_helper tools.tests.test_game_palette_updater tools.tests.test_game_queued_segment_writer tools.tests.test_game_dual_matrix_emitter tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_startup_thread_contract -q -f
```

Final production source compile, padding, link and progress generation pass:

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
```

Complete existing Init code/data, Debugger code and Game data remain retail-exact.
Matching counts remain total 3283/5463, Init 492/492, Game 2610/4790 and Debugger
181/181, with zero address drift. Existing owner functions are not edited;
their retained padding/guard checks pass the fresh owner build. No separate
historical-owner binary comparison is claimed.

These are finite native and low-word trace results, not FCSR, hardware, complete
renderer ordering, actual submission or pixel acceptance. Native pointer-overflow
equivalence is not inferred from the wrapping model cases.

## Init And Next

Init remains **492 C / 47 ASM**. Seventeen entries are investigation targets;
thirty intentionally retain assembly. The latest bitmap view fits nineteen
body words but differs at seventeen positions and has 80-byte aligned text
([Note 981](981-init-bitmap-record-view-fitting-and-ordered-read-qualification-20261005.md)).
MMIO's full eleven-word match is unresolved. The qualified decoder remains
4496 executable bytes versus 3984 retail, 512 over, with original entry/frame,
placement and private-stack reservation gates open. The formatter connection
remains 196 bytes over. No Init owner is converted in this checkpoint.

Read-only sibling audit finds the full original `func_1510B7B4` in
`64CBFDOGL/recomp_out/.c` at line 816590, through its original return at
`0x1510B950`, including existing gated `CONKER_CH18TABLE` diagnostics. The scoped
host `src`/CMake search finds no named override. Existing body presence is not
fresh PC acceptance. No sibling source, build, save or frozen Release changes.

- [x] Recover and qualify the complete initial command helper.
- [x] Preserve repeated reads, unsigned normalization and twelve-packet cursor.
- [x] Fresh-build the production owner and pass all 81 combined checks.
- [ ] Recover complete `func_1510B9D0`, including its signed-halfword slot,
  light/updater/callback ordering and returned display-list cursor.
- [ ] Qualify complete render submission and natural RSP/RDP effects separately.
- [ ] Pursue raw helper matching without broad instruction guards.

No push, ROM promotion or broad goal-completion claim.
