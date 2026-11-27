# Attachment-vector paired effect guarded match - 2026-11-26

`func_150FB324` replaces its zero-return placeholder in
`conker/src/game/generated_126F60.c`. Semantic C emits **100 words** with
the retail **160-byte frame**. **22 expected-word guards and one duplicated
incoming-owner-home load** recover all **101 body words**, followed by two
literal zero alignment words in its **103-word slot**. Seventy-nine raw words
need no replacement. This is a guarded C match, not a raw compiler byte match.
VA `0x150FB324..0x150FB4B8`; slot through `0x150FB4C0`.
ROM `0x1287D4..0x128968`; slot through `0x128970`.

Production: **4,707 / 5,528 (85.15%) total**, **4,034 / 4,855 (83.09%) Game**,
Init492/492, Debugger181/181, zero drift,821 still different. One matching
credit; no conversion-row, denominator, parent or helper credit. The active
**90% goal currently requires4,976 matches:269 more**.

Recovered entry: `void func_150FB324(struct127 *owner, u8 selector, s32 context)`.
Names describe observed roles; the original effect names remain unknown.
Use canonical struct127 attachment offset1D4 and canonical 12-byte/alignment4
struct17 fields unk0/unk4/unk8. All four global vector presets are copied
before the attachment-null gate. The contiguous48-byte table at
D800A1D30..D800A1D60, ROM2467F0..246820, contains
(-108,-9,85),(-150,-9,111),(-32,4,40),(-21,15,40).
SHA256 `24c0e4343bfeb74e332961c762a8ca610d00cb6208b6687f3296f6ebfb39d2e3`.
The source retains external presets rather than replacing them with literals.

With an attachment, transform presets0/2/3 into point/origin/direction through
the same matrix at attachment+380; the pointer-array helper advances its
input/output cursors, not the matrix. Subtract originXYZ from directionXYZ,
in the original three SUB.S operand/register/order sequence. Then call
150FEC28(owner,14,preset0,preset1,point,selector,context), followed by
151D4408(origin,direction,cachedMatrix,owner,1.f,selector,context).
The first helper consumes its second formal as u8, proved by LBU from the
homed argument. Both helpers consume the selector byte and full context
word. The last helper's original C formal spelling remains inferred from
consumption and callers. Return values are discarded.

The matrix helper117-word, first backend66-word and last backend152-word
slots are pinned to retail/frozenELF. Their static bodies establish argument
widths and relevant footprints; effect backends remain opaque dynamically.
The native and guest fixtures actually allocate3C0 bytes for each bank,
covering the complete64-byte matrix at380. This is a bounded accessible-bank
contract, not a proof of every retail allocator's extent. The nominal
struct255 header is only a prefix view and is not used to underallocate a bank.

Source fitting retained complete semantic bodies and the production O2/g3
profile. Declaration/order/scope, pointer-type and capture screens recovered
the original frame with a real owner capture and block-local pointer arrays.
Automatic pointer-array initializers rejected by IDO warning851 were discarded;
there is no warning suppression, gratuitous volatile, dummy local, padding
object or address escape. Eighteen additional call/capture/declaration screens
did not improve the bound56-word positional difference count. Much of that
count is the one-instruction shift, rather than distinct semantic differences.

Normalization is derived from a14-word private-home bijection (hex offsets):
raw44->retail78, raw48->retail74, raw4C..78->offset-8. RA24, incomingA0/A4/A8,
outputs94/88/7C, input array38/3C/40 and output array2C/30/34 remain fixed.
Pointer-valued input-array cells and the first backend's stack pointer argument
receive role-aware value mapping, not just byte-address remapping.

Retail repeats the stable incoming owner load atC4. The raw stream reusesT5
fromB4; no intervening call or owner-home store occurs. The insertion restores
that read toT1, redirects the attachment base, increases the null-branch
displacement by one and shifts subsequent bindings by four. Two closed GPR
role permutations and one ten-instruction argument-preparation permutation
complete the derivation. All24 reversed instruction pairs are mechanically
checked for GPR/FPR/FCSR and exact byte-memory dependency independence. All
COP1 words and their order stay literal. No FP commutative rewrite is used.

