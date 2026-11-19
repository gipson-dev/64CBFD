# Note 2574: Map-record packet dispatcher recovery and branch shape

Date: 2026-11-19. Consumer baseline `c7d85f025116acd3519e0a0e72550fec1234f2ab`;
tools baseline `8167ebc98f2c09be94034b00f5ed12857b9fb8a2`.

`func_15104A80` has a complete tested **private semantic C recovery:110 words,
original104-byte frame and all original packet/sequence homes**. Retail has113
words. The aligned word comparison still has71 differences, including the
three-word length gap; this is not a closed register-field-only normalization.
**The live function remains GLOBAL_ASM, with zero conversion or matching credit.**

All1964 frozen inputs, production source/objects/ELF, guards, Makefile, conversion
CSV and root README remain unchanged. Fresh recount stays **4,565 / 5,516
(82.76%)**, Game **3,892 / 4,843 (80.36%)**, zero drift and951 different.
**124 more matches** are needed for85% at the current denominator. The wider85%
goal remains active. The prior nearest-height match stays installed and exact.

## Complete routine and interface

The original113-word body is VA0x15104A80..0x15104C44, ROM0x131F30..0x1320F4.
It is a **void callback receiving one160-byte map record in A0**. The old local
`s32 func_15104A80()` declaration is a placeholder, not evidence of a result.
The recovered owner removes that prototype only in its private copied source.
No shared SDK declaration changes.

The routine loads the map-record base through `D_800DBEF4`, subtracts it from
the record address and divides the signed byte difference by160 with truncation
toward zero. The resulting index selects a32-bit mask through `D_800DBF94`.
The private C uses a32-bit unsigned address subtraction followed by the signed
interpretation/division, retaining the emitted SUBU/DIV behavior. Native cases
exercise positive/negative and partial-record deltas on valid aligned storage.

For a nonzero mask, the routine scans actor slots0..24 at the original0x32C
stride. It chooses the **first** actor whose signed interaction-state word is
nonzero and whose mask bit is set. Negative states are active; bit25 and higher
never select the spare26th SDK actor slot. A zero mask skips actor-state reads.
If no actor qualifies, the payload contains a null actor pointer.

Record byte+0x72 chooses the payload:

- F9/F8/F7 copy nine bytes respectively from `D_800A2380`, `D_800A238C` or
  `D_800A2398` to a private sequence. A12-byte packet contains length9, sequence
  pointer and selected actor pointer, and is submitted with command0x35.
- F6 passes the address of the selected-actor pointer with command0x38.
- Every other byte value submits no command. Return V0 is deliberately
  unconstrained because the callback is void.

The three original templates are `00 01 02 03 04 05 0F 10 11`,
`06 07 08 18 19 1A 12 13 14` and `09 0A 0B 0C 0D 0E 15 16 17`.
The source uses typed nine-byte aggregate copies from the existing globals,
rather than creating duplicate initializer pools. The actual original rodata
owner is `asm/data/246E40.rodata.s`; it and all constant pools stay unchanged.

## Original callback and wrapper evidence

`func_151177C0` materializes this callback at0x15117850/0x15117864 for its
0x34 mode. Its original JALR is VA0x15117958, ROM0x144E08. An eight-word
window at0x1511794C saves/restores the record and mode around the call. The
connected test executes that window with the original and recovered callback,
then observes its branch to0x1511799C. It passes61 scenarios per stream.

The original13-word `func_151494E0` wrapper at ROM0x176990 is connected to
guest tests. It forwards the packet to `func_15169260` as
`(&D_800A5770, 2, payload, command)`. Native tests compile the actual C wrapper
with SDK types and independently observe the forwarded fields. The queue
consumer is modeled; its production C placeholder and the rest of the parent
are not restored or claimed qualified by this work.

## Compiler recovery and remaining boundary

The first complete source emitted110 words/frame96. Declaring lookup scalars
before aggregates restores the original homes; retaining the meaningful record
index and command-pointer locals recovers frame104. The canonical private
source is `call-001-selected.c`, also stored literally in the recovery manifest.
Packet, sequences F9/F8/F7 and actor-only payload are at SP+4C,40,34,28 and24.
Ten other owner functions and all existing pools remain raw-identical.

