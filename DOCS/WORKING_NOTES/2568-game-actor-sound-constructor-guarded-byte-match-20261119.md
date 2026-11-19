# Note 2568: Actor sound constructor byte match

Date: 2026-11-19. Consumer baseline `0865e770b23573a4d9e8a0ff1b1d69b6e7876366`;
tools baseline `c03283a473ffab5952e054944cf94ecee93f91fc`.

`func_15103C14` is installed and **byte-exact across its 137-word body and
139-word slot**, with the original **80-byte frame**. Semantic C emits the
complete body; **two expected-word guards** restore commutative ADDU operand
orders. The two original alignment NOPs remain. There are no insertions,
omissions or compiler-profile changes.

Fresh ELF recount: **4,562 / 5,514 (82.73%)** total, **3,889 / 4,841 (80.33%)**
Game, zero address drift, 952 different functions. Init 492/492 and Debugger 181/181
remain complete. **125 further matches** are needed for 85%. Converted counts
stay 5,514/6,048 (91.17%), 86.19% of bytes; the conversion CSV is unchanged.

## Source and recovered interface

Owner `conker/src/game_130CB0.c`, body VA `0x15103C14..0x15103E38`, slot through
`0x15103E40`; ROM `0x1310C4..0x1312F0`. The old zero-return stub and obsolete
placeholder declaration block are removed. The original caller at
VA `0x1509F20C` ignores this routine's return and overwrites V0 with 0x7000;
the recovered function correctly returns `void`.

Its five arguments are the full 32-bit sound ID, actor key, unsigned variant
count, cooldown index and paired-variant flag. The actor lookup gets a local
typed prototype matching its actual definition. The unsigned sound ID keeps
variant addition and increment defined through 32-bit wrap, while the sound
registration call narrows the ID and coordinates through its existing ABI.
Names describe observed use, not recovered debug identifiers.

The routine caches the selected halfword cooldown pointer, permits the 0x58D
exception while a cooldown is active, resolves and validates the actor, then
selects an unsigned random variant. Paired variants have stride 2. A camera
selects the 30000-volume `func_15103910` registration with packed value 20;
otherwise the 32700-volume `func_15103AA0` registration includes paired bit 15
and advances the selected ID for the second member. Both paths pass the
actor pointer, 0x100 flags and zero cents, then store cooldown 600 even if the
registration returns handle 0. Coordinates are reloaded after providers and
truncated to signed32 before their signed16 ABI narrowing.

All four neighboring owner functions remain raw/padded byte-identical,
including both newly matched sound callbacks. Constant pools, original
assembly and shared headers remain unchanged. Their prior semantic receipts
are reused explicitly; unchanged neighbor suites are not claimed as fresh.

## Compiler frame and guard proof

The first C body already had 137 words and correct instruction order/bindings,
but used frame 88. Two fingerprint-locked compiler traces follow newly owned
CFE/UOPT/UGEN children. All compiler fingerprints, actual captured inputs,
fired frame observations, child/driver exits and normal-object identity pass.
Compound sound-ID assignments reserve one shared four-byte frontend temporary:
the frontend M definition is 16, the optimizer M definition 20, the rounded
UGEN local area 24 and the frame 88. Explicit assignments reduce those fields
to 12/16/16/80 respectively. One additional word crosses an eight-byte frame
rounding boundary. The named primary flag's
declaration order recovers its original SP+0x48 home and the cooldown
pointer remains at SP+0x40. Outgoing area 48 and saved component 16 are observed
internal layout fields, not performance measurements or a saved-byte census.

Only two commutative nontrapping unsigned additions remain different:

| Offset | C expected | Retail replacement |
| --- | --- | --- |
| 0x98 | 0x01718821 | 0x022B8821 |
| 0xB8 | 0x01B18821 | 0x022D8821 |

Both are SPECIAL/ADDU with destination S1 and shift0. Only their two source
register fields swap; the opcode, destination and all other bits are fixed.
ADDU reads both inputs before writing and computes their sum modulo 2^32,
which is commutative for all input words and has no overflow trap or flag
effect. Neither word has a relocation. Exact raw-body SHA and relocation
guards fail closed, and original/raw-C/guarded streams agree in full guest
state and access prefixes. Existing CSV bytes are preserved as an exact
prefix; precisely these two guarded rows are appended.

