# Sequence-direction guarded byte match

Date: 2026-11-10. `func_1501FE68` replaces its zero-return placeholder with a
semantic sequence-direction calculation. Its 96-word body matches retail after
eight guarded local-stack offset adjustments; it is a guarded match, not a
direct compiler match. The production recount is **4,322 / 5,513 (78.40%)**
overall and **3,649 / 4,840 (75.39%)** Game, with no address drift and 1,191
different functions. The 80% threshold needs 89 more matches.

Owner: `conker/src/game/generated_49D30.c`; original retained in
`conker/asm/49D30.s`. Target VA `0x1501FE68..0x1501FFE8`, ROM
`0x4D318..0x4D498`, 384 bytes and a `0x88` stack frame. The first float of a
64-byte sequence record is identified as `duration` from its observed use;
that field name is inferred rather than an original-source name.

When the selected key count is at least two, the function clamps the input
percentage to 0..100 using ordered comparisons, scales the record's duration,
and requests two points and a frame index from `func_1501F72C`. Depending on
the key's flag it computes X/Z from those points or from a matrix supplied by
`func_1501FFE8`. The result of `func_150484A0` is converted to degrees and
stored through the caller's output pointer. The inactive case writes nothing.
No extra pointer or range checks were introduced.

The compiler emits the complete logic with the retail frame and instruction
count. The eight expected-word guards move the frame index from SP+0x84 to
SP+0x60 and matrix accesses from SP+0x3C to SP+0x30. The points and saved
locations remain fixed. The full raw body and all relocation bindings are
pinned before those adjustments; independent padding paths agree with retail.

Typing the two existing helper placeholders changes each compiled stub from
12 to 28 bytes by writing its four incoming words to the ABI argument-home
area. This is observable and included in the complete image audit. Both helpers
remain unfinished zero-return stubs, and their real implementations are not
credited or qualified by this change. The calling parent is also unfinished.

Validation covers 590 guest cases (1,770 executions, all 96 instructions
visited), 436 defined SDK32 cases per O0/O2/O3 profile with UBSan and eight
effective incorrect-source controls, 112 triples through the original bounded
caller window, and 128 pairs of old/typed helper stubs. Six direct helper
continuation windows were inspected; this does not prove every possible
indirect caller. The mock helpers exercise specified side effects and do not
establish full helper behavior, FCSR or actual hardware/gameplay behavior.

Both padding implementations agree, 410 corrupt body/binding variants and eight
individual guard corruptions were rejected, and four independent symbol layouts
passed 16 GNU links and 64 executions. The access-cut comparison covers 123
instruction-boundary triples; portable-C fault behavior and raw private-stack
aliases are not claimed. The full suite passed in the mounted tools checkout and
in a private overlay using the sibling tools checkout; installed-state checks
reused only fingerprint-identical pre-install evidence.

The independent actual-Make image prediction has **432 changed bytes**, zero
exclusions, and accounts for the target, both typed stubs, and the closed ELF
metadata permutations. All 54 other owner functions, 6,050 function addresses,
and 189,088 protected data bytes match the baseline. The resulting ELF SHA-256
is `5504b83ae16271c1be8badff7c617e4cdcf191069176d7899269a50c30c55f9c`. The existing full-build checksum mismatch remains;
byte-exact here refers to this linked function, not a matching complete ROM.

The qualification tools were committed first as `344232499a555544647cf3bf0f2bbfc05a5a63b2`.
The consumer source and this note are committed separately. No push is implied.
