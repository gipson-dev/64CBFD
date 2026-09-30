# Init Leo resume helper pair match

Date: 2026-09-30

`__osLeoAbnormalResume` occupies 58 words and 232 bytes at
`0x100271F4..0x100272DC`. Its recovered libultra body waits for PI IO-busy to
clear, resets and restores the disk buffer-manager control shadow, invokes
the normal resume helper, clears the PI interrupt, and restores the PI bit in
the global interrupt mask.

`__osLeoResume` occupies 61 words and 244 bytes at
`0x100272DC..0x100273D0`. It selects the PI event state, rejects a missing or
full message queue, appends the event message at the wrapped queue tail,
increments the valid count, and wakes one waiting thread through the run
queue when present.

Both bodies come from the repository-local ultralib reference. The generated
slice now uses the stock SDK `-O1` profile already assigned to neighboring
libultra objects. This retail revision's abnormal-resume polling loops test
only `PI_STATUS_IO_BUSY` (`0x2`), rather than the newer local reference macro's
combined IO/DMA mask (`0x3`). Address-derived project symbols are used for the
disk handle, PI event state, interrupt mask, run queue, and queue helpers.
Both complete functions emit directly from C with no expected-word guards.

The focused object build, full linked rebuild, authoritative matcher, and
direct section-span comparisons pass. The linked Init section and pristine
image share SHA-256
`500e2acc2a1a8684d801922f996043336aa5ddb2a54566badb22d54f4dd60a14`
for `__osLeoAbnormalResume` and
`ebe24919f2d63e916824fb1bec7ffbb078a46070afe16b3420a1a5c3452b2cbe`
for `__osLeoResume`.

The matcher advances to `3,094 / 5,457 (56.70%)` overall and
`411 / 488 (84.22%)` in Init, with zero address drift and 77 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
