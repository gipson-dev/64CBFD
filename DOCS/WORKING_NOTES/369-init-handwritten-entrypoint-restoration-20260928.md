# Init handwritten entrypoint restoration - 2026-09-28

## Result

`func_10001000` is restored from a false zero-return C placeholder to its
original handwritten startup assembly. The complete 20-word, 80-byte slot at
`0x10001000..0x10001050` is byte-exact: 14 instruction words followed by six
retail padding words.

Because this is correctly classified as raw assembly, the current linked
matcher reports 2,868 / 5,467 (52.46%) exact C functions overall and
391 / 496 (78.83%) in Init. The genuinely different C queues fall to 2,598
overall and 104 in Init.

## Restoration

The authoritative body from `asm/entrypoint.s` is retained in the dedicated
`asm/nonmatchings/generated_entrypoint/func_10001000.s` boundary. It:

- loads the BSS clear start at `D_8002D4B0`;
- clears `0x16690` bytes with paired 32-bit stores;
- uses the original handwritten trapping `addi` instructions for the loop
  decrement and pointer increment;
- installs `D_800314B0` as the stack pointer; and
- jumps indirectly to `D_80005AB0` without a normal C return.

The former `return 0` body remains disabled under `#if 0` only to document
the placeholder that was removed. Modeling this entrypoint in C or normalizing
it with expected-word guards would obscure its intentional startup semantics.

## Verification

The focused generated-entrypoint object build, complete link and fresh matcher
pass succeed. The refreshed rebuilt slot at
`build/conker.us.init.code.bin+0x0` and pristine retail slot at
`conker.us.bin+0x1000` compare equal across all 80 bytes. Both have SHA-256:

`7a9dc3778670af618e34cc536d274199f7713bdf4a015df8141b8bcfe5fca943`

The replacement build, outer-ROM build, project-tool checks, all nine focused
Python tests and whitespace validation also pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified or launched.

## Next boundary

The adjacent audit of handwritten/control-register work is completed in
[Working Note 370](370-init-handwritten-maptlbrdb-restoration-20260928.md).
Resume by auditing 20-word Init `__osSetHWIntrRoutine`, now the smallest Init
row in the fresh mismatch list at 19 real differences.
