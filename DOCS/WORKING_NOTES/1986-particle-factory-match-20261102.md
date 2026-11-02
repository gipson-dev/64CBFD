# 1986 - Particle factory recovered as guarded C

Verified 2026-11-02. Production **4,053/5,507 (73.60%)**; Game **3,380/4,834
(69.92%)**, Init 492/492 and Debugger 181/181. Zero address drift, 1,454
different; one new installed match and unchanged C inventory. The active
goal is now **80%**: ceil(0.80 * 5,507) = **4,406**, requiring **353 more**.
Earlier notes retain their historical 75% target. This checkpoint is progress;
the goal remains active.

## Interface and recovered behavior

`void func_15152520(ParticleFactoryInput *input, u8 mode, s32 extra)` replaces
the zero-return placeholder in `conker/src/game/generated_17CAF0.c`.
Original `17CAF0.s`: VA15152520..15152874, ROM17F9D0..17FD24, 213 words,
256-byte frame, sixteen helper-call bindings. The byte formal reproduces
retail's low-byte mask while retaining the full incoming A1 home store.
The original caller passes the 120-byte payload described in Note 1985.

The factory initializes descriptor fields, colors, position, state property
and a cached state coefficient before the first integer RNG call. It then
reads live count fields and computes unsigned baseCount + RNG % (range+1).
Each iteration chooses a signed-halfword lifetime, three float rotations,
two signed-halfword angles and a spherical vector, velocity components and
two more randomized scalar fields. Explicit RNG temporaries preserve integer
call order; input fields remain live across providers. Nine spawn arguments
include the mode byte and complete extra word. A failed spawn does not stop
the remaining iterations. Unknown gameplay meanings retain offset-based names;
the state word at +0xC is `fieldC`, not an inferred radius.

The actual `func_15157898` interface returns s32, takes the encoded descriptor
address as s32, a complete scratch pointer as void*, and five further scalar/
pointer arguments before the mode and extra arguments. Production providers
remain their existing implementations; test providers do not replace them.

## Complete scratch extent and checked normalization

`ParticleSpawnScratch` contains a 52-byte state followed immediately by an
88-byte descriptor, total 140 bytes. The retained spawn wrapper copies **56
bytes** from the state address into child+0x120. This includes twelve float
words, one property byte, three untouched padding bytes and the descriptor's
first four bytes. Passing the complete scratch object preserves that extent.
Descriptor initialization defines 76 bytes and leaves twelve untouched.
Native checks never read uninitialized padding. Guest checks seed and compare
all bytes, including padding and the descriptor overlap in the copied tail.

The selected source emits 213 words/frame256. Its scratch begins at SP+0x74,
descriptor at SP+0xA8; retail uses SP+0x70/SP+0xA4. **66 expected-word guards**
close this four-byte private-object shift, register roles and commutative FP
operand order. These are checked normalization, not direct compiler matching.
No instruction is inserted or omitted; the frame, saved bank, branch targets,
all sixteen call offsets and relocation bindings stay fixed. Every appended
guard checks its original word; inherited CSV history is retained verbatim.

Raw payload SHA256:
`b93dae5d275ed5c49b0cea927bb1c02c75d4230e095dac75f6715e6b2a27eda7`.
The symbolic interpreter independently walks both instruction streams and
closes 132 ordered observations, sixteen callsites, six branches, saved roles
and the loop backedge under a single logical scratch mapping. Raw padding
requires a corresponding logical scratch seed. FP operand exchange is
qualified for finite operands/intermediates and default single rounding;
this is not an unrestricted NaN/FCSR equivalence claim. Four division traps
are retained and unreachable in the defined tested input domain.

Original, raw and normalized objects are independently GNU-linked at three
code/helper layouts. All 852 original/normalized bytes agree at each layout.
Fresh compilation pins the complete raw payload and every binding; guard,
binding and whole-image corruption controls reject changes.

## Fresh qualification

