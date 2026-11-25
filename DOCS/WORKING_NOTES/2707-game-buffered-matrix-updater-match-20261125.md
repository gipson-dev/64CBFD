# Buffered matrix updater match - 2026-11-25

`func_151D6E60` replaces its untyped zero-return placeholder in
`conker/src/game/generated_203E20.c`. The complete **104 words / 416 bytes
and 32-byte frame emit directly from semantic C**, with all eight relocation
positions exact. There are **zero guards, insertions, omissions, alignment
words or compiler-profile changes**. VA `0x151D6E60..0x151D7000`;
ROM `0x204310..0x2044B0`.

Production recount: **4,686 / 5,528 (84.77%) total**, **4,013 / 4,855
(82.66%) Game**, Init492/492 and Debugger181/181; zero address drift,
842 still different. **13 more verified matches reach85%.** One new match;
zero additional parent/provider credit. Conversion rows and denominators
remain unchanged.

The recovered interface returns signed32 status1 and accepts one owner
pointer. It calls the float angle provider15144AA8(0), adds25, and calls the
existing rotation-matrix provider150A8050 with angles0/result/0. Destination
is owner+0x7C plus64 times unsigned byteD800BE9C0. It then copies the position
from the owner+0x4C pointer's float fields0x14/0x18/0x1C, adding120 toY, into
the selected matrix translation row, and scales the nine3x3 basis elements.
The selector is reread before every field. Names describe observed matrix
use and partial views; they do not recover the complete original owner type
or assert arbitrary page indices are valid native allocations.

The coefficient is captured once after the matrix helper and before the
first translation store. Its constant is D800AB278, ROM24FD38, raw bits
`0x3F0D0E56` (approximately0.551); its following word is zero. Both words
agree across original rodata, ROM, frozen and live ELF. A first113-word
candidate repeatedly read this potentially aliased global after stores.
The genuine local scale lifetime recovers all104 words, bindings and the
retail S0/RA frame, with no storage tricks, volatile qualifiers or assembly.
Selected owner SHA256 `f25906c599a4f53dee319d946fc10ebe8ddf5f933fbb5583e199c7de1ab1ba1e`.

The actual provider interfaces are `f32(s32)` and
`void(f32[4][4], f32, f32, f32)`. Their complete35-word and83-word originals
are pinned against ROM and their implementations remain unchanged. The
rotation helper has its own handwritten frame/register behavior; this
checkpoint does not convert it or claim its complete runtime qualification.
Opaque providers may mutate the page, source pointer/coordinates, coefficient,
argument homes and FP status under the stated fixtures.

An aligned whole-ROM scan finds one literal target pointer at ROM22F86C,
VA8008ADAC, and no direct J/JAL patterns. This is the measured census, not
proof about every computed indirect call. All64 bytes of the surrounding
callback table at8008AD90 agree across ASM, ROM, frozen and live ELF.
The target is signed selector7 from the first table and selector3 from the
second table. The scalar D8008ADA8 wrapper reads another entry; it is not
misidentified as a direct call to this target.

The actual84-word/frame32 consumer151572D0 is already byte-exact in the
frozen linked ELF. Its two JALR sites15157340/1515737C pass the owner inA0
and test childV0 for zero, confirming the status-return ABI. Complete original
consumer execution passes **1536 cases per stream,1280 connected child calls
per stream**, across original/direct child streams. It exercises both signed
selector bytes, -1 skips, both callbacks together, lifetime expiry/wrapping,
fade paths, provider mutations and all four rounding modes. Each child is
checked against the independent full-memory/frame/FP/provider/return model.
Final parent memory, saved ABI and post-helper observations agree.

The two zero-result branch words15157354/15157390 are unreachable with this
child's authentic return1; both execute under supported negative controls.
For each indexed site, poisoning the child's verified result to zero and
inverting the consumer's zero test complete and reach release rather than
refresh. Post helpers1503F4B0/1516972C remain opaque. Original consumer code
is executed; no new independent semantic recovery or matching credit for
that unchanged parent is claimed.

