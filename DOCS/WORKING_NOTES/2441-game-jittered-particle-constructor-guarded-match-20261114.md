# Game jittered particle constructor guarded match

Date: 2026-11-14. `func_15174BF0` is recovered in
`conker/src/game/generated_1A20A0.c`. The complete **237-word / 948-byte**
routine spans **0x15174BF0..0x15174FA4**, ROM **0x1A20A0..0x1A2454**.
Raw and guarded C both use the original **0xD8-byte frame**.
**158 words emit directly from semantic C; 79 expected-word guards restore
private local homes, closed register roles and retail scheduling/control flow.**
This is not a direct C-only match. Eight neighboring placeholders remain
unchanged; the owner is now **1 / 9 byte-exact C functions**.

## Interface, fields and behavior

The void interface takes nine words: signed count, slot, X/Y/Z, view, float
base scale, float scale range and flags. The only direct JAL is
**0x151834D8 / ROM 0x1B0988**, in the newly recovered `func_15183290`.
Its **17-word success-window packet** is at 0x1518349C..0x151834E0. There
are no aligned literal pointers to the constructor. The caller already
declares the correct nine-word interface and ignores a return value.

The constructor first forms a three-float view-relative vector and calls
the shared `struct17` heading helper. It truncates the returned heading
even when count is zero or negative; those counts then allocate nothing.
Positive requests capture the external 0.01f rate coefficient and the
two float arguments, then allocate 0xF8-byte type-10 records until count
is reached or allocation fails. The explicit loop label preserves the
retail loop shape; the initially screened do/while form was too large.

Every successful allocation takes **eight random words**, in order:

1. X jitter in -63..64, added with 32-bit wrap to the captured X.
2. Z jitter in -63..64, added to the currently reloaded Z argument.
3. A signed halfword lifetime in 10..24; mode is a signed halfword 1.
4. Heading jitter in -15..16. A negative result adds 360 once; a result
   at least 360 subtracts 360 once. This is not full modulo reduction.
5. Initial tilt in -15..16; adjacent float fields become 0 and -1.
6. A signed byte-range value scaled by the captured coefficient.
7. A 16-bit fractional value scaled by range and added to base scale.
8. A one-bit variant selecting a model pointer from a 20-byte-stride table.

Only the first successful record submits the eleven-word sound packet;
later records receive a zero handle. The handle is **u16**, corroborated
by the updater's LHU loads, while lifetime/mode/record flags are signed
halfwords. Slot, variant and state fields are bytes, corroborated by LBU
consumers. The allocator's final two parameters are unsigned bytes.
The sound declaration intentionally describes full call-site transport
words; the provider performs its own narrowing. This preserves the retail
full-word coordinate stores and does not claim all unfinished provider
declarations have been reconciled globally.

Each allocation snapshots request flag bit 0 before the first random call.
When enabled, the routine rereads/sets record flag 0x80, calls the ground
query, converts its signed height to float and resolves the returned
surface through a signed /12 index. Surface flags choose one of four byte
codes. Without the request, surface flags/code are cleared while the height
field is retained. The two final state bytes are cleared. Other record
bytes and padding survive.

Captured X and integer/float Y survive helpers. Count, slot and Z retain
their actual argument-home reloads; the two scale arguments and external
coefficient are captured once. The private record view keeps uncertain
0xB0/0xB4/0xBC members neutral rather than asserting an unproved physical role.
The alternate auto-decomp was advisory; incorrect field widths and types
were replaced by primary assembly evidence.

## Early ground-query failure boundary

The original `func_1510F8D8` returns **-10000** when its initial lookup fails,
without writing its output pointer. The constructor then reads the existing
word at **SP+0x9C**. That word can be zero, a usable surface reference, or an
unmapped value. It is deliberately **not initialized** by this recovery.

The source records this behavior in a comment. Reading the unwritten local
has no portable C behavior guarantee. Those cases are qualified only in
the retail and guarded MIPS streams, with controlled prior stack contents.
The native harness always supplies initialized query outputs. The actual
215-word ground helper is connected through its **19-word failure path**,
with bounded context-reset and lookup providers, including the exact X/Z
lookup packet. This is partial provider qualification, not complete collision
or gameplay acceptance. Allocation, random and sound providers remain bounded.

## Normalization and focused qualification