## Qualification

The primary tools checkout and isolated sibling overlay each pass the same
five-test suite before and after installation:

- 430 independent cases per original, raw-C and guarded stream. They cover
  cooldown exceptions, null/rejected actors, unsigned divide and addition
  extremes, both callback paths, float truncation, all valid native cooldown
  slots and guest sparse/index wrap cases, helper effects and incoming homes.
- 179 access-fault prefix triples, five effective instruction negatives and
  two guest-only zero-divisor boundaries at the original DIVU instructions.
  All 135 normally reachable body words are visited. The two retained BREAK7
  instructions are checked byte-for-byte; mutated zero-divisor fixtures stop
  before DIVU rather than claiming portable modulo-zero C behavior. All 137
  body words and both alignment words are checked by exact comparison.
- 378 native SDK32 cases each at O0/O2/O3 with strict aliasing, UBSan and
  float-cast-overflow checks; eight executed source negatives per profile.
  Expected actor fields, timer values, call arguments and provider snapshots
  are serialized from the independent Python contract. Byte accessors avoid
  aliasing float storage through integer lvalues. The freestanding Linux
  entrypoint explicitly aligns its stack; GDB identified the original harness
  fault as an unaligned MOVAPS, and no game-source change was needed for it.
- Six independent GNU relocation rebases /12 links compare all 548 body
  bytes. Every raw byte and binding has an effective corruption control;
  strict-image controls include an alignment byte outside the symbol body.
- 64 scenarios through the original 11-word `func_1509EFF0` call window across
  all three streams. The 12-argument `func_1000FA64` ABI also gets 24 executions
  of its original seven-word callee prologue, checking the four register homes,
  eight incoming stack arguments, saved registers and 40-byte callee frame.

Full-ROM census finds exactly one direct JAL, ROM `0xCC6BC`, and no literal
target words. Computed references are not excluded. Caller and selected
callee source/assembly inputs are hash-pinned. Providers remain bounded
models, and these windows do not establish full-parent, hardware or gameplay
acceptance. Native tests require valid actor/table objects and signed32-range
float conversions; sparse addresses and argument-home mutations are guest-only.

## Production and documentation

Both independent padders agree across all five owner functions. The real
three-command Make owner recipe uses the proposed guard manifest and equals
the independently padded object. Production Make processes the actual CSV
dependency change; every other frozen object and function remains unchanged.
The ELF equals the strict 403-byte prediction: this body and its 12-to-548-byte
symbol extent only. There are no exclusions or symbol metadata permutations.
All 6,051 addresses stay fixed; all 189,088 protected data bytes across 720
owners remain exact. Makefile, guard history, original assembly, unrelated
inputs and conversion CSV are preserved. `make tools-check` passes.

Production ELF SHA256:
`9b320fb779551fc6177517b4112c16729369e7cdc4180cb111961a43161d2c91`.
The real dirty `64CBFD Tools` sibling remains untouched, including its HEAD,
raw status and 343 dependency hashes. The 915-file overlay has 339 matching
sibling files, 570 explicit primary fallbacks, five task files and an empty
bootstrap. Both installed suites import identical dependency bytes apart
from the bootstrap. The checkpoint records all frozen/adopted fingerprints.

Root README changes only its two aggregate matching rows; five concise
documentation indexes link here. Graphify's native update refuses shrink;
the scoped AST fallback retains all existing node IDs. Commit-hook producers
must be observed terminal before historical aliases and the literal manifest
reference are retained and the final graph hash sealed. This is not a full
corpus extraction. Ignored evidence and current handoff are in
`conker/build/game-sound-constructor-15103c14-private/`.

## Next

Continue with `func_15103E40`, the adjacent 204-word slot in
`conker/src/game/generated_1312F0.c`, VA `0x15103E40..0x15104170`. It currently
uses GLOBAL_ASM, so conversion and a fresh recount at the new conversion total are needed.
Inspect its complete body and own interface/profile independently. Preserve
the three recovered sound routines and the older private 591-word
`func_150BBB5C` candidate. The full 85% matching goal remains active.
