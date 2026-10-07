# Game Matrix-Route Private Layout And Semantic Recovery

Date: 2026-10-07

## Scope And Installed Recovery

Continue `func_1514654C` from audit commit `58abdfa9` and
[Note 1103](1103-game-matrix-route-recovery-and-private-frame-audit-20261007.md).
VA `1514654C..1514672C`, ROM `1739FC..173BDC`: **120 words / 480 bytes**.
The previous production baseline was a padded three-word zero-return C
placeholder, not restored assembly. The
[original assembly](../../conker/asm/nonmatchings/game_16EE20/func_1514654C.s)
remains the retail reference.

The [owner](../../conker/src/game_16EE20.c) now contains the complete semantic
six-word-ABI wrapper. **All 120 meaningful body words**, frame **`0xA0`**,
converted matrix **`sp+4C`**, resolver primary/secondary outputs
**`sp+90/+8C`** emit from C under the unchanged O2/g3/MIPS2 profile. This is
an **installed nonmatching recovery, not a byte match**: 60 raw word
differences remain, versus 115 in the padded zero-return slot. No new guard,
instruction insertion/omission, frame/private-offset patch, profile change,
shared header change or conversion-ledger edit.

## Contract And Real Source Lifetime

The wrapper preserves the four retail routes from Note 1103: attachment
flag/page/index selection, keyed lookup/resolution and post-callback
attachment reread, descriptor-bank page selection, and delegated actor-bank
selection through matched `func_15145EA4`. Null actor/descriptor/actor-bank,
failed lookup/resolver and null selected fixed matrix return zero. The
delegated route returns one independently of incidental callee V0.
Common fixed routes convert with `guMtxL2F`, then reload incoming point-list
and signed-count homes. Positive counts use the seven-word point-transform
ABI and four-byte list strides; nonpositive counts do not dereference lists.
There are no index clamps or delegated null/zero-point fallbacks on common routes.

The [layout driver](../../tools/experiments/game_matrix_route_layout_candidates.py)
fits real C storage rather than injecting padding or changing instructions:

- `matrix` holds the initial actor bank, then the selected fixed matrix.
- `input` holds the temporary lookup-node address, then the point-list cursor
  after conversion. Casts preserve that disjoint pointer lifetime.
- Real resolver outputs precede `converted[4][4]` in declaration order;
  seven scalar locals and the matrix recover the retail frame allocation.
- The common success return is outside the nonnull-matrix gate. The eight
  epilogue words emit directly as retail.

Selected source is `pointer-reuse1-first0-lookup0`. Existing ECOFF debug
parsing independently reports frame `0xA0`, matrix at entry SP minus 84,
primary at minus 16 and secondary at minus 20. Executed converter/resolver
arguments independently confirm the same real private addresses.

The old experimental C119/frame `0xA8`/58-difference form is retained as a
control, not installed. Its smaller raw difference count did not make it
equivalent: all sixteen private-matrix counterexamples differed publicly.
The new full-length C closes all sixteen without offset normalization.

## Remaining Byte-Matching Work

The sixty differences are not a proven independent scheduling permutation:

- Initial bank, descriptor, lookup and later point-cursor saved-register
  allocation phases still differ.
- C loads the lookup key into A1 and uses a branch-likely zero-key route;
  retail loads V0 and uses a normal branch with the key-to-A1 delay move.
- Retail reads the resolver primary before the post-resolver attachment
  branch and reloads it on the attached path. Current C reads it per branch.
- The selected C keeps the chosen matrix in S0 and moves it to A1 at
  conversion; retail already has it in A1. Earlier blocks shift by a word,
  then realign at the `guMtxL2F` call at `+150`.

Continue source key/primary-read/register lifetime fitting. Do not turn these
differences into sixty bulk guards or normalize branch/control-flow/read order.
Full byte matching remains the objective, separate from this semantic checkpoint.

## Maintained Qualification

[Layout tests](../../tools/tests/test_game_matrix_route_layout_recovery.py)
extend the [previous recovery tests](../../tools/tests/test_game_matrix_route_recovery.py)
without discarding the old private-overlap rejection evidence.

- **1,728 ordinary fixtures**, all routes/failures, signed counts, two pages,
  three valid indices, sequential aliases and two stack phases; compare
  public reads/writes/calls and the full return word.
