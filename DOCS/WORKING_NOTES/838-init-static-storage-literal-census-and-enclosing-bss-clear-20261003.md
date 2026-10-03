# Init Static Storage Literal Census and Enclosing BSS Clear

Date: 2026-10-03

## Scope

Follow-up to [Note 837](837-init-syscall-fault-dispatch-and-disabled-diagnostics-route-20261003.md).
Begin the static reservation-writer audit with reproducible retail address
evidence rather than treating observed untouched gaps as owned buffers.

Add `tools/experiments/audit_init_storage_literals.py` and seven focused tests.
The census decodes adjacent LUI plus ADDI/ADDIU/ORI or ordinary load/store
address pairs for interval `[0x80031AE0, 0x80035504)`. It reports instruction
PCs, words, candidate address, direction and access width. It deliberately
does not infer object capacities or ownership from symbol spacing.

## Provenance and Limits

- Validate original US ROM SHA1 before auditing.
- Init text: original ROM `[0x1000, 0x290D0)`, address base `0x10001000`.
- Game text: independently decompressed retail pages, base `0x15000000`,
  length `0x1FA130`.
- Debugger text: raw ROM `[0x19EA88, 0x1A2178)`, base `0x16000000`,
  length `0x36F0`, matching the text/rodata boundary in the project YAML.

This is a literal-pair candidate census, not a control-flow disassembler or
whole-program memory proof. It misses scheduled-apart pairs, register copies,
computed/indexed addresses, pointer-loaded accesses, DMA, aliases and bulk
clears. It excludes unaligned left/right operations rather than assigning
them misleading fixed write footprints. A word pattern in text is not alone
proof that the instruction executes. Zero candidates in a section do not
establish zero references or writers.

## Measured Candidates

| Section | Use PC | Kind | Address |
| --- | --- | --- | --- |
| Init | `0x1000131C` | materialize | `0x80033330` |
| Init | `0x100013A0` | materialize | `0x800354FC` |
| Init | `0x10005D38` | load | `0x800354FC` |
| Init | `0x10005D80` | load | `0x800354F8` |
| Init | `0x10005DF0` | load | `0x800354F8` |
| Init | `0x10005E20` | materialize | `0x80032B18` |
| Init | `0x10005EA8` | load | `0x800354F8` |
| Init | `0x10005F28` | materialize | `0x800340E8` |
| Init | `0x10006014` | materialize | `0x80032B18` |
| Debugger | `0x16000D50` | materialize | `0x80031AE0` |

Counts: Init 9, Game 0, Debugger 1. No adjacent literal-store pair is found in
this interval. That does not exclude stores: the existing wrapper writes the
saved SP through a materialized pointer, and startup pointer publications use
scheduled-apart instructions. Those are concrete known coverage gaps.

## Enclosing Clear

The startup test pins eight original words at `0x10001050..0x1000106C` and
executes argument preparation including the JAL delay instruction. The clear
call receives base `0x8002D4B0`, size `0x16690`, end `0x80043B40`, covering
the entire audited interval. It does not execute the clear callee or declare
individual decoder reservations.

`conker/conker.us.yaml` has enclosing `bss_size: 0x16690` and comments retaining
uncertainty about BSS boundaries. `undefined_syms_auto.txt` assigns fixed
addresses for the thread, context top, table, input and workspace; these
assignments provide addresses, not sizes. No individual capacity is inferred.

## Verification and Next Work

```sh
python3 -m tools.experiments.audit_init_storage_literals
python3 -m unittest tools.tests.test_init_storage_literals tools.tests.test_init_exception_storage tools.tests.test_init_syscall_fault_route -v
make tools-check
git diff --check
```

All 17 focused tests pass in 1.761 seconds; project tool and whitespace checks
pass. Synthetic tests cover signed lows, destination/base distinction, boundary
crossing, excluded pairs, alignment validation and wrong ROM rejection.

Next resolve scheduled-apart address pairs and indexed/pointer-based writers
at the identified call sites. Complete reservation ownership remains open;
do not enlarge the experimental decoder's buffers from this census. Decoder
fitting still exceeds retail by 896 bytes. No production, decoder/adapter,
README aggregate or unrelated Game changes; prior Init inventory unchanged.
