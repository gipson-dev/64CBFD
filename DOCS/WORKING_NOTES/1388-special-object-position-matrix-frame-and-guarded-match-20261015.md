# Special Object Position Matrix Frame And Guarded Match

Date: 2026-10-15. Continue the whole additional-source/Game audit from
[Note 1387](1387-capture-request-compiler-roles-and-guarded-byte-match-20261015.md).
This checkpoint restores one real C body, not the whole remaining-source goal.

## Scope And Baseline

`func_1511F31C`, owner `conker/src/game/generated_142560.c`, is retail
VA `0x1511F31C..0x1511F3E8`, ROM `0x14C7CC..0x14C898`: 51 words / 204 bytes,
frame `0x90`. Its previous 12-byte zero-return placeholder was already counted
as converted C. The original full-slice assembly remains unchanged.

Start with clean consumer `fe65ef5f` and tools `fdae1b3`. Freeze 28 named inputs
in ignored `conker/build/game-special-object-position/before-*`; the manifest
and every frozen input are fingerprint checked, not recaptured after editing.
The predecessor ELF is `d8f985cd62b1d83946febd871d4ecd69cf9e04056af69a829f5d6e91e720e4be`.

The read-only archive draft is in
`Another Source/CBFD-Recompiled/conker/conker/src/game/game_142560.c`, SHA-256
`46dc2e2365e4a9f543205120311718de26f50daef46199d595f75c6be9dd1fd8`.
Its `void *sp48`, word-sized field accesses and untyped helper declarations
cannot be imported as a valid matrix routine. Preserve all original 801
archive fingerprints, not just the selected file.

## Recovery And Guard Boundary

Keep the address-based function name; recover meaningful local argument names
and a short purpose/frame comment. The body:

- Captures the unsigned halfword at object+`0x3E` unconditionally. Only its low
  byte is passed to the actor lookup. Retail still performs this LHU when the
  kind gate fails; replacing it with a late or single-byte access is not exact.
- Requires unsigned kind `0x8005` at object+`0x54` and full-word category
  `D_800BE9F0 == 0x35`. The category is not read after a failed kind gate.
- Returns without coordinate stores if `func_151149AC` returns null.
- Allocates a real 64-byte `f32 matrix[4][4]`, calls `func_1511490C`, transforms
  `(-3.0f, 223.0f, 549.0f)` through `func_150A7960`, then truncates to signed
  words and stores the low halfwords at object+`0x10`, `0x12`, `0x14`.

Add only private helper prototypes and the category declaration in this owner;
leave shared headers, compiler flags, Makefile, other functions and assembly
alone. Fresh full-owner O2/g3 compiles have zero diagnostics. Fourteen bounded
source screens have zero diagnostics and no direct match. Selector capture
recovers 49/51 words, all five relocations, saved roles, branch delays and local
offsets. Raw C still allocates/releases `0x88` bytes instead of retail `0x90`.
Named coordinate temporaries, scalar widths and an aligned matrix do not close
this frame difference. Do not insert dummy locals or claim a direct C match.

Two fail-closed expected-word guards at offsets `0` and `0xC0` change only
balanced ADDIU SP frame immediates `-0x88/+0x88` to `-0x90/+0x90`. Nothing is
inserted, omitted, rescheduled or rebound. The raw function bytes and exact
five relocation records are pinned before normalization. Every raw-byte flip,
relocation deletion and duplicate guard append is effectively rejected. The
real generated-slice padder and linker produce all 51 retail words exactly.
**This is a guarded byte match, not an unguarded/direct compiler match.**

## Fresh Qualification

The final 14 top-level checks pass in 77.922 seconds:

