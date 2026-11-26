# Attached effect transition descriptors - 2026-11-26

`func_150DB9E0` replaces its zero-return placeholder in
`conker/src/game/generated_108E90.c` with a semantic two-stage effect handler.
**160 words / 640 bytes and all 25 binding positions, frame 208, match after
seven checked guards; 153 words emit directly from C.** Function and slot
extents are identical: VA `0x150DB9E0..0x150DBC60`, ROM
`0x108E90..0x109110`. No insertion, omission, alignment tail, compiler-profile
or Makefile change. All eleven raw/padded neighbors and pools stay fixed.

Production: **4,695 / 5,528 (84.93%) total**, **4,022 / 4,855 (82.84%) Game**,
Init 492/492, Debugger 181/181, zero drift, 833 still different.
**Four more accepted matches reach 85%.** One new match; conversion rows and
denominators are unchanged. Caller, helper and host credit remain unchanged.

The recovered interface is `void (struct127 *actor, s32 transition, u8 channel)`.
Null actors and transitions outside 0/1 do nothing. Transition 1 selects
attachment preset 2 through `func_15196438(actor, 2, channel, 0)`.
Transition 0 selects preset 1, prepares the 88-byte oriented input at SP+0x78,
submits it with `func_15152F70`, requests a record with
`func_151491F4(30, -1, 0, 1, 0, 0, channel, 0)`, then prepares the 64-byte
short input at SP+0x38 and calls `func_15153298(input, channel, 1)`.
Returned helper pointers are ignored. The existing oriented input definition
is moved before this new function; eleven other function bodies stay fixed.
The short input reproduces the existing emitter's measured field layout.
Descriptive names are inferred; uncertain fields retain offset-based names.

Oriented XYZ and one range/base field come from `D_800A0C00..0x800A0C0C`.
The input retains dimensions 3/3, speed 9/8, count 8/8, angle pairs
(-75,22)/(-38,35), remaining shorts (3,2,41,0), fixed bytes (10,40),
six words (1,0,0,0,0,0), and final bytes (255,255). The short input reads XYZ
from `D_800A0C10/14/18` and speed fields from `D_800A0C1C/20` after the
record request. Its count is (6,3), angle pairs (-74,21)/(-38,35), magnitude
(14,14), another pair (-61,28), fixed bytes (-1,18), shorts
(6,6,0,174,115,115,135), resource/address word `D_80090514`, and final bytes
(255,255). Unwritten bytes 0x3A/0x3B and 0x56/0x57 in the oriented input,
and 0x3E/0x3F in the short input, remain untouched and are not initialized
artificially. Native providers observe only the initialized input bytes.

The original 208-byte frame saves S0/RA at SP+0x28/0x2C. Incoming channel
home SP+0xD8 is retained; S0 captures its low byte across all calls. Two raw
MOVEs become retail ANDI-255 words. A structural check proves S0 was already
zero-extended and cannot change before either use. A single LUI address
initializer moves across four independent integer-immediate loads. Its HI16
binding moves with it; LO16 and every memory/FP transfer retain their original
order. The complete normalized words and symbolic bindings equal the retail
ASM. All seven rows are expected-word guarded; the old CSV prefix is fixed.
Completed and memory-access fault-cut private states agree. Asynchronous
instruction-interrupt identity is not claimed.

The actual caller is the event-0x35 arm of `func_150265CC`. Its complete
original 3,451-word ASM is pinned to ROM; its frame is 0x750. A bounded,
complete 13-word window `0x15029750..0x15029784` loads the actor from
SP+0x764, reads the signed command byte, clamps values >=2 to transition 1,
and loads the channel as an unsigned byte from SP+0x773 in the JAL delay slot.
After the child returns it branches to `0x15029BA4`, unconditionally assigning
its own V0=1 in that delay slot. The leaf's V0 is ignored. The alternate exit
is `0x15029784`. This is a qualified producer/consumer window; **complete
parent execution and parent production matching are not claimed**.

