# Init Distance Operation O2 Full Masked CU1 Set Corpus

Date: 2026-10-04. Starting HEAD: `fb4edfb5`.

## Scope

Complete the matching full guarded qualification of Note 911's distance-operation
local, combined with packed-remaining dynamic order, pointer-owned core and
176-byte tight adapter. Fresh setup compiles six images, then selects exactly
packed O2/g3. Input/fifth-slot initialization guards, live-SP write fencing
and pre-return callee receipt checks remain active. Candidate sources and flags
are unchanged from the CU1-clear run in Note 912.

```sh
env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=set CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalCorpusTests -v -f
```

Each DMA-rounded retail page is paired with reference execution and pristine
image output. Comparisons include output/result, architectural context, final
FPR/GPR state and guarded storage. Compiled-core execution is required, without
original-core fallback. This remains guest/model evidence, not hardware/gameplay.

## Result

All 507 paired pages pass in 818.478 seconds, no skips, exit zero.

```text
shadow corpus context: exception-masked cu1=set status=0x2400FF00
shadow CU1-set corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=set pages=507 text=4512 depth=3248 low=0x80031D60 margin=80
shadow corpus complete: modes=set runs=507
Ran 1 test in 818.478s
OK
```

With [Note 912](912-init-distance-operation-o2-full-masked-cu1-clear-corpus-20261004.md),
both masked CU1 modes now cover 1,014 paired page runs for this unchanged
candidate. Both confirm text 4,512, maximum descent 3,248, minimum SP
`0x80031D60` and known-neighbor margin 80. Observed depth equals the static
bound. Executable text remains 528 bytes above retail 3,984.

Known-neighbor clearance and write-only live-SP fencing do not establish full
private reservation ownership or absence of below-SP reads. Neither corpus
establishes retail ROM placement, hardware behavior or production ownership.

## Integrity And Supporting Checks

All six SHA-256 hashes match before/after this run and Note 912:

```text
43A3897FE734E8000F4C156CDB3DB69722D25A210B5B518C02EA315BD71CA0C2 init_decompressor_semantic.c
A8D2642E81EA3960B0A9CFABDF61BDB04F2F3A951D7E8B2251228B5FE9DC72CB init_decompressor_core_adapter.s
E5792E1FDB2A12A7273A0BE3B91BD67E557801CBC6EA54896F9A7926BCBA3506 compile_init_decompressor.py
1280377B35F3582B29A2D7FDC4F28A7237E7CF3F9BFBEA35093458A05275BAFD test_init_decompressor_distance_operation_local.py
0760CACC7BC4FD78C19E63D6D0B48B0195E2B7AF342B7CDE7E2139C22642616C test_init_decompressor_live_stack_writes.py
F9ADF06BEC8B674F78FAE7E7FAFA4D79DF62FA575F96A58A78543F90D3828663 test_init_decompressor_shadow_corpus.py
```

Twenty-two supporting ledger, corpus-selection, exception-mask and storage tests
pass in 47.894 seconds, no skips:

```sh
python3 -m unittest tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_corpus_selection tools.tests.test_init_decompressor_exception_mask tools.tests.test_init_exception_storage -v -f
```

Supporting compiled masked-context checks use their existing default configuration;
the changed candidate's full corpus is the separate result above. Note 911's
bounded suite, backreference table-stability gate and option-omitted default text
comparison are prior evidence, not rerun here. Tool and whitespace checks pass.

## Next Work

- [x] Full guarded packed O2 masked CU1-clear corpus: Note 912.
- [x] Full guarded packed O2 masked CU1-set corpus: this note.
- [ ] Reduce the complete linked footprint by at least the remaining 528 bytes.
- [ ] Prove full private-stack reservation and entry/frame ownership.
- [ ] Establish required hardware/context behavior before production promotion.
- [ ] Requalify any subsequently changed candidate; these receipts do not transfer
  automatically to new source, flags, adapters or layouts.

The current qualified O2 candidate is now Note 911 with `--distance-operation-local`
enabled, not the previous option-omitted dynamic-order baseline. This does not
change defaults or make the candidate production-ready. Continue fitting with a
new source hypothesis and compare whole linked text plus nested stack bounds.

Production Init remains 492 C / 47 assembly routines. No production source,
README aggregate, word guard, sibling artifact or Release changed. Pending Game
and actor/timeline work remains untouched and unstaged. No ROM build or push.
