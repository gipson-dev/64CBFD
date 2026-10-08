# Game Attachment Allocation Direct Conversion

Date: 2026-10-08

## Result

Continue [Note 1133](1133-game-attached-record-cleanup-direct-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
`func_151D7830` in [generated_204660.c](../../conker/src/game/generated_204660.c)
to complete semantic C. All **63 words / 252 bytes**, **frame 0x88**, emit
directly byte-exact under the existing IDO5.3 O2/g3 profile. **No guards**,
filler, pools, new globals, data, compiler-profile or Makefile changes.
VA 0x151D7830..0x151D792C, ROM 0x204CE0..0x204DDC.

Replace only its retained directive and add its local packet layouts and typed
declarations. Preserve [204660.s](../../conker/asm/204660.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_204660/func_151D7830.s).
All other owner routines and linked instructions remain unchanged.

## Recovered Contract

The 28-byte request contains owner+0x30 XYZ, unsigned duration 300, flags 0x76,
kind 0x12, mode 4, count 25 and a zero 32-bit value. Its two padding bytes at
+0x16/+0x17 are not initialized by retail and are not assigned a deterministic
C value by the fixture. Do not add memset or initialize the entire structure.

The separate 28-byte payload contains the original owner pointer, XYZ copied
before allocation and three positive-zero velocity words. Every payload field
is initialized; it has no padding on the qualified 32-bit layouts. The selected
source reads the same position object twice, preserving retail raw-word copies.
There is no arithmetic on those position values in this helper.

Call func_15147A80 with eleven supplied arguments:

```text
request pointer, 32, 28, 13, 16, 16, 0, 0, NULL,
unsigned owner[0xC], unsigned owner[1] promoted to s32
```

The O32 boundary uses four register arguments and seven stack arguments.
Allocation failure returns without reading record+0x98, copying nested storage
or writing the owner attachment slot. On success, load the fresh nested pointer
at allocated record+0x98, copy all 28 payload bytes, then store the captured
allocated record to original owner+0x28. Constructor/copy mutations and volatile
GP/FP clobbers must not cause a late XYZ reload, use of memcpy's return pointer,
or premature owner attachment. The observed direct caller ignores a return;
the typed void interface does not expose incidental V0 state as a new API.

## Fitting

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_attachment_allocation_candidates.py)
retains **41 measured forms**: 33 ordinary forms, including the 24 complete
declaration-order permutations, and eight effective negatives. Natural packet
construction without a shared position pointer emits 63 words/frame0x80 with
17 differences. The first position-pointer form recovers frame0x88 but has
15 local-slot differences. Declaring record, payload, request, position in that
order reproduces all 63 words directly. The pointer is used for both meaningful
position copies; no dead padding local or synthetic instruction scaffold is added.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 63 | 0x88 | 0 |
| O2 | 63 | 0x88 | 43 |
| O1/g3 | 71 | 0x78 | 70 |
| O1 | 71 | 0x78 | 70 |

Isolated compilation has zero diagnostics and pools. Two R_MIPS_26 relocations
at +0xC0/+0xD8 retain symbolic constructor and memcpy calls. No normalization
or guard-history edits are necessary.

## Qualification

[Eight focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_attachment_allocation_match.py)
reuse TriangleOracle, CopyOracle's signed-byte operation, native32, the owner
compiler/parser, actual padder and historical guard checks. The independent
public reference models packet fields, call order, required loads, byte copies
and final attachment; it does not compile or call the production body.

- **4,114 guest cases** cover both unsigned-byte values independently across
  all 256 values, raw zero/signed-zero/subnormal/finite/infinity/NaN XYZ,
  allocation success/failure, owner-as-record and three destination alias
  layouts. Five public mutation modes change XYZ, owner slot, nested pointer
  or copy return; two additional cases overwrite incoming register homes.
  All 63 words are reached. Full selected/retail GP/FP, private memory and
  access traces agree, plus independent public state/call/trace expectations.
  This is not the full byte-pair guest Cartesian product.
- **632 required fault prefixes**, plus two lazy-failure cases mapping only
  necessary owner fields, preserve complete partial retail/compiled state and
  independent public prefixes. Null nested storage and an unaligned allocated
  record fault as expected. An odd byte-copy destination is separately valid
  in the bounded byte-copy hook; this does not qualify the actual SDK memcpy's
  unaligned implementation. Guest mapping/alignment checks are not portable
  C fault semantics or N64 CP0 exception metadata.
- **138,752 actual native32 C executions** cover all 65,536 byte pairs with
  allocation success/failure, plus 7,680 mutation/alias checks. A volatile typed
  call invokes the actual C body; fixed offsets independently check every
  defined request/payload field and all 1,024 arena/canary bytes. Request padding
  is deliberately not inspected. Prepared aligned, no-strict-aliasing native32
  pointer/float representations are qualified, not universal ISO C alias,
  pointer or NaN-representation behavior.
- **41 compiled forms / 2,970 ordinary executions / eight effective negatives**
  discriminate wrong count/duration/flags, post-allocation XYZ reload,
  owner-before-copy attachment, short copy, signed player byte and use of
  memcpy's return as the allocated record. Unsupported instructions cannot
  count as successful negative controls.
- Copied full owners preserve **22 neighbors**, all relative relocations and
  normalized data/rodata pools. Four pre-existing pointer/integer warnings at
  func_151D7404/func_151D8764 call sites remain identical; none added or hidden.
  Real padder emits exactly 252 bytes without filler or guards. **Six independent
  links / 180 executions** verify both independently calculated R_MIPS_26 words
  across low/high/carry-boundary entries and freshly rebased callees.
