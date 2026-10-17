# Sequence Record Setup Installed Guarded Match

Date: 2026-10-17. Completes the installation gates from
[Note 1467](1467-sequence-record-setup-certified-guarded-match-qualification-20261016.md).

## Installed Result

`func_1501D348` in `conker/src/game/generated_49D30.c` now contains the
complete semantic record-group setup instead of a zero-return placeholder.
The recovered interface is
`void(s32 scene, s32 sequence, s32 slot, s32 hook, s32 parameter)`.
The function occupies **473 words / 1,892 bytes**, frame **0x78**,
VA **0x1501D348..0x1501DAAC**, ROM **0x4A7F8..0x4AF5C**.

All linked words are retail-exact. This is **guarded matching, not direct
compiler matching**: the complete raw C emits 474 words. The certified
165-row append contains 164 replacements and one omitted cursor-scale word,
with no insertions. Note 1467 owns the all-CFG cursor-one/scratch-role proof;
no guard repairs the frame, argument homes or nonvolatile register roles.
Keep the established O2/g3/no-unroll owner profile unchanged.

Preserve all previous guard bytes, including **298 CRLF lines**. The only
other production edits are precise five-word void declarations in
`game_34F20.c` and `generated_20AE20.c`. All **56 raw/padded setup-owner
neighbors**, **six raw/padded early-caller functions**, and **60 raw/padded
scene-caller functions** remain unchanged. Their existing diagnostic output
is unchanged; the early caller owner retains two pointer/integer warnings.

## Actual Callers And Helpers

The new connected tests execute the original, raw C and guarded setup with
six actual installed, independently ROM-exact helpers:

| Helper | Words | Role |
| --- | ---: | --- |
| func_1501D044 | 100 | Slot/shared reset |
| func_150233BC | 10 | Actor-table clear wrapper |
| func_1501D1D4 | 33 | Resource loader and slot publication |
| func_1501CFF8 | 19 | Preferred-entry sum |
| func_1501CDC0 | 37 | Per-record 16-byte clear |
| func_1501CE54 | 105 | Preferred/override/fallback maximum |

**480 three-way cases** cover both slots and stack phases, zero/one/three
records, load failure, status variants, hooks and signed maximum paths.
All **304 helper words** execute across the corpus. Compare public memory,
all allocation records and top-level physical call packets to an independent
sum/clear/maximum reference. Four effective mutations detect skipped reset,
record clear or maximum and an off-by-one sum.

Execute the complete **29-word func_150082CC** in **48 original/guarded
cases** and complete **50-word func_151E83E8** in **96 original/guarded
cases**. The latter includes its trailing padding, zero/nonzero started
gate, same/different scene, elapsed threshold, both stack phases and actual
post-call request packet. The threshold's `D_800D2E40` clear is one byte.
Unrelated menu providers remain bounded, not recovered by these tests.

Audit all **nine original assembly call sites** across 49D30, 20AE20, C98F0
and CDE80. **36 positively fired ABI cuts** check all five arguments and
delay slots using explicit pre-window register fixtures. Assembly comment
words are checked against the pristine ROM. These are actual call windows,
not full execution of the larger assembly callers.

Allocation, SDK bzero, the loader's seven-argument resource service and the
remaining setup providers are bounded contracts. This is not DMA, allocator,
hardware, menu presentation or full-game acceptance. Preserve Note 1467's
valid-array, allocation, alias and fault-equivalence limits.

## First Image And Validation

Before editing production inputs, reproduce the complete predecessor ELF
from captured link inputs, then link the qualified setup and both typed
callers. Independently predict the complete image by replacing the exact
retail slot, changing only its symbol size **12 -> 1,892**, and applying
seven explicitly pinned symbol-order groups. Membership, order, definitions
and string extents are checked; no metadata range is excluded.

