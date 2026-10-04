# Init Distance Operation Local Fitting

Date: 2026-10-04. Starting HEAD: `5629e192`.

## Retained Change

After the distance-table lookup, retain `ENTRY_OPERATION(entry)` in the existing
`operation` local for both the invalid-entry test and subsequent extra-bit
extraction. Previously the latter read occurred after `drop_bits`. Keep this
behind opt-in `--distance-operation-local` / `INIT_DECODE_DISTANCE_OPERATION_LOCAL`,
with a distinct default output-directory suffix. Production assembly is unchanged.

The candidate relies on table storage being distinct from decoder state and
unchanged during compressed decoding. `drop_bits` updates reservoir/bits, not
table entries. This is not a general equivalence claim for deliberately aliased
state/workspace objects, concurrent mutation or volatile table observations.
Invalid entry 99 still returns before dropping bits; bit widths, values,
output copying and ABI publications retain their existing logic.

## Fresh Fitting

Use the same complete packed-remaining pointer-owned dynamic-order configuration
as Notes 904-906, including the retained 176-byte adapter.

| Configuration | O2 core / compressed words / core call bound | O1 core / compressed words / core call bound |
| --- | --- | --- |
| Qualified dynamic-order baseline | 4352 / 121 / 400 | 5808 / 158 / 360 |
| Distance operation local | 4336 / 119 / 400 | 5808 / 157 / 360 |

O2 also reduces the core public unit from 53 to 51 words. O1's core grows
88 to 89 words, cancelling the compressed unit's one-word saving. Compressed
frames remain 64/O2 and 56/O1. This is a complete O2 text saving, not a
universal improvement or a byte-exact retail match.

Bounded linked receipts:

| Shape/profile | Linked executable text | Static / observed descent |
| --- | ---: | ---: |
| Frame O2/g3 | 5504 | 3240 / 3240 |
| Frame O1 | 5984 | 3176 / 3176 |
| Aligned end O2/g3 | 4528 | 3240 / 3240 |
| Aligned end O1 | 5968 | 3200 / 3200 |
| Packed remaining O2/g3 | 4512 | 3248 / 3248 |
| Packed remaining O1 | 5984 | 3208 / 3208 |

Packed O2 saves sixteen linked executable bytes and remains **528 bytes over**
retail 3984. Both packed profiles' next read-only section begins immediately
at code end; alignment does not absorb the saving. Packed O2 minimum SP remains
`0x80031D60`, with 80-byte known-neighbor margin, not proven reservation ownership.

## Fresh Qualification

```sh
python3 -m unittest tools.tests.test_init_decompressor_distance_operation_local -v -f
python3 -m unittest tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_backreference_table_storage_is_stable_during_decode -v -f
```

The initial module run completed 46 tests in 332.532 seconds: 45 passes and
one deliberate full-corpus skip. It inherited dynamic initialization, semantic
and error cases, alias-sensitive adapter poison checks, ordered ABI/FPR loads,
callee receipt controls, live-SP write fences, nested lookup, representative
retail pages and both masked CU1 paths. Candidate source/compiler flags stayed
fixed throughout. No full 507-page corpus was run for the changed candidate.

The additional table-stability test was added after that process loaded its
module and run separately: one pass in 4.515 seconds. Across six compiled images
and both masked CU1 modes, a fixed compressed stream produces 96 output bytes
through actual backreferences. The test asserts compressed-entry visits and
distance-source ABI publications, checks state/workspace separation and rejects
workspace writes after compressed entry. A direct injected write exercises the
guard's rejecting path; this is a fixture control, not an injected MIPS instruction.
These checks establish the assumption for those executions, not all possible
aliased or externally mutated inputs.

Twenty supporting slot-ledger, guest call-graph and storage-boundary tests
pass in 0.292 seconds, no skips. Project tool checks and whitespace checks pass.

Option-omitted packed O2/O1 builds have extracted `.text` byte-identical to
the freshly measured pre-edit baseline (4352/5808 bytes). Receipts remain under
ignored `conker/build/init-distance-operation-{packed-baseline,packed-trial,default-check}-20261004/`.
An earlier diagnostic build omitted the packed shape's cache/cursor flags;
it is not the baseline used above.

## Candidate Hashes

SHA-256, recorded for subsequent changed-candidate corpus qualification:

| File | SHA-256 |
| --- | --- |
| `init_decompressor_semantic.c` | `43A3897FE734E8000F4C156CDB3DB69722D25A210B5B518C02EA315BD71CA0C2` |
| `init_decompressor_core_adapter.s` | `A8D2642E81EA3960B0A9CFABDF61BDB04F2F3A951D7E8B2251228B5FE9DC72CB` |
| `compile_init_decompressor.py` | `E5792E1FDB2A12A7273A0BE3B91BD67E557801CBC6EA54896F9A7926BCBA3506` |
| `test_init_decompressor_distance_operation_local.py` | `1280377B35F3582B29A2D7FDC4F28A7237E7CF3F9BFBEA35093458A05275BAFD` |
| `test_init_decompressor_live_stack_writes.py` | `0760CACC7BC4FD78C19E63D6D0B48B0195E2B7AF342B7CDE7E2139C22642616C` |
| `test_init_decompressor_shadow_corpus.py` | `F9ADF06BEC8B674F78FAE7E7FAFA4D79DF62FA575F96A58A78543F90D3828663` |

## Next

- [x] Measure complete packed text and call bounds in both profiles.
- [x] Preserve option-omitted baseline text exactly.
- [x] Pass bounded inherited qualification and executed backreference storage gate.
- [x] Full guarded masked CU1-clear corpus: [Note 912](912-init-distance-operation-o2-full-masked-cu1-clear-corpus-20261004.md).
- [ ] Run matching full guarded masked CU1-set corpus for this changed candidate.
- [ ] Reduce remaining 528-byte fitting excess.
- [ ] Prove full reservation, entry/frame ownership and hardware/context behavior.
- [ ] Only then consider production ownership, full link and aggregate refresh.

Notes 905/906 remain full-corpus evidence for the option-omitted candidate only.
Production source, Init totals, README, word guards, sibling artifacts and Release
are unchanged. Existing Game and actor/timeline work remains unstaged.
