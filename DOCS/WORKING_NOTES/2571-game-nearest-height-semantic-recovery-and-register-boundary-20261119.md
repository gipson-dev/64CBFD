# Note 2571: Nearest-height semantic recovery and register boundary

Date: 2026-11-19. Consumer baseline `852fab3f0b52951530e39b64e2d35af378cbc9fa`;
tools baseline `5472bb9163aecddc1adbeed23aee5a7e77750930`.

`func_15104634` now has a complete, independently tested **private semantic C
recovery: 272 words / original frame224**, fitting its 275-word retail slot.
The saved F20/F22 opening, incoming homes and all three private array bases
match. **137 real word differences remain. No source installation, guards,
padding normalization, production rebuild or matching credit is claimed.**

The live owner remains `conker/src/game/generated_131A90.c` with its false
zero-return placeholder for this routine. Four original no-op/constant-return
neighbors remain raw byte-identical in the copied candidate owner. Shared
headers, original assembly, Makefile, guards, conversion CSV, every production
object and ELF are unchanged. Root README is unchanged.

Fresh recount confirms total **4,564 / 5,516 (82.74%)**, Game
**3,891 / 4,843 (80.34%)**, zero address drift, 952 different; **125 further
matches** are needed for85% at this denominator. Init492/492, Debugger181/181.
Converted totals remain5516/6048 (91.20%),86.24% bytes.

## Complete recovered behavior

Body VA `0x15104634..0x15104A74`, slot through `0x15104A80`, ROM
`0x131AE4..0x131F30`. The original has272 instructions and3 alignment NOPs.
The interface returns signed status and receives **f32 X, f32 Z, f32 target
height, pointer to f32 output** through F12/F14/A2/A3. It first selects collision
context0, then truncates X/Z to signed32 and calls `func_150A3A70`.

Each16-byte entry at `D_800D3300` contains signed fixed-point height, a pointer
to three unsigned vertex offsets, a packed vertex base and an unused word.
The shared variables header's pointer declaration is unsuitable for this direct
array access; the private source uses its own local typed extern and leaves the
shared header unchanged. Signed16 X/Z are read at vertex+0/+4.

For each returned hit, the routine reconstructs three X/Z vertices and evaluates
their projected orientation in the original single-precision order. Only strictly
positive orientation enters the accepted-index list. No hits or no accepted
triangles returns0 without writing through the output pointer. Negative provider
counts skip the first loop and also return0.

The second scan converts each accepted signed32 fixed height to f32 and scales
by1/256, then selects the smallest absolute difference from the supplied target.
Its initial bound is `D_800A2370`, retail bits0x461C4000 (10000). The first
accepted candidate is always selected, even with a negative/NaN bound; equal
distances retain the earlier hit. A NaN target likewise retains the first
accepted hit. The selected scaled height is stored and status1 returned.

The private candidate declares24 accepted indices and validates counts through24.
That is a bounded C fixture domain, **not a recovered original debug array type
or proof of safety at every count the handwritten query can return**. Original
capacity/overflow behavior beyond this domain is still open. No additional
runtime bounds check has been inserted into the candidate.

## Compiler shape and remaining differences

The first full body was183 words/frame232. Keeping an explicit vertex pointer
at function scope restores its original software-pipelined three-vertex loop.
Caching the selected record index before the height calculation restores the
original four-way unrolled nearest-height scan and its remainder loop.

Reusing the edge/intercept temporaries across the two separate scan phases
recovers frame224 and both saved FP lifetimes. Declaring two scalars before
the arrays puts vertex Z, vertex X and accepted indices at SP+0x60/+0x6C/+0x78.
The first10 bound words, including the F20/F22 save/parameter lifetime, match
retail literally. No padding variable, volatility, profile override or word
replacement was added.

A fingerprint-locked read-only trace follows newly owned CFE/UOPT/UGEN children.
It preserves complete normal output and records child/driver completion.
Frontend M is160, optimized M184; UGEN observes saved component24, outgoing16,
locals184, frame224. These are compiler layout fields, not performance timings
or an assertion about original source variable names.

