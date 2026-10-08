# Game Effect Record Updater Match

Date: 2026-10-06
Baseline: `279975fc` ([Note1063](1063-game-context-classifier-match-20261006.md)).
Continue the Game matching goal with the positive-count helper used by the
banked effect dispatcher and checked direct caller. Original N64 source
recovery, not host-port adoption or complete gameplay acceptance.

## Retail Contract

`func_15141E38`: **80 words /320 bytes**, frame **0x60**, VA
**15141E38..15141F78**, ROM **16F2E8..16F428**, owner
[`game_16EE20.c`](../../conker/src/game_16EE20.c). Recover typed ABI
`void func_15141E38(u8 *actor,s32 index)`; callers do not consume a result.
Incidental guest V0 is not a native scalar-return contract.

Read the live actor+2F4 list head, search type1A through a private cursor at
SP+58, and inspect each returned node's record+10. Compare the full32-bit
selector at record+28 against index. **Every matching record** receives the
current table count's low16 bits at record+E; retain the last matching node,
advance through the live cursor's next+14 and continue searching. Do not stop
after the first match or cache the count before helper calls.

If any match exists, return without allocation. Otherwise construct the
request at SP+40: index word+0, actor pointer+4, unsigned actor byte3B at+8.
Bytes9..11 are uninitialized private tail bytes, not implicit zeros. Call
`func_15149130` with signed table halfword+6, -1/-1/-1,1,50,12,255,1. Null
allocation stops before copy/link. Non-null allocation is kept across memcpy;
copy12 bytes to record+28, then `func_1514EC1C(record,live actor,0x1A)`.
The actor argument is reloaded from its N64 parameter home after copy.

The helper itself has no range/disable/callback/count-positive gate. The
already exact37-word `func_15141DA4` owns those checks; the100-word dispatcher
has its own positive-count branch. Guest-only bounded invalid-array indices
do not establish legal out-of-array access in native C.

## Source And Closed Derivation

[Maintained driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_effect_record_updater_candidates.py)
screens separate/shared created-record lifetimes, private/plain cursor stores,
inner/outer request scopes and four actual-SDK profiles: **32 controls**, empty
standalone diagnostics. Select the separate created-record local and outer
**12-byte** request with the private cursor store under existing O2/g3.
It emits80 words/frame0x60, **56 direct /24 different**. No compiler-profile
change, larger invented payload, frame rewrite, insertion or omission.

Exploratory receipts include64 lifetime/declaration/extent/cursor controls,
120 declaration permutations and eight alternate12-byte packet representations.
Larger unused workspaces are not installed. The separate created pointer
recovers the original frame and allocation-result saved-register lifetime;
remaining differences have a closed derivation:

- Pre-allocation raw cursor/index/match registers S0/S1/S2 map to retail
  S2/S0/S1. Close the entry saves and prefix order; allocation result and all
  final restores keep their existing retail register phase.
- Hoist independent search-key/result-pointer preparation before the selector
  branch. Its skip target advances to the live next-link read, not backward
  to the hoisted preparation. Close the index-shift/actor-store schedule.
- Replace the equivalent cursor-pointer store with SP+58 and replace the
  following extra private reload with the live T4 move. Bind that raw read
  exactly to initialSP-8 and the value just stored, not arbitrary frame reads.
- Move index/actor/identity stores and memcpy source from private SP+44 to
  retail SP+40: **four private-home guards**. This also preserves the exact
  original byte provenance for the three uninitialized tail bytes.

All24 changed offsets are relocation-free. Preserve all nine original call/
table relocations unchanged. Guards append after the existing10785 rows;
stable canonical prefix SHA-256:
`3dab8eceb937516ba0c03ffcef9a1bcd29f8dd9dd6e4cf62790ed3e903cbe077`.
No whole-function retail replacement or restored switch-pool changes.

Use `(s16)D_8008A0B4[index].unk4` for the constructor count: IDO emits the
original big-endian halfword load+6; native C retains low16-bit semantics
without a host-endian raw halfword reinterpretation. The existing SDK's seventh
constructor parameter is historically typed `struct37 *`; retain its literal
numeric size-12 cast locally, do not broaden this recovery into shared-header
cleanup. Native fixtures treat it as the original numeric size protocol and
never dereference it or claim original allocator execution.

## Qualification Boundaries

[Eleven maintained tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_effect_record_updater_match.py):

- All80 normalized words equal retail. Actual padding emits320 bytes with
  unchanged relocation metadata. Alternate table90018004 exercises signed-low
  HI16/LO16 carry at both table references; stale expected guards fail.
- **7680 three-body guest cases** cover four valid indices, ten full-word
  counts, eight list shapes, success/failure, six helper mutation modes and
  two SP phases. All80 words reached on raw/normalized/retail. Counts remain
  live after each search, every match refreshes, shared records/list links are
  exercised, and allocation/copy/link order and failure gates agree.
- **17600 extra raw private-cursor reads** are bound at one exact opcode/site
  in that matrix. No assertion that raw full traces equal retail is made.
- **1728 connected cases** execute all23 original list-search words with
  three indices/counts, eight lists, allocation failure/mutation, three output
  destinations and two SP phases. Aliased output points into actor storage or
  existing record storage; all other external bytes are compared.