The owner has five existing SDK pointer/integer diagnostics in unrelated
callbacks. Before/after diagnostics are compared after normalizing only the
fixture filename and shifted line numbers. Messages, statements and carets
remain exact; no warning is suppressed or introduced by the recovered function.
Actual Make dry-run confirms the existing O2/g3 profile.

Typed aggregate, pointer/first-member argument, explicit initialization, lookup
cast, switch and local-lifetime screens are retained in the private packet.
Ordinary common-call source is110 words. Per-case calls grow to117/119.
A reversed switch reaches113/frame104 but changes case layout, so equal size
does not qualify it. Literal nine-byte initializers create a duplicate data pool
and are not selected. No artificial padding, volatility or compiler override
has been added to the canonical source.

The main remaining question is the original per-arm A0 setup and second likely
dispatch branch. Retail's unvisited constant words are indices67,84,103; raw C's
are66,100. The three-word body gap is not justified merely by these dead words.
Full live-register/PC and complete control-flow equivalence remains open; public
agreement and the bounded memory-prefix checks below do not authorize71 literal
replacement rows or adoption.

## Fresh qualification

Primary tools and an isolated sibling overlay each pass five focused tests:

- 1032 cases per original/raw stream, including every byte kind, zero/high-bit
  masks, first/last/multiple/inactive actors, signed states, indexed record
  boundaries, dynamic template bytes and four effective instruction negatives.
  The original wrapper is executed, complete seeded public memory and observed
  payloads agree, and ABI saved state is preserved. Visited words are110/113
  retail and108/110 raw; static fingerprints retain every body word/binding.
- 1032 actual SDK32 native cases each at O0/O2/O3, strict aliasing and UBSan,
  with nine effective source controls per profile. SDK sizes812/160/9/12 are
  asserted. Byte snapshots cover records, actors, masks, templates, global
  pointers and queue storage. The actor-pointer payload is read through its
  declared type. Initial harness aliasing and callback-window API mistakes were
  corrected before the final fresh paired runs.
- Five representative memory-trace scenarios yield113 paired injected access
  boundaries with identical ordered traces, complete modeled memory/private
  bytes and helper observations. Those prefix probes model the helper opaquely;
  they do not claim literal GPR/PC fault-state identity or arbitrary-input proof.
- The original callback window and connected wrapper checks described above.

The real dirty `64CBFD Tools` sibling retains HEAD/status and343 dependency
hashes. The939-file overlay has339 same sibling files,594 explicit primary
fallbacks,5 task files and1 empty bootstrap. Dependency byte equality is checked
for all imported tool files apart from that bootstrap. `make tools-check` passes.
No host/frozen Release or older private actor-burst work changes.

Graphify's native update again refuses a shrinking corpus. A scoped four-file
AST merge retains prior IDs. The private manifest is linked explicitly to the
live GLOBAL_ASM annotation, not represented as an installed C definition.
Commit-hook writers are observed terminal before aliases/fingerprint sealing.
This is not full-corpus extraction. Routine work used zero Claude calls.

## Resume this function

1. Use the canonical110-word/frame104 source and five committed recovery tests;
   do not repeat the rejected declaration/cast/argument/switch screens without
   a new discriminating question.
2. Resolve the per-arm argument setup and likely-branch shape, or construct a
   complete CFG/live-role relation supporting a justified normalization. Preserve
   all three sequence buffers, packet/actor homes,14 bindings and dead words.
3. Only then qualify guards if needed, both padding paths, independent rebases,
   actual Make and strict full-image prediction. The original113-word routine
   remains live until installation passes those gates and a fresh recount.

Reproduction: `python3 -m unittest
tools.tests.test_game_map_record_dispatch_15104a80_recovery -v` under prepared WSL.
Ignored evidence: `conker/build/game-map-record-dispatch-15104a80-private/`.
