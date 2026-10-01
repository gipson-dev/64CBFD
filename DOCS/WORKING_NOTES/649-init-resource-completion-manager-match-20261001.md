# Init resource-completion manager match

Date: 2026-10-01

`func_1000A03C` occupies 195 words and 780 bytes at
`0x1000A03C..0x1000A348`. The recovered routine drains up to
`D_8002AE50` nonblocking messages from `D_800416F0`. Each successful message
identifies a node on `D_800406A0.unkC`; the node is unlinked, inserted after
the `unk4` list head, marked active, and reference-counted. Type-1 resources
carry a signed entry count at offset `0xE`; every word in their table at
offset `0x10` is relocated by the resource base.

The second pass scans `D_800406A0.unk10`. For type-1 resources it follows each
table entry through its wrapper pointer at offset `8`, clears an active voice
byte at offset `0xA`, and retains the resource for that pass. An idle resource
has its state bytes cleared, is released through `func_10004074`, is removed
from the release list, and is recycled after the `unk8` free-list head. A set
`D_8003E384` finally calls `func_1000A348` and is cleared.

Reusing one node cursor across both phases recovers retail's saved-register
lifetimes: `s0` holds the current node, `s1` the manager, `s2` the next node
after its phase-one constant use, and `s3` the type/busy constant. Shared list
temporaries recover the 120-byte frame. The semantic body emits 190 words.
Eighty-six function-scoped, stale-checked rows normalize temporary registers,
stack slots, branch distances, and the two closed list schedules; five of
those rows insert the compiler scheduling words required by the 195-word
retail span. All existing relocations already land at the retail offsets, so
none is moved or retargeted.

The focused object build, repository-wide serial stale-check rebuild, final
ELF link, authoritative matcher, and direct section-span comparison pass. The
whole-ROM SHA-1 target remains expectedly unavailable while other functions
still differ. The linked and pristine spans share SHA-256
`42c65b8dbbdff63a3471f0a348effb6a07ee2bf0293af5b159513b9340bbe989`.

The matcher advances to `3,148 / 5,457 (57.69%)` overall and
`465 / 488 (95.29%)` in Init, with zero address drift and 23 genuinely
different Init C rows.