- **36 guest-only actor-home probes** mutate the parameter home during copy;
  link receives the updated actor. Nonuniform stack poison deliberately makes
  all36 raw tail-byte triples differ from retail. Raw copies must come from
  their own untouched private tail bytes. Normalized and retail compare
  **complete traces and complete storage**, including exact copied padding.
- **7680 actual32-bit native cases** compare all helper calls, nine initialized
  request bytes, global tables and every other external storage byte across
  refresh/create, failure, live helper mutations and three output aliases.
  Only the three copied, unspecified request-tail bytes are excluded; native
  private actor-home aliases and deterministic padding are not claimed.
- **3072 three-body guest caller cases** execute the original37-word checked
  caller, compiled/raw/normalized updater and original23-word search. **1536
  native cases** execute its actual owner C with the recovered updater. Range,
  disable, null classifier/callback and signed nonpositive-count gates retain
  their original behavior. Caller20 is rejected while standalone helper20
  is a valid mapped test index.
- Full-width selectors/high-bit aliases and bounded guest-only indices-1/21
  preserve the absence of a new helper gate. Missing storage and cyclic lists
  fail strict mapped-read/instruction-budget gates, not native/hardware faults.
- Ten compiled negatives: placeholder, first-match early return, wrong
  selector/store width/count, cached count, wrong constructor flag/duration,
  short copy and missing link. Each must change calls or known storage on
  valid mapped inputs; compiler differences/faults do not count as acceptance.
- Copied actual-SDK owner has93 functions; only target raw words change, all92
  others' words/relocations and the existing608-byte pool remain unchanged.
  Typed void actor-pointer declarations remove one existing pointer-conversion
  warning:3->2, the remaining code/statement/caret diagnostics stay unchanged.
  Production binds complete target/caller/classifier slots and the old guard
  prefix, not a historical Git-object or ignored-test-fixture dependency.

The first ignored shape wrapper had an indentation error; dedent the borrowed
compile block. The first closed branch derivation mistakenly moved its skip
target backward with the hoisted argument instructions; explicitly resume at
the live next-link read instead. The first connected-case assertion incorrectly
doubled1728 to3456, and the negative oracle over-constrained candidate private
cursor homes. Correct the counted product and bind negatives to their actual
mapped private result pointers. A guest-only -1 reference initially omitted
32-bit address wrapping; use masked table addresses. These are recorded harness/
derivation corrections; positive gates still require actual semantics and bytes.

## Production Verification

Explicit ELF rebuild passes. Compared with `279975fc`, all6059 slot addresses/
extents stay fixed and **only func_15141E38 changes**. All80 linked words equal
retail. Dispatcher100, actor45, context57 and checked caller37 words remain
byte-exact. Target SHA-256:
`b3334c09d609054614bbdb3981bbf2ddbe33f8af2a1ffd5230daf23855cc88ec`.
Old10785 guard rows are unchanged; append24 for a total **10809**. Protected
`.init`, `.init_data`, `.debugger` and `.game_data` addresses/hashes unchanged.
All720 Game-data owners /189088 bytes match, zero differing owners/bytes.
Owner warnings3->2, no new warnings; the full build is not warning-free.

Regenerated conversion counts/byte coverage remain5464/6042 total,4791/5321
Game,85.57% total bytes/84.89% Game bytes. Exact total **3339/5464 (61.11%)**,
Game **2666/4791 (55.65%)**, **2125 different**, zero drift. Init492/492 and
Debugger181/181 stay exact. Linked-function qualification, not a complete
matching-ROM checksum or gameplay claim.

All56 focused post-link tests pass in430.719 seconds, no skips/errors/failures:
11 updater, eight actor classifier, eight context classifier,11 dispatcher,
five actual padder and13 earlier production/guard-metadata methods. This does
not rerun the complete semantic suites for those13 earlier routines.
Documentation:46 documents/3509 relative links/zero broken. Project tool,
scoped Python syntax and `git diff --check` gates pass. Ignored audit,
full-owner, native/guest, padding and regression receipts:
`conker/build/game-effect-record-updater-test/`.

## Next Function

Continue **func_15141F78**,96 words /384 bytes, frame0x78, VA
15141F78..151420F8, ROM16F428..16F5A8. It remains a production placeholder
with a partial commented draft. Recover its descriptor/RNG and sixteen-argument
`func_1513C650` call, not an unverified transplant of that draft.

1. Recover six input types, byte truncations, float-bit homes and void/result
   ABI from actual callers. Keep the initialized descriptor at SP+50 and its
   uninitialized padding distinct from initialized fields.
2. Preserve two ordered integer RNG calls: unsigned remainder61+100 and
   `(word&0x7F)+128`. Re-read source+18 afterward, then take the float RNG sample.
3. Preserve separate multiply5/add10/multiplyscale operations, source and
   position reads after the random providers, mode==2 boolean and low-byte tag.
4. Retail's A3 is **the address source+4**, not a dereferenced source word.
   The old commented draft uses `arg1->unk4` and is therefore not sufficient.
   Bind all sixteen scalar/float argument positions and their order.
5. Qualify aliases/provider mutations, finite/special floating behavior,
   actual SDK profile/frame/padding, semantic negatives, typed callers and
   all-slot/protected-data audit before installing the next routine.

Root README receives aggregate rows only. No allocator/list-link helper C
restoration, sibling source/build/save, frozen Release, runtime launch,
host adoption, hardware/FCSR/gameplay acceptance or push.
