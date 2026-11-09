# Game actor height-result builder guarded match - 2026-11-09

func_1504715C now matches the complete **89-word / 356-byte** retail slot.
The semantic C emits **87 words** with its natural **0x18-byte frame**.
**54 expected-word/relocation guards**, including two measured load insertions,
restore retail's register scheduling and separate copies of shared loads.
This is a guarded match. The former semantic body emitted 85 words and four
padding nops; this checkpoint does not change the C conversion inventory.

Fresh production totals: **4,294 / 5,513 (77.89%)** total, **3,621 / 4,840
(74.81%)** Game, Init 492/492, Debugger 181/181, zero drift and **1,219**
different C functions. **117** more accepted matches reach at least 80%, or
4,411/5,513. The root README changes only these aggregate rows.

## Source and recovered behavior

Owner: conker/src/game/generated_71820.c. Retail: conker/asm/71820.s.
VA 1504715C..150472C0; ROM 7460C..74770. Note 779 remains the semantic
recovery record. The API is void, with output result first and actor second.

Make the stored entity index's one-based-to-zero-based conversion explicit
before both pointer construction and helper submission. Express the helper's
full raw-integer truth as a 1/0 ternary. Keep the existing implicit helper-call
convention: introducing its u8 return prototype here would change the caller's
wide truth test. The actual helper returns normalized 0/1; wide mocked return
words qualify this caller's emitted interface rather than expanding the real
helper's behavior.

Keep height publication before the actor flag read, all three coordinate
conversions before synthesized vertex stores, metadata after vertex writes
and cached before output flags, the entity-index snapshot before value writes,
and the fresh flag load after the callback. Preserve both result padding fields.
No layout, shared-header, prototype, helper body or compiler-profile change is
introduced. All 42 other owner bodies and bindings stay unchanged.

## Two measured load clones

| Compiled guard offset | Inserted retail word | Meaning |
| --- | --- | --- |
| +0x080 | lw t2,0x184(a1) | Metadata read in the synthesized path's branch delay slot |
| +0x134 | lw ra,0x14(sp) | Return-address restore in the nonzero path's branch delay slot |

IDO shares each load in a common block; retail keeps two static copies in
mutually exclusive paths. The complete algorithm already emits from C. The
insertions reverse this scheduling choice; each returning path still performs
one metadata read after its vertex writes and one saved-RA restore. Existing
expected-word/relocation checks anchor both insertions. No word is omitted and
neither insertion adds padding or a new algorithm operation.

Retail also contains one unreachable duplicate lwl at +0x88, after an
unconditional branch and before the stored-copy target. The full slot is exact,
including that word. Positive guest cases visit **88 of 89** normalized/retail
words and **86 of 87** raw words; the sole unreachable word is explicitly
accounted for rather than claimed executed.

## Focused qualification

Six target checks run before and after installation in both tools environments.
The sibling environment uses a read-only overlay for the six new modules;
its 2,434 inherited dirty paths and relevant path states are preserved. Each
receipt fingerprints task files and loaded helpers. The original twelve
actor/result tests pass freshly after installation in both environments.

- Independent guest contract: **1,400 cases per raw, normalized and retail
  body**, **4,200 executions**, plus **768 runs with the original 16-word
  func_15145C90 helper**, whose installed bytes are also verified exact, and
  **24 independent entry/symbol/stack rebases**.
- Cover stored/synthesized vertices, every selector bit, signed truncation and
  halfword wrapping within the qualified arithmetic domain, zero/large entity
  indices, helper-entry publication, wide raw truth, every post-helper flag
  byte, helper mutation of globals/actor/result, caller-stack output and three
  actor/output aliases. All public bytes, full output/padding, callback arguments
  and entry snapshots, saved registers and stack storage are checked.
