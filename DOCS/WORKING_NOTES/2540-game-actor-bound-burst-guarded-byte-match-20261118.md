# Actor bound burst guarded byte match - 2026-11-18

`func_150B7B40` is restored from its zero-return placeholder to a complete C
actor-bound burst/ground-effect/two-endpoint spray routine. Its installed
**484-word /1936-byte retail slot is byte-exact**, with the original616-byte
frame. The C compiler emits483 words. **330 relocation-aware expected-word
guards and one inserted setup word** reproduce retail's allocation and schedule.
This is a guarded C match; the C body does not emit all484 retail words directly.

Fresh actual-ELF totals: **4,547 /5,514 (82.46%)**, Game **3,874 /4,841
(80.02%)**, Init492/492, Debugger181/181, zero drift and967 different.
The conversion rows remain5,514/6,048 (91.17%),86.19% bytes. At the current
converted-function denominator, **140 further matches** reach85%.
The root README changes only these aggregate byte-exact rows.

Baseline consumer `f6c21dbbb31fb5cc34c417b672dbf2c622902b0c`, tools
`035d77986dc3a507b41e065b6b7a3531e779476f`. Earlier recovery and qualification
are in [Note2537](2537-game-actor-bound-burst-parent-recovery-screen-20261118.md),
[Note2538](2538-game-actor-bound-burst-native-caller-qualification-and-frame-map-20261118.md)
and [Note2539](2539-game-actor-bound-burst-complete-instruction-relation-20261118.md).
The implementation/fixtures use the `game_actor_bound_burst_150b7b40_match`
stem in the tools repository. The ignored `adoption-match` packet retains all
source, suite, padder, image, Make, recount and commit receipts.

## C recovery and source-derived normalization

The interface is `void func_150B7B40(ActorBurstE4070 *actor, u8 slot, s32 context)`.
It preserves the null gate; model-point/fallback endpoints and origin; current
heading-based radial offsets; model reload and transformed/fallback bounds;
zero-radius ratio; both particle children; ground query and optional floor
factory; clamped descriptor scales; and the two endpoint submissions. The
floor RNG is sequenced before the remaining factory argument reads. Meaningful
local descriptor/model names and a semantic function comment accompany the body;
unknown actor fields keep their measured offset names.

Reordering declarations and separating the short-lived mean/component scale,
magnitude sample and two rotation samples recovers **all13 retail object homes
and the exact616-byte frame**, without added fields or padding. The existing
O2/g3/no-loop-unroll profile is unchanged. All20 owner neighbors and normalized
compiler pools remain exact. Raw compiler SHA:
`1f53ede65754eedb8f10470e33856bb8be8de40d72c3f9447a908c14e6ee183b`.

The normalizer retains480 compiler operations, drops one redundant NOP and two
redundant constant setups, and generates two argument copies and two zero-to-FPR
transfers from compiler instruction templates. It uses72 source-range chunks,
17 closed register-allocation phases, and one explicit read-before-definition
role for the captured model cursor. Branch labels follow the first scheduled
instruction of their source basic block. That rule is necessary at the joined
radius reload; retaining the original leader's mapped position skips the load.

The normalization plan contains ranges/roles and templates rather than a retail
instruction replacement array. Guard rows are generated from its output, with
expected source words and both old/new symbolic bindings. The pure normalizer
checks the complete raw payload hash and42 source bindings. The independently
GNU-assembled original routine and ROM remain the comparison authorities.
A private full-path operand collection checked all480 retained operation
value-sets. It exposed three falsely paired multiplications in the initial
opcode-only diagnostic; their logical operands corrected the schedule before
qualification. This diagnostic is separate from the maintained whole-path proof.

## Fresh qualification in both tool configurations

Both final suites pass **eight tests**, no failures/errors/skips: **386.645s
primary /392.13s private sibling overlay**, each346 imported tool
fingerprints. These are fresh runs for this source/normalizer, not reuse of the
old484-word/frame600 draft's suite.

- Complete relation:257 symbolic paths per stream,544 related private/incoming
 bytes, all13 identity homes, ordered FP/FCSR, exact calls/arguments, public
 read epochs/counts, retained-object effects, full mapped frame, emitted V0,
 and saved GPR/FPR/SP/RA custody. Source reaches482/483 words and normalized
 retail483/484; the duplicate LUI1.0 is explicitly checked unreachable.
 Maximum path lengths are595 and593 instructions.
