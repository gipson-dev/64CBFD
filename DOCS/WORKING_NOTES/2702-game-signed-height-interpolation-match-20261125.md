# Signed height interpolation callback match - 2026-11-25

`func_151155C0` replaces its zero-return placeholder with a typed scalar
height interpolator in `conker/src/game/generated_142560.c`.
VA151155C0..1511575C, ROM142A70..142C0C: **103 words / 412 bytes, frame0,
no alignment tail or relocations**. **27 words emit directly; 76 checked
expected-word guards normalize allocation, copy placement and nontrapping
integer scheduling. Raw C is not byte-exact.** There is no single global
GPR recoloring, private frame map, insertion, omission or compiler profile
change. NormalO2/g3 and all83 neighboring raw/padded functions and pools
remain fixed. Both complete-owner padders emit the same object.

Production recount: **4,681 / 5,528 (84.68%)** total; **4,008 / 4,855
(82.55%)** Game; Init492/492, Debugger181/181, zero address drift,
847 still different. **18 more verified matches reach85%.** One new match,
zero caller/helper credit; conversion rows and denominators remain fixed.

The recovered `HeightState151155C0` is160bytes, with signed height12,
callback38, packed parameters3C, flag4 at4F, signed delta5C, origin7C and
hold80. All16 member offsets/widths and the full record extent are pinned.
The packed low16bits give the signed target, bits16..23 the divisor and
bits24..31 plus1 the hold length. Zero origin captures the current height.
The signed division uses wrapping32-bit target-minus-origin. Zero hold
moves back toward origin or starts the forward hold; positive hold advances
toward target; negative hold increments toward zero. Endpoint updates clamp
the height and change hold sign. The final delta is a wrapping signed16
height difference. Retail's repeat hold80 read after the reverse height
store is retained with one scoped volatile access, supported by guest
mutation tests. Original volatile-source intent is unknown.

The selected C returns the machine's latest computed candidate, or the
divisor on paths that compute no candidate. This inferred `s32` interface
preserves actualV0 on defined paths. The callback field uses the compatible
one-pointer signature. Original source return intent is unknown: the actual
parent ignoresV0. The stronger recovered machine return contract makes the
live candidate lifetime explicit and emits103words with the exact retail
opcode multiset. A void source emitted101words; final-current reload forms
emitted104/105. No artificial uses, barriers or padding were accepted.

Fresh reconstruction checks also rejected another-source C with unaligned
widths and an ineffective final delta, and localm2c output whose final delta
was likewise zero. Correcting that delta still produced139words and changed
HI/LO by sinking the unconditional divide. A supportedO1 diagnostic produced
156words and extra stack writes. None is adopted, and no production profile
was changed. Raw shape equality and advisory consensus alone earn no credit.

The complete alignedROM target-reference census finds no directJ/JAL and
one literal callback pointer: tableD80088C90, selector28, column0, stride12,
ROM22D8A0 / VA80088DE0. All12bytes are pinned to ROM and frozen ELF.
Registration windows15003C94..3CE4 and1509EBBC..EC10 are inspected static
evidence; their initializer execution is not qualified. The LW38/JALR
heuristic is explicitly not a universal indirect-call census.

The complete original parent `func_15113E54` is127words/frame64 and matches
ROM141304..141500. Fresh connected tests execute all127words in803cases
per stream, with2,515 child invocations per stream. Direct and grouped loops,
160-byte stride, active/disabled/type gates, empty and wrapping counts, first
physical-entry delta/hold cache and cross-group retention are checked.
Full parent frame bytes, saved/return state, FPR/FCSR andHI/LO agree between
retail and raw child streams. Two supported wrong parent variants finish
then fail comparison. All callbacks point to this leaf within this scope;
other callback internals and complete gameplay remain unqualified. The
parent C placeholder stays unmatched and uncredited. A fixture initially
aliased group data with the parent stack; it was corrected before acceptance.

The independent scalar guest reference checks1,979cases per stream,
including54 machine divide-zero break7 traps. Four retail-identical streams
and raw compare all160 record bytes, canaries, saved state andHI/LO; defined
normal returns also compareV0. All100 feasible retail words are visited;
indices34/35/36 guard impossible divisor-1, since the packed divisor is an
unsigned byte. **35 access-fault quads** compare
exact PC/delay/trace, physical registers and memory across the four literal
retail streams. Raw scratchGPR/fault-prefix equality is not claimed.
Portable C division by zero remains undefined; the native suite excludes it.

