# Game Text Measurer Frontend Vreg And UOPT Call-Save Provenance - 2026-10-12

## Scope

Continue `func_150428D4` from consumer `78bf119` / tools `d515411` and
[Note 1304](1304-game-text-measurer-effectful-predicates-and-upstream-call-save-20261012.md).
The retail target is 219 words / frame 0x80. Production remains the
199-difference placeholder; preferred `flag-branches-captured` remains
222 words / 0x80 / 146 differences and rejected. Latest actual match is
`func_15042C40`, Note 1292. No installation, guards, compiler-profile change,
matching credit, aggregate change or root README edit.

## Source Screens

`carrier_candidates()` carries ordinary-font eligibility in the left operand
of bitwise OR, with extended-metrics effects returning zero on the right.
The existing 16-form generator remains the default. Five real metric fields
and the unchanged owner profile are used; no fabricated flag home or
physical-register binding.

| Carrier Form | Words | Frame | Differences |
| --- | ---: | --- | ---: |
| Simple, named result | 216 | 0x90 | 179 |
| Simple, direct condition | 218 | 0x88 | 193 |
| Retail gates, named result | 231 | 0x98 | 195 |
| Retail gates, direct condition | 233 | 0x90 | 201 |

Three expression controls are word-identical to simple/named: seven source
forms produce four instruction bodies, all with zero pool bytes. Simple/named
recovers the seven saved-register roles and retail words 1 through 12, but
has the wrong frame, late space-path T0 reset and SP+0x58 save/reload.

Six additional ignored initializer/scope/font-address forms produce five
distinct bodies. These are shape screens only, not public qualification.
Removing the redundant permanent font-address local gives 219 words, frame
0x80 and the SP+0x68 call-save, but introduces an eighth saved register,
shifts the save homes and still resets T0 only after the space-path width
read. The phase-union variant has the same disqualifying roles/reset. Neither
is a match or a replacement for the preferred seed.

## Measured Pipeline Provenance

The new read-only `game_text_measurer_frontend_trace` captures both wire
streams from newly owned compiler children under the normal compiler flags.
It reads each child's actual `/proc/<pid>/cmdline`, requires completed CFE
and UOPT producers, verifies that UGEN consumes the captured UOPT output,
and reads initialized opcode/type tables at the fired UGEN load-node probe.
No attach to an existing process, runtime call or native-memory write occurs.

For simple/named, the complete CFE stream is 18,632 bytes / 839 records:
`ef5a1252c20ad28a9144a8e4dafef7840e61e987dec16d8813426bef8829e7be`.
The complete UOPT output is 18,048 bytes / 799 records:
`e575729c6ddb71ec674337a0db456891fed3a2bb296066e3103c899851cabae7`.
Both decode from `bgn` through `stp`, with no leftover or truncated record.

CFE declares four explicit `vreg` records in M storage, lexical level 1,
length 4, at offsets -52, -56, -60 and -64. The ordinary-font predicate
result is stored/loaded at M-56 across the metrics call. CFE has no R8
operand; its only register load is the normalizer return at R2.

UOPT output instead contains `rstr J M level8 offset-56` immediately before
the metrics `cup`, followed by `rlod J M level8 offset-56`, and actual R8
loads/stores. Thus UOPT promotes the CFE temporary and introduces the
explicit register-8 call-save before UGEN receives it. Wire R offsets are
register numbers; UGEN tree R32 is a byte address for architectural R8.
This resolves the CFE-versus-UOPT boundary left open in Note 1304, not the
exact UOPT subpass or retail's complete allocation history.

The validator independently rechecks complete driver exit 0, fired probe,
child lifetime/cleanup, marker order, stream/table hashes, and normal-object
identity for text, functions, relocations and the union of every pool family.
Prepared cc/uopt/ugen/cfe fingerprints remain exact. The decoder follows the
prepared `f_readuinstr` / `f_ugetint` layout and captured tables, not a claim
of portability to arbitrary compiler versions.

Failed intermediate-preservation experiments remain unqualified: `-keep -v`
aborts on unsupported verbose formatting; plain `-keep` retains no wire
streams; `-K` ends with UGEN signal 11. Its four owned `kept.*` artifacts were
moved with path/size/hash checks into ignored `conker/build/` evidence, without
overwriting other files. Do not reuse a stale object as proof of the failed
driver or edit/rebuild the prepared compiler to bypass this failure.

## Qualification And Bank

Six fresh frontend tests pass in 25.779 seconds, no skips. Four complete
bodies each pass 755 public cases: 3,020 comparisons with actual helper
instructions/tables, saved-register/return checks and no call hooks. Effective
negative controls reject missing, altered or misordered captures, producer
failures, changed tables/fingerprints and invalid wire streams. Seven fresh
original-predicate regression tests pass in 37.549 seconds after the shared
input extraction; their original 16 forms / nine bodies / 6,795 comparisons
remain unchanged. No new native/private/fired-fault/full-owner/padder/rebase
qualification is claimed for any rejected current form. Earlier full-20
receipts apply only to their unchanged old bodies.

Tools `da8a377863ec2a66f575a980ecdf2e58659405fe` is committed first. Consumer
note, concise indexes, workflow command and exact gitlink follow. Consumer,
mounted and older tools checks, Windows py_compile and tools diff checks pass.
All nine frozen inputs and protected 189,088 bytes / 720 owners remain
unchanged, with effective corruption controls. Game remains 2,813 / 4,823
(58.32%) byte-exact; total remains 3,486 / 5,496 (63.43%), zero address drift.

Older standalone HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` is preserved.
Its existing logic helper was conflict-checked before synchronization; the
two new files were previously absent. All other 85 saved fingerprints are
unchanged; the final 88 task fingerprints match the expected checkpoint.
Dirty paths increase from 363 to 365. No older commit/reset or push, and no
OGL/Release/ROM/save/config/editor/existing guest-debugger change.

Standalone Graphify terminates with protective exit 1: 18,381 versus saved
40,159 nodes, retaining 19,398 excluded-but-existing nodes from 2,972 files.
Preserve version/zero-node warnings, no force or purge. Final bank requires
checked relative links, fresh post-documentation immutable controls and a
terminal post-consumer `Rebuilt` receipt with advanced log bytes/UTC, zero
native workers and clean active repositories.
All 4,512 relative links across eight checked documents resolve; fresh
post-documentation immutable/corruption tests 05/06 pass in 1.560 seconds.

## Next

Keep the same target and full Game goal active. Use the captured CFE
temporary/vreg homes and UOPT promotion to recover source declaration/order
without the hoisted font-address saved register. The shared T0 zero must
precede the first post-normalizer memory operation; retain the full-word
SP+0x68 call-save and exact 219-word / 0x80 body with all seven saved roles.
Then pass every final private/fired-fault/native/owner/neighbors/pools/
both-padders/independent-links/rebases/literal whole-ELF/data/guard-prefix gate
before installation. Do not repeat these source screens or infer that all C
is exhausted. `func_150417AC` follows only after a real match here.
