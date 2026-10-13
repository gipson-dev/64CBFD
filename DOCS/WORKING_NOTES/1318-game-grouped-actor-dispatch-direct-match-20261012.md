# Game Grouped Actor Dispatch Direct Match - 2026-10-12

## Scope And Recovery

Continue the full Game goal from consumer `523b27a4` / tools `6a9eb2d` and
[Note1317](1317-game-one-shot-timer-direct-match-20261012.md). Both active
repositories were clean. Inspect the local graph, complete original, current
caller/helper bodies, owner and actual compiler flags. Retain the open text
218/114/cut27 and matrix translator49/34 boundaries.

Target `func_150226BC` in
[generated_49D30.c](../../conker/src/game/generated_49D30.c:282):
VA0x150226BC..0x15022754, ROM0x4FB6C..0x4FC04, 38 words/152 bytes/frame0x20.
Its three-word zero-return placeholder had37 real differences. Replace it
with the semantic void two-index dispatcher and two local pointer-table
declarations. No shared header, guard, build/profile or layout change.

The owner already uses O2/g3/MIPS2 with `-Wo,-loopunroll,0`; use that unchanged
profile in both isolated and copied-owner qualification. Record-first locals
give38/frame0x20/two differences. Actor-first locals recover the original
SP+0x1C save/reload, producing all38 words directly with no pool/diagnostics.
Combined actor predicates and signed record offsets do not improve the earlier
record-first control. No physical register binding, arbitrary NOP or fake field.

## Contract

- Full signed32 index/group select a u16 pointer through D_800C35C8 and a
  halfword entry. Zero returns before reading the descriptor pointer/table.
- Nonzero selects an eight-byte descriptor through D_800C35F0; only unsigned
  halfword type3 proceeds. Descriptor byte2 is passed to func_151149AC.
- Null actor returns. Actor byte+0x6E must equal1, not merely be nonzero.
  Read its live byte+0x72 and dispatch func_15022640(value, group).
- Reload the saved actor pointer and clear its state byte after dispatch,
  even when the append helper deduplicates the value. Do not clear early,
  re-look up the actor, or re-check the descriptor after lookup.
- Preserve the original parameter home at incoming SP+4 / frame SP+0x24
  across lookup and the actor home at frame SP+0x1C across dispatch, RA at+0x14,
  and branch-likely delay restores. The source has no scalar return contract.
- Preserve low32 addressing for guest index arithmetic without a new range gate.
  Sparse full-word probes are not valid out-of-array native C claims.

## Qualification

```sh
python3 -m tools.experiments.game_grouped_actor_dispatch_candidates --controls
python3 -m unittest tools.tests.test_game_grouped_actor_dispatch_match -v
```

Seven pre-install tests pass in69.331 seconds and seven final post-install
tests in36.422 seconds, no skips.

- 17,280 isolated guest cases cover halfword gate/type edges, byte selectors/
  state/tag values, null/non-null results, two stack phases and three provider
  mutation modes. Compare complete RAM/events/GPR/FPR/calls to retail plus
  independent public results. Lookup mutations change state/tag/descriptor;
  dispatch mutations change state/tag before the final clear.
- Deliberate guest-only home overwrites change group after lookup and actor
  pointer during dispatch. The actor-first C matches original reload behavior;
  record-first's different home is effectively rejected. These are guest ABI
  probes, not portable C claims about overwriting another function's frame.
- Missing every reached external byte fails closed; inactive entries succeed
  with descriptor table/storage unmapped. All266 own-access cut pairs fire
  and agree, with terminal controls. Opaque-provider accesses are excluded.
- 288 connected cases execute the complete original26-word func_15022754
  caller, actual28-word lookup and31-word append helper, plus original/C target.
  Independent results cover no entries, disabled/type-mismatched entries,
  zero IDs, actor states, duplicate IDs and preexisting output rows. Compare
  full machine state and storage; this test does not use helper hooks.
- Native32 O2/O0 runs the unchanged recovered caller/lookup/append C bodies
  for216 cases per profile and isolated provider mutation tests for8,192 each:
  16,816 comparisons total. Expected rows/actor flags and complete isolated
  actor storage are checked. Fresh narrowed-type and early-clear controls fail.
- The existing linked caller and both helpers independently equal all104/112/
  124 pristine bytes before installation; the final full-image gate keeps them
  unchanged. No shared oracle or helper implementation is edited.
