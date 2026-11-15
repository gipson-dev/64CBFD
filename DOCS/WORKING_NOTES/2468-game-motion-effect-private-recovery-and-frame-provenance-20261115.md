# Private motion-gated effect recovery and compiler frame provenance

Date: 2026-11-15. Continue the 85% total exact-C goal from
[Note 2467](2467-game-radial-effect-guarded-match-and-frame-provenance-20261115.md).
The next target is **`func_150C2C00`**, VA **0x150C2C00..0x150C2FCC**, ROM
**0xF00B0..0xF047C**, **243 words / 972 bytes**, original **0xE8 frame**.

The complete routine is recovered as ordinary C and qualified in the finite
domain below. **It remains private, uninstalled and uncredited.** Production
`conker/src/game_EF410.c` retains its placeholder. All **843 frozen production
inputs**, including every production object, ELF, header, conversion CSV and
guard manifest, remain byte-identical. Root README is unchanged. This note
banks semantic recovery and compiler evidence, not another byte-exact match.

## Recovered behavior and packet

The routine takes an owner pointer and returns void. It adds
`(((randomFloat * 20) * D_800A02C0) * D_800BE9A4) * D_800A02C4`
to owner float **0x28**. Each arithmetic operation remains single precision
and in the original association. The coefficient words come from ROM
**0x244D80..0x244DD0**, not guessed host constants.

When the accumulator exceeds **1.0f**, `func_15144B34(D_80082FA4)` supplies
a motion pointer. If its X/Z squared magnitude does not exceed
**D_800A02C8**, the routine consumes units until the live accumulator is at
most one. Otherwise it initializes the effect packet and repeatedly attempts
emission. Each attempt draws a heading, obtains the motion angle, and compares
their difference with a cached angular limit. A rejected heading still consumes
one unit. Helpers may change owner data; the final decrement and loop test
reload the live accumulator rather than using a precomputed iteration count.

An accepted attempt derives packet X/Z through `func_1514373C`, draws the two
size scales, duration and color, then calls
`func_15149550(&packet, 10, 1, 0, owner[0xC], owner[1])`. The owner bytes are
read late. Duration is **unsigned random % 151 + 50**; the first second-color
byte is **unsigned random % 156 + 100**. A successful constructor receives
the four-byte heading at result **0x160**, using the original `memcpy` interface.
Allocation failure skips that copy and still consumes the attempt.

The existing **72-byte `RadialEffectPacket150C29F0`** layout is reused because
it is passed to the same constructor. Its three padding bytes **0x35..0x37**
remain uninitialized. This variant fixes Y to **-390.0f**, codes to
**0x6231 / 0x1A4D**, word **0x30** to mode **4**, kind byte **0x34** to **25**,
and value **0x3C** to zero. The inherited `zero30` field name is explained
locally: this variant sets it to four. The five scale-dependent floats and
value **0x38** retain their original ordered arithmetic and live coefficient
reads. Heading base, heading scale, angle limit and effect scale are captured
before the loop, as are packet values **0x40 / 0x44**.

No shared declaration, compiler profile, Makefile, classification or guard
manifest is changed. The private source includes the proper string prototype,
uses a pointer-returning constructor, and removes the obsolete local `s32`
placeholder declaration only in its private generated owner.

## Guest, helper and caller evidence

The complete retail and compiled private routines pass **576 finite cases /
two streams**. Cases cover accumulator boundaries including the next float
above one, zero/positive timing, motion below/at/above the threshold, accepted,
rejected and alternating heading tests, null/successful creation, high-bit
integer random results, two stack phases and helper mutations of live owner,
motion, selector and coefficient data. Allocation outcome is fixed per case;
alternating per-call allocation outcomes are not yet qualified.

The corpus observes **104 emissions / 51 successful heading copies**, with
zero through four emissions in a case. Checks compare the complete external
fixture memory, normalized call arguments and order, all **69 defined packet
bytes**, copied heading and callee-saved register restoration. Motion, owner,
output and stack fixture ranges are separate. The guest corpus was rerun after
correcting an initial fixture address that fell in the stack exclusion range;
the final checks include the complete motion backing. Four effective instruction
controls reject wrong duration/color ranges, constructor kind and owner byte.

All **241 reachable retail target words** and all **242 raw target words**
execute. The two unvisited retail words are unreachable division-by-zero
`break 7` checks for the fixed nonzero ranges. They are still required for
matching and are not omitted from the retail extent.

The original **22-word `func_1514373C`** and **11-word `memcpy`** bodies
execute completely in both streams. The polar helper's actual cosine-then-sine
call sequence and two output pointers are checked. Trigonometric providers,
random generation, motion lookup, angle/difference helpers and the effect
constructor remain bounded models; this is not physical trigonometry or
complete constructor/gameplay acceptance.

The entry census finds no direct Game JAL and one aligned entry pointer at
ROM **0x22EFF0**, **D_8008A4E8[18]**. The complete original **45-word
`func_15149264`** parent passes **384 cases / two streams**, dispatching through
JALR **0x151492B0**. Its exercised route visits **30 parent words**, covers
both timer-decrement choices, reloads owner state after the callback and
retains the positive timer. Wrong table slot and wrong callback argument
controls reject. Expiry/free routes are not covered by this caller test.