Independent assembly of the complete original body confirms all12 relocation
sites/bindings agree. The137 differences are34 SPECIAL GPR-field words,
49 other register-field words,48 COP1 register-field words and6 private X/Z
coordinate loads. Opcodes, operation functions, branch displacements, call
positions, constants and public addresses otherwise agree. The coordinate
loads feed differently allocated orientation expressions; they are not arbitrary
data corrections. This classification is **not yet a proof of complete private,
ordered FP/FCSR or fault-prefix equivalence**, and is not permission to append
137 replacement rows.

## Fresh qualification and limits

Primary tools and isolated sibling overlay each pass the same four-test suite:

- All1948 frozen inputs remain unchanged. Complete candidate owner compiles
  without diagnostics under existing O2/g3. All4 neighbors and constant pools
  remain raw-identical. Every one of1088 raw bytes and all bindings has an
  effective corruption check against the selected candidate fingerprint.
- 410 cases per original/private-C stream compare complete public memory,
  provider calls, returned status and saved F20/F22 pairs. Cases cover count
  boundaries0..24, negative counts, orientation rejection/degeneracy, signed16
  extremes, signed fixed-height extremes, first-hit/tie rules, signed zero,
  infinities, quiet NaNs, provider changes and guest-only incoming-home effects.
  Five effective instruction negatives pass. Each stream visits269 body words;
  words205/227/250 are unreachable fallback moves in later unrolled lanes
  after the first candidate has already established a nonnegative selection.
- 335 actual SDK32 C cases each at O0/O2/O3 with strict aliasing, UBSan and
  float-cast-overflow checks; eight source negatives per profile execute and
  return failure1. Expected results and complete table/coordinate values are
  serialized from the independent Python contract. Native fixtures use declared
  signed vertex fields and byte accessors for float bits. Stack entry alignment
  is explicit. Counts stay within24 and X/Z conversions within signed32 range.
- The genuine21-word `func_150538CC` window at VA0x15053CD8..0x15053D2C
  passes32 scenarios per stream. Its sole direct JAL is ROM0x811A0. F12/F14,
  target actorY+50 in A2, output SP+0xB4 in A3, success branch and actor-height
  clamp are checked. No literal target pointer occurs in the prior full-ROM
  census. The rest of that parent is not claimed qualified.

The guest model explicitly supports NEG.S by sign-bit inversion and seeds both
halves of saved FP pairs. An initial fixture mismatch used the parent's old
saved-register snapshot; it is corrected locally. An ineffective AND/OR mutation
of zero was not counted. Provider
models remain bounded. Public-result agreement is not private-state or complete
instruction-access/fault-prefix proof. FCSR, interrupts, hardware and host-port
gameplay are not modeled. `make tools-check` passes.

The real dirty `64CBFD Tools` sibling retains HEAD/status and343 dependency
hashes. The930-file overlay contains339 same sibling files,585 explicit primary
fallbacks,5 task files and1 empty bootstrap; imported dependency bytes agree
apart from the bootstrap. No host-port source or frozen Release artifact changes.

Graphify's native update refuses shrink. A scoped four-tool-file AST merge
retains prior IDs; the source manifest references the still-uninstalled target.
Commit-hook producers must exit before historical aliases and the graph hash
are sealed. This is not full-corpus extraction. Routine work used zero Claude
calls. Reproduction: `python3 -m unittest
tools.tests.test_game_nearest_height_15104634_recovery -v` under prepared WSL.
Ignored candidate, source screens, trace and handoff are in
`conker/build/game-nearest-height-15104634-private/`.

## Next steps for this function

1. Resume from canonical.c and the committed five-file recovery fixture. Use
   remaining-differences.json and frame-provenance.json; do not restart the
   failed size/loop screens or change the four already-exact neighbors.
2. Derive the live GPR/FPR role mapping and the ordered orientation expression
   relation, including the six private coordinate loads and retained fallback
   words. Improve source directly where supported. Keep the full private/fault
   and FP-status boundaries explicit; public tests alone do not authorize guards.
3. Once that relation is proved, qualify any necessary relocation-aware guards,
   independent padders/rebases, actual Make recipe and strict whole-image change.
4. Only then install the body, rebuild production, rerun both installed suites,
   recount actual ELF, update aggregate rows and commit tools before consumer.
   The full85% matching goal remains active. Older private func_150BBB5C remains
   uncredited and untouched.
