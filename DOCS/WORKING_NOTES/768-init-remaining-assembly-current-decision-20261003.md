# Remaining Init Assembly: Current Conversion Decision

Date: 2026-10-03. Resumed from the interrupted checkpoint at `46e7bdc`.

## Answer

Two remaining Init leaves can reasonably be expressed in ordinary C, but
neither has a proven byte-exact C replacement. There is no supported new
production Init conversion to bank from the current evidence. The other
45 assembly inventory rows are not independent ordinary-C recovery targets.
Retaining original assembly is appropriate for their hardware or register
contracts; an algorithmic rewrite is a separate project, not a matching claim.

Fresh `progress.csv` inventory confirms 492 C rows / 151,796 bytes and
47 assembly rows / 12,252 bytes, totaling 539 rows / 164,048 bytes.

| Group | Rows | Bytes | Current disposition |
| --- | ---: | ---: | --- |
| Separated SDK assembly | 19 | 2,288 | Preserve original SDK routines |
| Boot clear-and-jump entry | 1 | 80 | Preserve non-C entry contract |
| MMIO `func_100038E0` | 1 | 44 | Deferred matching C candidate |
| Hardware/context | 8 | 4,376 | Requires privileged/context assembly support |
| Shared-frame decompressor | 10 | 3,984 | Requires coordinated register/frame recovery |
| Bitmap `func_10005BE0` | 1 | 76 | Deferred matching C candidate |
| SDK thread queue leaves | 2 | 96 | Preserve proven SDK assembly provenance |
| Cleanup/debug/glyph | 5 | 1,308 | Recover connected nonstandard interfaces together |
| Total | 47 | 12,252 | No Init source changed |

Detailed function inventory and examples of shared stack slots, interior
entries, and nonstandard link registers remain in
[Note 735](735-init-retained-assembly-reassessment-20261002.md).

## Candidate Gates

1. `func_100038E0`: eleven words. Publish word `0xBC000C02` to
   `D_80038070`, publish halfword `0x4040` to `D_80038074`, then write the
   halfword to volatile MMIO `0xBC000C02`. Preserve access widths/order,
   address lifetime, and return-delay scheduling. Prior five initial,
   twenty follow-up, and twenty partial-volatility/profile variants have not
   matched. The latter twenty were rerun, not forty distinct candidates.
   A new attempt needs a genuinely new source/dataflow hypothesis or provenance,
   not repetition of those matrices or broad instruction substitution.
2. `func_10005BE0`: nineteen words. Fill from start through the inclusive
   final byte, including an unconditional first store. Reload the signed
   halfword count and mask the final byte only when its low three bits are
   nonzero. The prior 55-combination loop/mask/profile matrix did not match.
   Preserve all eight remainder classes and surrounding bytes before extracting
   this leaf from `init_5AB0`; require the complete nineteen-word match.
3. For either successful candidate, rebuild and regenerate progress, verify
   following symbol addresses, run behavior/regression tests, and compare both
   complete Init sections before replacing production assembly.

Prior compiler results are historical evidence, not new trials in this audit:
[Note 750](750-init-mmio-pointer-lifetime-profile-trials-20261002.md),
[Note 751](751-init-bitmap-loop-mask-profile-trials-20261002.md), and
[Note 762](762-init-mmio-partial-volatility-trials-20261003.md).

## Fresh Verification

The live MMIO and bitmap assembly were inspected again. The linked artifact
still matches both entire retail Init sections independently:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| `.init` | 164,048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| `.init_data` | 17,376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

All 218 repository tool tests and project checks pass. The adjacent interrupted
Game wrapper recovery is verified separately in
[Note 767](767-game-entity-height-wrapper-direct-match-20261003.md).
No new Init compiler experiment, guest MMIO execution, compressed-ROM build,
host-port build, or gameplay test was performed for this assessment.

If both small candidates eventually match, Init would reach 494 / 539 C rows
and 151,916 / 164,048 C bytes, leaving 45 assembly rows / 12,132 bytes.
These are conditional totals, not achieved progress. Finishing Init's existing
C matcher queue and preserving exact original assembly do not require forcing
every hardware routine into ordinary C.
