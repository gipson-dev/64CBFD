# Remaining Init assembly conversion triage

Date: 2026-10-02

Follow-up: Note 732 completes the Init `__sinf` conversion and restores its
constant block's retail addresses. The inventory below records the preceding
audit baseline. Current Init is 490 / 539 C rows, all 490 byte-exact, with
`__n_CSPHandleMIDIMsg` the one supported C conversion still remaining.

## Verified baseline

The resumed checkout is clean at `911df58`. The existing generated
`conker/progress.init.csv` contains 539 rows: 489 C and 50 assembly.
Their byte totals are 147,496 C and 16,552 assembly, out of 164,048.
A fresh, read-only linked matcher confirms all 489 Init C rows byte-exact,
with zero address-drift or different rows. No source conversion or rebuild
was performed for this audit.

## Conversion candidates

| Routine | Retail span | Words | Bytes | Disposition |
| --- | --- | ---: | ---: | --- |
| `__sinf` | `0x10026540..0x10026700` | 112 | 448 | Recover SDK C in a separate Init object |
| `__n_CSPHandleMIDIMsg` | `0x1001415C..0x10015044` | 954 | 3,816 | Recover SDK C plus Rare's audio extensions |

These are supported candidates, not completed conversions or demonstrated
compiler matches. Together they account for 4,264 bytes. Converting both
without changing function boundaries would bring Init to 491 / 539 C rows
(91.09%) and 151,760 / 164,048 C bytes (92.51%). The retained remainder would
be 48 assembly rows / 12,288 bytes. The original handwritten code should not
be rewritten merely to make the C percentage reach 100%.

### Correction to Note 730

Init `__sinf` is not established handwritten assembly. Its retail body in
`conker/asm/libultra/gu/sinf.s` follows the local SDK implementation in
`tools/ultralib/src/gu/sinf.c`: exponent extraction, the same two argument
size thresholds, double-precision polynomial evaluation, nearest-integer
pi reduction, odd-quadrant sign change, and NaN/large-input exits.
This is direct source/body evidence for a compiler-generated candidate.

The existing `conker/src/libultra/gu/sinf.c` is a different, Game-owned
zero-return placeholder. The YAML assigns Init's `__sinf` to assembly at
`0x26540` and Game's `sinf` to C at `0x75210`. Do not overwrite or repurpose
the shared source path to convert Init: introduce a distinct Init source
owner and preserve Game's symbol/layout ownership. Init's coefficient and
reduction constants already reside at `D_8002C8D0`, `D_8002C8F8`,
`D_8002C900`, `D_8002C908`, `D_8002C910`, and `D_8002C920`; retain their
existing addresses instead of duplicating allocatable rodata.

### MIDI recovery constraints

The MIDI handler has an ordinary `0xC8` frame and saved `$ra`, `$s0`, `$s1`,
and `$f20`, with a local reference in `tools/ultralib/src/audio/csplayer.c`.
The reference is a starting point, not a drop-in body. Retail evidence
requires all of the following:

- Channel-busy deferral by `0x8235` microseconds except for program changes.
- Disabled-channel/nonplaying duration bookkeeping and deferred note-off.
- Custom sound/voice/instrument lookups and channel envelope overrides.
- Seven-argument oscillator initialization, including channel extension
  state; the stock six-argument `ALOscInit` declaration is insufficient.
- Retained tremolo/vibrato state pointers at voice offsets `0x3C` and `0x40`.
- The custom ten-argument `n_alSynStartVoiceParams` interface and pitch path.
- Duration bookkeeping in `D_80042810` and nonblocking queue notifications.
- Controller callback tables at `D_8002BA50` and `D_8002BFC0` rather than the
  stock SDK controller switch.
- Program-change retry behavior and pitch-bend updates for allocated voices.

Use the custom headers under `conker/include/2.0L/PR`, existing `n_seqp.h`
helpers, and direct guest assembly to define narrowly scoped extension
types. Do not change shared oscillator interfaces speculatively.

## Retained assembly

All 26 `init_5AB0` rows / 9,840 bytes retain assembly ownership. This includes
the ten shared-frame decompressor fragments, handwritten thread enqueue/pop,
the live-register glyph helper, memory fill, TLB, exception, interrupt, and
cleanup machinery. Note 730's direct shared-register findings still apply.
In particular, `func_10006380` is not an independent ordinary-ABI C function.

The other 22 retained rows / 2,448 bytes are:

- `func_10001000`, `func_10001420`, `func_100038E0`, `osMapTLBRdb`.
- `bzero`, `bcopy`, `sqrtf`.
- `__osSetSR`, `__osGetSR`, `__osSetFpcCsr`, `__osGetCount`, `__osSetCompare`.
- `__osDisableInt`, `__osRestoreInt`, `osSetIntMask`.
- `osInvalICache`, `osInvalDCache`, `osWritebackDCache`, `osWritebackDCacheAll`.
- `osUnmapTLB`, `osMapTLB`, `__osProbeTLB`.

This corrects the previous count of 23 separated handwritten rows by moving
`__sinf` into the supported C queue. Assembly classification concerns original
source/ABI ownership, not whether a behaviorally similar C rewrite is possible.

## Next Steps

1. Recover Init `__sinf` first as the smaller, SDK-grounded conversion. Add
   distinct source ownership and preserve its 448-byte retail slot and
   existing data symbols. Do not alter the Game `sinf` placeholder.
2. Compile the focused object with the matching SDK compiler profile.
   Compare all 112 linked words, data relocations, and neighboring boundaries;
   tune the source before considering any narrow expected-word guard.
3. Run a full non-matching link, fresh conversion/match measurements, and
   direct byte comparison. Record the actual result before changing README
   aggregates; keep detailed recovery text in working notes.
4. Recover the complete MIDI handler in its own batch, beginning with
   declarations and the status dispatch, then note-on/off and custom envelope/
   oscillator paths, followed by pressure, controller, program, and pitch bend.
   Do not ship a partially implemented switch or zero-return substitute.
5. Verify the MIDI body, 97-entry jump table, `__n_CSPHandleNextSeqEvent` and
   `__n_CSPHandleMetaMsg` boundaries, and all existing voice-handler guards.
   Preserve the explicit meta-handler layout restored by Note 730.
6. Bank each verified conversion separately with its working note and measured
   aggregates. Keep the remaining original assembly intact.

## Audit Verification

The read-only matcher was run against `conker/build/conker.us.elf` and
`conker/conker.us.bin` using the existing progress inventory. Results:
3,237 / 5,458 total C rows byte-exact; Init 489 / 489; Game 2,567 / 4,788;
Debugger 181 / 181. There are zero address-drift rows and 2,221 different
Game C rows. This is static linked-image evidence, not gameplay acceptance.
