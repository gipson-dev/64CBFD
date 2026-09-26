# Init full data-cache writeback restoration - 2026-09-26

## Result

`osWritebackDCacheAll` is restored from an empty C placeholder to its original
handwritten 12-word libultra assembly body. Its complete 48-byte span at
`0x10024F10..0x10024F40` matches pristine retail independently.

## Behavior and ownership

The routine starts at cached address `0x80000000`, derives the last 16-byte
cache line in the `0x2000`-byte data cache, and walks the range in 16-byte
steps. Each iteration issues handwritten `cache 0x01` writeback through the
loop branch delay slot update.

The converted source was an empty generated placeholder, so the linked guest
routine returned immediately and omitted all cache operations. C cannot model
the required MIPS cache instruction. The initial project layout correctly
classified the original file as assembly, making this both a behavioral
restoration and an ownership correction.

## Restoration

`conker/src/game/generated_writebackdcacheall.c` now references a tracked copy
of the original body through `GLOBAL_ASM`. No guarded retail-word patches are
involved.

The conversion denominator drops by one while the exact-C numerator remains
unchanged:

| Section | C functions | Raw assembly | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,472 / 6,038 (90.63%) | 566 | 2,691 / 5,472 (49.18%) | 1 | 2,780 |
| Init | 498 / 538 (92.57%) | 40 | 390 / 498 (78.31%) | 1 | 107 |
| Game | 4,793 / 5,318 (90.13%) | 525 | 2,120 / 4,793 (44.23%) | 0 | 2,673 |
| Debugger | 181 / 182 (99.45%) | 1 | 181 / 181 (100.00%) | 0 | 0 |

## Exact-byte evidence

The linked Init-code slice at offset `0x23F10` and pristine retail slice at
offset `0x24F10` compare equal for all 48 bytes. Both have SHA-256
`9e2e910cf2dcf19b0d2826eea41187a62acc4584b8fb7316cc74acbd40f4b04f`.

## Sibling audit

`64CBFDOGL` routes guest calls to the dedicated
`osWritebackDCacheAll_recomp` entry and records the correct `0x30`-byte symbol
extent. This audit did not find that helper's implementation in tracked host
source and did not runtime-test its cache-coherence behavior, so no stronger
host claim is made. No sibling source or frozen Release artifact was changed.

## Validation

- The focused generated-object assembly-processor build passes with the cache
  instruction and full retail padding.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and LIST `match-progress` runs pass;
  `osWritebackDCacheAll` is no longer a C-classified mismatch.
- The independent 48-byte linked-versus-retail comparison passes.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Audit 16-word `osUnmapTLB`, now the first nonblocked Init row at nine real
differences. Keep address-blocked `func_10012588` parked.
