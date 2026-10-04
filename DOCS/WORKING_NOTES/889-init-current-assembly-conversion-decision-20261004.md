# Init Current Assembly Conversion Decision

Date: 2026-10-04. Starting HEAD: `92c0adca`.

## Decision

Some remaining Init routines can be expressed in C, but there is no additional
proven production replacement ready to adopt. Do not equate semantic recovery
with a byte-exact owner transition. Retain the current production assembly.

This refresh supersedes Note 801's decompressor next steps: frame mapping,
an isolated adapter and extensive guest differential qualification now exist.
Starting those steps again would repeat completed work. Fitting and production
ownership remain open.

## Fresh Inventory

Structured `Import-Csv conker/progress.init.csv` inspection confirms:

| Representation | Functions | Bytes |
| --- | ---: | ---: |
| C | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) |
| Assembly | 47 | 12,252 |

The current assembly names/lengths agree with the grouping in
[Note 792](792-init-resume-remaining-assembly-conversion-decision-20261003.md).

| Group | Functions | Bytes | Current disposition |
| --- | ---: | ---: | --- |
| Bitmap `func_10005BE0` | 1 | 76 | Ordinary C candidate; nineteen-word match unresolved |
| MMIO `func_100038E0` | 1 | 44 | Ordered volatile C candidate; eleven-word match unresolved |
| Connected decompressor | 10 | 3,984 | Experimental semantic C and adapter; too large to promote |
| Original separated SDK assembly | 19 | 2,288 | Retain original implementations |
| Boot entry | 1 | 80 | Retain clear-and-jump assembly contract |
| Hardware/context/setup | 8 | 4,376 | Privileged instructions and connected context contracts |
| SDK thread queue leaves | 2 | 96 | C-expressible algorithms, original assembly provenance |
| Cleanup/debug/glyph | 5 | 1,308 | Nonstandard interior entries and live-register/link interfaces |
| Total | 47 | 12,252 | No new production conversion |

## Where To Resume

1. Continue isolated decompressor fitting. The retained packed O2/g3 candidate
   has 4,384 core bytes plus a 192-byte adapter: 4,576 linked bytes against
   3,984 retail bytes, a 592-byte excess. Compare whole linked text and nested
   stack bounds, not just a smaller public function or raw unpadded body.
2. Require a genuinely new source hypothesis. Previous count-clear, stored-copy,
   limit-predicate, sort-cursor and cache variants are recorded in the working
   notes; unchanged rejected variants are not new progress. Keep discarded
   candidates isolated and restore the qualified source exactly.
3. Requalify any retained change with bounded semantic/ABI tests and both full
   guarded corpora. Notes 887/888 qualify the unchanged baseline across 507
   paired pages per masked CU1 mode, 1,014 total; they do not qualify new code.
4. Establish full private-stack reservation and entry/frame ownership, plus
   hardware/context behavior, before any production transition. Recorded depth
   3,240, minimum SP `0x80031D68`, and 88-byte known-neighbor clearance do not
   prove ownership of the complete reservation. Live-SP guards are write-only.
5. Revisit the bitmap or MMIO leaf only with a new compiler/dataflow explanation
   preserving full-slot control flow, access width/order, and neighbor addresses.
   The latest MMIO published-address trial in Note 885 still does not match.
6. After a successful ownership transition, rebuild/link, regenerate progress,
   compare complete Init code/data sections, and update README aggregate tables.
   Keep detailed updates in these docs, not the README.

## Verification Scope

Fresh focused execution:

```sh
python3 -m unittest tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries -v -f
```

All 33 tests pass in 1.929 seconds, no skips. These cover retained MMIO/bitmap
slots and behavior, conditional allocator contracts, decoder slot accounting,
and storage boundaries. They are bounded model/static tests, not hardware or
gameplay acceptance. Notes 887/888 are prior full-corpus evidence, not rerun here.
No production rebuild, compiler trial or new exact-match claim is made here.

Only working documentation changes. Production source, compiler profiles,
word guards, README totals, sibling-port artifacts and Release are unchanged.
Existing unrelated Game source/tests remain untouched and unstaged.
