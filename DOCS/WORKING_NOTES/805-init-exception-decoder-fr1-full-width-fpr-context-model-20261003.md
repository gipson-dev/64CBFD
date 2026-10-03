# Init Exception Decoder FR1 Full-Width FPR Context Model

Date: 2026-10-03. Baseline: `445554f`.

## Result

The retained exception wrapper now has a connected, bounded FR=1 context model.
It executes its actual words at `0x10005E1C..0x10006018`, including the shared
decoder core, and stops before cache/TLB processing at `0x1000601C`.
This advances the adapter contract but is not hardware execution, an adapter,
or a fitting production C replacement. Production assembly and aggregates stay
unchanged; unrelated pending Game edits are preserved.

## Architecture Boundary

The primary [NEC VR4300 user manual](https://hack64.net/docs/VR43XX.pdf),
printed pages 595-596 and 603-604, specifies that FR=1 `MTC1` defines the
destination's low word but leaves the upper word undefined. FR=1 doubleword
transfers address a whole FPR; FR=0 odd-register doubleword stores are undefined.
The fixture therefore tracks each upper word separately, marks it unknown on
`MTC1`, and restores known full-width values only on doubleword reload.
It explicitly rejects FR=0, disabled-CU1 COP1 accesses, unaligned doubleword
transfers and attempts to save an unknown upper word. It does not invent an
upper-half preservation rule or emulate pipeline timing.

Startup `conker/src/init_1050.c` sets `SR_CU1 | SR_FR`; that source observation
does not prove every interrupted runtime context has the same Status.

## Connected Evidence

`tools/tests/test_init_decompressor_exception.py` extends the existing low-word
core fixture. Fixed tables are bootstrapped independently, then registers and
memory are seeded for the actual wrapper. A new optional `stop_pc` in the shared
runner permits stopping at a real boundary without inserting synthetic return
instructions or replacing retained words. The default runner is unchanged.

- CU1 clear: the wrapper enables CU1, stores sixteen 64-bit FPR values
  (`f0..f11`, `f16..f19`), executes the decoder, reloads those values, and restores
  the original Status. All 32 seeded FPR values are unchanged afterward.
- CU1 set: it stores no FPR values. The ordinary BNE at `0x10005F40` still
  executes `ldc1 f0,0(sp)` at `0x10005F44`. Two distinct explicitly seeded stale
  slots produce two distinct final `f0` values; the slot is not written by this
  bounded call. Decoder-written FPR upper halves remain unknown.
- Successful stored and dynamic streams produce `XY` and `A`. Reserved-block
  and dynamic-repeat-overflow failures return zero at the core boundary with
  no output writes; both CU1 branches restore the tested GPR/Status/SP context.
- Core entry arguments are input `0x80033330`, synthetic output page
  `0x80050000`, and workspace `0x800340E8`. Entry SP is `0x80032A10`; modeled
  minimum SP is `0x80031F88`. Interrupted SP is published at `0x80032B18` and
  restored by the final wrapper load.
- Low-word GPR values are preserved except `a0`, which is replaced before its
  save and reused for the final interrupted-SP load. Full 64-bit GPR ownership
  is not modeled; do not infer it from word saves/loads.
- The complete 512-byte wrapper interval is compared directly with the local
  pristine decompressed image. The model uses its actual branch-delay words.

This does not establish the source of the real stale slot or call the retail
behavior a defect. Seeding is explicit test input, not a runtime observation.
CP0 Status moves are architectural-value assignments only. DMA, caches, address
translation, hazards, FCR31, HI/LO, nested exceptions and the later TLB/cache
tail are outside this fixture. Workspace and exception-stack allocation
ownership remain separate obligations.

## Verification

- Seven initial behavioral tests pass (1.057 seconds).
- All 105 Init tests before the final wrapper-byte receipt pass (40.076 seconds).
- All 581 project tool tests, including the final eight-test exception module,
  pass (97.565 seconds). The Init subset now contains 106 tests.
- Root `make tools-check` passes. The earlier `make -C conker tools-check`
  invocation had no such target; it was rerun from the correct root.
- `git diff --check` passes.

## Next

Qualify the complete adapter clobber contract and stack/workspace ownership.
Any adapter must preserve the retained conditional save behavior, defined
low-word state, and unconditional delay load unless an explicitly non-matching
behavioral change is separately authorized. The overlong C text and nested C
frames are still unresolved. Do not substitute this host-model evidence for
guest execution or count it as a new Init conversion.
