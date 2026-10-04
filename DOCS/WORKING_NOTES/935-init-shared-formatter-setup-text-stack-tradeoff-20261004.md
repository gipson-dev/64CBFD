# Init Shared Formatter Setup Text Stack Tradeoff

Date: 2026-10-04. Starting HEAD: `a8faffee`.

## Hypothesis

Note 934's C formatter trials duplicate destination-pointer validation,
cursor calculation and displacement calculation. New opt-in
`GLYPH_SHARED_SETUP` extracts those operations into a static helper returning
success and two caller-owned state words. Both formatters capture cursor and
displacement before rendering. Default source behavior remains the independent
setup control; no production source or compiler profile changes.

The helper preserves the volatile first-pointer read/null gate, then the
second-pointer read/null gate. Hex adds nine to its position before calling
setup; string uses its original position. Result cells remain private trial
state, not framebuffer output or a new retail calling convention.

## Measurements

All variants link the same selected 29-word frameless C pixel writer:

| Formatter variant | Allocated text | Delta vs control | Observed nested stack |
| --- | ---: | ---: | ---: |
| Independent O2/g3 no-unroll | 624 | 0 | 48 |
| Shared O2/g3 no-unroll | **608** | **-16** | **80** |
| Independent O1 | 704 | 0 | 48 |
| Shared O1 | **688** | **-16** | **56** |

The shared O2 body words are setup 29, hex 44, string 47, writer 29; its
allocated slots are 29 / 44 / 47 / 32 words. Shared O1 bodies are setup 35,
hex 46, string 59, writer 29, with slots 35 / 46 / 59 / 32. Full allocations
include padding; source-level duplication removal is not treated as a text
saving until independently linked.

Sharing saves sixteen executable bytes in both profiles, but increases
observed nested stack by 32 bytes in O2 and eight bytes in O1. The smallest
linked text is still **196 bytes over the 412-byte connected retail comparison
budget**, before formatter-level adapter cost. This is not a fitting solution.

## Stronger Measurement Labeling

IDO does not retain the static setup function's name in the linked symbol
table. Objdump presents its first body as `_ftext`. The measurement driver
now verifies both formatters' first JAL target equals that entry before
labeling the measured body `init_glyph_destination`; no words are omitted or
attributed to a public formatter. An initial symbol-name normalization attempt
failed because the static name is absent; direct call-target guards replace
that assumption. A new test pins complete linked byte counts and helper size.

## Qualification

Four variants run 288 paired fixtures each: **1,152 paired executions**.
The independent controls and shared-helper variants match complete external
interleaved memory operations, values and non-private memory, cursor/string
results, null behavior and ordinary ABI preservation. Output/string alias
timing and all 255 nonzero signed character bytes remain covered.

```sh
python3 -m unittest tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
```

Five formatter tests / sixteen combined tests pass in 35.664 seconds, no
skips, including the call-target normalization and footprint assertions.
The initial shared-shape run passed fifteen tests in 35.589 seconds before
the new footprint assertion. Measurements and stack receipts regenerate in
ignored `conker/build/init-glyph-formatters-semantic/`.

Stack/result operations remain explicitly private trial operations, excluded
from external trace equality. Synthetic fences are not real stack reservation
proof. Note 934's bounded-address, signed-overflow, alias and hardware limits
remain in force. Note 933's occupied experimental text address and two actual
caller stack regimes remain unchanged.

## Decision

Retain shared setup as an opt-in text/stack experiment, not the default or
production candidate. It demonstrates a real sixteen-byte text saving but
does not solve the linked fitting deficit, and its O2 stack cost worsens the
already-open reservation gate. Do not repeat this helper/state-array shape
unchanged as a fresh fitting attempt. Further work needs an interface/shape
that removes setup overhead without those call/state/frame costs, measured
against the complete linked text and both stack regimes.

Production Init remains 492 C / 47 assembly routines. README totals, production
owners, profiles and guards are unchanged. No production rebuild, sibling
build, Release change or push.