- Actual-profile copied owner retains all56 neighbor bodies and relative
  relocations, all normalized pools, no diagnostics and the raw target/
  relocation identity. Both full-owner padders emit identical objects.
- Independent GNU assembly/link at three code/data layouts, including signed
  LO16 carry boundaries, matches all38 words. Standalone section-alignment
  tails are checked zero outside the152-byte function, not matching credit.

The generic copied-owner harness initially used default O2/g3, making an
unchanged neighboring loop appear oversized. Consult Makefile line168 and
apply its existing no-unroll flag, not a profile change or weaker padder.
Native fixture fixes split misleading indentation and capture the initialized
state byte in its expected call-count witness. Production logic is not changed
for those harness errors.

Opaque/connected software models do not establish PC/EPC/FCSR, hardware fault,
rendering or full-gameplay acceptance. Wider Game matching remains open.

## Build And Closed Metadata Audit

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds, with only the
known duplicate generated_12D630 recipe warning. The owner compiles with its
preexisting no-unroll profile; it introduces no diagnostic.

The literal image gate catches a linker serialization permutation of the
existing absolute symbols D_800C35C8 and D_80099DEC when the table is referenced.
Compare the complete normalized symbol multiset after the target-size update:
every name/address/size/type/binding/section remains unchanged except size12->152.
Account only for the two adjacent value fields and two adjacent11-byte strings,
asserting their original identities/attributes. Then compare every ELF byte.
No broad symbol/string-table exclusion or artifact-order forcing is used.

Measured delta:120 target bytes across37 words, one size byte and16 closed
serialization bytes,137 total. All other code, named addresses, data, sections
and bytes remain fixed. All189,088 Game-data bytes/720 owners are exact,
SHA0bbc00e1. Guards/progress.csv/layout/Makefile stay byte-identical.

ELF SHA-256: `b3cdd933e62d5b3a07be4553db3b87cd3cf5a037234c9dc3e8112df59d75c151`.
Source SHA-256: `0525fb887b599c579a51162b9f3bd44b7995c317b20035b56b847bffc8047520`.
Fresh matching: Game2,818/4,823 (58.43%), total3,491/5,496 (63.52%),
different2,005/drift0. Converted totals stay fixed; root README gets only its
two aggregate rows. Detailed recovery updates stay in working docs.

## Fixture And Bank

After the independent full-image gate, archive the previous948C text manifest/
image in ignored `game-grouped-actor-dispatch-test/text-fixture-before-grouped-actor/`.
Advance only its expected ELF hash and generated before-image/manifest; all
other eight protected current/snapshot inputs remain unchanged. Fresh target
image and text immutable/corruption controls pass as three tests in9.749 seconds.
Unchanged broader receipts are reused explicitly, not called fresh; historical
full-image gates remain frozen to their own banks.

Mounted tools `a7b5b37bf18086ea9691c118805b8874cc8c414a` is committed first,
then source, note/indexes/workflow, README aggregates and gitlink.
Preserve older tools HEAD`ddbdd16b` and unrelated dirty work. Only two absent
task files and the verified shared fixture are synchronized/hash-checked;
all108 unrelated saved fingerprints remain identical. Dirty386 becomes388
and task hashes109 become111. WSL consumer/mounted/older tools checks,
Windows py_compile and whitespace checks pass. All4,591 relative links across
eight checked documents resolve. No older commit or history duplication. Require
syntax/tools/link checks, clean active checkouts, post-bank integrity and fresh
terminal Graphify Rebuilt/zero-workers receipt. Preserve existing graph/version/
scan-size warnings. Zero Claude calls, no push, dependency/compiler install,
host/OGL Release/ROM/save/config/editor change or full-goal completion claim.

## Next

Next ordinary entry is func_1503453C in `game/generated_61490.c`,
42 words/frame0x18/current37 differences, original in `asm/61490.s`.
It indexes0x32C-byte actors and dispatches types0..4,0x80,0xB0 to func_1503B9BC.
The five-word table at jtbl_80097D20 in `asm/data/23C630.rodata.s` sends all
five dense types to the same retail label; retain/recover that switch/table
layout rather than claiming a simplified predicate matches. No source fit is
accepted yet. Keep text218/114/cut27, translator49/34 and handwritten non-C-ABI
boundaries separately open, and keep the full Game goal active.