- Standalone guest: 192 cases / 576 executions of original, normalized and
  raw code; all 209 non-trap factory words, 732 spawn snapshots, 504 complete
  56-byte copies and 657 access-prefix triples. Original and normalized full
  states agree. Raw outputs, calls, packets, saved roles and translated access
  traces agree under the declared scratch mapping. Live input changes after
  the first RNG are distinguished from fields cached before it.
- The actual retained 32-word spawn wrapper and 11-word memcpy execute all
  43 words, including allocation success/failure and provider mutations of
  descriptor flags, state property and explicitly written padding. Allocator,
  RNG and spherical-vector outputs remain scripted providers; no gameplay
  acceptance is inferred from these tests.
- The aligned-ROM census finds one JAL, ROM1C0C8C / VA151937DC, and no aligned
  tail jump or literal target pointer. The complete original 101-word caller
  and retained 49-word point resolver execute across 768 cases / 2,304 runs;
  192 enter the factory. All caller gates, byte modes, extra0/1, fixed/float
  matrix paths and connected spawn/copy checks pass.
- Native32: 352 cases per O0/O2/O3, UBSan, finite-intermediate checks and ten
  effective controls per profile. These cover all 256 mode bytes, late RNG
  input mutation, cached prefix fields, unsigned random arithmetic, lifetime,
  angle, color, radius-input and extra fields, and continuing after failed
  allocation. The complete typed scratch is checked; undefined padding is
  excluded until a provider explicitly writes it. Guest home probes and
  padding correspondence are not claims about portable C behavior.

Both tools copies pass five fresh focused methods and the shared tools check.
The production installation repeats two compile/image methods per copy;
semantic checks are explicitly reused with unchanged source/code/preparation
fingerprints. A transcription error in a draft verifier was caught by the
fresh comparison and corrected before installation; the private candidate
and production guard rows were unaffected.

## Actual build, image and bank

All 40 raw and padded owner neighbors and their pools remain identical; the
owner compiler has zero diagnostics. The
actual owner recipe has **five commands**, including GLOBAL_ASM preprocessing
and postprocessing; its object equals the qualified 29,244-byte object.
The complete-image predictor replaces exactly the target's 852-byte slot and
symbol extent12->852, with no metadata permutation and zero exclusions.
All 6,052 function addresses, 6,051 other bodies, named definitions, 189,088
protected bytes and 720 data owners remain fixed. The complete map agrees.
Actual production Make and a separate Native-mounted ELF recount agree.
Before notes, all 17,816 prior sealed files were checked; only the target
source, object, guard CSV and ELF changed. No unplanned dependent object.

Linked ELF SHA256:
`6ae9f23a08f217174eaf205953426224966321f4d8769900dfd599bb7417dd4e`.
The stage is `conker/build/game-particle-factory-15152520-match/`, with thirty
canonical artifacts and 1,126 focused inputs. Current commits, Native/cache
seal and Graphify retention proof are recorded in BANKED_STATUS.json,
FINAL_AUDIT.json and HANDOFF.md. Tools are committed before the consumer pin;
no push. The older tools mirror's inherited dirty state is preserved.

The graph refresh is twelve-file AST only, zero LLM tokens. All prior nodes
and valid edge occurrences are retained; the obsolete s32 placeholder return
edge is explicitly archived. This is not full-corpus extraction or global
reclustering. README changes are aggregate rows only. Detailed recovery stays
here with concise links in the five indexes. No Claude calls were needed.

## Next step

Audit adjacent `func_15152874`, still a zero-return placeholder in the same
owner: 146 words / frame144, ROM17FD24..17FF6C. Recover its ordinary C, actual
caller ABI, random sequencing and outgoing descriptor before qualification.
Private exact words alone do not count; require guest/native/caller, raw and
padded neighbors, actual Make, complete image, production recount and docs.
Keep the 80% goal active and preserve the archived build checkpoints and four
restored small embedded-oscillator fixtures.
