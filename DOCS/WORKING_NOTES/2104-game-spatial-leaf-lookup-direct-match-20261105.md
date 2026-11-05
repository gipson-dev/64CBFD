# Spatial leaf lookup directly recovered with a consistent pointer interface

Date: 2026-11-05. Target `func_1510FD20`, owner `generated_13BB20`.
Source `conker/src/game/generated_13BB20.c`; original `conker/asm/13BB20.s`.

## Result and spatial record contract

All **68 words / 272 bytes** emit directly from C with **no frame, no
alignment tail, no guards and two bindings**. VA is
`0x1510FD20..0x1510FE30`; ROM is `0x13D1D0..0x13D2E0`. All thirteen
compact and padded owner neighbors remain unchanged, including the existing
`GLOBAL_ASM` body. Existing O2/g3 compiler options and every guard byte stay
fixed; all allocatable compact and padded non-text sections are identical.

The function returns the first spatial leaf containing the incoming signed
32-bit X/Z point, or NULL. `D_800DBE48` holds the root pointer. Each record
has a signed halfword sibling offset at +4, an unsigned halfword radius at
+6, signed halfword X/Z centers at +8/+10, and a signed child offset at +12.
Offsets are relative to the current byte address, not record indices.

The child field is loaded before bounds testing. Internal and leaf paths
retain separate inclusive bounds tests. A containing internal node follows
its child; a containing leaf returns immediately. A rejected node follows
its nonzero sibling offset; a zero sibling terminates. The second-axis load
is skipped when X already rejects the point. Negative child and sibling
offsets, overlapping leaves, empty roots, nested paths and dead ends are
qualified without inventing a record stride or graph scan limit.

The scoped `SPATIAL_ABS_13BB20` macro recovers the original compiler lifetime
and is undefined immediately afterward. Unsigned subtraction and negation,
followed by the original signed word interpretation, preserve two's-complement
wrapping without signed overflow. In particular, the absolute value of
INT_MIN remains negative, so the original signed bound comparison accepts
that axis. The independent model and native controls explicitly exercise
this counterintuitive retail behavior. The prepared IDO/GCC32 signed word
representation is qualified; arbitrary host64 pointer/long layouts are not.

Named intermediate distances initially caused a 69th coordinate copy;
direct expressions remove it and recover every original register word.
No instruction contraction, scheduling patch, inline assembly or compiler
profile exception is used.

## Pointer interface and complete caller qualification

The recovered signature is `u8 *func_1510FD20(s32 x, s32 z)`. The owner now
uses that full forward declaration. The shared functions header and local
declarations in `generated_10E240` and `generated_1B6DB0` also declare the
pointer result. Seven assignments in those two owners, `game_40490`,
`game_3DB80` and `game_3E460` explicitly cast that pointer to their existing
32-bit spatial-handle fields. Their original field layouts and stored bits
are preserved rather than guessing wider structure definitions.

A complete aligned retail census finds **26 direct calls across fourteen
owners**, with no direct tail jump or aligned function-address literal.
Before/after compilation against private old/new header overlays preserves
**217 functions across the thirteen other caller owners**, including their
bindings and every allocatable non-text byte. The current owner's thirteen
neighbors qualify its own `func_1510FC34` caller separately. Actual production
Make also preserves all thirteen complete other caller object files.

All 26 original JAL/delay-slot boundaries connect to original, natural and
padded target instructions for **104 cases per body**. Actual delay-slot
halfword loads, the immediate coordinate, no-ops and the view-coordinate
floating store are retained; effective incoming words and returned leaf
pointers are checked. Complete parent functions, their opaque helpers and
gameplay are not claimed.

## Fresh checks and language domains

The seven pre-install checks pass in **111.736 seconds**. A focused follow-up
restricts global-pointer aliases to four-byte-aligned addresses and passes
in **82.526 seconds**. The seven fresh installed checks, including
those final aligned fixtures, pass in **127.542 seconds**.

* **4,320 guest cases per body** cover eight record graphs, five radius
  widths through 65535, signed center endpoints, exact/outside bounds,
  full-word subtraction/absolute-value wrap and both stack phases.
* **Four aligned read-only aliases** and **47 fired access-prefix cuts**
  compare complete state across all three bodies. Rejected-X paths complete
  with Z and the unfollowed child unmapped. An empty root needs only its
  pointer word. These are guest instruction observations; hardware-MMU or
  arbitrary native alias semantics are not claimed.
* **Nine independent GNU links** exercise both root-pointer HI16/LO16
  carry edges in three text/data layouts, with 96 cases per body.
* Native32 O0/O2/O3 pass **12,960 executions** using typed pointer calls,
  bounded aligned fixtures, UBSan, all word-wrap cases and read-only checks.
  Strict alias optimization is disabled for the recovered flat field views.
  The precomputed expected routes come from the independent graph contract.
