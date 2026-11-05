# Fractional burst emitter directly recovered

Date: 2026-11-05. Target `func_151A0AF8`, owner `generated_1CC440`.
Source `conker/src/game/generated_1CC440.c`; original `conker/asm/1CC440.s`.

## Outcome and recovered layout

All ten pre-install checks pass in **55.723 seconds**. The ten fresh installed
checks pass in **48.308 seconds**.
Actual Make and independent complete-image prediction agree byte for byte.

The qualified C emits all **69 words / 276 bytes directly**, with the retail
96-byte frame, six bindings, no alignment tail and no guards. Both compact
and padded owners preserve all **38 neighbors**, their bindings and normalized
pools. VA is `0x151A0AF8..0x151A0C0C`; ROM is `0x1CDFA8..0x1CE0BC`.

The recovered interface is `void(FractionalBurstEmitter151A0AF8 *record)`.
The local type is 0x3C bytes: context at `+0x0C`, payload coordinates at
`+0x28/+0x2C/+0x30`, unsigned tag at `+0x34`, and phase at `+0x38`. The
embedded payload starts at `+0x28` and is 0x14 bytes. Native compile-time
checks verify these offsets and sizes. Shared headers/profiles are unchanged.

## Fractional phase and explicit helper sequencing

The routine adds the single-precision product `D_800A8D10 * D_800BE9A4`
to phase. The original increment factor is `0x3E333334`. Phase must be
strictly greater than one before entering the emission loop. Each iteration
draws a new `func_150ADA68` value, rounds its multiply by25 and addition of15,
then reads the current coordinates, tag and context for `func_1514C678`.
Only after that helper returns does it reload phase, subtract one, store it
and test the strict greater-than-one loop condition again.

The first inline-random expression already matched all69 MIPS words, but a
native O0 witness found C argument-evaluation ordering mattered: case7's
first emitted tag was7 while the post-RNG mutation required128. GCC could
read tag/context before evaluating the nested random call. The final body
computes an explicit `f32 magnitude` before the submission expression.
This guarantees the intended source order and still emits the identical
69-word body and raw hash. Both magnitude-local and sample-local screens
match; only the magnitude-local form is adopted. No ordering guard is needed.

The twelve submitted arguments are X/Y/Z/magnitude, signed-halfword bounds
0/255, signed-halfword count5, byte kind4, the zero-extended tag as a full
word, positive-zero float, null data pointer and unsigned context byte.
Each iteration rereads fields after RNG mutation and reloads phase after
submission mutation. Incoming-home overwrites do not replace the state
pointer retained in S1. F20/F22/F24/F26 preserve 1/25/15/0 across helpers;
their original paired saves and restores are literally matched.

## Registration, original caller and connected helpers

A complete aligned retail-word census finds no direct JAL or tail jump and
one address literal, ROM `0x22EFAC`, VA `0x8008A4EC`. The target occupies
slot1 of the **98-entry** `D_8008A4E8` table in `22EF80.rodata.s`. Its declared
words end at `0x8008A670`.
The initial fixture's inferred104 count is corrected to this measured98.

The full original **45-word `func_15149264` caller** is connected from
ROM `0x176714`. Its existing source is `game/done/game_1765E0.c`. It applies
the optional signed-halfword lifetime decrement, skips callback index-1 at
record `+0x11`, dispatches table slot1, and handles expired destructor/release
routes. Two poisoned callback-return values confirm the void interface.
Destructor and release effects are bounded providers; full heap reclamation
and unrelated destructor behavior are not claimed.

The original **25-word float RNG** is connected with its full 64-bit seed
updates. Its scale is the measured **`0x37800080`**, not an assumed exact
1/65536. Twelve seed patterns include zero, high-word and 64-bit extremes.
The fixed RNG scale is checked directly against retail data.

The original factory prefix is also connected through the branch to
`0x1514C700`: a 34-word source prefix, with26 words executed on the submitted
0/255 path. It proves the 160-byte callee frame, four float inputs and three
signed-halfword inputs, including count5 in S5. Remaining packet words are
checked at the caller boundary. The complete factory is not qualified here.

## Focused semantic and alias qualification

The ten-test suite provides these distinct receipts:

* **2,664 guest cases per body** cover strict phase boundaries, signed zero,
  NaNs, negative infinity, multiple emissions, every tag/context byte, seven
  random-value patterns and all32 provider mutation modes. All69 words are
  visited, with independently rounded arithmetic and exact public packets.
* **490 alias/private cases per body** cover all15 aligned record locations
  for each global, both stack phases, live helper mutations and70 private
  layouts. Eighteen deliberately destructive private cases overwrite a
  saved S0/S1/RA byte through the context field. Both bodies reach the same
  exact corruption boundary and complete state; normal ABI return is not
  claimed for these intentionally overlapping inputs.
* Positive infinity and phase33554432 each retain their value after subtracting
  one. Both bodies match prefixes of eight emissions; these are bounded
  observations of stalled phase, not successful termination or a source limit.
* **480 connected original-RNG cases**, **192 full original-caller cases**
  and **378 connected factory-prefix cases** qualify the interfaces above.
* **156 fired access-prefix cuts** compare complete registers, RAM and
  ordered traces. An inactive record completes with unused coordinates,
  tag and context bytes unmapped.
* **Nine independent GNU links** compare original assembly, compact C and
  padded C at three layouts. All six bindings, both global HI/LO carry edges
  and **72 rebased cases per body** pass.
