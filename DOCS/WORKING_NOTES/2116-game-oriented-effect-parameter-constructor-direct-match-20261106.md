# Oriented-effect parameter constructor directly recovered and matched

Date: 2026-11-06. Continue the 80% goal from consumer
`93e53de91df88b01eb47ff197e6b5720bbac5d12`, mounted tools
`5b305c06ce1d21b91b4e0956c45a5c33e7e18be7`, and
[Note 2115](2115-game-path-heading-turn-callback-guarded-match-20261106.md).

## Installed C and recovered interface

`func_150DBC60` matches all **68 words / 272 bytes** directly from semantic
C, using the existing **O2/g3/mips2/o32** profile. No guards, profile changes,
instruction insertion, or assembly substitutions are added. The original
**frame0x70**, saved RA at **SP+0x14**, descriptor at **SP+0x18**, late owner
byte read, and call-delay argument setup all emit naturally.

VA `0x150DBC60..0x150DBD70`; ROM `0x109110..0x109220`.
The false zero-return placeholder in `conker/src/game/generated_108E90.c`
becomes `void func_150DBC60(struct260 *owner)`. The existing `structs.h`
definition keeps the callback type compatible with `D_8008A4E8`; a byte view
reads owner offset0x0C without inventing a field name. Its input layout and helper prototype
are compatible with the already qualified oriented-effect factory
`func_15152F70(OrientedEffectInput *, u8)` from
[Note 1989](1989-oriented-effect-factory-guarded-match-20261102.md).
The exact four global HI/LO pairs and helper R26 give **nine bindings**.
Shared headers, helper owner, Makefile, original ASM, conversion inventory,
and the entire guarded-word manifest remain unchanged.

The constructor copies three global position floats, supplies the fourth
global as the field14 base, and sets speed to `7 + random*5`. Its count base1
and range2 select **one to three particles**. It retains the signed angle
bases -75/-38 and ranges22/35, the byte and short ranges, fixed flags, and
six integer submission arguments. The owner's unsigned mode byte0x0C is
read only after the descriptor stores. Unknown fields keep their existing
offset-based names rather than claiming an unproven gameplay meaning.

The descriptor is88 bytes. Retail leaves **four private bytes** at offsets
0x3A/0x3B/0x56/0x57 untouched. The C body therefore uses individual field
assignments rather than zero-initializing the structure. Guest tests compare
all88 seeded bytes; native C tests inspect only defined fields and verified
size/offsets, without promising portable padding contents.

The initial complete-owner screen had68 words/frame0x70 with21 differences.
Ordering the independent float assignments and signed halfword fields
recovered all allocations and schedules. Moving the two2.0f stores after
the halfword assignments removed the final eight differences. This is an
unguarded compiler match, not normalization credit.

## Qualification and boundaries

The focused eight-check suite passes before and after installation:

- **2,058 guest cases per body**, comparing retail, raw C and padded C:
  all256 modes, two stack phases, raw float bit patterns including signed
  zero/subnormal/infinity/NaN, provider mutations, the complete private
  descriptor, preserved ABI state and every constructor instruction.
- **528 alias cases per body** place the mode byte or global floats across
  the descriptor, preserving the early three loads, fourth load after the
  first position store, and final mode load. Every fired memory-access cut
  is compared literally across all three bodies (72 fired prefix pairs).
  These private-stack and
  fault-prefix experiments qualify guest instruction behavior, not portable
  C fault semantics.
- **64 cases per body** connect the complete original202-word oriented
  factory. An independent field/payload reference checks provider calls,
  all resulting descriptors/motion/header payloads, and all1/2/3 particle
  counts. This constructor reaches196 helper words; the five divisor traps
  and zero-count-only likely-delay RA load at0x1515307C are unreachable
  with countBase1/range2. RNG, float RNG, trig and final submission remain
  bounded opaque providers. No gameplay/hardware acceptance is implied.
- **2,048 cases per body** execute the complete45-word original record
  callback parent `func_15149264`, including its tick gate, callback0,
  signed -1 skip sentinel, owner-pointer ABI and discarded callback return.
  The qualified parent cases keep lifetime nonnegative; unrelated expiry
  cleanup is not claimed.
- **Nine independent GNU links** cover three address layouts, all nine
  relocations and HI/LO carry boundaries;51 guest cases per body execute
  those independently linked images.
