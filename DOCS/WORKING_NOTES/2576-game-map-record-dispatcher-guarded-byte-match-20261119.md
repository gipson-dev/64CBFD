# Note 2576: Map-record dispatcher guarded byte match

Date: 2026-11-19. Consumer baseline `3b3461b42ff8cc05700ac800b970da14d5bf35c0`;
tools baseline `601742bed51660af9e1c5ae75cb007ff1f79ff8c`.

`func_15104A80` is converted from GLOBAL_ASM to semantic C and **byte-exact
across its complete113-word/452-byte body, with the original104-byte frame**.
The closed mapping uses36 relocation-aware guards and three meaningful
instructions, with no omissions, artificial padding, volatility or profile
override. Ten owner neighbors and all original constant pools are unchanged.

Fresh production recount is **4,566 / 5,517 (82.76%)**, Game **3,893 / 4,844
(80.37%)**, zero address drift and951 different. Init492/492 and Debug181/181
remain exact. Conversion totals are **5,517 / 6,048 (91.22%)**,86.26% of bytes;
Game4,844/5,327 (90.93%),85.64% of bytes. One previous ASM row becomes C.
**124 more matches** reach85% at the current denominator; new conversions can
change that denominator. The full85% goal remains active/unfulfilled.

## Recovered body and interface

The routine occupies VA0x15104A80..0x15104C44, ROM0x131F30..0x1320F4.
It is a void callback taking one `struct131 *record` in A0; the obsolete
zero-argument signed-result prototype is removed locally. The original parent
uses the callback for mode0x34 and does not consume V0. SDK declarations remain
unchanged. Detailed semantic/native recovery is in Note2574; the complete
paired CFG/effect relation is in Note2575.

A signed32-bit byte difference from `D_800DBEF4`, divided by160 toward zero,
indexes the mask table through `D_800DBF94`. A nonzero mask selects the first
active actor among slots0..24, using stride0x32C and signed nonzero interaction
state. Bits25 and above do not select the spare26th SDK slot.

Record byte+0x72 F9/F8/F7 copies the corresponding existing nine-byte template
and submits `{length9, sequence pointer, actor pointer}` with command0x35.
F6 submits an actor-pointer address with command0x38; other kinds submit nothing.
The source uses descriptive local packet/sequence types and a brief function
comment. Original rodata ownership is retained in `asm/data/246E40.rodata.s`.

## Closed compiler transformation

The tested C emits110 words with the same104-byte frame and all original homes:
actor-only SP+24, F7/F8/F9 sequences SP+28/34/40, packet SP+4C and saved RA+14.
It has ten unchanged raw owner neighbors and unchanged original pools. The
five existing pointer/integer diagnostics in unrelated callbacks remain exact
after normalizing only fixture filenames/shifted line numbers; no suppression
or new diagnostic is introduced.

The three inserted instructions follow raw offsets0x104,0x10C and0x140:
two `addiu A0,SP,0x4C` per-arm argument setups and the second likely branch's
`addiu AT,zero,0xF7` delay setup. The36 guarded rows cover the associated opening
address/zero schedule, commutative AND operands, kind initialization, sequence
address/load scheduling and moved branch targets. Thirteen rows also move
explicit relocation bindings. Every expected word/binding is checked and all
14 final bindings match the independent original assembly exactly. There is
no blind71-word replacement of the earlier misaligned comparison.

The Note2575 fixed-point relation is checked freshly during each integration:
61 paired effect nodes/77 edges,117 worklist steps,131 effective instruction
controls and12 accepted pure/dead-setup controls. It establishes ordered memory
effects, explicit helper arguments and callee-saved return state under its
documented source-ABI helper abstraction. It does not equate raw physical return
PCs or helper-private RA spills. The **installed113-word stream itself is now
literally identical to retail**, including all branch/delay/dead-word positions;
the raw relation is not used to claim literal raw fault-register identity.

## Independent build, relocation and production gates

The owner is mixed C/ASM and has no preserved whole-file `asm/131F30.s`.
The production `pad_c_object` route is compared with `pad_generated_object`
using an independent layout assembled from the authoritative retail layout
and original ROM spans for all11 owner functions. Both normalized function
sets, bindings and pools agree. A complete original target is also assembled
independently from its preserved nonmatching ASM.

The actual mixed Make recipe runs five commands in a private shadow: ASM
preprocess, existing IDO O2/g3 compile, ASM postprocess, retail padding and
GNU assembly. The resulting complete object equals the predicted padded object.
Twelve independent GNU links across six rebases agree for normalized C and
original assembly, including HI/LO carry changes and helper call relocations.
Stale expected-word and expected-relocation controls fail in both padders.

Primary tools and a944-file isolated sibling overlay each pass eight fresh
pre-install tests, including1032 original/raw guest cases, actual SDK32 native
source at O0/O2/O3 with UBSan/strict aliasing and effective source controls,
the original13-word wrapper,61 original callback windows and113 paired bounded
memory-access cuts. Installed primary/overlay checks freshly revalidate the
full owner/Make/image gates and1032 guest cases. Unchanged native and relocation
receipts are explicitly reused after their source/profile/import fingerprints
are checked. `make tools-check` passes freshly.

The normal production Make completes successfully. All1973 frozen inputs are
audited against the declared source/guard/conversion changes. The target object
and complete linked ELF equal the private prediction. **All6051 linked function
bodies and addresses are unchanged; zero changed image bytes, zero exclusions.**
Protected game data remains exact across189088 bytes and720 owners. ELF SHA-256
stays `d3eeddd84c1cd3c6c0877467dfdf37015677dc0a81885ea7f5ed6d528b2f352d`.
Original ASM, headers, Makefile, prior guard history and unrelated work remain.

The real independently dirty `64CBFD Tools` sibling retains its HEAD, complete
raw Git status and343 dependency hashes. Its checkout is not overwritten.
Tools commit precedes the consumer source/docs/gitlink commit; no push.
Bounded sibling-port inspection found retained recompiler scratch outputs,
including an empty `cd64_out` stub; these are not active-host acceptance proof.
This decomp conversion changes no retail instructions or behavior to transfer.
No host files, builds or frozen Release artifacts are changed.

Graphify's normal update refuses a shrinking corpus. A scoped AST merge covers
the two new Python files and installed C owner, retains every prior node ID,
links the matching manifest to the actual C definition and marks the former
GLOBAL_ASM reference historical. Commit-hook writers are observed terminal
before heading aliases and final graph hashes are sealed. This is not full
corpus re-extraction. Routine work uses zero Claude calls.

## Next function

Continue with `func_15104C44`, still GLOBAL_ASM in the same owner, at
VA0x15104C44..0x15104FF8, ROM0x1320F4,237 words/frame224. Its original prologue
saves S0..S7/FP and F20/F22/F24/F26 and has an early signed halfword gate.
Recover the complete body and qualify its caller/ABI, FP/access order and owner
neighbors before installation; no recovery or matching credit is claimed yet.

Reproduce: `python3 -m unittest
tools.tests.test_game_map_record_dispatch_15104a80_match -v` under prepared WSL.
Ignored evidence: `conker/build/game-map-record-dispatch-15104a80-match-private/`.
