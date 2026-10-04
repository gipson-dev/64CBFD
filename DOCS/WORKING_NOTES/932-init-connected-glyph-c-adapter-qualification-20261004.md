# Init Connected Glyph C Adapter Qualification

Date: 2026-10-04. Starting HEAD: `0c9dc1e2`.

## Experimental Adapter

`tools/experiments/init_glyph_writer_adapter.s` bridges the retail glyph
register interface to Note 931's low-pixel/countdown/no-unroll C candidate.
It is independently linked at the original glyph entry 0x10007D28 for
fixtures only; production `conker/asm/init_5AB0.s` remains unchanged.

The adapter reserves a 56-byte, eight-byte-aligned frame: sixteen bytes of
ordinary outgoing argument space, nine saved words at offsets 16..48, and
four trailing alignment bytes. It preserves `$v0/$v1/$a0/$a1/$t0/$t2/$t4/
$t9/$ra`, passes `$t1/$t2/$t3/$t4` in `$a0/$a1/$a2/$a3`, then copies the
C cursor result into `$t1` before restoring the saved `$v0`. It restores
`$a2/$a3` to zero, matching the retail leaf's completed loop counters, and
releases the frame in the return delay slot. Ordinary C preserves the
callee-saved registers used by the surrounding connected caller.

This preserves the original formatters' live `$v0/$v1/$a1`, setup inputs
needed on repeated calls, and return links. Other retail-clobbered temporaries
are not promised identical final values; every register outside the retail
clobber set is checked in separate direct-leaf fixtures.

## Linked Text And Stack Cost

| Component | Body bytes | Allocated executable bytes |
| --- | ---: | ---: |
| Adapter at 0x10007D28 | 120 | 120 |
| C writer at experimental 0x10009000 | 116 | 128 |
| Connected replacement | 236 | **248** |
| Original retail leaf | 120 | 120 |

The adapter alone ends at 0x10007DA0, exactly fitting the original leaf
slot without overwriting the next syscall entry. It requires another 128
allocated executable bytes for the C writer. Combined allocated text is
therefore **128 bytes larger** than retail, despite the fitting C body.
The C object's twelve padding bytes are counted, not hidden as body text.
The connected path descends exactly 56 bytes; the C candidate is frameless.

The experimental address 0x10009000 is not a verified free production slot.
No code is placed there in production. This measurement establishes the
cost of this adapter design, not a viable ROM layout or real stack reservation.

## Connected Differential Qualification

`tools/tests/test_init_glyph_adapter.py` assembles the adapter, independently
compiles the chosen C variant warning-clean and links both. It runs actual
retail interior setup and formatter callers with either the original leaf or
the adapter/C implementation. External interleaved memory operations, values,
non-stack memory, glyph indices/cursors and required final registers agree.

Coverage includes twenty hex fixtures, all 255 nonzero signed character
bytes, three empty/multicharacter strings and two missing-buffer exits:
**280 connected paired fixtures**. Five additional direct-leaf pairs verify
all registers outside retail's clobber set, zero completed loop counters and
cursor/operation equality. Write-fence tests reject writes below the 56-byte
frame and into the original caller stack. Adjacent stack guard bytes are
included in the non-stack comparison and remain unchanged.

Formatter fixture branch handling now recognizes BEQL/BNEL and skips an
untaken likely branch's delay slot, needed by compiled C. The connected
retail formatter suite is rerun alongside adapter tests; the shared decoder
instruction fixture is not modified.

```sh
python3 -m unittest tools.tests.test_init_glyph_adapter tools.tests.test_init_glyph_formatters tools.tests.test_init_glyph_register_contract tools.tests.test_init_diagnostic_cleanup -q -f
```

Seven adapter tests / twenty combined tests pass in 10.793 seconds, no skips.
Measurements and independent object/images remain in ignored
`conker/build/init-glyph-adapter/`. Stack operations are explicitly private
trial operations, excluded from external memory-trace equality; this is not
an instruction-identical replacement.

## Production Gates Still Open

- [x] Preserve and qualify connected ordinary-C/retail register and link
  routing, including repeated formatter calls and direct leaf contracts.
- [x] Measure adapter plus C text and bounded nested stack descent together.
- [ ] Identify and justify executable placement for the additional 128 bytes,
  or redesign the whole connected implementation to fit its owned slots.
- [ ] Prove real caller-stack reservation and entry ownership for the added
  56-byte frame; synthetic fixture fences are not allocation proof.
- [ ] Requalify any changed source/adapter/layout, including required alias
  behavior and complete Init code/data before adoption.

Prior semantic C alias fixtures remain Note 931's receipt. This connected
run uses separate font/destination storage; arbitrary stack/output/font
overlap and physical hardware/framebuffer acceptance remain outside scope.
Public cleanup entry execution is also not covered by these formatters.

No production conversion: Init remains 492 C / 47 assembly routines. README
aggregate tables, production profiles, word guards and source ownership stay
unchanged. No production build, sibling artifact change, Release change or push.