- **76,800 native32 executions**, SDK types/layout, O0/O2/O3 and UBSan,
  check all defined fields and unsigned modes. Six semantic controls fail
  natively; seven fail under IDO/guest execution, including explicit
  clearing of the retail-private descriptor bytes.
- **272 raw-byte and nine binding corruptions** fail closed. Whole-image
  corruptions and the old zero-return stub are rejected.

The eleven other owner functions retain their complete bodies and bindings.
All compact data pools and all padded allocatable non-text sections remain
unchanged. IDO's compact `.reginfo` masks grow to describe the real float
body; the exact old/new24-byte records are pinned separately, not discarded.
The production GNU-padded owner has no unexplained metadata change.

Nineteen mounted shared checks and tools smoke pass. The separate dirty tools
sibling passes its twelve supported shared checks and smoke without edits.
Unchanged neighbor suites are reused through exact body/binding/pool identity,
not reported as newly executed. This routine target uses zero Claude calls.

## Literal production audit

The target build directory
`conker/build/game-oriented-effect-parameters-150DBC60-match/` retains
**99 frozen inputs** and the private/compiler/native/Make/image receipts.
The actual owner uses the production generated-slice padder and basename
`generated_108E90.c.o`. Actual Make equals the independently padded owner and
the literal **entire ELF** prediction with **zero excluded bytes**.

Exactly **353 ELF bytes** change:215 in the target slot and138 in metadata.
Metadata comprises the expected target size increase12→272 and six closed
GNU symbol/string hash-chain permutations. Every group pins its old names,
definitions, order, contiguous string block and resulting byte positions.
All named symbol values/definitions remain fixed except the target extent;
no blanket symbol-table or string-table exclusion is used.

All **6,052 executable addresses** remain fixed; only this body changes.
All **189,088 protected bytes across720 owners** remain exact. The complete
progress CSV and guard manifest are byte-identical to the predecessor.

| Artifact | SHA-256 |
| --- | --- |
| Production owner | `c9e60c82abe49e2403166ef1469a7cd47a4cd65f3ba306f4f1bfd89ffdb394b8` |
| Complete ELF | `a085abfe66c18a183f8cbe8464dd72a9df1557af1f0d67ec15282095fa3c95f4` |
| Code binary | `e1a600ba30719877d8dd75d7118672ba6ac4e9fa250f018d28fe591e372c5252` |
| Unchanged guards | `31a596ab2aed75f8e41e1119155b7381d597b7ae51ceda71eaa56b9c78854cd8` |

Production rebuild/recount takes **188.429 seconds**. The final typed
callback rebuild takes **179.191 seconds** and preserves the
entire owner and ELF byte-for-byte. The earlier `make all` checksum receipt
is reused through that complete-image identity; it is not a fresh second run.
`make -C conker all` reaches the known incomplete-project retail checksum
mismatch (exit2). Source newline styles and historical notes are preserved.
The root README changes only aggregate matching rows.

## Progress and continuation

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,186 / 5,512 | 75.94% | 0 | 1,326 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,513 / 4,839 | 72.60% | 0 | 1,326 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The converted inventory stays5,512/6,046. The80% threshold is4,410,
leaving **224 more exact functions**. Continue with **func_150D01A0**,
subject to its caller/ABI and complete-owner qualification. It is uncredited.

Retain the eight separate boundaries from Note2103: func_150A76F0,
func_151F8870, func_150A613C, func_150AE280, func_15115F68,
func_151AE2BC, func_150A6760 and func_150A70C0. Preserve sibling dirty
work, private inputs, real saves and frozen host Release. The80% goal stays
active; this checkpoint adds no host-port gameplay acceptance.

## Graphify audit

Graphify was queried before the constructor source screen and again for the next target. The ordinary update refused to replace the existing 58,854-node graph with its smaller 25,057-node reconstruction. The established scoped AST refresh preserves old nodes and requires explicit accounting for removed or relocated IDs; no force overwrite or extraction-policy change is used.

The scan retains 31,816 legacy nodes from 3,754 existing files outside the current detected corpus. This is a scoped refresh with retention auditing, not a full-corpus re-extraction claim. As in Note 2115, unmarked legacy type edges may remain stale; recovered C, original instructions and ABI qualification remain authoritative.
