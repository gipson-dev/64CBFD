# Init Resume Conversion Readiness And Repeatable Audit

Date: 2026-10-04. Starting HEAD: `b6eefb75`.

## Verdict

**Some remaining Init assembly can be expressed in C, but none of the retained
replacements is currently ready to adopt.** Do not replace exact assembly with
a placeholder or count an isolated, oversized semantic experiment as a finished
conversion. The remaining work is custom assembly rewriting and interface
qualification, not another ordinary original-C restoration batch.

Init currently has **492 / 539 C functions (91.28%)**, covering
**151,796 / 164,048 bytes (92.53%)**. The remaining **47 assembly entries occupy
12,252 bytes**. The existing linked code and data, including every remaining
assembly slot, match raw retail bytes. These are separate measures: exact
restoration does not require changing intentional assembly into C.

The complete per-function map remains in
[Note 947](947-init-remaining-assembly-conversion-map-20261004.md).
This resume adds fresh verification and a reusable inventory/ownership audit,
without changing production Init source, profiles or instruction guards.

## Conversion Queue

| Group | Entries | Bytes | Current decision |
| --- | ---: | ---: | --- |
| Small leaves | 2 | 120 | C candidates, neither fitted/matched for adoption |
| Connected decoder | 10 | 3,984 | Semantic C exists; whole-chain fitting and ownership remain open |
| Cleanup/diagnostic/glyph path | 5 | 1,308 | Connected recovery; do not substitute a leaf without its calling contract |
| Boot, hardware/context and retained SDK assembly | 30 | 6,840 | Keep the established original assembly owners |
| Total | 47 | 12,252 | No new production conversion |

The last group includes the two SDK queue leaves: their algorithms are
C-expressible, but their original register interfaces and SDK provenance are
reasons to retain them. This is a conversion-policy decision, not a claim that
all thirty algorithms are impossible in C. Likewise, the five diagnostic
entries are a connected investigation group, not five independently qualified
C replacements.

### 1. Bitmap Leaf: First Small Target

`func_10005BE0`: 76 bytes / nineteen words, owned by `asm/init_5AB0.s`.

Preserve inclusive endpoint filling, captured start/end pointers, the signed
count reload after filling, partial-byte masking, alias timing and the original
endpoint branch with increment delay slot. The latest equality-exit forms
compile to **21 O2 words**, not nineteen; other retained unsigned/exit-edge
forms also fail fitting. Fresh tests rerun those controls rather than adopt them.
See [Note 948](948-init-bitmap-equality-exit-lifetime-trials-20261004.md).

Next implementation step: formulate a genuinely new compiler/control-flow
shape that can remove the extra loop/return instructions while preserving
alias-sensitive observations. Do not repeat the rejected forms unchanged.
Only proceed to ownership replacement once the full nineteen-word slot is
qualified; a shorter host loop alone is insufficient.

### 2. MMIO Leaf: Second Small Target

`func_100038E0`: 44 bytes / eleven words, retained through
`src/init_38E0.c`'s `GLOBAL_ASM` owner.

Required external trace, with exact access widths and ordering:

1. Publish word `0xBC000C02` to `0x80038070`.
2. Publish halfword `0x4040` to `0x80038074`.
3. Write halfword `0x4040` to `0xBC000C02`.

All three assembly tests freshly pass, including reassembly and raw linked-byte
comparison. Existing C trials do not reproduce the complete eleven words;
the published-address trial's O1 result still has an extra address copy and a
different return-delay schedule. That is prior compiler evidence from
[Note 885](885-init-mmio-published-address-dataflow-trial-20261004.md), not a
newly repeated C compilation. Next work needs a justified address-lifetime or
scheduling hypothesis. Do not invent a return value to force `$v0`.

### 3. Decoder: Largest Connected Opportunity

Retain the qualified packed-remaining, pointer-owned, distance-operation-local
candidate and its 176-byte adapter. The freshly compiled O2 complete linked image is
**4,512 executable bytes against 3,984 retail: 528 bytes too large**.
Its shared registers, inherited stack state, entry wrappers and private-stack
reservation must be qualified together; ten ordinary helper substitutions
would not preserve the existing calling contract.

