# Game Matrix Scheduling And Point-List Lifetime Audit

Date: 2026-10-07. Baseline: `adced222`,
[Note 1095](1095-game-matrix-translation-qualified-recovery-20261007.md).

This checkpoint adds measured controls and maintained qualification, **not a
new byte match**. Production C, compiler profiles, headers, generated objects,
guards and README aggregates are unchanged. Neither target receives guards,
padding locals, inserted instructions or an assembly fallback.

| Function | Complete Raw C | Frame | Positional Differences | Status |
| --- | --- | --- | --- | --- |
| `func_15142314` | 49 words / 196 bytes | zero | 34 | Qualified arithmetic, scheduling still open |
| `func_15145CD0` | 57 words / 228 bytes | `0x88` | 46 | Ordinary public effects audited, saved-register/readback lifetime still open |

## Matrix Scheduling Controls

[Schedule driver](../../tools/experiments/game_matrix_translation_schedule_candidates.py)
adds **26 measurements** to the retained 152 historical measurements:

- Sixteen O2/g3 typed views: a size-checked 64-byte union of fixed halfword
  planes and float rows, signed-halfword indexing, float-row indexing and the
  actual SDK `Mtx` view; repeated/common address and scale operand placement.
  All sixteen still emit 49 words, frame zero, no pool and 34 differences.
- Eight assembler controls evidenced by the local IDO 5.3 `as1` option table:
  `-no_branch_target`, `-noxbb`, `-nobopt`, `-noglobal`, `-nopeep`, `-noswpipe`,
  `-O0` and `-O1`, forwarded with `-Wab`.
- Two generator controls from its option table: `-notailopt` and
  `-nooffsetopt`, forwarded with `-Wc`. The initial `-Wg` pass spelling was
  rejected, corrected and excluded from the measured bank. Two initial
  incompatible array-pointer initializers were likewise corrected before
  qualification; neither failed form is counted as evidence.

The original compiler files named in the local recompilation Makefile are
absent. Read the embedded option data from the available local recompiled
tools instead; do not infer support from unrelated modern compiler options.
Assembler optimization-level controls are measured output, not evidence that
the requested level overrode every binasm directive.

`-no_branch_target` and `-nobopt` each emit 49 words / 33 differences and an
ordinary branch, but retain a NOP delay slot and the unresolved constant and
return-store schedules. `-noxbb` emits 48 words / 46 differences;
`-noglobal` emits 49 / 37. The other six controls emit 49 / 34. None is exact.
These are isolated controls, not installed production profile changes.

All 26 pass 24 bounded public-effect fixtures each: **624 candidate
executions**, complete external memory and ordered output writes. Do not
claim every candidate's public-read order or general FCSR/hardware behavior.
The new bank is 26 measurements, not 26 distinct emitted bodies. The existing
152-measurement bank remains historical evidence, not another new sweep.

## Pointer-List Transformer

`func_15145CD0`, VA `0x15145CD0..0x15145DB4`, ROM
`0x173180..0x173264`, is already semantic C rather than a placeholder:

1. Always call `func_150A8050` with the three float words at descriptor `0/4/8`,
   even for zero or negative counts.
2. After that call, reread signed halfwords at `0x10/0x12/0x14`; convert each
   to float and fill matrix row three. Provider changes to those fields matter.
3. For every positive-count iteration, read the current source and destination
   pointers from their two four-byte-stride lists. Forward source XYZ and the
   three output addresses to `func_150A7960`.
4. Decrement the signed count and advance both cursors. In-place outputs and
   outputs overlapping future source records must affect subsequent calls;
   do not snapshot the whole list or all points.

[Candidate driver](../../tools/experiments/game_point_list_transform_candidates.py)
retains **48 nonmatching measurements**:

- Eight loop/record forms across O2/g3, O2, O1/g3 and O1: ordinary while,
  guarded do/while, for-loop updates and post-incremented list loads, each
  using `struct17` or float-array views. O2 forms have 57 or 58 words/frame
  `0x88`; O1 forms have 66-68 words/frame `0x70` and do not fit.
- Eight meaningful cursor/count declaration-lifetime forms. They have 59
  words/frame `0x90` or `0x98`; none fits or matches.
- Eight cursor/parameter-readback controls with pointer parameter qualifiers
  and the output-cursor initialization before or after translation loads.
  All retain 59 words/frame `0x90`/59 differences. The qualifiers do not
  produce the original readback schedule in this local compiler.

Each has empty diagnostics and no pool. All 48 pass **18 ordinary public-
effect fixtures / 864 candidate executions**. This does not qualify them
against arbitrary mutations of the incoming argument homes.

### Remaining Lifetime Boundary

Original prologue saves `s0..s3` plus RA, spills incoming A1/A2 at original
caller homes and retains the descriptor in `s1` until its final halfword read.
It loads the destination-list cursor into `s2` after the provider, then reuses
`s1` for the source-list cursor after the final descriptor load. Saved-register
slots begin at `sp+0x24`; RA is at `sp+0x34`; matrix is at `sp+0x48`.

