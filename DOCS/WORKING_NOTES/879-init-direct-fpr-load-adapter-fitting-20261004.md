# Init Direct FPR Load Adapter Fitting

Date: 2026-10-04. Baseline: `e5511c66` (Notes 873/875/877/878).

## Change And Scope

The experimental adapter accepts `INIT_DECODE_DIRECT_FPR_LOADS=1`.
Its sixteen stack-word publications use one `lwc1` each instead of
`lw $t0` followed by `mtc1`. The dirty-snapshot branch, physical saved
callee cells, core-owned state, RA restoration and stack layout are unchanged.
The default macro expansion retains the original two-instruction form.
Assembled default `.text` compares byte-for-byte equal to HEAD with all
three existing selected adapter symbols; `cmp` exits zero.

The [NEC VR4300 User's Manual](https://hack64.net/docs/VR43XX.pdf#page=592)
describes both LWC1 and MTC1 as defining the low word with an undefined
upper word in FR=1 (printed pages 592-593 and 596). LWC1 requires word
alignment. This justifies architectural-value modeling, not hardware timing
or scheduler qualification. The changed intermediate T0 value is not asserted
equal at adapter return; required final GPR context remains compared.

## Oracle

The shared FR=1 transfer model now recognizes opcode 49, rejects CU1-disabled
and unaligned accesses, sign-extends the address offset, reads four bytes,
marks the upper half unknown and records a separate `fpr_word_loads` trace.
Existing doubleword transfer receipts are not weakened or reclassified.
A focused test checks the low-word value/mask, signed negative offset,
read extent, unchanged GPRs, transfer trace and rejection boundaries.

`test_init_decompressor_direct_fpr_adapter.py` inherits the existing
first-refill/callee-preserving bounded suite and poison/callee-return guards.
It asserts exactly sixteen LWC1 instructions and no MTC1 in each adapter.
Both masked CU1 modes exercise clean and dirty publications: four result
loads always, twelve scratch loads only when dirty, in exact address order.
The dedicated corpus class selects the new assembler symbol explicitly.

## Size

Adapter body/aligned text: **192/192 bytes**, versus 256/256 previously.
Core text and stack bounds are unchanged. Packed O2/g3 core is 4,384 bytes,
linked text **4,576**, excess **592** over the 3,984-byte retail decoder.
Packed O1 core is 5,824, linked text 6,016. Both save 64 bytes.

## Verification

Fresh bounded suite: 37 tests run in 254.545 seconds, 36 passed and the
explicit opt-in full corpus skipped. No bounded failures. The executed
callee-clobber negative control is rejected across all six builds.

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_direct_fpr_adapter -v -f
```

| Shape/profile | Linked text | Static descent | Observed descent |
| --- | ---: | ---: | ---: |
| frame/o2g3 | 5,712 | 3,272 | 3,272 |
| frame/o1 | 6,224 | 3,208 | 3,208 |
| aligned-end/o2g3 | 4,608 | 3,232 | 3,232 |
| aligned-end/o1 | 6,016 | 3,192 | 3,192 |
| packed-remaining/o2g3 | 4,576 | 3,240 | 3,240 |
| packed-remaining/o1 | 6,016 | 3,200 | 3,200 |

Shared exception and default compiled-adapter regressions: 11 passed,
31.860 seconds, no skips. The default adapter's expected scratch-FPR gap
test remains a negative control, not a new regression.
Project tool checks and whitespace checks pass.
Together the fresh bounded and regression suites have 47 passes / one skip.
The initial new unit test failed because it had not initialized the shared
contract fixture; an explicit setUpClass fixed setup before the final run.

## Next Gates

- [ ] All 507 direct-load packed O2/g3 masked CU1-clear pages.
- [ ] All 507 matching masked CU1-set pages.
- [ ] Further fitting: linked text is still 592 bytes over retail.
- [ ] Complete entry/frame ownership, stack reservation and hardware/context gates.

Notes 877/878's 1,014 paired pages remain evidence for the old 256-byte
adapter, not this new option. No production assembly is converted here;
production remains 492 C / 47 assembly rows, with 12,252 assembly bytes.
README aggregates and production sources are unchanged. No ROM build,
sibling-port test, hardware acceptance or byte-exact C replacement is claimed.
Unrelated Game source/tests remain preserved and excluded from staging.
