# Packed Point Slot Provider Byte Match

Date: 2026-10-16. Consumer predecessor **dd05e48c**, tools predecessor
**6909297**. Previous goal turn: **progress**, installing the 55-word
transform. Continue the wider Game matching goal, not just this pair.

## Retail Contract

```text
func_1509499C  VA 0x1509499C..0x15094AB8  ROM 0xC1E4C..0xC1F68
71 words / 284 bytes / leaf frame 0
```

The packed source has an unsigned range byte at offset 1 and a point-array
pointer at offset 4. The low nibble is the first slot; the high nibble is the
inclusive last slot. Recover signed halfword bounds, a 32-bit cursor and
16-byte point rows. Clear the prefix, populate the selected range starting
at the first point row, then clear the tail. All 256 bytes produce exactly
sixteen stores. Reversed bounds clear the whole output, not an invalid loop.
The provider does not dereference the point rows or allocate a stack frame.

Replace the zero-return placeholder with a void two-argument routine and
correct its local prototype. Keep `PackedPointSource948C0` and descriptive
local names, plus the recovered behavior comment. The existing transform
ignores the old placeholder's false return value. Eighteen other owner
bodies and relative bindings, including that caller and the rectangle,
remain unchanged under the existing compiler profile.

## Source Fit And Guard Boundary

Revalidate **104 measured complete-owner source forms** and their physical
objects/bindings/linked words. Caching the packed byte often emits 63 words;
field-based bound expressions recover retail's 71-word unrolled prefix and
middle loops. Narrow cursors produce 44/45 words, and unsigned cursors add
a word. Declaration-only, register-hint, pointer-array and guarded-loop
variants do not produce a raw direct match. Install none of the worse fits.

The selected source has **33 raw differences**, all scratch-register fields.
Every operation, immediate, shift count, branch target, memory offset and
instruction position is identical. Thirty-three expected-word guards
normalize the closed scratch roles. They do not insert/omit instructions,
change compiler flags or reorder accesses. Preserve every prior guard as
an exact byte prefix. Do not call this an unguarded raw-C match or infer
general register-renaming safety from the structural check alone: the
execution, ABI, access-prefix and connected-caller checks below are required.

```text
Raw C target SHA-256
0cb01a05cbec562a37a4ba900c6a3cb3668e3fcf016668627a71859d32c49f64
Normalized 71-word target SHA-256
00996153493e8ce73b27bc32ac67eb55774ec90af0896987c6fc80d5ed1ba330
```

The old additional-source snapshot is a semantic lead only. Its pointer/
integer accesses, expanded optimizer loops and inferred signatures are not
copied into production. Retail `lbu`/`lw`, signed bound coercions, point
stride and stores are the authority. The Graphify query confirms the local
transform/provider edge; scoped source/assembly searches establish the
observed named interface, not a universal no-other-callers claim.

## Qualification

Seven pre-install tests pass in **66.518s** using the actual emitted padded
artifact. They include:

- **6,144** provider cases: every range byte, both stack phases, four output
  layouts including aliases over the source, and point-pointer values zero,
  ordinary and near 32-bit wrap. Compare complete memory/access traces for
  retail/raw/normalized bodies, check saved ABI state and cover all 71 words.
  Raw caller-saved register identity is explicitly not claimed; normalized
  complete modeled state is equal to retail.
- **4,608** fault-prefix cases: every range byte at each of 18 memory accesses
  (two reads, sixteen writes). Check partial memory and access trace; these
  are emitted flat-guest instruction checks, not portable C or hardware faults.
- **2,048** connected cases: actual 55-word recovered caller, actual candidate
  provider and real 40-word retail matrix routine. Exercise signed coordinate
  edges, output aliases and stack phases, with independent public outputs and
  no opaque helper hooks. The pair no longer relies on a production provider
  stub after installation; full gameplay and hardware FCSR remain unqualified.
