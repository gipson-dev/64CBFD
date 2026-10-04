# Init Rejected Match-Copy Refill Trials And Size Ledger

Date: 2026-10-03. Baseline: `fd8513e9`.

## Result

Four distinct copy/refill dataflow trials do not improve the selected
packed configuration. All temporary source branches and compiler selectors
are removed. Scoped Git diff confirms both experiment source files exactly
match the committed baseline. No smaller implementation is retained here.

A fresh baseline compile reproduces 4,448 core bytes / 392-byte call bound
in O2 and 5,856 / 352 in O1. With the unchanged 304-byte aligned adapter,
best linked text stays 4,752, 768 over retail. New ledger evidence directs
the next fitting work to the builder/shared helpers rather than these loops.
Production, defaults and README totals remain unchanged.

## Measurements

Trials use the complete Note 858 packed/remaining configuration:

| Trial | O2 core bytes / bound | O1 core bytes / bound |
| --- | ---: | ---: |
| Restored baseline | 4,448 / 392 | 5,856 / 352 |
| Match-copy pointer endpoint, rejected | 4,448 / 392 | 5,888 / 352 |
| Match-copy pointer countdown, rejected | 4,464 / 392 | 5,888 / 352 |
| Fully cached refill, rejected | 4,448 / 392 | 5,904 / 352 |
| Count-only cached refill, rejected | 4,448 / 392 | 5,872 / 352 |

Pointer endpoint/countdown compressed bodies are 123/125 words in O2 and
165/168 in O1, versus baseline 121/158. The countdown O1 compressed frame
grows to 72 from the 56-byte baseline (the endpoint trial uses 64), although
the largest overall call-chain bound is unchanged.
Fully cached refill saves one O2 prefix-helper word, but final padding absorbs
it and O1 grows 48 bytes. No rejected variant has semantic qualification;
compiler size evidence alone was sufficient to reject all four.

Ignored receipts, objects, logs and disassembly:

- `conker/build/init-match-copy-cursor-20261003`
- `conker/build/init-match-copy-countdown-20261003`
- `conker/build/init-cached-bit-refill-20261003`
- `conker/build/init-cached-bit-count-20261003`
- `conker/build/init-copy-refill-baseline-check-20261003`

## Trial Source Forms

The copy trials replaced only the final indexed match loop, after the
existing limit check and ABI shadow updates. They still copied forward one
byte at a time; no memcpy/memmove or backward-copy assumption was introduced.

```c
uint8_t *destination = s->output + produced;
const uint8_t *copySource = s->output + source;
uint8_t *copyEnd = s->output + end;
while (destination != copyEnd) *destination++ = *copySource++;
produced = end;
```

The countdown form removed `copyEnd` and substituted
`while (length--) *destination++ = *copySource++;`. Neither form was accepted
as semantically qualified; caching the output base also needs a separated
state/output domain argument, not a general alias-equivalence claim.

The fully cached `need_bits` body was:

```c
int32_t bits = s->bits;
if (bits < width) {
    const uint8_t *input = s->input;
    uint32_t reservoir = s->reservoir;
    do {
        reservoir |= (uint32_t)*input++ << (bits & 31);
        bits += 8;
    } while (bits < width);
    s->input = input;
    s->reservoir = reservoir;
    s->bits = bits;
}
```

The count-only form retained original input/reservoir accesses inside
`while (bits < width)` and committed `s->bits = bits` after the loop.
It adds a count store even when no refill occurs. Both change intermediate
state-store timing; no asynchronous, alias or hardware equivalence is claimed.
The original refill and match-copy forms are restored exactly.

## Fresh Core Ledger

The restored O2 object reports these word counts:

| C function region | Retail slot | C region | Public unit | Region delta |
| --- | ---: | ---: | ---: | ---: |
| Core | 52 | 54 | 54 | +2 |
| Stream | 62 | 79 | 79 | +17 |
| Dynamic | 257 | 256 | 256 | -1 |
| Stored | 65 | 54 | 54 | -11 |
| Builder | 293 | 415 | 343 | +122 |
| Compressed | 167 | 121 | 121 | -46 |
| Fixed initializer | 77 | 78 | 78 | +1 |

The builder region includes a 22-word ABI-capture helper and 50-word lookup
helper: 343 + 22 + 50 = 415. Its 122-word region excess must not be described
as 122 builder-body words. The public builder alone exceeds its retail slot
by 50 words / 200 bytes; its embedded helpers occupy 72 words / 288 bytes.
These are layout accounting, not proof those bytes can simply be removed.

Other outside-region helpers occupy 55 words. Retail's two wrapper slots
account for 23 words, with no separate C entries. Core total is 1,112 words
versus retail 996: 116 words / 464 bytes excess. The adapter adds 76 aligned
words / 304 bytes, giving 192 words / 768 bytes overall excess. This avoids
double-counting embedded helpers or omitting retail wrappers.

## Verification And Next

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_dynamic_repeat_fill.InitDecompressorDynamicRepeatFillTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_dynamic_repeat_fill.InitDecompressorDynamicRepeatFillTests.test_ordered_repeat_lengths_include_nonzero_previous_and_extremes
wsl make tools-check
git diff --check
```

All fifteen selected tests pass in 10.066 seconds, with no skips. This is
focused restored-baseline verification, not a fresh whole bounded suite or
full corpus. Tool/diff checks pass; compiler logs are empty. No production
build, hardware replay or sibling-port test is claimed.

- [x] Measure and remove all four inferior dataflow trials.
- [x] Recompile the restored baseline and pass focused size/ordered-fill gates.
- [x] Account for builder body, embedded helpers, outside helpers and wrappers separately.
- [ ] Continue builder/shared-call structural fitting; best excess remains 768 bytes.
- [ ] Changed Note 858 full corpus in both masked CU1 modes before promotion.
- [ ] Other-profile and complete ownership/hardware/resume gates.

Notes 856/857 remain full-corpus receipts for the older no-repeat-fill-option
combination. Unrelated Game work is preserved and excluded; no trial option
or source change survives this checkpoint.
