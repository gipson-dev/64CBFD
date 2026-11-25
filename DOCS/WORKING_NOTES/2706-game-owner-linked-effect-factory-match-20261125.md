# Owner-linked effect factory match - 2026-11-25

`func_151C6EA0` replaces its untyped zero-return placeholder with a semantic
owner-linked effect constructor in `conker/src/game/generated_1F3780.c`.
The complete **102-word / 408-byte slot and 176-byte frame emit directly
from C**, including all four relocation positions. There are **zero new
guards, insertions, omissions, alignment words or compiler-profile changes**.
VA `0x151C6EA0..0x151C7038`; ROM `0x1F4350..0x1F44E8`.

Production recount: **4,685 / 5,528 (84.75%) total**, **4,012 / 4,855
(82.64%) Game**, Init492/492 and Debugger181/181; zero address drift,
843 still different. **14 more verified matches reach85%.** One new match;
zero parent/provider credit. Conversion rows and denominators are unchanged.

The recovered interface is `void (OwnerEffectSource151C6EA0 *, u8, s32)`.
It reads only owner byte0x3B, forwards the slot's low byte and signed context,
constructs a124-byte descriptor, calls1513264C with resource3, value255,
null extended state and payload size1, and on success copies a separate zero
byte to created+0x170. Names describe observed use, not an asserted original
gameplay meaning or complete original object type. The local owner prefix is
60bytes; no shared header or neighboring ABI was changed.

The natural128-byte workspace contains one initial payload byte and the
four-byte-aligned descriptor at offset4. Its three implicit padding bytes
and the descriptor's seven unwritten bytes remain unwritten. The descriptor
contains117 initialized bytes; holes89/90/91/107/113/118/119 are retained.
Fields include unit scales and extents, four copies of the default vector,
flags0x11900, lifetime300, resource15, constants100/23/5, signed sentinel-1,
the owner pointer and identity, and final16-bit values1/255. No blanket clear
is substituted. Two independent extent assignments retain retail order.

Ordinary separate locals recovered102words/frame176 but35 word differences;
declaration reordering reduced the difference, then the natural workspace
and extent initialization order recovered all words. No dummy reads,
volatile qualifiers, inline assembly, artificial reserve or patched words
are present. Source SHA256
`47ef5cd4e8b7e9f061ebfc9778b769f57b93efbc53b272be3893131fd7da222f`.

The real seven-argument1513264C definition in generated15F680.c and its
complete256-word/frame80 original are pinned and unchanged. Its existing
extended-state pointer type is retained. The SDK `libc/string.h` declaration,
actual SDK memcpy C body and 32-bit unsigned-int size_t are pinned. The
three-word D800A5480 zero vector at ROM249F40 belongs to the592-byte
`assets/249F40.bin.o` data owner; its automatic undefined alias, frozen ELF,
live ELF and ROM agree. No fabricated ASM owner or primary symbol is claimed.

An aligned whole-ROM scan finds no literal target pointers, no direct J and
one JAL at ROM8D73C/VA1506028C. This is the measured direct/literal census,
not proof of absence of arbitrary computed indirect calls. The complete
original1137-word/frame144 parent1505F298 agrees with ROM and remains ASM.
Its actual call supplies ownerS0, slot255 and context1. Its later owner-byte81
load overwrites childV0 before use, supporting the void interface rather
than inheriting the placeholder's false signed return contract.

Bounded connected execution covers the real six-word prologue, call window
15060284..150602A4, common cleanup150603D4..15060448, and separately executed
five-/four-word epilogues at15060448/1506044C. **384 cases per stream across
original/direct streams and96 poisoned-childV0 checks** verify arguments,
full child frame, parent cleanup memory, provider observations and saved ABI
state. Three complete negative controls reject. Optional1505E650/15060A30
helpers are contracted. Earlier dispatch and the preceding sound call are
preconditions; whole-parent runtime and other dispatch cases are unqualified.