* **Six native and eight separately compiled IDO controls** reject exclusive
  bounds, signed radii, unsigned centers/offsets, the wrong coordinate,
  missing leaves and saturated INT_MIN magnitude. The two unsigned-offset
  mutants are guest-only because their wrong pointers can leave a native
  allocation. Every counted control has a fired witness.
* **272 raw-byte, two binding and six whole-image corruptions** fail closed.
  All 64 reachable words are visited. The duplicate loads at +0x74, +0x90
  and +0xE4 and the zero assignment at +0xF8 are unreachable from entry,
  but remain statically exact and corruption-checked.

The fixture corrections rebind instructions when moving the global into
record storage, map original caller store destinations, and keep word aliases
aligned. No production C change was required for those corrections.

All nineteen shared padder, relocation, matcher and data-layout checks pass
in **11.041 seconds**, and `make tools-check` passes. Earlier caller/neighbor
suites are reused through complete code/binding/data identity, not described
as freshly executed. Routine work uses zero Claude calls and the existing
IDO/GNU path under the documented REA MIPS-adapter limitation.

## Production and preserved evidence

The immutable snapshot contains **154 inputs**, including all headers,
target and caller sources/objects, available original assembly, retail ROM,
manifest, Makefile, linker, ELF, code binary, progress and graph. Artifacts
remain in `conker/build/game-spatial-leaf-lookup-1510FD20-match/`.
Main baseline is `ba3a8a5374afc04ad3762b47912221d99ae0e827`; mounted tools
baseline is `cc982da9f6a26c589f6ba3266f754e6a257e838a`. Both start clean.
The sibling tools checkout is untouched; no fresh sibling qualification or
host-port Release change is claimed.

Actual Make's owner and complete ELF equal the independent prediction byte
for byte. All **6,052 function addresses** stay fixed; only this body changes.
All **189,088 protected bytes across 720 owners** remain exact. The literal
full-file prediction accounts for **189 changed ELF bytes**, confined to the
target slot and its 12-to-272 symbol-size change, with **zero metadata
permutations and zero excluded bytes**. All other named definitions agree.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `29ef167bd2d2248907a4a488573cf2c06997ff8a6d93bfad8d402eaeff93b329` |
| Original target | `eaf82f4e2f801cf8feab9483cea652733efba6bb1fb347aeb4e8beb8792e209e` |
| Production owner | `f883822e184ac00b130a888804f9007348a3680050d6f54f219506f7f0276280` |
| Complete ELF | `15b6a6f00f9db774fb5998dcc036398c8f2237bc2a2090a0db6031045a7ba592` |
| Code binary | `91909dc83f5f23b2f8fc3748cdb41169ba8f75854a74d6bff1872949ec513a36` |
| Unchanged guard manifest | `892dcc21c80c8cc41c6970ed89c7f218e072b5a5487946d406a0d133e7f6d6d6` |

Actual Make performs the normal broader rebuild caused by the shared-header
dependency. `make -C conker all` produces the binary and returns 2 only at
the expected incomplete-project retail checksum mismatch. The inherited
duplicate generated_12D630 recipe warning remains unchanged. Source newline
styles and private/frozen inputs are preserved.

## Progress and continuation

The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,175 / 5,512 | 75.74% | 0 | 1,337 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,502 / 4,839 | 72.37% | 0 | 1,337 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. Root README changes aggregate rows
only. The 80% threshold is 4,410, leaving **235 more** exact functions.
Next ordinary candidate is **func_15149EC4**. Retain the eight separate
boundaries from Note 2103: `func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC`, `func_150A6760`,
`func_150A70C0`. Keep the wider 80% goal active.

Mounted tools are committed first as
`e5ccf4a552b3340154786ddfd0b4523f46a286bd`
(`test(game): qualify direct spatial leaf lookup`). The consumer records
that pointer with the direct C, consistent pointer/handle interface and notes.

The ordinary AST-only Graphify update refuses its smaller 24,962-node
replacement, preserving the existing 58,765-node graph. The thirteen-path
scoped refresh retains 58,762 old IDs, replaces three relocated update-log
IDs and adds twelve IDs. Every removed ID has a unique same-label/same-source
replacement; **zero nodes outside changed paths are lost**. The graph is
**58,774 nodes / 112,536 links / 5,098 communities**, SHA-256
`4ebc3ed9b5f383965bb1b8b2273f3247661a843e0bea2ad5af5a6b6f9b4b9f00`.
The 31,816 retained nodes from 3,754 files outside the current scan corpus
are preservation evidence, not fresh full-corpus extraction. No force
overwrite is used. Final receipt paragraphs add no headings; the final
scoped refresh verifies unchanged topology.
