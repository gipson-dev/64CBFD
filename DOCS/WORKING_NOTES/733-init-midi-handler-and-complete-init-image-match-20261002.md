# Init MIDI handler and complete Init image match

Date: 2026-10-02

Follow-up: Note 734 completes the Game vector-normalizer target named below
and independently reconfirms both entire Init sections remain byte-exact.
The current ordinary Game target is `func_15157FE8`.

## Complete MIDI Recovery

`__n_CSPHandleMIDIMsg` at `0x1001415C..0x10015044` replaces its `GLOBAL_ASM`
fallback with the complete 954-word / 3,816-byte semantic C handler in
`conker/src/libultra/audio/n_csplayer.c`. The local SDK `csplayer.c` is the
reference; retail instructions establish Rare's extensions and source shape.

The recovery includes missing-instrument deferral, banked program selection
and retry, disabled-channel duration bookkeeping, note-on and zero-velocity
note-off fallthrough, sustain/release handling, per-key and channel pressure,
custom controller callbacks, and pitch-bend updates across allocated voices.
Custom note setup includes envelope overrides, oscillator configuration and
retained state pointers, frequency parameters, duration bookkeeping, and
nonblocking voice-start/end notifications.

File-local channel/voice overlays and a seven-argument oscillator callback
type preserve the guest offsets without changing shared SDK interfaces.
Program retry clears MIDI `ticks`, not `duration`, matching retail's store at
event offset four. The disabled channel-specific check and empty out-of-range
program arm retain the original unoptimized compiler's control-flow structure.
The duplicated no-sound guards likewise preserve the retail break/return paths.

All 954 words emit directly from the existing `-g` audio compiler profile.
No new word patches, insertions, omissions, or profile overrides are required.
The `0xC8` frame, saved-register lifetimes, float conversions, event stores,
branch targets, delay slots, and the 97-entry dispatch all match. Existing
voice-handler guards and explicit meta-handler layout ownership are unchanged.

## Physical Data Ownership

An instruction-only comparison was insufficient: the original generated
linker grouped `.data` inputs ahead of `.rodata`, although retail Init audio
owners alternate between the two. `assets/2C460.bin` had been placed at
`0x8002C2C0`, and the MIDI table's declared `0x8002C520` address read error
message bytes instead of branch targets. Absolute assignments masked this
physical-layout defect from instruction matching.

`restore_init_audio_data_order` in `tools/patch_generated_slice_ld.py` restores
the original interleaving within Init data. Existing owners are moved, not
duplicated. Retail anchors preserve the compact audio constant slots at
`0x8002C460`, `0x8002C770`, and `0x8002C7A0`; the preceding math anchor remains.
Missing or duplicated expected owners are rejected rather than silently
generating a partial layout. Other versions keep their existing linker path.

The resulting table spans independently match the pristine image:

| Data span | Address | Bytes | Result |
| --- | --- | ---: | --- |
| Full sequence dispatch tables | `0x8002C460` | 592 | Exact |
| MIDI dispatch table (within the above) | `0x8002C520` | 388 | Exact |
| Ordinary controller callbacks | `0x8002BA50` | 372 | Exact |
| Four descending special-controller callbacks | `0x8002BBC4` | 16 | Exact |
| Math and NaN constants | `0x8002C850` | 224 | Exact |

The wider data comparison then exposed three empty 16-byte slots containing
six original floats. The existing C owners now emit readonly constant arrays:

- `init_128D0.c`: oscillator constants at `0x8002C450`, `0x8002C454`, and
  `0x8002C458` (`3F83F794`, `40C90FDB`, `40C90FDB`).
- `cents2ratio.c`: pitch ratios at `0x8002C760` and `0x8002C764`
  (`3F8012EF`, `3F7FDA28`).
- `init_1D900.c`: parameter scale at `0x8002C790` (`3DCCCCCD`).

The external retail aliases remain valid; definitions do not change function
bodies or their instruction generation. Object alignment supplies the original
zero padding. Direct whole-section comparison confirms all initialized bytes,
including these constants and table placement, rather than just symbol values.

## Verification

`make -C conker NON_MATCHING=1 all match-progress -j4` passes and regenerates
the linked ELF, code binary, and progress inventories. Direct extraction of
ELF sections using their actual VMAs, offsets, and lengths gives:

| Section | Address | Bytes | Byte differences |
| --- | --- | ---: | ---: |
| Entire Init code, including retained assembly | `0x10001000` | 164,048 | 0 |
| Entire Init initialized data | `0x800290D0` | 17,376 | 0 |

The pristine comparison spans are `0x1000..0x290D0` and
`0x290D0..0x2D4B0` in `conker/conker.us.bin`. Each extracted section has the
expected VMA and exact retail length. SHA-256 values are:

```text
MIDI handler
7894215952d8dc5c58167726f1853e54c18882b1bb25b58b28a939ebaba7babf
Entire Init code
34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf
Entire Init initialized data
a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239
```

Fresh aggregate results are:

- Total: 5,460 / 6,042 C rows; 3,239 byte-exact, zero drift, 2,221 different.
- Init: 491 / 539 C rows (91.09%); all 491 exact; C bytes 151,760 / 164,048
  (92.51%). The remaining 48 rows / 12,288 bytes retain original assembly.
- Game: 4,788 / 5,321 C rows; 2,567 exact, 2,221 different; unchanged.
- Debugger: 181 / 182 C rows; all 181 exact; unchanged.

All 16 tool unit tests pass, including interleaving/order, anchor placement,
missing-owner rejection, and unrelated-layout preservation. Project tool and
whitespace checks pass. Existing pointer-type warnings in the meta-handler
queue code remain outside this change.

This proves linked Init code and initialized-data matching, not a fresh
gameplay run, full compressed-ROM build, or BSS/runtime qualification. The
sibling host port and frozen Release artifacts remain untouched.

## Resume

The supported Init C-conversion queue is complete. Keep original handwritten
and shared-register routines as assembly; do not force the C percentage to
100%. The broader decomp work remains open in Game.

Fresh matcher output and Note 728 agree on the next ordinary Game target:
50-word `func_15145128`, currently at 35 real word differences. Preserve
`func_150A76F0`'s handwritten/register-contract workstream and
`func_150F631C`'s separate near-match cleanup queue.
