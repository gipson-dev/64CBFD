# Init Shared Lookup Loop Fitting And Context Qualification

Date: 2026-10-03. Baseline: `875b229`.

## Result

An opt-in shared lookup loop reduces the smallest shadow core text by 16 bytes
at O2/g3 and 48 bytes at O1. It passes 420 bounded context comparisons across
six compiler shapes/profiles and both CU1 modes, including masked entry samples.
Default profiles and production ownership remain unchanged.

The smallest combined core/adapter is now 4,880 bytes, still 896 bytes over
the retail 3,984-byte group. Stack descent and known-neighbor clearance remain
3,256 and 72 bytes. This is a small fitting improvement, not a finished
conversion or a new full-corpus qualification.

## Source Shape And Rejected Trials

`--loop-lookup` selects `INIT_DECODE_LOOP_LOOKUP` in the isolated compiler tool.
The old two-path lookup remains the default. The new loop shares root and
subtable dispatch: refill bits, select root or the previous entry's value,
compute the masked index, return on a leaf/invalid code, otherwise drop the
entry bits and repeat with the child width.

Importantly, the child entry value is read after the next `need_bits`, just
as in the original source. It is not cached before refill. The mask retains
the defined `width & 31` shift behavior; no defensive early return is added.
The entry pointer is null only before the initial root lookup.

Before retaining this shape, two other size-only trials were rejected:

| Packed/remaining shadow trial | O2/g3 core text | O1 core text |
| --- | ---: | ---: |
| Existing baseline | 4,576 | 5,984 |
| Existing `--flat-bits` | 4,608 | 6,048 |
| Inline lookup mask expressions | 4,592 | 6,000 |
| Retained shared lookup loop | 4,560 | 5,936 |

The temporary inline-mask flag/branch is removed; no equivalence is claimed
for it. `--flat-bits` remains an unchanged preexisting option, not a new default.
Local receipts are under ignored `conker/build/init-shadow-{flat-bits,inline-lookup-mask,loop-lookup}-20261003`.

## Qualified Costs

All six newly compiled loop variants retain the 116-byte shadow state and
320-byte adapter. The bounded tests report:

| Shape/profile | Linked text | Static total bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 6,112 | 3,272 | 3,272 |
| Frame O1 | 6,448 | 3,192 | 3,192 |
| Aligned/end O2/g3 | 4,912 | 3,240 | 3,240 |
| Aligned/end O1 | 6,240 | 3,176 | 3,176 |
| Packed/remaining O2/g3 | 4,880 | 3,256 | 3,256 |
| Packed/remaining O1 | 6,256 | 3,184 | 3,184 |

Total bounds include the original physical frame and shadow adapter area;
the packed core-only call-frame bounds remain 408/336 bytes. The O2 lookup
helper itself grows from a 40-byte to a 48-byte frame, but it does not increase
the overall maximum, which is dominated by the builder path. No universal
claim of lower stack use is made. Known protected neighbor ends at 0x80031D10;
packed O2 minimum SP remains 0x80031D58 in the tested domain.

The unchanged default suite is freshly compiled and reports the prior linked
text/descent values, including packed O2 4,896/3,256 and O1 6,304/3,184.

## Verification

The shadow fixture accepts optional subclass compilation flags without
changing its default shape set. A new test subclass selects `--loop-lookup`
and reuses the complete existing bounded shadow domain (348 comparisons),
plus the masked vector/sample domain (72). These 420 comparisons are a separate
new-source receipt, not added to the historical default-suite count.

They check modeled GPR/FPR values and masks, Status traces, wrapper context,
scratch FPR snapshots, base state, physical scratch and changed output/workspace
contents, with the corrected neighbor guard and rounded DMA read bounds.
Error, incomplete-tree, match-history and multiblock cases retain their gates.

A separate masked-CU1-set packed O2 execution on retail page 169 proves the
new nested loop is exercised: 3,212 helper calls, 3,383 loop iterations, 171
additional nested iterations. The test finds the unique internal backward
unconditional branch and checks its target is visited more than the helper
entry. It also checks output; this probe is not counted among the 420 paired
context comparisons.

Two terminal test receipts:

- Optimized module plus unchanged default shadow module: 22 tests pass in
  324.530 seconds. This run preceded addition of the explicit nested-path gate.
- Newly added nested gate, optimized corpus class and original mask module:
  eight tests in 68.111 seconds, seven pass and one intentional corpus skip.
- In total, 29 pass and one skip. Fresh compilation/linking logs are empty.
- Root `make tools-check`, three Python syntax checks and `git diff --check` pass.
- No new full corpus, production build, hardware replay or gameplay test.

The opt-in corpus subclass compiles this variant explicitly and inherits the
existing context/profile selectors. Ordinary discovery skips it. To qualify
all 507 masked CU1-set pages for the smallest new-source profile:

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_loop_lookup.InitDecompressorLoopLookupCorpusTests -v -f
```

That gate is not run in this checkpoint. [Note 827](827-init-full-masked-shadow-corpus-20261003.md)
remains the 507-page receipt for the previous default source shape; it is not
reassigned to the new variant. Production Init and README totals are unchanged;
pending Game work and sibling repositories remain untouched.

## Next

- [x] Retain a smaller opt-in lookup shape and qualify bounded contexts.
- [x] Prove the new nested path is exercised; verify defaults remain unchanged.
- [ ] Full masked corpus on the changed variant, starting with packed O2/g3.
- [ ] Remaining full-corpus profiles and explicit CU1-clear qualification.
- [ ] Complete storage ownership and synchronous-fault bounds.
- [ ] Continue actual builder/shared-helper/adapter fitting; 896 bytes remain.

Do not promote this variant into production solely from its smaller size and
bounded passes. The nonstandard entry/context and fitting gates still apply.
