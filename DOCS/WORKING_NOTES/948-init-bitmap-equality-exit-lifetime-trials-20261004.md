# Init Bitmap Equality-Exit Lifetime Trials

Date: 2026-10-04. Starting HEAD: `d03f9173`.

## Hypothesis

Following [Note 947](947-init-remaining-assembly-conversion-map-20261004.md),
test whether moving the count reload and final-byte mask into the equality
exit region shortens the captured end pointer's lifetime enough to recover
the direct retail cursor/end branch, without an XOR predicate temporary.

The new opt-in shapes use guest-width unsigned address induction and preserve
captured endpoints, volatile byte stores, post-fill signed count reload and
ordered partial-byte masking:

- Shape 16: after storing `0xFF`, an equal cursor/end exits through the mask
  written to the cursor, which is then known to equal the captured end.
- Shape 17: identical control flow, but the mask uses the captured end pointer.
  This is the address-lifetime control for Shape 16.

Both return void. Neither invents or qualifies an incidental return value.
The non-equality edge increments the cursor and repeats. The count is never
loaded on that edge, including during bounded reversed-endpoint probes.

The shared experiment source/driver now accept Shapes 16/17 explicitly. The
driver's default selection remains Shapes 1..11, and all earlier source shapes
retain their previous behavior. Production ownership is unchanged.

## Fresh Compiler Results

Each candidate is linked independently at `0x10005BE0`, with retail global
addresses and the same retained IDO profiles. All words through the final
return delay slot are included; subsequent object-alignment nops are excluded.
The complete retail slot is nineteen words / 76 bytes.

Each cell is **body words / differing aligned positions / frame bytes**:

| Shape | O2/g3 | O2/g3 no-unroll | O1 |
| --- | ---: | ---: | ---: |
| 16, cursor-address mask | 21 / 20 / 0 | 21 / 20 / 0 | 31 / 31 / 16 |
| 17, captured-end mask | 21 / 19 / 0 | 21 / 19 / 0 | 31 / 31 / 16 |

**Reject both for production.** Optimized bodies remove XOR but are two words
too large. The equal case falls into count/mask handling; the non-equal case
takes a forward branch to a separate unconditional back edge. Masked and
unmasked exits have distinct returns. Shortening the end pointer's lifetime
changes tail registers and the final store base, not the loop footprint.

The optimized shared loop/control tail is:

```text
10005BF4: bne   v0,v1,10005C24
10005BF8: sb    a0,0(v0)       # executes on both equality outcomes
          ... count reload / mask ...
10005C1C: jr    ra
10005C20: sb    t0,0(v0/v1)    # mask through cursor or captured end
10005C24: b     10005BF4
10005C28: addiu v0,v0,1
10005C2C: jr    ra
10005C30: nop
```

Retail's loop is instead `sb; bne cursor,end,loop; addiu cursor,1`, with one
shared return. A direct comparison alone is not sufficient: entry/back-edge
layout, live registers, tail schedule and complete slot extent must match.
No instruction guards were added to force the rejected bodies into the slot.

## Differential Qualification

`tools/tests/test_init_bitmap_equality_exit.py` freshly compiles both shapes
under all three profiles, then executes them against pristine retail through
the established guest fixture. The tests do not reuse old trial images.

Eight new tests pass in 1.936 seconds, no skips. The suite records:

- 1,002 completed retail/C execution pairs across six fresh guest images.
- Twelve paired bounded prefixes for reversed endpoints and wrapped addresses.
- Exact external read/write order, width, address and value agreement.
- Positive, zero and signed-negative count cases, all remainder classes,
  repeated calls, output sentinels and endpoint/count storage aliases.
- Guest 32-bit wrapping in the model, not real hardware execution.
- Preserved callee-saved registers and measured stack descent per profile.
- Rejecting output-fence and hoisted-count-load controls.
- Complete-slot rejection plus assertions for the direct comparison,
  unconditional back edge, two returns and final mask store bases.

The ordinary host fixtures also pass for both source shapes. These checks
qualify bounded memory behavior, not an original-C provenance claim, complete
input-domain proof, hardware acceptance or a production conversion.

The combined equality-exit, prior exit-edge/unsigned, MMIO/bitmap/allocator,
decoder-ledger/storage/startup and connected formatter/adoption/adapter suites
also pass: **78 tests in 58.085 seconds, no skips**. The new suite's 1,002
pairs/twelve prefixes are distinct from the separately rerun earlier receipts.

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py --shapes 16 17
python3 -m unittest tools.tests.test_init_bitmap_equality_exit -v -f
python3 -m unittest tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
```

Ignored receipts are under `conker/build/init-bitmap-ordered/`: linked images,
disassemblies, compiler logs, measurements and `equality-exit-qualification.json`.

## Baseline And Next Step

A fresh independent ELF32 big-endian MIPS extraction compares the existing
production artifact to the pristine ROM after validating its YAML SHA-1.
All 164,048 Init code bytes and 17,376 Init data bytes remain raw retail-exact.
This is an existing-artifact check, not a fresh production rebuild.
`make tools-check` and `git diff --check` pass.

Keep `func_10005BE0` in `conker/asm/init_5AB0.s`. Init remains 492 C / 47
assembly entries, with README aggregates unchanged. The latest small-leaf
assessment and whole-chain decoder/glyph gates remain in Note 947.

Another bitmap attempt needs a compiler/control-flow explanation that recovers
the three-word direct loop without an added entry jump, unconditional back
edge or duplicate returns. Do not repeat these equality-exit shapes unchanged
or confuse XOR removal with full-slot fitting. No remaining Init replacement
is newly ready to adopt. The broader decomp goal also retains the unfinished
Game creator work identified in Note 947 as a separate actionable recovery.

Only opt-in experiment, tests and working docs change. The two existing Game
edits are untouched and excluded from this checkpoint. No source-owner
transition, production profile change, word patch, compressed-ROM promotion,
sibling build, Release modification, hardware/gameplay acceptance or push.
