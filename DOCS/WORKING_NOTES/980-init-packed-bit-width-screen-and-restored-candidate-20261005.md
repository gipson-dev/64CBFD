# Init Packed Bit-Width Screen And Restored Candidate

Date: 2026-10-05. Starting HEAD: `dded248c`.

## Scope

Continue the connected decoder's 512-byte fitting gap after
[Note 979](979-init-byte-depth-full-masked-cu1-corpus-qualification-20261005.md)
qualified the banked byte-depth packed O2/g3 image across both full masked
CU1 corpora. This turn screens a different local-lifetime hypothesis before
semantic qualification. No production owner, compiler default or guard changes.

The packed builder currently declares `uint8_t entryOperation, entryBits`.
Widening the bit-count accumulator might remove intermediate byte narrowing
before its guest `<< 16` packing. Unlike the earlier operation-only experiment
in [Note 895](895-init-builder-wide-operation-and-header-packing-trials-20261004.md),
the first trial changes only `entryBits`; the second measures both fields
together on the current byte-depth candidate.

## Temporary Forms

1. Control: retain the banked source and both byte locals.
2. Wide bits: `uint8_t entryOperation; uint32_t entryBits;`. Keep the guest
   packing expression unchanged. Explicitly cast `entryBits` back to `uint8_t`
   in the little-endian native packing expression before shifting by eight.
3. Wide both: `uint32_t entryOperation, entryBits;`. Keep guest packing unchanged;
   explicitly narrow both fields in little-endian native packing.

These are temporary source screens, not retained selectors. The native casts
preserve the written byte-packing shape; they do not constitute execution proof
for either changed candidate. No range/equivalence claim is made for removing
guest bit-count narrowing. Reject both on text/stack costs before semantic tests.
The initially considered parent-width expression is not changed or tested.

Compile each form with the established packed-remaining shape, ABI FPR shadow
and `InitDecompressorBuilderByteLevelTests.shadow_extra_flags`. The shape flags
are read from the literal `shapes` assignment in the existing guest-builder
setup using Python AST, without executing its six-image setup. All remaining
options are inherited unchanged, including the byte-depth selector.

```text
--frame-backed --packed-entry --bounded-builder-shifts --no-unroll
--bounded-length-scan --dynamic-cursor --cache-builder counts-offsets
--builder-symbol-cursor remaining --abi-fpr-shadow
+ InitDecompressorBuilderByteLevelTests.shadow_extra_flags
```

Invoke `tools/experiments/compile_init_decompressor.py --output <form-directory>`
with those flags for each source form. Three forms produce six fresh objects,
O2/g3 and O1 each, all with empty compiler logs. Measurements, objects and
disassembly remain ignored under
`conker/build/init-packed-width-screen-20261005/{control,wide-bits,wide-both}/`.

## Measurements

Units are bytes except the public/region word counts. Executable totals add
the unchanged actual 176-byte adapter measured and executed in Note 979;
this size screen does not assemble or execute a new adapter.

| Form / profile | C / executable | Builder public / region words | Builder frame / core call bound |
| --- | ---: | ---: | ---: |
| Control O2/g3 | 4320 / 4496 | 330 / 398 | 200 / 400 |
| Wide bits O2/g3 | 4320 / 4496 | 329 / 397 | 208 / 408 |
| Wide both O2/g3 | 4320 / 4496 | 327 / 395 | 208 / 408 |
| Control O1 | 5792 / 5968 | 484 / 556 | 120 / 360 |
| Wide bits O1 | 5792 / 5968 | 484 / 556 | 128 / 368 |
| Wide both O1 | 5792 / 5968 | 484 / 556 | 128 / 368 |

Optimized public builder savings are one and three words, but complete object
text stays 4320 bytes. The last `init_decode_core` body stays fifty words;
its measured slot grows from fifty to fifty-one or fifty-three words, accounting
for trailing alignment. Other named regions keep their measured lengths.
O1 saves no body words. Both profiles gain eight bytes of builder frame and
conservative direct-call bound. No total-stack measurement is claimed for
these unexecuted trials.

The fresh control instruction hashes match the qualified candidate:

```text
O2 dce986104060637a90746c3c16c711b2bd792ee835c699c87a13904fb173082a
O1 fff009d0196e62e0cbf661ac1398edf62d02c8943a8032171889b02999567394
```

## Restoration And Verification

Remove both temporary forms with scoped source edits. The semantic candidate
and compiler driver have no diff from starting HEAD. The byte-depth lead,
adapter, flags, guard engine and full-corpus result from Note 979 stay intact.
The changed width images receive no semantic, malformed-input, corpus,
hardware or adoption credit.

**All 83 fresh restored connected/native/inventory/slot/call/reporting checks
pass in 345.010 seconds, exit zero, no skips.** They freshly compile the six
connected shapes/profiles, execute the actual adapters, qualify ordered physical
depth-table publications and check both byte-depth and disabled-option hashes.
Packed O2 remains 4496 executable bytes and 3248 conservative/observed total
descent; packed O1 remains 5968 and 3208. The independent inventory audit checks
all 47 existing Init ASM owners/raw slots, complete existing Init code/data and
Game data against checksum-validated retail. This is not a production relink.

These are 83 rerun existing checks, not newly added tests. No test or candidate
code is retained from the rejected width screens. Project tool, whitespace
and scoped note-link checks also pass.

```sh
python3 -m unittest tools.tests.test_init_decompressor_builder_byte_level tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_guest_calls tools.tests.test_init_decompressor_builder_byte_level_corpus_selection -q -f
make tools-check
```

## Decision And Next

- [x] Screen the bit-count width and both-field interaction on the byte-depth lead.
- [x] Reject whole-text-neutral, stack-growing forms and restore the banked source.
- [x] Verify the fresh restored connected/owner/slot/call/reporting suite.
- [ ] Remove 512 complete executable bytes with a different builder/shared-call lifetime hypothesis.
- [ ] Prove original entry/frame/placement, private-stack reservation and hardware gates.

Init remains 492 C / 47 ASM owners: seventeen investigation targets and thirty
intentional boot/SDK/hardware/context routines. No newly adopted conversion,
production relink, README aggregate change, host source/build, frozen Release,
save change, ROM promotion or push. The full corpus is not repeated for a
discarded source screen; unchanged banked image identities retain Note 979's
candidate-specific evidence.