The bounded structural integer proof first agrees with an independent VM on
3,958 concrete executions, including every physical GPR andRAM. It then
enumerates132 overapproximated abstract paths in each of two modes: ordinary
record memory, and an arbitrary guest-only second hold80-read mutation.
Arbitrary field bits, initial registers and every unknown predicate assignment
are represented. Signed quotient/remainder are identical-operand
uninterpreted operators. Final public bytes, ordered writes, reads per write
epoch, branch decisions, returnV0, callee state andHI/LO agree. Read-only
loads may reorder within a write epoch. Two supported complete corruption
controls reject. This is not anSMT solver, general binary proof, native
concurrency guarantee or raw fault-prefix claim.

Native32 executes the actual selected C in two translation units atO0/O2/O3:
4,482 direct/typed-callback calls per profile, all256flags,255nonzero
divisors, signed16/signed32 boundaries, hold/target/origin extremes, all
retained bytes and224-byte arena/canaries. All four rounding modes and six
MXCSR sticky bits survive. Strict aliasing, UBSan traps, LTO and type-mismatch
errors are enabled. Seven wrong C variants complete and return comparison42;
all normal profiles return0. No signal/trap counts as a successful control.

Boundary tests reject152 guarded corruptions and expose54 unguarded
corruptions. There are no external bindings to pin. All internal branches
remain in extent; both oversized probes reject.
20GNU links and60 guest runs cover four entry bases. The generic owner
emitter requires42 exported retail jump-label restorations: this local
wrapper adds only label directives and splits existing zero spaces. Full
before-owner object identity, definitions and relocation metadata prove that
all42exports and every byte are retained. Missing label metadata was a
qualification-fixture issue, not a source/neighbor regression; it is not
excluded from linked audits.

The actual five-command Make route includes GLOBAL_ASM pre/postprocessing,
IDO, generated padding and assembly, with zero diagnostics. The independent
reference uses frozen old C and the original412-byte targetASM, without the
new C or its guards. Reference, whole-owner Make link, literal prediction
and production ELF are identical: **279 changed bytes,
zero exclusions**. All189,088 protected Game data bytes across720owners,
all unrelated addresses/objects, old guard prefix and conversion rows remain
fixed. Named symbol/string serialization is reconstructed with closed byte
accounting rather than excluding ELF metadata.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 82.752 s | 5 fresh / 0 reused |
| preinstall-sibling | 86.017 s | 5 fresh / 0 reused |
| installed-primary | 81.129 s | 5 fresh / 0 reused |
| installed-sibling | 87.158 s | 5 fresh / 0 reused |

Task/import/data/profile/artifact fingerprints agree across primary and an
isolated second tools copy. The second copy uses
2125 immutable dependency links and10new
task copies. Freeze: 3761 inputs / 2679
copies. Shared tools-check passes. Its Make route uses its own tools. The
independently dirty real tools sibling is preserved.

The first packaged suite caught a fixture-generation replacement that damaged
`rng.randrange` and `rng.getrandbits`. Its failed receipt is preserved. Both
task copies were corrected and fingerprinted before all20 final fresh tests;
the production candidate and independent image result were unchanged.

One earlier packet-only ClaudePro review completed with empty tools/MCP and
zero tool uses; findings were independently reconciled in
`claude-reconciliation.json`. A second call was unnecessary. Early register
pressure and scheduler-cause suggestions were unproven; the final acceptance
rests on independently compiled source and explicit semantic/build/image
evidence. The review itself contributes no matching credit.

Baseline consumer `e14144293dcd9bbb8a11aa4867eadcc1ca0a0f4e`.
Tools commit `fe7fc8ede52a7f2db12b54fc667d64f7e023cd6e`.
Production ELF SHA256 `46263e4885273d3f34e194bafb472a8e2c00ff8a28c2c6b62850d9334517cb07`.
Padded owner SHA256 `97fdd9f9057cf23afccd769d6f60266ad601dba3cc129cfa82f035325681b95f`.
Receipts: `conker/build/game-height-interpolation-151155c0-private`.

Root README receives aggregate/date rows only. Graph work retains all old IDs
and qualification metadata and refreshes the changed owner and task Python
files after the actual hook writers finish. Scoped AST extraction is not
full-corpus reextraction. No host transfer, build, launch, Release change,
gameplay acceptance or push is claimed. Continue the active85% goal after
banking this result.
