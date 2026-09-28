# Init handwritten osMapTLBRdb restoration - 2026-09-28

## Result

`osMapTLBRdb` is restored from an empty C placeholder to its original
handwritten CP0/TLB assembly. The complete 24-word, 96-byte slot at
`0x10008120..0x10008180` is byte-exact: 22 instruction words followed by two
retail padding words.

The row is correctly classified as raw assembly. The fresh linked matcher
reports 2,868 / 5,466 (52.47%) exact C functions overall and 391 / 495
(78.99%) in Init, with 2,597 genuinely different C rows overall and 103 in
Init.

## Restoration

The authoritative body from `asm/libultra/os/maptlbrdb.s` is retained in the
dedicated
`asm/nonmatchings/generated_maptlbrdb/osMapTLBRdb.s` boundary. It preserves
the saved EntryHi value, installs TLB index zero and page mask zero, builds the
debug mapping entries, executes `tlbwi` with the original hazard nops, and
restores EntryHi before returning.

The empty C body remains disabled under `#if 0` only to document the removed
placeholder. CP0 register access and `tlbwi` are intentional handwritten
operations and must not be represented by synthetic C or expected-word guards.

## Verification

The focused generated slice build, complete link and fresh matcher pass
succeed. The refreshed rebuilt slot at
`build/conker.us.init.code.bin+0x7120` and pristine retail slot at
`conker.us.bin+0x8120` compare equal across all 96 bytes. Both have SHA-256:

`a45e7497d9b1ae318665a675d85972e06b9865a413346ccd382da7c89e7d7fa4`

The replacement build, outer-ROM build, project-tool checks, all nine focused
Python tests and whitespace validation also pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified or launched.

## Next boundary

Audit 20-word Init `__osSetHWIntrRoutine`, now the smallest Init row in the
fresh mismatch list at 19 real differences. Keep handwritten and privileged
routines in assembly; use C matching only where the retail function is
compiler-generated.
