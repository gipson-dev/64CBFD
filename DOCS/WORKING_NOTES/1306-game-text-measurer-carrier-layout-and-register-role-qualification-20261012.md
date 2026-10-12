# Game Text Measurer Carrier Layout And Register Roles - 2026-10-12

## Scope

Continue `func_150428D4` from consumer `27494dd3` / tools `da8a377` and
[Note 1305](1305-game-text-measurer-frontend-vreg-and-uopt-call-save-provenance-20261012.md).
Retail remains 219 words / frame 0x80; production remains the 199-difference
placeholder. Preferred `flag-branches-captured` remains 222 / 0x80 / 146 and
rejected. Latest actual match remains `func_15042C40`, Note 1292. No source
installation, guards, profile change, matching credit or root README edit.

## Ten Distinct Layout Bodies

The new `layout_candidates()` screens declaration order, separate scalar
metrics, lexical metrics scope and ordinary-predicate-before-effects order.
Original 16 predicate forms and seven carrier forms are unchanged. CLI
`--layouts` and `--carriers` are mutually exclusive; default mode is unchanged.
All bodies retain five real metric fields and the existing owner profile.

| Form | Words | Frame | Differences |
| --- | ---: | --- | ---: |
| Flag declaration before record | 216 | 0x90 | 179 |
| Separate scalar metrics | 216 | 0x90 | 179 |
| Scalar metrics, flag first | 216 | 0x90 | 179 |
| Record scoped under non-null text | 216 | 0x90 | 179 |
| Record scoped around normalizer | 216 | 0x90 | 184 |
| Ordinary predicate before effects | 222 | 0x90 | 193 |
| Same predicate, scalar metrics | 222 | 0x90 | 193 |
| Same predicate, direct font symbol | 224 | 0x90 | 220 |
| Ternary predicate before effects | 223 | 0x98 | 216 |
| Same ternary, direct font symbol | 226 | 0x98 | 225 |

All ten have zero pool bytes and fail the retail frame gate. Equal word,
frame and difference counts do not establish word identity: all ten emitted
bodies are distinct. The four 216/0x90/179 declaration forms retain the
simple carrier's first 13 words but change actual metric homes. Normalizer
scope additionally swaps maximum-width/baseline saved roles. An initial
six-body/word-identical fixture assumption was caught and corrected using
complete word comparisons, not relaxed matching gates. The initial generator
import also caught an unmatched parenthesis before any native compilation.

## Register Role, Not Just Spill Opcode

`ordinary-before-effects-direct-font` emits T0 zero and SP+0x88 save/reload
around both helper calls, but T0 is maximum width, not the font flag. A
read-only call observer runs `AB\n\xA8\0` at stack phases 0 and 8. Retail
enters the actual metrics helper with T0=0; the candidate enters it with
the positive maximum width computed from the preceding line. Public results
and helper calls still agree. The observer preserves the unobserved model's
complete events, GPRs, FPRs and RAM; it neither replaces nor hooks helpers.
Thus matching a T0 spill opcode alone would be a false lifetime diagnosis.

The ternary variant clears T0 before the space width write, but only on the
space branch. Other branches materialize it later. Extra saved roles and
0x98 frame remain. This is not the shared early reset required by retail.

## CFE Homes Versus UOPT Call Save

Fresh completed normal-profile captures compare flag-before-record and
record-scope-normalize. The former has CFE 18,632 bytes / 839 records and
UOPT 18,048 bytes / 799 records; the latter has CFE 18,648 / 841 and UOPT
18,080 / 802. All five record-address expressions use CFE M-44 in the first
form and M-48 in the second. Both retain the four explicit vreg homes
M-52/-56/-60/-64, lexical level 1, length 4. Both UOPT outputs still contain
the register-8 `rstr` / `rlod` pair at M-56; emitted call-save remains SP+0x58.
These declaration changes move the record, not the anonymous call-save home.

The existing fingerprint-locked read-only recipe requires actual owned-child
input paths, completed producers, fired initialized-table probe, full driver
exit 0, cleanup, marker order and stream/table hashes. Each diagnostic object
matches its own normal text/functions/relocations and every pool family.
Prepared cc/uopt/ugen/cfe binaries remain unchanged. No existing debugger
attach, native-memory write, runtime call, compiler rebuild or installation.

One additional ignored shape-only source reuses the existing extent local
as a union's font-address member during the disjoint ordinary-font phase,
preserving both live font-pointer reads. It emits 219 / 0x80 / 207, SP+0x68,
but retains hoisted font address S5, extra S7 and late space-path T0 reset.
All 219 instructions are word-identical to the earlier rejected phase-union
form from Note 1305. No new public/private/native/owner qualification or
distinct fit is inferred from that shape-only screen.

## Qualification And Bank

Six new tests pass in 34.697 seconds, no skips. All ten complete bodies each
pass 755 public cases: 7,550 comparisons with actual helpers/tables, saved-
register/return checks, aliases, live font pointer, payload skip and nested
truncation. The wrong-space-width source and conflicting CLI modes are
effective negatives. No new full private/fired-fault/native/owner/padder/
rebase qualification is claimed for these rejected bodies.

Fresh isolated original-predicate regression: seven tests / 6,795 public
comparisons in 33.713 seconds. Fresh isolated frontend/carrier regression:
six tests / 3,020 comparisons in 20.891 seconds. Earlier overlapping runs
were not used as the final isolated receipts. Earlier full-20 qualification
continues to apply only to its unchanged old bodies, not these new forms.

Tools e7ebb385220fb71502a608533461155f88fd243f is committed before consumer
notes, concise indexes, workflow command and exact gitlink. Consumer,
mounted and older tools checks, Windows py_compile and diff checks pass.
All nine frozen inputs and protected 189,088 bytes / 720 owners remain
unchanged, with effective corruption controls. Production ELF/source/guards/
Makefile hashes and matching totals remain unchanged: Game 2,813 / 4,823
(58.32%), total 3,486 / 5,496 (63.43%), zero drift. No OGL/Release/ROM/save/
config/editor/existing guest-debugger change, additional Claude call or push.

Older standalone HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` remains intact.
All 88 prior task fingerprints were checked before synchronization. Only
the known logic helper and previously absent layout test were copied; the
other 87 fingerprints stay unchanged. Final expected task set is 89 and
dirty paths increase from 365 to 366; no older commit/reset/history rewrite.
Final bank requires valid relative links, fresh post-documentation immutable
controls, clean active repos, and the installed post-commit Graphify hook's
terminal fresh `Rebuilt` receipt with advanced bytes/UTC and zero workers.
All 4,518 relative links across eight checked documents resolve. Fresh
post-documentation immutable/corruption tests 05/06 pass in 1.642 seconds.

## Next

Keep the same target and full Game goal active. Trace the optimized
predicate's default-zero definitions and merge paths: lexical declaration
reordering has not changed its anonymous call-save home. Recover one shared
T0 zero before every first post-normalizer memory operation, the seven saved
roles and full 219 / 0x80 / SP+0x68 lifetime without hoisted font-address
state. Do not repeat these ten layouts or either word-identical phase union.
Do not infer all C is exhausted. All final private/fired-fault/native/owner/
neighbors/pools/both-padders/independent-links/rebases/literal whole-ELF/data/
guard-prefix gates still precede installation or totals. `func_150417AC`
follows only after a real fit here.
