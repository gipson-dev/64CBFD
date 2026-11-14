# Game minimum-height particle constructor direct match

Date: 2026-11-14. `func_15174FA4` is recovered in
`conker/src/game/generated_1A20A0.c`. All **251 words / 1,004 bytes emit
directly from semantic C**, with **no new guards** and the original
**0x60-byte frame**. VA **0x15174FA4..0x15175390**, ROM
**0x1A2454..0x1A2840**. The owner is now **2 / 9 exact**; all eight
non-target bodies, including the previous guarded recovery, stay fixed.

## Recovered contract and behavior

The void interface takes ten transport words: count, slot, X/Y/Z, signed
spread width, unused view, elevated-mode word and two float scale values.
The seventh word is carried by the callers but never read by this routine.
Both direct JALs are in `func_15183290`: **0x15183548 / ROM 0x1B09F8** and
**0x151835A8 / ROM 0x1B0A58**. The authentic success windows cover 19 and
20 words. No aligned literal pointer to the constructor appears in the image.
The existing recovered caller declaration already describes the ten-word
interface and ignores a return value.

Mode zero calls `func_1510F800(0)` before the count test, even for zero or
negative requests. X/Y are captured before that helper; Z is captured after
it, and the spread width is captured before the allocation loop. Count,
slot, mode and both float arguments retain their measured live home reads.
Guest-only helper mutations qualify those reads; they are not a portable
C promise that external functions may modify arbitrary caller frames.

Each positive request allocates a **0xF8-byte type-19** record with the
original six-word allocator packet. Allocation failure stops the batch.
Seven random words set, in order:

1. X offset by unsigned remainder with the width, minus arithmetic width/2.
2. Z offset by the same rule. Both coordinate additions wrap at 32 bits.
3. Signed halfword lifetime in 4..6, with mode halfword zero.
4. Tilt in -15..16.
5. Unsigned-remainder heading in 0..359.
6. A second signed -15..16 float; adjacent fields become 0, 0 and 3.
7. The fractional scale, with the live scale-range/base words loaded after
   this random provider returns.

The model is loaded from `D_800DDF14`; the variant byte becomes 7. The
X/Z lookup returns a signed candidate count. Zero releases the newly
allocated record with `func_1516979C` and still advances the attempt count.
Every nonzero count reads the first 16-byte height entry; counts above one
scan the remaining entries for the **signed minimum**. The recovered
indexed loop emits the original four-entry unroll and signed comparisons.
A negative nonzero count therefore still selects the first entry.

The selected 24.8 height is arithmetically shifted right by eight before
float conversion. Mode zero sets state byte 0, height+10 and flags halfword
1. Any nonzero mode sets state byte 2 and flags 4, then takes two additional
random values to initialize the two independent height fields at 300..427
above the minimum. It copies the narrowed X/Z/half-width fields and clears the
original float, halfword, word and byte state members. Other bytes are not
initialized by this constructor; lookup failure skips these trailing stores.

The local record view keeps uncertain members neutral (`fieldB0`,
`fieldCC`, and so on). The signed fixed-height and 16-byte stride agree
with the primary query consumers. LBU/LH/LWC1 consumers corroborate the
byte, signed-halfword and float views. The release prototype uses the
existing `struct102` ABI; the allocator retains its unsigned-byte tail.

Explicit captured coordinates, statement order and the original integer
versus float zero assignments recover the retail saved-register roles and
two separate zero-FPR lifetimes. No compiler-profile or Makefile change is
needed. Complete raw code SHA-256:
`f075622b60e5cbcdf8a0271f520e1d7e2c939db7f32c301379e27c16046121c2`.

The preceding constructor's behavior receipts are reused after verifying
the identical raw body, named bindings, normalized pools and padded neighbor
bodies. The fresh suite below qualifies this newly recovered constructor.

## Qualification and boundaries

Mounted tools and the isolated sibling overlay both pass the complete
focused suite:

- **1,152 independent guest-model cases**, covering empty,
  negative and multiple requests; allocation failure; zero, negative and
  1/2/3/4/5/9 height counts; aliased records; helper mutations; positive and
  negative widths; wrapping coordinates; and two stack phases.
- **48 authentic caller-window cases**, both ten-word
  packets, **4 dispatched zero-width `break 7` paths**,
  and **324 complete memory-cut prefix comparisons**.
- **507 native32 cases each at O0/O2/O3**, with undefined-behavior
  trapping and full retained-record-byte/call-packet checks. Wrong minimum,
  mode and fixed-point-shift controls fail effectively.
- **251 raw-word and 21 relocation-binding corruption controls**, both
  full-owner padders, all nine functions, four independent layouts and
  **12 GNU link comparisons**. Shared `make tools-check` passes.

The guest cases visit **246 / 251 words**. The unchanged second zero-width
trap, three unsigned-float fallback words and duplicate likely-branch
store cannot be reached by these valid provider contracts. Their exact
words remain covered by full literal comparison and the corruption sweep.
The unvisited offsets are `0x104`, `0x178`, `0x17c`, `0x180`, `0x330`.

Width zero is undefined for portable C remainder. Its actual IDO output
retains the retail division and explicit `break 7`; those cases are
guest-only, not executed by native C. Providers remain bounded contracts,
not complete collision/allocation/release implementations. No emulator,
hardware or gameplay acceptance is claimed.

The sibling stays at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, preserving all **2,439** dirty
paths. Before/after status SHA-256:
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`. All five task-overlay files equal the mounted
files; no sibling checkout edits or commits are made. Zero Claude calls.

## Production evidence and next target

The independent shadow executes all three actual Make object commands;
its complete compact owner equals the independent compiler path. The
production padded owner and linked ELF equal the shadow prediction.
ELF SHA-256: `f3bedd6992fd8680e7436464997937845a18b6786ba192fad13892a342545fc6`.

The strict **815-byte** image delta contains this
body/extent and two reconstructed closed symbol/string permutations, with
**zero exclusions**. All **6,051 function addresses**, **189,088 protected
data bytes**, **82 headers**, existing guards and conversion rows stay fixed.
Only this owner changes among **698 objects**. The installed audit checks
**802 immutable fingerprints**. No guard CSV,
Makefile, compiler or shared-core tool changes are included. The preexisting
duplicate generated_12D630 Make recipe warning remains.

Fresh recount: total **4,487 / 5,515 (81.36%)**, Game **3,814 / 4,842 (78.77%)**,
Init **492 / 492**, Debugger **181 / 181**, zero drift and **1,028** different
C functions. Converted totals remain fixed. **201** further matches reach
85% at the current denominator.

Scoped Graphify AST merge retains all **60,624** old node
IDs: **60,660 nodes / 114,166 links**, zero lost nodes.
It covers this owner and five task tools files, not full-corpus extraction.
Tools commit `1e00379a70afc25381ed01d59ace569db9185523` banks qualification before the consumer.
Private receipts: `conker/build/game-height-particle-constructor-15174fa4-screen/`.

Next: **`func_15175390`**, the 370-word constructor in this owner, frame
**0xB8**, VA **0x15175390..0x15175958**, ROM **0x1A2840..0x1A2E08**.
Recover its distinct 18-word packet before credit. Keep the 85% goal active;
no push. `64CBFDOGL` has no host source checkout here; no host adoption is
claimed. Release remains frozen.
