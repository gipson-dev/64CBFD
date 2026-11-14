# Game configurable particle recovery and original-frame milestone

Date: 2026-11-14. **Private candidate only: no installation, no new guards,
no exact-C credit.** `func_15175390` now has its complete semantic body,
the original **370-word / 1,480-byte length** and **0xB8-byte frame**.
It still differs in **201 words**. Production remains the committed
placeholder in `conker/src/game/generated_1A20A0.c`.

The retained proposal is `SELECTED` in
`tools/experiments/game_configurable_particle_15175390_recovery.py`.
It replaces only this body, adds a private typed record view and corrects
the owner's PRNG declaration to signed `s32`, consistent with the primary
header and PRNG assembly interface. Independent recompilation keeps all
**eight neighboring function bodies and named bindings**, including the
preceding two recoveries, unchanged. Normalized owner pools stay absent.

VA **0x15175390..0x15175958**, ROM **0x1A2840..0x1A2E08**.
Raw SHA-256:
`a1a342568e95cc18b0d7283e7966b7f36abc9c79a5cb8a8f838dd1ff17c8bbf5`.
The experiment rejects all **370 altered raw words and 27 altered named
bindings**. These pins protect this private milestone; they do not assert
identity with retail or authorize a binary replacement.

## Recovered interface and behavior

The void interface carries **18 words**: count, slot, X/Y/Z, outer radius,
view, vertical range, inner radius, flags, base type, type range, base model,
model mask, state, two float scales and ground flags. Five direct JALs occur
in the already recovered `func_15183290`, at ROM
`0x1B0930`, `0x1B0B08`, `0x1B0BBC`, `0x1B0C58`, `0x1B0CEC`.
The existing caller transports these exact 18-word packets and ignores a
return value. This milestone inventories the sites; connected caller
execution is still an adoption gate.

Flag 0x40 rejects nonpositive vertical ranges before heading/count work.
Flag 0x10000 captures a view-relative three-float vector and truncates the
heading helper's float return even when the later count is nonpositive.
The heading flag is cached across providers. For positive counts, the
inner radius is captured before the loop. An optional unsigned type-range
draw precedes allocation, so allocation failure can still consume it.

Each successful allocation captures the ground bit and tilt bit 0x20000,
then computes signed remainders using `outer - captured_inner`. Nonnegative
remainders add the inner radius; negative remainders subtract it. Each
coordinate then adds its live X/Z home with 32-bit wrap. The query gate is
exactly **state == 0 OR captured ground bit != 0**, verified from the
retail branch and its delay slot. The initial handwritten draft's reversed
ground condition was rejected and is an effective negative control.

State zero truncates the queried height. Other states retain the initial
Y when vertical range is zero, or add an unsigned vertical remainder to
the current Y home. The routine initializes slot/flags/state, positions,
10..24 lifetime, heading, optional tilt, rates and scale. Heading receives
at most one +/-360 correction. `D_800A7178` is loaded after its random
provider, while both scale words preserve their actual later home reads.

Model mask -1 reuses the earlier type offset; zero selects offset zero;
other masks take another random word and AND the **reloaded** mask. The
full 32-bit sum with base model indexes the 20-byte model table. Only the
stored variant byte narrows. Source coordinates/ranges narrow into their
original halfwords. The first record plays the eleven-word sound packet
only when the live base type is 10. A first non-type-10 record retains its
old handle; later records clear it. Grounded classification rereads the
record flag, adds 0x80, resolves the surface through signed /12 and maps its
kind byte. Final state bytes are cleared.

The query may return without writing the surface word at retail SP+0x80.
Those retained-stack cases have no portable C guarantee and are tested in
the retail stream only. If the query is skipped, the captured ground bit
is clear and classification does not consume that local. No source
initialization or guessed guard is added.

Local m2c output was advisory. Its inferred signed-byte model index and
pointer guesses are not adopted; the full index and captured flag/home
lifetimes come from primary assembly and measured provider mutations.
The authoritative replay is the committed proposal above, not the earlier
scratch screens, several of which predate the corrected query condition.

