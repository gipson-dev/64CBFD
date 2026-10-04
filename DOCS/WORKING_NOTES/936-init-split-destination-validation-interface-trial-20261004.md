# Init Split Destination Validation Interface Trial

Date: 2026-10-04. Starting HEAD: `cc197938`.

## New Interface Hypothesis

Note 935's fully shared setup helper saves sixteen linked bytes but grows
nested stack through its two-word state interface. New opt-in
`GLYPH_SPLIT_SETUP` shares only ordered destination-pointer validation and
displacement calculation. It returns the nonzero first destination on
success, with displacement in one caller-owned cell; zero indicates either
null destination. Cursor arithmetic remains in each formatter.

Returning the first destination avoids treating a calculated cursor value
of zero as a null-buffer failure. The first-pointer null gate still prevents
the second-pointer read, and no displacement/result state is published on
failure. Default independent setup and the prior fully shared trial remain
unchanged and are compiled as controls.

## Measured Text And Stack

All variants use the same selected 29-word frameless C writer:

| Formatter variant | Allocated text | Observed nested stack |
| --- | ---: | ---: |
| Independent O2/g3 no-unroll | 624 | 48 |
| Fully shared O2/g3 no-unroll | 608 | 80 |
| Split validation O2/g3 no-unroll | **624** | **64** |
| Independent O1 | 704 | 48 |
| Fully shared O1 | 688 | 56 |
| Split validation O1 | **720** | **56** |

Split O2 body words are helper 17, hex 53, string 54 and writer 29, with
allocated slots 17 / 53 / 54 / 32. Split O1 bodies are helper 22, hex 57,
string 69 and writer 29, with slots 22 / 57 / 69 / 32. Full linked text
includes padding and helper code, not just the public formatter bodies.

The one-cell interface reduces O2 stack relative to the fully shared trial,
but still grows it sixteen bytes over the independent control while saving
no text. Under O1 it adds sixteen linked bytes and eight stack bytes over
that control. Neither split profile dominates the existing control or solves
the 412-byte connected retail comparison budget before adapter costs.

## Qualification

Six variants execute the same 288 paired fixtures each: **1,728 paired
retail/C executions**. Complete interleaved external memory operations,
values, non-private memory, cursor/string results, success/null behavior and
ordinary ABI state match across all variants. Fixtures retain all signed-byte
patterns, twenty hex position/value cases and output/string alias timing.
Helper measurement remains guarded by both formatter first-JAL targets,
because IDO omits the static helper's name from its linked symbol table.

```sh
python3 -m unittest tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
```

All sixteen combined tests pass in 50.604 seconds, no skips. Measurements
and nested stack receipts regenerate under ignored
`conker/build/init-glyph-formatters-semantic/`. The existing linked-footprint
assertions still pin the independent and fully shared controls; split values
above are measured from independently linked images and executed fixtures.
Private trial stack/result cells are explicitly excluded from external
trace/memory equality, not presented as retail writes.

The bounded address/alias/arithmetic and hardware exclusions in Notes 934/935
remain. In particular, the smaller cell interface does not prove real caller
stack ownership or remove Note 933's occupied text-placement restriction.

## Decision And Handoff

Reject split validation as a fitting improvement, retaining it as a
reproducible opt-in experiment. Do not repeat this interface unchanged or
promote either shared setup variant solely for semantic test success.
The Init request has a concrete readiness answer: semantic C recovery exists,
but code fitting, original entry/register contracts and actual ownership still
prevent these assembly conversions. Retain original production assembly.

Resume production decomp work at Game `func_150E76D0`, still the alternate
emitter helper placeholder following the recovered dispatcher/positioned
helper in Notes 924/925. Verify its current source and complete retail body
before editing. This leaves Init experiments available for a genuinely new
fitting/ownership hypothesis rather than repeating the rejected matrices.

Production Init stays 492 C / 47 assembly routines. No production owner,
profile, guard or README aggregate changes. No production build, sibling
artifact change, Release change or push.
