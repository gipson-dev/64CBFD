# Init Tight Adapter Return Scheduling And Alignment

Date: 2026-10-04. Starting HEAD: `e23ebaf9`.

## Opt-In Adapter

`INIT_DECODE_TIGHT_ADAPTER=1` requires ABI FPR shadow and a callee-preserving
core. It emits the adapter in `.text.init_decode_adapter` with four-byte
alignment, rather than the default sixteen-byte-padded input `.text` section.
GNU ld merges this executable subsection into linked `.text`.

The snapshot branch delay slot loads the saved return address from
`SP + 0xA80 + ADAPTER_EXTRA` (`lw ra,0xB18(sp)` for shadow mode), replacing
the nop. At return, one adjustment of `0xA88 + ADAPTER_EXTRA` (`0xB20`)
replaces the separate extra-frame and retail-frame adjustments. No frame
allocation, physical callee save, state store or FPR load is removed/reordered.
Core return is still checked before the adapter touches its saved RA.

This is experimental glue around the semantic C core, not an additional C
owner transition or proof of production slot ownership.

## Measurements And Layout Caveat

The adapter body and executable input section are 184 bytes, down from 192.
Packed scan-deficit O2 linked executable text is 4,568; O1 is 5,976. Core
text remains 4,384 / 5,792, and stack allocation is unchanged.

The isolated O2 linker receipt has `.text` size `0x11D8` at `0x10400000`,
then `.rodata` at `0x104011E0`. An eight-byte non-executable alignment gap
absorbs the removed words before the aligned rodata. Thus this is eight bytes
less executable text, NOT a demonstrated eight-byte whole code/rodata or ROM
footprint saving. Original production fitting/ownership remains unproven.
Do not count the old default's 592-byte excess as solved; even executable-only
accounting for this option is still 584 bytes over the 3,984-byte region.

Ignored artifacts:

- `conker/build/init-tight-adapter-trial-20261004.o`
- `conker/build/init-tight-adapter-o2-trial-20261004.elf`
- `conker/build/init-tight-default-{prior,current}-20261004.{o,bin}`

Default assembly without the symbol matches the prior committed adapter's
complete extracted `.text` exactly, 192 bytes. Prior revision source is fed
directly from Git to the assembler; no production source is replaced.

## Tests

The new subclass inherits the scan-deficit live-SP/callee/direct-FPR bounded
suite. It asserts adapter body size, packed linked sizes, unchanged bounds,
the unique snapshot branch's RA-load delay word, and the combined final SP
adjustment. Existing direct-FPR tests retain the exact original ordered loads.

A separate dependency test rejects missing shadow and missing callee-preserving
selection, passing in 2.344 seconds. It was added after the whole bounded
process imported the module, so it is reported separately.

Whole bounded run: 42 tests in 279.485 seconds, 41 passes and one deliberate
full-corpus skip. With the separately executed dependency test, forty-two
bounded tests pass. Source/adapter flags stayed fixed during the run.

| Shape/profile | Executable text | Static / observed descent |
| --- | ---: | ---: |
| Frame O2/g3 | 5,560 | 3,256 / 3,256 |
| Frame O1 | 5,992 | 3,176 / 3,176 |
| Aligned end O2/g3 | 4,600 | 3,232 / 3,232 |
| Aligned end O1 | 5,976 | 3,192 / 3,192 |
| Packed remaining O2/g3 | 4,568 | 3,240 / 3,240 |
| Packed remaining O1 | 5,976 | 3,200 / 3,200 |

All executable sizes are eight below the corresponding scan-deficit fixture
with the default adapter. Full changed-adapter corpora, hardware exception
timing and complete reservation remain open. Project tool and whitespace
checks pass; no production build, ROM or sibling-port qualification claimed.

## Next

- [x] Measure body, executable section and linked alignment gap separately.
- [x] Preserve default assembly exactly and reject missing contracts.
- [x] Pass inherited bounded guest/ABI/live-SP suite and exact FPR load order.
- [ ] Full changed-adapter masked corpora before assigning all-page credit.
- [ ] Resolve actual production layout/capacity, reservation and hardware/context gates.

Semantic C source, production source, compiler defaults, word guards, README
totals, sibling-port artifacts and unrelated Game work are unchanged.
