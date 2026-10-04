# Init Dynamic Order Cursor Text Stack Tradeoff

Date: 2026-10-04. Starting HEAD: `d65a4ce6`.

## Hypothesis And Trials

The dynamic header initializer indexes the nineteen-byte code-length order
table for transmitted lengths and zero fill. Walk that permutation through a
pointer cursor, preserving the three-bit read order and exactly nineteen
staging writes. This initializer, rather than the already-tried decoded-length
cursor or fixed-table endpoints, is the new fitting target.

Three isolated packed trials use Note 900's complete pointer-owned configuration:

| Shape | O2 core text / dynamic words / frame / core call bound | O1 core text / dynamic words / frame / core call bound |
| --- | --- | --- |
| Qualified indexed baseline | 4384 / 256 / 104 / 392 | 5792 / 311 / 112 / 352 |
| Order cursor with transmitted endpoint | 4352 / 247 / 112 / 400 | 5824 / 316 / 120 / 360 |
| Order cursor retaining index count | 4368 / 251 / 120 / 408 | 5808 / 315 / 120 / 360 |
| Order cursor with transmitted countdown | 4352 / 247 / 112 / 400 | 5808 / 313 / 120 / 360 |

Keep only the countdown form, behind opt-in `--dynamic-order-cursor` /
`INIT_DECODE_DYNAMIC_ORDER_CURSOR`. Default indexed code is unchanged.
The option receives its own output-directory suffix. It is a text/stack
tradeoff for O2, not a universally better profile or production replacement.

The four-bit header field plus four gives transmitted count 4..19. Therefore
the countdown's do-loop is nonempty and cannot decrement from zero. It ends
with the order pointer at the first untransmitted entry; the remaining loop
zeros through the end of the same permutation. The consumed local transmitted
count is not subsequently exported or used. Existing decoded-length cursor
and ABI publication behavior remain unchanged.

Ignored trial receipts under `conker/build/`:
`init-dynamic-order-{cursor,counted,countdown}-trial-20261004/`.
These were measured before the retained opt-in gate was added.

## Guarded Qualification

```sh
python3 -m unittest tools.tests.test_init_decompressor_dynamic_order_cursor -v -f
```

Whole bounded suite: 46 tests in 334.687 seconds, 45 passes and one deliberate
full-corpus skip. Candidate source/flags stayed fixed during that run. The
fixture inherits pointer-owned input/fifth-slot checks, live-SP write fencing,
callee-return guards, ordered FR=1 loads and semantic/error/storage cases.

The new initializer test executes all sixteen transmitted counts across six
compiled images and both masked CU1 modes: 192 prefix runs. It stops at the
first compiled builder entry, asserts the dynamic routine was visited and
builder count is nineteen, and checks every staging write's address, value,
size and order. This is initializer-prefix evidence, not valid full-stream
qualification for those synthetic code alphabets. Existing bounded tests cover
complete valid streams, repeat codes and failures.

| Shape/profile | Linked executable text | Static / observed descent |
| --- | ---: | ---: |
| Frame O2/g3 | 5504 | 3240 / 3240 |
| Frame O1 | 5984 | 3176 / 3176 |
| Aligned end O2/g3 | 4544 | 3240 / 3240 |
| Aligned end O1 | 5968 | 3200 / 3200 |
| Packed remaining O2/g3 | 4528 | 3248 / 3248 |
| Packed remaining O1 | 5984 | 3208 / 3208 |

Packed O2 saves 32 executable bytes from the qualified 4560-byte baseline,
leaving 544 bytes above retail 3984. Packed O1 grows sixteen bytes. Packed
descent grows eight bytes in both profiles. O2 minimum SP is `0x80031D60`,
80 bytes above known neighbor end `0x80031D10`; O1 minimum SP is `0x80031D88`,
margin 120. These clearances and write-only fencing are not full reservation
ownership or absence-of-below-SP-read proofs.

After the whole run, the size test additionally asserts that the next read-only
section starts directly at code end for both packed profiles. That updated
test and thirteen call-graph/slot-ledger tests pass separately in 1.847 seconds,
no skips. Alignment does not absorb the executable saving; no production
ROM placement claim is made.

## Default Preservation

Fresh packed builds with the new option omitted produce extracted `.text`
identical to the prior pointer-owned trial objects: 4384 O2 / 5792 O1 bytes.
Receipt: `conker/build/init-dynamic-order-default-check-20261004/`.
Assembler and physical adapter allocation are unchanged. Project tool and
whitespace checks pass. No native whole-suite or production rebuild claimed.

## Next

- [x] Measure initializer endpoint/index/countdown variants.
- [x] Keep countdown as an opt-in O2 fitting tradeoff; preserve default text.
- [x] Pass full bounded suite, all-count initializer gate and alignment check.
- [ ] Full guarded corpora for changed candidate across both masked CU1 modes.
- [ ] Reduce fitting excess and prove reservation, entry/frame ownership and hardware/context.

Notes 901/902 remain full-corpus evidence only for the option-omitted baseline.
Production Init remains 492 C / 47 assembly functions. Production sources,
README totals, word guards, sibling-port artifacts and unrelated Game edits
remain unchanged. No ROM or hardware run is claimed.
