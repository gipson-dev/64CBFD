# Init Dynamic Shared Repeat Extraction And Stack Fitting

Date: 2026-10-03. Baseline: `35f51d78`.

## Result

Opt-in `--dynamic-shared-repeats` selects the dynamic code-length repeat
width before one shared `take_bits` call. After extraction, the repeat base
is `3 + ((symbol > 17) << 3)`: three for codes 16/17, eleven otherwise.
The preceding literal branch establishes symbol >= 16; the otherwise branch
continues to include any larger stale symbol, as in the original candidate.
The original three separate extraction branches remain the default.

All three O2 shapes save eight bytes of call-stack descent. All three O1
shapes grow eight bytes. Aligned O2 saves 16 linked bytes; other linked
totals remain unchanged. Best packed O2 remains 4,800 bytes, 816 over the
3,984-byte retail decoder group. This is an isolated structural-fitting
checkpoint, not a production conversion or a byte-exact claim.

## Trial Accounting

Packed trials include all retained Note 851 flags:

| Trial | O2 core bytes / bound | O1 core bytes / bound |
| --- | ---: | ---: |
| Note 851 baseline | 4,480 / 408 | 5,888 / 344 |
| Builder sorting length cursor, rejected | 4,480 / not qualified | 5,904 / not qualified |
| Shared repeat width and live base, rejected | 4,480 / 432 | 5,904 / 352 |
| Shared width, conditional base after call, rejected | 4,480 / 400 | 5,888 / 352 |
| Shared width, arithmetic base after call, retained | 4,480 / 400 | 5,888 / 352 |
| Arithmetic width and base, rejected | 4,480 / 416 | 5,856 / 344 |

The live-base trial enlarged the O2 frame. Arithmetic width saved O1 text
but enlarged the O2 stack bound; it is removed. Only the arithmetic-base
boolean option remains. Rejected forms have size evidence, not semantic
qualification. Ignored receipts are under `conker/build/init-builder-sort-cursor-*`
and `init-dynamic-shared-repeats-*`, suffixed `-20261003`.

Packed O2 dynamic body shrinks 263 to 261 words, frame 112 to 104;
final padding absorbs the two saved words. Packed O1 dynamic body stays
319 words, frame grows 104 to 112. A fresh omitted-option build reproduces
4,480/408 and 5,888/344 core text/bounds; it is not a new default corpus run.

## Qualified Costs

State remains 116 bytes; adapter assembly remains 320 bytes. Static total
descent includes the physical 0xA88 frame, 0x98 adapter area and call bound.

| Shape/profile | Linked bytes | Static total bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 6,032 | 3,272 | 3,272 |
| Frame O1 | 6,400 | 3,208 | 3,208 |
| Aligned/end O2/g3 | 4,816 | 3,232 | 3,232 |
| Aligned/end O1 | 6,192 | 3,184 | 3,184 |
| Packed/remaining O2/g3 | 4,800 | 3,248 | 3,248 |
| Packed/remaining O1 | 6,208 | 3,200 | 3,200 |

For packed O2 the static minimum SP is `0x80031D60`, 80 bytes above the
known protected neighbor ending `0x80031D10`. This is a bounded fence,
not complete stack-reservation ownership or hardware/resume proof.

## Active Repeat Gates

A constructed zlib-valid stream emits `A`. Its code-length alphabet
includes 0/1/16/17/18. It builds 65 zeros, literal A, 190 zeros, EOB and one
distance length. Three variants replace the final distance length with
repeat 16, 17 or 18, each exceeding the one remaining destination slot.

All four streams are paired against retail in six builds and both masked
CU1 modes: 48 additional comparisons, bringing the bounded stream/context
domain to 492. The valid case produces `A`; each overflow returns failure
with no output and matching retail state. The isolated gate passes in
20.023 seconds.

Separate executions in all six builds prove the shared extractor is active:
the dynamic routine has exactly three calls to its opening extractor target
(header, code alphabet, repeat). At the repeat callee entry, after the JAL
delay slot, the argument sequence is 2,3,7,7,7, with one additional 2/3/7
for each respective overflow. The probe checks the callee's first executed
instruction and the exact caller return address, not only a PC visit.

Inherited tests retain 114 direct builders, six exact initializers and
48 direct all-alignment/header-format comparisons, plus nested lookup,
byte rewind, packed layout rejection and stored-complement restoration.

Final verification:

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_dynamic_shared_repeats
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger
wsl make tools-check
git diff --check
```

Final module: 24 tests in 235.180 seconds, 23 pass and one intentional
full-corpus skip. All thirteen call-analysis/slot-ledger tests pass in
0.034 seconds: 36 passed, one skip across the final commands. Compiler/linker
logs are empty; tool and diff checks pass. No production build, ordinary
full-suite, new full corpus, hardware replay or sibling-port test is claimed.

## Next

- [x] Remove sorting-cursor and inferior repeat dataflow trials.
- [x] Qualify active codes 16/17/18 and each overflow against retail.
- [x] Rerun the complete bounded module and record all six observed stack costs.
- [ ] Continue structural fitting; best O2 remains 816 bytes over retail.
- [ ] Changed full corpus in both masked CU1 modes before promotion.
- [ ] Other-profile corpus and complete ownership/hardware/resume gates.

The opt-in corpus class is `InitDecompressorDynamicSharedRepeatsCorpusTests`
in `tools.tests.test_init_decompressor_dynamic_shared_repeats`; it is not run
here. No older corpus receipt is reassigned. Production Init, adapter,
default flags and README aggregates remain unchanged. Unrelated Game work
is preserved and excluded from this checkpoint.