The complete raw body and every named relocation are pinned. Raw SHA-256:
`ada7251ec22b14da6b1e59b38bfdafdbb22010d86bb67bd65e553118d9d8ca0f`.
All **237 raw-word corruptions** and one altered heading binding reject.

The frame, incoming homes, saved GPR/FPR offsets and outgoing argument area
remain fixed. The private surface local maps SP+0xC8 to SP+0x9C; the three
relative-vector floats map SP+0xCC/+0xD0/+0xD4 to SP+0xA4/+0xA8/+0xAC.
The four saved float roles are renamed only within their live body, preserving
the original saved-register restores. Closed temporary cycles and independent
coordinate/model/sound scheduling restore the original word order.

The surface lowering coalesces one repeated ordinary local load and merges
two mutually exclusive material shifts at a common successor. Its material
zero moves after the helper when changing from saved S1 to volatile V3.
The helper's arbitrary memory effects are represented in the symbolic proof;
both null/non-null paths agree, S1 is dead on all successors, and the complete
operation inventory permits only the declared load/shift/branch lowering.
An effective changed surface-code offset fails the proof. No word slots are
inserted or omitted. Raw C is not claimed to preserve private stack bytes,
instruction faults or every guest alias; guarded prefix identity is separate.

Mounted tools and the final isolated sibling overlay pass:

- **1,152 semantic cases across retail/raw/guarded streams**, including failed
  allocations, aliased records, varied material lookups, live argument-home
  mutations, helper writes and two stack phases.
- **72 authentic caller-window cases**, four invalid heading-conversion
  prefixes, **36 unwritten-output cases**, **36 real ground-helper failure
  cases**, **391 memory-cut prefixes**, and two unmapped-surface prefixes.
- **351 native32 cases each at O0/O2/O3**, with undefined-behavior trapping,
  including negative scales and large valid headings. Three wrong lifetime,
  repeated-sound and material-stride controls fail as intended.
- Both full-owner padders, all nine owner functions, four independent link
  layouts and **12 GNU link comparisons**. The eight non-target bodies and
  normalized pools remain identical. Shared `make tools-check` passes.
- Four additional directed guest cases independently cover all four material
  code indices. These are separate from the 1,152-case suite count above.

The sibling remains at `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, preserving all **2,439** dirty
paths; before/after status SHA-256 is `a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.
All six overlay files equal the mounted task files. Routine work used zero
Claude calls. No emulator, hardware or full provider/gameplay claim is made.

## Production audit and continuation

The shadow executes the three actual Make object commands and verifies its
complete compact owner against the independent compiler path. Production
equals the prediction exactly, ELF SHA-256:
`5e4d48f35a1080cbd1fa85a80c9f0a7b4d0ae1b37ce7e64b455f048fa718c6ba`.

The strict **872-byte** delta comprises this body/extent
and four reconstructed closed symbol/string permutations, with **zero
exclusions**. All **6,051 function addresses**, all **189,088 protected data
bytes**, **82 headers**, existing guards and conversion CSV rows stay fixed.
Only the target owner changes among **698 objects**. The production audit
checks **800 immutable input fingerprints**; 79 guard rows
append. The existing duplicate generated_12D630 Make recipe warning remains.
The owner gains `.rel.text` for recovered symbolic references; `.shstrtab`
adds that section name. Its complete padded object equals the independent
shadow object byte for byte, including the unchanged `.reginfo` section.

Actual recount: total **4,486 / 5,515 (81.34%)**, Game **3,813 / 4,842 (78.75%)**,
Init **492 / 492**, Debugger **181 / 181**, zero drift and **1,029** different
C functions. Converted totals are unchanged. **202** further matches reach
85% at the current denominator.

Scoped Graphify AST refresh retains all **60,576** previous node
IDs: **60,618 nodes / 114,098 links**, zero lost nodes.
It covers this owner and the six tools files, not full-corpus extraction.
Tools commit `d8844445960b70dcd3dd3cc0a74cb0d5020dbfb4` banks qualification before the consumer.
Private receipts are under `conker/build/game-ground-particle-constructor-15174bf0-screen/`.

Next: **`func_15174FA4`**, the 251-word companion constructor in this owner,
original **0x60-byte frame**, VA 0x15174FA4..0x15175390, ROM 0x1A2454..0x1A2840.
Recover its distinct packet and resource behavior before adoption. Keep the
85% goal active; no push. `64CBFDOGL` has no host source checkout available
here; no host adoption or runtime claim is made. Release remains frozen.
