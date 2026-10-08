# Game Cached Primitive Color Direct Match

Date: 2026-10-07. Baseline: `548b94b9`,
[Note 1093](1093-game-cached-environment-color-match-and-sampler-flow-audit-20261007.md).

`func_15142CF0`, VA `0x15142CF0..0x15142E24`, ROM
`0x1701A0..0x1702D4`, now emits **all 77 words / 308 bytes directly from C**
under unchanged **O2/g3**, with the original **frame `0x8`** and saved S0.
Recover the positive six-field cache-miss gate and actual SDK
`gDPSetPrimColor(output++, minimumLod, lodFraction, red, green, blue, alpha)`.
No guards, compiler-profile/header/padder edits or padding locals are needed.
The previous early-return/manual-packet C body was semantic but nonmatching.

## Source Controls

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_cached_primitive_color_candidates.py)
retains twelve cache-gate/cursor/SDK/explicit-packet forms across four SDK
profiles: **48 measurements**. Only `positive1-cursor0-sdk-o2g3` is exact,
77 words/frame `0x8`, empty diagnostics. Using the same positive gate with
an explicit packet local gives 77 words but 12 differences; direct stores
give 76 words and 25 differences. Keeping the original output variable
matters: a separate cursor shortens the O2/g3 SDK body to 73 words/frame zero
and does not match. Word count alone is not a qualification gate.

Use the SDK's unsigned packing to remove the old signed red-channel left
shift. Preserve full signed32 inputs and the six signed16 cache declarations;
narrowing inputs before comparison would change cache hits.

## Contract

- Compare minimum LOD, LOD fraction, R, G, B, A lazily in that order against
  `D_800DD204`, `D_800DD206`, `D_800DD1C0`, `D_800DD1C2`, `D_800DD1C4`,
  `D_800DD1C6`. A hit returns the original cursor without reading sync/output.
- On a miss, read sync once. Only byte **one**, not any nonzero byte, emits
  `E7000000 / 00000000`, advances the cursor, then clears sync.
- Emit `FA000000 | (minimumLod.low8 << 8) | lodFraction.low8` and
  `RRGGBBAA`. Advance the cursor, then write all six input low halfwords
  back to the caches in comparison order. No calls or allocation occur.
- Preserve packet/clear/cache order when output, either physical cache block
  or sync storage overlap. A sync clear may overwrite a just-emitted byte;
  later cache stores may overwrite command words. Do not invent alias guards.
- Remaining stack arguments are loaded before packet writes. Command storage
  may overwrite their incoming homes without changing the values used for
  packing or the subsequent cache stores.

## Qualification

[Eight maintained tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_cached_primitive_color_match.py)
bind the full direct slot and original assembly:

- **174,720 guest fixtures**: every byte value in each of six fields, four
  signed/full-word edge vectors, seven first-miss/cache-hit positions, four
  sync bytes, three output locations, four sync aliases and two stack phases.
  These are not all Cartesian six-field combinations. The independent
  reference checks complete external memory, returned cursor and every
  ordered public read/write. Raw C/retail additionally agree on complete
  memory, traces, GPR/FPR values, calls and visits. All 77 words execute.
- **448 incoming-home overwrite fixtures** cover edge inputs, lazy hits,
  all first-miss positions, sync states, both stack phases and sync aliasing
  a home. Independently seed incoming stack arguments before the reference;
  the incoming alpha word initializes the aliased sync byte. Check all
  overwritten home bytes plus complete external storage and returned cursor.
  Raw C/retail agree on complete memory, traces, registers, calls and visits.
- **7,280 actual freestanding native 32-bit fixtures** run the SDK macros
  with signed/full-word cache gates, LOD/RGBA packing, exact sync behavior,
  all six updates and unused-command fences. Native storage is disjoint;
  guest alias tests are not native-alias/hardware/rendering acceptance.
- A cache hit succeeds with sync/output unmapped. Every required cache,
  sync and output byte fails closed when removed. Seven compiled negatives
  change public results or lazy traces: unconditional emission, nonzero-sync
  gate, swapped LOD fields, swapped channels, missing clear, unsigned cache
  declarations and missing alpha-cache update. Private layout differences
  alone do not count as detecting a negative.
- The production-preprocessed/postprocessed copied owner retains **89
  functions / 88 neighbors**, relative relocations, normalized pools and
  the same **two warnings**. Its selected raw 308-byte target equals the
  isolated object. The real padder emits all 77 words, without overflow or
  guards. Independently move each of the six caches by `0x18000`; only its
  actual HI16/LO16 relocations change, including signed-low carry handling.
- The installed source, linked exact slot/address and unchanged guard history
  are pinned by a separate production gate.

Six pre-install behavior/owner/padder gates pass in **135.472 seconds**.
Repeated fixture runs are not additional distinct behavioral cases.

```sh
python3 -m unittest tools.tests.test_game_cached_primitive_color_match \
  tools.tests.test_game_cached_environment_color_match \
  tools.tests.test_game_owner_pool tools.tests.test_pad_c_object_word_patches -v
```

The combined regression passes **23 tests in 269.557 seconds**, zero skips,
errors or failures. Final tools/syntax/whitespace gates pass; the scoped
documentation gate checks **76 documents / 3,886 relative links**, zero broken.
After requiring both real relocation kinds for all six symbols and an actual
word change for every independent move, rerun the strengthened owner/padder
gate: **one test in 2.623 seconds**. This is a repeat gate, not another distinct
behavioral fixture set.

## Build And Audit

`make -C conker build/conker.us.elf -j2` succeeds with the existing duplicate
recipe warning and the same two owner pointer warnings. Fresh pre-edit and
post-link audits retain **6,058 linked symbols**: **6,042 retail slots** plus
16 compiler overflows. Every address/extent stays fixed; only `func_15142CF0`
changes. All **6,041 other retail bodies**, including the environment-color
emitter, translator and unresolved sampler, and all overflow symbols are
identical to the fresh baseline.

Protected Init/Init-data/Debugger/Game-data sections, **720 Game-data owners /
189,088 bytes** and all **11,006 guards** remain unchanged and exact. Neither
color emitter nor sampler has guards. Converted functions/bytes do not change;
this color routine already had C.

Exact total advances to **3,360 / 5,466 (61.47%)**, Game to
**2,687 / 4,793 (56.06%)**, **2,106 different**, zero drift. Init492/492 and
Debugger181/181 C functions remain exact. Main README changes only its two
aggregate matching rows; detailed updates stay under DOCS.

## Resume

Next ordinary owner target: **49-word `func_15142314`**, matrix translation
extraction. Original fixed mode converts the shifted signed high half and
signed low half separately to float before addition/scaling. Current C instead
adds the integers before converting, and uses signed left shifts. Recover
the original arithmetic and repeated matrix addressing, then qualify fixed/
float modes, signed-halfword extremes, index/addressing, sequential output/input
aliases, full original helper execution and owner/padder/install gates. It
remains untouched and nonmatching in this checkpoint; see the original-helper
coverage in [Note 1073](1073-game-point-transform-assembly-to-c-match-20261006.md).

Sampler `func_151432BC` still needs two legitimate per-path RA loads and the
circle RNG-byte store schedule. Do not repeat the 252 historical measurements
as new evidence, install a short nonmatch, add scheduling instructions or
patch private/frame offsets. This checkpoint adds no sampler measurements.
No sibling/frozen Release, save/runtime, rendering/hardware acceptance or push.

Ignored receipts: `conker/build/game-cached-primitive-color/` and
`conker/build/game-cached-primitive-color-test/`.
