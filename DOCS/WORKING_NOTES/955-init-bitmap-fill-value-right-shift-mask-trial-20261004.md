# Init Bitmap Fill-Value Right-Shift Mask Trial

Date: 2026-10-04. Starting HEAD: `9a5214d6`.

## Hypothesis And Result

Test a new `func_10005BE0` value-lifetime shape, separate from production.
Shape 19 reuses the unsigned fill value `0xFF` for the final low-bit mask:

```c
unsigned int value = 0xFF;
do {
    *(volatile u8 *)cursor = value;
} while (cursor++ != end);
bits = D_8003BE78 & 7;
if (bits) {
    value >>= 8 - bits;
    *(volatile u8 *)end = value;
}
```

Cursor and endpoint are captured unsigned addresses, checked as 32-bit O32
guest values. The count is still read after filling. For nonzero remainders
1..7, `0xFF >> (8 - bits)` is the same low-bit mask as retail's
`(2 << (bits - 1)) - 1`; zero remainder still skips the final mask store.
No return value, count hoist, clamp or changed termination rule is introduced.

| IDO profile | Body words | Different aligned positions | Frame bytes |
| --- | ---: | ---: | ---: |
| O2/g3 | 20 | 20 | 0 |
| O2/g3, no unroll | 20 | 20 | 0 |
| O1 | 33 | 33 | 24 |

Retail is nineteen words. IDO retains the loop's XOR comparison and
rematerializes `0xFF` in a different register after the count load. The mask
uses a subtraction from eight and logical variable right shift. Reusing one
source variable does not produce one machine-register lifetime. Reject this
shape without changing production ownership or adding instruction guards.

Older one-based-mask trials did fit nineteen words without matching retail;
see [Note 751](751-init-bitmap-loop-mask-profile-trials-20261002.md).
Size is only one adoption gate. This new shape fails both fitting and matching,
and does not supersede those earlier results.

## Fresh Qualification

Eight new tests in `tools/tests/test_init_bitmap_fill_value_mask.py` execute
the three freshly compiled guest images through the existing bounded oracle.
They verify external read/write order, final memory, captured start/end
aliases, post-fill count aliases, all remainder classes, signed counts,
allocator counts, repeat calls, wrapping addresses and reversed-range prefixes.
Output fences and a hoisted-count mutant demonstrate rejection paths.
Required callee registers, restored SP and measured frame descent are checked.

The new receipt records **501 completed retail/C pairs and six bounded prefix
pairs**, with all 79 host cases passing for each profile. These are bounded
model-address-domain checks, not hardware or whole-game acceptance.
Compiler logs are empty. Artifacts and the shape-specific receipt stay under
ignored `conker/build/init-bitmap-ordered/`.

```sh
python3 tools/experiments/compile_init_bitmap_ordered.py --shapes 19
python3 -m unittest tools.tests.test_init_bitmap_fill_value_mask tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_mmio_assembly -q -f
```

All **34 combined tests pass in 3.446 seconds, no skips**. Existing retained
Init owners/slots, full linked Init code/data and Game data remain retail-exact.
The existing ELF predates the two dirty Game recovery files; this is not a
successful dirty-source production rebuild.

## Next Work

- [x] Test the new shared fill-value/right-shift mask hypothesis.
- [x] Qualify bounded alias, wrap, prefix and stack behavior.
- [x] Reject the oversized non-matching body without production changes.
- [ ] Require a new full-slot compiler explanation before another bitmap trial.
- [ ] Resolve decoder/glyph connected fitting and ownership before adoption.
- [ ] Resume the preserved Game child callback's one-word fitting failure,
  then qualify its complete callback chain and fresh production link.

Init remains 492 C / 47 assembly entries. README totals, production Init
profiles/guards and both dirty Game files are unchanged by this experiment.
No sibling/Release change, ROM promotion, runtime acceptance or push.
