# Extended angular emitter direct byte match

Date: 2026-11-19. `func_150BB498` replaces the zero-return placeholder in
`conker/src/game/generated_E8090.c`. The complete **151-word / 604-byte body**
emits directly from C, VA `150BB498..150BB6F4`, ROM `E8948..E8BA4`.
Three original zero alignment words complete its **154-word / 616-byte slot**
through `150BB700` / ROM `E8BB0`. The original **192-byte frame** and **22
relocation sites** match. There are **zero guards, insertions or omissions**;
the normal O2/g3 profile and original ASM are retained.

Fresh production totals: **4,557 / 5,514 (82.64%)** overall,
**3,884 / 4,841 (80.23%)** Game, Init **492 / 492**, Debugger **181 / 181**,
zero drift and **957** still different. **130 more** matches reach 85%.
Conversion stays 5,514 / 6,048 (91.17%), 86.19% of bytes. The goal remains active.

## Recovered interface and descriptor

The shared callback retains all fifteen o32 words: coordinates at arguments
2/3/4, a word heading at 8 and byte context at 14. Retail loads the heading
word before byte narrowing, so the direct C formal remains `u32`; the actual
dispatcher zero-extends its byte heading. Qualification connects the original
MIPS call and does not invoke an incompatible native callback pointer.

The descriptor is **124 bytes**, of which **112 are initialized**. Reserved
bytes `59..5B`, `69`, `6B`, `71`, and `76..7B` remain unspecified. The frozen
backend source copies all `0x7C` bytes. Do not add a memset or field defaults.
Pitch, four trigonometric temporaries and speed must precede the descriptor
declaration to recover its original SP+`2C` home. Rotation-zero assignments
precede scale-one assignments in the recovered source, restoring the original
FP constant allocation while the scheduler emits the original store order.

Four byte-angle samples recover heading/pitch sine and cosine. Unsigned RNG
chooses pitch `%13-52` and duration `%68+38`. Speed is REAL*9+3; horizontal
velocity uses the repeated `speed*pitchSine` expression and Y uses
`-speed * pitchCosine`, preserving negation before multiplication. Two other
REAL samples produce independent `*50 + -25` offsets. The additional scalar
fields read `D_8009FE7C`, `D_8009FE80`, `D_8009FE84`, `D_8009FE88`, and
`D_8009FE8C` at their original times around helper calls. Two size fields share
the final computed REAL/global expression. Flags are `9E8`, resource is 31,
and the original byte/halfword constants and untouched holes are retained.

The call is `func_15132A4C(&descriptor, 3, 255, 0, context, 0)`.
Its result is ignored; this callback **returns one even on creation failure**.
The complete original 15-word wrapper forwards seven backend words:
`(descriptor, 3, 255, 0, 0, contextByte, 0)`. The backend `func_1513264C` and
allocator remain opaque modeled services; the wrapper tests do not qualify
the entire backend or resource system.

The aligned retail census finds one pointer, ROM `22F4D8`,
`D_8008AA00[6]` / VA `8008AA18`, and no aligned direct JALs. The original
dispatcher window `1514C3C4..1514C404` forwards all fifteen argument words.
The successful return-one path visits 15 of its 16 words: `BEQZL` annuls
`1514C400`. Two effective return-zero controls exercise that word and branch
to `1514C42C`. The complete parent dispatcher remains outside this gate.

## Validation and production audit

Both final configurations pass **five tests**, zero failures/errors/skips,
**75.301s primary / 116.810s sibling overlay**,
with **316 imported tool fingerprints each**. The 866-file overlay contains
339 matching sibling files, 520 primary fallbacks, six task files and one
bootstrap. The real sibling dirty HEAD/status and 343 dependency hashes are
unchanged; conflicting sibling edits were not overwritten or claimed tested.

- Complete before/after owner compilation preserves all five neighbors and
  pools. Both production padders reproduce the complete body and three-word
  alignment tail, with 12 GNU rebases and 173 rejected instruction/binding
  corruptions. Raw source and assembled retail payloads match directly.
