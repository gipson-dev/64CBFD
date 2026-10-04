# Init Simple Seed Full Masked CU1-Set Corpus

Date: 2026-10-03. Baseline: `4748564e`.

## Result

All 507 retail pages pass on the freshly compiled current packed/remaining
O2/g3 combination with exception-masked FR=1 and CU1 set. The full-corpus
test passes in 784.455 seconds, with no skips.

```text
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4768 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=set runs=507
Ran 1 test in 784.455s
OK
```

Together with Note 856, both masked CU1 modes now pass on this unchanged
current combination: 1,014 paired retail-page runs. The two separately
banked receipts have identical text, maximum descent, minimum SP and
known-neighbor clearance. This completes the two-mode gate for this profile,
not the decoder conversion or complete hardware/context qualification.

| Masked mode | Paired pages | Seconds | Linked bytes | Observed descent | Clearance |
| --- | ---: | ---: | ---: | ---: | ---: |
| CU1 clear, Note 856 | 507 | 800.807 | 4,768 | 3,240 | 88 |
| CU1 set, this note | 507 | 784.455 | 4,768 | 3,240 | 88 |

Maximum observed descent equals the static bound. Minimum SP is
`0x80031D68`; the known protected neighbor ends at `0x80031D10`.
Complete reservation ownership and actual hardware behavior remain open.

## Selected Implementation

This run targets the same Note 855 simple-operation/ABI-seed combination
as the CU1-clear corpus in [Note 856](856-init-simple-seed-full-masked-cu1-clear-corpus-20261003.md).
Scoped Git inspection confirms the relevant experiment/test sources are
unchanged from `bcdf026`. All six guest images compile freshly; only
packed/remaining O2/g3 is selected for this full corpus.

The selected image has 4,464 core bytes plus the Note 853 core-owned-state
adapter's 304-byte aligned contribution: 4,768 linked bytes. The adapter
body is 296 bytes and the C state is 116 bytes. The current text remains
784 bytes above the 3,984-byte retail decoder group. Complete flags,
matrix selection and bounded semantic domain are recorded in Note 855.

## Reproduction

Run from the repository root:

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_simple_seed_combination.InitDecompressorSimpleSeedCombinationCorpusTests -v -f
```

The printed context status is `0x2400FF00`: FR=1, CU1 set, with the
exception-masked selector. The class carries the selected C flags,
core-owned-state adapter flag and poisoned-state fixture. This is paired
guest instruction-oracle qualification, not MIPS hardware execution.

## Comparison Scope

Each retail page is paired with original assembly and the reference
decompressed image. The checks cover return/state, output/workspace writes,
restored GPR/FPR values, scratch FPR snapshots, status values/transitions,
FPR context load/store receipts, physical frame and caller context,
rounded DMA input-read bounds and call-stack descent. The compiled core
and adapter must execute; the original core must not.

The fixture still poisons reservoir, bits, produced count, limit, allocation
count and workspace address. Reads before executed initialization fail.
This does not prove asynchronous intermediate-state or hardware fault/cache/
bus behavior. The Note 855 bounded domain is prior evidence for unchanged
source/flags, not a fresh bounded rerun here.

## Supporting Checks

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger
wsl make tools-check
git diff --check
```

All thirteen helper/slot-ledger tests pass in 0.045 seconds. Together with
the corpus test, fourteen tests pass with no skips. Tool and diff checks
pass; compiler/linker logs are empty. No production build, ordinary full
suite, other-profile corpus, hardware replay or sibling-port test is claimed.

## Next

- [x] Current-combination full masked CU1-clear and CU1-set corpora: Notes 856/857.
- [ ] Return to structural fitting: selected linked text remains 784 bytes over retail.
- [ ] Other-profile full corpora before broader profile claims or promotion.
- [ ] Complete reservation ownership, hardware behavior and real scheduler/
  debugger resume gates.

Older histogram-only full-corpus receipts are not reassigned to the current
implementation. Production Init, experimental source bodies, adapter,
compiler defaults and README totals remain unchanged. Unrelated Game work
is preserved and excluded.
