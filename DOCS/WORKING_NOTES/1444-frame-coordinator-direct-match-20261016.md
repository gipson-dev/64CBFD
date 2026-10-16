# Frame Coordinator Direct Match

Date: 2026-10-16. Consumer predecessor **7fded482**, tools predecessor
**d7a8bb1**. Previous goal turn: **progress**, restoring matrix preparation.
The wider Game matching goal remains active.

## Recovered Routine

```text
func_15019130  VA 0x15019130..0x15019414  ROM 0x465E0..0x468C4
185 words / 740 bytes / frame 0x28
```

Replace the false zero-return C placeholder in game_45B80.c with its
ordered frame/view coordinator. Preserve callback order, the reset byte
before func_10004250, independent live disabled-flag checks, signed-byte
flag load, live context/page arguments and the success return **1**.

The first view loop has an s32 cursor; the second has a u8 cursor. Both
use the inclusive signed maximum D_80082FA0 and reread it after callbacks.
Do not cache that bound, merge independent gates, widen the second cursor
or insert a non-retail clamp. An unchanged bound >=255 can keep the byte
loop running after wrap; tests use finite mutation cases and bounded
prefixes rather than changing production behavior.

After all callbacks, increment the u32 age at offset 4 of every one of
508 eight-byte software-page records. Preserve the first word/tag and
unsigned wrap at 0xFFFFFFFF. The legacy D_80043B40 pointer declaration
labels this table's address, not a stored table pointer: take its address.
Keep this correction local instead of changing the shared variables header.
Typed local callback declarations preserve the current recovered return
classes and the observed integer argument interface; keep address-based
function names rather than invent unsupported behavioral names.

Six complete-owner screens are retained and physically revalidated:

| Source form | Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| pair-pointer-limit | 181 | 0x28 | 23 |
| pair-pointer-equal | 198 | 0x20 | 165 |
| pair-pointer-fixed | 176 | 0x28 | 24 |
| indexed-ages, selected | 185 | 0x28 | 0 |
| signed-flag-value | 181 | 0x28 | 23 |
| reverse-cursor-declarations | 181 | 0x28 | 27 |

All **185 words emit directly from C**, with zero new guards, insertions,
omissions or compiler-profile changes. Raw target SHA-256:
`dbcbe78409e04795168d1e760db8592e2cf2b52aae4129b0046bbf34f24fdbe4`.
Linked slot SHA-256:
`db23322789f9b3e81cddb0417c857bd1d4cd58255f6612a88b96548354c9ec49`.

## Qualification

Seven pre-install tests pass in **115.435s**. All **ten final tests pass
in 179.908s**, using:

- 1,024 complete-state original/raw/padded guest cases, two stack phases,
  byte/age edge values, eight callback modes, all 185 root instructions
  and 14 distinct fired effect sites. Sweep all 256 disabled-byte values.
  Opaque callbacks trash volatile registers and all four O32 argument homes.
- Every one of the **1,058** root memory-access fault prefixes on the
  representative path, comparing complete modeled states. Three finite
  wrap cases exercise 255/257/257 second-loop invocations; three bounded
  large/nonterminating prefixes retain the original byte cursor.
- **256** connected cases / **448** preparation invocations, using freshly
  qualified real 40-word preparation, 46-word SDK conversion and 78-word
  product slots. The product kernel remains assembly, not converted C.
- The original eight-word upstream call/success-gate window at
  0x150188FC..0x1501891C. Test the real return-1 fallthrough and disabled
  skip with its original delay slot. **func_1501878C remains a 12-byte
  installed stub**, versus 412 retail words; this cut is not a full-caller
  restoration or installed gameplay qualification.
- Separate-unit native32 O2/O0 with UBSan, **131 cases each**. Python
  independently supplies expected callback packets, all 508 ages and final
  globals. Valid fixture arrays bind the legacy table label without altering
  the shared header. Harness flags include -mstackrealign and
  -fno-strict-aliasing, not production guest compiler changes.
- Seven compiled, effective controls: cached disabled flag/bound, return 0,
  509 ages, tag-field update, widened second loop and narrowed first loop.
  They fail at explicit protocol/data gates with exits 21/23/25/26, not
  compiler errors, signals or unexplained timeouts.