Historical full masked CU1-clear/set corpora for this candidate are recorded in
[Note 912](912-init-distance-operation-o2-full-masked-cu1-clear-corpus-20261004.md)
and [Note 913](913-init-distance-operation-o2-full-masked-cu1-set-corpus-20261004.md).
All six recorded candidate/tool/test SHA-256 hashes still match those notes.
The corpora are prior evidence, not full-corpus reruns in this resume. After a candidate
change, refresh both corpora and prove reservation/placement ownership before
adoption. Known-neighbor clearance alone is not stack ownership.

### 4. Glyph/Formatter: Fit The Complete Calling Path

The C writer's **29-word body** fits the original thirty-word leaf body, but
it does not solve the complete path. Fresh formatter compilations still show:

| O2/no-unroll shape | Allocated text | Observed stack descent |
| --- | ---: | ---: |
| Separate setup | 624 bytes | 48 bytes |
| Shared setup | 608 bytes | 80 bytes |
| Split setup | 624 bytes | 64 bytes |

The connected retail text budget is **412 bytes**. The experimental address
`0x10009000` overlaps the existing `func_10008F90` owner, and the diagnostic
caller has two different stack regimes. Preserve interior entry and inherited
register contracts. Resolve text, placement and stack ownership together before
counting a conversion. See
[Note 933](933-init-glyph-adapter-production-placement-and-stack-boundaries-20261004.md).

## Fresh Verification

New `tools/tests/test_init_remaining_assembly.py` adds seven checks:
complete contiguous CSV inventory, disjoint/exhaustive decision groups,
checksum-verified ROM, every active assembly source owner and recorded word,
all retained raw linked slots/full Init code, Init data, and complete Game data.
It uses the existing ELF/parser utilities and skips artifact checks explicitly
when no linked ELF exists. It does not build or qualify replacement C.

This checkout passes all seven checks with no skips. The separately rerun
Init contract/compiler suite passes **78 tests in 58.677 seconds, no skips**.
Each of the three bitmap suites records 1,002 completed model pairs and twelve
bounded prefixes. These are bounded model/compiler checks, not hardware or
guest gameplay acceptance.

The retained decoder class also freshly passes **46 tests in 319.476 seconds,
no skips**. It recompiles all six shape/profile adapter images, exercises bounded
guest/model contracts and confirms the best packed O2 image at 4,512 bytes with
3,248-byte static/observed descent. The seven new audit tests take 0.800 seconds.
Across these three separate invocations, **131 tests pass, no skips**.
The full 507-page CU1 corpora were not rerun. Project tool checks, document
links and whitespace checks pass.

| Existing linked section | Bytes | Different bytes |
| --- | ---: | ---: |
| Init code | 164,048 | 0 |
| Init data | 17,376 | 0 |
| Game data, 720 owners | 189,088 | 0 |

```sh
python3 -m unittest tools.tests.test_init_remaining_assembly -v -f
python3 -m unittest tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
python3 -m unittest tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests -q -f
```

## Resume Boundary

- [x] Recount and resolve all 47 remaining assembly entries.
- [x] Verify existing raw Init code/data and Game data against pristine retail.
- [x] Rerun bitmap, MMIO and connected formatter/compiler controls.
- [x] Recompile/test the retained decoder and confirm its 528-byte fitting excess.
- [x] Add a repeatable retained-ownership and artifact audit.
- [ ] Fit and qualify a genuinely new bitmap or MMIO C shape.
- [ ] Resolve whole-decoder size/reservation/entry ownership.
- [ ] Resolve connected glyph text/placement/stack ownership.
- [ ] Adopt only after full-slot/contract proof and a production relink.

The pending Note 950 Game emitter source/test/documentation remains preserved;
this assessment does not commit or requalify it. README aggregates are already
correct and unchanged. No production rebuild, ROM promotion, sibling/Release
change, hardware/gameplay qualification or push is claimed.
