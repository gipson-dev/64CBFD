# Surface-impact query and descriptor recovery - 2026-11-18

`func_150B9ED0` now has a complete, tested **private C recovery**. It is **not
installed or credited**: the candidate emits291 words /frame328; retail is291
words /frame344. Both streams have33 symbolic binding sites. Equal length does
not establish a byte match, private-frame identity or safe normalization.

Production remains the checkpoint from [Note2549](2549-game-cached-target-terminal-callback-guarded-byte-match-20261118.md):
**4,551 /5,514 (82.54%)** total, **3,878 /4,841 (80.11%)** Game, Init492/492,
Debugger181/181, zero drift,963 different. **136 more matches** reach85%.
These are the retained actual production recount, verified against unchanged
ELF/source/CSV/progress inputs; no new production recount or matching credit
is claimed for this recovery. The root README remains byte-for-byte unchanged.

Starting commits: consumer `b2c40e35666bdfaa0cd9d206f944927edcc6da8f`, tools
`db6110022bf0265c12e3dc005f92d36d561ae49b`. The new baseline verifies1,781
previous committed inputs and additionally freezes the owner C/assembly, the
actual caller assembly and the integrity-window assembly: **1,785 inputs**.
All remain exact. Snapshots are copied bytes with immutable predecessor
references, with no live hardlinks. The prior goal turn made concrete progress
by installing and committing the438-word cached-target callback.

## Function, ABI and retained behavior

Owner `conker/src/game/generated_E7380.c`, original `conker/asm/E7380.s`;
VA150B9ED0..150BA35C, ROM E7380..E780C, **1,164 bytes**. The production owner
still contains its old zero-return placeholder. The recovered declaration is
`void func_150B9ED0(u8 *point, f32 oldX, f32 oldZ, u8 mode, s32 tag)`.

The prepared image contains one direct JAL, at15058BF8 in `func_15058898`, and
no aligned literal pointer to this address. This is a scoped census, not a
proof against every possible indirect address construction. The genuine caller
passes the actor pointer, old X/Z float bits, mode255 and tag0; it ignores V0,
reloads its float temporaries and actor flag, then performs its cleanup stores.
The25-word window15058BC0..15058C24 is executed in the focused caller tests;
the full caller remains unqualified.

The recovered routine preserves:

- The null pointer return and the complemented-word integrity sum over the26
 words at151E7EF8..151E7F60. Retail and current production both sum to3843095E;
 mismatch sets D_80084060 to255, while success preserves its prior byte. The
 original check and failure write remain intact.
- Subtype2 then subtype1 position gates, each independently reloading X/Y/Z,
 truncating to signed32 and narrowing to signed16. Helper mutations between
 calls are observed. The tests keep conversions within the valid signed32
 domain, while including signed16 wrap boundaries.
- The15-argument surface query: current position with Y+80, negated X/Z deltas,
 positive-zero vertical delta,18-byte context, three output floats, hit word,
 null optional output and zero trailing controls. The deltas remain snapshots
 across later provider mutations.
- Optional category6 burst after the hit predicate, unsigned random remainder
 operations modulo51 and101, exact random/real-provider order, two scaled
 floats, selected random bits and all mode/tag arguments.
- The unconditional category7 spray after a successful query, late position,
 context and seven constant reads, negated delta components and a negative-zero
 vertical component. Unknown fields retain offset names and explicit widths.

The first descriptor is40 bytes, with32 explicitly initialized and eight left
untouched; the spray is116 bytes, with110 initialized and six untouched.
Context is exactly nine halfwords. The C uses local typed structures with
explicit reserved ranges; it does not clear retained bytes or infer names for
unknown fields. Three neighboring functions and normalized pools remain exact
under complete copied-owner compilation. No shared declarations or compiler
profile, production source, assembly, guards, object or ELF are changed.

Selected unbound C text SHA:
`6fea10f66b291d71da733ba9d0ec380e9261963522e5bac60a22e3c49a287e12`.
The `game_surface_impact_150b9ed0_screen`/`_manifest` tools retain this body,
declarations, binding map and qualified compiler fingerprint. The private
`conker/build/game-next-150b9ed0-private/` packet retains the source-shape
screens and the authoritative final-primary/final-sibling receipts.

