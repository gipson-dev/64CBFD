# Actor Record List Lookup Direct Match - 2026-11-07

`func_150A2AEC` replaces its zero-return placeholder with the complete active
record-list lookup. All **110 words emit directly from C**, including the
original **64-byte frame**, fourteen bindings and saved-register lifetimes.
No guards, compiler profile changes, data changes or metadata reordering.

Fresh production count: **4242/5512 = 76.96%**, Game **3569/4839 = 73.75%**,
Init 492/492, Debugger 181/181, zero drift. **168 more** exact functions reach
4410/5512 and 80%. Conversion counts and the progress CSV remain unchanged.

## Source, ABI and ordered behavior

Entry 150A2AEC..150A2CA4, retail ROM CFF9C..D0154, 440 bytes. Owner:
`conker/src/game/generated_CDE80.c`, normal IDO 5.3 O2/g3, MIPS2/O32.
Interface: `s32 func_150A2AEC(s32 actorIndex, s32 count, s32 *identities)`.

The function selects its path once. Actors 0..15 with their bit set in the
u16 D_800D2340 use three u64 mask words per actor at D_800D30F0. Other actors
use the volume/collision provider. Each path scans the signed positive count,
masks each supplied identity to twelve bits, and checks the live unsigned
D_800D3094 record bound. A mask hit or zero collision result returns the first
matching identity; an empty/exhausted scan returns -1.

The mask row is 24 bytes; word/bit selection is identity>>6 / identity&63.
The fallback uses actor stride 0x32C and descriptor stride 0x34, reloads the
descriptor pointer from D_800D3098 before each eligible provider call, and
preserves the original count/list behavior across calls. Changes to the
enabled mask during fallback do not switch paths mid-scan.

A pointer-postincrement/flat-mask form already had 110 words/frame64 but
91 word differences. Indexed list reads and a typed three-word row view
recover the complete retail sequence directly. Raw function SHA-256:
`9f235a40c238669a1466fcb8755de095a45260f8815d7cec829036525841096b`.

## Complete owner and image gates

Predecessor consumer 7f0721e7926db48fba369a80b90a5410e55ae75d; tools
3188dcbf19b5f6aea7a118ba41c61c42b7f0aeaa. Preparation freezes 104
source/header/compiler/input files, compiles the complete GLOBAL_ASM owner,
and preserves all 27 raw and padded neighbors and bindings.

The compact object's register metadata adds exactly FP and S7 usage bits,
0x40800000 (A37FFFFE -> E3FFFFFE). All remaining .reginfo bytes and other
allocatable pools agree. The production and strict padded objects agree on
all 28 functions and pools; all 31 original case-label definitions in the
assembly-slice output are explicitly accounted for. The padded metadata is
unchanged. No new runtime pool or shared declaration repair is introduced.

The actual five-command copied-owner Make recipe, including GLOBAL_ASM
processing, reproduces the qualified complete object. The independent
whole-image prediction equals production after **340 changed bytes, zero
exclusions**: 338 bytes inside this function and two symbol-size bytes.
Every other linked body and all 6052 addresses remain fixed; complete named
definitions differ only in this function's size, from 12 to 440 bytes.
All 189088 protected data bytes across 720 owners, Makefile, and guard history
remain byte-identical. The ordinary build emits one O2/g3 compilation and no
C warnings. Existing duplicate generated_12D630 recipe warnings and the
expected development-image checksum rejection remain separately recorded.

## Focused qualification

Both mounted and sibling configurations pass seven fresh tests before and
after installation. The sibling overlay contains only the three new modules,
records its missing-pool-helper fallback, and preserves all 2434 inherited
dirty paths. Both shared smoke checks are fresh. Three unchanged shared
regressions per copy are explicitly reused by exact helper/test fingerprints.

| Check | Evidence |
| --- | --- |
| Independent ordered RAM model | 628 cases; all 110 target instructions reached; literal state agreement |
| Count and identity boundaries | Signed empty/negative counts, unsigned record bounds, full-word actors, flagged twelve-bit IDs, word/bit boundaries and first-match order |
| Live behavior | Descriptor-pointer/count/list mutations, fixed chosen path, preserved FP/S0..S7/RA/SP and floating saved roles |
| Original SDK shift | All eleven original words, 384 vectors over all 64 shift counts, O32 high/low arguments, original home stores and 64-bit loads/shifts |
| Native32 | 467 cases at each of O0/O2/O3, typed callback, SDK actor812/descriptor52/pointer32 sizes, valid arrays and trapping UBSan |
| Effective negatives | Stub, byte count, wrong row, truncated u64 mask, wrong ID mask, inclusive bound, wrong collision truth and short scan |
| Callers | All three JALs inventoried; two complete callers totaling 108 words, plus an original ten-word script window, eleven connected cases |
| Fault cuts | 210 executed-access cuts, including original SDK accesses, with identical literal modeled state |
| Relocation/image controls | Two independent GNU links of all fourteen bindings with signed LO16 carries; raw, binding and whole-image corruptions rejected |

The original `__ull_rshift` instructions execute in the bounded guest decoder;
they are no longer an opaque shift hook. The standalone negative initially
failed because the connected SDK map overwrote its modified root words. The
fixture now keeps standalone root words and asserts that the mutation is
actually installed before checking rejection. The alias reference also now
includes the opaque collision provider's deliberate argument-home writes.
A signedness warning in the native harness was fixed without changing the
candidate body. The final native checks also verify exact provider-call counts.

All three direct callers consume an integer identity or -1: the script path
adds 0x4000 to success, the six-ID actor predicate returns Boolean acceptance,
and the five-ID classifier returns effect 6 or -1. Their complete/window
instructions and ABI are checked against retail. No additional entry/interior
pointers occur in the whole original image.

Arbitrary wrapped addresses, sparse mask rows, private count rewrites and
argument-home aliases are guest contracts. Native checks use valid actor,
record and mask arrays. The decoder models the root's low-word O32 state and
the SDK's necessary 64-bit operations, not full hardware upper-register/FCSR
behavior. The collision provider `func_150A1DA0` remains a separate production
placeholder/bounded test service; its complete geometry and gameplay behavior
are not claimed. Routine task: zero Claude calls.

## Bank and next action

Production ELF SHA-256:
`42e11f4c8d50d9f6bff2b207c2fb38f3eb9bb087e0763578efc840eb58de5c3e`.
Binary: `e4751b676866920d8ce43e80bbca6b207006c2847802a3237000cdd4948a2261`.
Owner: `9726722bfe20717649264120061b95a593db4716461d64d716d31c7b57ff49a1`.

Reproduce from the consumer root under prepared WSL:
`python3 -m unittest tools.tests.test_game_actor_record_list_150a2aec_match -v`.
Canonical receipts: `conker/build/game-actor-record-list-150A2AEC-match/`.
Tools first, then source/docs/README aggregate rows/pin are committed locally.
No guard/Makefile edits, push or host/frozen Release work.

Next inspect `func_150A2940`, the adjacent 34-word record-parameter updater,
with its signed sentinels, byte store, live descriptor pointer and callers.
Keep the full 80% goal active. The `func_1513FAB4` layout study remains
uninstalled and uncredited at [Note 2171](2171-game-triangle-facing-match-20261107.md).