Private stack addresses are normalized for these semantic comparisons.
Literal frame equality, access-prefix/fault-state equality, owner/output/stack
aliases, exceptional FP/FCSR behavior and 64-bit FP-register semantics remain
unqualified. No finite-output or visited-word count substitutes for those gates.

## Actual native C execution

SDK32 **O0 / O2 / O3** each compile and execute the actual private C over all
**576 cases**, with undefined-behavior traps and **eight effective compiled
source controls**. The checks cover the **160-byte owner backing**, **64-byte
motion backing**, **448-byte result backing**, twenty coefficient words,
selector, side-effect marker, exact call script, 69 defined packet bytes and
success/failure copy counts. Typed float/halfword fields are normalized for
the native host's byte order; surrounding bytes are checked individually.

Controls reject altered accumulator threshold, motion norm, duration range,
color range, constructor kind, owner byte, heading destination and live reload
of values that retail caches before the loop. Tests preserve padding's
undefined status. This qualifies the finite C behavior and ABI layout; native
exceptional arithmetic and literal MIPS stack behavior are not claimed.

## Open fit and compiler provenance

The full private owner compiles under the existing **O2/g3/mips2/o32** profile.
All **17 non-target functions**, normalized bindings and owner pools remain
unchanged. The target emits **242 words / frame 0x100**, with **210 positional
word differences** after its **58** normal relocations are bound.

Raw body SHA-256:
`c415c48e08302436ec8568feed4685035a67cc8deb8fdd7a16eaee9647a01cc0`.

Canonical raw layout is packet **SP+0xB8**, heading **SP+0xB4**, RA
**SP+0x74**, owner in S2 and motion in S3. Retail instead uses packet
**SP+0x94**, heading **SP+0x8C**, RA **SP+0x6C**, owner in S3 and motion in S2.
The raw loop hoists four coefficient-address bases into saved registers,
including S8. Retail instead keeps the duration/color ranges in S5/S6 and
heading address in S7. Merely introducing named integer ranges does not
recover that allocation.

A fingerprint-locked owned CFE/UOPT/UGEN trace completed with fired observation
gates, producer/driver exits and two effective negative controls. Observed and
normal emitted code, relocations and pools are identical; complete object
metadata identity is not claimed. UGEN frame reservations progress
**0 -> 96 saved -> 120 after 24 outgoing -> 256 after 136 locals**.
CFE's M reservation is **128 bytes**; UOPT's is **136**. These reservations
are distinguished from the physical byte count written by save instructions.

Twelve diagnostic source/profile forms and their **24 C/object hashes** are
retained separately from the qualified canonical owner:

| Diagnostic | Words | Frame | Positional differences |
| --- | ---: | ---: | ---: |
| Canonical and split-assignment/angle forms | 242 | 0x100 | 210 |
| Named modulo ranges | 242 | 0x108 | 210 |
| O2 with loop unrolling disabled | 242 | 0x100 | 210 |
| O1 | 250 | 0xA8 | 250 |
| Inline motion norm, removing three locals | 242 | 0xF8 | 212 |
| Earlier accumulator pointer | 241 | 0xF8 | 236 |
| Reordered live local declarations | 241 | 0xF8 | 236 |
| Scoped constructor result | 242 | 0xF8 | 232 |

The isolated canonical body hash equals the full-owner target hash, so those
shape comparisons use the same compiler input context. The smaller-frame
diagnostics are not installed or credited and do not inherit the canonical
source's semantic qualification. There are no new word guards.

## Checks, preserved state and next action

Fresh complete private suites pass mounted in **67.774 seconds** and through
the sibling overlay in **77.715 seconds**. Each run recompiles the full owner
and executes every native profile. `make tools-check` passes. Routine Claude
calls: zero. Tools commit **`ddd87336d54ec02a5d4b821b3330ba6a628eba17`** precedes
the consumer documentation/pin commit.

The five-file ignored overlay preserves sibling HEAD
**`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`** and all **2,434 Windows-Git dirty
paths**, raw status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Scoped Graphify extraction covers five Python files, retains all **61,609 old
IDs** and records **61,649 nodes / 115,618 links**, zero lost IDs. It is not
a full-corpus extraction.

The production ELF remains
`6ead78c1257966a133ada96e0272f1ce476fb9eb167b5ded57091e56ce87628d`.
The previous actual production recount remains applicable because the complete
ELF and classification inputs are unchanged: total **4,502 / 5,514 (81.65%)**,
Game **3,829 / 4,841 (79.10%)**, zero drift, **185** further matches to 85%.
No fresh production build/recount or full-image adoption audit is claimed for
this private-only work. All evidence remains under
`conker/build/game-motion-effect-150c2c00-private/`.

Next, keep this function. Start with the measured local-reservation reduction
and compare actual CFE/UOPT lifetimes and saved coefficient-address bases.
Recover **243 words / frame 0xE8**, the original homes, range-register lifetime
and arithmetic/access order. Then qualify aliases, mixed allocation outcomes,
exceptional/order and literal state boundaries, both padders, independent
rebases, actual Make, strict image, production audit and recount before adoption.
The host path still contains only scratch `.codex` / `recomp_scene` directories;
no host import/build is made and frozen Release is untouched. No push. The
85% goal remains active.
