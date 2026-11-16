# Game scaled argument packet recovery and ordered FP proof - 2026-11-15

`func_151A1010` now has maintained private C recoveries, a complete ordered
FP/call-transfer proof for one source form, and fresh guest/native checks in
both tools configurations. It is **not installed or byte-matched**. The original
111-word / frame `0x78` routine remains the next matching target.

Production remains **4,514 / 5,514 (81.86%)**, Game **3,841 / 4,841 (79.34%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift and 1,000 different.
The unchanged 85% goal needs **173** further verified functions. A fresh recount
of the actual production ELF confirms these numbers; no private credit is added.

## Target, baseline and recovered behavior

Owner: `conker/src/game/generated_1CC440.c`, still the zero-return placeholder
at line 940. Retail VA `0x151A1010..0x151A11CC`, ROM `0x1CE4C0..0x1CE67C`.
Consumer baseline `ebff7c5f9c1037d64137abb8186b641e008fb0e7`, tools baseline
`04135f783813cb178d9b1c873c46ddefda59bf12`. A new immutable 887-input snapshot
includes the original `D_800A8D28` data definition. It is not overwritten or
re-frozen as qualification proceeds.

The routine submits 28 arguments to the existing `func_151A11CC` retail stub.
Its first two floats travel in F12/F14, the next float bit pattern and span in
A2/A3, and the remaining incoming values in their o32 stack homes. The private
signature is `void(f32 x, f32 y, f32 value, s16 span, f32 scale, f32 rate,
u8 variant, s32 flags)`.

The void return remains a **type hypothesis**, consistent with the neighboring
void wrappers and absence of an explicit result after the final void call.
The symbolic contract does not treat residual V0 as a returned value. Static
inspection found no aligned direct J/JAL or literal pointer references to this
entry anywhere in the retail blob. That finite census does not disprove computed
runtime references or establish all caller types. No caller was fabricated.

The adjusted span is signed-16 wrap of `span - 32`. One outgoing argument uses
`max(1, adjustedSpan)`; the final span argument uses **original adjustedSpan + 16**
as a full signed word, without a second short narrowing. The variant is an
unsigned low byte and flags retain all 32 bits.

| Values | Recovered conversion and use |
| --- | --- |
| x, y, value | First three outgoing float values, unchanged |
| 250 * scale | Fourth float argument; stays floating point |
| 70 * rate, 30 * rate | Truncate to signed 32, then narrow to signed 16; reused |
| 1500 * scale, 100 * scale | Truncate to signed 32, then narrow to signed 16; reused |
| 90 * rate, 20 * rate | Full signed-32 truncations, with no short narrowing |
| 15 * scale, 10 * scale | Full signed-32 truncations, with no short narrowing |
| 1.0, 18, 16 | Original fixed packet constants |

The 1500.0f multiplier uses original immutable `D_800A8D28` (`0x44BB8000`),
keeping the owner's existing 16-byte normalized pools intact. Direct out-of-range
float-to-short conversion is deliberately avoided: explicit float-to-s32 followed
by integer narrowing preserves the target behavior and the tested native domain.

## Two private source forms and the remaining matching boundary

The original local-variable recovery emits **109 words / frame 0x78**, with
**103 positional differences** from retail. It agrees numerically on the packet
but moves the 1500 multiplication ahead of the original 250 multiplication.
The independent ordered transfer checker rejects it. Numeric agreement does
not qualify its FP/FCSR behavior.

Updating the span formal and expressing the packet arithmetic at the call
recovers retail's complete **17-operation FP sequence**: nine multiplies and
eight truncations, with the same operand order and status transitions. It emits
**109 words / frame 0x80**, with **111 positional differences** including the
two missing positions. IDO promotes the modified span into S0, saving/restoring
it and growing the frame by eight bytes. This is not two independent missing
NOPs: frame, saved span lifetime, allocation and schedule remain coupled.

Raw original-frame SHA-256:
`43b4a0fc8bfa77b038f2fdd7b1e7222b02b10f594eff0e1547cde05740482086`.
Raw ordered-FP SHA-256:
`805a4775e6c8c266ecdee864535c46d0be42e336a92258501a53de3d5ccdd809`.

Both maintained sources preserve all **38 raw owner neighbors** and normalized
pools when compiled with the existing retail O2/g3 owner profile. Bounded
expression, clamp-width, parameter-width and span-lifetime screens are retained
privately. They supply diagnostics rather than accepted substitutes for the
remaining frame/allocation problem. No normalization mapping or guards are added.

## Fresh qualification and its limits

The instruction-driven symbolic checker covers both clamp paths, all reachable
**109 raw / 111 retail words**, all 28 outgoing arguments, original incoming
homes, saved ABI and return-address custody. FP values and FCSR transitions are
opaque symbolic terms keyed by the actual opcode, ordered operands and prior
status. No floating commutation or numeric approximation is used by the proof.
Signed-short reductions use exact low-16 linear arithmetic and signed extension.

Two provider contracts are checked separately: the real retail stub and an
opaque o32 provider that may clobber every caller register, all 28 argument homes
and FCSR. Six effective instruction corruptions are rejected, covering span
subtraction, clamp value, FP operand order, return save, byte signedness and the
unclamped final offset. An independent S0/S1 allocation swap is accepted as a
positive control. The checker is independent of any normalizer or register map.

This proves the normal-execution typed call relation under the stated **void
ABI hypothesis**, mapped private stacks and immutable literal contract. Private
frame sizes may differ in this semantic checker. Providers cannot inspect code,
return PCs or unpassed private bytes. It is not a proof of original frame/private
byte identity, raw fault registers, trapping hardware behavior, portable undefined
inputs, runtime reachability or gameplay acceptance.

Fresh guest execution checks **528 cases per three streams**: original retail,
the original-frame recovery and the ordered-FP recovery. It executes the actual
six retail callee words, whose production body remains exact, and checks all
28 arguments, all 256 variant bytes, signed-short wrap/clamp boundaries, selected
noncanonical high-bit argument words, wider full-32 products, saved ABI and both
stack phases. Every target word is visited across the corpus.

Native32 checks both source forms across O0/O2/O3 with strict aliasing enabled
and disabled: **12 profiles**, each with **496 guest-checked vectors plus all
65,536 representable short inputs**. That is **66,032 cases per profile / 792,384
per tools configuration**. UBSan and float-cast-overflow traps are enabled.
The valid domain is finite float inputs/intermediates inside the s32 truncation
range, with target two's-complement integer narrowing. Four effective source
controls reject direct float-to-short casts, clamped final-span reuse, narrowing
a full-32 result and signed variant handling. Native checks do not substitute
for the emitted guest FP/FCSR proof.

The maintained four-test suite passes freshly in the primary tools checkout
(**66.973 s**) and sibling overlay (**79.221 s**), with identical six task-file
fingerprints. `make tools-check` passes separately. Zero Claude calls were used.
The sibling remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with all **2,434**
dirty paths and their Windows Git status fingerprint unchanged. Its files are
not overwritten; the six task files are supplied through an isolated overlay.

## Preservation, receipts and continuation

All **887 production inputs** remain byte-identical, including source, guard
CSV, every frozen object, layout, progress CSV and ELF. The production ELF stays
`7c7e434c3e4e3e805094513bb5deb44b44f7611eb67623b4f1d134c503cceb7f`.
Prior accepted-function, linked-image and protected-data receipts remain valid
because their inputs are unchanged; they are reused explicitly, not called fresh
rebuilds. No production Make/adoption or both-padder pass is claimed for this
uninstalled recovery. Host-port Release artifacts and saves are untouched.

Maintained tools use the `game_scaled_argument_packet_151a1010_` prefix. Sources
live in its manifest, with owner/provenance compilation, guest, native32 and
independent symbolic checkers. Receipts and rejected source diagnostics remain in
`conker/build/game-scaled-argument-packet-151a1010-private/`. Root README aggregate
rows stay unchanged; detailed recovery updates belong here and in concise DOCS
indexes. Native Graphify update refused a shrinking replacement and retained
all 62,772 old IDs. The scoped five-file AST merge and explicit source reference
retain those IDs and produce **62,816 nodes / 117,931 links** before the consumer
commit hook. Post-hook retention is checked separately; no force, upgrade or
full-corpus extraction is claimed.

```sh
python3 -m unittest tools.tests.test_game_scaled_argument_packet_151a1010_recovery -v
make tools-check
# Recount from 64CBFD/conker:
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

Next: retain the exact FP sequence while recovering the retail `0x78` frame and
span lifetime, then resolve the 109-versus-111-word allocation/scheduling gap.
Finish the return/caller contract before adoption, qualify any proposed
normalization independently, and complete both-padder, rebase, strict whole-image,
actual Make, production audit/recount and documentation gates. Keep the same
target and the wider 85% goal active; this recovery receives **zero new matches**.