- Separate native32 O2/O0 units with UBSan, **2,560 cases each**, compiling
  the actual provider and actual caller rather than a provider contract fixture.
  Wrong first nibble, exclusive end, point stride and uncleared-prefix controls
  fail observably with exits 22/22/21/22, not compiler failures.
- All 18 copied neighbors, 71 word/operation controls, unexpected binding/pool
  controls, 100 frozen-input controls, 33 guard rows and original guard history.

Native cases use valid disjoint C storage; alias/wrapping-pointer receipts
apply only to compiled flat-guest execution. Do not generalize these tests
to portable C aliasing, asynchronous behavior, all callers or full gameplay.

## Complete First Prediction

Before installation, reproduce the predecessor with its saved link script
and owner object, then freeze the candidate image. The full prediction
changes **220 ELF bytes**: 218 code bytes inside the original 284-byte slot
and two function-size bytes (**12 -> 284**). No symbol/string reorder, new
symbols, metadata exclusions or unexplained changes are accepted.

```text
ELF    931955c4a1beee4e093894ea1cb87602f7177a1dc064165aafd28159ae2390fa
Owner  d6e245b869f60915b84d4a7c22da60dbe96f018635238aea7bde6bc8929897c3
Guards 6d409b75d30f2d5d7db243a5220aaa97011ed8a59054445693761ed1f25df465
```

The normal guest build is required after installation. The shared CSV
dependency rebuilds unrelated SDK/Game/Init objects too; preserve the known
duplicate `generated_12D630` recipe and existing unrelated pointer/varargs
warnings rather than mixing cleanup into this match.

## Verified Checkpoint

The normal guest build completes with exit 0, and **all ten final tests pass
in 112.747s**. The entire 3,257,636-byte installed ELF equals the first
prediction, including every byte outside the target slot and symbol extent.
Protected **189,088 bytes / 720 owners** are exact, the 18 neighboring raw
bodies/bindings and **97** other tracked inputs stay fixed, and all prior
guards are an exact byte prefix. The exact-successor adapter recognizes only
the three fingerprints above and validates both fixture stages; unknown
current files are not normalized.

Fresh official measurements:

| Section | Converted | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,501 / 6,044 (91.02%) | 3,597 / 5,501 (65.39%) | 0 | 1,904 |
| Init | 492 / 539 (91.28%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,828 / 5,323 (90.70%) | 2,924 / 4,828 (60.56%) | 0 | 1,904 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

The replaced placeholder already counted as converted C, so only exact
counts rise. Conversion bytes remain 86.04% overall and 85.41% Game. Ignore
the two repeated concatenated CSV header rows when counting function records.
Root README changes only its two affected aggregate match rows; narratives
remain in the working documents. Check off the provider in the prior roadmap
entry, keeping the still-unmatched rectangle as a separate open task.

Tools commit **cc49cf5dc413a15ee144b0fb303bb020421f9f63** banks the four new
experiment/checkpoint/test files before the consumer pin. Windows AST parsing
passes for all eight files across both tools copies; their four new files
are byte-identical. Eleven shared padder tests pass in each copy (0.051s
consumer, 0.048s old mirror), and `make tools-check` passes. Preserve the
old standalone mirror's HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**,
all **833** initial dirty-file hashes and **837** final dirty paths. No mirror
commit, reset or overwrite of pre-existing work.

## Resume Boundary

Next inspect **func_15094EA0**, the adjacent 40-word/frame-0x98 matrix
preparation routine: two `guMtxL2F` calls followed by `func_150A7A48`.
Its production stub and the larger 250-word `func_15094AB8` remain unchanged.

**func_15095D34 remains at 18 differences**, 346 words / frame 0x88 and
literal 148/91-word spans. Its twelve flip-block scratch/schedule words and
six macro-home accesses remain open. Continue the wider Game/additional-
source/caller queues; this checkpoint does not complete the Game goal.
No push, Claude/auth retry, host-port/frozen Release edit, build or launch.
