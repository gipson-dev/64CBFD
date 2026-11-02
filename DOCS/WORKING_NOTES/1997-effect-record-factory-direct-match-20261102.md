# 1997 - Effect-record factory recovered directly from C

Verified 2026-11-02. Production **4,064/5,510 (73.76%)**; Game
**3,391/4,837 (70.11%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,446 different; one newly converted and byte-exact function. The active
80% target remains **4,408/5,510**, requiring **344 more**. This is progress
toward that goal, not completion.

## Interface and recovered behavior

`void *func_1515548C(u8 *descriptor, s32 callback, s32 *pair, s32 pairCount,
s32 extraBytes, u8 slot, s32 context)` replaces the assembly placeholder in
`conker/src/game/generated_17CAF0.c`. Original `17CAF0.s`:
VA1515548C..15155564, ROM18293C, 216 bytes, 54 words and a 56-byte frame.

When `pair` is non-null and `pairCount` is positive, the routine snapshots the
two descriptor position floats and asks `func_151555AC` whether the requested
record overlaps an existing entry. A nonzero answer rejects the request. The
allocator category is `0x57` when descriptor flag `0x20` is set and `0x5D`
otherwise. `func_15167A68` receives the full context, `extraBytes + 0x70`,
allocation mode one, all 256 slot values and pool one. Allocation failure
returns null. Success copies the complete 0x58-byte descriptor to record offset
0x10, clears callback byte 0x68 and ORs in the callback selector.

The complete retail census finds 43 aligned JAL sites, no aligned jump and no
literal function pointer. Every callsite materializes O32 stack arguments five,
six and seven at `SP+0x10`, `SP+0x14` and `SP+0x18`; matching seven-argument C
prototypes in `generated_113D60.c` and `generated_FC5F0.c` agree. Complete
execution of all 43 parent functions is not claimed.

Alternate-source code was consulted only as a broad semantic clue. Its
descriptor, pointer and argument-width types were unsuitable for matching.
The installed name, signature, comments and source shape are independently
established from retail instructions, original callers and runtime controls.

## Direct compiler match

The semantic C emits all 54 retail words directly with no expected-word
guards. Its three relocation bindings are exact:

- `+0x38 R_MIPS_26 func_151555AC`;
- `+0x84 R_MIPS_26 func_15167A68`;
- `+0xA8 R_MIPS_26 memcpy`.

Three independently shifted GNU links agree with the original routine. Raw
unresolved object SHA256:
`8b6a8a4da84a6e2026c14960d67b90c06ee46e6e16fb8767b3908be544757cd0`.
Linked retail payload SHA256:
`bfc9cd49d31564dfea6fbd81289d8679d7c6f3fcd39ad2c6ebedd6f19ca6e953`.

## Fresh qualification

- Guest execution covers 256 cases at each of three independent links, 768
  executions total. It reaches all 53 reachable words. The sole unreachable
  word is the duplicate `lhu` at function offset `0x50`, isolated between an
  unconditional branch and the branch-likely target.
- Null, zero, negative and positive overlap inputs, overlap pass/reject,
  allocation success/failure, both categories and all 256 callback/slot bytes
  execute. Complete 88-byte copies and live descriptor mutations after both
  helper calls agree with an independent reference.
- Native O0/O2/O3 runs 256 cases per profile, 768 total, with six effective
  negative controls per profile, complete descriptor/record images, canaries
  and stop-on-first-error UBSan. Every profile is clean.
- The caller census checks all 43 exact retail JAL offsets and the three stack
  argument stores at every site. No complete-parent gameplay claim is made.

The permanent five-method suite reproduces raw/binding, guest, caller, native,
owner/padder/actual-Make and complete-image gates from retained receipts. It
passes before and after installation. The bounded Graphify refresh is
structural AST only, retains every prior node and every prior edge occurrence,
and uses zero LLM tokens. No full-corpus extraction, global reclustering or
gameplay acceptance is claimed.

## Owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical. The real owner recipe executed its five commands and produced the
qualified object exactly. Protected Game data remains exactly 189,088 bytes
across 720 owners, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The strict complete-image predictor has zero exclusions: all 6,052 function
addresses, 6,051 other bodies and the complete named-definition multiset
remain fixed. Because the direct C reproduces the original target and owner
bytes, the complete production linked image is byte-identical.

Installed object SHA256:
`486b0599b1480bcbe15d9fa114c62a563916857a4660d1bf07d53d9dff2b8a80`.
Linked ELF SHA256:
`752feb861f0a37a4ce3ee397f1a52952a048048aff9c3521ad2b3ff3d9b122da`.
Production linker-map SHA256:
`ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.

The qualification tools were committed first at `c1b314a`. The retained stage
is `conker/build/game-effect-record-factory-1515548C-match/`; it contains the
source, guest, native, caller, owner, whole-image and installed receipts. The
root README changes only aggregate rows; detailed recovery stays here and in
the five concise indexes. No Claude call was needed.

## Next step

Privately audit `func_151555AC`, the next assembly placeholder in this owner.
Keep it uncredited until ABI/caller, semantic runtime, owner/actual-Make,
strict-image, installed recount, documentation and bounded Graphify-retention
gates pass.
