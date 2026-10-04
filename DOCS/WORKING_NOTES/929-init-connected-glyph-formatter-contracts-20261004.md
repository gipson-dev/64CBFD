# Init Connected Glyph Formatter Contracts

Date: 2026-10-04. Production baseline: `ec2bf64f`.

## Connected Runtime Boundary

New `tools/tests/test_init_glyph_formatters.py` executes the retail interior
destination setup entry, both formatter callers and the actual glyph writer
together. All code words are compared against the local retail ROM first.
The public `__osCleanupThread` entry and `osDestroyThread` are not executed.
This continues [Note 928](928-init-glyph-writer-register-and-pixel-contract-20261004.md).

`func_10007C74` and `func_10007CC4` enter `0x10007C04` using a `$t3` link.
Setup reads the two destination pointers at `0x8002AAE8` and `0x8002AAEC`.
When either pointer is zero it returns through the original `$ra`, bypassing
the formatter body. With both pointers present it computes:

```text
cursor = first + (position & 0xFFE0) * 146
               + (position & 31) * 16 + 0x4A0
displacement = second - first
font = 0x8002AC84
```

It then returns through `$t3` into the formatter. The signed SUB and ADDI
instructions are modeled with overflow checks, not silently changed to
wrapping arithmetic. Successful fixture addresses do not trigger overflow.
The constant symbol address itself cannot be null in this retail placement;
the two loaded destination-pointer null branches are exercised.

## Hex Formatter

`func_10007C74` adds nine to the position for setup and restores the original
position afterward. It processes all eight nibbles of the input word, low
nibble first, with glyph indices `nibble + 9`.

Before each glyph call it subtracts **32 bytes** from `$t1` in the JAL delay
slot. The writer advances sixteen bytes on return. Thus glyph starts are
`setupCursor - 32 - i * 16`, while the final returned `$v0` cursor is
`setupCursor - 128`. Those are distinct formulas: a naive sixteen-byte
predecrement places the first glyph incorrectly.

The formatter shifts `$v1` and counts in `$v0`; the writer preserves both.
Its original continuation is retained in `$a1`, and final return uses that
register rather than the glyph call's `$ra`.

## String Formatter

`func_10007CC4` reads signed bytes until the first zero. For each nonzero
byte, its glyph mapping is:

```text
signedByte = byte < 128 ? byte : byte - 256
glyph = max(0, signedByte - (signedByte >= 65 ? 7 : 0) - 39)
```

This is not a general ASCII normalization rule. In particular, high-bit
bytes are negative and map to glyph zero; lowercase bytes are not folded
to uppercase. Glyphs advance left-to-right in sixteen-byte steps. Empty
strings still perform destination setup but produce no glyph stores.
The original continuation again resides in `$a1`.

## Fresh Tests

Five new tests cover complete connected retail-word comparison, twenty hex
fixtures (five positions by four word patterns), all 255 nonzero character
bytes, three empty/multicharacter strings and six missing-buffer exit cases.
Each rendering fixture checks exact glyph indices/cursors, every ordered
halfword pixel write, pixel values, preserved callee registers/SP and the
successful `$a1` return continuation. Failure fixtures check absence of
glyph writes and preservation of the original `$ra` return link.

The local fixture adds only the signed byte/arithmetic and general register
jump/link operations needed here; it does not change the shared decoder
emulator. The hex test initially exposed the incorrect sixteen-byte
predecrement expectation and was corrected from the actual retail delay slot.
The write range was also expanded for the included position `0x300`, whose
calculated row address lies beyond the initial 64 KiB fixture range.

```sh
python3 -m unittest tools.tests.test_init_glyph_formatters tools.tests.test_init_glyph_register_contract tools.tests.test_init_diagnostic_cleanup tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly -q -f
```

All 24 tests pass in 4.345 seconds, no skips. These are bounded instruction
fixtures, not hardware rendering or framebuffer-allocation proof. Arbitrary
font/output aliasing, overflowing coordinates/displacements and public
cleanup entry behavior remain outside this qualification.

## Next Gates

- [x] Execute connected interior setup and both formatting callers with the
  real glyph leaf, including null-buffer return links and signed-byte mapping.
- [ ] Qualify semantic C against ordered memory operations, including required
  alias behavior, before considering an assembly adapter.
- [ ] Preserve `$v0/$v1/$a1`, nonstandard argument registers, link routing and
  `$t1` cursor results across the proposed connected C interface.
- [ ] Measure full linked layout and compare complete Init code/data before
  any production ownership change. Passing a model is not a new byte match.

Production source, profiles and guards remain unchanged. Init stays 492 C /
47 assembly routines. No README aggregate update, sibling build or push.