**Raw fault order is intentionally not called identical.** Moving independent
incoming-home loads/private stores can change the state at a memory fault.
Four literal streams retain every full private/register/FP/FCSR/access/PC/delay
fault comparison. Separately, raw successful runs prove the whole frame,
private pointers, consumed operands and access events under the explicit
instruction permutation;214 raw fault prefixes retain their own access order,
event values and FP/call prefixes. Three explicit extra-read fault/stutter
boundaries prove the stable home value without hiding the extra access.
The relation assumes ordinary mapped o32 stack homes and disabled FP traps;
it does not claim equivalence under asynchronous stack writes or arbitrary
memory-fault injection into a different schedule frontier.

Validation:

- All17 raw neighbors/pools remain fixed. Both complete padders reconstruct
  the frozen BEFORE owner and emit identical AFTER objects. The actual normal
  three-command Make recipe agrees without new diagnostics/profile changes.
- Guest:256 cases per five streams; all101 retail body words executed;
  217 full literal fault-prefix quadruples,214 raw prefixes and3 extra-home
  boundaries. Independent public-memory/calls/vector-packets/ordered-FP/FCSR
  reference includes four rounding modes, signed zero, subnormal/overflow
  inputs, helper clobbers, public/preset/attachment changes and guest-only
  incoming-home changes. Five semantic negatives cause comparison differences;
  the sixth rejects an invalid transform-count helper contract.
- Original caller func150265CC: all3,451 retail words pinned,32 executed on
  bounded paths through its37-entry jump table, actual ownerSP764/selectorSP773
  loads, third argument1, actor type86(hex), null/default routes and full
  epilogue.384 cases/stream,128 connected children, three return poisons prove
  V0 is overwritten with1. **The current production parent remains its12-byte
  zero-return stub.** This is original-retail caller evidence, not a claim that
  the production parent is restored or that the full original parent ran.
  One aligned plain JAL and no aligned plain pointers were found in the
  original input; derived/script/compressed references are not excluded.
- Native32 actual C:2,048 cases at each O0/O2/O3, three translation units,
  frozen canonical actor prefix, asserted offsets/vector layout, full3C0 bank
  allocations, all initialized actors/banks/presets, vector packets, calls and
  MXCSR compared. Strict aliasing, UBSan traps and LTO type checks pass.
  Twelve defined negative controls exit42 through comparison; no signal/trap
  is counted as success. Two controls initially left an unused local; their
  dead declarations were removed. The output-routing control swaps two fully
  initialized destinations, avoiding an uninitialized-data negative.
- Both padders reject44 guarded-word corruptions and expose156 unguarded-word
  and22 relocation corruptions. Oversized bodies are rejected. Twenty actual
  GNU links cover four jump regions and signed HI16/LO16 carry boundaries,
  with100 rebased guest runs including raw/private schedule relations.
- Independent full-image prediction uses frozen before-C and original ASM,
  then equals actual Make-linked/production ELF byte-for-byte:428 changed
  bytes, zero exclusions. Protected data189,088 bytes across720 owners and
  all neighboring functions/addresses/extents remain fixed. Existing guards
  are an unchanged prefix; only the22 qualified rows are appended.

| Phase | Seconds | Coverage |
| --- | ---: | --- |
| preinstall-primary | 169.198 s | 5 fresh / 0 reused |
| preinstall-sibling | 106.189 s | 5 fresh / 0 reused |
| installed-primary | 92.032 s | 5 fresh / 0 reused |
| installed-sibling | 101.09 s | 5 fresh / 0 reused |

All20 target tests are fresh; primary/isolated-sibling task, dependency,
data and artifact fingerprints agree. Shared tools-check passes. Unchanged
broad suites are not reported fresh. Frozen inputs:4121;
copies:3073. The separately dirty real tools sibling is
preserved. Tools commit:`cfcd5c09d74effb84112531ca51f75c00e9b1623`.
Baseline consumer:`eb5d2497503940e1f2565894883b2e7bf2092569`. Receipts:
`conker/build/game-attachment-vector-effect-150fb324-private`.

One completed packet-only Claude review (no tools/writes) offered unaccepted
layout hypotheses. No further Claude call, no subagents. The host's generated
target remains a stub; no host transfer/build/launch or Release change.
Scoped Graphify refresh audits18 current owner definitions and retains old
IDs/qualification metadata after observing actual hook termination. No full
corpus re-extraction claim. README receives aggregate rows/date only.
Continue from sealed N73 toward90% with another unmatched Game routine.
