# Neighbor Row Builder Recovery And Private Boundary

Date: 2026-10-19

## Scope And Baseline

Continue the Game goal with `func_1508A1BC`, VA1508A1BC..1508A6FC,
ROM B766C..B7BAC:336 words/1,344 bytes, retail frame168. The direct caller
`func_1508B9BC` invokes it immediately after now-exact `func_1508C5B8`.
Consumer predecessor65dc7db and primary tools predecessorfaa4dfb were clean.
Tools5b33fbe is committed before this documentation/pin checkpoint. No push.

The complete recovered C remains experimental. Production still contains its
12-byte zero-return stub with327 classified word differences. No source,
assembly, guard, Makefile, linked ELF, progress CSV or root README changes;
no new conversion/matching credit and no production build in this checkpoint.

Frozen installed fingerprints:

```text
Source:   6bd6a7aea0861135038d9709e42a2a72378c3d67b4d8a644807b007fc0fc3e6d
Manifest: 6da8e07397f8b4340de5d95b44ffc14cf881793fc23c0d1ac2e539ae7ea6648d
Makefile: cf6de057267055cf5ad789e72426b7433c0bfe37d04ae56c241332cf2f2febf4
ELF:      067be2667e83c916756a9eb7f69d9cd29d8349886ff0e8c09bc7c6057a777b5c
Progress: 16798cbd1f7d69f7ecdd8b7e0071ba9ea975a50652bd8797673d1ec2b500c9be
```

The unchanged ELF/progress retain Note1609's measured Game3015/4832 (62.40%),
total3688/5505 (66.99%),1,817 different/zero drift, owner67/73 exact.
Init492/492 and Debugger181/181 remain exact; conversion5505/6044 (91.08%),
86.08% bytes. These are retained installed measurements, not new match credit.

## Recovered Semantics

- Snapshot the entry context's group/state/activity/team/neighbor/score tables,
  count and enabled mask. Increment its signed byte cursor with byte wrap;
  reload the live context and reset only on equality with its current count.
- Clear exactly16 neighbor IDs when the selected enabled bit is absent;
  leave scores and the published minimum untouched in that path.
- Visit active, different-group candidates using the captured count/group.
  Truncate float32 X/Z distance, retain that unweighted value, and apply the
  retail team penalty, high-mask/flag gate, signed primary count and mode gates.
- In B7 mode restore rejected distance, apply the optional second doubling,
  call `func_150859AC((s16)i,6)`, divide by the wrapping result-plus-two and
  reload the signed primary count. Use the fresh context's multiplier for
  eligible primary candidates; preserve the checked divide traps.
- Insert ascending scores, placing a newly encountered equal score before
  older equals. Interleave ID/score shifts, do not add a16-entry capacity cap,
  pad only IDs, and include rejected candidates in the unweighted minimum.
- Publish through the final fresh context only when its table base plus51C
  is nonzero; the null check is not on the indexed destination. Return zero.

The old alternative-source reference was inspected, not imported wholesale:
its incorrect byte/halfword/float reads and pointer steps are not evidence of
retail behavior. Names retain the existing address-based function identity;
the candidate has a short semantic comment and meaningful local names.

## Source And Layout Frontier

| Complete source/profile | Words | Frame | Raw word differences |
| --- | ---: | ---: | ---: |
| Initial/no-unroll (`SELECTED`) |293|184|330|
| Initial/normal |346|192|327|
| Byte-stride fill, signed-byte primary/normal |330|176|315|
| Retail |336|168|0|

The byte-stride candidate is `dict(shapes())['byte-fill-narrow']`, not a
silent replacement of SELECTED or production. It agrees with completed
public values/calls across353 fixtures and native32 O2, but266 ordered store
traces still differ. The initial normal profile has692 differing profile/
phase traces; its final RAM/store multiset agrees, not its ordered trace.
The initial no-unroll profile agrees with the retail ordered public stores.