- All **15** neighboring raw bodies and relative bindings fixed. Reject
  corruptions of all 185 target words, all **76** bindings, unexpected pools,
  all 103 frozen/live inputs, slot prediction, code/callee/upstream/metadata
  bytes and both saved fixture stages. Check independent J26/HI16/LO16
  rebases and the table end's nonzero 0xFE0 addend at two allocation positions.

The target has no new compiler diagnostics. Four existing Warning 712
pointer/integer warnings remain in func_15018F08, func_15019BB8 (two sites)
and func_15019E60. Compile the predecessor too and check warning code,
statement, caret, actual source line and containing function. Do not suppress
or misreport the owner stream as empty. The SDK retains its known
-Xfullwarn warning; the fresh product-owner diagnostics are empty.

These are flat guest instruction/ABI and valid-storage native checks.
They do not establish portable C fault/alias behavior, hardware FCSR,
semantics of every opaque callback, a completed upstream or full gameplay.
Prior unchanged broad suites are not claimed as freshly rerun.

## Complete First Prediction

Freeze the original owner object/link script and reproduce the entire
predecessor before installation. The first strict slot/extent-only
prediction correctly rejects **16 additional bytes**. Diagnose them as two
adjacent equal-length symbol/string swaps:

```text
D_80088894 <-> D_800884D4
D_80084190 <-> D_80084930
```

Require each original record's exact location, string and semantic fields,
apply only those named permutations, and verify canonical-symbol equality.
No metadata section is excluded. The complete first accepted prediction is
**516 changed ELF bytes**: 498 inside the target slot, two extent bytes
(12 -> 740), and exactly 16 serialized metadata bytes. The normal guest
build reproduces the entire 3,257,636-byte predicted ELF:

```text
ELF    c67f8312dad8796dfc0a49a2f0896639b9561b1ddd0b127fe69b6352fa7d0894
Owner  43c2eff427f2727668e82bfe1c70200588a500991e47abeae0af30a0471eccfa
Guards 6d409b75d30f2d5d7db243a5220aaa97011ed8a59054445693761ed1f25df465
```

The guard CSV, progress CSV, Makefile and shared headers are unchanged.
Only this owner recompiles before link/progress regeneration. Preserve the
known duplicate generated_12D630 recipe warning. All **101** other captured
inputs and protected **189,088 bytes / 720 owners** remain fixed; symbol
names and semantic attributes are unchanged except the target size.
The successor adapter recognizes only the exact two hashes above and checks
its immutable before/after fixtures. Unknown live bytes are never normalized.

## Verified Checkpoint

| Section | Converted | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,501 / 6,044 (91.02%) | 3,599 / 5,501 (65.42%) | 0 | 1,902 |
| Init | 492 / 539 (91.28%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,828 / 5,323 (90.70%) | 2,926 / 4,828 (60.60%) | 0 | 1,902 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts/bytes do not change because the old placeholder already
counted as C. Root README changes only its two aggregate match rows; detailed
recovery belongs here. Check off the old coordinator item and keep the
independent upstream, rectangle and wider Game work open.

Tools commit **c820bde199f521e4e6a173df9232a973582e872c** banks six task files before the consumer
pin. Windows AST parsing passes all 12 files across both copies; all six
mirrored files are byte-identical. Eleven shared padder tests pass in each
copy (0.053s consumer, 0.071s mirror), and make tools-check passes. Preserve
mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **841** initial
dirty-file hashes and **847** final dirty paths, without committing or
resetting that independent checkout.

## Resume Boundary

Continue upstream **func_1501878C**, 412 original words, under its own
semantic/ABI/owner/image gates. The adjacent 250-word func_15094AB8 remains
stubbed; rectangle func_15095D34 remains 346 words / frame 0x88 /
18 differences, including the twelve flip-block words and six macro homes.
The broader matching/additional-source queue remains active.

Zero Claude calls: existing compiler/retail/model evidence settles this
routine. No push, Claude/auth retry, host-port edit/build/launch or frozen
Release action. The user confirmed the previously overwritten parent
Conkers scratch file was disposable; no recovery action is required.
