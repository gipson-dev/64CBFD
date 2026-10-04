# Init Glyph Pixel Seeding And Countdown Fitting

Date: 2026-10-04. Starting HEAD: `99cddf37`.

## Hypotheses

Note 930's smallest ordinary-ABI semantic writer emitted 31 words against
thirty retail words. New opt-in shapes preserve the default control source:

- `GLYPH_SEEDED_PIXEL` initializes a 32-bit pixel to -1 and assigns 0x10001
  only when the source bit is clear, following retail's full-width constants.
- `GLYPH_LOW_PIXEL` instead assigns 1 for a clear bit. Only the low halfword
  is externally stored, so this preserves the observable halfword writes.
- `GLYPH_COUNTDOWN` uses eight-iteration decrementing row/column counters.
  Its tested variant combines the low-halfword pixel shape with no unrolling.

No production source owner, compiler profile or instruction guard changes.

## Measurements

| Shape / profile | Body words | Bytes |
| --- | ---: | ---: |
| Control O2/g3 | 63 | 252 |
| Control O2/g3 no-unroll | 31 | 124 |
| Control O1 | 58 | 232 |
| Retail-width seeded O2/g3 | 61 | 244 |
| Retail-width seeded O2/g3 no-unroll | 32 | 128 |
| Retail-width seeded O1 | 58 | 232 |
| Low-halfword seeded O2/g3 no-unroll | 30 | 120 |
| Low-halfword seeded countdown O2/g3 no-unroll | **29** | **116** |
| Original nonstandard-ABI retail leaf | 30 | 120 |

The retail-width shape removes the unconditional pixel selection jump, but
IDO hoists 0x10001 into a register. Constant setup and register movement grow
its no-unroll body to 32 words. Using the stored value 1 avoids that full-word
constant cost, reaching thirty words. Countdown counters remove another word.
The 29-word candidate is frameless; its body fits the leaf's byte budget, but
its ordinary ABI, register allocation and branch schedule are not retail.

Counts exclude linker padding. Experimental objects are independently linked
at 0x10007D20, not adopted into the retail slot starting at 0x10007D28.
Full production object placement, adapter cost and byte matching are still
unresolved. Do not equate a fitting C body with a fitting connected replacement.

## Qualification

All eight compiled variants run the same 266 paired fixtures each:
**2,128 paired retail/C executions**. This includes byte-pattern/glyph-offset
cases, overlapping destinations and font bytes changed by prior output stores.
Every variant matches complete interleaved external memory operations and
values, non-stack memory and cursor results, while preserving ordinary ABI
callee registers, SP and return link. Note 930's private-stack exclusion for
O1 remains explicit; the new O2 shapes are frameless.

```sh
python3 -m unittest tools.tests.test_init_glyph_semantic tools.tests.test_init_glyph_formatters tools.tests.test_init_glyph_register_contract tools.tests.test_init_diagnostic_cleanup -q -f
```

The full sixteen-test suite passes in 49.468 seconds, no skips. A subsequent
new footprint test independently recompiles all eight variants and asserts
thirty/29 words for the low-value and countdown candidates, with no SP
adjustment in the latter. It passes in 0.950 seconds. That extra test was
added after the full receipt; no seventeen-test combined rerun is claimed.

Measurements/disassembly are regenerated in ignored
`conker/build/init-glyph-semantic/`. Qualification retains the bounded alias,
address and hardware exclusions from Note 930. This is neither hardware
pixel acceptance nor proof of connected adapter stack ownership.

## Continue Here

Retain the 29-word low-value/countdown/no-unroll variant as the fitting
experimental candidate. Next recover and test the adapter, preserving the
formatters' `$v0/$v1/$a1`, argument setup registers, `$t1` cursor output and
return links. Measure the adapter plus C text and stack together; the one-word
body headroom alone cannot accommodate an ordinary stack-saving wrapper.
Do not promote it or raise conversion totals before those connected gates.

Init remains 492 C / 47 assembly routines. README aggregates and production
sources remain unchanged. No production rebuild, sibling build or push.
