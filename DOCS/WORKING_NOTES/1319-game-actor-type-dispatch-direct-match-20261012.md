# Game Actor Type Dispatch Direct Match - 2026-10-12

## Scope And Recovery

Resume the full Game matching goal from consumer `358f6fd9` / mounted tools
`a7b5b37` and [Note 1318](1318-game-grouped-actor-dispatch-direct-match-20261012.md).
Both active checkouts were clean. Inspect the focused graph, complete original,
direct caller, table ownership and actual O2/g3/MIPS2/o32 owner profile.
Zero Claude calls; preserve the independent older tools checkout and host Release.

Target [func_1503453C](../../conker/src/game/generated_61490.c:39):
VA0x1503453C..0x150345E4, ROM0x619EC..0x61A94, 42 words/168 bytes/frame0x18.
Its three-word zero-return placeholder had37 real differences. The first
ordinary switch candidate emits all42 words and all five table entries directly.
No guards, compiler-profile change, register binding, fabricated fields or NOPs.

The signed32 argument is forwarded unchanged to func_1503B9BC. Read the unsigned
actor-type byte at D_800CC2D4 plus low32 index*0x32C; types0..4,0x80,0xB0 call
the helper once, all other bytes return without a call. The function is void:
its inactive paths do not establish a scalar result, and its caller ignores it.
Keep the original signed comparisons, dense table jump, branch-delay RA loads,
and RA lifetime at SP+0x14. A simplified predicate is not matching source credit.

The five entries at jtbl_80097D20 / VA0x80097D20 / ROM0x23C7E0 all target
0x150345CC. The following12 bytes are alignment, not additional entries.
Keep the original table/data owner; add only generated_61490's existing-style
RETAIL_RODATA_SYMBOL binding to jtbl_80097D20_game and Makefile dependency.
The compiler's32-byte pool is checked then omitted by the production padder,
which binds the code references to the already-owned original retail table.
No shared header, layout, guard, linker script or original assembly change.

## Qualification

```sh
python3 -m tools.experiments.game_actor_type_dispatch_candidates
python3 -m unittest tools.tests.test_game_actor_type_dispatch_match -v
```

Seven pre-install tests pass in49.093 seconds; seven final installed tests
pass in25.464 seconds, no skips. Reuse the prepared compiler/parsers/oracles.

- Five bounded source controls measure differences0,0,0,2,31. Inline,
  signed-index and signed32-selector forms are direct42/frame0x18; unsigned32
  selector changes two comparisons, and u8 selector changes length/table targets.
- 6,144 guest cases cover all256 type bytes, six full-word indices, two stack
  phases and helper mutation modes. Compare entire RAM/events/GPR/FPR/calls,
  independent call count/index and live byte mutation. All42 words are visited.
  Sparse wraparound indices are guest-address probes, not native C array claims.
- Inactive high types succeed with the table unmapped. Every type fails closed
  when its actor byte is missing; each dense table entry rejects an unowned
  destination. All23 own-access fault-prefix pairs fire and agree, with completed
  controls. Provider accesses are excluded from own-access gates.
- Native32 O2/O0 executes the unchanged selected source for13,312 cases each:
  all types, every valid index0..25 and mutation modes, complete actor storage.
  Four fresh signed-byte, missing-high-type, wrong-stride and wrong-argument
  controls fail by observed results, not by compilation failure.
- 360 connected cases execute all81 original caller words in func_150345E4
  plus original/C target. State1/0x22, flag7, index and live helper type mutation
  exercise both call sites and re-check behavior; independent call counts agree.
  The large func_1503B9BC provider remains opaque and unconverted. This is not
  qualification of its complete body or a claim the caller placeholder is restored.
- Copied owner uses the real normal O2/g3 profile and completes GLOBAL_ASM
  postprocessing. All nine neighbor bodies/relative relocations remain identical,
  data pools stay fixed, and only the five normalized target-table entries appear.
  Raw target bytes/relative relocations agree with the isolated candidate.
  Both full-owner padders produce identical objects with the168-byte target size.
- Independent original assembly and C agree at three code/actor/table layouts,
  including both signed-LO16 carry directions; table targets move with the code.

Initial test-only errors excluded a reached word, misstated the connected-case
product, and let GCC reject a negative control's narrow switch expression.
Correct those fixtures and run the signed-byte negative as a signed32 local;
do not alter the matching production body for a fixture failure.

These software models qualify emitted instruction order, not hardware PC/EPC,
FCSR, rendering or full-gameplay behavior. Wider Game matching stays open.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds. The Makefile
dependency triggers a wider rebuild; report the known duplicate generated_12D630
recipe warning and existing pointer diagnostics in unchanged files. The target
owner introduces no diagnostic. No ROM build or private-input replacement.

The literal whole-image gate permits only the complete target slot and its
symbol size12->168. Exactly119 target bytes across37 words and one size byte
change,120 total. No symbol serialization exception is needed. Every other
ELF byte, function body/address/extent, section and named symbol remains fixed.
All189,088 Game-data bytes /720 owners remain exact, SHA0bbc00e1.
Guards, progress.csv and layout are byte-identical; Makefile has only the two
qualified table-binding/dependency lines.

Fresh matching: Game2,819/4,823 (58.45%), total3,492/5,496 (63.54%), drift0,
different2,004. Converted totals stay5,496/6,044 and Game4,823/5,323.
The root README changes only its two measured matching rows.

Source SHA256: 2a2522263f90d21040980f5532654bd17dead9ddd3c303b4f5c94176ad410a7d.
ELF SHA256: 85de31d41e6f97fc14b398e84237d79b29c99a72e5a16a8b18307ea337105be0.
Makefile SHA256: fa975a22531dab077a7ac6ccd90c03084c485fe8df5915cf2f57cfbe52c65127.
Guard SHA256 remains3f12cf872b84100963934734de2e67f5f07073ce3112ccbd2e5c4cb8af84666e.

After the independent literal image gate passes, archive the old text fixture
manifest, ELF and Makefile snapshots in this target's ignored build folder.
Advance only the ELF and exact two-line Makefile receipts; verify all seven
other source/assembly/table/pool/guard/progress/layout fingerprints unchanged.
Fresh text tests05/06 pass in3.179 seconds with effective corruption controls.
No text implementation, shared oracle semantics or historical image gate changes.
Explicitly reuse unchanged broader receipts from Note1318, not fresh-test claims.

## Banking And Next

Mounted tools `84cfb3ae601010a75f1d35f853a09d7de0ce89f5` is committed first,
then the consumer source, Makefile, docs/README aggregates and tools gitlink.
Consumer/mounted/older tools checks, both Windows syntax checks and whitespace
checks pass. Older HEAD`ddbdd16b` and all110 unrelated saved task fingerprints
remain fixed. Copy only two absent new files and the verified shared fixture;
dirty388 becomes390 and saved fingerprints111 become113. No older commit.
Banking includes relative-link validation, clean active checkouts, post-bank
integrity and a fresh terminal Graphify Rebuilt/zero-workers receipt. Preserve
existing graph scan/version/HTML-size warnings; no push or dependency install.

Next ordinary target is func_15034728 in the same generated_61490 owner:
48 words/frame0x20/current47 differences, original ROM0x61BD8..0x61C98.
Recover the actor's buffer/mask gates, helper-derived signed last index clamped
to31, live mask re-reads and backwards selected-bone3x3 clear inside64-byte
records. Preserve fourth components/last row and reload the buffer after the
helper. No new candidate or matching credit is accepted for it yet.
Keep text218/114/cut27 and translator49/34 open. No host/OGL Release, save,
configuration or editor changes; do not close or silently pause the full goal.
