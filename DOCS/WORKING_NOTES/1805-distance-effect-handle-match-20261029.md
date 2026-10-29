# Distance-scaled effect handle: direct C match

Verified 2026-10-29. `func_150E3208` replaces its zero-return placeholder in
`conker/src/game/generated_1104D0.c`. Its complete 50-word, 200-byte routine
emits directly from semantic C with the original 64-byte frame and two call
relocations. No guards, inserted instructions, alignment words or global
declaration changes were needed.

The adopted live ELF recount is **3,883 / 5,506 (70.52%)** byte-exact C
functions: Game **3,210 / 4,833 (66.42%)**, Init 492/492 and Debugger 181/181.
There is no address drift; 1,623 C functions still differ. The 75% target is
4,130 exact functions, leaving **247**. Conversion inventory is unchanged.

## Recovered behavior and interface

The eight signed word arguments are start coordinates, target coordinates,
effect kind and duration. Coordinate differences wrap as the original MIPS
`subu` instructions do; explicit unsigned subtraction followed by signed
conversion avoids C signed subtraction overflow. The original distance helper's
signed result and duration are each converted to single precision before
division. The effect constructor receives the six coordinates, full-width kind,
computed step, five zero arguments and the signed halfword sentinel `-99`.
Allocation failure returns zero; success reads unsigned byte `effect[0x48]`
and returns its one-based value, including 256 for a byte value of 255.

The existing constructor declaration returns `s32`, carrying the original
32-bit pointer bits. This recovery preserves that shared interface and casts
locally. Its provider C body remains a placeholder. This is a wrapper recovery,
not credit for the constructor or the still-unrecovered parent dispatcher.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x150E3208..0x150E32D0` |
| Retail ROM range | `0x1106B8..0x110780` |
| Owner | `generated_1104D0`, 13 compact functions |
| Call at byte 56 | `R_MIPS_26 func_150AD9A0` |
| Call at byte 160 | `R_MIPS_26 func_150E3020` |
| Raw object body SHA-256 | `072a85ec46680ef18bc685071b757919036858417359cd9cd93901a9d268fab0` |
| Retail slot SHA-256 | `f05c57c0a55d4ca2360ba20446d4f9ce5f93f45685e9d27d1e1aae129bd0da2d` |
| Adopted ELF SHA-256 | `1ff94fdfa879efa06f48b04185843032be078ab7cf312289e8a3e347e25b4093` |

## Qualification

The private suite and both independent tools copies pass all eight methods;
shared project-tools checks pass in both copies. Production reruns the two
installed-source/image checks per copy and reuses six semantic checks only
after verifying the complete input, module and artifact fingerprints.

- 619 direct guest cases cover every instruction, every output-byte lane,
  signed word boundaries, wrapping coordinate differences, duration zero,
  single-precision rounding, both allocation results and late incoming-home
  reloads. Legal volatile-register and outgoing-home clobbers occur at calls.
- 563 connected cases execute the original 32-word handwritten distance helper
  and original 122-word constructor with a bounded allocator. All 32 distance
  words and 118 reachable constructor words execute. The four duplicate words
  at `0x150E3184`, `0x150E31A4`, `0x150E31C4`, `0x150E31E4` are unreachable
  through the original branches and remain intact.
- The distance helper retains trapping signed `sub` and `add` semantics.
  Five overflow cases cover each `INT_MIN` absolute-value operation and both
  sum operations, including two delay slots. Comparisons cover registers, RAM,
  PC and delay prefixes; they do not claim CP0 exception-entry emulation.
- All 256 occupancy patterns and allocation failure are checked for the
  constructor's eight slots. A full table leaves the allocated pointer intact,
  writes slot byte zero and returns handle one without inserting a table entry.
- The only aligned retail `jal` occurs at ROM `0xCAA40`. Twenty-four cases
  execute its original 19-word caller window at `0x1509D564` through the
  returned-handle encoding, `(handle << 6) | 0xE004`, with zero on failure.
  The parent `func_1509D180` remains a C placeholder; no current C caller edge
  is invented from this original assembly evidence.
- Native32 SDK builds pass 617 vectors per profile at `-O0`, `-O2`, `-O3`
  with trapping UBSan, valid backing and object canaries. Floating tests use
  default rounding with masked exceptions; NaNs are compared by classification,
  not architecture-specific payload. FCSR and hardware exception behavior are
  outside this test scope.
- Eleven compiled wrong implementations are rejected by observable arguments
  or results. The same controls fail native tests. There are 428 guest access
  fault-prefix pairs, including 38 delay-slot cuts. These prove emitted access
  order, not portable C fault behavior.
- Original, selected and actual-Make objects link identically at three GNU
  layouts across 48 cases. All 50 word corruptions and both binding corruptions
  are rejected; eight whole-image corruption controls are rejected.

The first private test run exposed missing XOR and floating-negation support
in the reused bounded emulator, not a candidate mismatch. Local oracle support
was completed and the full suite rerun successfully before tool installation.
No candidate source tuning or production compiler changes were required.

## Build, preservation and commit boundaries

Full-owner before/after compiles and the actual three-command Make rule agree
with the selected object. All twelve neighboring functions, their relocations
and normalized pools are unchanged, with no compiler diagnostics. Production
reproduces the previously qualified private image.

Independent whole-image prediction permits exactly **158 changed bytes**:
157 in the target slot plus one symbol-size byte. There are no metadata moves
or exclusions. All 6,056 disassembled function addresses and 6,055 other bodies
are preserved. All 189,088 protected Game data bytes across 720 owners,
the complete guard CSV and the conversion inventory remain unchanged.

469 focused inputs and 16,533 sealed current inputs are verified. The older
standalone tools mirror keeps its 1,856 inherited dirty paths plus the three
new qualification modules; it is not committed or reset. Tools are banked
first in `ea50dff042e50680f7c31063bd135332f03413bb`; the consumer commit
contains this source, tools pin, this note and measured documentation only.
No push or sibling host/Release changes are part of this work.

Ignored receipts live in `conker/build/game-distance-effect-handle-match/`.
After the consumer commit, `FINAL_AUDIT.json`, `BANKED_STATUS.json` and the
banked input seal record the independent final audit. The graph refresh is
limited to the eleven changed source/document/tool files, with old-node and
directed-relationship retention checks. Historical global analytics are not
recomputed or represented as fresh full-corpus extraction.

## Next work

Inspect `func_15131C84` in `generated_15D730.c`, the next 50-word placeholder
in the measured queue. Reconstruct its ABI and original caller before giving
it credit. `func_1514E920` remains parked and uncredited. The 75% goal stays
active; all future candidates must pass the same adoption and recount gates.
