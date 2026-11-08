# Sound Mask Selection Match - 2026-11-08

`func_1509F354` now matches all **74 words / 296 bytes** with the original
**0x30-byte frame**. The semantic C emits 76 words; **31 checked guards**
normalize register allocation and independent scheduling, including omission
of two explicit shift masks that MIPS SLLV already applies in hardware.
This is a guarded C match, with no compiler-profile or shared-header change.

Production recount: Total **4,255 / 5,513 (77.18%)**, Game **3,582 / 4,840
(74.01%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift and
**1,258** different converted functions. **156** additional exact functions
reach 4,411 / 5,513 and the active 80% goal. Conversion rows and denominators
are unchanged.

## Source and original interface

Owner: `conker/src/game/generated_CBDB0.c`. Retail VA
0x1509F354..0x1509F47C; ROM 0xCC804..0xCC92C.

```c
u32 func_1509F354(u32 first, u32 last, u32 mask, u32 volume,
                  s32 actorKey, s16 distance, u32 farDistance);
```

Seven physical O32 argument words are observed. The first helper,
`func_1505EEF4`, takes the full actor key from incoming SP+0x10 and returns
an existing `struct127` pointer. The body does not dereference it, so a
forward declaration suffices. The existing actor lookup scans the active
25-record table; `func_10010894` tests its sound state. Local declarations
match these providers without changing global headers.

Incoming A0/A1/A3 are saved in their homes, while the mask survives in S1.
The sixth word is read late as a signed low halfword at incoming SP+0x16;
the seventh word is reloaded in full at SP+0x18 after selection. Playback
uses the existing `func_10010344(u16, void *, s32, s16, u16)` interface:
the sound narrows to u16, the sixth word sign-extends, and the final physical
word remains full-width in the outgoing home before provider narrowing.

The pristine-image census finds one direct JAL at ROM **0xCC598**, VA
**0x1509F0E8**, in `func_1509EFF0`, and no aligned entry/interior pointer
literals or interior direct entries. Its 14-word original call window
extracts the low 12-bit end, reads mask/volume and both distance words,
and places word seven in the JAL delay slot. The original four-word
parent epilogue preserves the returned mask. **288 connected cases** cover
that original packet, result, SP, RA and restored S0. The parent C remains
a placeholder; full-parent or gameplay acceptance is not claimed.

## Recovered behavior and widths

Look up the actor first, then clamp the unsigned volume at 0x8000 to 0x7FFF.
Null lookup or nonzero busy result returns the incoming mask. A zero mask
becomes `0xFFFFFFFF >> ((-span) & 31)`, where span is the low byte of
`last - first + 1`; a span of 32 therefore enables all 32 bits.

Sample the full unsigned RNG result modulo the captured byte span. Retry
until the selected offset's modulo-32 bit is enabled. Reload the current
first sound, volume, actor spill and two late distance words, then submit
playback. Only successful playback toggles the selected bit out of the
returned mask. Failure preserves it.

The original zero-span path performs DIVU and reaches **BREAK 7 at
0x1509F418**. A mask with no reachable enabled bit can retry indefinitely.
These paths are preserved, with two guest trap cases and an eight-sample
nonterminating prefix; native valid-domain tests exclude both. Explicit
`& 31` C shifts avoid undefined native shift counts for offsets above 31.
Guest-only home/private-spill aliases remain separate from portable C
semantics and from the ordinary native fixtures.

## Normalization and owner proof

The default-mask ANDI/NEG order is equivalent modulo 32. The opening first
and end home reads move only across independent operations without an
intervening write or helper. A closed temporary-register mapping restores
the retail lifetimes. Two ANDI-31 instructions are omitted only at their
SLLV consumers; the final independent constant occupies the original branch
delay slot. All remaining operations survive, and branch displacements and
four call relocations are derived. Every raw word and binding is pinned;
76 altered-word and four altered-binding controls fail closed.

All **16** raw and padded neighbors, all pools and **41** original labels
are unchanged. The complete owner's GPR declaration adds S1 only
(0x00020000); an independently compiled isolated body has identical target
words and derives the exact owner-register union. All 72 single-byte
register-metadata corruptions are rejected. Both generated and strict
padders agree on all 17 function bodies and preserved metadata/labels.
The actual three-command Make recipe emits the identical padded owner with
zero compiler diagnostics, using the inherited O2/g3 MIPS2/O32 profile.

## Fresh and reused verification

Six focused checks pass before and after installation in both tools copies,
with four sequential runs and exact source/dependency fingerprints. The
sibling uses an isolated three-file overlay and explicitly records mounted
fallbacks for absent helpers; its **2,434 pre-existing dirty paths** are
fingerprinted and preserved.

- **2,214 guest cases**, including all byte spans, success/failure/null/busy
  exits, unsigned clamps, wrapping sound offsets, signed halfwords, repeated
  rejection and 16 late-home/private-spill mutation modes.
- All **74 original words** reached; normalized and pristine execution have
  identical literal state/read traces. The safe raw compiler stream also
  agrees on public effects, helper packets and returned masks.
- **105 memory-fault cuts** compare exact original/normalized prefixes.
- **2,180 native32 cases per profile**, at O0/O2/O3 with trapping UBSan;
  all **14** deliberate semantic controls are detected in each executable.
- Three independent GNU links, including rebased function/helper addresses,
  and **12** rebased guest executions qualify all four call bindings.
- Both fresh shared tools smoke checks pass. Three prior shared regression
  receipts per copy are reused only with identical helper/test fingerprints;
  these six reused checks are not represented as fresh executions.

The local guest oracle adds the required SLLV/SRLV/XOR operations and the
VR4300 DIVU-zero/BREAK model; shared execution helpers are unchanged.

## Complete image and production gate

An independent full-ELF predictor replaces only the target slot and its
symbol extent (12 -> 296 bytes). The actual linker output equals that image
byte for byte: **226 changed bytes, zero exclusions**. All **6,052**
disassembled entries retain their addresses and extents except this target's
expected extent. Every other linked function body is unchanged. Protected
data remains **720 owners / 189,088 bytes**, with no changed byte.

Production Make compiles only the selected owner, links the predicted ELF,
regenerates an identical progress CSV and passes a fresh matching recount.
`make all` still exits 2 at the existing whole-ROM checksum mismatch; this
function match does not claim a byte-exact complete ROM. The inherited
Make warning about generated_12D630's duplicate recipe is unchanged.

ELF SHA-256: `6fdb290ac4d80a5872aeb222a1729b5f240a09adafdbabf16daaa403fd217509`.
Binary SHA-256: `3dae96aaf752a3f97028e18f516980e939a9aa40f5a404978b0fea042a7a65c5`.
Owner SHA-256: `879862d4083066ae8be53df7b3389c59324400880b11d8c2fe7f8c3ffe605428`.
Guard CSV SHA-256: `944ed3d5d42a8d537e8730f76afa3da81d6806a5e8fd46391a3edd7cdb747f9b`.

## Resume boundary

Next candidate: **`func_150A03B0`**, 74 words with a 0x28-byte frame in
`generated_CD860.c`, VA 0x150A03B0..0x150A04D8 / ROM 0xCD860..0xCD988.
It remains a zero-return placeholder and is uncredited. Its six-command
switch has one entry pointer at ROM 0x22CFA0 and six protected interior
jump-table pointers at ROM 0x244010..0x244024; no direct J/JAL entry was
found. Graphify identifies its resource-status helper relationship.

Next work: qualify the original indirect dispatcher and three argument
words, command-dependent signed/unsigned record reads, six-word outgoing
packet, 999/zero/other state mapping, 0x34-byte record indexing, all returns,
protected jump-table labels, and the complete owner before adoption.
Scratch: `conker/build/game-record-dispatch-150A03B0-match/`.

Current receipts: `conker/build/game-sound-record-1509F354-match/`.
Tools are committed before the consumer pin. Graphify is refreshed with
changed-path and old-node-retention evidence; unscanned existing nodes are
retained, and this is not a fresh full-corpus extraction. Host frozen
Release artifacts are untouched.
