# Init Bitmap Return Value Lifetime Trials

Date: 2026-10-04. Starting HEAD: `d47dcc68`.

## Hypothesis

Retail `func_10005BE0` leaves the inclusive end plus one in `v0` after its
complete nineteen-word leaf. Notes 751/799 used void candidates. Test whether
making that result explicit keeps the cursor live and allows IDO to reproduce
the retail compare-before-delay-increment loop. This is a new return-lifetime
hypothesis, not another unchanged loop/profile matrix or a recovered signature.

Extend the isolated Note 799 tool with two shapes using its volatile byte
stores and postincrement comparison:

- Shape 4 returns the advanced cursor.
- Shape 5 returns the captured end plus one.

Neither changes a production declaration, owner, compiler setting or guard.

## Reproduction And Measurements

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py
```

The driver runs warning-clean host builds, then IDO O2/g3 and O1 compiles.
Each guest object is independently linked at `0x10005BE0`, with retail global
addresses. Extracted words through the return delay slot are compared to
pristine ROM `0x5BE0..0x5C2C`, excluding section alignment nops.
Receipts remain under ignored `conker/build/init-bitmap-ordered/`.

| Shape | O2/g3 body words / differing positions | O1 body words / differing positions |
| --- | ---: | ---: |
| 1: void postincrement control | 20 / 19 | 31 / 31 |
| 2: void saved-comparison control | 20 / 19 | 34 / 34 |
| 3: void break-loop control | 20 / 19 | 32 / 32 |
| 4: return advanced cursor | 21 / 20 | 32 / 32 |
| 5: return captured end + 1 | 21 / 20 | 33 / 33 |

The three controls reproduce Note 799. Both new O2 forms retain the XOR
comparison temporary, cursor increment before the conditional branch and
byte store in its delay slot. Shape 4 adds `move v0,v1` before return; Shape 5
adds `addiu v0,v1,1`. Retail has no final move/increment: its original cursor
already stays in `v0`, and its branch delay slot advances that register.
Explicit return-value liveness therefore does not explain the missing shape.
No instruction normalization or production conversion is justified.

## Behavior And Verification

All five actual host candidates pass 79 cases each, including repeated calls
for 77 endpoint/count cases and two global-alias cases: 395 shape/case
combinations total, of which 158 belong to the new shapes. Shapes 4/5 also
check the returned end-plus-one pointer on each call. The driver exposes
`host_return_checked` so void controls are not credited with return checks.
Counts include 1..64, zero with an explicit valid endpoint, four signed
negative values, seven retail counts and 32,767. Every buffer byte and guard
is checked, along with post-fill count reload and captured endpoint behavior.

These are native C tests and guest code-generation comparisons, not execution
of the new guest binaries or general invalid-pointer/wraparound proof.
They do not establish that callers use a return value.

Thirty-three focused retained bitmap, allocator, MMIO, slot-ledger and
storage-boundary tests pass in 9.913 seconds, no skips. Project tool and
whitespace checks pass. The qualified decompressor sources remain unchanged.

```sh
python3 -m unittest tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_mmio_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries -v -f
make tools-check
git diff --check
```

## Decision

- [x] Test cursor-return and endpoint-return lifetime hypotheses with controls.
- [x] Reject both as production matching conversions; preserve retail owner.
- [ ] A distinct compiler/dataflow explanation for this leaf's nineteen words.
- [ ] Continue qualified decompressor fitting and production ownership gates.

Init remains 492 C / 47 assembly functions. No production ROM, README totals,
sibling-port artifact or unrelated Game work changes. No hardware/gameplay
test or production signature recovery is claimed.
