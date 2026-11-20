# Note 2579: Map-edge emitter recovery and original frame

Date: 2026-11-19. Consumer baseline `2f35cc1857a9c437ed651805ffcecdf6ffe249f9`;
tools baseline `10feca24c6b7799c7c10eee4a86b5e5dea7eba8a`.

`func_151050B0` now has a tested **private 275-word semantic recovery**, with
its original **208-byte frame** and original packet/vector homes. Retail has
279 words. The live source remains GLOBAL_ASM; **this stage is uninstalled and
has zero matching credit**. No guards, conversion rows or production objects
change. Root README is unchanged because its aggregate measurements agree.

Fresh linked recount stays **4,568 / 5,519 (82.77%)** total, **3,895 / 4,846
(80.38%)** Game, zero address drift and 951 different. Init 492/492 and
Debugger 181/181 stay exact. The full 85% goal remains active; 124 more matches
reach it at the current denominator, which later ASM conversions can increase.

## Complete body and observed interfaces

The retail body spans VA 0x151050B0..0x1510550C, ROM 0x132560..0x1329BC, with
279 words and frame 0xD0. It is a void update callback taking `struct260 *`:
registry `D_8008A4E8` slot 61, literal pointer ROM 0x22F09C/VA 0x8008A5DC. The
original dispatcher `func_15149264` does not consume a result. The candidate
removes only the local zero-argument/signed-result placeholder declaration.

A complete 152-byte outer record contains the 36-byte SDK header, observed
four-byte gap and 112-byte inline emitter at +0x28. The emitter contains a source
pointer, signed 16-bit timer at +0x4, accumulator at +0x8, four XYZ positions at +0xC, four
XYZ direction vectors at +0x3C and a gate pointer at +0x6C. The source state byte is
at source +0x14. Local types describe those observed offsets; shared headers
and all ten neighboring owner functions remain unchanged.

A negative initial timer sets source state 1 and returns. Otherwise the body
sets source state 0, subtracts the current 32-bit frame ticks with wrapping and
signed 16-bit narrowing, and dispatches commands 0x39 and 0x4B if the result is
negative. This expiry path continues into the gate test. Explicit unsigned
subtraction avoids signed-overflow UB for extreme tick values.

When the gate permits it, the body calls the float RNG before reading the
rate globals, then adds `(D_800A23B4 + random * D_800A23B8) * D_800BE9A4` to
the accumulator. The pinned rate words are0x3D23D70B and 0x3D8F5C29. An
accumulator strictly above 1 enters emission. A cached D_800A23BC value
(0x3EA66667) is retained for all iterations, including helper mutations.

Each iteration chooses a first byte index from `random * 3`, then a second
byte from `(random * 2 + 1) + first`, subtracting 4 if needed. Two further
random samples interpolate XYZ from the selected position/direction pairs.
The body calls `func_15106F98(firstPoint, secondPoint, 3, packet, cachedWidth,
2, recordByteC, recordByte1)`, reloads/decrements the accumulator by 1 and
repeats only while it remains strictly above 1. The child begins by copying all
48 packet bytes; that copy extent/interface is observed, not full child proof.
Packet field names follow their observed writes; parameter units remain open.

## Source/profile and layout evidence

The first complete candidate had272 words/frame 200 and reloaded the width
inside the loop. A cached width and a named second-index scale retain the
original multiply rather than the compiler's add-to-self fold. Explicitly
sequencing the initial RNG result recovers frame 208 and fixes the source's
helper/global-read boundary. Writing the natural position-plus-scaled-direction
expressions recovers the tested original ordered FP operands.

Moving the meaningful RNG temporary before the aggregate declarations recovers
all original homes: secondPoint at SP+0x84, firstPoint at SP+0x90, packet at SP+0x9C. This also
closes the five raw descriptor-padding differences seen in the earlier +4
layout. The accepted275-word body matches all 48 copied descriptor bytes in
guest execution, including seeded padding. No artificial frame padding,
volatility, extra pools or compiler-profile changes are introduced.

All probes use the existing O2/g3 mixed owner. Its ten other functions,
relocations and pools stay fixed; five pre-existing unrelated diagnostics
remain equal after only fixture-name/shifted-line normalization. Seven source
shape probes precede the final home-placement probe; their artifacts remain
private. Reproduction uses the canonical fragment and owner in the manifest.

