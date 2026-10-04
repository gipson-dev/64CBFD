# Init Resume: Linked Baseline And Conversion Shortlist

Date: 2026-10-04. Starting HEAD: `09c5743d`, clean tracked checkout.

## Decision

Some remaining Init assembly is C-expressible, but **no remaining replacement
is currently qualified for production adoption**. Start an Init-only fitting
experiment with `func_10005BE0`; use `func_100038E0` as the second small target.
The decoder and diagnostic/glyph paths are connected conversion projects,
not independent leaf replacements. Original SDK, boot and privileged/context
assembly should not be forced into C merely to increase representation counts.

This resumes the requested Init assessment, not the pending Game placeholder
`func_150E81A8`. Unlike the earlier assessment in
[Note 940](940-init-pause-resume-conversion-decision-20261004.md), the current
production ELF exists and its complete Init sections are verified below.
[Note 942](942-game-physical-data-order-and-literal-pool-restoration-20261004.md)
has already resolved the separate Game-data link gate.

## Current Inventory

Structured parsing of `conker/progress.init.csv` confirms 539 entries:

| Representation | Functions | Bytes |
| --- | ---: | ---: |
| C | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) |
| Assembly | 47 | 12,252 |

| Remaining group | Functions | Bytes | Decision |
| --- | ---: | ---: | --- |
| Bitmap `func_10005BE0` | 1 | 76 | Best small ordinary-C fitting target |
| MMIO `func_100038E0` | 1 | 44 | Ordered volatile-C fitting target |
| Connected decoder | 10 | 3,984 | Semantic candidate exists; fitting and ownership unresolved |
| Cleanup/debug/glyph machinery | 5 | 1,308 | Connected trials exist; nonstandard interfaces and placement unresolved |
| SDK thread queue leaves | 2 | 96 | C-expressible algorithms, intentional original SDK assembly owners |
| Hardware/context/setup | 8 | 4,376 | Retain privileged/context assembly contracts |
| Separated SDK assembly | 19 | 2,288 | Retain original machine-level implementations |
| Boot entry `func_10001000` | 1 | 80 | Retain handwritten clear-and-jump entry |
| Total | 47 | 12,252 | No new production conversion |

The full named grouping remains in
[Note 735](735-init-retained-assembly-reassessment-20261002.md); exclude its
already-finished `func_10001420` row. This run also checked the raw linked bytes
of each of the current 47 assembly slots against its retail address and length.

## Resume Order And Adoption Gates

1. **Bitmap `func_10005BE0`, nineteen words, no frame.** Recover the direct
   cursor/end branch with its increment delay slot. Preserve the inclusive
   fill, captured endpoints, signed count reload after filling and partial-byte
   mask. The latest freshly recompiled unsigned equality control is twenty
   words; countdown is twenty-two. Both are rejected, even though semantic
   fixtures pass. Do not repeat these source forms unchanged or overwrite
   the neighboring exception entry at `0x10005C2C`.
2. **MMIO `func_100038E0`, eleven words.** A new source-lifetime hypothesis
   must preserve the ordered four-byte publication of `0xBC000C02` to
   `0x80038070`, two-byte publication of `0x4040` to `0x80038074`, then the
   two-byte write to `0xBC000C02`. Exact widths, order and full-slot matching
   matter; host tracing does not prove hardware acceptance. Existing shapes
   are not production-ready.
3. **Connected decoder, ten assembly entries.** Continue the existing
   candidate from [Note 911](911-init-distance-operation-local-fitting-20261004.md),
   rather than reconstructing each shared-frame helper separately. Its last
   qualified linked footprint is 4,512 executable bytes against 3,984 retail,
   **528 bytes excess**. Reduce that complete footprint, rerun both guarded
   CU1 corpora for changed code, and prove reservation, entry/frame ownership
   and required hardware/context behavior before adoption. The full decoder
   corpora were not rerun in this assessment.
4. **Connected glyph/formatter path.** The 29-word C writer fits the 30-word
   leaf body, but this excludes adapter and caller costs. Fresh O2 connected
   controls are 624 bytes / 48 stack for independent setup, 608 / 80 fully
   shared, and 624 / 64 split validation, against 412 connected retail bytes.
   A smaller leaf alone does not resolve occupied placement, inherited stack
   or the interior-entry/register contracts. Keep this experimental.
5. **After an actual qualified conversion:** transition only its established
   source owner, preserve neighbors and addresses, link the production ELF,
   regenerate progress, then compare the complete Init code/data and repaired
   Game data. Only achieved aggregate changes belong in the README.

If both small leaves become qualified, the conditional target is 494 / 539 C
functions (91.65%) and 151,916 / 164,048 C bytes (92.60%), leaving 45 assembly
functions / 12,132 bytes. These are prospective numbers, not current progress.

## Fresh Verification

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
```

Make succeeds and reports the production ELF up to date; **this is not a fresh
relink**. The matcher is freshly run: Init 492 / 492 C entries exact, zero
drift; total 3,278 / 5,463 exact, Game 2,605 / 4,790, Debugger 181 / 181.
Existing duplicate-recipe warnings for `generated_12D630` remain unchanged.

An independent ELF32 big-endian section parser compares the current
`conker/build/conker.us.elf` with pristine ROM after validating the ROM SHA-1
against `conker.us.yaml`. No instruction or relocation normalization is used.

| Current production section | Address | Bytes | Different bytes |
| --- | --- | ---: | ---: |
| `.init` | `0x10001000` | 164,048 | 0 |
| `.init_data` | `0x800290D0` | 17,376 | 0 |

SHA-256 receipts:

```text
.init       34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf
.init_data  a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239
```

**62 tests pass in 55.168 seconds, no skips.** Bitmap trials are recompiled
and executed: 1,002 completed retail/C pairs and twelve bounded prefixes.
The formatter tests also freshly compile/link all six retained profiles.
These are bounded model/guest-fixture checks, not hardware or gameplay proof.
`make tools-check` and `git diff --check` also pass.

## Checkpoint

- [x] Refresh the current 492 C / 47 assembly inventory.
- [x] Verify current production Init code/data and all 47 assembly slots.
- [x] Rerun the small-leaf, storage/startup and connected formatter checks.
- [x] Separate C-expressible candidates from intentional assembly owners.
- [ ] Develop a new bitmap fitting hypothesis and qualify the full slot.
- [ ] Pursue MMIO only with a new scheduling/lifetime hypothesis.
- [ ] Resolve connected decoder/glyph fitting and ownership before adoption.

Only working documentation changes. Production source, compiler profiles,
word guards and README aggregate tables remain unchanged. No new conversion,
full decoder corpus run, hardware execution, sibling build, Release change,
compressed-ROM promotion or push is claimed.
