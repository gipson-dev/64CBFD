# Init Pause-Resume Conversion Decision

Date: 2026-10-04. Starting HEAD: `6b5593d7`.

## Answer

Some remaining Init assembly can be expressed in C, but **none of the
remaining replacements is currently qualified for production adoption**.
The best small matching target is still `func_10005BE0`, followed by
`func_100038E0`. The decoder and glyph/formatter paths already have semantic
C experiments; their outstanding work is fitting and interface/ownership
qualification, not starting another recovery from scratch.

This assessment resumes the requested Init work. It does not continue the
unfinished Game-data linker repair or count experiments as conversions.

## Fresh Inventory

Structured inspection of `conker/progress.init.csv` confirms:

| Representation | Functions | Bytes |
| --- | ---: | ---: |
| C | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) |
| Assembly | 47 | 12,252 |

All 47 assembly names were checked against actual source owners: `GLOBAL_ASM`
wrappers or directly selected assembly inputs in `conker/conker.ld`.
The monolithic `init_5AB0.s`, standalone SDK inputs and wrapped inputs are
accounted for; CSV filename labels are not treated as source paths.

| Remaining group | Functions | Bytes | Conversion decision |
| --- | ---: | ---: | --- |
| Bitmap `func_10005BE0` | 1 | 76 | Ordinary-C candidate; full nineteen-word match unresolved |
| MMIO `func_100038E0` | 1 | 44 | Ordered volatile-C candidate; full eleven-word match unresolved |
| Connected decoder | 10 | 3,984 | Semantic C exists; linked-size and production ownership gates open |
| Cleanup/debug/glyph | 5 | 1,308 | Connected C trials exist for part of the group; nonstandard interfaces remain |
| SDK thread queue leaves | 2 | 96 | Algorithms are C-expressible, but original handwritten SDK owners are intentional |
| Hardware/context/setup | 8 | 4,376 | Privileged/context contracts require assembly or supported intrinsics |
| Separated SDK assembly | 19 | 2,288 | Retain original machine-level implementations |
| Boot entry | 1 | 80 | Retain handwritten clear-and-jump entry |
| Total | 47 | 12,252 | No newly achieved conversion |

Complete names and grouping are in
[Note 735](735-init-retained-assembly-reassessment-20261002.md), whose
48-row baseline predates the completed `func_10001420` memory-clear conversion.
The current table above excludes that finished routine.

## Candidate Gates

1. **Bitmap:** [Note 927](927-init-bitmap-unsigned-range-comparison-trials-20261004.md)
   records the latest rejected source shapes. O2 controls and unsigned-range
   variants emit twenty words against nineteen retail. The next trial needs
   a new explanation for the direct endpoint branch and increment delay slot.
   Preserve the inclusive fill, pointer snapshots, post-fill count reload,
   partial-byte mask and alias timing. Repeating existing qualifier, sentinel,
   explicit-return or unsigned-range shapes unchanged is not new progress.
2. **MMIO:** preserve address publication to `0x80038070`, halfword publication
   to `0x80038074`, then the halfword store through `0xBC000C02`, all in that
   order. The eleven-word register lifetime/schedule remains unmatched.
   Host tracing is not hardware acceptance; broad instruction guards are not
   a substitute for the recovered body.
3. **Decoder:** the latest qualified candidate from
   [Note 911](911-init-distance-operation-local-fitting-20261004.md) is
   **4,512 linked executable bytes versus 3,984 retail: 528 bytes excess**.
   This supersedes older 544/592-byte deficits. Shared-frame entries cannot
   be promoted independently. Reduce the complete linked footprint, requalify
   both guarded CU1 corpora, then prove complete reservation, production
   entry/frame ownership and required hardware/context behavior. Existing
   corpus receipts in Notes 912/913 were not rerun in this assessment.
4. **Glyph/formatters:** fresh compiled/linked fixtures reproduce the retained
   O2 controls: independent setup **624 bytes / 48 stack**, fully shared
   **608 / 80**, split validation **624 / 64**. The connected retail budget is
   412 bytes. The 29-word writer body fits its own 30-word retail slot, but
   that alone does not qualify the connected adapter, formatter text or stack
   ownership. Keep the nonstandard register/interior-entry contracts from
   Notes 928-936; do not promote based only on semantic test success.

## Pick Up Here

- [x] Recount the current Init inventory and verify all 47 assembly owners.
- [x] Rerun retained small-leaf, allocation, decoder-storage/startup and
  connected glyph/formatter qualification tests.
- [x] Independently compare preserved baseline Init code/data with retail.
- [ ] Develop a new isolated bitmap compiler-shape trial, using the characterized
  retail contract rather than narrowing it to convenient valid inputs.
- [ ] Require a complete nineteen-word match and contract tests before changing
  the bitmap owner inside `init_5AB0.s`; preserve the following exception entry
  `func_10005C2C` at `0x10005C2C`.
- [ ] Revisit MMIO only with a new address-lifetime/scheduling hypothesis.
- [ ] Continue decoder or connected glyph fitting only with a new measurable
  improvement, then requalify changed code and resolve ownership gates.
- [ ] After an actual owner transition, restore a successful full link,
  regenerate progress and compare complete Init code/data before updating
  README aggregate tables.

If both small leaves succeed, the conditional result is 494 / 539 C functions
(91.65%) and 151,916 / 164,048 C bytes (92.60%), leaving 45 assembly routines
/ 12,132 bytes. These are targets, not achieved totals. A faithful finished
Init need not force original boot, hardware or SDK assembly into artificial C.

## Fresh Evidence And Build Boundary

```sh
python3 -m unittest tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
```

**54 tests pass in 51.279 seconds, no skips.** The formatter suite recompiles
and links all six isolated profiles and executes their bounded paired fixtures.
These are focused model/guest-fixture checks, not real-hardware or gameplay
acceptance and not a fresh full decoder corpus run.

An independent ELF32 big-endian section parser compares
`conker/build/game-data-before-6b5593d7.elf` against YAML-bounded pristine ROM
bytes, without normalization:

| Preserved ELF section | Address | Bytes | Different bytes |
| --- | --- | ---: | ---: |
| `.init` | `0x10001000` | 164,048 | 0 |
| `.init_data` | `0x800290D0` | 17,376 | 0 |

This proves the **preserved pre-edit artifact**, not a fresh production build.
The sole starting dirty file is `tools/patch_generated_slice_ld.py`, containing
an unfinished Game-data owner-order repair. Its preceding link stopped when
the `0x236578` owner's assembler padding exceeded its retail span; the current
`conker/build/conker.us.elf` is absent. Preserve that edit and its saved ELF/map.
Complete or explicitly isolate that repair before claiming a current successful
production link. Do not silently discard it to make this assessment build.

Only working documentation changes in this assessment. Production Init source,
profiles, word guards and README aggregates remain unchanged. No new conversion,
commit, push, sibling build, Release change or guest execution is claimed.
