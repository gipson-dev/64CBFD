# Init spatial attenuation and pan calculator match

Date: 2026-10-01

`func_1000A420` occupies 204 words and 816 bytes at
`0x1000A420..0x1000A750`. The high bit of its near-distance argument selects
the two-axis `func_150AD960` distance helper; otherwise it uses the three-axis
`func_150AD9A0` helper. The selected distance is normalized between the near
and far limits into a signed 15-bit attenuation value. Values below the
routine's 401-unit activity threshold produce zero attenuation; active values
are clamped to `0..0x7FFF`.

When a pan output is requested and the horizontal separation is at least 31,
the routine normalizes the first horizontal component, converts it through
`func_150487E0`, scales the resulting angle, mirrors it for positive depth,
and applies the listener rotation. The signed pan is folded into the engine's
packed center/side representation. Close sources receive centered pan `64`.
The routine also supports an optional raw-distance output and returns the same
distance to its caller.

The recovered C emits the retail 56-byte frame, homes all four register
arguments, preserves both guarded integer-division sequences, and reproduces
the complete floating-point and clamp control flow. It emits 203 words.
Eighty-one function-scoped, stale-checked rows normalize one closed temporary-
register and floating-point allocation schedule. One checked insertion after
the positive-pan narrowing restores retail's additional move and expands the
body to its 204-word slot. All call and constant relocations already occupy
their retail positions; none is moved or retargeted.

The focused object build, repository-wide serial stale-check rebuild, final
ELF link, authoritative matcher, and direct section-span comparison pass. The
whole-ROM SHA-1 target remains expectedly unavailable while other functions
still differ. The linked and pristine spans share SHA-256
`c55660dda7d31b77b81018ecf5bfe1fcdaac6a2bb3f29ba21604485e066964b1`.

The matcher advances to `3,149 / 5,457 (57.71%)` overall and
`466 / 488 (95.49%)` in Init, with zero address drift and 22 genuinely
different Init C rows.
