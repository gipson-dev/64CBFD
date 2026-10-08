# Game Point Transform Assembly To C Match

Date:2026-10-06. Baseline:`1412e18e`
([Note1072](1072-game-texture-resolver-match-and-table-binding-20261006.md)).
Convert only `func_15143134` from its preserved original assembly inclusion to
semantic C. Keep the original assembly reference. No other production routine,
profile, shared header, padder algorithm or sibling project changes.

## Recovered Contract

Retail:98 words/392 bytes, frame0x78, VA15143134..151432BC,
ROM1705E4..17076C. Three-input ABI:float point pointer, float output pointer,
generic matrix buffer pointer. The last is a fixed Mtx when D_800C3E90 is
nonzero, otherwise a float4x4 matrix. The routine does not return a value.
Correct its local false s32/no-argument declaration, without broad caller edits.
Some original callers pass an unused fourth register argument.

Diagnostic D_800DCA00 must remain volatile:all intermediate status writes are
observable. D_800DCA04 records the matrix pointer; D_800DCA08/0C/10 record the
input point before conversion. Preserve input rereads after guMtxL2F, including
helper mutations and aliases. Do not cache those coordinates across conversion.

| Path | Status Writes | Work |
| --- | --- | --- |
| Null or all-zero point |1,7,8,0|Translate matrix index0 with func_15142314; leave diagnostic point/pointer untouched|
| Nonzero, fixed matrix |1,2,3,4,0|Copy diagnostics, convert into private float4x4, transform, clear and return early|
| Nonzero, float matrix |1,2,5,6,0|Copy diagnostics, transform original buffer, clear|

Equality treats both zero signs as zero. NaN comparisons enter the nonzero
path in the bounded instruction oracle. Do not infer hardware FCSR exception,
rounding-mode, signaling-NaN or payload acceptance from that oracle.
Output pointers and callbacks may alias diagnostics/input; the status sequence
above describes ordinary non-aliasing inputs, not immutable diagnostic storage.

## Compiler And Guards

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_point_transform_candidates.py) retains
17 shapes under O2/g3 with plain/volatile declarations:34 measurements. Shapes
cover direct versus explicit status pointer, inverted zero equality, separate
outer clear, goto, per-write volatile casts, array/struct global storage and
register-qualified arguments. Four SDK profiles are separately checked for the
selected body. No alternate compiler profile is installed.

Shared-final-clear baseline:97 words/frame0x78/39 differences. Adding the
retail fixed-path clear and early return recovers98 words/frame0x78 with only
31 allocation/saved-store words different. Dropping volatility can remove
observable intermediate writes and does not qualify as a restoration.

Retail keeps point/output/matrix/status in s0/s1/s2/s3. IDO's selected C keeps
them in s0/s2/s3/s1. Normalize that closed s1->s3, s2->s1, s3->s2 cycle through
31 existing-schema expected-word guards, including the independent initial
saved-register-store ordering. Saved values keep their original stack slots.
All other instructions, branch displacements, helper positions, frame and
private matrix offset0x38 already match. No insertions, omissions, arithmetic,
constant, frame, argument-home or control-flow patches.

Four guarded words retain exactly their original relocation identities:
status HI16/LO16 and two matrix-pointer diagnostic LO16 stores. All helper
relocations are untouched. Actual owner padding rejects a stale expected word
or relocation and reproduces all98 retail words. Alternate global addresses
exercise HI/LO carry handling; alternate helper addresses retarget all calls.

All10811 prior guard rows are immutable; append only these31,10842 total.
Prior canonical SHA256:
`9e8f11db1c07370f470888d62e63b3b8ced846afa67a1db81ca94f0c44e601da`.
[Neighbor guard-history helper](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/game_owner_pool.py) pins that
prefix, the older10809 prefix, the two resolver table bindings and exactly the
31 new rows. It does not accept an arbitrary suffix.

## Qualification

[Eleven maintained tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_point_transform_match.py)
include ten pre-install checks and one production gate:

- 1950 paired guest cases cover all98 words in both raw C and original bodies:
  null/zero/nonzero axes, both signed zeros, subnormals, finite/infinite/quiet-NaN
  words, flags0/1/255, two stack phases, nine input/output/diagnostic alias
  combinations and bounded conversion-helper mutations. Whole mapped memory,
  ordered external traces, helper calls and preserved GPR/FPR/SP/RA agree.
  Independent private save ordering is intentionally not an identical trace.
- Independent normal-path status sequences and conversion input-reread checks
  bind the observable writes and pre-conversion diagnostic snapshot.
