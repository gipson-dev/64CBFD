# Init Core-Owned State Initialization And Adapter Fitting

Date: 2026-10-03. Baseline: `4f9972a`.

## Result

The isolated adapter accepts assembler symbol `INIT_DECODE_CORE_OWNS_STATE=1`
to omit six redundant state stores. This turn qualifies that option only
with the FPR-shadow adapter and the Note 852 C flags. Default assembly is
unchanged: a fresh object compares byte-for-byte equal to the object assembled
from the previous committed source, with the same assembler flags.

The adapter body shrinks 320 to 296 bytes. Its object text is 304 bytes
after alignment, so all six linked images save 16 bytes. Smallest packed
O2 linked text is now 4,784, still 800 above the 3,984-byte retail group.
Stack depth and the 116-byte state / 0x98 extra adapter area do not change.
This is an experimental fitting improvement, not production conversion.

## Initialization Ownership

| State byte offset | Field | Initialization before first use |
| --- | --- | --- |
| 12 | Reservoir | Stream writes zero before taking the block header |
| 16 | Buffered bits | Stream writes zero before taking the block header |
| 20 | Produced count | Stream writes zero before dispatch |
| 24 | Output limit | Core writes default and applies distance bounds before stream |
| 28 | Allocated entries | Stream writes zero before each block dispatch |
| 36 | Workspace address | Core writes the fifth argument before stream |

Adapter stores for input, output, workspace and physical-frame pointer remain.
The fifth C argument at stack offset 0x10 remains. All register save/restore,
FPR restoration, return handling and stack allocation instructions remain.
Omitted stores were at adapter offsets 0x2C/30/34/38/3C/44.

## Poison And Read-Before-Write Gate

`CoreOwnedStateFixture` seeds each omitted field with a distinct nonzero
`0xCCFF0000 + offset` poison after fixture setup. A guest read overlapping
any field fails until an executed four-byte write initializes that field.
The check covers actual guest memory accesses, including delay-slot execution.
All inherited paired stream/context comparisons use this fixture.

A direct negative gate attempts to read each poisoned field and confirms
the checker raises. It also inspects the poison bytes directly, confirms
the adapter contains none of the six stores, then executes an empty valid
stored stream and verifies all six fields were initialized by the C path.
This gate passes across six builds in 3.354 seconds.

This proves initialization-before-read within the bounded guest oracle.
It does not prove asynchronous equivalence of intermediate adapter-state
memory, cache/bus behavior, hardware exceptions or complete stack ownership.
The extra state area is experimental; changing its write timing is not
assigned a broader hardware/context qualification.

## Linked Costs

| Shape/profile | Linked bytes | Static total bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 6,016 | 3,272 | 3,272 |
| Frame O1 | 6,384 | 3,208 | 3,208 |
| Aligned/end O2/g3 | 4,800 | 3,232 | 3,232 |
| Aligned/end O1 | 6,176 | 3,184 | 3,184 |
| Packed/remaining O2/g3 | 4,784 | 3,248 | 3,248 |
| Packed/remaining O1 | 6,192 | 3,200 | 3,200 |

Packed O2 static minimum SP remains `0x80031D60`, 80 bytes above the known
protected neighbor ending `0x80031D10`. The saved text bytes do not reduce
the state size, physical frame or stack descent.

Ignored receipts include `core-owned-adapter.o`, `default-adapter-check.o`
and `previous-adapter-check.o` under
`conker/build/init-dynamic-shared-repeats-arithmetic-20261003`. Six persistent
`*-core-owned.elf` links reuse unchanged Note 852 C objects under its
frame/aligned/arithmetic directories; the tests compile all six C images
freshly and link the new adapter independently.

## Final Verification

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_core_owned_state
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger
wsl python3 -m unittest tools.tests.test_init_decompressor_dynamic_shared_repeats.InitDecompressorDynamicSharedRepeatsTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_dynamic_shared_repeats.InitDecompressorDynamicSharedRepeatsTests.test_repeat_widths_and_each_overflow_path
wsl make tools-check
git diff --check
```

Poisoned-state module: 25 tests in 252.436 seconds, 24 pass and one
intentional full-corpus skip. All 492 bounded stream/context comparisons
pass with initialization-before-read checks; inherited 114 builders, six
exact initializers and 48 direct header/alignment comparisons also pass.
Repeat/overflow, nested lookup and byte-rewind gates remain active.

Thirteen call-analysis/slot-ledger tests pass in 0.031 seconds. Two selected
default-adapter regression tests pass in 20.335 seconds. Across these final
commands, 39 pass and one skips. Compiler/linker logs are empty. Tool and
diff checks pass. No production build, ordinary full-suite, new full corpus,
hardware replay or sibling-port test is claimed.

## Next

- [x] Remove redundant adapter stores behind an opt-in assembler symbol.
- [x] Prove poison rejection and actual C initialization of all six fields.
- [x] Confirm default adapter object remains byte-identical.
- [x] Rerun the complete bounded module and record all six observed stack costs.
- [ ] Continue structural fitting; best O2 excess is 800 bytes.
- [ ] Changed full corpus in both masked CU1 modes before promotion.
- [ ] Other-profile corpus and remaining ownership/hardware/resume gates.

Opt-in corpus class: `InitDecompressorCoreOwnedStateCorpusTests` in
`tools.tests.test_init_decompressor_core_owned_state`. It selects both
Note 852 C flags and the new assembler symbol, with the poisoned-state
fixture. It is not run here. Older corpus receipts are not reassigned.
Production Init, default flags and README totals remain unchanged;
unrelated Game work is preserved and excluded.
