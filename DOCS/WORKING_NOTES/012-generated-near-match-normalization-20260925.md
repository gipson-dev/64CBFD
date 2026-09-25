# Generated game near-match normalization - 2026-09-25

## Result

The final four one-difference game functions are byte-exact in the linked US
ELF:

| Function | Length | Offset | Compiled | Retail | Resolution |
| --- | ---: | ---: | ---: | ---: | --- |
| `func_150AF2E0` | 18 words | `0x018` | `0x01C27821` | `0x004E7821` | commuted integer `addu` operands |
| `func_151061EC` | 10 words | `0x018` | `0x01C41021` | `0x008E1021` | commuted address `addu` operands |
| `func_15144A74` | 13 words | `0x028` | `0x46048000` | `0x46102000` | commuted `add.s` operands |
| `func_151ACB60` | 13 words | `0x020` | `0x00000000` | `0xAFA40018` | incoming pointer home in the `jal` delay slot |

Every other word, function extent, control-flow edge, call, and return already
matched retail. Earlier source-shape experiments did not change the first
three operand orders, and IDO would not schedule the fourth store into the
retail delay slot. These four independent compiler-layout differences are now
encoded as expected-word-guarded normalizations in
`conker/retail_word_patches.us.csv`.

## Tooling

Three functions live in generated slices, whose build path uses
`tools/pad_generated_object.py` rather than `tools/pad_c_object.py`. The
generated-object padder now accepts the same CSV contract for word
replacement, verifies the expected compiled word and optional relocations,
rejects unsupported insertion rows, and fails if a selected patch is not
applied. Generated-slice Makefile rules pass the CSV and source filename key.

## Verification

- Full `make -j8 build/conker.us.elf` rebuild and link passed.
- The generated-padder and C-padder unit suites passed: 4 tests.
- The linked matcher reports `2532 / 5497 (46.06%)` total,
  `1964 / 4808 (40.85%)` game, and `181 / 181 (100.00%)` debugger.
- None of the four function names remains in the linked differing-function
  list. Game functions still different decreased from 2,848 to 2,844.
- The `64CBFDOGL` sibling contains these as generated recomp functions. The
  changes are IDO-only normalization/tooling and do not transfer. Its dirty
  worktree was not modified, and frozen Release was not built or launched.

## Next boundary

There are no one-difference game rows left. Re-triage the two-difference game
queue, beginning with the smallest non-placeholder bodies. Current candidates
include `func_150A6354` (3 words), `func_150AD770` (4 words),
`func_15087FC4` (10 words), `func_1519C910` (14 words), and
`func_15087FEC` (16 words). Inspect each body before editing: very short rows
may be placeholders, stubs, or compiler artifacts rather than useful source
recovery targets.
