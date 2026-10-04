# Init Bitmap Exit-Edge Control-Flow Trials

Date: 2026-10-04. Starting HEAD: `940ec4ee`.

## Hypothesis And Scope

Following [Note 943](943-init-resume-linked-baseline-and-conversion-shortlist-20261004.md),
test whether eliminating the cursor increment on the exit edge lets IDO emit
the direct endpoint branch without the old-cursor XOR temporary. Both new
opt-in shapes use unsigned address induction with guest 32-bit width asserted:

- Shape 14: loop while cursor differs from end, then perform the final store
  outside the loop.
- Shape 15: jump to the shared store/compare block initially; subsequent taken
  back edges execute the cursor increment before reentering that block.

Unlike the postincrement control, these void trials leave the local cursor at
end, not end plus one. Neither publishes that local or claims a recovered
return signature. Preserve captured start/end, volatile byte-store ordering,
the signed count reload after filling and the original partial-byte mask.
Unsigned arithmetic retains the fixture's modulo-32-bit address domain;
native host tests do not prove that guest wrapping behavior.

The existing driver accepts shapes 14/15 explicitly. Its no-argument selection
remains shapes 1..11. Production Init source, profiles and ownership are untouched.

## Fresh Compiler Measurements

Each object is independently linked at `0x10005BE0` with the retail global
addresses. The complete body through its return delay slot is compared with
all nineteen pristine retail words. Alignment nops after the body are excluded
from body length, not counted as spare bytes inside the retail slot.

Each cell is **body words / differing aligned positions / frame bytes**:

| Shape | O2/g3 | O2/g3 no-unroll | O1 |
| --- | ---: | ---: | ---: |
| 1, postincrement control | 20 / 19 / 0 | 20 / 19 / 0 | 31 / 31 / 16 |
| 14, separate final store | 34 / 33 / 0 | 22 / 21 / 0 | 35 / 35 / 16 |
| 15, taken-edge increment | 20 / 19 / 0 | 20 / 19 / 0 | 32 / 32 / 16 |

Shape 14 enables unrolling under ordinary O2. Disabling unrolling leaves an
initial endpoint gate and separate final store; it is still three words over
the retail slot. Shape 15 removes the XOR, but replaces that cost with an
unconditional entry jump. Its O2 loop is:

```text
10005BF0: b     10005BFC
10005BF4: li    a0,255          ; entry jump delay slot
10005BF8: addiu v0,v0,1
10005BFC: bne   v0,v1,10005BF8
10005C00: sb    a0,0(v0)        ; conditional branch delay slot
```

Retail instead stores first, branches directly to that store, then increments
in the branch delay slot. Shape 15's opening four words and entire eleven-word
mask/return tail are byte-identical to the freshly compiled shape-1 control;
only the five-word loop/setup span changes. Eliminating XOR alone does not
explain the nineteen-word routine. No profile matches the complete function.

## Actual Guest-Fixture Qualification

New `tools/tests/test_init_bitmap_exit_edge.py` runs the established trace,
alias, wrap, stack and rejecting controls on **the six new compiled images**,
not the earlier unsigned-induction images. The retail control is checked
against the pristine ROM before paired execution.

- 77 count/endpoint fixtures, repeated twice per image: 924 completed pairs.
- Five start/end/count storage aliases per image: 30 completed pairs.
- Eight wrapping-address fixtures per image: 48 completed pairs.
- Two reversed-endpoint cases per image: twelve bounded sixteen-store prefixes.

Total: **1,002 completed retail/C pairs plus twelve bounded prefixes** for the
new shapes. Qualification compares interleaved external reads/writes including
values and widths, external memory, callee-saved registers and SP. O1's private
stack cells are excluded from external trace/memory comparison; observed frame
descent must match the emitted sixteen bytes. Stores are fenced to the fixture
output bytes. Reversed ranges stop before the seventeenth store; this is not a
complete 2^32-byte termination proof or a safe real-hardware address domain.

The inherited count-hoist mutant and out-of-output write controls still reject
incorrect behavior. These validate the oracle/fence gates, not the correctness
of every possible input or any real MMIO/guest gameplay behavior.

The three warning-clean native executables each pass 79 fixtures: 237 host
shape/case combinations, 158 belonging to the new shapes. No return-value
checks are credited to these void trials.

## Reproduction

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py --shapes 1 14 15
python3 -m unittest tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract -q -f
```

Eight new tests pass independently in 6.863 seconds. After strengthening the
fresh-control tail comparison, **54 combined tests pass in 7.815 seconds, no
skips**. The combined run separately reruns the original unsigned-induction
corpus; its 1,002 pairs/twelve prefixes are distinct from the new trial receipt.
Generated objects, disassembly and `exit-edge-qualification.json` remain under
ignored `conker/build/init-bitmap-ordered/`. `measurements.json` is overwritten
by each selected-shape run; reproduce the desired selection before using it.
`make tools-check` and `git diff --check` also pass.

## Decision And Next Action

- [x] Test both new exit-edge hypotheses with a freshly compiled control.
- [x] Qualify complete external trace and bounded alias/wrap behavior.
- [x] Reject both as production fitting improvements; retain original assembly.
- [ ] A new explanation for the complete retail loop, mask and allocation
  schedule, not merely the absence of XOR or a shorter source loop.

Init remains 492 C / 47 assembly entries. README totals are unchanged. This
is an experiment checkpoint, not a new production conversion. The current
production Init image was verified in Note 943; it was not rebuilt here.
Decoder and connected glyph fitting/ownership gates are unchanged.

For concrete production recovery under the broader decomp goal, the pending
Game `func_150E81A8` placeholder remains the next actionable semantic target.
Do not rerun these exit-edge shapes unchanged as another matching attempt.
No word guards, full decoder corpus, hardware execution, sibling build,
Release change, compressed-ROM promotion or push is claimed.
