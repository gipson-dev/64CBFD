# Actor phase motion direct match - 2026-10-31

`func_150DE6D8` is restored from its false zero-return placeholder to a semantic
`void` callback. All **58 compiler words match directly**, with 13 relocation
bindings, no guards, inserted words or omitted instructions.

The adopted ELF recount is **3,978 / 5,506 (72.25%)** exact C functions;
Game **3,305 / 4,833 (68.38%)**, Init 492/492, debugger 181/181, zero drift.
There are 1,528 different C routines. The 75% threshold is 4,130, leaving
**152** more exact matches. The matching goal remains active.

## Source and ABI

Owner `conker/src/game/generated_10B7D0.c`; original `conker/asm/10B7D0.s`.
VA `0x150DE6D8..0x150DE7C0`; ROM code-input span `0x10BB88..0x10BC70`.
Signature: `void func_150DE6D8(ActorPhaseMotion *actor)`.
The frame is 32 bytes, S0 at SP+24 and RA at SP+28. The existing standard
O2/g3 owner profile and shared headers are unchanged.

The callback computes a signed halfword pitch at +0x12 from phase +0x7C,
X at +0 from phase +0x80, and Z at +8 from phase +0x84. Each phase supplies
an eight-bit angle after an arithmetic shift by three. Pitch uses separately
rounded f32 multiply/add, followed by truncation toward zero. Retail constants
are 10.2f, 1130.0f and two copies of 1.1f. The three phase accumulators then
advance by ticks times 12, 16 and 24. Unsigned fields and arithmetic preserve
32-bit wrapping without introducing signed-overflow undefined behavior.

The three `func_15048A40` calls remain observable mutation boundaries. Constants
reload after the corresponding calls. Later angle inputs and final phases
observe provider mutations. All three final phase values are captured before
the Z store, and ticks reload separately after each preceding phase store.
Guest aliases qualify this emitted order; native C uses disjoint typed storage.

## Owner, build and image

Eight complete raw/padded neighbors and normalized pools remain unchanged.
The actual three-command Make recipe reproduces the qualified padded object.
Selected, before/after owner and actual-Make diagnostics are empty. No source
profile or Makefile change is needed.

Strict independent whole-image prediction has **zero exclusions**:
237 changed bytes = 192 root-code bytes + one symbol-extent byte + 44 metadata
bytes. Metadata consists only of two closed symbol/string-table permutations:
`func_150CBCE0` / `D_8009ECFC`, and `D_800A0D50` / `D_800A08F0`.
Named values, sizes and definitions are checked independently. All 6,055 other
linked bodies and all addresses remain fixed. All 189,088 protected Game data
bytes across 720 owners remain exact. Existing word guards are byte-identical.
The initial prediction without the two metadata permutations was rejected and
retained privately; it never supplied matching credit or an audit exclusion.

- Raw/unlinked target SHA-256: `9eb1a7e42873c15850c1c9895662e2b6aed90ebadc03548e6e4a8e3adac39189`.
- Qualified ELF SHA-256: `ace49b51048949cb5c42d328bfdc63847bebe868ae79398f25a1a9e317c8c9d3`.

## Qualification

Guest validation runs 4,864 ordinary cases / 19,456 executions through original,
raw compiler, padded and actual-Make images. Three GNU address layouts include
HI/LO carry. All 58 root words are visited, with 12 additional alias cases and
92 access-prefix cuts, including eight branch-delay cuts. Complete registers,
FPRs, memory, callbacks and access traces agree. Synthetic callbacks mutate
phases, constants, ticks and prior output fields between calls.

Connected tests retain the original 12-word angle wrapper and 36-word quadrant
lookup, plus original table bytes. All 48 helper words and all 256 angle values
are exercised in 1,536 cases / 6,144 executions.

Native SDK32 C passes 262,144 cases at each of O0/O2/O3 with trapping UBSan.
Coverage includes all 65,536 low halfwords, four high-word extremes and all
64 provider-mutation modes. Fifteen compiled semantic controls each produce
the designated mismatch exit; compiler failures and traps do not count.
Floating conversion fixtures remain finite and in the signed-halfword range.
There is no claim about arbitrary invalid conversions, FCSR exceptions,
portable alias behavior or full gameplay/hardware acceptance.

The aligned census of the complete provided retail code input finds no direct
JAL root references and one literal root pointer at `0x22D990`, VA `0x80088ED0`.
It is row 48, field zero of the 12-byte `D_80088C90` callback table. Nine original
constructor-window words copy that field into record+0x38; ten registration
fixtures check the root row and neighbors. The nearby non-absolute ELF label
`D_80088C00` denotes a display list and is not the callback table base.

Two original `func_15113E54` caller windows contain the indirect calls at
`0x15113EE8` and `0x15113FC0`. The original windows are 13 and 30 words;
96 cases / 1,536 executions cover skip gates, second-iteration stores and four
poisoned return-register values. A0 receives the record pointer and V0 is
ignored and overwritten. The registered callback therefore has a void ABI.
These are bounded original windows, not a full-parent execution claim.
An ELF-only caller scan initially found none because the updater is still a
placeholder; the authoritative scan uses its retail instructions.

## Adoption and continuation

Both tools copies pass all eight fresh canonical tests and shared checks.
Installed source/image gates run freshly in both copies; six unchanged semantic
gates are reused only through complete artifact, module, compiler-adapter and
input-seal identity. Tools are committed first at `f30f6b4c068d3353692542857eed5bad76245ce1`. The consumer then
banks source, tools pin and seven docs. Root README changes only two aggregate
rows. The scoped graph retains all old valid relationships and retires the
single obsolete s32 placeholder-return edge after validating the void source.

Retained evidence: `conker/build/game-actor-phase-motion-150DE6D8-match/`,
including `preparation.json`, `private-semantics-v13.json`, both preinstall and
installed receipts, `sealed-production-proof.json`, actual `75-percent-queue.json`,
full function views, `graph-final-proof.json` and `BANKED_STATUS.json`.
Next screen: `func_151CB510`. Private matches remain uncredited until complete gates pass.