- **336 incoming-home mutations** and **24 post-resolver attachment changes**;
  exact private argument addresses agree, with caller-saved GP/FP clobbers.
- **864 connected original-helper cases**, using retail lookup/resolver,
  converter/point/list/translation instructions. This is bounded coverage,
  not complete callee-path coverage or full stack-memory equivalence.
- **16 old private-matrix counterexamples**: old C differs in all sixteen,
  new C differs in none. **560 additional overlaps** exercise matrix source,
  destination and primary/secondary output storage using original helpers;
  public outputs/calls and private argument addresses agree.
- **77 additional source controls**, none raw exact: twelve topology, sixteen
  storage, sixteen parameter, twelve indexed, twelve pointer-phase and nine
  output-phase forms. **1,848 ordinary executions** qualify; private/home
  equivalence is not asserted for every control. Together with Note 1103's
  208 controls / 4,992 ordinary executions, retain **285 measured forms**.
- **Six compiled semantic negatives** produce actual public output/return
  differences; unexpected faults are not accepted as detections. Five lazy
  gates, twelve required-storage faults and four guest-only wrapping indices
  retain the prior contract. Native cases stay inside valid matrix objects.
- **9,216 native 32-bit cases plus three lazy gates**, complete selected C
  and actual SDK converter C, warnings-as-errors. Other native callbacks
  remain bounded validating models. No hardware FCSR/rendering claim.
- Copied owner: **89 functions / 88 unchanged neighbors**, equal normalized
  pools, same two warning statements and exact isolated target bytes/relocations.
- Actual padder: complete **120 words / nine relocations / six independent
  symbols**, independently rebased through HI/LO carry. Raw nonmatching body
  preserved with no new guards, insertion or omission.

Production `func_15031070` remains a separate zero-return placeholder.
Connecting its original instructions in tests does not restore that callee to
production C, qualify arbitrary stack aliases or establish PC-port acceptance.

Early parameter declaration insertion and renamed lookup-marker mistakes in
the experiment generator were corrected before qualification. The corpus
caught the omitted primary assignment; failed harness runs are not passing
receipts. A read-only GDB debug-local attempt failed; the existing repo ECOFF
parser supplies the independent metadata check instead.

Ten corrected core pre-install tests pass in **111.756 seconds**, and the
actual-padder test passes in **3.357 seconds**. After installation/build,
all **twenty combined tests pass in 313.807 seconds**, zero skips/errors/
failures. Three affected tests re-pass in **4.211 seconds** after receipt-only
wording corrections. Tools, Python syntax and scoped whitespace checks pass.
The documentation checker verifies **86 documents / 3,996 relative links /
zero broken links**.

```sh
python3 -m unittest tools.tests.test_game_matrix_route_layout_recovery tools.tests.test_game_matrix_route_recovery -v
make -C conker -j4 build/conker.us.elf
make tools-check
```

## Linked Audit And Resume

The production ELF rebuild succeeds. Existing duplicate-recipe warnings and
the owner's two existing warning statements remain; no isolated candidate
diagnostic. Only `func_1514654C` changes across **6,058 symbols / 6,042 retail
slots**. All **6,041 other retail bodies**, addresses/extents, sixteen overflow
symbols, protected sections, **11,063 guard rows** and conversion-ledger hash
remain unchanged. All **720 Game-data owners / 189,088 bytes** remain exact.
Matched neighbors `func_151464B8`, `func_15146508` and `func_1514672C` stay intact.

Matching is unchanged: total **3,364/5,466 (61.54%)**, Game
**2,691/4,793 (56.14%)**, **2,102 different**, zero address drift; Init
492/492 and Debugger 181/181 exact. Conversion totals are unchanged because
the replaced placeholder already counted as C. Leave root README aggregates
unchanged and keep the detailed update here.

The ignored authoritative checkpoint is
`conker/build/game-matrix-route-layout-test/after.json`, with `audit.json`.
The previous matrix-route audit script assumes the old production placeholder;
do not rerun it after this installation. Resume from the new checkpoint and
maintained private/home tests, then fit the key branch, primary read order and
register phases above. Resolver C, basis layout, translator scheduling and
sampler lifetime remain separate work. No sibling repository, frozen Release,
real save, runtime/hardware or push action.