- **512 guest cases / 1,024 source-and-retail executions** match an independent
  semantic reference, visit all 151 body words, preserve saved ABI, and cover
  modular angles, unsigned RNG boundaries, signed-zero/finite FP inputs,
  helper-time global mutation, descriptor contents and creation failure.
- **320 original callback-window cases** check all fifteen argument words;
  **128 original factory-wrapper cases** visit all 15 wrapper words and check
  every backend argument word. Deeper factory behavior remains modeled.
- **256 SDK32 native cases each at O0/O2/O3**, UBSan, strict aliasing and no
  fast math pass. All 12 semantic negative controls fail. Initialized integer
  fields are compared in guest byte order; the 12 reserved bytes are not assigned
  invented native values. This native value boundary does not exclude image bytes.
- Actual Make and independent complete-image prediction agree on **649
  explained changed bytes** and **zero exclusions**. Four image corruptions
  are rejected. Production really rebuilt this owner; no prebuilt object was
  copied into production.

The linker makes seven exact record/string order permutations. They are pinned
in the manifest and reconstructed explicitly; these distinct-address symbols
are not aliases:

| Original order | Rebuilt order |
| --- | --- |
| `D_8009FE80, D_800A0280` | `D_800A0280, D_8009FE80` |
| `D_8009FE84, D_800A0284` | `D_800A0284, D_8009FE84` |
| `D_8009FE8C, D_800A028C` | `D_800A028C, D_8009FE8C` |
| `D_8009FE7C, func_1510B128, D_800A027C` | `func_1510B128, D_800A027C, D_8009FE7C` |
| `__n_seqpReleaseVoice, func_151F8994` | `func_151F8994, __n_seqpReleaseVoice` |
| `func_15071B18, func_151F8CF0` | `func_151F8CF0, func_15071B18` |
| `func_150DF4B8, func_151F9BF0` | `func_151F9BF0, func_150DF4B8` |

Every named ELF definition is compared, with only the target's explicit
12-to-604-byte symbol-size change. The complete ELF is byte-compared after
the specific payload/size/permutation changes; no metadata section is excluded.

Only source, owner object and ELF change among **1,841 frozen inputs**. All
**698 objects** are audited; only this owner changes. All **6,050 other
function bodies, addresses and extents**, five neighbors/pools and **189,088
protected bytes / 720 owners** stay unchanged. Guard CSV, progress rows,
Makefile, compiler inputs, shared headers and original ASM are byte-identical.
Production ELF SHA-256:
`258c298e429040ecb832ab5930f8050b84fb2b19af7ed9b22fd61ffcd09d8c8d`.

Fresh installed checks recompile all six owner functions/pools, compare the
actual 151 production words and three padding words, and rerun 512 guest,
320 caller and 128 wrapper cases. Unchanged padder/rebase/corruption/native/image
receipts are fingerprinted reuses. Required `match-progress` and `tools-check`
pass; the existing duplicate generated_12D630 recipe warning remains.

The first private source already had the correct body length/frame but 52
word differences. Declaration order reduced that to eight; rotation/scale
assignment order completed the direct match. The first qualification harness
omitted the original tail from its isolated reference object; it now emits
those 12 zero bytes after the 604-byte function symbol. The early failed
output is historical. Final paired suites ran after the metadata pins and
an AST-identical surplus-EOF cleanup were sealed.

Root README changes only two aggregate matching rows. Detailed progress is
here and in five concise documentation indexes. Graphify uses a native update
attempt, five-file scoped AST refresh, explicit target reference and old-ID
retention; this is not a full-corpus extraction claim. Routine work uses zero
Claude calls, no REA/WSL reconfiguration and no host/Release/save/capture changes.
The supplied `64CBFDOGL` path still contains `.codex` and `recomp_scene` captures
without an identifiable active host checkout; no host adoption is inferred.
Tools are committed before the consumer; no automatic push or pause.

Next inspect **func_150BB760**, still a zero-return placeholder in
`generated_E8C10.c`: VA `150BB760..150BBB5C`, **255 words / 248-byte frame**,
called from `game_981E0.c`. Preserve its actor-byte4 read before its null check.
The intervening `func_150BB700` already has C and is absent from the unmatched
list. No next-target candidate is drafted or credited; freeze its evidence
against this committed baseline before recovery.