An early byte-fill experiment incorrectly used `i != 64` for the final
padding loop without guarding `used > 16`. The26-actor fixture exposes its
runaway unmapped store. Keep `i < 64` there; the corrected candidate safely
skips padding on wide rows. This effective negative is rerun by test09.

Three fired access-zero gates record the unresolved private boundary:
retail SP-168 versus raw SP-184/SP-192, with first stores at caller SP-0x74
versus SP-0x84. All requested faults fired; none is interpreted from absent
output. The330-word/frame176 frontier still needs its literal private homes,
allocation, unroll, branch-delay and ordered-access matching work.

## Qualification

Primary: ten tests pass in47.833s. Standalone mirror: the same ten tests pass
in58.767s against prepared consumer inputs, with mirror module paths checked
and only the test input root redirected. `make tools-check` also passes.

-353 fixtures,2,106 completed retail/raw profile-phase runs and12 fired
  divide-trap prefixes; the main corpus visits326/336 retail words, not all.
-99 finite/native-safe fixtures at O0/O2/O3 with UBSan; eight effective
  semantic negatives exit26, plus the guest-only unsigned-cursor negative.
  The byte-stride frontier also passes these99 fixtures at native O2.
-18 returning runs connected to the full original68-word field-query helper
  and original seven-entry jump table. The structured Game-data layout maps
  table8009D9A0 to ROM242460 inside owner242420; field6 jumps to15085A9C and
  reads signed word800D2148+slot*28. Production's helper remains a stub;
  this is original-retail helper evidence, not a production call-chain claim.
-Both complete owner profiles preserve all72 other raw functions and pools,
  including the existing typed caller. Three independent GNU maps give27
  rebased completed runs across original assembly and both compiler profiles.
-All frozen production input bytes remain unchanged. No new expected-word
  rows, profile override, normalizer, source-origin recipe or padder change.

Limits: completed positive counts are bounded to32; larger synthetic counts,
arbitrary aliases/callers, actual hardware/FCSR and gameplay are not qualified.
Nonfinite/out-of-range float conversions use the explicit guest indefinite
integer model and are excluded from native C. Invalid division is a fired
guest prefix, not portable C or full HI/LO exception-state equivalence.
Private RAM/register/fault-prefix identity is explicitly not established.

Three previously absent task files are copied to `64CBFD Tools`. Preserve
all1,419 prior dirty leaf hashes and HEADddbdd16b; no mirror commit/reset/
stash/clean or conflicting-file overwrite. No host/frozen Release, save,
dependency, account/configuration or advisory-agent operation. The user
confirmed the earlier overwritten `Conkers` compiler scratch was disposable;
no recovery is needed and compiler paths remain relative to avoid spaces.

Receipts are ignored under `conker/build/game-neighbor-row-builder/`:
`qualification/qualification-primary.json`, mirror `qualification.json`,
`test-run.txt`, `test-run-mirror.txt` and `graph-before.json`. The consumer
commit hook refreshes Graphify; retain its before/after preservation audit.

## Resume This Function

1. Recover frame168 and real private homes from semantic local lifetimes/
   declaration order. Start from the330-word/frame176 byte-stride frontier;
   retain the initial ordered no-unroll candidate as the semantic baseline.
2. Close GP/FP allocation, both four-way loops, padding-store ordering,
   signed cursor masks and branch-delay scheduling. No dummy storage or
   wholesale instruction replacement; qualify any checked layout recipe.
3. Pass complete literal/private/access/alias, relocation, actual padder,
   Make shadow and strict linked-image gates before installation. Preserve
   every existing guard and all72 neighbors; requalify affected interfaces.
4. Only then replace the stub, rebuild/audit the full ELF/progress and update
   README aggregates. Keep the wider Game goal open. The other five owner
   nonmatches remain15086364,1508A6FC,1508B3F8,1508CAD8 and1508DC24.
