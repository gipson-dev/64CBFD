# Init TLB unmap restoration - 2026-09-26

## Result

`osUnmapTLB` is restored from an empty C placeholder to its original
handwritten 16-word libultra assembly body. Its complete 64-byte span at
`0x100262D0..0x10026310` matches pristine retail independently.

## Behavior and ownership

The routine saves CP0 EntryHi, writes the caller's TLB index, installs
`0x80000000` as the temporary EntryHi value, clears EntryLo0 and EntryLo1,
executes `tlbwi`, waits through the required hazard nops, and restores the old
EntryHi value before returning.

The converted source was an empty generated placeholder. Its linked body only
stored the argument in the stack home area and returned, omitting every CP0
write and the indexed TLB operation. Standard C cannot express this sequence;
the initial project layout correctly classified it as assembly.

## Restoration

`conker/src/game/generated_unmaptlb.c` now references a tracked copy of the
original body through `GLOBAL_ASM`. No guarded retail-word patches are
involved.

The conversion denominator drops by one while the exact-C numerator remains
unchanged:

| Section | C functions | Raw assembly | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,471 / 6,038 (90.61%) | 567 | 2,691 / 5,471 (49.19%) | 1 | 2,779 |
| Init | 497 / 538 (92.38%) | 41 | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,793 / 5,318 (90.13%) | 525 | 2,120 / 4,793 (44.23%) | 0 | 2,673 |
| Debugger | 181 / 182 (99.45%) | 1 | 181 / 181 (100.00%) | 0 | 0 |

## Exact-byte evidence

The linked Init-code slice at offset `0x252D0` and pristine retail slice at
offset `0x262D0` compare equal for all 64 bytes. Both have SHA-256
`2fea954023376ffbe406e320314f3a2b6cf1acddb591e2fc0754e2259c01bf3b`.

## Sibling audit

`64CBFDOGL/recomp/conker_us_symbols.toml` records the correct `0x40`-byte
symbol extent. This audit did not find a tracked generated or helper body for
`osUnmapTLB` and did not runtime-test host TLB behavior, so no host
implementation claim is made. No sibling source or frozen Release artifact
was changed.

## Validation

- The focused generated-object assembly-processor build passes with the CP0
  and `tlbwi` instructions and full retail padding.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and LIST `match-progress` runs pass; `osUnmapTLB` is no
  longer a C-classified mismatch.
- The independent 64-byte linked-versus-retail comparison passes.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Continue ordinary Game matching with 13-word `func_151F892C`, now the first
nonblocked row at 13 real differences. Keep address-blocked
`func_10012588` parked; the next ordinary Init C row is 20-word
`func_10001000` at 14 real differences.
