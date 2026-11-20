# Note 2584: Randomized map-trail emitter guarded byte match

Date: 2026-11-20. Consumer baseline `3ac380eaa52f483c2053b7a632de06f4b85333ec`;
tools baseline `364bb77adbfa74249fdc2d940de0d0b0f9815da2`.
Qualified tools commit: `bd443a14d6d4a2dd7a6a2ac886bf97f384428110`.

`func_151058B4` is restored from GLOBAL_ASM to complete semantic C and matches
all **197 words / 788 bytes**, with the retail **240-byte frame** after guarded
normalization. Raw IDO C still emits 197 words with a **248-byte frame**.
**47 checked word/binding guards** adjust 39 frame/stack operands and permute
eight independent initializer words. There are no insertions or omissions;
150 words remain direct. This is a guarded C match, not a compiler-only match.

Production recount: **4,571 / 5,522 (82.78%)** total and **3,898 / 4,849
(80.39%)** Game, zero address drift and 951 different. Init 492/492 and
Debugger 181/181 remain exact. Converted functions: **5,522 / 6,048
(91.30%)**, 86.42% of bytes;
Game **4,849 / 5,327 (91.03%)**,
85.82% of bytes. One ASM row becomes C. The 85% goal
remains active; **123 more matches** at this denominator. Further ASM conversions
can increase the denominator.

## Interface and recovered behavior

VA 0x151058B4..0x15105BC8, ROM 0x132D64..0x133078, owner
`conker/src/game_131F30.c`. The void routine takes one observed record pointer;
the inline emitter is at +0x28. Its source pointer, floating scale, gate and flag
byte are recovered locally. Unknown packet fields keep measured offset names.
No shared headers, profiles, compiler binaries, callee bodies or original ASM
are changed. The local wrapper/type repair removes three false warnings and
preserves its exact instructions; two unrelated owner warnings remain.

The actual 27-word `func_15105848` wrapper narrows its command to a byte. Command
0x38 invokes the emitter and sets flag bit 0; 0x39 clears it. The unused second
wrapper argument remains unused. A ROM census finds one direct call in this
wrapper and no literal pointer or nearby same-register HI/LO materialization;
arbitrary computed calls are not excluded by that census.

The body checks the gate, derives a floating emission count from the RNG, global
rate/base and emitter scale, and emits while that count is strictly above one.
It initializes a 24-byte header and 60-byte packet, samples source geometry,
sets randomized bytes and duration, calls the direction helper with narrowed
angles and radius, reloads live scale/base and two record channels, submits the
packet, then decrements the remaining count. Cached range globals remain cached
across iterations; late globals, source and channel reads retain their lifetimes.

The direction member is a real `vertex`, passed as `vertex *` to the actual
`void func_15143794(s16, s16, f32, vertex *)` definition. Compiling that complete
definition with this declaration reproduces its production body. An intentionally
widened pitch declaration fails as incompatible. No ABI widening is accepted.
Sampler, trig and allocation providers remain bounded test contracts; this
does not qualify their complete unrecovered implementations or gameplay.

## Physical homes and source-derived guards

The earlier private refinement in [Note 2583](2583-game-map-trail-emitter-frame-provenance-and-private-refinement-20261120.md)
had helper pointers eight bytes below retail and seven padding differences.
Moving the two integer declarations after scratch, and loading cached scale
before base, gives the selected source the **literal retail entry-relative
homes**: bottom -104, top -100, packet -96, direction -92, header -36 and header
Z -28. All 24 header and 60 packet bytes now agree, including their seven
uninitialized padding bytes. Padding is deliberately not filled with invented
values. The old warning against an unqualified frame patch is superseded by
these physical-home gates and the complete relation below.

The raw frame contains an unused eight-byte gap at entry-relative [-128,-120).
The normalizer verifies the exact 197-word source hash and every binding, rejects
gap accesses, derives 39 SP/frame operands and carries relocations with an
eight-word initializer permutation. It contains no replacement retail-word
array. Raw SHA-256:
`676ad38411e9dcd2c89753905e5f5262d28dee85c7a80920445b217f11bc134a`.
The raw source's saved/outgoing homes use a canonical +8 correspondence; exposed
objects keep their literal physical addresses. The retained unreachable BREAK
at offset 0x1C4 is pinned, not executed or removed.

