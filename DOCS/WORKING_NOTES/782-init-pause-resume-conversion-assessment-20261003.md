# Init Pause Resume: Remaining Assembly Conversion Assessment

Date: 2026-10-03.

## Decision

Two remaining Init routines have ordinary C-expressible behavior, but neither
has a demonstrated matching replacement. The other 45 assembly rows require
retaining SDK assembly or recovering hardware/nonstandard interfaces as a
connected project. They are not 45 independent compiler-generated C targets.
This is a conversion assessment, not a new conversion or impossibility proof.

## Current Verified Baseline

Fresh `conker/progress.csv` inspection reports 492 C rows / 151,796 bytes and
47 assembly rows / 12,252 bytes: 539 rows / 164,048 bytes in total.
`make -C conker NON_MATCHING=1 all match-progress -j4` succeeds; the build is
up to date and the regenerated matcher reports Init 492 / 492 exact, zero
address drift, and zero different C rows.

Independent extraction from the linked ELF matches the entire retail sections:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| `.init` | 164,048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| `.init_data` | 17,376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |

The six tests in `test_init_mmio_assembly` and `test_init_memory_clear` pass.
These tests do not qualify a new bitmap implementation or hardware execution.
The existing duplicate-recipe warning for `generated_12D630.c.o` remains;
it did not prevent this build or the independent Init comparisons.

## Remaining Groups

| Group | Rows | Bytes | Disposition |
| --- | ---: | ---: | --- |
| Separated SDK assembly | 19 | 2,288 | Retain original SDK routines |
| Boot clear-and-jump entry | 1 | 80 | Retain non-C entry contract |
| MMIO `func_100038E0` | 1 | 44 | Deferred matching C candidate |
| Hardware/context | 8 | 4,376 | Assembly/intrinsic support required |
| Shared-frame decompressor | 10 | 3,984 | Recover the connected interface first |
| Bitmap `func_10005BE0` | 1 | 76 | Best remaining bounded C candidate |
| SDK thread queue leaves | 2 | 96 | Retain original SDK assembly |
| Cleanup/debug/glyph | 5 | 1,308 | Recover connected nonstandard interfaces |
| Total | 47 | 12,252 | Production Init unchanged |

The live bodies and complete inventory remain consistent with
[Note 735](735-init-retained-assembly-reassessment-20261002.md) and
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).

## Where To Pick Up

1. Investigate bitmap `func_10005BE0` first, at
   `conker/asm/init_5AB0.s:97`. It loads start/end once, unconditionally stores
   the first byte, fills through the inclusive endpoint, then reloads the
   signed halfword count and masks the final byte for a nonzero remainder.
   Preserve the delay-slot cursor increment and conditional remainder decrement.
2. Establish a new source/dataflow or compiler-provenance hypothesis before
   compiling. [Note 751](751-init-bitmap-loop-mask-profile-trials-20261002.md)
   already covers 55 shape/profile combinations without a complete nineteen-word
   match. A nineteen-word length alone is insufficient: the closest listed
   shape still differs at fifteen aligned positions.
3. Qualify any new hypothesis against all eight remainder classes, single-byte
   and multi-byte ranges, surrounding bytes, and repeated calls. Explicitly
   resolve the earlier untested zero-count and global/data-alias boundaries;
   do not introduce an early return absent from retail. Invalid/reversed ranges
   need a caller-contract decision, not an invented defensive behavior.
4. Require the complete nineteen-word match before extracting the leaf from
   its shared assembly owner. Verify the following `func_10005C2C` address,
   regenerate progress, and compare both complete Init sections again.
5. Keep MMIO `func_100038E0` secondary. Its eleven words publish a word address,
   publish halfword `0x4040`, then issue the volatile halfword MMIO write.
   [Note 762](762-init-mmio-partial-volatility-trials-20261003.md) records twenty
   partial-volatility/profile variants in addition to earlier trials; none
   matches. Reopen only with new evidence explaining retained address lifetime,
   separate constant materializations, and the nop return delay slot.

If both candidates eventually match, Init would have 494 / 539 C rows and
151,916 / 164,048 C bytes, leaving 45 assembly rows / 12,132 bytes.
Those figures are conditional, not achieved progress. A non-matching semantic
rewrite is technically a different option, but would relinquish the currently
exact Init image; it is not substituted here for a matching conversion.

## Scope

No Init production source, compiler profile, word guard, or README aggregate
changed. No new compiler matrix, guest execution, host-port build, or gameplay
qualification was performed. Pending Game look-at recovery and its documents
were preserved, not committed or reverted as part of this Init assessment.
The sibling port and frozen Release artifacts were untouched.
