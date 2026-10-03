# Init Block-Local Storage Writers and FR1 Fixture Correction

Date: 2026-10-03

## Block-Local Audit

Extend [Note 838](838-init-static-storage-literal-census-and-enclosing-bss-clear-20261003.md)
with opt-in `--block-local` tracking in `audit_init_storage_literals.py`.
The original adjacent-pair reference list is unchanged. The new output is a
separate `block_local_references` list with defining instruction PCs.

Track known literal values through supported integer immediates, arithmetic,
shifts and copies. Report ordinary loads/stores through known bases. A loaded
pointer becomes unknown rather than being assigned its address. Direct incoming
branch/jump targets discard incoming values; branches/calls discard values
after their delay slots. Unknown instructions discard all tracked values.
Trapping ADDI overflow does not create a propagated result.

These are lexical block candidates, not a full control-flow or execution proof.
There is no path merge, interprocedural tracking, loop fixed point, loaded-global
pointer value, alias resolution, DMA model or full indirect-target inventory.
Branch-likely delay-slot candidates may be conditional. Text may also contain
nonexecuted words. No writer-absence or reservation-size claim follows.

## Retail Result

On the same SHA1-validated retail Init/Game/Debugger text ranges:

| Section | Address Candidates | Loads | Stores | Total |
| --- | --- | --- | --- | --- |
| Init | 17 | 5 | 33 | 55 |
| Game | 0 | 0 | 0 | 0 |
| Debugger | 1 | 0 | 0 | 1 |

The 33 Init store candidates are:

- `0x10001350` -> `0x800354F8`, publishing the aligned input pointer.
- `0x1000137C` -> `0x800354FC`, publishing the aligned page-table pointer.
- `0x100020A8` -> `0x80035500`, the clear in `init_2070.c`.
- Thirty wrapper saved-context stores from `0x10005E24` through
  `0x10005EA0`, including saved SP at `0x80032B18` and GPR cells below it.

Thread materializers at `0x10001128`, `0x100014B0`, `0x1000530C` and
Debugger `0x16000D50` also appear. The scanner discovers scheduled-apart
references missed by the original ten adjacent pairs, but it still does not
establish capacities or all writes. The existing executed wrapper/storage
tests remain stronger evidence for their particular paths.

## Callback Fixture Correction

Review found that Note 836's local callback fixture modeled SDC1/LDC1 as
FR=0 even/odd register pairs. This project's startup enables FR=1. Correct
that fixture to maintain an independent high word per FPR, saving/restoring
the full value of FPR20 without touching FPR21. SWC1 writes only the low word.

The independent test now uses a distinct FPR21 sentinel and verifies high/low
FPR20 round-trip plus big-endian SWC1. The retail callback scenario seeds a
separate high-word sentinel for FPR20. It passes both IDO caller profiles.
This supersedes the old pair-transfer interpretation, not the ROM-pinned
null-list branch or heap results. No Status transitions, CP0/COP1 enable checks
or pipeline behavior are modeled in that local callback fixture.

## Verification

```sh
python3 -m tools.experiments.audit_init_storage_literals --block-local
python3 -m unittest tools.tests.test_init_storage_literals tools.tests.test_init_allocator_guest_free tools.tests.test_init_exception_storage tools.tests.test_init_syscall_fault_route -v
make tools-check
git diff --check
```

All 34 focused tests pass in 6.906 seconds. Project tool and whitespace checks
pass. New scanner tests cover scheduled pairs/copies, pointer-load invalidation,
call delay-slot boundaries, incoming branch targets, unknown opcodes, ADDI
overflow and retail pointer/context writers.

## Next Work

Resolve loaded-pointer/loop writers and diagnostic-enabled storage effects at
the identified sites. Complete stack/workspace ownership remains unproven;
decoder fitting remains 896 bytes over retail. No production C/assembly,
decoder/adapter, README aggregate or unrelated Game changes. Prior Init
inventory stays unchanged.