## Focused behavioral qualification

The mounted suite and the final isolated sibling overlay pass:

- **1,152 independent observable-memory/call comparisons**
  across retail and the candidate, including allocation failure, empty and
  negative counts, flags/states, aliased records, live argument mutations,
  type/model modes, and two stack phases.
- **63 additional source-stream cases** cover
  negative and large valid headings, the single-step wrap, negative scales,
  negative zero and negative scale ranges.
- **Eight emitted guest boundaries**: three actual `break 7` paths, both
  signed-overflow `break 6` paths and three invalid float conversions.
  These compare public memory/calls and dispatched boundary type; they are
  not native-C or full private-register/fault equivalence claims.
- **24 retail-only retained-surface cases**,
  covering zero/valid prior references, two states, aliases and stack phases.
- Effective wrong unsigned-remainder, ground-query-gate and first-sound
  controls fail by observable behavior. Unsupported-instruction failures
  are not accepted as negative-control evidence. Shared `make tools-check`
  passes.

The fixtures execute **366 / 370 retail words**.
The remaining offsets are `0x140`, `0x200`, `0x3a8`, `0x578`.
The candidate remains non-matching and uncredited. Native32, connected
caller/padder/rebase work and a candidate whole-image audit remain open.
No emulator, hardware, full provider or host-port acceptance is claimed.

The sibling remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` with all **2,439** dirty
paths preserved; before/after status SHA-256 is
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`. Four task files are replayed from the ignored
overlay with byte-identical contents. No sibling files/commits are changed.
Routine work uses zero Claude calls.

## Concrete fitting handoff

The raw stream keeps the signed divisor in S1 and puts the final Z sample
in S3. Retail overwrites/reuses S1 for Z after the second division checks.
The extra live saved role shifts X/Y/inner/counter allocation and spills
the tilt mask to **SP+0x70**, while retail keeps it in S7. Recover that
nonoverlapping divisor-to-Z lifetime first; do not describe all 201 words
as independent scheduling differences.

The transient heading already uses A0, saved at candidate **SP+0x88**
across the tilt RNG; retail uses **SP+0xA0**. Other private homes differ:
candidate vector **SP+0xAC/+0xB0/+0xB4**, heading **SP+0xA4**, surface
**SP+0xA8** versus retail **SP+0x88/+0x8C/+0x90**, **SP+0x9C**, **SP+0x80**.
The complete save/restore offsets and incoming homes already use the
original frame. Named-variable reuse found the original frame/length;
register keywords and simple block-scope moves did not resolve the live
saved-role conflict. Earlier variants and opcode-shape diagnostics remain
under `conker/build/game-configurable-particle-constructor-15175390-screen/`.

Next gates: recover the saved lifetime and exact homes/control forms, keep
the behavioral/corruption controls effective, then qualify native ABI,
actual caller windows, both padders/rebases, independent actual-Make image
prediction and production recount before adoption or matching credit.
Use the frozen production baseline; do not advance its pins speculatively.

All **805 frozen production inputs**, including
**698 objects**, **82 headers**, source, guards, conversion rows and ELF,
remain unchanged. ELF SHA-256: `f3bedd6992fd8680e7436464997937845a18b6786ba192fad13892a342545fc6`.
Fresh recount remains total **4,487 / 5,515 (81.36%)**, Game
**3,814 / 4,842 (78.77%)**, zero drift and **1,028** different C functions.
**201 more matching functions** reach 85% at the current denominator;
this is separate from this candidate's **201 different words**.

Scoped AST refresh covers the four tools files, retaining all
**60,698** old IDs in its final pass:
**60,698 nodes / 114,229 links**, zero lost nodes.
This is not full-corpus extraction. Tools commit `bd56233a36cafea6d81784ff0a61fbf743845592` banks the
private reconstruction and checks before this consumer handoff. The main
README's aggregate rows remain accurate and are unchanged. Keep the 85%
goal active; no push. Host sources are unavailable in `64CBFDOGL` here;
Release stays frozen.
