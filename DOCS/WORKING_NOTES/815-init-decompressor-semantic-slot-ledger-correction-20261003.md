# Init Decompressor Semantic Slot Ledger Correction

Date: 2026-10-03. Baseline: `6e05ce4`.

Follow-up: [Note 816](816-init-builder-leaf-fill-and-bounded-length-scan-trials-20261003.md)
separates public call units from embedded helpers: the 413-word builder
symbol region below comprises 357 builder words and 56 lookup-helper words.
Region totals remain valid; they are not standalone function-body sizes.

## Result

The manual slot ledgers in Notes 812-813 swapped the dynamic and compressed
decoder roles. They also mislabeled the fixed decoder wrapper as a builder
wrapper. These documentation errors are corrected. The isolated semantic C
candidate, existing assembly fixtures and aggregate measurements were not
affected. Note 793 already recorded the correct roles.

The cursor-only packed/cached-builder O2 candidate's dynamic decoder is 220
words against 257 retail words, not 53 words over. The compressed decoder is
100 against 167, not 157 words spare. Builder remains 413 against 293, a
120-word overrun. The aggregate remains 4,208 versus 3,984 bytes, 224 over.
No production function conversion or README percentage change is claimed.

## Retail Evidence

- `func_10006424` builds dynamic code/literal/distance tables: three direct
  calls to `func_1000696C`, followed by a call to `func_10006E00`.
- `func_10006E00` decodes compressed literals/lengths/distances and copies
  back-references. It contains no direct JAL calls.
- `func_1000692C` calls `func_10006E00`, restores workspace state and forces
  zero return with final word `0x24020000`. It is the fixed decoder wrapper.
- Fixed setup `func_1000709C` contains 75 body words and two alignment NOPs
  before `func_100071D0`, so its available slot is 77 words.

The new tests check these call targets and the wrapper return instruction
against actual `init_5AB0.s` words, rather than duplicating narrative labels.

## Corrected Current Size Ledger

Cursor-only packed/bounded, no-unroll, builder counts/offsets cached, O2:

| Retail role / entry | Retail slot words | C slot words | C minus retail |
| --- | ---: | ---: | ---: |
| Core `func_1000625C` | 52 | 49 | -3 |
| Stream/dispatch `func_1000632C` + `func_10006380` | 62 | 78 | +16 |
| Dynamic `func_10006424` | 257 | 220 | -37 |
| Stored `func_10006828` | 65 | 55 | -10 |
| Builder `func_1000696C` | 293 | 413 | +120 |
| Compressed `func_10006E00` | 167 | 100 | -67 |
| Fixed tables `func_1000709C` | 77 | 82 | +5 |
| Entry wrapper `func_10006240` | 7 | Not emitted separately | -7 |
| Fixed decoder wrapper `func_1000692C` | 16 | Not emitted separately | -16 |
| Leading C helpers | 0 | 55 | +55 |
| Total | 996 | 1,052 | +56 |

The core C body is 48 words plus one padding word. Fixed-wrapper behavior is
folded into the C stream's fixed-block path, not emitted at the original entry.
Absent distinct wrappers are not recovered zero-length ABI implementations.
This ledger is size accounting only: neither per-role size fit nor aggregate
fit proves preserved entry addresses, word matching or original-entry ABI.

## Generated Accounting

`compile_init_decompressor.py` now includes `retail_slot_ledger` in each
profile receipt. It reuses `pad_generated_object.parse_retail_slice`, reads
explicit retail start/end labels, checks contiguous aligned slots and requires
the exact seven-function compiled set. It rejects duplicates, invalid body/
slot sizes and text totals smaller than named slots. Wrappers are recorded
separately as lacking distinct C entries; leading helpers are accounted for.
Compiler flags and candidate C source are unchanged.

## Verification

Focused slot-ledger and guest-call tests: 12 pass in 0.073 seconds.
Eight fresh IDO objects (embedded/frame controls and both cursor comparison
points, O2/g3 and O1) compile with independently checked empty logs. All eight
retain their pre-change `.text` SHA-256 hashes. The packed cursor O2 receipt
confirms 997 named-slot words plus 55 helper words, 56 over retail's 996.
Root `make tools-check`, Python syntax checks and `git diff --check` pass.
All 1,421 project tool tests pass in 585.379 seconds. No production source,
compiler profile or word guard changes are included in this checkpoint.

Fresh structured CSV accounting remains 492 C rows / 151,796 bytes and 47
assembly rows / 12,252 bytes. The remaining-group decisions in
[Note 801](801-init-post-pause-assembly-conversion-assessment-20261003.md)
still apply: bitmap/MMIO are small C-expressible matching candidates, the
decompressor is connected ABI/layout work, and SDK/boot/privileged owners are
not an ordinary missing-C backlog. No production build is rerun here.

## Next

Target the builder's actual 120-word overrun before another dynamic-only
optimization. Fixed setup and merged stream also exceed their individual
allowances; helper placement and original entry adapters remain unresolved.
Spare dynamic/compressed words do not automatically repair those entries.
Keep the byte-exact production ASM until fitting, ABI and storage ownership
are independently qualified. Native semantic tests and guest codegen receipts
do not execute compiled C on MIPS or establish hardware/gameplay acceptance.