- 180 connected finite cases execute original guMtxL2F and matrix/translation
  instructions. SDK slot46 words contains45 executed words plus alignment;
  transform helper40 words and translation helper49 words are fully covered.
  Correct the initial handoff's incorrect53-word translation length:layout and
  original assembly agree on VA15142314..151423D8,196 bytes/49 words.
  Original transform helper150A7960 returns normally; its separate tail-entry
  wrapper150A7A00 is not called here and is not included in the connection.
- 144 actual freestanding32-bit native typed-caller cases use the current SDK
  guMtxL2F C body, fixed/float input matrices, null/zero points, output/input
  aliases and callback point mutations. All matrix bytes remain unchanged.
  Native transform/translation helpers are explicitly bounded models; they
  are not claimed as original MIPS execution.
- All39 original call/delay sites,234 seeded guest cases, forward the actual
  three inputs and return correctly for both bodies. Execute each original
  delay instruction and derive forwarded inputs independently before the
  connected run. Other caller instructions and the final synthetic return
  are not evidence of complete original caller behavior.
- Six compiled negatives change output/status/call contracts across12 mapped
  cases each:zero stub, wrong zero gate/diagnostic/final status, translation
  index and output pointer. Missing required input/global/matrix/output bytes
  fail closed; no null-output or matrix validation is invented.
- Copied owners preserve both existing warnings and the624-byte compact pool
  by actual relocation ownership. After original assembly post-processing,
  all89 typed function symbols are retained;88 typed neighbors preserve their
  full raw bytes and relative relocation metadata. The recovered target's
  392 raw bytes/relocations agree with the standalone candidate. Remaining
  assembly boundaries require the complete post-link slot audit.

Initial fixture failures were not acceptance:register renaming must not rename
COP1 destination registers; conversion callbacks can legitimately overwrite
status through aliased point storage; a53-word translation connection included
four words from the next routine. Corrected gates bind GPR fields, live alias
effects and the independently verified49-word translation boundary.

## Production Receipt

US ELF rebuild passes. Full6059-slot audit against Note1072 has no changed
slots:the prior assembly and the newly linked C emit identical code. All
addresses/extents and protected init/init_data/debugger/game_data sections are
unchanged. All720 Game-data owners/189088 bytes exact. Owner warnings2->2,
zero new warnings. Target SHA256:
`b848f699d7cae4cc984acdde51a3e9139b6bf78750dea8248c453cb796ca196e`.
10842 guards; all10811 prior rows unchanged. Canonical full SHA256:
`500b722e15c6ce30c740e6b55bc6feb0afe0a24e46df571c8aa94955b7b94639`.

Regenerate conversion CSV explicitly using
`make -C conker VERSION=us NON_MATCHING=1 progress`. The ordinary progress
target attempted the whole-binary checksum and failed, as expected for the
still-nonmatching project; this is not a new byte-match regression. ELF-only
builds do not regenerate the conversion CSV. No retail full-binary acceptance
is claimed by disabling that reporting target's checksum prerequisite.

| Section | Converted Functions | Converted Bytes | Byte-Exact C |
| --- | --- | --- | --- |
| Total |5465/6042 (90.45%)|1931568/2256728 (85.59%)|3346/5465 (61.23%)|
| Game |4792/5321 (90.06%)|1760132/2072880 (84.91%)|2673/4792 (55.78%)|
| Init |492/539 (91.28%)|151796/164048 (92.53%)|492/492 (100.00%)|
| Debugger |181/182 (99.45%)|19640/19800 (99.19%)|181/181 (100.00%)|

One additional exact C function and392 converted bytes;2119 still different,
zero address drift. Root README changes only four aggregate table rows.
All92 focused post-link tests pass in371.491s, no skips/errors/failures:
point transform11, resolver10, pool3, cache11, row matrix11, oriented13,
scaled matrix12, actor classifier8, context classifier8 and word-padder5.
Tools-check, scoped compileall and whitespace checks pass. Documentation
qualification covers55 files/3623 relative links with zero broken links.

## Resume Boundary

Next:`func_151432BC`,254 words, remains a zero-return C placeholder with a
commented draft. Recover its descriptor mode, random/angle callbacks, signed
fields and four output stores from original instructions before installation.
Its original mode2 path saves/sets/restores FCSR around float-to-unsigned angle
conversion; retain that compiler-generated conversion contract and bound guest
fixtures explicitly rather than claiming general hardware FCSR acceptance.
Oriented `func_15142600` still has27 private-layout differences and stays open.
No sibling OGL/editor/Release/save/runtime build or change,64-bit host adoption,
original rendering/gameplay/hardware acceptance, or push is claimed.