- Fourteen effective semantic negatives: nine source controls and five
 normalization controls. The latter reject FP allocation, trig argument copy,
 generated zero transfers, captured-model read role and the joined-radius label.
 Unsupported instructions and exhausted bounds are not accepted negatives.
- Both real complete-owner padders match every target word/binding and retain
 all20 neighbors and pools. Twelve actual GNU links test low16 values0,7FFC,
 8000 andFFFC. All525 source-word/binding corruptions are rejected. Another154
 effective padder controls cover17 allocation phases,23 selected guard families,
 insertion changes and all three relocation classes.
- Retail/raw/normalized guest streams each pass129 cases and4,160 provider
 calls, with full124/136-byte descriptor observations and saved ABI.
- Native32 O0/O2/O3 each pass129 cases/4,160 calls with exact arguments and
 initialized bytes, strict aliasing, UBSan, SSE/no-fast-math/contraction disabled.
 Eight native negative bodies exit3. The112/132 initialized descriptor bytes
 are compared; unwritten12/4 bytes are not read by the native checker.
- The genuine252-word dispatcher is GNU/ROM/current-ELF verified. Both original
 jump tables select state13, and the actual call passes actor/slot255/context1.
 All three parent streams pass128 cases/4,160 modeled calls,72 caller-owned
 bytes and saved ABI; the caller ignores parent V0 and returns0.
- Both real production children150B82D0 and150B85C0 execute together in every
 parent stream:516 cases,1,024 verified child invocations and379,392 child
 provider calls per stream. Each child is checked against its reference,
 public effects, complete vectors/packet and saved ABI. Coverage is187/188
 burst words and119/119 radial words. Three effective controls reject both
 child durations and parent routing. Other external providers remain modeled.

The symbolic proof assumes ordinary mapped/aligned execution, quiet-epoch
public reads, private/incoming separation from public objects, and extensional
providers on declared arguments and related passed objects. Providers may
mutate retained objects but cannot inspect implementation PCs, physical private
pointer bits, undeclared registers or unpassed locals. Arbitrary mapped padding
is related, not silently zeroed. Raw faults, interrupts, hardware FCSR behavior
and live gameplay are not acceptance claims of these tests.

## Production installation and independent audit

Only the qualified source and appended guards were installed. Production Make
compiled its own owner with the existing profile, padded/assembled it, relinked
and regenerated progress. No qualified object or ELF was copied into production.
The only build warning is the pre-existing duplicate generated_12D630 recipe.

The actual ELF exactly equals both independently predicted images:
`6e2699246b68d5fc35d1cdab6def91a171169761a374e54681511c5e12432abc`. The strict audit accounts for1,780 changed
bytes, the target extent and eight qualified zero-size alias-order groups, with
**zero exclusions**. All other6,050 bodies and every address remain unchanged.
Four deliberate whole-image corruptions are rejected. All189,088 protected
bytes and720 data owners remain exact.

Of1705 frozen source/build/tool inputs (1696 original plus nine dependency
artifacts), only the four declared source/guard/owner-object/ELF inputs changed.
Exactly one of698 production objects changed; its other20 functions/pools are
unchanged. Progress classifications/bytes are unchanged. Actual-ELF recount,
match-progress and tools-check pass.

A fresh installed-source compile matches all21 qualified raw functions/pools.
The actual484-word production body is the reference for new guest and genuine
caller checks; both pass. These two installed checks take30.379s.
The unchanged pre-install proof/native/padder/child/image receipts are explicitly
reused after exact artifact/task fingerprint checks, rather than called fresh.

The actual sibling tools HEAD,2,434 dirty paths and343 dependencies are preserved.
Its private755-file overlay uses339 sibling files,407 pinned primary fallbacks
and nine task artifacts. The supplied64CBFDOGL path currently contains only
retained `.codex`/`recomp_scene` directories, with no host source checkout to
transfer this C recovery into. No host files, Release artifact or saves are
changed; no host build/launch, dependency installation, Claude call or push.

Graph maintenance records the native updater's fail-closed refusal separately
from scoped AST extraction/merge, retaining old IDs and source-to-target evidence.
Tools are committed before consumer source/guards/docs and the new pin. The85%
goal remains active. Next inspect the remaining `func_150B879C` stub at the end
of this owner, qualifying its complete retail body and caller before adoption.