This uses the established guarded-frame method from
[Note 2543](2543-game-amplitude-terminal-callback-guarded-byte-match-20261118.md).
Raw compiler output still differs in frame and public read scheduling. Its
fault state, instruction PCs and hardware acceptance are not claimed equal.
The installed guarded stream is independently equal to all 197 original words
and relocations, including the original access order.

## Qualification and production

- Nine fresh tests pass in primary tools and the **997-file isolated
  sibling overlay**. The real dirty sibling's HEAD, raw status and 343 dependency
  hashes are preserved. Overlay origins: 341 equal sibling, 647 explicit primary
  fallbacks, eight task files and one bootstrap. All imported Python dependencies
  are hash-paired. Both copies rerun two focused installed tests; other unchanged
  native/caller/rebase/negative receipts are explicitly reused. `make tools-check`
  passes.
- **140 cases per retail/raw/guarded stream** visit 196 reachable words, preserve
  saved ABI registers, helper order, public state, all packet bytes and physical
  helper pointers. Raw public read order differs in 68 cases within quiet ordinary
  nonfaulting epochs; guarded order differs in zero. **40 cases per stream** run
  the original wrapper, including commands 0x38/0x39/0x37/0x138.
- Actual SDK32 C at **O0/O2/O3 each passes 68 finite cases and 54 wrapper cases**,
  strict aliasing and UBSan. Eight compiled semantic mutations fail at runtime.
  Native C compares defined bytes; complete padding uses guest/symbolic evidence.
- The complete loop-inductive relation checks **three prefix paths and two
  arbitrary iteration/exit paths**, all 196 reachable words and the pinned dead
  BREAK. It compares 264 canonical private/incoming bytes, full packets, ordered
  FP/FCSR operations, public aliases and arbitrary public/retained-exposed-range
  provider writes. The raw gap is never accessed; saved registers, return link,
  live loop roles and stack restoration agree. Ordinary memory is stable inside
  each quiet epoch; every public store/call invalidates that epoch. Providers
  cannot inspect implementation PCs or unpassed locals. This is normal-execution
  source/ABI equivalence, separate from raw exception or hardware acceptance.
  **13 effective mutations** challenge semantic constants, FP order, saved homes,
  private pointers, frame-only changes, the gap and partial permutations.
- All **197 source-word and 25 binding corruptions** fail the closed normalizer.
  **188 stale guard tests** exercise every row's expected word/binding through
  both real padders. Eight independent GNU links cover four rebases with low
  halves 0/0x7FFC/0x8000/0xFFFC. Both complete-owner padders and the actual five
  command mixed C/ASM Make route agree, preserving ten neighbors and pools.
- Actual production Make passes in **348.53 seconds**. The production owner
  object and entire ELF equal the independent prediction: **zero changed bytes,
  zero exclusions**, all 6,051 named function bodies/extents/addresses and 189,088
  protected data bytes across 720 owners unchanged. All **2,047 frozen inputs**
  are audited except declared source/guard/conversion/docs changes. Four full-image
  corruption controls fail. ELF SHA-256 remains
  `d3eeddd84c1cd3c6c0877467dfdf37015677dc0a81885ea7f5ed6d528b2f352d`.

Tools are committed before the consumer source, guard rows, docs and gitlink.
Root README changes only aggregate status rows and snapshot date. No push,
host/save change or frozen Release operation occurs. One bounded Claude advisory
attempt returned an expired-token error with zero model tokens; no advisory
analysis was returned or used. Account settings were not changed.

Graphify runs after adoption and retains prior IDs in the scoped AST merge,
linking the manifest to the installed C definition and marking original ASM
historical. Post-commit producers are observed to completion before final sealing.
This is not a full-corpus semantic extraction claim; exact graph receipts remain
in the ignored target packet.

## Resume

Next remaining ASM in this owner is `func_15105C24`, starting VA 0x15105C24 /
ROM 0x1330D4. Its opening instructions inspect the two-by-two record chains at
`D_800DCE50` indexed through `D_800A5770`, compare object type 0x2E and its +0x28
field, and return a matching pointer. Only the opening was inspected here;
caller/type/full-body qualification and matching remain open. No credit for it.

Reproduce the installed target suite under prepared WSL:
`python3 -m unittest tools.tests.test_game_map_trail_emitter_151058b4_match -v`.
Transient source, immutable input copies, both suites, production receipts and
the current handoff are under
`conker/build/game-map-trail-emitter-151058b4-storage/`.