- Native32 O0/O2/O3 with UBSan reuses all twelve contracts, including every
  entity index 1..65,535 and all 256 post-helper flags. Thirteen compiled native
  controls are effective at every profile. The same thirteen IDO controls have
  independent guest witnesses, including early/late metadata, low-byte truth,
  stale flags, wrong index/stride and padding writes.
- Both padders reject all 54 stale expected words plus a stale relocation
  specification, **55 rejections per padder**. Dropping or corrupting either
  inserted load is rejected by exact-body/extent checks in both padders:
  four insertion controls per padder. Scope, payload/binding and four independent
  whole-image corruptions are also rejected.
- The real recovered func_150BA930 caller executes with this builder at all
  three native profiles, including its null-result early return and full shared
  path to a bounded final func_15046C80 query. The helper's flag mutation and
  the final query return are preserved.

Stored structure copies with partial overlap, nonfinite/out-of-range coordinate
casts and signed coordinate-add overflow are outside the qualified C domain.
The qualified aliases preserve the metadata and flag ordering without relying
on partial stored-structure overlap. Native fixtures retain the existing
non-strict-aliasing policy. Hardware/gameplay acceptance and complete execution
of every retail caller are not claimed.

## Caller census and complete linked audit

There are **53 retail JAL sites in 53 callers**, no literal address values, and
**25 retained calls** in the current linked build. Twenty-eight calls are absent
in pre-existing non-matching caller bodies; the receipt names every such owner
and its linked word length. They are retained as an existing limitation. All
53 caller bodies are byte-identical to this checkpoint's baseline. No missing
caller is silently credited or described as running this builder.

The complete owner retains all 42 raw/padded neighbors, pools and register-usage
metadata. Both padders agree on all 43 functions. Actual unmodified Make in a
disposable tree produces the predicted padded object using ordinary -O2 -g3.
Strict whole-ELF prediction permits exactly the target slot and its symbol
extent change from 340 to 356 bytes: **232 changed bytes**, zero exclusions,
zero unexplained bytes and no symbol permutation. All **6,052** function
addresses, every other linked body, and all **189,088** protected Game-data
bytes / 720 owners stay fixed. Complete Init and Debugger images are covered
by whole-image equality.

Production Make compiles only this owner, and its object/ELF equal the isolated
predictions. Conversion CSV and Makefile are byte-identical; all inherited
guards are an exact prefix. Ordinary make all still reaches the inherited
whole-ROM checksum mismatch, exit 2. The fresh match-progress recount supplies
the totals above. Shared smoke checks pass in both tools environments; three
unchanged shared regression receipts are explicitly reused after exact helper
and test fingerprint checks.

Production fingerprints:

- ELF: `54ce42977a1ba599810c7b4839e8a936942b2e8b8869ac0bd745c41dab8600d2`
- Binary: `2389d5fb337304cfe42fea3c9c20f241d61e11d0b2110abd89da974aae868417`
- Owner object: `92fef567bc6d427805d30fad98757d558e3e4e3a61cb0aba64fc84ca22b82472`
- Guards: `5a88dba322b05e6953c09dd58e25f33fc99ec6f63b7f9d13cc0f88431d11ea32`
- Makefile: `8e676e04318f8645e6b277ed60ed9f221d8901a5e6a02efd279d478d46a615f8`

## Continuation

Graphify is refreshed with scoped AST work and fail-closed retention of old
unscanned nodes. Its receipt verifies source positions for all 41 C definitions
and accounts for the two retained assembly functions. This is not a full-corpus
semantic extraction. The tools commit precedes the consumer pin commit.

Next target: func_1513E13C in conker/src/game_169510.c, the recovered 90-word
vertex builder. Re-query the graph, inspect its complete retail body, signature,
float lifetimes and callers before choosing a source probe. It is uncredited
and still needs every source/ABI, owner, guest/native, Make, full-image,
production/recount, documentation and commit gate.

The separate func_1510D404 investigation remains non-matching with its private
compiler traces retained. No wide-temporary frame fit is adopted. No sibling
tools work, host-port source or frozen Release artifact is changed.
