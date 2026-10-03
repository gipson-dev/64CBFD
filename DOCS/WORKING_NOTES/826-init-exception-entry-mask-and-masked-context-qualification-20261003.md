# Init Exception Entry Mask And Masked Context Qualification

Date: 2026-10-03. Baseline: `37e4711`.

## Result And Scope

The original exception prelude saves incoming Status, then clears IE and EXL
with `Status & ~3`. The TLB-load-fault branch reaches `func_10005C2C` before
the IRQ-dispatch calls. New tests execute the actual five-word Status prefix,
pin the direct route to pristine ROM words, and qualify compiled shadow
contexts with the derived low bits clear.

This strengthens the normal-interrupt masking evidence for that entry path.
It is not an interrupt-controller/pipeline model, a complete exception-handler
replay, a hardware test, or a proof against synchronous/nested faults. Complete
storage ownership and fitting remain open. Production ownership, SDK headers
and README aggregates are unchanged; pending Game work is excluded.

## Original Status And Route Evidence

The prefix at `0x100071EC..0x100071FC` performs:

- MFC0 of incoming Status into k1.
- A word save to the temporary context at `0x118(k0)`.
- ADDIU of -4 into at, producing mask 0xFFFFFFFC.
- AND of k1 with that mask.
- MTC0 of masked k1 into Status.

The existing FR=1 architectural-value fixture executes those words for all
four incoming IE/EXL combinations, CU1 clear/set, and stored/dynamic payloads:
16 prefix-plus-wrapper runs. Every run preserves the original saved Status,
clears both low bits and keeps them clear through the decoding wrapper.
Other Status bits, including FR and CU1, survive the prefix.

The wrapper enables CU1 only when needed, and unconditionally restores its
saved temporary Status at `0x10005F88`. CU1-clear traces contain enable/restore;
CU1-set traces still contain the restore. An initial test expectation incorrectly
omitted that CU1-set write; source inspection corrected the expectation, and
the new module was rerun successfully. No implementation change was needed.

The route check pins Cause masking at `0x100073FC`, the comparison with 8,
and the BEQ at `0x10007404` targeting `0x10007708`. That target JALs
`func_10005C2C`; both branch/call delay slots are NOPs. The lowest-address
handler JAL/JALR is `0x100074A4`, after the taken TLBL classification branch.
No linked call appears before that classification.

Direct Status-write sites in the retained handler are only `0x100071FC`;
the decoder wrapper has only `0x10005ED4` and `0x10005F88`. All six fresh
compiled core/adapter images contain no MTC0 Status instruction. This is a
word/control-flow check, not a claim about arbitrary indirect callees or the
fatal/debugger route. The middle of the handler is not executed in the prefix
fixture, and CP0 Cause/TLB/MMIO operations are not newly emulated.

## Masked Compiled Contexts

Three vector cases (stored, dynamic success, repeat overflow) and retail
pages 0, 169 and 506 run in both CU1 modes on all six shadow profiles:
72 additional compiled context comparisons. The Status values are 0x0400FF00
and 0x2400FF00, not the earlier generic-entry values ending in 01.

Comparisons retain complete modeled register values/known-bit masks, Status
write traces, wrapper save/load addresses, pre-wrapper f0-f11, base state,
physical scratch and output/workspace checks. The corrected retail thread
neighbor guard at 0x80031D10 remains enabled; ROM reads stay within DMA spans.
The bounded shadow domain is now 420 comparisons (348 earlier plus 72 masked).
Code sizes and stack costs are unchanged; smallest text/descent remains
4,896/3,256, with 72 bytes above the known neighboring retail thread footprint.

## Explicit Corpus Context Selector

The opt-in corpus test now accepts `CONKER_INIT_SHADOW_CORPUS_CONTEXT`:

- `generic` (default): Status 0x2400FF01, preserving Note 825's command semantics.
- `exception-masked`: Status 0x2400FF00, matching the prefix-derived low bits.
- Unknown names fail instead of silently selecting another context.

The selected context and exact Status are printed before the corpus loop.
Selector tests cover both values and rejection; the masked sample comparisons
use this same selector. Ordinary discovery still skips the corpus.

Note 825's 507-page corrected-boundary result remains a generic-entry CU1-set
receipt for one profile. It is not relabeled as a masked-entry corpus or as
complete exception-handler execution. No new full corpus is claimed here.

```sh
CONKER_INIT_SHADOW_CORPUS=1 CONKER_INIT_SHADOW_CORPUS_CONTEXT=exception-masked CONKER_INIT_SHADOW_CORPUS_PROFILE=packed-remaining/o2g3 python3 -m unittest tools.tests.test_init_decompressor_shadow_corpus -v -f
```

Omit the profile selector for all six images; that full masked gate remains open.

## Verification

- Final combined mask/layout/shadow/default-adapter/provenance suite: all 29
  tests pass in 273.741 seconds. The six-test mask module adds 72 compiled
  masked comparisons and 16 original prefix-plus-wrapper executions.
- Fresh compiler/assembler/linker logs are empty; the route/prefix words match
  the locally present pristine ROM. No compiled Status-write sites are found.
- The ordinary corpus invocation still skips unless explicitly enabled.
- Root `make tools-check`, two Python syntax checks and `git diff --check` pass.
- No new full corpus, production build, all-project suite or hardware replay
  is claimed. Decoder and adapter implementation, costs and counts unchanged.

## Next

- [x] Execute the Status mask prefix and preserve the separately saved incoming SR.
- [x] Pin the direct TLBL route and its Status-write sites to original words.
- [x] Qualify masked vector/sample contexts across six profiles and both CU1 modes.
- [x] Keep corpus entry-context selection explicit and preserve historical defaults.
- [ ] Run full masked corpus and remaining profile/mode gates.
- [ ] Recover complete stack/state/workspace owners and synchronous-fault bounds.
- [ ] Reduce/fix fitting before changing production ownership.
