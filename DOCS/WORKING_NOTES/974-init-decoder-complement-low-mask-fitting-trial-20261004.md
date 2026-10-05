# Init Decoder Complemented Low-Mask Fitting Trial

Date: 2026-10-04. Starting HEAD: `36b67c92`.

Subsequent [Note 975](975-init-builder-byte-depth-induction-and-rejected-replication-helpers-20261004.md)
qualifies a separate opt-in byte-depth counter: packed executable is sixteen
bytes smaller in both profiles, optimized 4496 / 512 excess. The default
candidate and this neutral-mask result remain unchanged.

## Result

Continue the requested Init conversion work beyond the inventory recheck in
[Note 971](971-init-pause-resume-remaining-assembly-decision-20261004.md).
A new shared low-mask expression changes two instructions but saves no bytes.
The complete optimized candidate remains **4512 executable bytes against 3984
retail, 528 over**. No production adoption is justified.

The initially considered bitmap fill-value reuse was already rejected in
[Note 910](910-init-bitmap-shared-fill-mask-lifetime-trials-20261004.md).
Unsigned-address induction is also an existing byte-identical control. Their
combination is not presented as a new fitting result. The new experiment below
instead changes the connected decoder's shared mask helper.

## Hypothesis

The opt-in `--complement-low-mask` flag selects
`~(~0u << (width & 31))` instead of `(1u << (width & 31)) - 1`.
The unsigned identity preserves every masked shift class, including zero and
high input-width bits. It introduces no table, extra data owner, changed caller
interface, memory access or adapter. The default expression is unchanged.

IDO emits a load of minus one and NOR in place of a load of one and decrement.
The O2 helper remains six words, frameless, with an empty return delay slot;
O1 remains five words, with NOR in that slot. The rest of each packed control's
instruction image is unchanged. This is a mask code-generation experiment,
not evidence that a mask expression alone can close the decoder's fitting gap.

## Fresh Measurements

Both profiles use the retained packed-remaining configuration, ABI shadow,
pointer-owned core, first-refill lookup and distance-operation capture from
[Note 967](967-init-decoder-entry-value-lifetime-fitting-trials-20261004.md).
The entry-value option stays disabled. Every executable total below counts the
actual 176-byte adapter.

| Profile / shape | C text | With adapter | Core direct-call frame bound | Compressed words / frame |
| --- | ---: | ---: | ---: | ---: |
| O2/g3 control | 4336 | 4512 | 400 | 119 / 64 |
| O2/g3 complemented mask | 4336 | 4512 | 400 | 119 / 64 |
| O1 control | 5808 | 5984 | 360 | 157 / 56 |
| O1 complemented mask | 5808 | 5984 | 360 | 157 / 56 |

The optimized dynamic body remains 247 words / 112-byte frame; O1 remains
313 / 120. Core body/allocation remains 50 / 51 optimized words and 86 / 89 O1
words. No savings have been moved into alignment, wrappers or uncounted helpers.

Complete object `.text` SHA-256 receipts:

```text
O2 control    177d7344426bb233f32c0cfbc92f40e533e2f344889f473bee0540e7bafeb62d
O2 complement 1a46899a4c4786bd5cadfc045db1c4cf441171b7668d98b994615dd3e5268908
O1 control    8797fe0eef6f346ea9a90a36e0206b76f648ec3dd5026c7a7f1f6b75d2fb6755
O1 complement 6d4d93e097d117490215bc54ca85d85718ce05595c559b4ccb4df31f52518691
```

Only object word indices 1 and 3 change in O2, and 1 and 4 in O1. The second
O1 change is the return delay slot. Objects/logs/disassembly and qualification
receipts live under ignored `conker/build/init-complement-low-mask-20261004/`.

## Qualification

**59 distinct trial tests pass across two invocations, no skips:** the initial
58-test connected/native run in 319.659 seconds, followed by the new complete
ledger assertion in 2.002 seconds. Twenty separate inventory/slot-ledger/call-
graph checks pass in 0.849 seconds, no skips: 79 distinct passing checks in
this turn. Project tool and whitespace checks pass. The prior turn's 110-test
inventory assessment is not added to this count.

The new test module recompiles and links all three retained shapes in both
profiles with the actual adapter. It exercises the changed compiled mask across
all 32 shift classes and high width bits, and checks the disabled packed control
against its banked instruction hashes. Connected and native tests use the
existing decoder contract fixtures rather than a replacement decoder model.
The direct mask test runs 259 widths across six compiled images: 1554 bounded
instruction cases with no memory accesses and preserved callee registers.
Packed O2 conservative/observed total stack descent remains 3248 bytes; O1 is
3208. This does not prove private-stack reservation in the actual game.

```sh
python3 -m unittest tools.tests.test_init_decompressor_complement_low_mask -q -f
python3 -m unittest tools.tests.test_init_decompressor_complement_low_mask.InitDecompressorComplementLowMaskTests.test_complete_packed_ledger_counts_helpers_and_adapter -q -f
python3 -m unittest tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_guest_calls -q -f
make tools-check
```

The fresh optimized ledger counts 1029 named-region words plus 55 outside-region
helper words, totaling 1084 C words versus 996 retail. That is 352 excess C
bytes plus the 176-byte adapter: exactly 528 bytes excess. The builder region's
401 words comprise a 333-word public unit and 22-/46-word embedded helpers.
Its 108-word regional excess must not be called 108 builder-body words; the
public unit itself is 40 words over its 293-word retail budget. Prior smaller
compressed/dynamic/stored units already offset part of this excess.

Next sustained Init fitting should address **builder/shared-call structure**
with complete allocation accounting, rather than repeat this neutral mask
identity. An arithmetic substitution that does not reduce allocation cannot
close the connected conversion gate.

## Adoption Boundary

- [x] Measure both complete allocations and actual adapter costs.
- [x] Attribute the entire packed instruction change to two mask words.
- [x] Reject adoption because the complete optimized size does not shrink.
- [x] Finish connected/native qualification and restored-default verification.
- [ ] Reduce the complete decoder image by at least 528 bytes.
- [ ] Prove private-stack reservation and entry/frame/placement ownership.
- [ ] Rerun both full guarded CU1 corpora after an adoptable candidate change.

No production Init owner, word guard, compiler override or README aggregate
changes. The prior turn's three documentation edits are included in this Init
checkpoint. No production relink, full guarded corpus, hardware/gameplay proof,
sibling source/build, frozen Release change, save change, ROM promotion or push
is claimed. The opt-in source and test are retained only as fitting evidence.
