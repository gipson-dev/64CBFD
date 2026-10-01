# Init handle-record lookup match

Date: 2026-10-01

`func_1000FEF0` occupies 40 words and 160 bytes at
`0x1000FEF0..0x1000FF90`. A zero 16-bit handle returns `-1` immediately.
Otherwise the routine scans the active 0x30-byte `D_80041FE0` records and
returns the first index whose `unk24` handle, `unk18` owner, and `unk1C`
selector all match while flag `0x80` in `unk10` is clear. It returns `-1` when
no enabled record matches.

Retaining explicit active-count and narrowed-handle lifetimes recovers the
retail 8-byte frame, saved `s0` selector lifetime, argument moves, branch-likely
predicate chain, delay-slot index updates, and 0x30-byte pointer stride. IDO
otherwise unrolls this loop four ways, so the recovered function is compiled
through a no-unroll compact-object override. The rest of `init_EB00.c` remains
on its established profile; in particular, the previously exact
`func_1000F1A8` remains exact.

`pad_c_object.py` now accepts the same scoped `--function-object NAME=OBJECT`
selection already used by generated slices. Its focused regression test proves
that only the named function comes from the alternate object. The Makefile
builds normal and no-unroll `init_EB00` compact objects, then selects only
`func_1000FEF0` from the latter.

Thirty-two of 40 words emit unchanged from semantic C. Eight stale-checked
rows normalize the opening load schedule and one closed `v0`/`a1` allocation
choice. Five rows explicitly preserve or move the `D_80042760` and
`D_80041FE0` relocations; no word is inserted or omitted.

The authoritative linked matcher no longer lists `func_1000FEF0` or the
neighboring `func_1000F1A8`. The linked and retail 160-byte spans share
SHA-256
`634cdf00d310c2aa443ae12aeb10a84e894b20225f95659a9e8738eac2ed2f50`.
The repository-wide stale-check build and final link pass. Project tool checks
pass, all 11 focused tool tests pass, and `git diff --check` is clean.

The measured checkpoint is `3,146 / 5,457 (57.65%)` overall and
`463 / 488 (94.88%)` in Init, with zero address drift and 25 genuinely
different Init C rows. The next Init candidate is `func_1000F85C`, a 48-word
routine with 47 real linked-word differences.