Guest checks pass **1600 cases per stream across five identical instruction
streams**, executing all104 words. **180 fault-prefix quintuples** preserve
complete modeled memory,32-byte frame, saved ABI, status return, provider
observations, ordered FP operands and modeled FCSR. Coverage includes all256
unsigned selector bytes, source/matrix overlap, selector/coefficient aliases,
caller-stack owner storage and provider mutations. Four complete instruction
controls reject. Arithmetic uses the existing bounded finite FP model;
raw fault-prefix equality applies to emitted code under those providers,
not portable C fault semantics or an N64 hardware/trigonometry proof.

Native32 executes the actual selected body in two translation units against
an independent reference: **2048 cases at each ofO0/O2/O3**, strict aliasing,
UBSan traps, LTO type checks and strict FP flags. Real typed owner/position
arenas use two valid matrix pages. The full284-byte owner arena, two64-byte
position arenas, retained bytes/canaries, pointer fields, globals, return,
provider snapshots and MXCSR agree in all four rounding modes with sticky
flags, including finite/subnormal argument patterns. All **eight wrong C
variants finish and return comparison42**; signals/traps never count.
Arbitrary address aliases and all256 indices belong to the guest fixture.

Both complete owner padders agree and retain all six neighbors, pools and
exports (zero interior retail labels). Actual Make uses three commands,
with no GLOBAL_ASM processing, diagnostics or profile change. The independent
image reference uses frozen old C plus original target ASM. Reference,
actual Make link, literal prediction and production ELF agree: **338 changed
bytes, zero exclusions**. All189088 protected Game data bytes/720 owners,
unrelated bodies/addresses/extents, the entire guard file and conversion
rows are fixed. Symbol/string metadata uses closed byte accounting.
Padded owner SHA256 `37752d86ae5b2ea969df6b9753e5b511d17157bc03d992676c75ca57d6c5f54a`.

Boundary tests expose208 word corruptions and16 binding corruptions, pin
eight relocation positions, and run20 GNU links/100 guest rebases over
address/carry patterns. Oversized generic output visibly overflows; the
generated padder rejects its oversized probe. Neither probe is accepted.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 137.196 s | 5 fresh / 0 reused |
| preinstall-sibling | 108.56 s | 5 fresh / 0 reused |
| installed-primary | 114.821 s | 5 fresh / 0 reused |
| installed-sibling | 112.52 s | 5 fresh / 0 reused |

All20 final tests are fresh. The isolated second copy has
2174 immutable dependency links and nine
independent task copies; freeze 3834 inputs /
2755 copies. Task/import/data/profile/artifact fingerprints
agree across copies, including each Make route's task tools. Shared
tools-check passes. The independently dirty real tools sibling is preserved.

One connected reference correction retains the second callback's actual
incoming FP status from the first call rather than resetting it to rounding
mode alone. The failure affected only its first provider observation; the
complete comparison remains enabled. Native provider seeding indexes the
real inner matrix arrays explicitly. Repeated callback-table/object reads
are cached only while their verified bindings remain identical; all1536
cases and their observations still execute. These fixture changes leave
the selected source/profile unchanged and are covered by the final suites.

Baseline consumer `02ed95e5a25d0a575affa5ea7202214467e6b5cf`.
Tools commit `93f30f34bf3ebd60aec9a9de2677bdbe5c66ce25`.
Production ELF SHA256 `2bb1dbd4141586206876cf520ff96d691f7a422f1872f5022b2c6ad0c1c035e7`.
Receipts: `conker/build/game-buffered-matrix-update-151d6e60-private`.

Read-only sibling applicability finds the known
`64CBFDOGL/recomp_scene/cd64_out/func_151D6E60.c` is an empty generated
stub and that historical directory has no Git root. No active host code was
qualified or transferred; host-applicability.json preserves the evidence.

Routine work uses zero Claude calls and no subagents. Root README receives
aggregate/date rows only. Scoped Graphify retention and actual hook-writer
termination are audited before banking. No host transfer/build/launch,
Release change, hardware/gameplay acceptance or push is claimed.
The85% matching goal remains active.
