# Init Byte-Packed Header Load And Unaligned Core Qualification

Date: 2026-10-03. Baseline: `ed98184`.

## Result

Opt-in `--packed-header` selects an IDO byte-packed four-byte header field
instead of assembling the opening word from four volatile byte loads.
The guest load remains volatile. Both IDO profiles accept `#pragma pack(1)`
and its reset without warnings; the emitted header size/alignment receipt
is `(4, 1)`. All six guest builds emit `LWL` at offset zero and `LWR` at
offset three through the same base/target registers, not an aligned `LW`.

Packed O2 core text shrinks from 4,512 to 4,480 bytes. Including the unchanged
320-byte adapter, best linked text is now 4,800 bytes, leaving 816 above the
3,984-byte retail group (previously 848). All six linked images shrink by
32 bytes without increasing stack bounds. This is experimental fitting,
not a production assembly conversion.

The packed O2 core body/slot is 52/52 words, down from 60/60. It now equals
the retail core slot's word count, but its ABI, instructions and connected
helper/adapter interface are not a byte-exact replacement. O1 core body/slot
is 81/84, versus the prior 89/92. No individual slot promotion is inferred.

## Implementation And Guard

The packed type and alignment probe are conditional. The original byte-load
expression remains the default and also remains the native fallback even
when the option is selected. This checkpoint qualifies the guest packed load,
not a native packed-word endian interpretation.

The isolated object inspector reads the exported two-word header layout
receipt with its existing structured ELF parser. A present receipt other
than `(4, 1)` is rejected, and selecting the flag requires that receipt to
exist. This prevents silently accepting ignored packing as a potentially
unaligned `LW`. Existing entry/frame/state layout checks remain active.
A negative test simulates a four-byte-aligned receipt and confirms rejection.

The loop/shift helpers were inspected but not changed. Modulo-32 shift
behavior, four-byte logical header coverage, the 0x1172 two-byte versus other
four-byte header skip, limit calculations and FPR shadow behavior remain.

Ignored measurements/objects/logs live under
`conker/build/init-packed-header-20261003`; a fresh omitted-flag check under
`init-packed-header-default-check-20261003` reports the previous packed
4512/408 O2 and 5952/344 O1 text/frame values, without header metadata.
That is a size/layout receipt, not a new default full-corpus run.

## Qualified Costs

All final images retain 116-byte state and a 320-byte adapter:

| Shape/profile | Linked text | Static total bound | Observed descent |
| --- | ---: | ---: | ---: |
| Frame O2/g3 | 6,048 | 3,280 | 3,280 |
| Frame O1 | 6,432 | 3,200 | 3,200 |
| Aligned/end O2/g3 | 4,832 | 3,240 | 3,240 |
| Aligned/end O1 | 6,224 | 3,176 | 3,176 |
| Packed/remaining O2/g3 | 4,800 | 3,256 | 3,256 |
| Packed/remaining O1 | 6,240 | 3,192 | 3,192 |

Packed core-only bounds remain 408/O2 and 344/O1. O2 minimum SP remains
`0x80031D58`, 72 bytes above the known protected neighbor. Complete
reservation ownership and real hardware fault behavior remain unproven.

## Verification

The inherited domain passes 432 stream/context comparisons, 114 direct
builder comparisons and six exact initializer comparisons. It retains the
constructed active byte-rewind gate (11 bits, one byte, three remaining),
nested lookup gate, malformed cases and saved-context/physical scratch guards.

Additional packed-header tests verify:

- `(4, 1)` header layout and the actual unaligned load pair in all six builds.
- Primitive pair execution at all four offsets, starting with a stale target
  register; merged value is 0x1172AABB and the logical read-byte union is
  exactly the four header bytes. This is oracle byte coverage, not a claim
  about bus transactions or hardware page/fault behavior.
- Both two-byte and four-byte header formats at all four input alignments
  across six builds: 48 direct compiled-core/retail comparisons. Return,
  output, all ten base state words, physical scratch and saved registers match.
  The private direct fixture permits the measured 116-byte shadow state;
  these are direct C-core calls, not 48 additional exception-wrapper runs.
- Invalid alignment metadata is rejected by the inspector.

Terminal commands:

```powershell
wsl python3 -m unittest tools.tests.test_init_decompressor_packed_header
wsl python3 -m unittest tools.tests.test_init_decompressor_packed_header.InitDecompressorPackedHeaderTests.test_nonpacked_header_layout_is_rejected
wsl python3 -m unittest tools.tests.test_init_decompressor_guest_calls
wsl python3 -m unittest tools.tests.test_init_decompressor_slot_ledger
```

The first run loaded before the negative metadata test was added: 21 tests
in 199.762 seconds, 20 pass and one intentional corpus skip. The added test
passes separately in 2.207 seconds. Six call-analysis and seven slot-ledger
tests also pass. Combined: 34 pass, one skip. Compile/link logs are empty;
root `make tools-check` and `git diff --check` pass.

No production build, ordinary full-suite, changed full corpus, hardware replay
or sibling-port test is claimed. The earlier default/histogram corpus receipts
are not reassigned to this packed-header variant.

## Next

- [x] Confirm IDO packed layout and actual unaligned loads before retaining.
- [x] Reduce all six linked images by 32 bytes with unchanged stack bounds.
- [x] Qualify both header formats/all alignments and reject ignored packing.
- [ ] Continue fitting: 816 linked bytes remain above retail capacity.
- [ ] Full changed corpus in both masked CU1 modes before promotion.
- [ ] Other-profile corpus and remaining ownership/hardware/resume gates.

The opt-in corpus class is `InitDecompressorPackedHeaderCorpusTests` in
`tools.tests.test_init_decompressor_packed_header`, with the existing corpus
environment selectors. It was not run here. Production Init, adapter assembly,
default flags and README aggregates remain unchanged. Unrelated Game edits
are preserved and excluded from this checkpoint. Nothing is pushed.
