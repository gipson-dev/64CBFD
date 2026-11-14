# Game four-slot effect dispatch guarded match

Date: 2026-11-14. `func_15183290` is recovered in
`conker/src/game/generated_1B0740.c`. Its complete **392-word / 1,568-byte**
routine occupies **0x15183290..0x151838B0**, ROM **0x1B0740..0x1B0D60**.
The raw and guarded bodies both use the original **0x68-byte frame**.
**348 words emit directly from semantic C; 44 expected-word guards normalize
closed temporary-register choices and one commutative address addition.**
This is guarded matching, not a direct C-only match.

All eight neighbors remain identical. The owner now contains **9 / 9
byte-exact recovered C functions**, with no zero-return placeholders.
Its obsolete placeholder heading is replaced by a recovered-routines heading.

## Behavior and recovered interface

The signed 32-bit return is -1 on failure or the selected slot 0..3. Eleven
word arguments carry X/Y/Z, an effect value, kind, an unused word, view,
three event parameters and flags. Their full transport words are preserved;
only kinds 0 and 1 explicitly narrow the value to a byte. The constructor
interfaces have 9, 10, 11 or 18 words, with their two float arguments kept
in the retail stack positions. The unused sixth word remains explicit.

The routine scans four bytes at `D_800DDF5C` for the first zero. A full pool
returns -1; the retail delay-slot read of the first event parameter survives.
With a free slot, all three event parameters shift left four bits with word
wrap and are stored back into their incoming homes. Unsigned casts avoid
signed-shift undefined behavior. The actor pointer is fetched eagerly from
`D_800DBFF0 + view * 0x9A0 + 0x3D0`, before the switch bounds check.

Kinds 0/1 submit a point or attached effect. Kind 2 prepares record 0 and
submits its fixed constructor packet. Kind 3 checks the actor predicate and
returns -1 without reservation when it fails. Kinds 4/10 prepare records and
use the first shifted parameter scaled by four again. Kinds 5/11 prepare
records 2..5 and retain their distinct constructor mode. Kinds 6/7 retain
their separate resource selectors, command flags and float scales.

Kind 8 returns -1 without reserving a slot. Kind 9 converts the captured
actor's three position floats to integers, submits the existing burst
routine, and returns the slot without reserving it. Unsupported unsigned
kinds, including negative signed inputs, still reserve the selected slot.
The selected index and flag pointer survive helpers; the pool is not rescanned
after helper mutations. Neutral event-parameter names avoid asserting an
unproven physical meaning.

The only direct JAL is at **0x150A255C**, ROM **0xCFA0C**, in
`func_150A24C0`. Its 23-word argument window recovers signed halfword
coordinates, the adjusted Y coordinate, event bytes and flags. The caller
uses the return value, confirming the signed result interface. There are
no aligned literal pointers to the dispatcher. The alternate source was
read as an advisory lead; its incomplete helper declarations were not adopted.

## Object, table and normalization qualification

The raw body SHA-256 and every named relocation are pinned:
`65fe4e9c404d408350a1fdb2ade08db32f805d8211e17775c941ce1b6f6e4279`.
All **392 raw-word corruption controls** and one helper-binding control reject
changes. Register cycles affect only T3/T4/T5 in nine straight-line regions.
A symbolic check covers **245 instructions / 162 ordered memory events**,
including alias-aware memory state, all other GPRs and all FPRs. A successor
liveness check includes all twelve switch edges and branch/call delay slots;
the ignored temporary values are dead. Effective wrong-store and call-delay
controls reject changed behavior. No instructions are inserted or omitted.

The compiler emits a 48-byte twelve-entry table whose every target agrees
with the original case offset. The existing assembly data owner retains
`jtbl_800A72F0`; a single owner-specific `RETAIL_RODATA_SYMBOL` Make binding
maps compiler references to that original table. No copied table or float
pool is installed. Both complete-owner padders agree on all nine functions;
four independent GNU link layouts give **12 literal link comparisons**.

## Semantic checks and limits

The mounted tools and isolated sibling overlay each pass the focused suite:

- **1,216 guest cases**, all **392 retail words** visited, including full
  pools, all kinds, unsupported words, wide parameters, sparse guest views,
  both predicate outcomes, helper mutations and two stack phases.
- **72 real caller-window cases**, **493 memory-cut prefixes**, and **12
  invalid float-conversion prefixes**. Raw C is checked semantically; complete
  machine-state and fault-prefix identity apply to retail versus guarded code.
- **24 connected executions** of the original actor predicate, covering all
  ten reachable predicate words; the original unreachable word is retained.
- **394 native32 cases each at O0/O2/O3**, with undefined-behavior trapping,
  and three effective wrong-reservation/shift/return controls.

GDB identified an initial native-harness SSE crash as startup stack
misalignment. `force_align_arg_pointer` corrects the harness entry only;
production source is unchanged by that repair. Native tests use valid C
pointer ranges and valid conversions. Sparse/wrapping guest addresses,
incoming-home overwrites and invalid conversions are guest-only evidence.
Other large effect constructors remain opaque providers and include existing
unrecovered production functions; this does not claim complete gameplay or
provider correctness. Routine work used zero Claude calls.

The sibling checkout remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` with all **2,439**
preexisting dirty paths preserved; status SHA-256 is
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`. All six overlay files equal the mounted task files.
Shared `make tools-check` passes. The existing duplicate generated_12D630
Make recipe warning remains unrelated to this change.

## Production result and next target

The independent shadow executes the three actual Make object commands using
the exact proposed Makefile. Production agrees byte-for-byte with its ELF:
`8400f94bcc5155c73e2e4df8c762ee8608af6c4d6aec9f3be647992b2356f875`.

The strict **1,337-byte** image delta contains only the
declared body/extent and six explicitly reconstructed closed symbol/string
permutations. There are **zero exclusions**. All **6,051 function addresses**,
all **189,088 protected data bytes**, all **82 headers**, every existing guard,
and conversion CSV rows remain fixed. Only the target owner changes among
**698 objects**. The audit checks **792 immutable inputs**;
exactly 44 new guard rows and the scoped table binding are installed.

Actual recount: total **4,485 / 5,515 (81.32%)**, Game **3,812 / 4,842 (78.73%)**,
Init **492 / 492**, Debugger **181 / 181**. There is zero address drift and
**1,030** different C functions. Converted totals remain unchanged. **203**
more matches reach the active 85% goal at the current denominator.

Scoped Graphify AST refresh covers the owner and six tools files, retaining
all **60,530** old node IDs: **60,570 nodes /
114,015 links**, zero lost nodes. This is not full-corpus extraction.
Private receipts are under `conker/build/game-effect-dispatch-15183290-screen/`.
Tools commit `16c1f9cbb4033571cca8876408af25a17a47a6ec` banks the six qualification files before the consumer.

Next: **`func_15174BF0`**, the 237-word effect constructor in
`generated_1A20A0.c`, with original frame **0xD8**. Recover its complete
argument, actor/view and allocation behavior before adoption. The 85% goal
stays active; no push. `64CBFDOGL` has no host source checkout available here,
so no host adoption or runtime claim is made. Release remains frozen.