- **64 connected cases / 128 compiled-and-retail executions** install the
  complete original 115-word func_15147A80 constructor, complete 81-word
  func_151D7264 caller, both, or neither. Each exercised function returns through
  its real epilogue. The caller's allocation arm and constructor's null arg8 /
  zero arg6 arms are covered, not their entire alternate-branch domains.
  Original allocation requests exactly (0x4D, category, 892, 1, player, 1);
  record+0x98/+0x94 become record+0xA0/+0xC0. Check copied request fields,
  attached payload, counters and cleared state. No lazy player-global read.

The last connection uses the **original retail constructor**, not the live
linked C implementation: generated_174BF0.c still has its zero-return
placeholder. This conversion does not restore that constructor. Allocation,
SDK memcpy/bzero, callback and floating distance remain bounded hooks; actual
hardware, alternate caller gates and gameplay parity remain open.

Two initial fixture failures were corrected before installation: an odd
byte-copy destination was incorrectly expected to fault, and the signed-byte
negative needed existing CopyOracle LB support. The first ignored audit launch
also lacked PYTHONPATH; rerunning with PYTHONPATH=. passed. No production fix
was inferred from these fixture/setup failures.

Fresh pre-install **eight tests pass in 84.000s**, no skips. Fresh installed
**eight tests pass in 54.737s**, no skips. Ten shared word-patch/PC16 tests pass
in 0.043s. Both tools project checks, candidate CLI help and syntax checks in
both mirrors pass. Previous unchanged neighbor-suite results remain historical
receipts, not fresh full-suite or gameplay claims.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` exits 0. Only this owner
recompiles, then relink/progress run. Four pre-existing owner warnings and
duplicate generated_12D630 recipes remain; this is not a warning-free build.
`make -C conker match-progress NON_MATCHING=1` also exits 0.

Fresh audit compares `game-attached-record-cleanup-test/after.json`:

- All **6,058 function bodies, addresses and extents** unchanged: 6,042 retail
  rows plus 16 overflow symbols. Init/init-data/debugger/game-data unchanged.
- All **720 game-data owners / 189,088 bytes** remain exact. The complete
  attachment helper and original gate caller match retail in the linked ELF.
- All **11,155 guard rows** unchanged; zero new guards. Reference assembly,
  Makefile and raw CSV fingerprints are unchanged.
- Exactly one progress row changes: func_151D7830, 252 bytes, asm -> c.
- Total converted **5,478 / 6,042 (90.67%)**, bytes 1,934,096 / 2,256,728 (85.70%).
  Game **4,805 / 5,321 (90.30%)**, bytes 1,762,660 / 2,072,880 (85.03%).
- Byte-exact **3,389 / 5,478 (61.87%)** overall and **2,716 / 4,805 (56.52%)**
  Game; 2,089 still different, zero address drift. Init 492/492 and debugger
  181/181 remain exact.

Ignored receipts live in `conker/build/game-attachment-allocation-test/`:
slot, guest, faults, native, controls, owner-padder, connected, installed,
audit-baseline, audit-installed, before-progress and new `after.json` baseline.
README updates aggregate tables only; detailed evidence stays in this note.

## Workflow And Next

Entry source `4356e8209b8b1fb689c26103b7dc894bccee98c5`, mounted tools
`6f18cf1f100b0c5fd2a05f18a007e831ca4085c5`, both clean. Pre-edit SHA-256:

```text
source: 24a2d3b9784354e6ae81ae6b9288fcd2787212aafdd748cba82f12fc64aae11c
reference ASM: 14c690097e848287eb8f9e5f3f1031cfa7c3fd65ebdb31075cdafc30a732fa48
Makefile: d5e4c8459b9bf1ac7485b913f559fe9e0242ec284d76cddf0650c210e2a73466
progress: 9e043978e57d0a6322562ea3127fd303098ac7863152bad44bb29073546ab1e0
guard CSV: d20b5a5057b8d3f58d2813799bb5e4be83e3b59772342a7d36a514ca93ded518
prior linked snapshot: 8baa2ad986ecfe229532c97cbd236ea01e2a47786b4ac80de6b7f6ec8ce35c0f
```

Zero Claude calls; routine fitting and ABI settled locally. No host/runtime/
save/editor/bridge/account changes; OGL Release remains frozen. Preserve the
older independently dirty standalone tools checkout; task files are mirrored
byte-identically without reset or a duplicate divergent-history commit.

Graph query exits 0 without a node. Refresh exits 1: 16,765 new nodes versus
38,553 existing; it refuses overwrite and retains 19,398 nodes from 2,972
excluded-but-existing files. No forced overwrite or ignore edits. Graph refresh
is not complete; a commit-hook background attempt is not proof of completion.

Next retained target **func_151D792C**, **67 words / 268 bytes**, frame **0x30**:
VA 0x151D792C..0x151D7A38, ROM 0x204DDC..0x204EE8. Recover the signed state/flag
gate, backward circular cursor, unsigned wrap count, live goal/state/global
reloads, captured ring buffer and final raw XYZ copy/zero return contract.
It calls the already qualified mixed-ABI velocity integrator. The previous
integrator note has bounded complete caller evidence, not fitted C for this
caller. Keep its assembly until copied-owner and current matching qualification
pass; wider Game/constructor/hardware/gameplay work remains open.

## Banking

Per "Keep commited", mounted tools
**56c4132b93e75ef9a5a8944f15a9edd22afd255d** banks the candidate and eight-test
fixture first. The parent source/docs checkpoint records that exact tools pin.
No push, reset, stash, unrelated staging or duplicate divergent tools commit.
Final verification checks **120 documents / 4,011 relative links / zero broken
links** and **29 byte-identical relevant tools files** across the mounted and
older standalone checkouts. Scoped diff checks pass. The wider Game goal stays
active; no pause or publication is implied by this local checkpoint.
