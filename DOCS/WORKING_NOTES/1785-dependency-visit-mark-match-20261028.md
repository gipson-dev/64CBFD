# Dependency visit and mark - guarded C match

Verified 2026-10-28. Restore func_1509CE64 in generated_C9EC0:
VA 0x1509CE64..0x1509CF28, ROM 0xCA314..0xCA3D8, 49 words / 196 bytes.
The existing O2/g3 no-unroll profile emits the complete semantic routine with
a 56-byte frame and all four retail relocations. Sixteen checked word guards
normalize register allocation, an equivalent zero-extension transfer and the
symmetric loop comparison. Raw compiler output is qualified separately; it is
not a direct, unguarded instruction match.

## Recovered behavior and interface

The interface is void func_1509CE64(u16 *dependency, void (*visit)(s32)).
Walk a halfword dependency list until its 0xFFFF terminator. For each entry:

1. Call visit with the unsigned halfword promoted to a signed 32-bit argument.
2. Reload the current list entry after the callback; set its byte in
   D_800D2E70 to 3.
3. Reload that same entry after the state store, then advance the cursor.
4. Reload the bitmap pointer D_800D2E4C and OR the selected bit into its byte.
5. Read the next list entry and test the terminator.

Both list reloads matter: the callback can change the current entry, and a
state/list alias can change it again. A callback-written 0xFFFF is still used
for the current mark; the sentinel test applies to the loop's next entry.
Existing bitmap bits are preserved, and a callback's new bitmap pointer is
observed. Empty lists make no calls or marks.

The owner already has the recovered local bitmap pointer declaration. Keep
that local definition and the existing shared headers. Replace the false
s32/no-argument declaration with the typed void interface. The original
func_1509CCB4 caller now loads its list through u16 **; this type correction
changes no caller instructions. All 18 owner neighbors and their bindings and
pools remain unchanged. Selected, owner and Make compiler diagnostics are empty.

## Original callers and recursion

The aligned ROM census finds one direct call at ROM 0xCA18C / VA 0x1509CCDC,
inside the complete 16-word func_1509CCB4. There are no target pointer literals.
That parent loads a list from D_8008743C using a 20-byte table stride and passes
itself as the visitor. The eight-word func_1509CC94 wrapper invokes the parent.
Both original callers remain byte-exact.

The qualification executes the complete parent, wrapper and restored routine,
including the actual recursive callback. Its 64 cases cover empty lists,
shared dependency graphs, repeated children and depth-eight chains, with two
stack phases and four bitmap seeds. Every original instruction in both callers
executes. Cyclic lists retain the original unbounded recursion; six bounded
fault prefixes verify that no depth limit or cycle shortcut was introduced.
This is function-level execution evidence, not a full-game acceptance claim.

## Checked instruction normalization

The 16 guards are derived from decoded register fields and expected compiler
words. They do not insert or omit instructions or change relocations, frame,
saved-register lifetime, call placement or memory access order.

| Offsets | Qualified transformation |
| --- | --- |
| +0x2C / +0x38 / +0x3C | Entry halfword in T6 instead of V0; ANDI 0xFFFF instead of OR zero after LHU |
| +0x58..+0x8C, twelve words | Closed scratch-register allocation exchange during live state and bitmap updates |
| +0x94 | Swap the symmetric BNE comparison operands |

All 65,536 possible entry halfwords reach the same entry join and saved value.
Three GNU linker layouts exercise HI16/LO16 carries. The four global bindings
remain at bitmap +0x34/+0x48 and state +0x40/+0x44. The indirect call remains
at +0x50, with its A0 update in the delay slot at +0x54.

## Qualification and production

Both tools copies pass eight fresh canonical methods and shared tools checks.
After production, both pass two fresh installed methods; the six unchanged
semantic methods are reused only with exact input, module and artifact hashes.

- 464 guest cases visit all 49 words and compare the raw C, normalized output
  and retail routine. They include callback mutations, every bitmap byte seed,
  high halfword indices, repeated entries, outgoing argument-home clobbers and
  state/list/bitmap aliases. Raw C preserves public state, memory, calls and
  access order; normalized output also preserves complete machine state.
- 141 access-fault prefix pairs preserve full state, trace, PC and delay slot.
  Six additional prefix pairs execute actual recursive cycles.
- Native32 O0/O2/O3 each pass 65,536 cases with trapping UBSan and complete final
  state and both bitmap images checked. Nine semantic controls fail in each
  profile; nine independently compiled IDO controls fail in guest execution.
- Three GNU layouts pass 54 further guest cases. Three raw/binding corruptions
  and six full-image corruptions are rejected. Actual generated-padder output
  agrees with the qualified object.
- The actual three-command Make recipe uses its existing no-unroll profile.
  It reproduces both compact and padded owner output. Make retains its known
  unrelated duplicate generated_12D630 recipe warning.

The immutable qualification seal covers 16,393 paths and 379 focused inputs.
Production reproduces the independent entire-image prediction: exactly 152
changed bytes, comprising 151 code bytes and one symbol-size byte (12 -> 196),
with zero exclusions. All 6,056 addresses, 6,055 other linked bodies and 720
protected Game owners / 189,088 bytes remain unchanged. Sixteen rows are
appended to the guard manifest; every inherited byte remains intact. The
Makefile, retail layout, conversion inventory and other objects are unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler body | e62bdff65d663a9e7de1e336da5ffc94f7822e0291f3bded9d1d8ad98cd96579 |
| Normalized original relocatable body | 9529ee3276fcdcd94801d0439686e07682301a6556621f50aeb61d12f92cde82 |
| Linked retail slot | 75abdaee22efa95a287fe07c426d1fec36372a19725011f53ae464bb516acd36 |
| Adopted owner object | 489b42c48aec311770b4bc0176c940f012e9314c75a36cd2bdb4c00c63438fad |
| Adopted ELF | feea5868de3eb5a9938f2a171c6268d8cccf142a99567e2e793520f91c2fc7a1 |
| Guard manifest | 91cfc61697b2f874f74475c5dadac1faec1f2e3c4f2a515d593b62d15b71ba03 |

## Bank and measured progress

Predecessor consumer: 963b9120fec7fad4107f78313dab31196730cab1.
Tools committed first: 26ab7c6f8712ddfd6ccce50ae0ef5193d75f5c7a.
The consumer commit records this source, guard append, tools pin and measured
docs. No push is performed. Preserve all 1,796 inherited older-mirror dirty
paths and the three new qualification modules; do not reset or commit that mirror.

| Section | Byte-exact C | Address drift | Different |
| --- | --- | --- | --- |
| Total | 3,863 / 5,506 (70.16%) | 0 | 1,643 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,190 / 4,833 (66.00%) | 0 | 1,643 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

267 more exact functions are needed to reach 4,130 / 75%. Remaining source
shapes: 1,514 placeholders, 120 semantic/other and nine unlocated. This function
is the only newly credited entry. Keep func_1514E920 parked and uncredited.
Next inspect func_151140C4 in generated_13D350; screening alone earns no credit.

Retained evidence: conker/build/game-dependency-visit-mark-match/ contains
preparation.json, both canonical/installed receipts, sealed-production-proof.json,
sealed-live-adoption-audit.json, canonical-function-views.json and
75-percent-queue.json. The final handoff records the consumer commit, scoped
graph refresh and independent closing audit. Root README changes only totals.
