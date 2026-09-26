# Game table sum loop match - 2026-09-26

## Result

All 19 words of `func_1501CFF8` now match retail across
`0x1501CFF8..0x1501D044`. This source-only result is included in the fresh
two-function checkpoint of `2600 / 5484 (47.41%)` overall and
`2032 / 4795 (42.38%)` game. Debugger remains complete at `181 / 181`.

## Evidence

The function sums the unsigned-halfword entries addressed by
`D_800C35D8[arg0]`, using the byte in `D_800C363A[arg0]` as the count. The
previous local count made IDO prove exact iteration and reduce the relational
back edge to a direct `bne`; its declaration order also assigned the count and
index to the opposite registers.

Declaring the sum and index first, then spelling both count tests directly as
`D_800C363A[arg0]`, recovers retail without guards. IDO still emits one byte
load, keeps it in `a1`, uses `v0` for the index and `v1` for the sum, and
preserves the `slt`/`bnez` back edge. Both global relocation pairs, pointer
advance, sum delay slot, return, and trailing extent agree.

The exhaustive non-matching rebuild, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x4A478` and pristine
retail `conker/conker.us.bin+0x4A4A8` share SHA-256
`5e8669328165c7bbc1972b40dfe5c9162102aff28a9088f06f5276ee387ee090`.
No guarded row targets this function.

The `64CBFDOGL` sibling has no hand-maintained source body for this function.
Its 1,659 existing dirty entries were left untouched, and frozen Release was
not built, modified, or launched.

## Next boundary

The pass continued directly into `func_15031E2C`; its completed evidence is in
[Working Note 087](087-game-mirrored-counter-table-update-match-20260926.md).