Guest qualification passes **848 cases per stream across five identical
instruction streams**, executing all102 words. **268 fault-prefix quintuples**
compare complete memory,176-byte frame, incoming argument homes, saved ABI,
provider observations and incidental machineV0/FCSR. Coverage includes every
slot and identity byte, context classes, source/default/packet/incoming-home
mutations, caller-stack owner aliases, nonfinite/subnormal bit copies, four
rounding modes and opaque provider sticky flags. All six supported complete
instruction controls reject. IncidentalV0 equality is a machine observation;
the recovered C function promises no return value.

Native32 executes the selected body and actual SDK memcpy for valid calls,
with an independent reference/provider in a second translation unit:
**4096 cases at each ofO0/O2/O3**, strict aliasing, UBSan traps, LTO type
errors, four rounding modes and provider stickyMXCSR. It checks all117 defined
descriptor bytes, the complete448-byte post-factory output arena,92-byte
source arena, globals and canaries. Descriptor/payload observations occur
only during their valid lifetime. Native padding values are not assumed.
All **13 wrong C variants complete and return comparison42**; signals and
traps never count. Wrong-width controls detect the mismatch before an invalid
control read. There is no special native FP optimization override.

Both complete owner padders agree, preserving all seven neighbors, exports
(zero interior labels), literal/data pools and current guard manifest. Actual
Make executes five commands, including the owner's three existing GLOBAL_ASM
functions; zero diagnostics and no profile changes. The independent image
reference uses frozen old C plus original target ASM, without recovered C.
Actual Make, independent reference, literal prediction and production ELF
agree with **303 changed bytes and zero exclusions**. All189088 protected
Game data bytes across720 owners, unrelated bodies/addresses/extents, the
entire guard file and conversion rows remain fixed. Symbol/string metadata
uses closed byte accounting. Padded owner SHA256 `085ca49a811f73be8adcd0c558b8b6d3cdce0c7ca13f4a6735923bc8b8c93f29`.

Boundary tests expose204 word corruptions and eight binding corruptions,
pin four relocation positions, and run20 GNU links/100 guest rebases across
address/carry patterns. The oversized generic probe visibly overflows and
the generated padder rejects its oversized probe; neither is accepted.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 143.704 s | 5 fresh / 0 reused |
| preinstall-sibling | 102.769 s | 5 fresh / 0 reused |
| installed-primary | 104.543 s | 5 fresh / 0 reused |
| installed-sibling | 111.689 s | 5 fresh / 0 reused |

All20 final tests are fresh. The isolated second tools copy has
2165 immutable dependency links and nine
independent task copies. Freeze: 3815 inputs /
2735 copies. Import/data/profile/artifact fingerprints
agree across both copies; each actual Make route uses its own task tools.
Shared tools-check passes. Existing unchanged neighbor receipts are reused,
not counted as fresh tests; the measured owner/image audit justifies their
scope. The independently dirty real tools sibling is preserved.

Private fixture corrections are retained in ignored diagnostics: track the
actual bounded epilogue PC rather than a stale interpreter field; use the
target-only empty guard CSV in isolated boundary probes instead of passing
unrelated neighbor guards; provide the independent image helper alias before
executing it; omit the nonexistent normalization-proof import because this
body is direct. None changed the selected body or relaxed a comparison.

Baseline consumer `b3e65b68c9598f1784e570b5f0dc1c6a70e079e0`.
Tools commit `4e630df373a20adb2cf3ec0e7c2c5f36d417799b`.
Production ELF SHA256 `19c636b33663906b3ab37e5bf5f56248c9ebd71774ceca73959dd4796563f3dc`.
Receipts: `conker/build/game-owner-effect-factory-151c6ea0-private`.

Read-only sibling applicability checked the known
`64CBFDOGL/recomp_scene/cd64_out/func_151C6EA0.c`: it is an empty generated
stub, and that historical directory has no Git root. No active host
implementation was qualified or changed; see host-applicability.json.

Routine work uses zero Claude calls and no subagents. Root README receives
aggregate/date rows only. Scoped Graphify retention and actual hook-writer
termination are audited before banking. No host transfer/build/launch,
Release change, hardware/gameplay acceptance or push is claimed.
The85% matching goal remains active.
