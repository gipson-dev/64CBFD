# Init Scan Deficit O1 Full Masked CU1 Clear Corpus

Date: 2026-10-04. Starting HEAD: `c9854073`.

## Scope

Qualifies the Note 892 opt-in builder scan-deficit candidate in packed O1,
masked exception context, CU1 clear. This is the profile with the 32-byte
fitting improvement. Setup freshly builds six shapes, then selects exactly
`packed-remaining/o1` for all-page execution. Live-SP and core-return callee
guards remain inherited from the strongest retained fixture.

```sh
env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o1 python3 -m unittest tools.tests.test_init_decompressor_builder_scan_deficit.InitDecompressorBuilderScanDeficitCorpusTests -v -f
```

Each of the 507 supplied pages is rounded to its retail DMA extent and paired
with reference execution. Expected output is checked against the pristine
retail image. The inherited comparison requires executed compiled core/adapter,
checks outputs/result, architectural context and final FPR/GPR state, and
rejects guarded storage/callee violations. No original-core fallback is used.
This is bounded guest/model qualification, not MIPS hardware acceptance.

## Result

All 507 paired pages pass in 975.542 seconds, no skips, process exit zero.

```text
shadow corpus context: exception-masked cu1=clear status=0x0400FF00
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o1 cu1=clear pages=507 text=5984 depth=3200 low=0x80031D90 margin=128
shadow corpus complete: modes=clear runs=507
Ran 1 test in 975.542s
OK
```

Linked text is 5,984 bytes. Maximum observed descent 3,200 equals the bounded
suite's static packed O1 bound. Minimum SP `0x80031D90` clears the known
neighbor end `0x80031D10` by 128 bytes. Clearance and the write-only live-SP
fence do not establish full stack reservation or ownership.

This new result does not qualify CU1 set or changed packed O2. Notes 887/888
remain evidence for their unchanged default packed O2 configuration, not this
option. Host harness time is not hardware performance.

## Supporting Verification

Twenty-six focused ledger/selection, FR=1 word-load, scan-domain algebra,
executed scan-branch, CLI dependency, exception/storage regressions pass in
5.154 seconds, no skips. With the corpus, twenty-seven tests pass without
skips. Note 892's whole bounded suite is prior evidence, not rerun here.

Six tracked source blobs match before/after, with empty scoped Git diffs:

| Source | Git blob |
| --- | --- |
| `init_decompressor_semantic.c` | `42b4a7d418964cb81900a6206fb31096e9089bd4` |
| `init_decompressor_core_adapter.s` | `68f9ede617a36aebe706b6b30feed89dcfef7b4f` |
| `compile_init_decompressor.py` | `52d259f9b93f3a3cf92c63382dc0166c5f9404f5` |
| `test_init_decompressor_builder_scan_deficit.py` | `8fd693e4d391ccc7456e020e815b31593ec6bcf9` |
| `test_init_decompressor_live_stack_writes.py` | `b78e5e609ed103ae51e6f0db0a0c7e2f17ac946c` |
| `test_init_decompressor_shadow_corpus.py` | `d2a3f155672616bbeb3033a9f73e5bdce43a59fa` |

Current structured inventory remains 492 C / 151,796 bytes and 47 assembly /
12,252 bytes. No production conversion, ROM build, gameplay or sibling-port
test is claimed. Production/defaults/README and unrelated Game work unchanged.

## Remaining Gates

- [x] All 507 guarded scan-deficit packed O1 masked CU1-clear pages.
- [x] Matching guarded packed O1 masked CU1-set corpus in [Note 894](894-init-scan-deficit-o1-full-masked-cu1-set-corpus-20261004.md).
- [ ] Changed-option packed O2 qualification if selected for continued fitting.
- [ ] Best-profile fitting, full reservation, entry/frame ownership and hardware/context.
