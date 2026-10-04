# Init Simple Seed Full Masked CU1-Clear Corpus

Date: 2026-10-03. Baseline: `bcdf026`.

## Result

All 507 retail pages pass on the freshly compiled packed/remaining O2/g3
simple-operation/seed-cursor combination, with exception-masked FR=1 and
CU1 clear. The full-corpus test passes in 800.807 seconds with no skips.
This is the first full-corpus receipt for the current Note 855 combination;
the other masked CU1 mode remains open for this changed implementation.

```text
shadow CU1-clear corpus: pages=507/507 runs=507/507
shadow corpus terminal: packed-remaining/o2g3 cu1=clear pages=507 text=4768 depth=3240 low=0x80031D68 margin=88
shadow corpus complete: modes=clear runs=507
Ran 1 test in 800.807s
OK
```

Linked text remains 4,768 bytes. Maximum observed descent is 3,240 bytes,
equal to the static bound; minimum SP is `0x80031D68`, 88 bytes above the
known protected neighbor ending `0x80031D10`. Neither this fence nor the
full corpus resolves complete reservation ownership or hardware behavior.

## Selected Implementation

This run targets the current smallest bounded-qualified Note 855 combination,
not the older histogram-only implementation from Notes 845/846. It compiles
all six guest images freshly, then selects only packed/remaining O2/g3 for
the full corpus. Selected state is 116 bytes; core text 4,464 bytes; the
core-owned-state adapter has 296-byte body / 304-byte aligned contribution.
Selected linked text is 4,768 bytes, 784 above the 3,984-byte retail group.

The selected C flags include packed entries, bounded builder shifts/scans,
no loop unroll, dynamic/symbol/histogram/fixed cursors, counts/offsets caching,
loop lookup, masked block dispatch, buffered-byte rewind, packed header,
shared stored lengths, shared dynamic repeats, ABI seed cursor and arithmetic
simple-operation selection. FPR-shadow and physical-frame modes remain active.
Adapter symbol `INIT_DECODE_CORE_OWNS_STATE=1` omits the redundant stores;
the fixture poisons those fields and rejects reads before initialization.

## Reproduction

Run from the repository root:

```powershell
wsl env CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_CU1=clear CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_simple_seed_combination.InitDecompressorSimpleSeedCombinationCorpusTests -v -f
```

The printed context status is `0x0400FF00`: FR=1, CU1 clear, with the
exception-masked selector. The opt-in class carries the current C flags,
adapter flag and poisoned-state fixture. It is a paired instruction-oracle
qualification, not execution on MIPS hardware.

## Comparison Scope

Each of the 507 retail pages is paired with original guest assembly. The
decompressed output also matches the reference image at its page offset.
The fixture checks decoder return/state, output/workspace writes, full
restored GPR/FPR values, scratch FPR snapshots, status values/transitions,
FPR context load/store receipts, physical frame contents, preserved caller
context, rounded DMA input-read bounds and call-stack descent. Execution
must reach the compiled core and adapter, not the original retail core.

The poisoned fields cover reservoir, buffered bits, produced count, limit,
allocation count and workspace address. Their guest reads fail until an
executed four-byte write initializes each field. This does not qualify
asynchronous intermediate-state observations or hardware faults.

## Supporting Checks

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_slot_ledger
wsl make tools-check
git diff --check
```

All thirteen helper/slot-ledger tests pass in 0.033 seconds. Together with
the corpus test, fourteen tests pass with no skips. Tool and diff checks
pass. Compiler/linker logs are empty. No production build, ordinary full
suite, other-profile corpus, hardware replay or sibling-port test is claimed.

## Remaining Work

- [x] Fresh changed-source masked CU1-clear full corpus: all 507 pages.
- [ ] Fresh changed-source masked CU1-set full corpus.
- [ ] Other-profile full corpora before any broader profile claim.
- [ ] Structural fitting: selected text is still 784 bytes over retail.
- [ ] Complete stack-reservation ownership, hardware fault/cache/bus behavior,
  real scheduler/debugger resume and promotion gates.

The Note 855 bounded domain is historical evidence for the same unchanged
source/flags, not a fresh bounded rerun in this note. No prior full-corpus
receipt is reassigned to this changed combination. Production Init,
experimental source bodies, adapter, compiler defaults and README totals
remain unchanged. Unrelated Game work is preserved and excluded.