The existing 196-word attachment helper and 202/231-word oriented/short
emitters match their original ROM in the frozen ELF. Their layouts and
interfaces are reused, with no additional matching credit. The record factory's
existing signed/unsigned eight-word parameter ABI is retained; its returned
pointer is unused here. These services remain opaque in this target's tests.
Static helper pins are separate from new dynamic helper execution claims.

Validation:

- Both complete padders produce the same owner and preserve eleven neighbors
  and all pools. The actual three-command Make recipe emits the identical
  owner with zero diagnostics and no ASM-processing or profile change.
- Guest: 640 cases across five streams, every one of the 160 target words,
  and 163 access-cut quintuples. Raw and literal full memory/private frame,
  GPR/FPR, HI/LO, FCSR and ordered access traces agree. An independent reference
  checks public memory, call order, initialized input bytes and FCSR. The void
  return register is not independently equated. Cases include null actors,
  invalid/signed transition bounds, high incoming channel words, helper/global
  mutations, incoming-home overwrites and stack alignment. Distinct mutation
  values at successive calls expose stale/early scalar reads. Private guest
  home probes are not portable-C claims. All nine scalar bindings are pinned
  independently to ROM/frozen ELF.
- Native: actual selected C, separately compiled typed providers and an
  independent reference in three TUs. All 4,096 cases pass at O0/O2/O3 under
  strict aliasing/FP, UBSan traps and LTO type checks. Public arenas, canaries,
  call metadata, initialized record bytes, scalar bits and MXCSR agree. Tests
  transfer signed zero, infinities, quiet/signaling NaN bits, use all four
  rounding modes and retain pre-existing MXCSR flags. There is no FP arithmetic
  in this leaf. Eight controls complete with comparison exit 42, including an
  early scalar read across a mutating helper call. No error/trap/signal counts
  as a semantic rejection. Provider-local record addresses are normalized by
  their measured roles, without claiming independent private-stack identity.
- Caller: 576 complete bounded-window cases per original/raw stream, with
  288 connected children each. All thirteen caller words execute. Original/raw
  private states agree; a separate semantic leaf-provider counterpart agrees
  publicly. Three deliberately poisoned child return values still give caller
  result 1. Wrong command clamping and wrong return consumption are rejected.
- Both scoped padders reject fourteen guarded-word and two guarded-binding
  corruptions, exposing 306 unguarded-word and 48 other binding corruptions.
  Twenty GNU links and 100 guest rebases exercise jump regions and independent
  scalar/address HI/LO carry seams. Both reject oversize input.
- Independent frozen-old-C plus original-ASM prediction equals the complete
  private and production ELF: **786 changed bytes, zero exclusions**.
  All 189,088 protected Game-data bytes across 720 owners remain unchanged.
  ELF SHA-256: `276ab6282eb44fc379e5024cc5c534b02ce38f5eaa15cc3d181eb335d9995ad1`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 122.379 s | 5 fresh / 0 reused |
| preinstall-sibling | 116.955 s | 5 fresh / 0 reused |
| installed-primary | 96.966 s | 5 fresh / 0 reused |
| installed-sibling | 113.014 s | 5 fresh / 0 reused |

All 20 packaged target tests are fresh across primary and isolated sibling
copies, with matching task/import/data/source fingerprints. Shared tools-check
passes; unchanged broad suites are not reported fresh. Frozen inputs:
3947; snapshots: 2879. The independently
dirty real sibling is preserved. Baseline consumer:
`582357c5461124236b831bd5da7905bb93939b65`. Tools commit:
`6e4f3e3d7f998741d3f0029f177769c25c22bbeb`. Receipts:
`conker/build/game-effect-transition-150db9e0-private`.

No Claude calls or subagents for this routine. The historical generated host
target is an empty stub; active host applicability remains unqualified.
No source transfer, host build/launch, Release change, push or gameplay/hardware
acceptance. Scoped Graphify refresh audits all twelve owner definitions,
retains old IDs/qualification metadata and waits for actual commit-hook
termination. README receives aggregate/date rows only. Goal 85% stays active.