## Fresh qualification and its limits

Both final configurations pass **four tests**, zero failures/errors/skips:
**114.096s primary /142.293s private sibling overlay**.
Each observed import is fingerprinted: **316 primary /
316 overlay tool files**. The overlay contains
820 files: 339 matching sibling copies,
474 primary fallbacks, six task artifacts and
1 empty package bootstrap. The real sibling is preserved;
this is not a claim that its conflicting pending edits were overwritten or tested.

1. Complete before/after owner compilation, unchanged three neighbors/pools,
 all291 input words and33 binding sites, independent GNU original assembly and
 original-ROM binding, plus the direct-caller/integrity census.
2. **1792 guest cases per stream**, visiting **all291 words** in each.
 Complete40/116-byte descriptors and untouched bytes, ordered helper arguments,
 public memory, all256 mode bytes, randomized unsigned values, signed-zero
 deltas, provider mutations and saved GPR/FPR/SP/RA custody are compared with
 an independently written behavioral model.
3. **576 actual caller-window cases** across both streams, enabled/disabled
 and category branches, mode255/tag0, ignored return, float/flag reloads,
 stack and saved actor pointer, and post-call cleanup.
4. **1024 SDK32 native C cases each at O0/O2/O3**, strict aliasing,
 no fast math and UBSan. All32/110 initialized descriptor bytes, ordered helper
 arguments and public outputs agree with independently retail-executed
 transcripts. Unwritten native bytes are intentionally unobserved. **Ten
 effective negatives** reject checksum, gate subtype, direction, duration,
 color, random-byte mask, negative zero, late constant, mode and tag mutations.

The initial interpreter lacked NEG.S; its target-local implementation flips the
sign bit and is exercised by signed-zero cases. The native debug launcher first
failed an optimized aligned SSE store; GDB identified MOVAPS with a misaligned
stack. Applying the existing native harness's `force_align_arg_pointer` entry
convention made O0/O2/O3 pass. Earlier rejected/debug receipts are retained;
the final paired receipts use the corrected, sealed six task files.

This establishes finite public behavior and named descriptor agreement under
the specified nonoverlapping objects and opaque-service contracts. It does
**not** establish complete raw private-frame identity or an all-input symbolic
relation. Arbitrary private aliases, raw FCSR exception flags/traps, NaN payloads,
asynchronous effects, fault prefixes, full deep services, full caller and gameplay
remain outside this stage. Native code-symbol aliases supply the frozen26-word
integrity fixture; they do not inspect host executable instructions.

## Matching boundary and continuation

Do not install this source, add guards or increment counters on these receipts.
The selected source is291 words /frame328 versus retail291/frame344, with real
stack-role, scheduling and FP-allocation differences still open. Six meaningful
source shapes were screened; integer zero fields and a shared zero recover the
retail count without dummy locals or guessed volatility.

Continue the same function:

1. Freeze the six newly committed tools in addition to this1,785-input baseline.
 Establish the complete private/frame correspondence and saved-role lifetimes,
 including query outputs, random/real temporaries, both packets and untouched
 frame ranges. Retain the actual caller and explicit FP/alias boundaries.
2. Recover the original source layout or derive only justified instruction,
 frame, register and scheduling changes from the compiled semantic source.
 Verify all291 words and33 symbolic bindings independently; equal length and
 finite public cases alone are insufficient.
3. Qualify both actual padders, rebases and effective word/binding/guard controls,
 relevant connected services, actual Make and an independent strict full-image
 prediction. Add no blanket metadata/data exclusions.
4. Only then install, rebuild production, audit all other bodies/addresses/data,
 run installed checks/recount, update aggregate README rows and bank tools first.

Native Graphify update exited1 after refusing a27,136-node replacement
of66,509 nodes, retaining the old graph. Scoped AST/target references and old-ID
retention are recorded separately; no forced or full-corpus extraction is claimed.
Routine work uses zero Claude calls and no REA/WSL reconfiguration. Real sibling
HEAD/status and343 dependency hashes, retained host captures, frozen Release and
real saves remain protected. Tools are committed before the consumer; no push or
automatic pause. The85% total matching goal remains active.
