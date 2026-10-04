# Init Connected Semantic C Formatters And Layout Cost

Date: 2026-10-04. Starting HEAD: `96186928`.

## Recovered Trial Bodies

`tools/experiments/init_glyph_formatters_semantic.c` recovers both formatters
as ordinary-ABI semantic C trials, calling Note 931's selected C pixel writer
directly instead of using Note 932's per-glyph adapter. The source preserves
ordered volatile destination-pointer reads, conditional null exits, position
addressing, low-nibble-first right-to-left hex rendering, signed-byte string
mapping, and late string reads after each glyph call.

The trial interface returns a success flag and writes cursor/string state
to caller-owned result cells only on success. These cells let a future
formatter-level adapter reconstruct the nonstandard retail outputs; they are
not framebuffer writes or a claim of original ordinary-C return semantics.
Null destinations leave result cells untouched, and a null first destination
prevents reading the second cell, as in retail's interior setup.

## Independent Linked Measurements

Each formatter object is linked with the selected 29-word frameless O2
pixel writer. Both formatter profiles are warning-clean:

| Formatter profile | Hex body words | String body words | Writer body words | Allocated text | Observed nested stack |
| --- | ---: | ---: | ---: | ---: | ---: |
| O2/g3 no-unroll | 59 | 63 | 29 | **624 bytes** | 48 bytes |
| O1 | 65 | 77 | 29 | **704 bytes** | 48 bytes |

Original hex/string/writer slots consume 80 + 100 + 120 = 300 bytes;
interior setup consumes another 112 bytes after the twelve-byte public
cleanup prefix, for a **412-byte connected comparison budget**. O2 is still
212 allocated bytes over that budget, before any formatter-level adapter.
This is an aggregate comparison, not permission to overwrite the cleanup
interior entry, move its public prefix or merge independently referenced slots.

Experimental images are linked at 0x10009000, which Note 933 confirms is
occupied production code. They are fixture images only. Allocated counts
include function/object padding: O2 slots are 59 / 65 / 32 words, while O1
slots are 65 / 79 / 32. Reported body counts end at the last return delay slot.
Real entry/slot ownership and the 48-byte frame reservation remain open.

## Differential Qualification

`tools/tests/test_init_glyph_formatter_semantic.py` executes the retail
setup/formatters/writer and each compiled connected C image. It checks full
interleaved external read/write addresses, widths, values and order;
complete non-private memory; cursor/string-pointer results; success/null
behavior; ordinary ABI callee registers and restored SP/return link.

Each profile runs twenty hex position/value cases, all 255 nonzero signed
bytes, three empty/multicharacter strings, four output/string alias cases and
six null-buffer cases: **288 paired fixtures per profile / 576 total**.
Alias cases place initial string bytes in the first output row so earlier
glyph stores modify later reads; the compiled C and retail observe the same
mutations. Fixture private frames/result cells are explicitly excluded from
external trace/memory equality. Maximum observed nested descent is 48 bytes
for both profiles, with the selected frameless writer.

```sh
python3 -m unittest tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
```

Four new / fifteen combined tests pass in 25.053 seconds, no skips. The
initial isolated four-test receipt was 14.477 seconds. Measurements, images
and stack receipts regenerate under ignored
`conker/build/init-glyph-formatters-semantic/`.

Qualification is bounded to tested mapped/aligned addresses and nonoverflowing
retail signed position/displacement arithmetic. Trial unsigned arithmetic
does not reproduce arbitrary retail ADDI/SUB overflow exceptions. Physical
hardware, actual allocation lifetimes, arbitrary alias geometry and public
cleanup execution are unqualified. No fresh production rebuild is claimed.

## Decision And Next Work

Retain the connected C recovery and differential tests. Replacing the
per-glyph adapter with full C formatters does **not** solve text fitting in
these two profiles. Further connected fitting needs a new measured source
hypothesis, such as shared destination setup, while preserving volatile
access order, character/cursor state and alias timing. Any new candidate must
rerun the connected fixtures, count complete allocated text plus adapter cost,
and address all fifteen diagnostic callers' stack regimes before adoption.

Production Init remains 492 C / 47 assembly routines. No production owner,
profile, guard or README aggregate changes; no sibling build, Release change
or push. This is connected semantic recovery, not a production conversion.
