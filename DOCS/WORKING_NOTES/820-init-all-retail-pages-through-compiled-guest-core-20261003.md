# Init All Retail Pages Through Compiled Guest Core

Date: 2026-10-03. Baseline: `efe7861`.

## Result

The new corpus test freshly compiles and links the same six IDO images used
in Note 819: frame baseline, aligned/end and packed/remaining shapes, each
at O2/g3 and O1. It runs all 507 SHA1-verified retail pages through each
compiled core, with compiled fixed-table initialization before every call.
The terminal receipt confirms 3,042 passing core runs and 3,042 passing
initializer runs. The exhaustive test passes in 3,062.499 seconds.

| Measurement | Bytes |
| --- | ---: |
| Maximum workspace write span | 3,564 |
| Maximum observed input read extent | 3,057 |
| Maximum rounded DMA input span | 3,072 |
| Private workspace capacity | 4,096 |
| Private output capacity | 65,536 |

Every page/image read extent stays within that page's supplied DMA span.
These maxima do not establish original caller allocation ownership.

The input ROM SHA1 is `4cbadd3c4e0729dec46af64ad018050eada4f47a`.
Each page is independently decoded by raw zlib and compared with the pristine
image at `0x2D4B0 + page * 0x1000`. A retained-assembly core call supplies
the expected state, frame and workspace writes for each page.

## Addresses And Checks

The input, workspace and caller-SP addresses are `0x80033330`, `0x800340E8`
and `0x80032A10`. The fixture owns 4 KiB of workspace and 64 KiB of output
at `0x80050000`; these are private test allocations, not recovered hardware
allocation ownership. Workspace/output capacities are now explicit instead
of deriving the output extent from the input address.

Actual ROM bytes fill each input's rounded 16-byte DMA span. Sixteen extra
mapped padding bytes allow instrumentation to detect lookahead; acceptance
still requires every observed input read to stay within the rounded span.
The supplied DMA bytes must remain unchanged.

Checks cover output and its untouched tail, all ten state words, the complete
scratch prefix through `0xA44`, the union of retail and guest workspace
writes, fixed-table bytes, saved O32 registers, per-image direct-call stack
bounds, read-only image sections and surrounding guards. Explicit entry
visits confirm that the compiled core and stream paths ran.

## Remaining Conversion Gates

A fresh structured read of `conker/progress.init.csv` confirms 492 C / 539
functions, 151,796 C bytes, and 47 assembly rows / 12,252 bytes. This
checkpoint does not regenerate or change those counts.

| Remaining group | Rows | Bytes | Decision |
| --- | ---: | ---: | --- |
| Bitmap and MMIO | 2 | 120 | C behavior characterized; exact compiler bodies still open |
| Original SDK assembly | 19 | 2,288 | Retain original owners |
| Boot entry | 1 | 80 | Retain clear-and-jump assembly contract |
| Hardware/context/setup | 8 | 4,376 | Assembly/intrinsics and connected ABI work required |
| Shared-frame decompressor | 10 | 3,984 | Qualify compiled C, then original ABI and fitting layout |
| SDK thread queue leaves | 2 | 96 | C-expressible algorithms, but original SDK assembly owns retail slots |
| Cleanup/debug/glyph | 5 | 1,308 | Recover interior entries and live-register/link contracts first |
| Total | 47 | 12,252 | No new production conversion |

See [Note 801](801-init-post-pause-assembly-conversion-assessment-20261003.md)
for inventory evidence and small-candidate matching boundaries.

This is bounded compiler-instruction execution, not R4300 hardware execution,
DMA/cache qualification or the original shared-register/FPR entry ABI.
No candidate code, compiler profile, production assembly owner or README
aggregate changes. The smallest candidate remains 4,160 bytes against the
3,984-byte retail region, before original-entry adapters.

After corpus acceptance, original-entry/context adapters and size/stack fitting
remain independent requirements before production conversion. The two small
ordinary C candidates remain bitmap `func_10005BE0` and ordered MMIO
`func_100038E0`; neither has a proven additional byte-exact C replacement.

## Next Steps

- [x] Execute freshly linked IDO builder and connected stream/core vectors.
- [x] Qualify explicit buffer capacities with focused regressions and a
  final-source representative retail-page replay.
- [x] Reach the terminal all-507-page, six-image corpus receipt.
- [ ] Recover and test original-entry adapters, including live-register and
  full-width FR=1 context/save restoration contracts.
- [ ] Establish actual caller allocation and nested stack ownership; private
  fixture capacities and O32 frame bounds are not that proof.
- [ ] Fit code and adapters into the 3,984-byte retail region while preserving
  required public/interior entries and connected call contracts.
- [ ] Change production ownership only after fitting and ABI gates pass, then
  rebuild, independently compare complete sections and refresh progress tables.

## Verification

- Full corpus: one exhaustive test passes in 3,062.499 seconds, with 507
  retained core reference calls, 3,042 compiled core runs and 3,042 compiled
  fixed initializations across six freshly compiled/linked images.

- All 83 focused guest builder/stream, retained/native decoder, frame, guest
  call and slot-ledger regression tests pass in 84.382 seconds.
- A separate final-source representative-page test passes in 13.843 seconds:
  pages 0, 169 and 506 through six fresh images (18 additional core and fixed
  initialization runs).
- Root `make tools-check`, final two Python syntax checks and `git diff --check`
  pass. No production build or full all-project suite rerun is claimed.

The first regression run exposed guard initialization overwriting the default
builder's root/width cells immediately after its workspace. Guard seeding now
preserves already initialized cells with `setdefault`; the complete focused
regression rerun passes. The long corpus process had already loaded the earlier
seeding code. That code seeds exactly the same bytes for the isolated retail
workspace, whose guards do not overlap root/width cells; the final-source
representative replay separately verifies that layout. The all-page receipt
must not be described as a fresh rerun after this fixture correction.

```sh
python3 -m unittest tools.tests.test_init_decompressor_guest_retail_pages -v -f
```
