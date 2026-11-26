# Axis quad vertex writer direct match - 2026-11-26

`func_150DB2D8` replaces the zero-return placeholder in
`conker/src/game/generated_108320.c` with a typed four-vertex writer.
All **144 words / 576 bytes and all three call relocations emit directly
from C**, with **frame 72 and zero guards**. The first semantic candidate
matches every raw instruction and binding. VA `0x150DB2D8..0x150DB518`, ROM
`0x108788..0x1089C8`. Function and slot extents are identical; there is no
alignment tail, insertion, omission, compiler-profile or Makefile change.
All five raw/padded neighbors, including the previous bouncing-effect update,
and all raw/padded pools are unchanged. The complete guard CSV is unchanged.

Production: **4,693 / 5,528 (84.90%) total**, **4,020 / 4,855 (82.80%) Game**,
Init 492/492, Debugger 181/181, zero drift and 835 still different. One new
match; no additional caller, helper or host credit. **Six more accepted matches
reach 85%.** Conversion rows and denominators remain unchanged.

The recovered ABI is `Vtx *(AxisQuadOwner150DB2D8 *, s16 view)`. The measured
partial owner is 272 bytes. Half extents at 0x2C/0x30, XYZ at 0x34/0x38/0x3C,
and horizontal/depth axis factors at 0x40/0x48 supply the four corners. The
64-byte four-vertex template is at 0xC0 and four native-qualified buffer slots
start at 0x100. `Vtx` is 16 bytes. These descriptive names and the partial view
are inferred from code and observed accesses, not original source names.

`func_151D5D60(owner->buffers, view, 64, &cursor, &fresh)` returns its buffer
through a pointer output. The leaf captures that pointer separately for its
return value. Null returns immediately. A fresh buffer copies the retained
template to both 64-byte pages, reloading the selected buffer pointer after
the first copy. It then computes `horizontal = halfWidth*axisX` and
`depth = -halfWidth*axisZ`, retaining the retail FP operand order. The four
corners use X signs `+,+,-,-`, Y signs `+,-,-,+`, and Z signs `+,+,-,-`.
Each coordinate truncates to signed 32 bits and narrows to its signed-halfword
vertex field. All four flags are zeroed. UV and colour bytes retain their
template or prior contents. The originally captured pointer is returned even
if an opaque provider redirects the live output cursor during copying.

The original frame saves S0 at SP+0x20 and RA at SP+0x24. Freshness is the byte
at SP+0x37, the captured first pointer is SP+0x40, and the live cursor output is
SP+0x44. The signed view is recovered from its incoming home. No dummy local,
physical-register declaration, instruction guard or artificial padding is used.
The existing checked binding for the preceding bouncing-effect function's
three float literals is reused unchanged in this owner; both compiled versions
pass that checker before both complete padders run.

The sole aligned target pointer is ROM `0x22E8F8`, index 7 in the 39-entry
`D_80089E1C` table. No aligned direct J/JAL pattern names the leaf. The table
matches the ROM and frozen ELF; the following graphics word is excluded.
The complete original `func_1513DB00` dispatcher is 295 words / frame 144.
It passes the owner and narrowed signed view at JALR `0x1513DC24`, consumes
the pointer result at `0x1513DC30`, and frees/skips on null. **This production
dispatcher remains a zero-return placeholder.** Its complete retail ASM/ROM
body is qualified here; neither its C restoration nor gameplay integration
is claimed. The existing 52-word buffer helper and 11-word `memcpy` already
match their ROM words in the frozen ELF and receive no new matching credit.

Validation:

- Complete owner compilation and both production padders match. All five
  other functions and pools are fixed. Actual Make replays the existing five
  commands, producing the complete qualified owner with zero diagnostics.
- Guest: 1,008 cases across five literal instruction streams and 558 access
  fault-cut quintuples. Every one of the 144 target words executes. Full
  literal-stream memory, private frame, GPR/FPR, HI/LO, FCSR, access sequence
  and saved ABI state agree. An independent reference compares public memory,
  calls, ordered FP operations, FCSR and pointer return; independent reference
  private-stack identity is not claimed. Cases cover signed view boundaries,
  null/fresh paths, template retention, live buffer/cursor changes, return-home
  redirects, bounded aliases and four rounding modes. The actual original
  52-word buffer helper and 11-word copy routine also execute together and
  separately; allocation is opaque. Private guest home/alias probes are not
  portable C claims, and the finite FP model is not an N64 hardware claim.
- Native: actual recovered C, separate typed pointer-output/copy providers
  and an independent reference in three TUs. All 8,192 cases pass at O0/O2/O3
  with strict aliasing/FP, UBSan traps and LTO ABI checks. Typed owner/vertices,
  two buffers, canaries, provider metadata, cursor redirection, returned pointer
  and MXCSR agree. Four rounding modes execute. Negative signed views use only
  the null path, and all float-to-s32 conversions stay in range. Seven controls
  complete with comparison exit 42; no compiler error, trap or signal counts
  as a semantic rejection. The return control retains use of the captured
  pointer; an initially unused-variable control was rejected by the harness.
- Caller: both full retail literal streams complete 306 cases with 144
  connected child calls each, including two visibility/free paths and signed
  view forwarding. All 293 reachable parent words execute; only duplicate
  default words 115/146 are unreachable. An independent semantic leaf-provider
  counterpart agrees on public state, calls, FP state and final return; its
  private stack is not equated. Hiding or inventing a returned buffer changes
  the complete parent's behavior. Render services and free remain opaque.
- Both scoped padders expose all 288 word corruptions and six binding
  corruptions. Twenty GNU links and 100 guest rebases independently move both
  helper addresses. Generic oversize remains visible; generated oversize
  rejects. The zero-guard manifest and absent alignment tail are pinned.
- Independent frozen-old-C plus original-ASM prediction equals the full
  private and production ELF: exactly 401 changed bytes, zero exclusions.
  All 189,088 protected Game-data bytes across 720 owners remain unchanged.
  Production ELF SHA-256: `5ecc07a84ab0262877f90b73f56eb56e1e971fa0985e465532db06dfef0c25e5`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 263.303 s | 5 fresh / 0 reused |
| preinstall-sibling | 212.502 s | 5 fresh / 0 reused |
| installed-primary | 189.384 s | 5 fresh / 0 reused |
| installed-sibling | 232.026 s | 5 fresh / 0 reused |

All 20 packaged target tests are fresh with matching source, import, data and
task fingerprints across the primary and isolated sibling tools copies.
Shared tools-check passes; unchanged broad suites are not reported as fresh.
Frozen inputs: 3927; snapshot entries:
2859. The isolated sibling uses
2243 immutable dependency links and nine
independent task copies, preserving the independently dirty real sibling.

Baseline consumer `98f71d299a72b594b8ccc0e982add6afc26f6827`.
Tools commit `e059d3ca826164e0256acf4ff365fbdd3a5a6e15`.
Receipts: `conker/build/game-axis-quad-vertices-150db2d8-private`.
The historical generated host target is an empty stub; active host applicability
is unqualified. No host transfer/build/launch, Release change, push, hardware
or gameplay acceptance. Zero Claude calls and no subagents for this function.
Scoped Graphify refresh audits all six owner definitions, retains old IDs and
qualification metadata, and observes actual commit-hook termination before
publication. README receives aggregate/date rows only. The 85% goal is active.
