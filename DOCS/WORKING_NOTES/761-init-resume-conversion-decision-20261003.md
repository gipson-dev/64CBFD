# Init Resume: Can Remaining Assembly Become C?

Date: 2026-10-03.

## Decision

Two small leaves are reasonable bounded C candidates, but neither has a proven
matching replacement. The remaining 45 rows are not an ordinary independent
C-conversion queue. Algorithms can be rewritten in C; preserving their original
hardware, shared-frame, and register interfaces is a different requirement.

| Group | Rows | Bytes | Disposition |
| --- | ---: | ---: | --- |
| Separated SDK assembly | 19 | 2,288 | Retain original SDK implementations |
| Boot clear-and-jump entry | 1 | 80 | Retain non-C entry contract |
| MMIO `func_100038E0` | 1 | 44 | New justified matching experiment only |
| Hardware/context | 8 | 4,376 | Privileged/context assembly retained |
| Shared-frame decompressor | 10 | 3,984 | Whole-contract rewrite, not leaf extraction |
| Bitmap `func_10005BE0` | 1 | 76 | Match before shared-owner extraction |
| SDK thread queue leaves | 2 | 96 | Retain original SDK assembly |
| Cleanup/debug/glyph | 5 | 1,308 | Recover nonstandard interfaces together |
| Total | 47 | 12,252 | No Init conversion in this checkpoint |

## Candidates And Gates

1. Start with `func_100038E0` only with a new source-shape/dataflow hypothesis.
   Its eleven words publish address `0xBC000C02`, publish halfword `0x4040`,
   then write that halfword to volatile MMIO. Preserve this order and its
   return contract. Prior five trials plus twenty follow-up trials did not
   match; repeating them unchanged adds no evidence.
2. Compare the complete eleven-word body, retained address lifetime, repeated
   constant materialization, and return-delay scheduling. No broad word
   substitutions or weakened expected-word guards.
3. Then consider `func_10005BE0`: nineteen words, an unconditional first store,
   inclusive fill endpoint, signed-halfword count, and low-three-bit final
   mask. The prior 55-combination matrix had no exact candidate.
4. Prove all eight remainder classes and surrounding-byte preservation, then
   match all nineteen words before extracting from `init_5AB0`.
5. Before banking a conversion, rebuild, regenerate progress, compare the
   following addresses, and compare both complete Init sections.

Prior trial evidence:
[Note 750](750-init-mmio-pointer-lifetime-profile-trials-20261002.md),
[Note 751](751-init-bitmap-loop-mask-profile-trials-20261002.md).
Detailed retained-interface inventory:
[Note 735](735-init-retained-assembly-reassessment-20261002.md).

## Fresh Evidence

Live CSV: 492 C rows / 151,796 bytes and 47 assembly rows / 12,252 bytes,
539 rows / 164,048 bytes overall. C coverage is 91.28% of rows and 92.53%
of bytes. Live assembly confirms CP0 writes, shared caller-stack slots,
`jalr $t3` links, and a syscall entry; ordinary ABI C is not equivalent.

Independent linked ELF comparison matches retail:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| `.init` | 164,048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| `.init_data` | 17,376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

All 167 repository tool tests and project checks pass; these do not represent
new Init compiler trials or gameplay qualification. No Init source changed.
If both candidates eventually succeed, coverage would be 494 / 539 C rows,
leaving 45 assembly rows / 12,132 bytes. This is conditional, not progress.

The sibling host port and frozen Release artifacts remain untouched.