* Native32 O0/O2/O3 pass **12,288 positive executions**, with direct/typed
  calls, live helper mutation, complete twelve-word packets and four valid
  float-field aliases per global. Reserved/guard bytes are preserved. UBSan
  is enabled and FP contraction is disabled. Native NaN outputs are compared
  by value classification; guest retail/C state remains literally equal.
* Twelve native controls and twelve independently compiled IDO controls
  reject threshold ties, inverted increment, wrong decrement/scale/base,
  signed tag, wrong context/axis/count, cached coordinates and reused RNG.
* Every changed raw target byte, six bad binding substitutions and four
  independent whole-file corruptions are rejected. No target guard row exists.

Fixture corrections are separate from the source-order recovery. The shared
initializer resets its own `limit` attribute, so the test uses a dedicated
`emission_limit`; the freestanding native fixture defines `NULL`. Private
saved-register corruption is an expected boundary. The factory's actual
0/255 branch reaches `+0x88`, and a nonzero-step witness makes the inverted
increment control effective. No shared oracle or production guard is changed.

The shared nineteen padder, relocation, matcher and protected-layout checks
pass in **6.355 seconds**, and `make tools-check` passes. Unchanged neighbor
suites are reused through verified byte/binding/pool identity rather than
claimed freshly executed. No FCSR, hardware or gameplay acceptance is claimed.

## Immutable inputs and complete production image

The private snapshot freezes **97 files**, including all headers, source,
object, ELF, code binary, retail input, original target/helpers/registry,
caller source, increment data, guard history, layout, Makefile, linker,
progress and graph. Artifacts are in
`conker/build/game-fractional-burst-emitter-151A0AF8-match/`, with adjacent
source-order screens. The original generated-owner padder is used unchanged.

All **6,052 function addresses** remain fixed; only the target body changes.
All **189,088 protected Game bytes across 720 owners** remain exact. The
literal complete-file prediction changes only the target slot and symbol
extent: **213 bytes**, zero exclusions, no symbol/string serialization
correction and no metadata substitution. Production owner and complete ELF
equal their independently qualified artifacts.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `53d625fe8e86c6ec0c05a1492287511ea09fc738c1fb9001b4e1496da89c599e` |
| Retail target | `3ce4e70dbc436d32c9ba1c3a5647d05b8a13f407134da0ccdb5e3d1b0d416f56` |
| Frozen predecessor ELF | `de83c495f3f7ba430fe8d252ad09111059fc6969d4c41f28cebc652169bba20f` |
| Qualified padded owner | `0d21815369ae3a2272c447879dd59ed1a630712068eb145eaafeb07097328934` |
| Production complete ELF | `2b159614d3d148da67218b70c03f8caa8e463dc23b675257e2c84325bdd5e5f9` |
| Production code binary | `1634ed3761a1f8e6f81588d6152830fd6608826d98d7694548a52eb25d2044a7` |
| Unchanged guard CSV working bytes | `87a70532340ab80357051ae8b6e0b77d09b65d08c2af717f3b1cf32b35e8b3ce` |

The guard manifest's bytes and modification time are unchanged. Frozen
headers, retail input/assembly, layout, Makefile and linker are unchanged.
The predecessor and candidate owner produce no compiler diagnostics. Actual
Make retains the inherited duplicate `generated_12D630` recipe warning.
`make -C conker all` creates the code binary and returns2 solely at the
expected overall retail SHA mismatch for this incomplete decompilation.

## Baselines, progress and continuation

Main baseline: `899a2f687c829058715a4e7db8b752179f176777`. Mounted tools
baseline: `ec88172bbd701baff707b2be613531ad87a230f6`. Both start clean.
The separate sibling tools checkout is freshly checked at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with six tracked changes and
2,428 untracked files. It is untouched; no fresh sibling qualification is
claimed. No host-port or frozen Release changes are made. Routine work uses
zero Claude calls. IDO/GNU tools are used under the documented Windows REA
MIPS-adapter limit, without repeating configuration setup.

The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,170 / 5,512 | 75.65% | 0 | 1,342 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,497 / 4,839 | 72.27% | 0 | 1,342 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory stays 5,512/6,046. Root README edits are aggregate rows
only. The 80% threshold is 4,410/5,512, leaving **240 more** exact functions.
Fresh ranking selects `func_151DCDE0`, 68 words and65 real differences, as
the next ordinary target. Keep `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC` and
`func_150A6760` as the separate documented boundary cases. Keep the wider
80% goal open. Tools-first commit and graph retention receipts follow.

Mounted tools are committed first as
`5fb79574c85c98e288ac889f165eaabc1ff8a1b1`
(`test(game): qualify fractional burst emitter sequencing`). The consumer
includes that pointer, the sequenced typed C and documentation. The final
native helper rerun also passes O0/O2/O3 after fixture cleanup.

The standard Graphify update refused a reduced 24,930-node extraction
against the existing 58,723-node graph, preserving the larger graph. The
seven-path scoped refresh retains 58,720 old nodes and relocates three
existing `DOCS/UPDATE_LOG.md` headings. It adds this note's file node and
seven headings plus the `FractionalBurstEmitter151A0AF8` type reference:
58,732 nodes, 112,488 links and 5,135 communities. No node outside the
changed paths is removed. The retention receipt records SHA-256
`9b6e9ff2c82d13ce881ad604db07a4a6779db5a911618e7ce634b66b5b74bbe3`.
The 31,816 retained nodes from 3,754 still-existing files outside the current
scan corpus are preservation evidence, not a fresh full-corpus extraction
claim. This AST-only refresh makes no LLM calls. The ignored
`graph-retention.json` receipt is retained in the qualification directory.