There are267 differences in a naive same-offset word comparison, which is
affected by the four-word length gap and allocation/scheduling shifts. A
diagnostic opcode census, abstracting registers, branch destinations and private
homes, finds four retail-only occurrences: one saved-FPR store/load pair and
an additional LUI1.0/FP-transfer pair. The raw body has no extra opcode classes
under that abstraction. **This census is not an equivalence proof or a guard
ledger.** It does not justify copying retail words into the C object.

## Fresh qualification

Primary tools and the isolated968-file sibling overlay each pass six tests.
The real independently dirty sibling checkout and its 343 dependency hashes are
preserved; the overlay combines341 byte-equal sibling files,620 explicit
primary fallbacks, six task files and one package bootstrap.

- 684 cases per original/raw guest stream check all public bytes, ordered
  public accesses, calls/arguments, preserved ABI registers and all 48 copied
  descriptor bytes. Cases cover timer wrapping, equality thresholds, misses,
  helper changes to rates/positions/accumulator/packet/channel/category, cached
  width behavior and two explicit NaN operand-selection models.
- Guest coverage visits239/279 retail words and 235/275 raw words. Forty
  positions per stream remain unvisited, principally unsigned-conversion
  fallback paths outside the actual RNG range and retained redundant words.
  Whole-CFG and arbitrary-FCSR/hardware equivalence are not claimed.
- 158 fired public-access prefixes agree across both streams. This is emitted
  guest instruction evidence, not portable C fault-PC/private-frame identity.
  Six effective instruction mutations are rejected.
- 35 scenarios per stream execute the original 45-word dispatcher through
  actual slot 61. Other selectors and complete cleanup behavior are separate.
- Actual SDK32 O0/O2/O3 builds each pass496 finite cases, including248 calls
  through the actual C dispatcher. Strict aliasing and UBSan are enabled; eight
  compiled source controls fail. Native checks compare43 defined packet bytes;
  C padding and nonfinite payload/FCSR claims remain separate from guest tests.
- The original RNG mask/conversion/scale suffix and ROM coefficient are pinned.
  All65,536 possible masked values are checked against independent Python FP
  results in each native profile, proving the bounded float results and valid,
  distinct 0..3 selections. This does not execute/qualify the complete 64-bit
  seed-update algorithm.

An O2 fixture initially faulted on `movaps` with a stack address four bytes
off the native ABI alignment. GDB located it in the freestanding C-entry call
chain. Explicit alignment on that fixture entry fixes it; recovered production
C and shared compiler flags are unchanged. The width-reload negative control
also removes its unused cached variable so warning rejection cannot masquerade
as a semantic control failure. All accepted controls compile without warnings.

`make tools-check` passes. All2,001 frozen predecessor inputs and the unchanged
production ELF/progress/guards/source are audited. There is no production build
or candidate whole-image claim at this uninstalled stage. Tools are committed
before the consumer documentation/gitlink. No push or Claude calls occur.
The bounded host reference is a generated stub, not active-host acceptance;
there is no retail behavior delta to transfer and no host/Release change.

Graphify links the private recovery manifest to the actual original ASM
definition, with explicit uninstalled/zero-credit metadata. It does not create
a false installed C function. A scoped four-Python-file AST merge retains old
IDs; native update results and post-commit writer/alias receipts are separate.

## Next matching work

Continue this same function. Derive a complete paired CFG/effect relation across
279 retail and 275 raw words, including unsigned conversion control/FCSR paths,
saved-FPR lifetimes, ordered FP operands and complete private helper inputs.
Then derive only proven expected-word layout guards/meaningful insertions,
qualify both padders, actual mixed Make, independent GNU rebases and strict
whole-image prediction in both tools configurations. Install/rebuild/recount
only after those gates pass. Do not count this private recovery as a match.

Reproduce under prepared WSL:
`python3 -m unittest tools.tests.test_game_map_edge_emitter_151050b0_recovery -v`.
Evidence: `conker/build/game-map-edge-emitter-151050b0-private/`; canonical C
and exact inputs are retained in the committed recovery manifest.