The first predicted and normally rebuilt ELF are byte-identical:
**6f52c4154a4aca1cdecdbb5a0043d1332b89c4a928b6cb7d96354a19e43cf458**.
Of **1,637 changed ELF bytes**, **1,468** are in the target code slot,
**two** are its extent, and **167** are exact symbol/string serialization.
All other canonical symbol definitions remain unchanged.

Installed source owner:
**8de78d8035bd112e32b9bcd54425b86f6e7323bef06cefe686abc56f3f10fb80**.
Guard manifest:
**bb20ecd3785ed2e3fe949d7c9a4bfa8f6648b78e5f9eb1712af941c38faf415b**.
The two caller source hashes and all five before/after fixture pairs are
pinned in `tools/tests/sequence_record_setup_checkpoint.py`.

The normal `all` rebuild completed **694 compiler and 686 padder commands**
in its retained log, linked the ELF and emitted the binary. The final whole
binary retail checksum still fails because the overall project is not fully
matching. An earlier default-target invocation rebuilt one additional owner;
it is not used as proof of a complete build. The explicit development command
`make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1` passes.
Existing compiler and duplicate-recipe warnings remain.

All **25 final tests pass in 325.866s**: eight setup matching tests, five
connected tests, three installation tests and nine predecessor reset,
maximum and microcode-loader installed checks. Note 1467's complete native32
O2/O0/UBSan, symbolic controls, rebases and 417 fault-prefix tests are rerun.
The new exact-successor audit protects **140 inputs / 135 unchanged inputs**,
including every metadata definition and all five fixture pairs. Protected
Game data remains **189,088 bytes / 720 owners / zero differences**.

## Progress And Bank

Fresh official measurements: Game **2,940/4,828 (60.89%)**, total
**3,613/5,501 (65.68%)**, still different **1,888**, zero address drift.
Init remains **492/492**, Debugger **181/181**. Conversion remains
**5,501/6,044 functions / 86.04% bytes**; the old placeholder already counted
as C. Regenerated conversion CSV bytes are unchanged. Root README updates
only the verification date and two aggregate matching rows.

Tools **987e90b** banks seven files before the consumer pin. Both copies
have identical task pairs and **14 ASCII/AST checks**. All eleven WSL padder
tests pass per copy: active **0.030s + 0.020s**, mirror **0.029s + 0.019s**;
consumer tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **964 unrelated initial
dirty-file hashes**, and its independent history. Three existing task files
are updated exactly and four files added: **971 final dirty paths**. No
mirror commit/reset, push, Claude call, dependency/configuration change,
host-port build/launch or frozen Release action.

Prepared-checkout reproduction, sequentially:

```sh
python3 -m tools.experiments.game_sequence_record_setup_installation
make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1
python3 -m unittest tools.tests.test_game_sequence_record_setup_match \
  tools.tests.test_game_sequence_record_setup_connected \
  tools.tests.test_game_sequence_record_setup_installed \
  tools.tests.test_game_sequence_state_reset_installed \
  tools.tests.test_game_record_maximum_installed \
  tools.tests.test_game_microcode_loader_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Verify both typed callers, all nine original assembly call packets and the actual six-helper chain.
- [x] Reproduce the predecessor and freeze the first complete ELF/source/caller/guard prediction before installation.
- [x] Install only the selected qualified C, precise caller declarations and certified guard append.
- [x] Complete normal rebuild, 25 passing tests, complete image/input/metadata/data audit and fresh progress.
- [x] Update aggregate README status, concise indexes and roadmap checkboxes; bank tools first.

Next: **func_1501DAAC**, still a zero-return stub in the same owner:
**219 words / 876 bytes**, frame **0x80**, VA **0x1501DAAC..0x1501DE18**,
ROM **0x4AF5C..0x4B2C8**. It is the newly installed setup's final provider;
its internals were not accepted by the bounded provider checks above.
Recover and qualify its full body before crediting another match. Timing's
**141 differences**, wider Game/additional-source matching and full gameplay
acceptance remain separately open.