Current raw C instead retains both lists in registers across the provider,
uses an additional saved `s4` for the descriptor, has different save slots,
and shifts the helper-call/loop locations within the same 57-word extent.
This is **not just a closed register rename or independent instruction swap**.
Do not normalize 46 words blindly or move private offsets by hand.

Two explicit incoming-home overwrite probes, at both tested stack phases,
confirm a public-storage difference: when the provider rewrites caller homes
`SP+4/SP+8`, retail reloads redirected lists and current C uses retained lists.
This is a nonstandard assembly/ABI boundary, not a claim that an ordinary C
callee may freely overwrite its caller's arguments. Preserve and test it
before claiming complete retail matching. The production source stays put.

## Maintained Qualification

[Audit tests](../../tools/tests/test_game_point_list_transform_audit.py) cover:

- **1,344 guest fixtures** over seven signed count patterns, 16 angle/halfword
  patterns, three output/source alias arrangements, provider mutation and two
  stack phases. Raw C and retail agree on all external memory, actual forwarded
  calls and ordered public traces. Both complete 57-word bodies are covered;
  hooks validate all 16 matrix words, not only the translation row.
- **580 connected cases** execute the actual original 40-word
  `func_150A7960`, including four nonpositive routes with all lists/point/
  output storage unmapped. The rotation provider remains a bounded hook;
  final external storage is independently checked. This is not a hardware
  timing, rendering or general FCSR claim.
- **131,076 actual native 32-bit cases**: every signed-halfword pattern in
  each translation field through correlated permutations, both provider
  mutation modes, real pointers, all five input/output records and descriptor
  fence bytes; four nonpositive-count calls use null lists. The native transform
  is a validating copy hook, not the SDK's full matrix arithmetic. This is not
  Cartesian-domain or 64-bit host-port qualification.
- Required descriptor/list/point/output bytes fail closed; nonpositive paths
  do not read unused lists. Two argument-home probes retain the open mismatch.
- Five effective compiled negatives change public storage: unsigned
  translation, exact-one count gate, wrong input stride, cached first source
  and translation assignments before the provider.
- The 48 pointer-list and 26 matrix-schedule measurements are pinned with
  bounded public-effect fixtures. Both installed source bodies, complete
  linked slots/addresses/raw differences and unchanged guard history are pinned.

Initial eight-test audit passes in **65.838 seconds**. Combined translator/
point-list/owner-pool/padder regression passes **25 tests in 376.363 seconds**.
The strengthened native-storage and added fail-closed gates pass **two tests
in 0.684 seconds**. Final complete nine-test audit, including explicit helper
word coverage and redirected input/output assertions, passes **nine tests in
70.488 seconds**. All runs have zero skips/errors/failures. Repeated runs are
not additional distinct fixtures. Tool checks, syntax and scoped whitespace
checks pass. Final documentation gate checks **78 documents / 3,910 relative
links**, zero broken.

```sh
python3 -m tools.experiments.game_matrix_translation_schedule_candidates
python3 -m tools.experiments.game_point_list_transform_candidates
python3 -m unittest tools.tests.test_game_matrix_translation_recovery \
  tools.tests.test_game_point_list_transform_audit tools.tests.test_game_owner_pool \
  tools.tests.test_pad_c_object_word_patches -v
```

## Production Audit And Resume

Compare the fresh linked image against the retained `adced222` snapshot:
all **6,058 symbols / 6,042 retail slots / 16 overflows**, every address/extent,
protected Init/Init-data/Debugger/Game-data section and **11,006 guards** remain
identical. All **720 Game-data owners / 189,088 bytes** remain exact. No
production rebuild is required or claimed for this tools/tests/docs checkpoint.

Matching totals remain **3,360 / 5,466 (61.47%)** overall and
**2,687 / 4,793 (56.06%)** Game, **2,106 different**, zero drift. Main README
already has the correct aggregates and remains unchanged. Detailed progress
belongs here and in the status/index/log/roadmap, not in the main README.

Next resume: investigate the legitimate descriptor-to-source cursor lifetime
and incoming-list readbacks in `func_15145CD0`, without adding dummy work or
patching private storage. Keep the 48 measurements and home-overwrite probes;
do not repeat the same forms as new evidence. Translator scheduling remains
open with 178 retained measurements; the selected 49-word body stays unguarded.
Sampler `func_151432BC` remains unchanged and still needs its per-path RA
reloads and circle RNG-byte schedule. No new sampler measurements here.

No sibling/frozen Release build, source transplant, save/runtime action,
rendering/hardware acceptance or push. Ignored receipts are under
`conker/build/game-matrix-translation-schedule/`,
`conker/build/game-point-list-transform/` and
`conker/build/game-point-list-transform-test/`.
