# Init compact-sequence event handler and assembly audit

Date: 2026-10-02

Correction: the subsequent direct assembly audit and linked-body check in
Note 730 supersede this note's candidate classification and address-drift
explanation. `func_10006380` is an assembly fragment with a shared frame and
live-register calling convention. The meta handler was omitted from the
padded object, rather than merely shifted; its layout ownership is now fixed.

`__n_CSPHandleNextSeqEvent` replaces its `GLOBAL_ASM` fallback with the
complete 69-word compact-sequence event dispatcher at
`0x10014048..0x1001415C`. The recovered body is based on the local libultra
reference in `tools/ultralib/src/audio/csplayer.c`, with Conker's extended
player-state gate, three-argument `n_alCSeqNextEvent`, four-argument event
post, and `AL_SEQP_STOPPING_EVT` behavior retained from the retail routine.

The semantic C reproduces the frame, target and paused-state exits, sequence
event fetch, 21-entry switch range, MIDI and tempo dispatch, end-event post,
track/loop continuation cases, empty default arm, and both final branches.
It requires no expected-word guards, insertions, omissions, or alternate
compiler profile. The object needs a retail rodata anchor at
`jtbl_8002C460_init`; its generated table begins at compact rodata offset
`0x6C`, which resolves exactly to `jtbl_8002C4CC_init`.

The linked matcher classifies the routine as the sole Init address-drift row.
All instructions are otherwise retail-equivalent, but its call follows the
currently shifted `__n_CSPHandleMetaMsg` symbol at `0x10015044` instead of the
retail address `0x10015000`. This is an existing downstream layout shift, not
a real difference in the recovered handler. A hardcoded call target was not
used because it would call the wrong routine in the current linked image.

The refreshed Init inventory contains 488 C rows and 50 assembly rows. The
assembly remainder is not a single convertible backlog:

- 23 separated rows are already established handwritten entry, CP0/TLB,
  cache, interrupt, memory, and math routines. They should remain assembly.
- `init_5AB0` contains 26 rows. Twelve rows, totaling 5,564 bytes, include
  instructions explicitly marked handwritten and cover TLB, exception,
  interrupt, thread, or cleanup machinery.
- The other 14 `init_5AB0` rows total 4,276 bytes and use ordinary
  instructions. They are candidates for provenance review, not automatically
  C: the monolithic segment must be split around any converted function, and
  some small SDK queue/memory primitives may still be original assembly.
- The cross-project description of `func_10006380` as compiler-generated was
  contradicted by direct assembly inspection in Note 730. It uses live `$s7`,
  `$gp`, and `$fp` state and its caller's stack frame. `func_10007A24` is a
  self-contained 20-byte queue-pop helper matching handwritten SDK assembly,
  while `func_10005BE0` is a 76-byte memory-fill routine already described by
  the port notes as handwritten; source shape must decide ownership rather
  than size alone.
- `__n_CSPHandleMIDIMsg` is the one remaining `n_csplayer` fallback. It is a
  definite compiler-generated C candidate with a local libultra reference,
  but Conker's 4,532-byte retail body has substantial custom event, voice,
  and synthesizer behavior and should be recovered as its own focused batch.

Init can advance further, but its original handwritten routines should keep
assembly ownership. The next supported conversion is `__n_CSPHandleMIDIMsg`.
Use Note 730's revised inventory before undertaking segment-splitting work.

The focused object build, full `NON_MATCHING=1` link, and linked matcher pass.
Current totals are 5,457 / 6,041 C functions and 3,235 / 5,457 byte-exact C
functions, with one address-drift row and 2,221 genuinely different C rows.
Init is 488 / 538 converted, with 487 exact, one address-drift row, and zero
genuinely different C rows. No fresh gameplay run was performed.