```sh
python3 -m unittest tools.tests.test_game_special_object_position \
  tools.tests.test_game_special_object_position_candidates \
  tools.tests.test_game_special_object_position_installed -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- Preserve all 83 raw owner neighbors: body bytes, symbol sizes, relative
  relocation records and normalized data pools. No new pool or profile.
- 2,560 modeled guest cases cover gates, selector widths, null/success returns,
  provider mutations, both stack phases and finite coordinate truncation.
  All 51 words are reached; normalized complete modeled states agree. The
  unguarded body has equal public output but a different private frame.
- 122 paired, fired parent-access cuts agree in complete modeled state.
  Missing selector bytes still fail on an inactive object; missing category
  memory is tolerated only behind the failed kind gate. This is instruction
  prefix evidence, not hardware exception/FCSR equivalence.
- Native32 O2 and O0 execute the actual C body over 32,768 cases per profile,
  all 256 selector bytes, two finite signed-short-range vectors, object bytes
  and canaries. Five returned controls effectively reject wrong kind, category,
  selector byte, point parameter and coordinate. No NaN/out-of-range C claim.
- Connect the actual unchanged 40-word retail point-transform assembly in 34
  guest cases. Three independent original-assembly rebase pairs also match,
  including signed-low relocation carry and moved call targets.
- Independently construct the complete expected ELF from the pinned old image,
  retail target bytes and only the symbol extent `12 -> 204`. The normal build
  equals that expected image byte for byte: 152 changed bytes total, with every
  other byte fixed. All 189,088 protected data bytes / 720 owners remain exact.
- Check all 28 current input paths and effective corruption controls. Only the
  three exact known changed inputs are inverted for historical tests; unknown
  and corrupt inputs are not mapped. Five previous capture-request checks pass,
  embedding five prior view checks and eight earlier actor/matrix checks.
  The original 801-file archive fingerprint manifest passes freshly.

The build retains the known duplicate generated_12D630 recipe warnings and
existing warnings in other rebuilt owners. It is not a warning-free project
build. The target and complete target owner have zero compiler diagnostics.

## Installed Results

| Input | SHA-256 |
| --- | --- |
| ELF | 52b0efe2da54e3d78c4ad3ca102189d57d877ed313a245a055630650372133f6 |
| Position owner | c9e6044506b47ac23ef11f88612d30dd705f51cdfb287572956bea6bf24a4759 |
| Guards | 311c81d50de789b4a51e3d27ac3ad2d0e0aabb9b07393ce004d34fdd1c822af2 |
| Unchanged progress CSV | 3ad7466c067bdb27e92248b8b237fb3dff392097ef3cd5d9a337d8268fbda091 |

Fresh matching: Game **2,888/4,829 (59.81%)**, total **3,561/5,502 (64.72%)**,
different **1,941**, zero address drift. Converted counts remain 5,502/6,044
(91.03%), bytes 86.06%; Game 4,829/5,323 (90.72%), bytes 85.42%. Init and
Debugger remain 492/492 and 181/181 exact. README changes aggregate rows only.

Bank qualification tools `c51788d` first. Shared tools checks, five-file syntax
and the three ROM-free checks pass in the independently dirty standalone copy.
Gate its `ddbdd16` HEAD and all 601 initial dirty fingerprints before copying
five new owned files; never overwrite existing paths or commit the mirror.
All 606 final dirty fingerprints are verified, including the 601 initial ones.
Seven documentation files / 4,919 relative Markdown links validate with none broken.
No push, host source/build/launch, save/configuration or frozen Release action.

Full `graphify update .` refuses 19,266 nodes against the 41,046-node curated
graph and retains 19,398 nodes from 2,972 excluded-but-present files. Preserve
that fail-closed result; do not force the smaller scan. Await the normal
incremental consumer-commit worker separately.

Claude budget/calls: zero. Direct assembly, compiler, oracle, relocation and
literal-image evidence settle this bounded task without an advisory call.

## Next Action And Limits

`func_1511490C` in `generated_13D350.c` is still a zero-return production stub.
Its 40-word retail matrix builder must be recovered next, using its actual
angle/translation/scale inputs and three helper calls. Its interface remains
an explicit modeled boundary in this checkpoint. The actor lookup is unchanged;
only the actual point-transform connection is freshly exercised here.
Do not claim initialized production matrix data, complete gameplay, portable
fault semantics, hardware FCSR parity or an automatic PC-port repair.

Continue that helper and the wider failed-source/binding queue. The handwritten
Init hardware routines and unmatched `func_1510BF60` seed remain separate open
work. This single guarded recovery does not complete the full goal.
