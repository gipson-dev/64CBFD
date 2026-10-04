# Init Glyph Writer Register And Pixel Contract

Date: 2026-10-04. Production baseline: `ec2bf64f`.

## Recovered Leaf Contract

`func_10007D28` occupies thirty words / 120 bytes at
`0x10007D28..0x10007DA0`. New tests compare the complete assembly slot
against the local retail ROM and execute its words with the existing bounded
guest instruction fixture. No production replacement is installed.

Inputs are not an ordinary o32 argument list:

| Register | Input / output |
| --- | --- |
| `$t1` | First destination cursor; advances sixteen bytes on return |
| `$t2` | Byte displacement from first destination to second; preserved |
| `$t3` | Glyph index, multiplied by eight; clobbered during rendering |
| `$t4` | Font byte base; preserved |
| `$ra` | Return link; preserved by the leaf |

The writer reads eight font bytes starting at `font + glyph * 8`.
Each byte supplies eight pixels, most significant bit first. A set bit emits
halfword `0xFFFF`; a clear bit emits halfword `0x0001`, not zero.
For each pixel it writes destination one, then destination two. Pixel stride
is two bytes; row stride is `0x248` bytes (584). The sixteen pixel bytes plus
the row-end adjustment `0x238` produce that full stride. Final `$t1` advances
one glyph width only, not eight rows.

Observed clobbered registers are `$at`, `$a2`, `$a3`, `$t1`, `$t3`, `$t5`,
`$t6`, `$t7`, `$t8`. Tests verify every other register retains its input,
including SP, callee-saved registers, `$t2`, `$t4` and the return link.
`$a2/$a3` finish at zero; `$t6` finishes just past the eight font bytes.

## Connected Entry Boundary

Static source inspection explains why this leaf cannot be independently
replaced with an ordinary C call:

- `func_10007C74` and `func_10007CC4` enter `__osCleanupThread + 0xC`
  (`0x10007C04`) using `jalr $t3,$t0`, not the cleanup function's public entry.
- That interior helper prepares `$t1/$t2/$t4`, then returns through `$t3` on
  its successful path. Its failure paths return through `$ra` instead.
- The formatting callers retain their continuation in `$a1`, iteration state
  in `$v0/$v1`, and call the glyph writer repeatedly. The writer must preserve
  those values; an ordinary C callee may legally clobber them.
- `func_10007C74` shifts and renders eight nibbles, adjusting `$t1` before
  each glyph. `func_10007CC4` maps signed character bytes before calling the
  same leaf. Their complete runtime entry contracts are not qualified by the
  leaf tests added here.

The named cleanup slot therefore contains both a public cleanup entry and
an interior debug destination setup interface. Preserve those distinct
interfaces rather than treating the whole slot as a single normal C body.

## Fresh Verification

`tools/tests/test_init_glyph_register_contract.py` adds four tests:

- Complete thirty-word retail slot comparison.
- All 256 byte patterns, varied rows and glyph offsets 0..40.
- Six uniform/alternating/single-bit patterns, including blank and solid glyphs.
- Write fences rejecting row gaps, surrounding bytes and font writes.

All 262 rendering fixtures execute the retail leaf, check all 128 ordered
halfword writes, verify pixels and adjacent guards, and check register effects.
The independent suite passes four tests in 1.426 seconds. Combined glyph,
diagnostic cleanup, MMIO and bitmap suites pass nineteen tests in 2.050
seconds, no skips:

```sh
python3 -m unittest tools.tests.test_init_glyph_register_contract tools.tests.test_init_diagnostic_cleanup tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly -q -f
```

These fixtures cover separated writable destinations and synthetic read-only
font bytes. They do not establish arbitrary overlapping font/destination
semantics, invalid glyph indices, framebuffer ownership, hardware pixels or
complete formatter/cleanup execution. No fresh production rebuild is needed
for this test-only change, and no fresh whole-section match is claimed.

## Next Conversion Gates

- [x] Pin the glyph leaf's original bytes, bounded pixels and register effects.
- [ ] Execute connected interior setup and both formatter paths, including
  success/failure return links, signed-byte mapping and destination ownership.
- [ ] Qualify a semantic C pixel writer against ordered reads/writes and
  required alias behavior, not final pixels alone.
- [ ] Design and test a connected assembly adapter preserving the live
  caller-saved state and `$t1` cursor result before considering C adoption.
- [ ] Independently measure full slot/layout and complete Init code/data
  before changing production ownership. An adapter-plus-C implementation
  must not be presented as a direct ordinary-ABI C match.

Init remains 492 C / 47 assembly routines. Production sources, guards,
profiles and README totals are unchanged. No sibling build, Release change
or push. Existing readiness/trial documentation remains preserved.
