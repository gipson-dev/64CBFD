# Init nearest-anchor forwarder match

Date: 2026-10-01

`func_1000F6B8` occupies 105 words and 420 bytes at
`0x1000F6B8..0x1000F85C`. Its former zero-return placeholder discarded the
spatial-anchor selection and parameter forwarding used by its nearby audio
callers.

The restored function treats its three coordinate arguments as signed
16-bit values. When `D_80082FA0` is nonzero and nonnegative, it scans the
inclusive `D_80041F68[0..D_80082FA0]` record range. Each record is compared
with unsigned squared distance from fields `unkC`, `unk10`, and `unk14`; the
routine retains both the nearest record and that record's relative coordinate
triple. The zero-count path selects the first record directly and computes
the same triple without entering the scan.

The selected record supplies a second relative coordinate triple from fields
`unk0`, `unk4`, and `unk8`, plus `unk18`. Those values, the retained nearest
triple, the caller's two signed limits, packed-output pointer, result pointer,
and a null final output are forwarded to `func_1000A420`. The helper returns
the value written through the result pointer. The first incoming argument is
retail-unused.

The recovered C emits the exact 105-word extent, `0x80` frame, saved-register
set, inclusive scan, branch topology, multiply sequence, and twelve-argument
call contract. IDO persistently assigns the anchor-address temporaries,
distance intermediates, retained vector slots, selected-record slot, result
slot, and final call setup differently. Sixty-eight stale-checked guard rows
normalize 69 words; one row inserts the retail stack restore in the return
delay slot. Relocation-aware rows move the second `D_80041F68` address pair
and the `func_1000A420` call relocation without changing behavior. Thirty-six
words emit directly from the semantic C.

The exhaustive padded-object rebuild, complete ELF link, authoritative
matcher, project tool tests, and direct 420-byte section-span comparison pass.
The linked and retail spans share SHA-256
`a41ddca24f43504374daf24585eb0bc8b865ffb36960baf9dc2ce8296df570bd`.

The matcher advances to `3,121 / 5,457 (57.19%)` overall and
`438 / 488 (89.75%)` in Init, with zero address drift and 50 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
